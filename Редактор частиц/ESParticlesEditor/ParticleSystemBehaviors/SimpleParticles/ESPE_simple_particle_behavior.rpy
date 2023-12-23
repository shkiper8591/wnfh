init python:
    import random
    import builtins
    import math

    class ESPESimpleParticle(renpy.object.Object):
        def __init__(self, displayable, speed, speed_extra, accelerate, lifetime, appear_delay, manager, psystem):
            self.displayable = displayable
            self.manager = manager
            self.psystem = psystem

            self.sprite = manager.create(displayable)

            ##[
            self.x = 960
            self.y = 540

            self.x_speed = speed[0]
            self.y_speed = speed[1]
            self.x_acceleration = accelerate[0]
            self.y_acceleration = accelerate[1]
            ####[
            self.x_extra = 0
            self.y_extra = 0

            self.extra_move_phase = 0
            self.radius_x_extra = 0.0
            self.radius_y_extra = 0.0

            self.speed_extra = speed_extra

            self.last_x_offset = 0
            self.last_y_offset = 0
            ####]
            ##]

            self.lifetime = lifetime
            self.cur_lifetime = 0.0

            self.appear_delay = appear_delay
            self.cur_appear_delay = 0.0

            self.active = False

            self.hide_child()

        def hide_child(self):
            self.y = config.screen_height + 10

        def set_child(self, displ):
            self.sprite.set_child(displ)

        def destroy(self):
            self.sprite.destroy()

        @property
        def x(self):
            return self.sprite.x
        
        @x.setter
        def x(self, value):
            self.sprite.x = value

        @property
        def y(self):
            return self.sprite.y
        
        @y.setter
        def y(self, value):
            self.sprite.y = value

    class ESPESimpleParticles(renpy.object.Object):
        def __init__(self, displayable_list, manager, amount, lifetime=1.0):
            self.displayable_list = displayable_list
            self.displayable_list_length = len(displayable_list)

            self.amount = amount

            #*Зона появления.*#
            ##[
            self.dot_emitter_pos = (960, 540)

            self.rectangle_emitter_pos = (960, 540)
            self.rectangle_spawn_area = (100, 100)

            self.radial_emitter_pos = (960, 540)
            self.emitter_radius = 50

            self.out_of_bounds_spawn_dict = {"Left": False, "Right": False, "Top": True, "Bottom": False}
            self.current_sides = ["Top"]

            self.positioning_func = self.dot_emitter
            ##]

            #*Движение.*#
            ##[
            self.move_func = self.simple_move
            self.move_prop_changer_func = self.move_prop_static_changer

            self.max_x_speed = 0.0
            self.min_x_speed = 0.0
            self.max_y_speed = 250.0
            self.min_y_speed = 250.0

            self.max_x_accelerate = 0.0
            self.min_x_accelerate = 0.0
            self.max_y_accelerate = 0.0
            self.min_y_accelerate = 0.0

                #*Дополнительное движение.*#
            ####[
            self.move_extra_func = None
            self.move_extra_prop_changer_func = None
            self.move_extra_speed_changer_func = self.extra_move_speed_static
            self.move_extra_radius_changer_func = self.extra_move_radius_static
            self.move_extra_phase_changer_func = self.extra_move_phase_static

            self.max_speed_oscillatory = 200.0
            self.min_speed_oscillatory = 200.0

            self.extra_move_phase = 0.0
            self.angle_value = 0

            self.max_x_oscillatory = 0.0
            self.min_x_oscillatory = 0.0
            self.max_y_oscillatory = 0.0
            self.min_y_oscillatory = 0.0
            ####]
            ##]

            #*Время жизни.*#
            ##[
            self.lifetime = lifetime
            self.lifetime_random_enable = False
            self.lifetime_random = 0.0
            self.lifetime_spread = 0.2
            self.lifetime_spread_random_enable = False
            self.lifetime_spread_random = 0.0
            ##]

            #*Взрывчатость.*#
            ##[
            self.is_explosiveness = False
            self.explosiveness_factor = 0.0
            self.explosiveness_amount = 0
            ##]

            self.is_screen_bounded = False

            #*Свойства вызова функции отрисовки.*#
            ##[
            self.inner_frame_check = True
            self.st = 0.0
            self.old_st = 0.0
            self.frame_dtime = 0.0
            self.fixed_dtime = 0.016
            self.update_time = 0.0
            self.dtime_func = self.get_delta_frame_time
            ##]

            self.manager = manager

            self.omath = espe_ov

            ##[
            self.particle_processing_dict = {"move_func": self.move_func}
            self.particle_processing_changer_dict = {"move_func_changer": self.move_prop_changer_func}
            self.particle_processing = self.particle_processing_dict.values()
            self.particle_processing_changer = self.particle_processing_changer_dict.values()
            ##]

            self.active_particles = []
            self.inactive_particles = [ESPESimpleParticle(random.choice(displayable_list),
                                                            [self.max_x_speed, self.max_y_speed],
                                                            self.max_speed_oscillatory,
                                                            [self.max_x_accelerate, self.max_y_accelerate],
                                                            lifetime,
                                                            i * self.lifetime_spread,
                                                            manager,
                                                            self
                                                            )
                                                            for i in range(amount)]

        def particles_process(self, st): #Основа для генерации кода.
            self.frame_dtime = self.dtime_func(st)
            self.st = st

            for particle in reversed(self.active_particles):
                if self.dead_or_alive(particle):
                    for process in self.particle_processing:
                        process(particle)
                else:
                    self.from_active_to_inactive(particle)

            if self.is_explosiveness:
                if self.explosiveness_func():
                    for particle in reversed(self.inactive_particles):
                        self.reset_or_wait(particle)
                        if particle.active:
                            self.from_inactive_to_active(particle)
            else:
                for particle in reversed(self.inactive_particles):
                    self.reset_or_wait(particle)
                    if particle.active:
                        self.from_inactive_to_active(particle)
        
        def lifetime_behavior(self, particle): #Основа для генерации кода (первое условие. Иначе нет смысла генерировать метод).
            if espe_editor_data.p_lifetime_random_enable:
                lifetime_difference = espe_editor_data.p_lifetime * espe_editor_data.p_lifetime_random
                particle.lifetime = random.uniform(espe_editor_data.p_lifetime - lifetime_difference, espe_editor_data.p_lifetime)
            else:
                particle.lifetime = espe_editor_data.p_lifetime

        def from_inactive_to_active(self, particle): #Основа для генерации кода.
            self.inactive_particles.remove(particle)
            self.active_particles.append(particle)

        def from_active_to_inactive(self, particle): #Основа для генерации кода.
            self.active_particles.remove(particle)
            self.inactive_particles.append(particle)

        def dead_or_alive(self, particle):
            particle.cur_lifetime += self.frame_dtime

            if particle.cur_lifetime > particle.lifetime:
                particle.hide_child()
                particle.active = False
                return False
            
            if particle.psystem.is_screen_bounded:
                if -110 > particle.x < 1990 or -110 > particle.y < 1100:
                    particle.hide_child()
                    particle.active = False
                    return False
            
            return True

        def reset_or_wait(self, particle): #Основа для генерации кода.
            particle.cur_appear_delay += self.frame_dtime
            if particle.cur_appear_delay >= particle.appear_delay:
                self.reset_particle(particle)

        def reset_particle(self, particle): #Основа для генерации кода.
            self.lifetime_behavior(particle)
            self.choice_sprite(particle)
            particle.x, particle.y = self.positioning_func()

            particle.cur_lifetime = 0.0
            particle.active = True

            for process_prop_changer in self.particle_processing_changer:
                process_prop_changer(particle)

        def get_delta_frame_time(self, st): #Основа для генерации кода.
            dtime = st - self.old_st
            self.old_st = st
            return dtime

        def get_fixed_delta_time(self, st): #Основа для генерации кода.
            self.old_st = st #Только для редактора.
            return self.fixed_dtime
        
        def reduce_amount(self, cur_length):
            delete_amount = cur_length - self.amount
    
            for i in range(delete_amount):
                if self.active_particles:
                    particle = self.active_particles.pop(0)
                    particle.destroy()
                    continue
                if self.inactive_particles:
                    particle = self.inactive_particles.pop(0)
                    particle.destroy()
        
        def increase_amount(self, cur_length):
            new_amount = self.amount - cur_length
            for i in range(new_amount):
                particle = ESPESimpleParticle(random.choice(self.displayable_list),
                                                [self.max_x_speed, self.max_y_speed],
                                                self.max_speed_oscillatory,
                                                [self.max_x_accelerate, self.max_y_accelerate],
                                                self.lifetime,
                                                i * (self.lifetime_spread),
                                                self.manager,
                                                self
                                                )
                self.inactive_particles.append(particle)
            
        def choice_sprite(self, particle): #Основа для генерации кода.
            particle.displayable = renpy.random.choice(self.displayable_list)
            particle.set_child(particle.displayable)

        ##[
        def explosiveness_func(self): #Основа для генерации кода.
            if len(self.inactive_particles) < self.explosiveness_amount:
                return False
            return True
        ##]

        ##[
        def dot_emitter(self): #Основа для генерации кода.
            return self.dot_emitter_pos

        def rectangle_emitter(self): #Основа для генерации кода.
            x_border = self.rectangle_spawn_area[0] >> 1 ##Сдвиг на 1 бит вправо == деление на 2.
            y_border = self.rectangle_spawn_area[1] >> 1 ##Однако, я не уверен, что это даст скорость, но по идее должно.
            x = self.rectangle_emitter_pos[0] + renpy.random.randint(-x_border, x_border + 1)
            y = self.rectangle_emitter_pos[1] + renpy.random.randint(-y_border, y_border + 1)

            return x, y

        def radial_emitter(self): #Основа для генерации кода.
            radius = float(renpy.random.randint(0, self.emitter_radius))
            angle = renpy.random.randint(0, self.omath.trigonometric_len - 1)
            x = self.radial_emitter_pos[0] + int(radius * self.omath.ocos_angle_d(angle))
            y = self.radial_emitter_pos[1] + int(radius * self.omath.osin_angle_d(angle))

            return x, y
        
        def screen_emitter(self): #Основа для генерации кода.
            x = renpy.random.randint(0, config.screen_width)
            y = renpy.random.randint(0, config.screen_height)

            return x, y
        
        def sides_emitter(self): #Основа для генерации кода.
            side = renpy.random.choice(self.current_sides)

            ##Неприятно? Зато быстрее чем каждый раз словарь генерировать для каждой частицы.##
            if side == "Left":
                return (-120, renpy.random.randint(0, config.screen_height))
            if side == "Right":
                return (config.screen_width + 120, renpy.random.randint(0, config.screen_height))
            if side == "Top":
                return (renpy.random.randint(0, config.screen_width), -120)
            if side == "Bottom":
                return (renpy.random.randint(0, config.screen_width), config.screen_height + 120)
        ##]

        ##[
        def static_move(self, particle): #Основа для генерации кода.
            return True
        
        def simple_move(self, particle): #Основа для генерации кода.
            dx = particle.x_speed * self.frame_dtime
            dy = particle.y_speed * self.frame_dtime

            particle.x += dx
            particle.y += dy

            return True

        def accelerate_move(self, particle): #Основа для генерации кода.
            particle.x_speed += particle.x_acceleration
            particle.y_speed += particle.y_acceleration

            dx = particle.x_speed * self.frame_dtime
            dy = particle.y_speed * self.frame_dtime

            particle.x += dx
            particle.y += dy

            return True

        def move_prop_static_changer(self, particle): ##ТОЛЬКО ДЛЯ РЕДАКТОРА.
            particle.x_speed = self.max_x_speed
            particle.y_speed = self.max_y_speed

            particle.x_acceleration = self.max_x_accelerate
            particle.y_acceleration = self.max_y_accelerate

        def speed_changer(self, particle): #Основа для генерации кода.
            particle.x_speed = renpy.random.uniform(self.min_x_speed, self.max_x_speed)
            particle.y_speed = renpy.random.uniform(self.min_y_speed, self.max_y_speed)

        def static_accelerate_changer(self, particle): #Основа для генерации кода.
            particle.x_speed = renpy.random.uniform(self.min_x_speed, self.max_x_speed)
            particle.y_speed = renpy.random.uniform(self.min_y_speed, self.max_y_speed)

            particle.x_acceleration = self.max_x_accelerate
            particle.y_acceleration = self.max_y_accelerate
        
        def accelerate_changer(self, particle): #Основа для генерации кода.
            particle.x_speed = self.max_x_speed
            particle.y_speed = self.max_y_speed
            
            particle.x_acceleration = renpy.random.uniform(self.min_x_accelerate, self.max_x_accelerate)
            particle.y_acceleration = renpy.random.uniform(self.min_y_accelerate, self.max_y_accelerate)
        
        def speed_acc_changer(self, particle): #Основа для генерации кода.
            particle.x_speed = renpy.random.uniform(self.min_x_speed, self.max_x_speed)
            particle.y_speed = renpy.random.uniform(self.min_y_speed, self.max_y_speed)

            particle.x_acceleration = renpy.random.uniform(self.min_x_accelerate, self.max_x_accelerate)
            particle.y_acceleration = renpy.random.uniform(self.min_y_accelerate, self.max_y_accelerate)

        ####[ 
        def extra_move_oscillatory(self, particle): #Основа для генерации кода.
            angle = int(particle.extra_move_phase + self.st * particle.speed_extra) % 360
            dx = particle.radius_x_extra * self.omath.ocos_angle_d(angle)
            dy = particle.radius_y_extra * self.omath.osin_angle_d(angle)

            particle.x += dx - particle.last_x_offset
            particle.y += dy - particle.last_y_offset

            particle.last_x_offset = dx
            particle.last_y_offset = dy

        def extra_move_prop_changer_oscillatory_zip(self, particle): #Основа для генерации кода.
            self.move_extra_speed_changer_func(particle)
            self.move_extra_radius_changer_func(particle)
            self.move_extra_phase_changer_func(particle)

        def extra_move_speed_static(self, particle): #Основа для генерации кода.
            particle.speed_extra = self.max_speed_oscillatory
        
        def extra_move_radius_static(self, particle): #Основа для генерации кода.
            particle.radius_x_extra = self.max_x_oscillatory
            particle.radius_y_extra = self.max_y_oscillatory

        def extra_move_phase_static(self, particle): #Основа для генерации кода.
            particle.extra_move_phase = self.extra_move_phase

        def extra_move_speed_changer(self, particle): #Основа для генерации кода.
            particle.speed_extra = renpy.random.uniform(self.min_speed_oscillatory, self.max_speed_oscillatory)

        def extra_move_radius_changer(self, particle): #Основа для генерации кода.
            particle.radius_x_extra = renpy.random.uniform(self.min_x_oscillatory, self.max_x_oscillatory)
            particle.radius_y_extra = renpy.random.uniform(self.min_y_oscillatory, self.max_y_oscillatory)

        def extra_move_phase_changer(self, particle): #Основа для генерации кода.
            particle.extra_move_phase = renpy.random.uniform(0.0, 360.0)
        ####]
        ##]

    def espe_psystem_simple_update(st):
        ESPE_simple_particles.particles_process(st)

        espe_editor_psystem_amount_updater() #ТОЛЬКО ДЛЯ РЕДАКТОРА.

        return ESPE_simple_particles.update_time
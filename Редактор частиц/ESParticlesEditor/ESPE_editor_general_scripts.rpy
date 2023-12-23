init python:
    import builtins

    def espe_get_property_check(property):
        if property:
            return "☑"
        return "☐"

    def espe_get_property_radiobutton(property, your_value):
        if property == your_value:
            return "◉"
        return "◎"

    def espe_sprite_in_selected(sprite_name, sprite_list):
        for spr_data in sprite_list:
            if sprite_name == spr_data[0]:
                return True
        return False

    def espe_sprite_left_right_arrow(string, to_right):
        if to_right:
            return string + " »»"
        return "«« " + string

    def espe_sprite_selecting(sprite_name, sprite_list):
        if espe_sprite_in_selected(sprite_name, sprite_list):
            return "{u}" + sprite_name + "{/u}"
        return sprite_name

    def espe_set_sprite_list(editor_data, sprite_list):
        sprite_dict = dict(sprite_list)

        sprite_sources = list(sprite_dict.values())
        sprite_names = list(sprite_dict.keys())

        editor_data.psystem_object.displayable_list = sprite_sources
        editor_data.p_displayable_list = sprite_sources
        editor_data.p_displayable_names = sprite_names

        editor_data.psystem_object.displayable_list = sprite_sources
        editor_data.psystem_object.displayable_list_length = len(sprite_sources)

    def espe_get_displayable_size(displ):
        displ_object = renpy.displayable(displ)
        w, h = renpy.render(displ_object, config.screen_width, config.screen_height, 0, 0).get_size()
        return (w, h)

    def espe_show_particles():
        ToggleScreen(espe_editor_data.psystem_screen)()
        store.espe_particles_show = not store.espe_particles_show
    
    def espe_enable_position_picker():
        ToggleScreen("ESPE_position_picker")()
        store.espe_position_picker_enable = not store.espe_position_picker_enable

    def espe_enable_fps_counter():
        ToggleScreen("ESPE_performance")()
        store.espe_fps_counter_enable = not store.espe_fps_counter_enable

    def espe_update_value(object_to_update, field, value):
        setattr(object_to_update, field, value)

    def espe_editor_psystem_force_update():
        active_particles_len = len(espe_editor_data.psystem_object.active_particles)
        inactive_particles_len = len(espe_editor_data.psystem_object.inactive_particles)
        reseted_particles = []
        ind = 0

        for _ in range(active_particles_len):
            particle = espe_editor_data.psystem_object.active_particles.pop(0)
            particle.hide_child()
            espe_editor_psystem_lifetime_behavior_updater(particle)
            espe_psystem_lifetime_spread_behavior_updater(particle, ind)
            particle.active = False
            reseted_particles.append(particle)
            ind += 1
        
        for _ in range(inactive_particles_len):
            particle = espe_editor_data.psystem_object.inactive_particles.pop(0)
            particle.hide_child()
            espe_editor_psystem_lifetime_behavior_updater(particle)
            espe_psystem_lifetime_spread_behavior_updater(particle, ind)
            reseted_particles.append(particle)
            ind += 1
        
        espe_editor_data.psystem_object.inactive_particles = reseted_particles
    
    def espe_editor_psystem_deep_reset():
        active_particles_len = len(espe_editor_data.psystem_object.active_particles)
        inactive_particles_len = len(espe_editor_data.psystem_object.inactive_particles)

        for _ in range(active_particles_len):
            particle = espe_editor_data.psystem_object.active_particles.pop(0)
            particle.destroy()
        
        for _ in range(inactive_particles_len):
            particle = espe_editor_data.psystem_object.inactive_particles.pop(0)
            particle.destroy()

        espe_editor_data.psystem_object.increase_amount(0)


    def espe_psystem_lifetime_spread_randomizer(particle):
        appear_delay = espe_editor_data.psystem_object.lifetime_spread

        appear_delay_difference = appear_delay * espe_editor_data.p_lifetime_spread_random
        particle.appear_delay = random.uniform(appear_delay - appear_delay_difference, appear_delay)

    def espe_editor_psystem_lifetime_behavior_updater(particle):
        if espe_editor_data.p_lifetime_random_enable:
            lifetime_difference = espe_editor_data.p_lifetime * espe_editor_data.p_lifetime_random
            particle.lifetime = random.uniform(espe_editor_data.p_lifetime - lifetime_difference, espe_editor_data.p_lifetime)
        else:
            particle.lifetime = espe_editor_data.p_lifetime
    
    def espe_psystem_lifetime_spread_behavior_updater(particle, ind):
        appear_delay = espe_editor_data.p_lifetime_spread

        if espe_editor_data.p_lifetime_random_spread_enable:
            appear_delay_difference = appear_delay * espe_editor_data.p_lifetime_spread_random
            particle.appear_delay = random.uniform(appear_delay - appear_delay_difference, appear_delay)
        else:
            particle.appear_delay = ind * espe_editor_data.p_lifetime_spread
        
        particle.cur_appear_delay = 0.0

    def espe_editor_psystem_lifetime_spread_update():
        lifetime_spread = espe_editor_data.p_lifetime_spread
        particles_array = []
        ind = 0

        for _ in range(len(espe_editor_data.psystem_object.active_particles)):
            particle = espe_editor_data.psystem_object.active_particles.pop(0)
            particle.set_child(Transform(particle.displayable, alpha=0.0))
            particle.appear_delay = ind * lifetime_spread
            particle.cur_appear_delay = 0.0
            particle.active = False
            particles_array.append(particle)
            ind += 1
        for _ in range(len(espe_editor_data.psystem_object.inactive_particles)):
            particle = espe_editor_data.psystem_object.inactive_particles.pop(0)
            particle.set_child(Transform(particle.displayable, alpha=0.0))
            particle.appear_delay = ind * lifetime_spread
            particle.cur_appear_delay = 0.0
            particles_array.append(particle)
            ind += 1
        espe_editor_data.psystem_object.inactive_particles = particles_array

    def espe_editor_psystem_amount_updater():
        cur_len = len(espe_editor_data.psystem_object.active_particles) + len(espe_editor_data.psystem_object.inactive_particles)
        if cur_len < espe_editor_data.p_amount:
            espe_editor_data.psystem_object.increase_amount(cur_len)
        elif cur_len > espe_editor_data.p_amount:
            espe_editor_data.psystem_object.reduce_amount(cur_len)

    def espe_set_explosiveness():
        explosiveness_factor = espe_editor_data.p_explosiveness_factor
        explosiveness_amount = int(float(espe_editor_data.p_amount) * explosiveness_factor)
        espe_editor_data.p_explosiveness_amount = explosiveness_amount
        espe_editor_data.psystem_object.explosiveness_factor = explosiveness_factor
        espe_editor_data.psystem_object.explosiveness_amount = explosiveness_amount

    def espe_setattr_safe(field, object_to_update=None, attr_to_update=None, field_type=str):
        if object_to_update is not None and attr_to_update is not None:
            setattr(object_to_update, attr_to_update, field_type(getattr(espe_editor_data, field)))

    def espe_init_editor_psystem_complex():
        displayable_list = espe_editor_data.p_displayable_list
        manager = ESPE_complex_particles_manager
        amount = espe_editor_data.p_amount
        max_alpha = espe_editor_data.p_intermediate_max_alpha
        min_alpha = espe_editor_data.p_intermediate_min_alpha
        max_zoom = espe_editor_data.p_intermediate_max_zoom
        min_zoom = espe_editor_data.p_intermediate_min_zoom
        max_angle = espe_editor_data.p_max_angle
        min_angle = espe_editor_data.p_min_angle

        return ESPEComplexParticles(displayable_list, manager, amount, max_alpha, min_alpha, max_zoom, min_zoom, max_angle, min_angle)

    def espe_init_editor_psystem_simple():
        displayable_list = espe_editor_data.p_displayable_list
        manager = ESPE_simple_particles_manager
        amount = espe_editor_data.p_amount

        return ESPESimpleParticles(displayable_list, manager, amount)

    def espe_set_complex_particle_system():
        espe_editor_data.psystem_type = "Сложная"
        espe_editor_data.psystem_name = "Сложная система!"

        espe_editor_data.psystem_manager = ESPE_complex_particles_manager
        espe_editor_data.psystem_screen = "ESPE_editor_complex_particles_show"

        espe_editor_data.psystem_object = ESPE_complex_particles

    def espe_set_simple_particle_system():
        espe_editor_data.psystem_type = "Простая"
        espe_editor_data.psystem_name = "Простая система!"

        espe_editor_data.psystem_manager = ESPE_simple_particles_manager
        espe_editor_data.psystem_screen = "ESPE_editor_simple_particles_show"

        espe_editor_data.psystem_object = ESPE_simple_particles
    
    ##.*НЕ РАБОТАЕТ :(*.##
    ##[
    def espe_update_anchor():
        psystem = espe_editor_data.psystem_object

        psystem.particle_anchor = espe_editor_data.p_anchor
    ##]

    ##[
    def espe_update_dot_emitter_pos():
        espe_editor_data.psystem_object.dot_emitter_pos = espe_editor_data.p_emitter_pos

    def espe_update_rectangle_emitter_pos():
        espe_editor_data.psystem_object.rectangle_emitter_pos = espe_editor_data.p_rectangle_emitter_pos

    def espe_update_rectangle_spawn_area():
        espe_editor_data.psystem_object.rectangle_spawn_area = espe_editor_data.p_rectangle_spawn_area

    def espe_update_radial_emitter_pos():
        espe_editor_data.psystem_object.radial_emitter_pos = espe_editor_data.p_radial_emitter_pos
    
    def espe_update_emitter_radius_pos():
        espe_editor_data.psystem_object.emitter_radius = espe_editor_data.p_emitter_radius

    def espe_update_sides_emitter():
        espe_editor_data.psystem_object.out_of_bounds_spawn_dict = espe_editor_data.p_out_of_bounds_spawn_dict
        espe_editor_data.psystem_object.current_sides = [side for side in espe_editor_data.p_out_of_bounds_spawn_dict.keys() if espe_editor_data.p_out_of_bounds_spawn_dict[side] is True]

    def espe_update_screen_bounded_property():
        espe_editor_data.psystem_object.is_screen_bounded = espe_editor_data.p_is_screen_bounded

    def espe_set_dot_emitter_pos():
        psystem = espe_editor_data.psystem_object

        psystem.positioning_func = psystem.dot_emitter
    
    def espe_set_rectangle_emitter_pos():
        psystem = espe_editor_data.psystem_object

        psystem.positioning_func = psystem.rectangle_emitter
    
    def espe_set_radial_emitter_pos():
        psystem = espe_editor_data.psystem_object

        psystem.positioning_func = psystem.radial_emitter

    def espe_set_screen_emitter_pos():
        psystem = espe_editor_data.psystem_object

        psystem.positioning_func = psystem.screen_emitter
    
    def espe_set_sides_emitter_pos():
        psystem = espe_editor_data.psystem_object

        psystem.positioning_func = psystem.sides_emitter
    ##]

    ##[
    def espe_update_dtime_func():
        fixed_dtime_func = espe_editor_data.psystem_object.get_fixed_delta_time
        active_dtime_func = espe_editor_data.psystem_object.get_delta_frame_time

        espe_editor_data.psystem_object.inner_frame_check = espe_editor_data.p_inner_frame_check

        if espe_editor_data.p_inner_frame_check:
            espe_editor_data.psystem_object.dtime_func = fixed_dtime_func
            espe_editor_data.psystem_object.fixed_dtime = 0.016
        
        else:
            espe_editor_data.psystem_object.dtime_func = active_dtime_func

    def espe_update_update_time():
        new_update_time = espe_editor_data.p_update_time

        espe_editor_data.p_update_time_last = new_update_time
        espe_editor_data.psystem_object.update_time = new_update_time
    ##]

    ##Возможно это дебилизм, но я не хочу, чтобы в методе обработки частицы постоянно вызывался .values(). Это же постоянное копирование!##
    ##В сгенерированном коде этого не будет, там всё будет проще, но в редакторе это необходимо учитывать.##
    def espe_update_processes():
        psystem = espe_editor_data.psystem_object

        psystem.particle_processing = psystem.particle_processing_dict.values()
        psystem.particle_processing_changer = psystem.particle_processing_changer_dict.values()

    ##[
    def espe_simple_move_update():
        psystem = espe_editor_data.psystem_object
        speed_changer = espe_editor_data.p_speed_simple_move_changer_type

        if speed_changer:
            psystem.move_prop_changer_func = psystem.speed_changer
            psystem.particle_processing_changer_dict["move_func_changer"] = psystem.speed_changer
        else:
            psystem.move_prop_changer_func = psystem.move_prop_static_changer
            psystem.particle_processing_changer_dict["move_func_changer"] = psystem.move_prop_static_changer

        espe_update_processes()

    def espe_accelerate_move_update(): #Лучше сука я не придумал. Балбес.
        psystem = espe_editor_data.psystem_object
        speed_changer = espe_editor_data.p_speed_accelerate_move_changer_type
        accelerate_changer = espe_editor_data.p_acc_accelerate_move_changer_type

        if speed_changer and accelerate_changer:
            psystem.move_prop_changer_func = psystem.speed_acc_changer
            psystem.particle_processing_changer_dict["move_func_changer"] = psystem.move_prop_changer_func
        elif speed_changer:
            psystem.move_prop_changer_func = psystem.static_accelerate_changer
            psystem.particle_processing_changer_dict["move_func_changer"] = psystem.move_prop_changer_func
        elif accelerate_changer:
            psystem.move_prop_changer_func = psystem.accelerate_changer
            psystem.particle_processing_changer_dict["move_func_changer"] = psystem.move_prop_changer_func
        else:
           psystem.move_prop_changer_func = psystem.move_prop_static_changer
           psystem.particle_processing_changer_dict["move_func_changer"] = psystem.move_prop_changer_func
        
        espe_update_processes()
    
    def espe_set_static_move():
        psystem = espe_editor_data.psystem_object

        psystem.move_func = psystem.static_move
        psystem.move_prop_changer_func = psystem.move_prop_static_changer

        ##Решено сделать функцию движения "Константой".##
        psystem.particle_processing_dict["move_func"] = psystem.move_func
        psystem.particle_processing_changer_dict["move_func_changer"] = psystem.move_prop_changer_func

        espe_update_processes()

    def espe_set_simple_move():
        psystem = espe_editor_data.psystem_object

        psystem.move_func = psystem.simple_move

        psystem.particle_processing_dict["move_func"] = psystem.move_func
        espe_simple_move_update()

    def espe_set_accelerate_move():
        psystem = espe_editor_data.psystem_object

        psystem.move_func = psystem.accelerate_move

        psystem.particle_processing_dict["move_func"] = psystem.move_func
        espe_accelerate_move_update()

    def espe_update_speed():
        psystem = espe_editor_data.psystem_object

        psystem.max_x_speed = espe_editor_data.p_max_x_speed - 1000.0
        psystem.min_x_speed = espe_editor_data.p_min_x_speed - 1000.0
        psystem.max_y_speed = espe_editor_data.p_max_y_speed - 1000.0
        psystem.min_y_speed = espe_editor_data.p_min_y_speed - 1000.0
    
    def espe_update_accelerate():
        psystem = espe_editor_data.psystem_object

        psystem.max_x_accelerate = espe_editor_data.p_max_x_accelerate - 100.0
        psystem.min_x_accelerate = espe_editor_data.p_min_x_accelerate - 100.0
        psystem.max_y_accelerate = espe_editor_data.p_max_y_accelerate - 100.0
        psystem.min_y_accelerate = espe_editor_data.p_min_y_accelerate - 100.0
    
    ####[
    def espe_set_prop_changer_none():
        espe_editor_data.psystem_object.move_extra_prop_changer_func = None

    def espe_set_prop_changer_oscillatory():
        psystem = espe_editor_data.psystem_object

        psystem.move_extra_prop_changer_func = psystem.extra_move_prop_changer_oscillatory_zip

    def espe_update_extra_move():
        psystem = espe_editor_data.psystem_object

        if espe_editor_data.p_move_extra_type == 0:
            psystem.move_extra_func = None
            psystem.particle_processing_dict.pop("move_extra_func", None)
            espe_set_prop_changer_none()

        elif espe_editor_data.p_move_extra_type == 1:
            espe_set_prop_changer_oscillatory()
            psystem.move_extra_func = psystem.extra_move_oscillatory
            psystem.particle_processing_dict["move_extra_func"] = psystem.move_extra_func

        espe_toggle_extra_prop_changer()

    def espe_toggle_extra_prop_changer():
        psystem = espe_editor_data.psystem_object

        if espe_editor_data.p_move_extra_type == 0:
            psystem.particle_processing_changer_dict.pop("move_extra_prop_changer_func", None)
        else:
            psystem.particle_processing_changer_dict["move_extra_prop_changer_func"] = psystem.move_extra_prop_changer_func

        espe_update_processes()

    def espe_update_oscillatory_speed_changer():
        psystem = espe_editor_data.psystem_object

        if espe_editor_data.p_speed_extra_changer_type:
            psystem.move_extra_speed_changer_func = psystem.extra_move_speed_changer
        else:
            psystem.move_extra_speed_changer_func = psystem.extra_move_speed_static
        
        espe_toggle_extra_prop_changer()
    
    def espe_update_oscillatory_radius_changer():
        psystem = espe_editor_data.psystem_object

        if espe_editor_data.p_radius_oscillatory_changer_type:
            psystem.move_extra_radius_changer_func = psystem.extra_move_radius_changer
        else:
            psystem.move_extra_radius_changer_func = psystem.extra_move_radius_static
        
        espe_toggle_extra_prop_changer()
    
    def espe_update_oscillatory_phase_changer():
        psystem = espe_editor_data.psystem_object

        if espe_editor_data.p_random_start_phase:
            psystem.move_extra_phase_changer_func = psystem.extra_move_phase_changer
        else:
            psystem.move_extra_phase_changer_func = psystem.extra_move_phase_static

        espe_toggle_extra_prop_changer()

    def espe_update_extra_speed_oscillatory():
        psystem = espe_editor_data.psystem_object

        psystem.max_speed_oscillatory = espe_editor_data.p_max_speed_oscillatory - 1000.0
        psystem.min_speed_oscillatory = espe_editor_data.p_min_speed_oscillatory - 1000.0
    
    def espe_update_extra_radius_oscillatory():
        psystem = espe_editor_data.psystem_object

        psystem.max_x_oscillatory = espe_editor_data.p_max_x_oscillatory
        psystem.min_x_oscillatory = espe_editor_data.p_min_x_oscillatory
        psystem.max_y_oscillatory = espe_editor_data.p_max_y_oscillatory
        psystem.min_y_oscillatory = espe_editor_data.p_min_y_oscillatory
    
    def espe_update_extra_phase_oscillatory():
        psystem = espe_editor_data.psystem_object

        psystem.extra_move_phase = espe_editor_data.p_extra_phase
    ####]
    ##]

    ##[
    ##Функция прозрачности вызывается всегда. Нет смысла её добавлять в список обновлений значений свойств.##
    def espe_static_alpha_update():
        psystem = espe_editor_data.psystem_object
        alpha_changer_static = espe_editor_data.p_alpha_changer_static_type

        if alpha_changer_static:
            psystem.alpha_changer_func = psystem.alpha_static_changer
        else:
            psystem.alpha_changer_func = psystem.alpha_static_constant_changer

    def espe_alpha_fade_in_out_update():
        psystem = espe_editor_data.psystem_object
        alpha_changer_fade_in_out = espe_editor_data.p_alpha_changer_fade_in_out_type

        if alpha_changer_fade_in_out:
            psystem.alpha_changer_func = psystem.alpha_fade_in_out_changer
        else:
            psystem.alpha_changer_func = psystem.alpha_fade_in_out_constant_changer

    def espe_alpha_oscillatory_update():
        psystem = espe_editor_data.psystem_object
        alpha_changer_oscillatory = espe_editor_data.p_alpha_changer_oscillatory_type

        if alpha_changer_oscillatory:
            psystem.alpha_transparency_changer_func = psystem.alpha_fade_in_out_changer
        else:
            psystem.alpha_transparency_changer_func = psystem.alpha_fade_in_out_constant_changer

    def espe_alpha_oscillatory_speed_update():
        psystem = espe_editor_data.psystem_object
        alpha_changer_oscillatory_speed = espe_editor_data.p_alpha_changer_oscillatory_speed_type
        
        if alpha_changer_oscillatory_speed:
            psystem.alpha_speed_changer_func = psystem.alpha_oscillatory_speed_changer
        else:
            psystem.alpha_speed_changer_func = psystem.alpha_oscillatory_speed_constant_changer
    
    def espe_alpha_oscillatory_phase_update():
        psystem = espe_editor_data.psystem_object
        alpha_changer_oscillatory_phase = espe_editor_data.p_alpha_changer_oscillatory_phase_type

        if alpha_changer_oscillatory_phase:
            psystem.alpha_phase_changer_func = psystem.alpha_oscillatory_phase_changer
        else:
            psystem.alpha_phase_changer_func = psystem.alpha_oscillatory_phase_constant_changer

    def espe_set_static_alpha():
        psystem = espe_editor_data.psystem_object

        psystem.alpha_func = None

        psystem.particle_processing_dict.pop("alpha_func", None)

        espe_static_alpha_update()
        espe_update_processes()

    def espe_set_fade_in_out_alpha():
        psystem = espe_editor_data.psystem_object

        psystem.alpha_func = psystem.alpha_fade_in_out_func
        psystem.particle_processing_dict["alpha_func"] = psystem.alpha_func

        espe_alpha_fade_in_out_update()
        espe_update_processes()
    
    def espe_set_oscillatory_alpha():
        psystem = espe_editor_data.psystem_object

        psystem.alpha_func = psystem.alpha_oscillatory_func
        psystem.alpha_changer_func = psystem.alpha_oscillatory_changer_zip
        psystem.particle_processing_dict["alpha_func"] = psystem.alpha_func

        espe_alpha_oscillatory_update()
        espe_update_processes()

    def espe_update_alpha():
        psystem = espe_editor_data.psystem_object

        psystem.intermediate_max_alpha = espe_editor_data.p_intermediate_max_alpha
        psystem.intermediate_min_alpha = espe_editor_data.p_intermediate_min_alpha


    def espe_safe_update_time_alpha():
        psystem = espe_editor_data.psystem_object

        main_difference = 1.0 - (espe_editor_data.p_alpha_appear_time_percentage + espe_editor_data.p_alpha_disappear_time_percentage)

        if main_difference < 0:
            difference_between_in_out = builtins.abs(espe_editor_data.p_alpha_appear_time_percentage - espe_editor_data.p_alpha_disappear_time_percentage)
            if espe_editor_data.p_alpha_appear_time_percentage >= espe_editor_data.p_alpha_disappear_time_percentage:
                espe_editor_data.p_alpha_appear_time_percentage -= difference_between_in_out
            else:
                espe_editor_data.p_alpha_disappear_time_percentage -= difference_between_in_out
        
        psystem.alpha_appear_time_percentage = espe_editor_data.p_alpha_appear_time_percentage
        psystem.alpha_disappear_time_percentage = espe_editor_data.p_alpha_disappear_time_percentage

    def espe_update_alpha_speed():
        psystem = espe_editor_data.psystem_object

        psystem.alpha_max_speed = espe_editor_data.p_alpha_max_speed
        psystem.alpha_min_speed = espe_editor_data.p_alpha_min_speed

    def espe_update_alpha_phase():
        psystem = espe_editor_data.psystem_object

        psystem.alpha_phase = espe_editor_data.p_alpha_phase
    ##]

    ##[
    ##Функция масштабирования вызывается всегда. Нет смысла её добавлять в список обновлений значений свойств.##
    def espe_static_zoom_update():
        psystem = espe_editor_data.psystem_object
        zoom_changer_static = espe_editor_data.p_zoom_changer_static_type

        if zoom_changer_static:
            psystem.zoom_changer_func = psystem.zoom_static_changer
        else:
            psystem.zoom_changer_func = psystem.zoom_static_constant_changer

    def espe_zoom_fade_in_out_update():
        psystem = espe_editor_data.psystem_object
        zoom_changer_fade_in_out = espe_editor_data.p_zoom_changer_fade_in_out_type

        if zoom_changer_fade_in_out:
            psystem.zoom_changer_func = psystem.zoom_fade_in_out_changer
        else:
            psystem.zoom_changer_func = psystem.zoom_fade_in_out_constant_changer

    def espe_zoom_oscillatory_update():
        psystem = espe_editor_data.psystem_object
        zoom_changer_oscillatory = espe_editor_data.p_zoom_changer_oscillatory_type

        if zoom_changer_oscillatory:
            psystem.zoom_scale_changer_func = psystem.zoom_fade_in_out_changer
        else:
            psystem.zoom_scale_changer_func = psystem.zoom_fade_in_out_constant_changer

    def espe_zoom_oscillatory_speed_update():
        psystem = espe_editor_data.psystem_object
        zoom_changer_oscillatory_speed = espe_editor_data.p_zoom_changer_oscillatory_speed_type
        
        if zoom_changer_oscillatory_speed:
            psystem.zoom_speed_changer_func = psystem.zoom_oscillatory_speed_changer
        else:
            psystem.zoom_speed_changer_func = psystem.zoom_oscillatory_speed_constant_changer
    
    def espe_zoom_oscillatory_phase_update():
        psystem = espe_editor_data.psystem_object
        zoom_changer_oscillatory_phase = espe_editor_data.p_zoom_changer_oscillatory_phase_type

        if zoom_changer_oscillatory_phase:
            psystem.zoom_phase_changer_func = psystem.zoom_oscillatory_phase_changer
        else:
            psystem.zoom_phase_changer_func = psystem.zoom_oscillatory_phase_constant_changer

    def espe_set_static_zoom():
        psystem = espe_editor_data.psystem_object

        psystem.zoom_func = None

        psystem.particle_processing_dict.pop("zoom_func", None)

        espe_static_zoom_update()
        espe_update_processes()

    def espe_set_fade_in_out_zoom():
        psystem = espe_editor_data.psystem_object

        psystem.zoom_func = psystem.zoom_fade_in_out_func
        psystem.particle_processing_dict["zoom_func"] = psystem.zoom_func

        espe_zoom_fade_in_out_update()
        espe_update_processes()
    
    def espe_set_oscillatory_zoom():
        psystem = espe_editor_data.psystem_object

        psystem.zoom_func = psystem.zoom_oscillatory_func
        psystem.zoom_changer_func = psystem.zoom_oscillatory_changer_zip
        psystem.particle_processing_dict["zoom_func"] = psystem.zoom_func

        espe_zoom_oscillatory_update()
        espe_update_processes()

    def espe_update_zoom():
        psystem = espe_editor_data.psystem_object

        psystem.intermediate_max_zoom = espe_editor_data.p_intermediate_max_zoom
        psystem.intermediate_min_zoom = espe_editor_data.p_intermediate_min_zoom

    def espe_safe_update_time_zoom():
        psystem = espe_editor_data.psystem_object

        main_difference = 1.0 - (espe_editor_data.p_zoom_appear_time_percentage + espe_editor_data.p_zoom_disappear_time_percentage)

        if main_difference < 0:
            difference_between_in_out = builtins.abs(espe_editor_data.p_zoom_appear_time_percentage - espe_editor_data.p_zoom_disappear_time_percentage)
            if espe_editor_data.p_zoom_appear_time_percentage >= espe_editor_data.p_zoom_disappear_time_percentage:
                espe_editor_data.p_zoom_appear_time_percentage -= difference_between_in_out
            else:
                espe_editor_data.p_zoom_disappear_time_percentage -= difference_between_in_out
        
        psystem.zoom_appear_time_percentage = espe_editor_data.p_zoom_appear_time_percentage
        psystem.zoom_disappear_time_percentage = espe_editor_data.p_zoom_disappear_time_percentage

    def espe_update_zoom_speed():
        psystem = espe_editor_data.psystem_object

        psystem.zoom_max_speed = espe_editor_data.p_zoom_max_speed
        psystem.zoom_min_speed = espe_editor_data.p_zoom_min_speed

    def espe_update_zoom_phase():
        psystem = espe_editor_data.psystem_object

        psystem.zoom_phase = espe_editor_data.p_zoom_phase
    ##]

    ##[
    ##Функция вращения вызывается всегда. Нет смысла её добавлять в список обновлений значений свойств.##
    ##Вызывается всегда потому что в редакторе нужно постоянно обновлять свойства частиц.##
    ##При генерации кода это будет учитываться.##
    def espe_static_rotate_update():
        psystem = espe_editor_data.psystem_object
        rotate_changer_static = espe_editor_data.p_rotate_changer_static_type

        if rotate_changer_static:
            psystem.rotate_changer_func = psystem.rotate_static_changer
        else:
            psystem.rotate_changer_func = psystem.rotate_static_constant_changer

    def espe_dynamic_rotate_start_angle_update():
        psystem = espe_editor_data.psystem_object
        rotate_changer_start_angle = espe_editor_data.p_dynamic_rotate_changer_angle_type

        if rotate_changer_start_angle:
            psystem.dynamic_rotate_changer_angle_func = psystem.dynamic_rotate_start_angle_changer
        else:
            psystem.dynamic_rotate_changer_angle_func = psystem.dynamic_rotate_start_angle_constant_changer

    def espe_dynamic_rotate_speed_update():
        psystem = espe_editor_data.psystem_object
        rotate_changer_speed_angle = espe_editor_data.p_dynamic_rotate_changer_speed_type

        if rotate_changer_speed_angle:
            psystem.dynamic_rotate_changer_speed_func = psystem.dynamic_rotate_speed_changer
        else:
            psystem.dynamic_rotate_changer_speed_func = psystem.dynamic_rotate_speed_constant_changer

    def espe_rotate_by_speed_speed_type_update(update_processes=False):
        psystem = espe_editor_data.psystem_object

        if espe_editor_data.p_rotate_by_speed_type == 0:
            psystem.rotate_func = psystem.rotate_by_speed_x_func
            psystem.rotate_changer_func = psystem.rotate_by_speed_x_changer
        else:
            psystem.rotate_func = psystem.rotate_by_speed_y_func
            psystem.rotate_changer_func = psystem.rotate_by_speed_y_changer

        if update_processes:
            psystem.particle_processing_dict["rotate_func"] = psystem.rotate_func
            espe_update_processes()

    def espe_set_static_rotate():
        psystem = espe_editor_data.psystem_object

        psystem.rotate_func = None

        psystem.particle_processing_dict.pop("rotate_func", None)

        espe_static_rotate_update()
        espe_update_processes()

    def espe_set_dynamic_rotate():
        psystem = espe_editor_data.psystem_object

        psystem.rotate_func = psystem.dynamic_rotate_func
        psystem.rotate_changer_func = psystem.dynamic_rotate_changer_zip
        psystem.particle_processing_dict["rotate_func"] = psystem.rotate_func

        espe_update_processes()

    def espe_set_rotate_by_speed():
        psystem = espe_editor_data.psystem_object

        espe_rotate_by_speed_speed_type_update()

        psystem.particle_processing_dict["rotate_func"] = psystem.rotate_func

        espe_update_processes()

    def espe_update_rotate_static_angle():
        psystem = espe_editor_data.psystem_object

        psystem.max_angle = espe_editor_data.p_max_angle
        psystem.min_angle = espe_editor_data.p_min_angle

    def espe_update_dynamic_rotate_start_angle():
        psystem = espe_editor_data.psystem_object

        psystem.dynamic_rotate_max_start_angle = espe_editor_data.p_dynamic_rotate_max_start_angle
        psystem.dynamic_rotate_min_start_angle = espe_editor_data.p_dynamic_rotate_min_start_angle

    def espe_update_dynamic_rotate_speed():
        psystem = espe_editor_data.psystem_object

        psystem.dynamic_rotate_max_speed = espe_editor_data.p_dynamic_rotate_max_speed - 1000.0
        psystem.dynamic_rotate_min_speed = espe_editor_data.p_dynamic_rotate_min_speed - 1000.0
    
    def espe_update_rotate_by_speed_start_angle():
        psystem = espe_editor_data.psystem_object

        psystem.rotate_by_speed_start_angle = espe_editor_data.p_rotate_by_speed_start_angle

    def espe_update_rotate_by_speed_max_min_speed():
        psystem = espe_editor_data.psystem_object

        psystem.rotate_by_speed_max_speed = espe_editor_data.p_rotate_by_speed_max_speed - 1000.0
    ##]

    def espe_clamp(value, range):
        if not isinstance(value, (int, float)):
            return value

        if range is None:
            return value

        return builtins.max(builtins.min(value, range[1]), range[0])

    ##Это неправильно. Этой функции не должно быть.
    def espe_additional(value, additional):
        if additional is None:
            return value
        if type(value) == type(additional):
            return value + additional
        return value

    ##Это неправильно. Этой функции не должно быть.
    def espe_additional_substract(value, additional):
        if additional is None:
            return value
        if type(value) == type(additional):
            return value - additional
        return value

    ##Это неправильно. Этой функции не должно быть.
    def espe_multiplie_value(value, multiplier):
        if multiplier is None:
            return value
        if type(value) == type(multiplier):
            return value * multiplier
        return value

    ##Это неправильно. Этой функции не должно быть.
    def espe_divide_value(value, multiplier):
        if multiplier is None:
            return value
        if type(value) == type(multiplier):
            return value / multiplier
        return value
    
    def espe_input_safe_check(var, var_type, obj, field, allow_empty=False):
        try:
            converted_var = var_type(var)
        except (ValueError, TypeError):
                return False
        if getattr(obj, field) == converted_var:
            return False
        if not var and not allow_empty:
            return False
        return True

    def espe_input_collections_safe(field_collection, value, index, obj):
        collection = getattr(obj, field_collection)
        collection[index] = value

        setattr(obj, field_collection, collection)

    def espe_field_type_safe(field_value, field_type):
        try:
            return field_type(field_value)
        except ValueError:
            #raise ValueError("Cannot convert string \'{}\' to integer".format(field_value))
            return field_value
    
    def espe_get_elem_by_index_safe(cur_list, index):
        try:
            return cur_list[index]
        except IndexError:
            return None
    
    def espe_simple_min(value_1, value_2):
        if value_1 > value_2:
            return value_2
        return value_1
    
    def beautifuly_string(string):
        intermediate_string = string[1:].replace('_', ' ').replace("won t", "won't") #.replace("that s", "that's") - не работает. huh?
        first_letter_upper = string[0].upper()
        beautiful_string = first_letter_upper + intermediate_string
        return beautiful_string

    #*Для получения ифнормации о системе частиц.*#
    ##[
    def espe_get_position_spawn_type_string(data_from_file=None):
        position_types = ["Точечный испускатель", "Прямоугольная зона", "Радиальная зона", "По всему экрану", "От границ экрана"]

        if data_from_file is not None:
            return position_types[data_from_file]

        return position_types[espe_editor_data.p_spawn_area_type]
    
    def espe_get_emitting_borders(data_from_file=None):
        borders = {"Left": "Левая", "Right": "Правая", "Top": "Верхняя", "Bottom":"Нижняя"}

        string = ""

        if data_from_file is not None:
            for key, value in data_from_file.items():
                if value:
                    string += borders[key] + ", "
        else:
            for key, value in espe_editor_data.p_out_of_bounds_spawn_dict.items():
                if value:
                    string += borders[key] + ", "

        return string[:-2]
    
    def espe_get_movement_type_string(data_from_file=None):
        movement_types = ["Статика", "Простое движение", "Движение с ускорением"]

        if data_from_file is not None:
            return movement_types[data_from_file]

        return movement_types[espe_editor_data.p_move_type]
    
    #Нахуя, да? По-приколу.#
    def espe_get_speed_changer_simple_move_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        speed_changer = espe_editor_data.p_speed_simple_move_changer_type

        return speed_changer
    
    def espe_get_speed_changer_accelerate_move_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        speed_changer = espe_editor_data.p_speed_accelerate_move_changer_type

        return speed_changer
    
    def espe_get_speed_changer_accelerate_move_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        acc_changer = espe_editor_data.p_acc_accelerate_move_changer_type

        return acc_changer

    def espe_get_extra_movement_type_string(data_from_file=None):
        extra_movement_types = ["Без дополнительного движения", "Колебательное движение"]

        if data_from_file is not None:
            return extra_movement_types[data_from_file]

        return extra_movement_types[espe_editor_data.p_move_extra_type]

    def espe_get_speed_changer_extra_move_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        speed_changer = espe_editor_data.p_speed_extra_changer_type

        return speed_changer
    
    def espe_get_radius_oscillatory_changer_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        radius_changer = espe_editor_data.p_radius_oscillatory_changer_type

        return radius_changer

    def espe_get_phase_oscillatory_changer_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        phase_changer = espe_editor_data.p_random_start_phase

        return phase_changer
    
    def espe_get_alpha_type_string(data_from_file=None):
        alpha_types = ["Постоянная", "Появление/затухание", "Колебательная"]

        if data_from_file is not None:
            return alpha_types[data_from_file]

        return alpha_types[espe_editor_data.p_alpha_type]
    
    def espe_get_alpha_transaprency_changer_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        alpha_changer = espe_editor_data.p_alpha_changer_static_type

        return alpha_changer
    
    def espe_get_alpha_transaprency_fade_in_out_changer_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        alpha_changer = espe_editor_data.p_alpha_changer_fade_in_out_type

        return alpha_changer
    
    def espe_get_alpha_transaprency_oscillatory_changer_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        alpha_changer = espe_editor_data.p_alpha_changer_oscillatory_type

        return alpha_changer

    def espe_get_alpha_speed_oscillatory_changer_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        speed_changer = espe_editor_data.p_alpha_changer_oscillatory_type

        return speed_changer
    
    def espe_get_alpha_phase_oscillatory_changer_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        phase_changer = espe_editor_data.p_alpha_changer_oscillatory_type

        return phase_changer
    
    def espe_get_zoom_type_string(data_from_file=None):
        zoom_types = ["Постоянный", "Появление/затухание", "Колебательный"]

        if data_from_file is not None:
            return zoom_types[data_from_file]

        return zoom_types[espe_editor_data.p_zoom_type]
    
    def espe_get_zoom_scale_changer_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        zoom_changer = espe_editor_data.p_zoom_changer_static_type

        return zoom_changer
    
    def espe_get_zoom_scale_fade_in_out_changer_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        zoom_changer = espe_editor_data.p_zoom_changer_fade_in_out_type

        return zoom_changer
    
    def espe_get_zoom_scale_oscillatory_changer_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        zoom_changer = espe_editor_data.p_zoom_changer_oscillatory_type

        return zoom_changer

    def espe_get_zoom_speed_oscillatory_changer_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        speed_changer = espe_editor_data.p_zoom_changer_oscillatory_type

        return speed_changer
    
    def espe_get_zoom_phase_oscillatory_changer_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        phase_changer = espe_editor_data.p_zoom_changer_oscillatory_type

        return phase_changer
    
    def espe_get_rotate_type_string(data_from_file=None):
        rotate_types = ["Постоянное", "Динамическое", "Зависимое от скорости"]

        if data_from_file is not None:
            return rotate_types[data_from_file]

        return rotate_types[espe_editor_data.p_rotate_type]
    
    def espe_get_rotate_static_changer_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        rotate_changer = espe_editor_data.p_rotate_changer_static_type

        return rotate_changer

    def espe_get_dynamic_rotate_speed_changer_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        speed_changer = espe_editor_data.p_dynamic_rotate_changer_speed_type

        return speed_changer

    def espe_get_dynamic_rotate_angle_changer_type(data_from_file=None):
        if data_from_file is not None:
            return data_from_file

        rotate_changer = espe_editor_data.p_dynamic_rotate_changer_angle_type

        return rotate_changer
    ##]
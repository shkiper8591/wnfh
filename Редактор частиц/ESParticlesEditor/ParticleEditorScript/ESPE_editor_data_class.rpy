init python:
    class ESPEEditorData(renpy.object.Object):
        """
        Класс, отвечающий за редактор частиц. В нём хранится вся информация о свойствах системы частиц.
        Данный класс анализируется при генерации кода. 
        """

        def __init__(self):
             #*Общее.*#
            ##[
            self.psystem_name = "Система частиц!"
            self.psystem_type = None

            self.psystem_object = None
            self.psystem_manager = None
            self.psystem_screen = None
            ##]

             #*Спрайты.*#
             ##[
            self.p_displayable_list = ["espe_primitive_square"]
            self.p_displayable_names = ["Квадрат"]
            ##]

            #*Субпикселирование.*#
            #НЕ РЕАЛИЗОВАНО.#
            #self.p_subpixel = False

            #*Привязка.*#
            ##НЕ РАБОТАЕТ.##
            ##[
            #self.p_anchor = [0.0, 0.0]
            ##]

            #*Позиционирование.*#
            ##[
            self.p_spawn_area_type = 0 #0 - точка; 1 - прямоугольная зона; 2 - круговая зона; 3 - по всему видимому экрану; 4 - за пределами экрана.
            self.p_emitter_pos = [960, 540]
            
            self.p_rectangle_emitter_pos = [960, 540]
            self.p_rectangle_spawn_area = [100, 100]

            self.p_radial_emitter_pos = [960, 540]
            self.p_emitter_radius = 50

            self.p_out_of_bounds_spawn_dict = {"Left": False, "Right": False, "Top": True, "Bottom": False}
            ##]

            #*Движение.*#
            ##[
            self.p_move_type = 1 #0 - недвижимы; 1 - движение по скорости; 2 - движение с ускорением.
            self.p_speed_simple_move_changer_type = False #False - не изменяется; True - случайная в диапазоне.
            self.p_speed_accelerate_move_changer_type = False #False - не изменяется; True - случайная скорость в диапазоне.
            self.p_acc_accelerate_move_changer_type = False #False - не изменяется; True - случайное ускорение в диапазоне.

            self.p_max_x_speed = 1000.0 #Отнимайте 1000. Это для шкалы. Диапазаон скоростей от -1000 до 1000.
            self.p_min_x_speed = 1000.0
            self.p_max_y_speed = 1250.0
            self.p_min_y_speed = 1250.0

            self.p_max_x_accelerate = 100.0 #Отнимайте 100. Диапазон от -100 до 100.
            self.p_min_x_accelerate = 100.0
            self.p_max_y_accelerate = 100.0
            self.p_min_y_accelerate = 100.0

                #*Дополнительное движение.*#
            ####[
            self.p_move_extra_type = 0 #0 - без дополнительного движения; 1 - колебательное движение.
            self.p_speed_extra_changer_type = False #False - не изменяется; True - случайная скорость в диапазоне.
            self.p_radius_oscillatory_changer_type = False #False - не изменяется; True - случайный радиус (x и y) в диапазоне.
            self.p_random_start_phase = False #False - начальный угол у всех частиц постоянный; True - случайный угол от 0 до 360 градусов.

            self.p_max_speed_oscillatory = 1200.0 #Отнимайте 1000. Это для шкалы. Диапазаон скоростей от -1000 до 1000.
            self.p_min_speed_oscillatory = 1200.0

            self.p_extra_phase = 0.0

            self.p_max_x_oscillatory = 0.0
            self.p_min_x_oscillatory = 0.0
            self.p_max_y_oscillatory = 0.0
            self.p_min_y_oscillatory = 0.0
            ####]
            ##]
            
            #*Непрозрачность.*#
            ##[
            self.p_alpha_type = 0 #0 - постоянная прозрачность; 1 - появление/затухание; 2 - колебательная прозрачность.
            self.p_alpha_changer_static_type = False #False - не изменяется; True - случайная прозрачность в диапазоне.

            self.p_alpha_changer_fade_in_out_type = False #False - не изменяется; True - случайная прозрачность в диапазоне.

            self.p_alpha_changer_oscillatory_type = False #False - не изменяется; True - случайная прозрачность в диапазоне (колебательная прозрачность).
            self.p_alpha_changer_oscillatory_speed_type = False #False - не изменяется; True - случайная частота в диапазоне (колебательная прозрачность).
            self.p_alpha_changer_oscillatory_phase_type = False #False - не изменяется; True - случайная фаза от 0 до 360 градусов (колебательная прозрачность).

            self.p_intermediate_max_alpha = 1.0
            self.p_intermediate_min_alpha = 1.0
            self.p_alpha_appear_time_percentage = 0.0
            self.p_alpha_disappear_time_percentage = 0.0

            self.p_alpha_max_speed = 200.0
            self.p_alpha_min_speed = 200.0
            self.p_alpha_phase = 0.0
            ##]

            #*Масштаб.*#
            ##[
            self.p_zoom_type = 0 #0 - постоянный масштаб; 1 - появление/затухание; 2 - колебательный масштаб.
            self.p_zoom_changer_static_type = False #False - не изменяется; True - случайный масштаб в диапазоне.

            self.p_zoom_changer_fade_in_out_type = False #False - не изменяется; True - случайный масштаб в диапазоне.

            self.p_zoom_changer_oscillatory_type = False #False - не изменяется; True - случайный масштаб в диапазоне (колебательный масштаб).
            self.p_zoom_changer_oscillatory_speed_type = False #False - не изменяется; True - случайная частота в диапазоне (колебательный масштаб).
            self.p_zoom_changer_oscillatory_phase_type = False #False - не изменяется; True - случайная фаза от 0 до 360 градусов (колебательный масштаб).

            self.p_intermediate_max_zoom = 1.0
            self.p_intermediate_min_zoom = 1.0
            self.p_zoom_appear_time_percentage = 0.0
            self.p_zoom_disappear_time_percentage = 0.0

            self.p_zoom_max_speed = 200.0
            self.p_zoom_min_speed = 200.0
            self.p_zoom_phase = 0.0
            ##]

            #*Вращение.*#
            ##[
            self.p_rotate_type = 0 #0 - постоянный угол; 1 - динамическое вращение; 2 - зависимость от скорости.
            self.p_rotate_changer_static_type = False #False - не изменяется; True - случайный угол в диапазоне.

            self.p_dynamic_rotate_changer_angle_type = False #False - не изменяется; True - случайный начальный угол в диапазоне.
            self.p_dynamic_rotate_changer_speed_type = False #False - не изменяется; True - случайная скорость в диапазоне.

            self.p_max_angle = 0.0
            self.p_min_angle = 0.0

            self.p_dynamic_rotate_max_start_angle = 0.0
            self.p_dynamic_rotate_min_start_angle = 0.0
            self.p_dynamic_rotate_max_speed = 1200.0 #Отнимайте 1000. Это для шкалы. Диапазаон скоростей от -1000 до 1000.
            self.p_dynamic_rotate_min_speed = 1200.0

            self.p_rotate_by_speed_type = 1 #0 - зависимость от горизантальной скорости; 1 - зависимость от вертикальной скорости.
            self.p_rotate_by_speed_start_angle = 0.0
            self.p_rotate_by_speed_max_speed = 1200.0 #Отнимайте 1000. Это для шкалы. Диапазаон скоростей от -1000 до 1000.
            ##]

            #*Количество.*#
            ##[
            self.p_amount = 5
            ##]

            #*Время жизни/задержка.*#
            ##[
            self.p_lifetime = 1.0
            self.p_lifetime_random_enable = False
            self.p_lifetime_random = 0.0
            self.p_lifetime_spread = 0.2
            self.p_lifetime_random_spread_enable = False
            self.p_lifetime_spread_random = 0.0
            ##]

            #*Взрывчатость.*#
            ##[
            self.p_is_explosiveness = False
            self.p_explosiveness_factor = 0.0
            self.p_explosiveness_amount = 0
            ##]

            #self.psys_oneshot = False

            #*Свойства вызова функции отрисовки.*#
            ##[
            self.p_inner_frame_check = True
            self.p_fixed_dtime = 0.016
            self.p_update_time = 0.0
            ##]

            #*Гибель за пределами экрана.*#
            ##[
            self.p_is_screen_bounded = False
            ##]

            self.last_edit_field_name = None
            self.prelast_edit_field_value = None

        ##Почему не словарём? Потому что гладиолус блять. Ну а вообще я сначала парсер под редактор сцены, а там мне был важен порядок, тут же и правда можно было сделать всё супер красиво словарём.##
        ##Довольствуйтесь [] и циферкаим :).##
        def set_data(self, psystem_data):
            filename = psystem_data[0]
            editor_data = psystem_data[1]
            name_data = psystem_data[2]
            sprites_data = psystem_data[3]
            amount_data = psystem_data[4]
            lifetime_data = psystem_data[5]
            explosiveness_data = psystem_data[6]
            emitter_type_data = psystem_data[7]
            movement_data = psystem_data[8]
            extra_movement_data = psystem_data[9]
            alpha_data = psystem_data[10]
            scale_data = psystem_data[11]
            rotate_data = psystem_data[12]
            optimization_data = psystem_data[13]

             #*Общее.*#
            ##[
            self.psystem_name = name_data[0]
            self.psystem_type = editor_data[0]

            self.set_psystem_object_by_type()
            self.set_manager_object_by_type()
            self.psystem_screen = editor_data[1]
            ##]

             #*Спрайты.*#
             ##[
            self.p_displayable_list = sprites_data[0]
            self.p_displayable_names = sprites_data[1]

            self.psystem_object.displayable_list = self.p_displayable_list
            ##]

            #*Позиционирование.*#
            ##[
            self.p_spawn_area_type = emitter_type_data[0]
            self.p_emitter_pos = emitter_type_data[1]
            
            self.p_rectangle_emitter_pos = emitter_type_data[2]
            self.p_rectangle_spawn_area = emitter_type_data[3]

            self.p_radial_emitter_pos = emitter_type_data[4]
            self.p_emitter_radius = emitter_type_data[5]

            self.p_out_of_bounds_spawn_dict = emitter_type_data[6]
            ##]

            #*Движение.*#
            ##[
            self.p_move_type = movement_data[0]
            self.p_speed_simple_move_changer_type = movement_data[1]
            self.p_speed_accelerate_move_changer_type = movement_data[2]
            self.p_acc_accelerate_move_changer_type = movement_data[3]

            self.p_max_x_speed = movement_data[4] + 1000.0
            self.p_min_x_speed = movement_data[5] + 1000.0
            self.p_max_y_speed = movement_data[6] + 1000.0
            self.p_min_y_speed = movement_data[7] + 1000.0

            self.p_max_x_accelerate = movement_data[8] + 100.0
            self.p_min_x_accelerate = movement_data[9] + 100.0
            self.p_max_y_accelerate = movement_data[10] + 100.0
            self.p_min_y_accelerate = movement_data[11] + 100.0

                #*Дополнительное движение.*#
            ####[
            self.p_move_extra_type = extra_movement_data[0]
            self.p_speed_extra_changer_type = extra_movement_data[1]
            self.p_radius_oscillatory_changer_type = extra_movement_data[2]
            self.p_random_start_phase = extra_movement_data[3]

            self.p_max_speed_oscillatory = extra_movement_data[4] + 1000.0
            self.p_min_speed_oscillatory = extra_movement_data[5] + 1000.0

            self.p_extra_phase = extra_movement_data[6]

            self.p_max_x_oscillatory = extra_movement_data[7]
            self.p_min_x_oscillatory = extra_movement_data[8]
            self.p_max_y_oscillatory = extra_movement_data[9]
            self.p_min_y_oscillatory = extra_movement_data[10]
            ####]
            ##]
            
            #*Непрозрачность.*#
            ##[
            self.p_alpha_type = alpha_data[0]
            self.p_alpha_changer_static_type = alpha_data[1]

            self.p_alpha_changer_fade_in_out_type = alpha_data[2]

            self.p_alpha_changer_oscillatory_type = alpha_data[3]
            self.p_alpha_changer_oscillatory_speed_type = alpha_data[4]
            self.p_alpha_changer_oscillatory_phase_type = alpha_data[5]
            self.p_intermediate_max_alpha = alpha_data[6]
            self.p_intermediate_min_alpha = alpha_data[7]
            self.p_alpha_appear_time_percentage = alpha_data[8]
            self.p_alpha_disappear_time_percentage = alpha_data[9]

            self.p_alpha_max_speed = alpha_data[10] + 200.0
            self.p_alpha_min_speed = alpha_data[11] + 200.0
            self.p_alpha_phase = alpha_data[12]
            ##]

            #*Масштаб.*#
            ##[
            self.p_zoom_type = scale_data[0]
            self.p_zoom_changer_static_type = scale_data[1]

            self.p_zoom_changer_fade_in_out_type = scale_data[2]

            self.p_zoom_changer_oscillatory_type = scale_data[3]
            self.p_zoom_changer_oscillatory_speed_type = scale_data[4]
            self.p_zoom_changer_oscillatory_phase_type = scale_data[5]

            self.p_intermediate_max_zoom = scale_data[6]
            self.p_intermediate_min_zoom = scale_data[7]
            self.p_zoom_appear_time_percentage = scale_data[8]
            self.p_zoom_disappear_time_percentage = scale_data[9]

            self.p_zoom_max_speed = scale_data[10] + 200.0
            self.p_zoom_min_speed = scale_data[11] + 200.0
            self.p_zoom_phase = scale_data[12]
            ##]

            #*Вращение.*#
            ##[
            self.p_rotate_type = rotate_data[0]
            self.p_rotate_changer_static_type = rotate_data[1]

            self.p_dynamic_rotate_changer_angle_type = rotate_data[2]
            self.p_dynamic_rotate_changer_speed_type = rotate_data[3]

            self.p_max_angle = rotate_data[4]
            self.p_min_angle = rotate_data[5]

            self.p_dynamic_rotate_max_start_angle = rotate_data[6]
            self.p_dynamic_rotate_min_start_angle = rotate_data[7]
            self.p_dynamic_rotate_max_speed = rotate_data[8] + 1000.0
            self.p_dynamic_rotate_min_speed = rotate_data[9] + 1000.0

            self.p_rotate_by_speed_type = rotate_data[10]
            self.p_rotate_by_speed_start_angle = rotate_data[11]
            self.p_rotate_by_speed_max_speed = rotate_data[12] + 1000.0
            ##]

            #*Количество.*#
            ##[
            self.p_amount = amount_data[0]
            ##]

            #*Время жизни/задержка.*#
            ##[
            self.p_lifetime = lifetime_data[0]
            self.p_lifetime_random_enable = lifetime_data[1]
            self.p_lifetime_random = lifetime_data[2]
            self.p_lifetime_spread = lifetime_data[3]
            self.p_lifetime_random_spread_enable = lifetime_data[4]
            self.p_lifetime_spread_random = lifetime_data[5]
            ##]

            #*Взрывчатость.*#
            ##[
            self.p_is_explosiveness = explosiveness_data[0]
            self.p_explosiveness_factor = explosiveness_data[1]
            self.p_explosiveness_amount = explosiveness_data[2]
            ##]

            #*Свойства вызова функции отрисовки.*#
            ##[
            self.p_inner_frame_check = optimization_data[0]
            self.p_fixed_dtime = optimization_data[1]
            self.p_update_time = optimization_data[2]
            
            self.psystem_object.old_st = 0.0
            ##]

            #*Гибель за пределами экрана.*#
            ##[
            self.p_is_screen_bounded = optimization_data[3]
            ##]
            
            self.change_psystem_type_safe()
            self.update_properties_types_safe()
            espe_editor_psystem_deep_reset()
        
        ##СИЛА В ХАРДКОДИНГЕ, БРАТ! (нет).##
        def get_data(self):
            editor_data = [
                self.psystem_type,
                self.psystem_screen
            ]

            name_data = [
                self.psystem_name
            ]

            sprites_data = [
                self.p_displayable_list,
                self.p_displayable_names
            ]

            amount_data = [
                self.p_amount
            ]

            lifetime_data = [
                self.p_lifetime,
                self.p_lifetime_random_enable,
                self.p_lifetime_random,
                self.p_lifetime_spread,
                self.p_lifetime_random_spread_enable,
                self.p_lifetime_spread_random
            ]

            explosiveness_data = [
                self.p_is_explosiveness,
                self.p_explosiveness_factor,
                self.p_explosiveness_amount
            ]

            emitter_type_data = [
                self.p_spawn_area_type,
                self.p_emitter_pos,
                self.p_rectangle_emitter_pos,
                self.p_rectangle_spawn_area,
                self.p_radial_emitter_pos,
                self.p_emitter_radius,
                self.p_out_of_bounds_spawn_dict
            ]

            movement_data = [
                self.p_move_type,
                self.p_speed_simple_move_changer_type,
                self.p_speed_accelerate_move_changer_type,
                self.p_acc_accelerate_move_changer_type,
                self.p_max_x_speed - 1000.0,
                self.p_min_x_speed - 1000.0,
                self.p_max_y_speed - 1000.0,
                self.p_min_y_speed - 1000.0,
                self.p_max_x_accelerate - 100.0,
                self.p_min_x_accelerate - 100.0,
                self.p_max_y_accelerate - 100.0,
                self.p_min_y_accelerate - 100.0
            ]
            extra_movement_data = [
                self.p_move_extra_type,
                self.p_speed_extra_changer_type,
                self.p_radius_oscillatory_changer_type,
                self.p_random_start_phase,
                self.p_max_speed_oscillatory - 1000.0,
                self.p_min_speed_oscillatory - 1000.0,
                self.p_extra_phase,
                self.p_max_x_oscillatory,
                self.p_min_x_oscillatory,
                self.p_max_y_oscillatory,
                self.p_min_y_oscillatory
            ]

            alpha_data = [
                self.p_alpha_type,
                self.p_alpha_changer_static_type,
                self.p_alpha_changer_fade_in_out_type,
                self.p_alpha_changer_oscillatory_type,
                self.p_alpha_changer_oscillatory_speed_type,
                self.p_alpha_changer_oscillatory_phase_type,
                self.p_intermediate_max_alpha,
                self.p_intermediate_min_alpha,
                self.p_alpha_appear_time_percentage,
                self.p_alpha_disappear_time_percentage,
                self.p_alpha_max_speed - 200.0,
                self.p_alpha_min_speed - 200.0,
                self.p_alpha_phase
            ]

            scale_data = [
                self.p_zoom_type,
                self.p_zoom_changer_static_type,
                self.p_zoom_changer_fade_in_out_type,
                self.p_zoom_changer_oscillatory_type,
                self.p_zoom_changer_oscillatory_speed_type,
                self.p_zoom_changer_oscillatory_phase_type,
                self.p_intermediate_max_zoom,
                self.p_intermediate_min_zoom,
                self.p_zoom_appear_time_percentage,
                self.p_zoom_disappear_time_percentage,
                self.p_zoom_max_speed - 200.0,
                self.p_zoom_min_speed - 200.0,
                self.p_zoom_phase
            ]

            rotate_data = [
                self.p_rotate_type,
                self.p_rotate_changer_static_type,
                self.p_dynamic_rotate_changer_angle_type,
                self.p_dynamic_rotate_changer_speed_type,
                self.p_max_angle,
                self.p_min_angle,
                self.p_dynamic_rotate_max_start_angle,
                self.p_dynamic_rotate_min_start_angle,
                self.p_dynamic_rotate_max_speed - 1000.0,
                self.p_dynamic_rotate_min_speed - 1000.0,
                self.p_rotate_by_speed_type,
                self.p_rotate_by_speed_start_angle,
                self.p_rotate_by_speed_max_speed - 1000.0
            ]

            optimization_data = [
                self.p_inner_frame_check,
                self.p_fixed_dtime,
                self.p_update_time,
                self.p_is_screen_bounded
            ]

            return (editor_data, name_data, sprites_data, amount_data, lifetime_data, explosiveness_data, emitter_type_data, movement_data, extra_movement_data, alpha_data, scale_data, rotate_data, optimization_data)

        def update_properties_types_safe(self):
            spawn_area_set_funcs = [espe_update_dot_emitter_pos, espe_update_rectangle_emitter_pos, espe_update_rectangle_spawn_area, espe_update_radial_emitter_pos, espe_update_emitter_radius_pos, espe_update_sides_emitter, espe_update_sides_emitter]
            spawn_area_psystem_funcs = [espe_set_dot_emitter_pos, espe_set_rectangle_emitter_pos, espe_set_radial_emitter_pos, espe_set_screen_emitter_pos, espe_set_sides_emitter_pos]
            
            movement_funcs = [espe_set_static_move, espe_set_simple_move, espe_set_accelerate_move]
            alpha_funs = [espe_set_static_alpha, espe_set_fade_in_out_alpha, espe_set_oscillatory_alpha]
            zoom_funcs = [espe_set_static_zoom, espe_set_fade_in_out_zoom, espe_set_oscillatory_zoom]
            rotate_funcs = [espe_set_static_rotate, espe_set_dynamic_rotate, espe_set_rotate_by_speed]

            self.psystem_object.amount = self.p_amount

            self.psystem_object.lifetime = self.p_lifetime
            self.psystem_object.lifetime_random_enable = self.p_lifetime_random_enable
            self.psystem_object.lifetime_random = self.p_lifetime_random
            self.psystem_object.lifetime_spread = self.p_lifetime_spread
            self.psystem_object.lifetime_spread_random_enable = self.p_lifetime_random_spread_enable
            self.psystem_object.lifetime_spread_random = self.p_lifetime_spread_random

            self.psystem_object.is_explosiveness = self.p_is_explosiveness
            self.psystem_object.explosiveness_factor = self.p_explosiveness_factor
            self.psystem_object.explosiveness_amount = self.p_explosiveness_amount

            espe_update_screen_bounded_property()
            espe_update_dtime_func()

            for func in spawn_area_set_funcs:
                func()
            spawn_area_psystem_funcs[self.p_spawn_area_type]()

            movement_funcs[self.p_move_type]()
            espe_update_speed()
            espe_update_accelerate()

            espe_update_extra_move()
            espe_update_oscillatory_speed_changer()
            espe_update_oscillatory_radius_changer()
            espe_update_oscillatory_phase_changer()
            espe_update_extra_speed_oscillatory()
            espe_update_extra_radius_oscillatory()
            espe_update_extra_phase_oscillatory()

            if self.psystem_type == "Сложная":
                alpha_funs[self.p_alpha_type]()
                espe_update_alpha()
                espe_safe_update_time_alpha()
                espe_update_alpha_speed()
                espe_update_alpha_phase()

                zoom_funcs[self.p_zoom_type]()
                espe_update_zoom()
                espe_safe_update_time_zoom()
                espe_update_zoom_speed()
                espe_update_zoom_phase()

                rotate_funcs[self.p_rotate_type]()
                espe_update_rotate_static_angle()
                espe_update_dynamic_rotate_start_angle()
                espe_update_dynamic_rotate_speed()
                espe_update_rotate_by_speed_start_angle()
                espe_update_rotate_by_speed_max_min_speed()

        def set_psystem_object_by_type(self):
            if self.psystem_type == "Сложная":
                self.psystem_object = ESPE_complex_particles
            else:
                self.psystem_object = ESPE_simple_particles

        def set_manager_object_by_type(self):
            if self.psystem_type == "Сложная":
                self.psystem_manager = ESPE_complex_particles_manager
            else:
                self.psystem_manager = ESPE_simple_particles_manager

        def change_psystem_type_safe(self):
            if self.psystem_type == "Сложная":
                renpy.hide_screen("ESPE_editor_simple_particles_show")
                renpy.show_screen("ESPE_editor_complex_particles_show")
            else:
                renpy.hide_screen("ESPE_editor_complex_particles_show")
                renpy.show_screen("ESPE_editor_simple_particles_show")
##Экраны для просмотра полной информации системы частиц.##
screen ESPE_particle_system_general_data():
    tag espe_editor_main

    $ data = espe_editor_data

    $ is_sprite_one = True if len(data.p_displayable_names) == 1 else False
    $ sprite_section_name = "Спрайт" if is_sprite_one else "Список спрайтов"
    $ rotate_by_speed_type_name = "X" if data.p_rotate_by_speed_type == 0 else "Y"

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)
    add Solid("#000", xsize=0.5, ysize=0.5) at fast_align_alpha(0.5, 0.5, 0.4)

    vbox:
        xalign 0.5
        yalign 0.18

        text "Параметры системы частиц" style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_heading_36"

    fixed:
        area (0.25, 0.26, 0.49, 0.48)
        viewport id "psystem_general_data":
            xalign 0.05
            xoffset 10
            draggable True
            mousewheel True
            scrollbars None

            has vbox:
                text "Общее" xalign 0.1 style "espe_text_heading_36"
                text "Название системы: {}".format(data.psystem_name) style "espe_text_24_0align"
                text "Тип системы: {}".format(data.psystem_type) style "espe_text_24_0align"
                text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                text sprite_section_name xalign 0.1 style "espe_text_heading_36"
                for sprite_name in data.p_displayable_names:
                    text sprite_name style "espe_text_24_0align"

                text "Количество частиц: {}".format(data.p_amount) style "espe_text_24_0align"
                
                text "Время жизни частиц: {:0.2f} секунд".format(data.p_lifetime) style "espe_text_24_0align"
                text "Случайное время жизни частиц: {}".format(espe_get_property_check(data.p_lifetime_random_enable)) style "espe_text_24_0align"
                if data.p_lifetime_random_enable:
                    text "Разброс времени жизни: {:0.0f}%".format(espe_editor_data.p_lifetime_random * 100) style "espe_text_24_0align"
                
                text "Задержка появления частиц: {:0.2f}".format(data.p_lifetime_spread) style "espe_text_24_0align"
                text "Случайная задержка появления частиц: {}".format(espe_get_property_check(data.p_lifetime_random_spread_enable)) style "espe_text_24_0align"
                if data.p_lifetime_random_spread_enable:
                    text "Разброс времени жизни: {:0.0f}%".format(espe_editor_data.p_lifetime_spread_random * 100) style "espe_text_24_0align"
                
                text "Взрывчатость частиц: {}".format(espe_get_property_check(data.p_is_explosiveness)) style "espe_text_24_0align"
                if data.p_is_explosiveness:
                    text "Коэффициент взрывчатости: {:0.0f}%".format(espe_editor_data.p_explosiveness_factor * 100) style "espe_text_24_0align"
                text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                text "Позиционирование" xalign 0.1 style "espe_text_heading_36"
                text "Тип: {}".format(espe_get_position_spawn_type_string()) style "espe_text_24_0align"
                if data.p_spawn_area_type == 0:
                    text "Позиция испускания: X: {}, Y: {}".format(*data.p_emitter_pos) style "espe_text_24_0align"
                elif data.p_spawn_area_type == 1:
                    text "Позиция испускания: X: {}, Y: {}".format(*data.p_rectangle_emitter_pos) style "espe_text_24_0align"
                    text "Размер зоны: Ш: {}, В: {}".format(*data.p_rectangle_spawn_area) style "espe_text_24_0align"
                elif data.p_spawn_area_type == 2:
                    text "Позиция испускания: X: {}, Y: {}".format(*data.p_radial_emitter_pos) style "espe_text_24_0align"
                    text "Радиус зоны: {}".format(data.p_emitter_radius) style "espe_text_24_0align"
                elif data.p_spawn_area_type == 3:
                    text "Размер зоны: Ш: {}, В: {}".format(config.screen_width, config.screen_height) style "espe_text_24_0align"
                elif data.p_spawn_area_type == 4:
                    text "Границы испускания: {}".format(espe_get_emitting_borders()) style "espe_text_24_0align"

                text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                text "Движение" xalign 0.1 style "espe_text_heading_36"
                text "Тип: {}".format(espe_get_movement_type_string()) style "espe_text_24_0align"
                if data.p_move_type == 0:
                    text "Тип без параметров" style "espe_text_24_0align"
                if data.p_move_type == 1:
                    if espe_get_speed_changer_simple_move_type():
                        text "Горизонтальная скорость в диапазоне: {:0.1f}, {:0.1f}".format(data.p_min_x_speed, data.p_max_x_speed - 1000.0) style "espe_text_24_0align"
                        text "Вертикальная скорость в диапазоне: {:0.1f}, {:0.1f}".format(data.p_min_y_speed, data.p_max_y_speed - 1000.0) style "espe_text_24_0align"
                    else:
                        text "Горизонтальная скорость: {:0.1f}".format(data.p_max_x_speed - 1000.0) style "espe_text_24_0align"
                        text "Вертикальная скорость: {:0.1f}".format(data.p_max_y_speed - 1000.0) style "espe_text_24_0align"
                if data.p_move_type == 2:
                    if espe_get_speed_changer_accelerate_move_type():
                        text "Горизонтальная скорость в диапазоне: {:0.1f}, {:0.1f}".format(data.p_min_x_speed - 1000.0, data.p_max_x_speed - 1000.0) style "espe_text_24_0align"
                        text "Вертикальная скорость в диапазоне: {:0.1f}, {:0.1f}".format(data.p_min_y_speed - 1000.0, data.p_max_y_speed - 1000.0) style "espe_text_24_0align"
                    else:
                        text "Горизонтальная скорость: {:0.1f}".format(data.p_max_x_speed) style "espe_text_24_0align"
                        text "Вертикальная скорость: {:0.1f}".format(data.p_max_y_speed) style "espe_text_24_0align"
                    if espe_get_speed_changer_accelerate_move_type():
                        text "Горизонтальное ускорение в диапазоне: {:0.1f}, {:0.1f}".format(data.p_min_x_accelerate - 100.0, data.p_max_x_accelerate - 100.0) style "espe_text_24_0align"
                        text "Вертикальное ускорение в диапазоне: {:0.1f}, {:0.1f}".format(data.p_min_y_accelerate - 100.0, data.p_max_y_accelerate - 100.0) style "espe_text_24_0align"
                    else:
                        text "Горизонтальное ускорение: {:0.1f}".format(data.p_max_x_accelerate - 100.0) style "espe_text_24_0align"
                        text "Вертикальное ускорение: {:0.1f}".format(data.p_max_y_accelerate - 100.0) style "espe_text_24_0align"
                text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                text "Дополнительное движение" xalign 0.1 style "espe_text_heading_36"
                text "Тип: {}".format(espe_get_extra_movement_type_string()) style "espe_text_24_0align"
                if data.p_move_extra_type == 1:
                    if espe_get_speed_changer_extra_move_type():
                        text "Скорость колебания в диапазоне: {:0.1f}, {:0.1f}".format(data.p_min_speed_oscillatory - 1000.0, data.p_max_speed_oscillatory - 1000.0) style "espe_text_24_0align"
                    else:
                        text "Скорость колебания: {:0.1f}".format(data.p_max_speed_oscillatory - 1000.0) style "espe_text_24_0align"
                    if espe_get_radius_oscillatory_changer_type():
                        text "Горизонтальная амплитуда в диапазоне: {:0.1f}, {:0.1f}".format(data.p_min_x_oscillatory, data.p_max_x_oscillatory) style "espe_text_24_0align"
                        text "Вертикальная амплитуда в диапазоне: {:0.1f}, {:0.1f}".format(data.p_min_y_oscillatory, data.p_max_y_oscillatory) style "espe_text_24_0align"
                    else:
                        text "Горизонтальная амплитуда: {:0.1f}".format(data.p_max_x_oscillatory) style "espe_text_24_0align"
                        text "Вертикальная амплитуда: {:0.1f}".format(data.p_max_y_oscillatory) style "espe_text_24_0align"
                    if espe_get_phase_oscillatory_changer_type():
                        text "Начальная фаза в диапазоне: {}°, {}°".format(0, 360) style "espe_text_24_0align"
                    else:
                        text "Начальная фаза: {:0.1f}°".format(data.p_extra_phase) style "espe_text_24_0align"
                text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                if data.psystem_type == "Сложная":
                    text "Прозрачность" xalign 0.1 style "espe_text_heading_36"
                    text "Тип: {}".format(espe_get_alpha_type_string()) style "espe_text_24_0align"
                    if data.p_alpha_type == 0:
                        if espe_get_alpha_transaprency_changer_type():
                            text "Непрозрачность в диапазоне: {:0.0f}%, {:0.0f}%".format(data.p_intermediate_min_alpha * 100, data.p_intermediate_max_alpha * 100) style "espe_text_24_0align"
                        else:
                            text "Непрозрачность: {:0.0f}%".format(data.p_intermediate_max_alpha * 100) style "espe_text_24_0align"
                    elif data.p_alpha_type == 1:
                        if espe_get_alpha_transaprency_fade_in_out_changer_type():
                            text "Непрозрачность в диапазоне: {:0.0f}%, {:0.0f}%".format(data.p_intermediate_min_alpha * 100, data.p_intermediate_max_alpha * 100) style "espe_text_24_0align"
                        else:
                            text "Непрозрачность: {:0.0f}%".format(data.p_intermediate_max_alpha * 100) style "espe_text_24_0align"
                        text "Время появления: {:0.0f}%".format(data.p_alpha_appear_time_percentage * 100) style "espe_text_24_0align"
                        text "Время затухания: {:0.0f}%".format(data.p_alpha_disappear_time_percentage * 100) style "espe_text_24_0align"
                    elif data.p_alpha_type == 2:
                        if espe_get_alpha_transaprency_oscillatory_changer_type():
                            text "Непрозрачность в диапазоне: {:0.0f}%, {:0.0f}%".format(data.p_intermediate_min_alpha * 100, data.p_intermediate_max_alpha * 100) style "espe_text_24_0align"
                        else:
                            text "Непрозрачность: {:0.0f}%".format(data.p_intermediate_max_alpha * 100) style "espe_text_24_0align"
                        if espe_get_alpha_speed_oscillatory_changer_type():
                            text "Скорость колебания в диапазоне: {:0.0f}, {:0.0f}".format(data.p_alpha_min_speed, data.p_alpha_max_speed) style "espe_text_24_0align"
                        else:
                            text "Скорость колебания: {:0.0f}".format(data.p_alpha_max_speed) style "espe_text_24_0align"
                        if espe_get_alpha_phase_oscillatory_changer_type():
                            text "Начальная фаза в диапазоне: {:0.0f}°, {:0.0f}°".format(0, 360) style "espe_text_24_0align"
                        else:
                            text "Начальная фаза: {:0.0f}°".format(data.p_alpha_phase) style "espe_text_24_0align"
                    text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                    text "Масштаб" xalign 0.1 style "espe_text_heading_36"
                    text "Тип: {}".format(espe_get_zoom_type_string()) style "espe_text_24_0align"
                    if data.p_zoom_type == 0:
                        if espe_get_zoom_scale_changer_type():
                            text "Масштаб в диапазоне: {:0.0f}%, {:0.0f}%".format(data.p_intermediate_min_zoom * 100, data.p_intermediate_max_zoom * 100) style "espe_text_24_0align"
                        else:
                            text "Масштаб: {:0.0f}%".format(data.p_intermediate_max_zoom * 100) style "espe_text_24_0align"
                    elif data.p_zoom_type == 1:
                        if espe_get_zoom_scale_fade_in_out_changer_type():
                            text "Масштаб в диапазоне: {:0.0f}%, {:0.0f}%".format(data.p_intermediate_min_zoom * 100, data.p_intermediate_max_zoom * 100) style "espe_text_24_0align"
                        else:
                            text "Масштаб: {:0.0f}%".format(data.p_intermediate_max_zoom * 100) style "espe_text_24_0align"
                        text "Время появления: {:0.0f}%".format(data.p_zoom_appear_time_percentage * 100) style "espe_text_24_0align"
                        text "Время затухания: {:0.0f}%".format(data.p_zoom_disappear_time_percentage * 100) style "espe_text_24_0align"
                    elif data.p_zoom_type == 2:
                        if espe_get_zoom_scale_oscillatory_changer_type():
                            text "Масштаб в диапазоне: {:0.0f}%, {:0.0f}%".format(data.p_intermediate_min_zoom * 100, data.p_intermediate_max_zoom * 100) style "espe_text_24_0align"
                        else:
                            text "Масштаб: {:0.0f}%".format(data.p_intermediate_max_zoom * 100) style "espe_text_24_0align"
                        if espe_get_zoom_speed_oscillatory_changer_type():
                            text "Скорость колебания в диапазоне: {:0.0f}, {:0.0f}".format(data.p_zoom_min_speed, data.p_zoom_max_speed) style "espe_text_24_0align"
                        else:
                            text "Скорость колебания: {:0.0f}".format(data.p_zoom_max_speed) style "espe_text_24_0align"
                        if espe_get_zoom_phase_oscillatory_changer_type():
                            text "Начальная фаза в диапазоне: {:0.0f}°, {:0.0f}°".format(0, 360) style "espe_text_24_0align"
                        else:
                            text "Начальная фаза: {:0.0f}°".format(data.p_zoom_phase) style "espe_text_24_0align"
                    text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                    text "Вращение" xalign 0.1 style "espe_text_heading_36"
                    text "Тип: {}".format(espe_get_rotate_type_string()) style "espe_text_24_0align"
                    if data.p_rotate_type == 0:
                        if espe_get_rotate_static_changer_type():
                            text "Угол в диапазоне: {:0.0f}°, {:0.0f}°".format(data.p_min_angle, data.p_max_angle) style "espe_text_24_0align"
                        else:
                            text "Угол: {:0.0f}°".format(data.p_max_angle) style "espe_text_24_0align"
                    elif data.p_rotate_type == 1:
                        if espe_get_dynamic_rotate_speed_changer_type():
                            text "Скорость вращения в диапазоне: {:0.0f}, {:0.0f}".format(data.p_dynamic_rotate_min_speed - 1000.0, data.p_dynamic_rotate_max_speed - 1000.0) style "espe_text_24_0align"
                        else:
                            text "Скорость вращения: {:0.0f}".format(data.p_dynamic_rotate_max_speed) style "espe_text_24_0align"   
                        if espe_get_dynamic_rotate_angle_changer_type():
                            text "Начальный угол в диапазоне: {:0.0f}°, {:0.0f}°".format(data.p_dynamic_rotate_min_start_angle, data.p_dynamic_rotate_max_start_angle) style "espe_text_24_0align"
                        else:
                            text "Начальный угол: {:0.0f}°".format(data.p_dynamic_rotate_max_start_angle) style "espe_text_24_0align"
                    elif data.p_rotate_type == 2:
                        text "Максимальная скорость {}: {:0.0f}".format(rotate_by_speed_type_name, data.p_rotate_by_speed_max_speed) style "espe_text_24_0align"
                        text "Начальный угол: {:0.0f}°".format(data.p_rotate_by_speed_start_angle) style "espe_text_24_0align"
                    text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                text "Оптимизация" xalign 0.1 style "espe_text_heading_36"
                text "Вычисление времени между кадрами отрисовки: {}".format(espe_get_property_check(data.p_inner_frame_check)) style "espe_text_24_0align"
                text "Время между вызовами функции отрисовки: {:0.3f} секунд".format(data.p_update_time) style "espe_text_24_0align"
                text "Гибель за экраном: {}".format(espe_get_property_check(data.p_is_screen_bounded)) style "espe_text_24_0align"
                text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

    vbar:
        value YScrollValue("psystem_general_data")
        style "espe_scrollbar"
        yalign 0.5
        xalign 0.77
    
    text espe_properties_divider_huge yalign 0.79 xalign 0.5 style "espe_text_heading_36"

    textbutton "Назад" xmaximum 0.2 yalign 0.83 xalign 0.5 style "espe_button" text_style "espe_button_text_36":
        action [Show("ESPE_editor_main_menu"),
                SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_main_menu")]
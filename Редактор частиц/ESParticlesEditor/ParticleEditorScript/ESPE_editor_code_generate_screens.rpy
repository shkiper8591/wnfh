##Экраны с помощью и настройкой генерации кода.##
screen ESPE_generate_psystem_input():
    modal True
    tag espe_editor_main

    $ data = espe_editor_data

    $ is_sprite_one = True if len(data.p_displayable_names) == 1 else False
    $ sprite_section_name = "Спрайт" if is_sprite_one else "Список спрайтов"
    $ rotate_by_speed_type_name = "X" if data.p_rotate_by_speed_type == 0 else "Y"

    default filename_value = ESPECodeGenerator.PSYSTEM_CODE_NAME

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)
    add Solid("#000", xsize=0.3, ysize=0.2) at fast_align_alpha(0.5, 0.9, 0.5)
    add Solid("#000", xsize=0.5, ysize=0.5) at fast_align_alpha(0.5, 0.25, 0.5)

    vbox:
        xalign 0.5
        yalign 0.05

        text "Параметры системы частиц" style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_heading_36"

    fixed:
        area (0.25, 0.125, 0.6, 0.48)
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
                        text "Горизонтальная скорость в диапазоне: {}, {}".format(data.p_min_x_speed - 1000.0, data.p_max_x_speed - 1000.0) style "espe_text_24_0align"
                        text "Вертикальная скорость в диапазоне: {}, {}".format(data.p_min_y_speed - 1000.0, data.p_max_y_speed - 1000.0) style "espe_text_24_0align"
                    else:
                        text "Горизонтальная скорость: {}".format(data.p_max_x_speed - 1000.0) style "espe_text_24_0align"
                        text "Вертикальная скорость: {}".format(data.p_max_y_speed - 1000.0) style "espe_text_24_0align"
                if data.p_move_type == 2:
                    if espe_get_speed_changer_accelerate_move_type():
                        text "Горизонтальная скорость в диапазоне: {}, {}".format(data.p_min_x_speed - 1000.0, data.p_max_x_speed - 1000.0) style "espe_text_24_0align"
                        text "Вертикальная скорость в диапазоне: {}, {}".format(data.p_min_y_speed - 1000.0, data.p_max_y_speed - 1000.0) style "espe_text_24_0align"
                    else:
                        text "Горизонтальная скорость: {}".format(data.p_max_x_speed - 1000.0) style "espe_text_24_0align"
                        text "Вертикальная скорость: {}".format(data.p_max_y_speed - 1000.0) style "espe_text_24_0align"
                    if espe_get_speed_changer_accelerate_move_type():
                        text "Горизонтальное ускорение в диапазоне: {}, {}".format(data.p_min_x_accelerate - 200.0, data.p_max_x_accelerate - 200.0) style "espe_text_24_0align"
                        text "Вертикальное ускорение в диапазоне: {}, {}".format(data.p_min_y_accelerate - 200.0, data.p_max_y_accelerate - 200.0) style "espe_text_24_0align"
                    else:
                        text "Горизонтальное ускорение: {}".format(data.p_max_x_accelerate - 200.0) style "espe_text_24_0align"
                        text "Вертикальное ускорение: {}".format(data.p_max_y_accelerate - 200.0) style "espe_text_24_0align"
                text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                text "Дополнительное движение" xalign 0.1 style "espe_text_heading_36"
                text "Тип: {}".format(espe_get_extra_movement_type_string()) style "espe_text_24_0align"
                if data.p_move_extra_type == 1:
                    if espe_get_speed_changer_extra_move_type():
                        text "Скорость колебания в диапазоне: {}".format(data.p_min_speed_oscillatory - 1000.0, data.p_max_speed_oscillatory - 1000.0) style "espe_text_24_0align"
                    else:
                        text "Скорость колебания: {}".format(data.p_max_speed_oscillatory - 1000.0) style "espe_text_24_0align"
                    if espe_get_radius_oscillatory_changer_type():
                        text "Горизонтальная амплитуда в диапазоне: {}, {}".format(data.p_min_x_oscillatory, data.p_max_x_oscillatory) style "espe_text_24_0align"
                        text "Вертикальная амплитуда в диапазоне: {}, {}".format(data.p_min_y_oscillatory, data.p_max_y_oscillatory) style "espe_text_24_0align"
                    else:
                        text "Горизонтальная амплитуда: {}".format(data.p_max_x_oscillatory) style "espe_text_24_0align"
                        text "Вертикальная амплитуда: {}".format(data.p_max_y_oscillatory) style "espe_text_24_0align"
                    if espe_get_phase_oscillatory_changer_type():
                        text "Начальная фаза в диапазоне: {}°, {}°".format(0, 360) style "espe_text_24_0align"
                    else:
                        text "Начальная фаза: {}°".format(data.p_extra_phase) style "espe_text_24_0align"
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
                            text "Скорость вращения: {:0.0f}".format(data.p_dynamic_rotate_max_speed - 1000.0) style "espe_text_24_0align"   
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
    
    text espe_properties_divider_huge yalign 0.65 xalign 0.5 style "espe_text_heading_36"

    vbox:
        xalign 0.5
        yalign 0.8
        first_spacing 50
        spacing 20

        text "Введите название системы частиц" yoffset 40 xmaximum 0.4 style "espe_text_heading_36"

        input:
            value AdvancedScreenVariableInputValue(variable="filename_value", var_type=str, exclude=None, returnable=False)
            length 24
            xmaximum 0.3
            size 24
            xalign 0.5
            yoffset 60
    
        textbutton "Перейти к настройке генерации" xmaximum 0.3 yoffset 90 style "espe_button" text_style "espe_button_text_36":
            action [SetField(ESPECodeGenerator, "PSYSTEM_CODE_NAME", filename_value),
                    Show("ESPE_generate_psystem_settings")]
        
    textbutton "Назад" yalign 0.98 style "espe_button" text_style "espe_button_text_36":
        action Show("ESPE_editor_main_menu")

screen ESPE_generate_psystem_settings():
    tag espe_editor_main

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)
    add Solid("#000", xsize=0.5, ysize=0.5) at fast_align_alpha(0.5, 0.25, 0.5)

    vbox:
        xalign 0.5
        yalign 0.05

        text "Настройка генерации кода" style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_heading_36"
    
    vbox:
        xanchor 0.5
        xpos 0.5
        ypos 0.185

        # textbutton "Единый файл {}".format(espe_get_property_check(ESPECodeGenerator.SINGLE_FILE)) style "espe_button" text_style "espe_button_text_36":
        #     hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint_code_generate", hint=ESPE_hints_describe_dict["p_code_generate_single_file"]))
        #     unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint_code_generate"))
        #     action [ToggleField(ESPECodeGenerator, "SINGLE_FILE"),
        #             Hide("ESPE_editor_hint_code_generate")]
        
        # text espe_properties_divider_huge style "espe_text_heading_36"

        textbutton "Быстрая математика {}".format(espe_get_property_check(ESPECodeGenerator.GENERATE_FAST_MATH)) style "espe_button" text_style "espe_button_text_36":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint_code_generate", hint=ESPE_hints_describe_dict["p_code_generate_fast_math"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint_code_generate"))
            action [ToggleField(ESPECodeGenerator, "GENERATE_FAST_MATH"),
                    Hide("ESPE_editor_hint_code_generate")]

        text espe_properties_divider_huge style "espe_text_heading_36"

        # textbutton "Функция сброса {}".format(espe_get_property_check(ESPECodeGenerator.GENERATE_PARTICLE_RESET_FUNC)) style "espe_button" text_style "espe_button_text_36":
        #     hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint_code_generate", hint=ESPE_hints_describe_dict["p_code_generate_reset_func"]))
        #     unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint_code_generate"))
        #     action [ToggleField(ESPECodeGenerator, "GENERATE_PARTICLE_RESET_FUNC"),
        #             Hide("ESPE_editor_hint_code_generate")]

        # text espe_properties_divider_huge style "espe_text_heading_36"

        textbutton "Универсальная система {}".format(espe_get_property_check(ESPECodeGenerator.UNIVERSAL_SYSTEM)) style "espe_button" text_style "espe_button_text_36":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint_code_generate", hint=ESPE_hints_describe_dict["p_code_generate_universal_system"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint_code_generate"))
            action [Hide("ESPE_editor_hint_code_generate")]
            #ToggleField(ESPECodeGenerator, "UNIVERSAL_SYSTEM"),  

    text espe_properties_divider_huge yalign 0.79 xalign 0.5 style "espe_text_heading_36"

    hbox:
        xalign 0.5
        yalign 0.83
        spacing 10

        textbutton "Сгенерировать код" style "espe_button" text_style "espe_button_text_36":
            action If(espe_is_psystem_not_exist(ESPECodeGenerator.PSYSTEM_CODE_NAME),
                        true=[Function(espe_generate_psystem, filename=espe_get_system_filename(ESPECodeGenerator.PSYSTEM_CODE_NAME, "")),
                                Show("ESPE_generated_notify"),
                                Show("ESPE_generate_psystem_big_hints", hint=ESPE_hints_describe_dict["p_code_generate_file_location"], image_hint="espe_file_location_hint")],
                        false=Show("ESPE_generate_psystem_exist_caution"))

        textbutton "Назад" style "espe_button" text_style "espe_button_text_36":
            action Show("ESPE_generate_psystem_input")

screen ESPE_generate_psystem_big_hints(hint, image_hint=None):
    tag espe_editor_main

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)
    add Solid("#000", xsize=0.5, ysize=0.5) at fast_align_alpha(0.5, 0.25, 0.5)

    vbox:
        xalign 0.5
        yalign 0.05

        text "Инструкция к использованию" style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_heading_36"

    vbox:
        xanchor 0.5
        xpos 0.5
        ypos 0.15
        xmaximum 0.495

        text hint style "espe_text_24"

    if image_hint is not None:
        add image_hint at fast_pos_05anchor(0.5, 0.46)
    
    text espe_properties_divider_huge ypos 0.64 xalign 0.5 style "espe_text_heading_36"

    hbox:
        xalign 0.5
        yalign 0.7
        spacing 10

        if ESPE_code_generation_list_page < len(ESPE_code_generation_list):
            textbutton "Далее" style "espe_button" text_style "espe_button_text_36":
                    action [SetVariable("ESPE_code_generation_list_page", ESPE_code_generation_list_page + 1),
                            Show("ESPE_generate_psystem_big_hints", hint=ESPE_hints_describe_dict[ESPE_code_generation_list[ESPE_code_generation_list_page]], image_hint=ESPE_code_generation_image_hints_list[ESPE_code_generation_list_page])]

        textbutton "В меню свойств" style "espe_button" text_style "espe_button_text_36":
                action [SetVariable("ESPE_code_generation_list_page", 0),
                        Show("ESPE_editor_main_menu")]

screen ESPE_generate_psystem_exist_caution():
    modal True
    tag espe_editor_main

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)
    add Solid("#000", xsize=0.3, ysize=0.2) at fast_align_alpha(0.5, 0.5, 0.5)

    text "Такое название системы частиц уже используется! Вам следует назвать её по другому." xmaximum 0.3 xalign 0.5 yalign 0.5 style "espe_text_heading_36"

    text espe_properties_divider_huge yalign 0.625 xalign 0.5 style "espe_text_heading_36"

    hbox:
        xalign 0.5
        yalign 0.655
        spacing 10

        textbutton "К вводу названия" xmaximum 0.3 style "espe_button" text_style "espe_button_text_36":
            action [Show("ESPE_generate_psystem_input")]

screen ESPE_generated_notify():
    tag espe_generated_notify

    add Solid("#000", xsize=0.3, ysize=0.1) at fast_align_alpha(0.5, 0.5, 0.5)

    text "Сгенерировано!" xmaximum 0.3 style "espe_text_heading_36" at fast_align(0.5, 0.5)

    timer 1.5 action Hide("ESPE_generated_notify", transition=Dissolve(0.5))

##Экраны для сохранения и загрузки системы частиц.##
screen ESPE_load_psystem_choice():
    tag espe_editor_main

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)
    add Solid("#000", xsize=0.5, ysize=0.5) at fast_align_alpha(0.5, 0.5, 0.4)

    vbox:
        xalign 0.5
        yalign 0.125

        text "Сохранённые системы частиц" style "espe_text_heading_36"

        text espe_properties_divider_huge style "espe_text_heading_36"

        textbutton "Обновить список" xmaximum 0.3 style "espe_button" text_style "espe_button_text_36":
            action Function(espe_list_psystem_files)
    fixed:
        area (0.25, 0.26, 0.49, 0.48)
        viewport id "psystem_files":
            xalign 0.05
            xoffset 10
            draggable True
            mousewheel True
            scrollbars None

            has vbox:
                for filename, filepath in espe_psystem_saves_dict.items():
                    hbox:
                        spacing 5
                        text filename style "espe_text_24"
                        text ">>" style "espe_text_24"
                        textbutton "Загрузить" style "espe_button" text_style "espe_button_text_24":
                            action [SetVariable("espe_special_label_data", filepath), Jump("ESPE_load_psystem_from_file")]
                        text "|" style "espe_text_24"
                        textbutton "Информация" style "espe_button" text_style "espe_button_text_24":
                            action Show("ESPE_load_psystem_view", file_data=espe_get_data_from_psystem_file(filepath=filepath))
    
    vbar:
        value YScrollValue("psystem_files")
        style "espe_scrollbar"
        yalign 0.5
        xalign 0.77

    text espe_properties_divider_huge yalign 0.79 xalign 0.5 style "espe_text_heading_36"

    textbutton "Назад" yalign 0.83 xalign 0.5 style "espe_button" text_style "espe_button_text_36":
        action Show("ESPE_editor_main_menu")

screen ESPE_load_psystem_view(file_data):
    tag espe_editor_main

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)

    if file_data is None:
        add Solid("#000", xsize=0.5, ysize=0.2) at fast_align_alpha(0.5, 0.5, 0.4)

        text "Не удалось прочитать файл!" xalign 0.5 yalign 0.5 style "espe_text_heading_36"

        textbutton "Назад" xalign 0.5 yalign 0.6 style "espe_button" text_style "espe_button_text_36":
                action Show("ESPE_load_psystem_choice")

    ##Damn.##
    else:
        $ data = file_data
        $ filename = data[0]
        $ editor_data = data[1]
        $ name_data = data[2]
        $ sprites_data = data[3]
        $ amount_data = data[4]
        $ lifetime_data = data[5]
        $ explosiveness_data = data[6]
        $ emitter_type_data = data[7]
        $ movement_data = data[8]
        $ extra_movement_data = data[9]
        $ alpha_data = data[10]
        $ scale_data = data[11]
        $ rotate_data = data[12]
        $ optimization_data = data[13]

        $ is_sprite_one = True if len(sprites_data[1]) == 1 else False
        $ sprite_section_name = "Спрайт" if is_sprite_one else "Список спрайтов"
        $ rotate_by_speed_type_name = "X" if rotate_data[10] == 0 else "Y"

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
                    text "Название системы: {}".format(name_data[0]) style "espe_text_24_0align"
                    text "Тип системы: {}".format(editor_data[0]) style "espe_text_24_0align"
                    text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                    text sprite_section_name xalign 0.1 style "espe_text_heading_36"
                    for sprite_name in sprites_data[1]:
                        text sprite_name style "espe_text_24_0align"
                    text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                    text "Количество частиц: {}".format(amount_data[0]) style "espe_text_24_0align"
                    
                    text "Время жизни частиц: {:0.2f} секунд".format(lifetime_data[0]) style "espe_text_24_0align"
                    text "Случайное время жизни частиц: {}".format(espe_get_property_check(lifetime_data[1])) style "espe_text_24_0align"
                    if lifetime_data[1]:
                        text "Разброс времени жизни: {:0.0f}%".format(lifetime_data[2] * 100) style "espe_text_24_0align"
                    
                    text "Задержка появления частиц: {:0.2f}".format(lifetime_data[3]) style "espe_text_24_0align"
                    text "Случайная задержка появления частиц: {}".format(espe_get_property_check(lifetime_data[4])) style "espe_text_24_0align"
                    if lifetime_data[4]:
                        text "Разброс времени жизни: {:0.0f}%".format(lifetime_data[5] * 100) style "espe_text_24_0align"
                    
                    text "Взрывчатость частиц: {}".format(espe_get_property_check(explosiveness_data[0])) style "espe_text_24_0align"
                    if explosiveness_data[0]:
                        text "Коэффициент взрывчатости: {:0.0f}%".format(explosiveness_data[1] * 100) style "espe_text_24_0align"
                    text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                    text "Позиционирование" xalign 0.1 style "espe_text_heading_36"
                    text "Тип: {}".format(espe_get_position_spawn_type_string(emitter_type_data[0])) style "espe_text_24_0align"
                    if emitter_type_data[0] == 0:
                        text "Позиция испускания: X: {}, Y: {}".format(*emitter_type_data[1]) style "espe_text_24_0align"
                    elif emitter_type_data[0] == 1:
                        text "Позиция испускания: X: {}, Y: {}".format(*emitter_type_data[2]) style "espe_text_24_0align"
                        text "Размер зоны: Ш: {}, В: {}".format(*emitter_type_data[3]) style "espe_text_24_0align"
                    elif emitter_type_data[0] == 2:
                        text "Позиция испускания: X: {}, Y: {}".format(*emitter_type_data[4]) style "espe_text_24_0align"
                        text "Радиус зоны: {}".format(emitter_type_data[5]) style "espe_text_24_0align"
                    elif emitter_type_data[0] == 3:
                        text "Размер зоны: Ш: {}, В: {}".format(config.screen_width, config.screen_height) style "espe_text_24_0align"
                    elif emitter_type_data[0] == 4:
                        text "Границы испускания: {}".format(espe_get_emitting_borders(emitter_type_data[6])) style "espe_text_24_0align"

                    text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                    text "Движение" xalign 0.1 style "espe_text_heading_36"
                    text "Тип: {}".format(espe_get_movement_type_string(movement_data[0])) style "espe_text_24_0align"
                    if movement_data[0] == 0:
                        text "Тип без параметров" style "espe_text_24_0align"
                    if movement_data[0] == 1:
                        if espe_get_speed_changer_simple_move_type(movement_data[1]):
                            text "Горизонтальная скорость в диапазоне: {:0.1f}, {:0.1f}".format(movement_data[5], movement_data[4]) style "espe_text_24_0align"
                            text "Вертикальная скорость в диапазоне: {:0.1f}, {:0.1f}".format(movement_data[7], movement_data[6]) style "espe_text_24_0align"
                        else:
                            text "Горизонтальная скорость: {:0.1f}".format(movement_data[4]) style "espe_text_24_0align"
                            text "Вертикальная скорость: {:0.1f}".format(movement_data[6]) style "espe_text_24_0align"
                    if movement_data[0] == 2:
                        if espe_get_speed_changer_accelerate_move_type(movement_data[2]):
                            text "Горизонтальная скорость в диапазоне: {:0.1f}, {:0.1f}".format(movement_data[5], movement_data[4]) style "espe_text_24_0align"
                            text "Вертикальная скорость в диапазоне: {:0.1f}, {:0.1f}".format(movement_data[7], movement_data[6]) style "espe_text_24_0align"
                        else:
                            text "Горизонтальная скорость: {:0.1f}".format(movement_data[4]) style "espe_text_24_0align"
                            text "Вертикальная скорость: {:0.1f}".format(movement_data[6]) style "espe_text_24_0align"
                        if espe_get_speed_changer_accelerate_move_type(movement_data[3]):
                            text "Горизонтальное ускорение в диапазоне: {:0.1f}, {:0.1f}".format(movement_data[9], movement_data[8]) style "espe_text_24_0align"
                            text "Вертикальное ускорение в диапазоне: {:0.1f}, {:0.1f}".format(movement_data[11], movement_data[10]) style "espe_text_24_0align"
                        else:
                            text "Горизонтальное ускорение: {:0.1f}".format(movement_data[8]) style "espe_text_24_0align"
                            text "Вертикальное ускорение: {:0.1f}".format(movement_data[10]) style "espe_text_24_0align"
                    text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                    text "Дополнительное движение" xalign 0.1 style "espe_text_heading_36"
                    text "Тип: {}".format(espe_get_extra_movement_type_string(extra_movement_data[0])) style "espe_text_24_0align"
                    if extra_movement_data[0] == 1:
                        if espe_get_speed_changer_extra_move_type(extra_movement_data[1]):
                            text "Скорость колебания в диапазоне: {:0.1f}, {:0.1f}".format(extra_movement_data[5], extra_movement_data[4]) style "espe_text_24_0align"
                        else:
                            text "Скорость колебания: {:0.1f}".format(extra_movement_data[4]) style "espe_text_24_0align"
                        if espe_get_radius_oscillatory_changer_type(extra_movement_data[2]):
                            text "Горизонтальная амплитуда в диапазоне: {:0.1f}, {:0.1f}".format(extra_movement_data[8], extra_movement_data[7]) style "espe_text_24_0align"
                            text "Вертикальная амплитуда в диапазоне: {:0.1f}, {:0.1f}".format(extra_movement_data[10], extra_movement_data[9]) style "espe_text_24_0align"
                        else:
                            text "Горизонтальная амплитуда: {:0.1f}".format(extra_movement_data[7]) style "espe_text_24_0align"
                            text "Вертикальная амплитуда: {:0.1f}".format(extra_movement_data[9]) style "espe_text_24_0align"
                        if espe_get_phase_oscillatory_changer_type(extra_movement_data[3]):
                            text "Начальная фаза в диапазоне: {}°, {}°".format(0, 360) style "espe_text_24_0align"
                        else:
                            text "Начальная фаза: {:0.1f}°".format(extra_movement_data[6]) style "espe_text_24_0align"
                    text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                    if editor_data[0] == "Сложная":
                        text "Прозрачность" xalign 0.1 style "espe_text_heading_36"
                        text "Тип: {}".format(espe_get_alpha_type_string(alpha_data[0])) style "espe_text_24_0align"
                        if alpha_data[0] == 0:
                            if espe_get_alpha_transaprency_changer_type(alpha_data[1]):
                                text "Непрозрачность в диапазоне: {:0.0f}%, {:0.0f}%".format(alpha_data[7] * 100, alpha_data[6] * 100) style "espe_text_24_0align"
                            else:
                                text "Непрозрачность: {:0.0f}%".format(alpha_data[6] * 100) style "espe_text_24_0align"
                        elif alpha_data[0] == 1:
                            if espe_get_alpha_transaprency_fade_in_out_changer_type(alpha_data[2]):
                                text "Непрозрачность в диапазоне: {:0.0f}%, {:0.0f}%".format(alpha_data[7] * 100, alpha_data[6] * 100) style "espe_text_24_0align"
                            else:
                                text "Непрозрачность: {:0.0f}%".format(alpha_data[6] * 100) style "espe_text_24_0align"
                            text "Время появления: {:0.0f}%".format(alpha_data[8] * 100) style "espe_text_24_0align"
                            text "Время затухания: {:0.0f}%".format(alpha_data[9] * 100) style "espe_text_24_0align"
                        elif alpha_data[0] == 2:
                            if espe_get_alpha_transaprency_oscillatory_changer_type(alpha_data[3]):
                                text "Непрозрачность в диапазоне: {:0.0f}%, {:0.0f}%".format(alpha_data[6] * 100, alpha_data[5] * 100) style "espe_text_24_0align"
                            else:
                                text "Непрозрачность: {:0.0f}%".format(alpha_data[5] * 100) style "espe_text_24_0align"
                            if espe_get_alpha_speed_oscillatory_changer_type(alpha_data[4]):
                                text "Скорость колебания в диапазоне: {:0.0f}, {:0.0f}".format(alpha_data[11], alpha_data[10]) style "espe_text_24_0align"
                            else:
                                text "Скорость колебания: {:0.0f}".format(alpha_data[10]) style "espe_text_24_0align"
                            if espe_get_alpha_phase_oscillatory_changer_type(alpha_data[5]):
                                text "Начальная фаза в диапазоне: {:0.0f}°, {:0.0f}°".format(0, 360) style "espe_text_24_0align"
                            else:
                                text "Начальная фаза: {:0.0f}°".format(alpha_data[12]) style "espe_text_24_0align"
                        text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                        text "Масштаб" xalign 0.1 style "espe_text_heading_36"
                        text "Тип: {}".format(espe_get_alpha_type_string(scale_data[0])) style "espe_text_24_0align"
                        if scale_data[0] == 0:
                            if espe_get_zoom_scale_changer_type(scale_data[1]):
                                text "Масштаб в диапазоне: {:0.0f}%, {:0.0f}%".format(scale_data[7] * 100, scale_data[6] * 100) style "espe_text_24_0align"
                            else:
                                text "Масштаб: {:0.0f}%".format(scale_data[6] * 100) style "espe_text_24_0align"
                        elif scale_data[0] == 1:
                            if espe_get_zoom_scale_fade_in_out_changer_type(scale_data[2]):
                                text "Масштаб в диапазоне: {:0.0f}%, {:0.0f}%".format(scale_data[7] * 100, scale_data[6] * 100) style "espe_text_24_0align"
                            else:
                                text "Масштаб: {:0.0f}%".format(scale_data[6] * 100) style "espe_text_24_0align"
                            text "Время появления: {:0.0f}%".format(scale_data[8] * 100) style "espe_text_24_0align"
                            text "Время затухания: {:0.0f}%".format(scale_data[9] * 100) style "espe_text_24_0align"
                        elif scale_data[0] == 2:
                            if espe_get_zoom_scale_oscillatory_changer_type(scale_data[3]):
                                text "Масштаб в диапазоне: {:0.0f}%, {:0.0f}%".format(scale_data[6] * 100, scale_data[5] * 100) style "espe_text_24_0align"
                            else:
                                text "Масштаб: {:0.0f}%".format(scale_data[5] * 100) style "espe_text_24_0align"
                            if espe_get_zoom_speed_oscillatory_changer_type(scale_data[4]):
                                text "Скорость колебания в диапазоне: {:0.0f}, {:0.0f}".format(scale_data[11], scale_data[10]) style "espe_text_24_0align"
                            else:
                                text "Скорость колебания: {:0.0f}".format(scale_data[10]) style "espe_text_24_0align"
                            if espe_get_zoom_phase_oscillatory_changer_type(scale_data[5]):
                                text "Начальная фаза в диапазоне: {:0.0f}°, {:0.0f}°".format(0, 360) style "espe_text_24_0align"
                            else:
                                text "Начальная фаза: {:0.0f}°".format(scale_data[12]) style "espe_text_24_0align"
                        text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                        text "Вращение" xalign 0.1 style "espe_text_heading_36"
                        text "Тип: {}".format(espe_get_rotate_type_string(rotate_data[0])) style "espe_text_24_0align"
                        if rotate_data[0] == 0:
                            if espe_get_rotate_static_changer_type(rotate_data[1]):
                                text "Угол в диапазоне: {:0.0f}°, {:0.0f}°".format(rotate_data[5], rotate_data[4]) style "espe_text_24_0align"
                            else:
                                text "Угол: {:0.0f}°".format(rotate_data[4]) style "espe_text_24_0align"
                        elif rotate_data[0] == 1:
                            if espe_get_dynamic_rotate_speed_changer_type(rotate_data[2]):
                                text "Скорость вращения в диапазоне: {:0.0f}, {:0.0f}".format(rotate_data[9], rotate_data[8]) style "espe_text_24_0align"
                            else:
                                text "Скорость вращения: {:0.0f}".format(rotate_data[8]) style "espe_text_24_0align"   
                            if espe_get_dynamic_rotate_angle_changer_type(rotate_data[3]):
                                text "Начальный угол в диапазоне: {:0.0f}°, {:0.0f}°".format(rotate_data[7], rotate_data[6]) style "espe_text_24_0align"
                            else:
                                text "Начальный угол: {:0.0f}°".format(rotate_data[6]) style "espe_text_24_0align"
                        elif rotate_data[0] == 2:
                            text "Максимальная скорость {}: {:0.0f}".format(rotate_by_speed_type_name, rotate_data[12]) style "espe_text_24_0align"
                            text "Начальный угол: {:0.0f}°".format(rotate_data[11]) style "espe_text_24_0align"
                        text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                    text "Оптимизация" xalign 0.1 style "espe_text_heading_36"
                    text "Вычисление времени между кадрами отрисовки: {}".format(espe_get_property_check(optimization_data[0])) style "espe_text_24_0align"
                    text "Время между вызовами функции отрисовки: {:0.3f} секунд".format(optimization_data[2]) style "espe_text_24_0align"
                    text "Гибель за экраном: {}".format(espe_get_property_check(optimization_data[3])) style "espe_text_24_0align"
                    text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

        vbar:
            value YScrollValue("psystem_general_data")
            style "espe_scrollbar"
            yalign 0.5
            xalign 0.77
                
        text espe_properties_divider_huge yalign 0.79 xalign 0.5 style "espe_text_heading_36"

        hbox:
            xalign 0.5
            yalign 0.83
            spacing 10

            textbutton "Загрузить систему частиц" style "espe_button" text_style "espe_button_text_36":
                action [Show("ESPE_editor_main_menu"), Function(espe_load_psystem_from_data, data=data, _update_screens=False),
                        Show("ESPE_saved_loaded_notify", is_save=False)]

            textbutton "Назад" style "espe_button" text_style "espe_button_text_36":
                action Show("ESPE_load_psystem_choice")

screen ESPE_load_psystem_fail():
    tag espe_editor_main

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)
    add Solid("#000", xsize=0.5, ysize=0.96) at fast_align_alpha(0.5, 1.0, 0.5)

    text "Не удалось открыть файл системы частиц!\nФайл повреждён или содержит неправильный синтаксис для анализа." xmaximum 0.5 style "espe_text_heading_36" at fast_align(0.5, 0.5)

    textbutton "Назад" yalign 0.96 xalign 0.5 style "espe_button" text_style "espe_button_text_36":
        action Show("ESPE_load_psystem_choice")

screen ESPE_save_psystem_input(def_name=None):
    modal True
    tag espe_editor_main

    $ data = espe_editor_data

    $ is_sprite_one = True if len(data.p_displayable_names) == 1 else False
    $ sprite_section_name = "Спрайт" if is_sprite_one else "Список спрайтов"
    $ rotate_by_speed_type_name = "X" if data.p_rotate_by_speed_type == 0 else "Y"

    default filename_value = data.psystem_name if def_name is None else def_name

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

        text "Введите название системы частиц" xmaximum 0.4 style "espe_text_heading_36"

        input:
            value AdvancedScreenVariableInputValue(variable="filename_value", var_type=str, exclude=None, returnable=False)
            length 24
            xmaximum 0.3
            size 24
            xalign 0.5
            yoffset 60

        textbutton "Сохранить" xmaximum 0.3 yoffset 90 style "espe_button" text_style "espe_button_text_36":
            action [Hide("ESPE_save_psystem_input"),
                    If(espe_check_file_on_exist(filename_value, espe_psystem_saves_dict),
                        true=Show("ESPE_save_psystem_exist_caution", stored_name=filename_value),
                        false=[Function(espe_save_psystem, filename=filename_value), Show("ESPE_editor_main_menu"), Show("ESPE_saved_loaded_notify", is_save=True)])]
        
    textbutton "Назад" yalign 0.98 style "espe_button" text_style "espe_button_text_36":
        action Show("ESPE_editor_main_menu")

screen ESPE_save_psystem_exist_caution(stored_name):
    modal True
    tag espe_editor_main

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)
    add Solid("#000", xsize=0.3, ysize=0.2) at fast_align_alpha(0.5, 0.5, 0.5)

    text "Такое название системы частиц уже используется! Перезаписать файл?" xmaximum 0.3 xalign 0.5 yalign 0.5 style "espe_text_heading_36"

    text espe_properties_divider_huge yalign 0.625 xalign 0.5 style "espe_text_heading_36"

    hbox:
        xalign 0.5
        yalign 0.655
        spacing 10

        textbutton "Перезаписать" xmaximum 0.3 style "espe_button" text_style "espe_button_text_36":
            action [Function(espe_save_psystem, filename=stored_name), Show("ESPE_editor_main_menu"), Show("ESPE_saved_loaded_notify", is_save=True)]

        textbutton "Назад" xmaximum 0.3 style "espe_button" text_style "espe_button_text_36":
            action Show("ESPE_save_psystem_input", def_name=stored_name)
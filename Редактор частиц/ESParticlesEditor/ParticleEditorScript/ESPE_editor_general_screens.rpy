##Основные экраны (заглушка, выбор частиц, выбор раздела свойств).##
screen ESPE_screen_holder():
    add Null()

screen ESPE_editor_menu_startup():
    tag espe_editor_main

    add Solid("#000", xsize=0.2, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.1, 0.07)

        text "Тип частиц" xalign 0.5 style "espe_text_heading_36" size 32
        text espe_properties_divider_huge style "espe_text_24"

    vbox:
        at fast_pos_05anchor(0.1, 0.5)

        textbutton "Простые частицы" xmaximum 0.2 style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_simple"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Show("ESPE_editor_simple_particles_show"), Show("ESPE_editor_main_menu"),
                    Show("ESPE_psystem_type_notify", simple=True),
                    SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_main_menu"),
                    Function(espe_set_simple_particle_system),
                    Hide("ESPE_editor_hint")]

        text espe_properties_divider style "espe_text_24"
        
        textbutton "Сложные частицы" xmaximum 0.2 style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_complex"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Show("ESPE_editor_complex_particles_show"), Show("ESPE_editor_main_menu"),
                    Show("ESPE_psystem_type_notify", simple=False),
                    SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_main_menu"),
                    Function(espe_set_complex_particle_system),
                    Hide("ESPE_editor_hint")]

screen ESPE_editor_main_menu():
    tag espe_editor_main

    add Solid("#000", xsize=0.2, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)
    vbox:
        at fast_pos_05anchor(0.1, 0.07)

        text "Свойства" xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"
    vbox:
        at fast_pos_05anchor(0.1, 0.55)

        textbutton "Основные свойства" style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_main_properties"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Show("ESPE_editor_main_properties"),
                    Hide("ESPE_editor_hint"),
                    SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_main_properties")]
        
        text espe_properties_divider style "espe_text_24"

        textbutton "Позиционирование" style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_spawn_properties"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Show("ESPE_editor_position_properties"),
                    Hide("ESPE_editor_hint"),
                    SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_position_properties")]

        text espe_properties_divider style "espe_text_24"

        textbutton "Движение" style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_move_properties"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Show("ESPE_editor_movement_properties"),
                    Hide("ESPE_editor_hint"),
                    SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_movement_properties")]

        text espe_properties_divider style "espe_text_24"

        textbutton "Непрозрачность" style "espe_button" text_style "espe_button_text_24":
            sensitive espe_editor_data.psystem_type == "Сложная"
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_alpha_properties"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Show("ESPE_editor_alpha_properties"),
                    Hide("ESPE_editor_hint"),
                    SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_alpha_properties")]

        text espe_properties_divider style "espe_text_24"

        textbutton "Масштабирование" style "espe_button" text_style "espe_button_text_24":
            sensitive espe_editor_data.psystem_type == "Сложная"
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_zoom_properties"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Show("ESPE_editor_zoom_properties"),
                    Hide("ESPE_editor_hint"),
                    SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_zoom_properties")]

        text espe_properties_divider style "espe_text_24"

        textbutton "Вращение" style "espe_button" text_style "espe_button_text_24":
            sensitive espe_editor_data.psystem_type == "Сложная"
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_rotate_properties"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Show("ESPE_editor_rotate_properties"),
                    Hide("ESPE_editor_hint"),
                    SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_rotate_properties")]

        text espe_properties_divider style "espe_text_24"

        textbutton "Оптимизация" style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_optimization_properties"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Show("ESPE_editor_optimization_properties"),
                    Hide("ESPE_editor_hint"),
                    SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_optimization_properties")]
        
        text espe_properties_divider_huge style "espe_text_24"

        textbutton "Информация о системе" style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_particle_system_general_data"),
                    SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_particle_system_general_data")]

        text espe_properties_divider_huge style "espe_text_24"

        textbutton "Сохранить систему частиц" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            action Show("ESPE_save_psystem_input")

        textbutton "Загрузить систему частиц" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            action [Function(espe_list_psystem_files), Show("ESPE_load_psystem_choice")]

        text espe_properties_divider_huge style "espe_text_24"

        textbutton "Сгенерировать код" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_code_generate"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    Show("ESPE_generate_psystem_input")]
        
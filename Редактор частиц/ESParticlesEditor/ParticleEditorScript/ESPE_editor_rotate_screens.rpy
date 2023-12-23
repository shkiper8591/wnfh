##Экраны раздела "Позиционирование".##
screen ESPE_editor_rotate_properties():
    tag espe_editor_main

    $ editor_data = espe_editor_data

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.125, 0.07)

        text "Вращение" xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"
    
    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.1
        spacing -7

        textbutton "Постоянный угол " + espe_get_property_radiobutton(editor_data.p_rotate_type, 0) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_rotate_static"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_rotate_type", 0),
                    Function(espe_set_static_rotate)]
        
        text espe_properties_divider style "espe_text_24"

        textbutton "Динамическое вращение " + espe_get_property_radiobutton(editor_data.p_rotate_type, 1) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_rotate_dynamic"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_rotate_type", 1),
                    Function(espe_set_dynamic_rotate)]
        
        text espe_properties_divider style "espe_text_24"

        textbutton "Зависимость от скорости " + espe_get_property_radiobutton(editor_data.p_rotate_type, 2) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_rotate_by_speed"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_rotate_type", 2),
                    Function(espe_set_rotate_by_speed)]
        
        text espe_properties_divider style "espe_text_24"
    
    if editor_data.p_rotate_type == 0:
        use ESPE_static_rotate_subscreen()
    elif editor_data.p_rotate_type == 1:
        use ESPE_dynamic_rotate_subscreen()
    elif editor_data.p_rotate_type == 2:
        use ESPE_rotate_by_speed_subscreen()

    textbutton "Назад" style "espe_button" text_style "espe_button_text_36" at fast_pos_05anchor(0.125, 0.95):
        mouse "ESPE_cursor_choice"
        action [Show("ESPE_editor_main_menu"),
                SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_main_menu")]

screen ESPE_static_rotate_subscreen():
    tag espe_pos_subscreen
    zorder 10

    $ editor_data = espe_editor_data
    $ if_range_rotate_string = "Значение" if not editor_data.p_rotate_changer_static_type else "Значение 1"

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.39

        text espe_properties_divider_huge style "espe_text_24"
    
    grid 1 6:
        xanchor 0.5
        xpos 0.125
        ypos 0.46
        spacing -5

        text "Угол" style "espe_text_heading_24"
        textbutton "Диапазон угла {}".format(espe_get_property_check(editor_data.p_rotate_changer_static_type)) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_angle_range"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [ToggleField(espe_editor_data, "p_rotate_changer_static_type"),
                    Function(espe_static_rotate_update),
                    Hide("ESPE_editor_hint")
                    ]
        textbutton "{}: {:0.0f}°".format(if_range_rotate_string, editor_data.psystem_object.max_angle) style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_editor_input", obj=editor_data, field="p_max_angle", field_type=float, clamp_range=(0.0, 360.0), max_length=5,
                        exclude=espe_input_exclude_letters,
                        force_update_attr_func=espe_update_rotate_static_angle)]
        bar:
            value FieldValue(espe_editor_data, "p_max_angle", 360.0, step=1.0,
                            action=Function(espe_update_rotate_static_angle))
            style "espe_property_bar"
            xsize 0.18

        textbutton "Значение 2: {:0.0f}°".format(editor_data.psystem_object.min_angle) style "espe_button" text_style "espe_button_text_24":
            sensitive editor_data.p_rotate_changer_static_type
            action [Show("ESPE_editor_input", obj=editor_data, field="p_min_angle", field_type=float, clamp_range=(0.0, 360.0), max_length=5,
                        exclude=espe_input_exclude_letters,
                        force_update_attr_func=espe_update_rotate_static_angle)]
        
        if editor_data.p_rotate_changer_static_type:
            bar:
                value FieldValue(espe_editor_data, "p_min_angle", 360.0, step=1.0,
                                action=Function(espe_update_rotate_static_angle))
                style "espe_property_bar"
                xsize 0.18
        else:
            bar:
                value StaticValue(espe_editor_data.p_min_angle, 360.0)
                style "espe_property_inactive_bar"
                xsize 0.18

screen ESPE_dynamic_rotate_subscreen():
    tag espe_pos_subscreen
    zorder 10

    $ editor_data = espe_editor_data
    $ if_range_speed_string = "Значение" if not editor_data.p_dynamic_rotate_changer_speed_type else "Значение 1"
    $ if_range_rotate_string = "Значение" if not editor_data.p_dynamic_rotate_changer_angle_type else "Значение 1"

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.39

        text espe_properties_divider_huge style "espe_text_24"
    
    fixed:
        area (0.0, 0.46, 0.25, 0.436)
        viewport id "dynamic_rotate_prop":
            draggable True
            mousewheel True
            scrollbars None

            has grid 1 14:
                xanchor 0.5
                xpos 0.125
                ypos 0.46
                spacing -5

                text "Скорость вращения" style "espe_text_heading_24"
                textbutton "Диапазон скорости {}".format(espe_get_property_check(editor_data.p_dynamic_rotate_changer_speed_type)) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_rotate_speed_range"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [ToggleField(espe_editor_data, "p_dynamic_rotate_changer_speed_type"),
                            Function(espe_dynamic_rotate_speed_update),
                            Hide("ESPE_editor_hint")
                            ]
                textbutton "{}: {:0.0f}".format(if_range_speed_string, editor_data.psystem_object.dynamic_rotate_max_speed) style "espe_button" text_style "espe_button_text_24":
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_dynamic_rotate_max_speed", field_type=float, additional_value=1000.0, clamp_range=(-1000.0, 1000.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_dynamic_rotate_speed_update)]
                bar:
                    value FieldValue(espe_editor_data, "p_dynamic_rotate_max_speed", 2000.0, step=1.0,
                                    action=Function(espe_update_dynamic_rotate_speed))
                    style "espe_property_bar"

                textbutton "Значение 2: {:0.0f}".format(editor_data.psystem_object.dynamic_rotate_min_speed) style "espe_button" text_style "espe_button_text_24":
                    sensitive editor_data.p_dynamic_rotate_changer_speed_type
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_dynamic_rotate_min_speed", field_type=float, additional_value=1000.0, clamp_range=(-1000.0, 1000.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_dynamic_rotate_speed)]
                
                if editor_data.p_dynamic_rotate_changer_speed_type:
                    bar:
                        value FieldValue(espe_editor_data, "p_dynamic_rotate_min_speed", 2000.0, step=1.0,
                                        action=Function(espe_update_dynamic_rotate_speed))
                        style "espe_property_bar"
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_dynamic_rotate_min_speed, 2000.0)
                        style "espe_property_inactive_bar"

                text espe_properties_divider_huge style "espe_text_24"

                text "Начальный yгол" style "espe_text_heading_24"
                textbutton "Диапазон угла {}".format(espe_get_property_check(editor_data.p_dynamic_rotate_changer_angle_type)) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_start_angle_range"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [ToggleField(espe_editor_data, "p_dynamic_rotate_changer_angle_type"),
                            Function(espe_dynamic_rotate_start_angle_update),
                            Hide("ESPE_editor_hint")
                            ]
                textbutton "{}: {:0.0f}°".format(if_range_rotate_string, editor_data.psystem_object.dynamic_rotate_max_start_angle) style "espe_button" text_style "espe_button_text_24":
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_dynamic_rotate_max_start_angle", field_type=float, clamp_range=(0.0, 360.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_dynamic_rotate_start_angle)]
                bar:
                    value FieldValue(espe_editor_data, "p_dynamic_rotate_max_start_angle", 360.0, step=1.0,
                                    action=Function(espe_update_dynamic_rotate_start_angle))
                    style "espe_property_bar"

                textbutton "Значение 2: {:0.0f}°".format(editor_data.psystem_object.dynamic_rotate_min_start_angle) style "espe_button" text_style "espe_button_text_24":
                    sensitive editor_data.p_dynamic_rotate_changer_angle_type
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_dynamic_rotate_min_start_angle", field_type=float, clamp_range=(0.0, 360.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_dynamic_rotate_start_angle)]
                
                if editor_data.p_dynamic_rotate_changer_angle_type:
                    bar:
                        value FieldValue(espe_editor_data, "p_dynamic_rotate_min_start_angle", 360.0, step=1.0,
                                        action=Function(espe_update_dynamic_rotate_start_angle))
                        style "espe_property_bar"
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_dynamic_rotate_min_start_angle, 360.0)
                        style "espe_property_inactive_bar"
        
            add Null(width=480)

    vbar:
        value YScrollValue("dynamic_rotate_prop")
        style "espe_scrollbar"
        yalign 0.5

screen ESPE_rotate_by_speed_subscreen():
    tag espe_pos_subscreen
    zorder 10

    $ editor_data = espe_editor_data
    $ speed_type = "X" if editor_data.p_rotate_by_speed_type == 0 else "Y"

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.39

        text espe_properties_divider_huge style "espe_text_24"
    
    fixed:
        area (0.0, 0.46, 0.25, 0.436)
        viewport id "rotate_by_speed_prop":
            draggable True
            mousewheel True
            scrollbars None

            has grid 1 11:
                xanchor 0.5
                xpos 0.125
                ypos 0.46
                spacing -5

                textbutton "Горизонтальная скорость " + espe_get_property_radiobutton(editor_data.p_rotate_by_speed_type, 0) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_rotate_by_speed_x_speed"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [Hide("ESPE_editor_hint"),
                            SetField(editor_data, "p_rotate_by_speed_type", 0),
                            Function(espe_rotate_by_speed_speed_type_update, update_processes=True)]

                textbutton "Вертикальная скорость " + espe_get_property_radiobutton(editor_data.p_rotate_by_speed_type, 1) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_rotate_by_speed_y_speed"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [Hide("ESPE_editor_hint"),
                            SetField(editor_data, "p_rotate_by_speed_type", 1),
                            Function(espe_rotate_by_speed_speed_type_update, update_processes=True)]

                text espe_properties_divider_huge style "espe_text_24"

                text "Базовый угол" style "espe_text_heading_24"
                textbutton "Значение: {:0.0f}°".format(editor_data.psystem_object.rotate_by_speed_start_angle) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_rotate_base_angle"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [Hide("ESPE_editor_hint"),
                            Show("ESPE_editor_input", obj=editor_data, field="p_rotate_by_speed_start_angle", field_type=float, clamp_range=(0.0, 360.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_rotate_by_speed_start_angle)
                                ]
                bar:
                    value FieldValue(espe_editor_data, "p_rotate_by_speed_start_angle", 360.0, step=1.0,
                                    action=Function(espe_update_rotate_by_speed_start_angle))
                    style "espe_property_bar"

                text espe_properties_divider_huge style "espe_text_24"

                text "Максимальная скорость" style "espe_text_heading_24"
                textbutton "Значение {}: {:0.0f}".format(speed_type, editor_data.psystem_object.rotate_by_speed_max_speed) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_rotate_by_speed_max_speed"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [Hide("ESPE_editor_hint"),
                            Show("ESPE_editor_input", obj=editor_data, field="p_rotate_by_speed_max_speed", field_type=float, additional_value=1000.0, clamp_range=(-1000.0, 1000.0), max_length=5,
                            exclude=espe_input_exclude_letters,
                            force_update_attr_func=espe_update_rotate_by_speed_max_min_speed)]
                bar:
                    value FieldValue(espe_editor_data, "p_rotate_by_speed_max_speed", 2000.0, step=1.0,
                                    action=Function(espe_update_rotate_by_speed_max_min_speed))
                    style "espe_property_bar"

            add Null(width=480)

    vbar:
        value YScrollValue("rotate_by_speed_prop")
        style "espe_scrollbar"
        yalign 0.5
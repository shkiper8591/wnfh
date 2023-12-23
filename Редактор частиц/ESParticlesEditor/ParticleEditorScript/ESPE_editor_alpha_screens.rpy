##Экраны раздела "Прозрачность".##
screen ESPE_editor_alpha_properties():
    tag espe_editor_main

    $ editor_data = espe_editor_data

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.125, 0.07)

        text "Непрозрачность" xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"
    
    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.1
        spacing -7

        textbutton "Постоянная непрозрачность " + espe_get_property_radiobutton(editor_data.p_alpha_type, 0) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_alpha_static"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_alpha_type", 0),
                    Function(espe_set_static_alpha)]
        
        text espe_properties_divider style "espe_text_24"

        textbutton "Появление/затухание " + espe_get_property_radiobutton(editor_data.p_alpha_type, 1) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_alpha_fade_in_out"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_alpha_type", 1),
                    Function(espe_set_fade_in_out_alpha)]
        
        text espe_properties_divider style "espe_text_24"

        textbutton "Колебательная прозрачность " + espe_get_property_radiobutton(editor_data.p_alpha_type, 2) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_alpha_oscillatory"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_alpha_type", 2),
                    Function(espe_set_oscillatory_alpha)]
        
        text espe_properties_divider style "espe_text_24"
    
    if editor_data.p_alpha_type == 0:
        use ESPE_static_alpha_subscreen()
    elif editor_data.p_alpha_type == 1:
        use ESPE_fade_in_out_alpha_subscreen()
    elif editor_data.p_alpha_type == 2:
        use ESPE_oscillatory_subscreen()

    textbutton "Назад" style "espe_button" text_style "espe_button_text_36" at fast_pos_05anchor(0.125, 0.95):
        mouse "ESPE_cursor_choice"
        action [Show("ESPE_editor_main_menu"),
                SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_main_menu")]

screen ESPE_static_alpha_subscreen():
    tag espe_pos_subscreen
    zorder 10

    $ editor_data = espe_editor_data
    $ if_range_alpha_string = "Значение" if not editor_data.p_alpha_changer_static_type else "Значение 1"

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

        text "Непрозрачность" style "espe_text_heading_24"
        textbutton "Диапазон непрозрачности {}".format(espe_get_property_check(editor_data.p_alpha_changer_static_type)) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_alpha_range"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [ToggleField(espe_editor_data, "p_alpha_changer_static_type"),
                    Function(espe_static_alpha_update),
                    Hide("ESPE_editor_hint")
                    ]
        textbutton "{}: {:0.0f}%".format(if_range_alpha_string, editor_data.psystem_object.intermediate_max_alpha * 100) style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_editor_input", obj=editor_data, field="p_intermediate_max_alpha", field_type=float, multiplie_value=100.0, clamp_range=(0, 100.0), max_length=5,
                        exclude=espe_input_exclude_letters,
                        force_update_attr_func=espe_update_alpha)]
        bar:
            value FieldValue(espe_editor_data, "p_intermediate_max_alpha", 1.0, step=1.0,
                            action=Function(espe_update_alpha))
            style "espe_property_bar"
            xsize 0.18

        textbutton "Значение 2: {:0.0f}%".format(editor_data.psystem_object.intermediate_min_alpha * 100) style "espe_button" text_style "espe_button_text_24":
            sensitive editor_data.p_alpha_changer_static_type
            action [Show("ESPE_editor_input", obj=editor_data, field="p_intermediate_min_alpha", field_type=float, multiplie_value=100.0, clamp_range=(0, 100.0), max_length=5,
                        exclude=espe_input_exclude_letters,
                        force_update_attr_func=espe_update_alpha)]
        
        if editor_data.p_alpha_changer_static_type:
            bar:
                value FieldValue(espe_editor_data, "p_intermediate_min_alpha", 1.0, step=1.0,
                                action=Function(espe_update_alpha))
                style "espe_property_bar"
                xsize 0.18
        else:
            bar:
                value StaticValue(espe_editor_data.p_intermediate_min_alpha, 1.0)
                style "espe_property_inactive_bar"
                xsize 0.18

screen ESPE_fade_in_out_alpha_subscreen():
    tag espe_pos_subscreen
    zorder 10

    $ editor_data = espe_editor_data
    $ if_range_alpha_string = "Значение" if not editor_data.p_alpha_changer_static_type else "Значение 1"

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.39

        text espe_properties_divider_huge style "espe_text_24"
    
    fixed:
        area (0.0, 0.46, 0.25, 0.436)
        viewport id "alpha_fade_in_out_prop":
            draggable True
            mousewheel True
            scrollbars None

            has grid 1 15:
                spacing -5

                text "Непрозрачность" style "espe_text_heading_24"
                textbutton "Диапазон непрозрачности {}".format(espe_get_property_check(editor_data.p_alpha_changer_fade_in_out_type)) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_alpha_range"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [ToggleField(espe_editor_data, "p_alpha_changer_fade_in_out_type"),
                            Function(espe_alpha_fade_in_out_update),
                            Hide("ESPE_editor_hint")
                            ]
                textbutton "{}: {:0.0f}%".format(if_range_alpha_string, editor_data.psystem_object.intermediate_max_alpha * 100) style "espe_button" text_style "espe_button_text_24":
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_intermediate_max_alpha", field_type=float, multiplie_value=100.0, clamp_range=(0, 100.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_alpha)]
                bar:
                    value FieldValue(espe_editor_data, "p_intermediate_max_alpha", 1.0, step=1.0,
                                    action=Function(espe_update_alpha))
                    style "espe_property_bar"

                textbutton "Значение 2: {:0.0f}%".format(editor_data.psystem_object.intermediate_min_alpha * 100) style "espe_button" text_style "espe_button_text_24":
                    sensitive editor_data.p_alpha_changer_fade_in_out_type
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_intermediate_min_alpha", field_type=float, multiplie_value=100.0, clamp_range=(0, 100.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_alpha)]
                
                if editor_data.p_alpha_changer_fade_in_out_type:
                    bar:
                        value FieldValue(espe_editor_data, "p_intermediate_min_alpha", 1.0, step=1.0,
                                        action=Function(espe_update_alpha))
                        style "espe_property_bar"
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_intermediate_min_alpha, 1.0)
                        style "espe_property_inactive_bar"
                
                text espe_properties_divider_huge style "espe_text_24"

                text "Время появления" style "espe_text_heading_24"
                textbutton "{}: {:0.0f}%".format(if_range_alpha_string, editor_data.psystem_object.alpha_appear_time_percentage * 100) style "espe_button" text_style "espe_button_text_24":
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_alpha_appear_time_percentage", field_type=float, multiplie_value=100.0, clamp_range=(0, 100.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_safe_update_time_alpha)]
                bar:
                    value FieldValue(espe_editor_data, "p_alpha_appear_time_percentage", 1.0, step=1.0,
                                    action=Function(espe_safe_update_time_alpha))
                    style "espe_property_bar"

                text espe_properties_divider style "espe_text_24"

                text "Время затухания" style "espe_text_heading_24"
                textbutton "{}: {:0.0f}%".format(if_range_alpha_string, editor_data.psystem_object.alpha_disappear_time_percentage * 100) style "espe_button" text_style "espe_button_text_24":
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_alpha_disappear_time_percentage", field_type=float, multiplie_value=100.0, clamp_range=(0, 100.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_safe_update_time_alpha)]
                bar:
                    value FieldValue(espe_editor_data, "p_alpha_disappear_time_percentage", 1.0, step=1.0,
                                    action=Function(espe_safe_update_time_alpha))
                    style "espe_property_bar"

            add Null(width=480)

    vbar:
        value YScrollValue("alpha_fade_in_out_prop")
        style "espe_scrollbar"
        yalign 0.5

screen ESPE_oscillatory_subscreen():
    tag espe_pos_subscreen
    zorder 10

    $ editor_data = espe_editor_data
    $ if_range_alpha_string = "Значение" if not editor_data.p_alpha_changer_static_type else "Значение 1"
    $ if_range_alpha_speed = "Значение" if not editor_data.p_alpha_changer_oscillatory_speed_type else "Значение 1"

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.39

        text espe_properties_divider_huge style "espe_text_24"
    
    fixed:
        area (0.0, 0.46, 0.25, 0.436)
        viewport id "alpha_oscillatory_prop":
            draggable True
            mousewheel True
            scrollbars None

            has grid 1 19:
                spacing -5

                text "Непрозрачность" style "espe_text_heading_24"
                textbutton "Диапазон непрозрачности {}".format(espe_get_property_check(editor_data.p_alpha_changer_oscillatory_type)) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_alpha_range"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [ToggleField(espe_editor_data, "p_alpha_changer_oscillatory_type"),
                            Function(espe_alpha_oscillatory_update),
                            Hide("ESPE_editor_hint")
                            ]
                textbutton "{}: {:0.0f}%".format(if_range_alpha_string, editor_data.psystem_object.intermediate_max_alpha * 100) style "espe_button" text_style "espe_button_text_24":
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_intermediate_max_alpha", field_type=float, multiplie_value=100.0, clamp_range=(0, 100.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_alpha)]
                bar:
                    value FieldValue(espe_editor_data, "p_intermediate_max_alpha", 1.0, step=1.0,
                                    action=Function(espe_update_alpha))
                    style "espe_property_bar"

                textbutton "Значение 2: {:0.0f}%".format(editor_data.psystem_object.intermediate_min_alpha * 100) style "espe_button" text_style "espe_button_text_24":
                    sensitive editor_data.p_alpha_changer_oscillatory_type
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_intermediate_min_alpha", field_type=float, multiplie_value=100.0, clamp_range=(0, 100.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_alpha)]
                
                if editor_data.p_alpha_changer_oscillatory_type:
                    bar:
                        value FieldValue(espe_editor_data, "p_intermediate_min_alpha", 1.0, step=1.0,
                                        action=Function(espe_update_alpha))
                        style "espe_property_bar"
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_intermediate_min_alpha, 1.0)
                        style "espe_property_inactive_bar"
                
                text espe_properties_divider_huge style "espe_text_24"

                text "Скорость колебания" style "espe_text_heading_24"
                textbutton "Диапазон скорости {}".format(espe_get_property_check(editor_data.p_alpha_changer_oscillatory_speed_type)) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_alpha_speed_oscillatory"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [ToggleField(espe_editor_data, "p_alpha_changer_oscillatory_speed_type"),
                            Function(espe_alpha_oscillatory_speed_update),
                            Hide("ESPE_editor_hint")
                            ]
                textbutton "{}: {:0.0f}".format(if_range_alpha_speed, editor_data.psystem_object.alpha_max_speed) style "espe_button" text_style "espe_button_text_24":
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_alpha_max_speed", field_type=float, clamp_range=(0.0, 1000.0), max_length=6,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_alpha_speed)]
                bar:
                    value FieldValue(espe_editor_data, "p_alpha_max_speed", 1000.0, step=1.0,
                                    action=Function(espe_update_alpha_speed))
                    style "espe_property_bar"
                
                textbutton "Значение 2: {:0.0f}".format(editor_data.psystem_object.alpha_min_speed) style "espe_button" text_style "espe_button_text_24":
                    sensitive editor_data.p_alpha_changer_oscillatory_speed_type
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_alpha_min_speed", field_type=float, clamp_range=(0.0, 1000.0), max_length=6,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_alpha_speed)]

                if editor_data.p_alpha_changer_oscillatory_speed_type:
                    bar:
                        value FieldValue(espe_editor_data, "p_alpha_min_speed", 1000.0, step=1.0,
                                        action=Function(espe_update_alpha_speed))
                        style "espe_property_bar"
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_alpha_min_speed, 1000.0)
                        style "espe_property_inactive_bar"

                text espe_properties_divider_huge style "espe_text_24"

                text "Начальная фаза" style "espe_text_heading_24"
                textbutton "Случайная фаза {}".format(espe_get_property_check(editor_data.p_alpha_changer_oscillatory_phase_type)) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_alpha_oscillatory_random_phase"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [ToggleField(espe_editor_data, "p_alpha_changer_oscillatory_phase_type"),
                            Function(espe_alpha_oscillatory_phase_update),
                            Hide("ESPE_editor_hint")
                            ]

                textbutton "Значение: {:0.0f}°".format(editor_data.psystem_object.alpha_phase) style "espe_button" text_style "espe_button_text_24":
                    sensitive not editor_data.p_alpha_changer_oscillatory_phase_type
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_alpha_phase", field_type=float, clamp_range=(0.0, 360.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_alpha_phase)]

                if not editor_data.p_alpha_changer_oscillatory_phase_type:
                    bar:
                        value FieldValue(espe_editor_data, "p_alpha_phase", 360.0, step=1.0,
                                        action=Function(espe_update_alpha_phase))
                        style "espe_property_bar"
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_alpha_phase, 360.0)
                        style "espe_property_inactive_bar"

            add Null(width=480)
    vbar:
        value YScrollValue("alpha_oscillatory_prop")
        style "espe_scrollbar"
        yalign 0.5
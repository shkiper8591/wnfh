##Экраны раздела "Движение".##
screen ESPE_editor_movement_properties():
    tag espe_editor_main

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.125, 0.07)

        text "Движение" xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"
    
    vbox:
        at fast_pos_05anchor(0.125, 0.5)

        textbutton "Основное движение" style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_main_move_properties"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Show("ESPE_editor_main_movement"),
                    Hide("ESPE_editor_hint"),
                    SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_main_movement")]
        
        text espe_properties_divider style "espe_text_24"

        textbutton "Дополнительное движение" style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_extra_move_properties"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Show("ESPE_editor_extra_movement"),
                    Hide("ESPE_editor_hint"),
                    SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_extra_movement")]

    textbutton "Назад" style "espe_button" text_style "espe_button_text_36" at fast_pos_05anchor(0.125, 0.95):
        mouse "ESPE_cursor_choice"
        action [Show("ESPE_editor_main_menu"),
                SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_main_menu")]

screen ESPE_editor_main_movement():
    tag espe_editor_main

    $ editor_data = espe_editor_data
    $ psystem = editor_data.psystem_object

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.125, 0.07)

        text "Основное движение" xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.1
        spacing -7

        textbutton "Статика " + espe_get_property_radiobutton(editor_data.p_move_type, 0) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_move_static"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_move_type", 0),
                    Function(espe_set_static_move)]
        
        text espe_properties_divider style "espe_text_24"

        textbutton "Простое движение" + espe_get_property_radiobutton(editor_data.p_move_type, 1) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_move_simple"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_move_type", 1),
                    Function(espe_set_simple_move)]

        text espe_properties_divider style "espe_text_24"

        textbutton "Движение с ускорением " + espe_get_property_radiobutton(editor_data.p_move_type, 2) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_move_accelerate"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_move_type", 2),
                    Function(espe_set_accelerate_move)]
        
        text espe_properties_divider style "espe_text_24"

    if editor_data.p_move_type == 0:
        use ESPE_static_move_subscreen()
    elif editor_data.p_move_type == 1:
        use ESPE_simple_move_subscreen()
    elif editor_data.p_move_type == 2:
        use ESPE_accelerate_move_subscreen()
    
    textbutton "Назад" style "espe_button" text_style "espe_button_text_36" at fast_pos_05anchor(0.125, 0.95):
        mouse "ESPE_cursor_choice"
        action [Show("ESPE_editor_movement_properties"),
                SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_movement_properties")]

screen ESPE_static_move_subscreen():
    tag espe_pos_subscreen
    zorder 10

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.39

        text espe_properties_divider_huge style "espe_text_24"

    vbox:
        at fast_pos_05anchor(0.125, 0.55)

        text espe_properties_divider style "espe_text_24"
        text "Не настраивается" xalign 0.5 xmaximum 0.24 style "espe_text_heading_24"
        text espe_properties_divider style "espe_text_24"

screen ESPE_simple_move_subscreen():
    tag espe_pos_subscreen
    zorder 10

    $ editor_data = espe_editor_data
    $ if_range_string = "Значение" if not editor_data.p_speed_simple_move_changer_type else "Значение 1"

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.39

        text espe_properties_divider_huge style "espe_text_24"
    
    grid 1 10:
        xanchor 0.5
        xpos 0.125
        ypos 0.46
        spacing -5

        text "Скорость" style "espe_text_heading_24"
        textbutton "Диапазон скорости {}".format(espe_get_property_check(editor_data.p_speed_simple_move_changer_type)) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_move_speed_range"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [ToggleField(espe_editor_data, "p_speed_simple_move_changer_type"),
                    Function(espe_simple_move_update),
                    Hide("ESPE_editor_hint")
                    ]
        textbutton "{} X: {:0.0f}".format(if_range_string, editor_data.psystem_object.max_x_speed) style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_editor_input", obj=editor_data, field="p_max_x_speed", field_type=float, additional_value=1000.0, clamp_range=(-1000, 1000), max_length=4,
                        exclude=espe_input_exclude_letters,
                        force_update_attr_func=espe_update_speed)]
        bar:
            value FieldValue(espe_editor_data, "p_max_x_speed", 2000.0, step=1.0,
                            action=Function(espe_update_speed))
            style "espe_property_bar"
            xsize 0.18

        textbutton "Значение 2 X: {:0.0f}".format(editor_data.psystem_object.min_x_speed) style "espe_button" text_style "espe_button_text_24":
            sensitive editor_data.p_speed_simple_move_changer_type
            action [Show("ESPE_editor_input", obj=editor_data, field="p_min_x_speed", field_type=float, additional_value=1000.0, clamp_range=(-1000, 1000), max_length=4,
                        exclude=espe_input_exclude_letters,
                        force_update_attr_func=espe_update_speed)]
        
        if editor_data.p_speed_simple_move_changer_type:
            bar:
                value FieldValue(espe_editor_data, "p_min_x_speed", 2000.0, step=1.0,
                                action=Function(espe_update_speed))
                style "espe_property_bar"
                xsize 0.18
        else:
            bar:
                value StaticValue(espe_editor_data.p_min_x_speed, 2000.0)
                style "espe_property_inactive_bar"
                xsize 0.18
        
        textbutton "{} Y: {:0.0f}".format(if_range_string, editor_data.psystem_object.max_y_speed) style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_editor_input", obj=editor_data, field="p_max_y_speed", field_type=float, additional_value=1000.0, clamp_range=(-1000, 1000), max_length=4,
                        exclude=espe_input_exclude_letters,
                        force_update_attr_func=espe_update_speed)]
        bar:
            value FieldValue(espe_editor_data, "p_max_y_speed", 2000.0, step=1.0,
                            action=Function(espe_update_speed))
            style "espe_property_bar"
            xsize 0.18

        textbutton "Значение 2 Y: {:0.0f}".format(editor_data.psystem_object.min_y_speed) style "espe_button" text_style "espe_button_text_24":
            sensitive editor_data.p_speed_simple_move_changer_type
            action [Show("ESPE_editor_input", obj=editor_data, field="p_min_y_speed", field_type=float, additional_value=1000.0, clamp_range=(-1000, 1000), max_length=4,
                        exclude=espe_input_exclude_letters,
                        force_update_attr_func=espe_update_speed)]
        
        if editor_data.p_speed_simple_move_changer_type:
            bar:
                value FieldValue(espe_editor_data, "p_min_y_speed", 2000.0, step=1.0,
                                action=Function(espe_update_speed))
                style "espe_property_bar"
                xsize 0.18
        else:
            bar:
                value StaticValue(espe_editor_data.p_min_y_speed, 2000.0)
                style "espe_property_inactive_bar"
                xsize 0.18

screen ESPE_accelerate_move_subscreen():
    tag espe_pos_subscreen
    zorder 10

    $ editor_data = espe_editor_data
    $ if_range_string_speed = "Значение" if not editor_data.p_speed_accelerate_move_changer_type else "Значение 1"
    $ if_range_string_acc = "Значение" if not editor_data.p_acc_accelerate_move_changer_type else "Значение 1"


    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.39

        text espe_properties_divider_huge style "espe_text_24"
    
    fixed:
        area (0.0, 0.46, 0.25, 0.436)
        viewport id "accelerate_prop":
            draggable True
            mousewheel True
            scrollbars None

            has grid 1 22:
                spacing -5

                text "Скорость" style "espe_text_heading_24"
                textbutton "Диапазон скорости {}".format(espe_get_property_check(editor_data.p_speed_accelerate_move_changer_type)) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_move_speed_range"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [ToggleField(espe_editor_data, "p_speed_accelerate_move_changer_type"),
                            Function(espe_accelerate_move_update),
                            Hide("ESPE_editor_hint")
                            ]
                textbutton "{} X: {:0.0f}".format(if_range_string_speed, editor_data.psystem_object.max_x_speed) style "espe_button" text_style "espe_button_text_24":
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_max_x_speed", field_type=float, additional_value=1000.0, clamp_range=(-1000, 1000), max_length=4,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_speed)]
                bar:
                    value FieldValue(espe_editor_data, "p_max_x_speed", 2000.0, step=1.0,
                                    action=Function(espe_update_speed))
                    style "espe_property_bar"

                textbutton "Значение 2 X: {:0.0f}".format(editor_data.psystem_object.min_x_speed) style "espe_button" text_style "espe_button_text_24":
                    sensitive editor_data.p_speed_accelerate_move_changer_type
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_min_x_speed", field_type=float, additional_value=1000.0, clamp_range=(-1000, 1000), max_length=4,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_speed)]
                
                if editor_data.p_speed_accelerate_move_changer_type:
                    bar:
                        value FieldValue(espe_editor_data, "p_min_x_speed", 2000.0, step=1.0,
                                        action=Function(espe_update_speed))
                        style "espe_property_bar"
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_min_x_speed, 2000.0)
                        style "espe_property_inactive_bar"
                
                textbutton "{} Y: {:0.0f}".format(if_range_string_speed, editor_data.psystem_object.max_y_speed) style "espe_button" text_style "espe_button_text_24":
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_max_y_speed", field_type=float, additional_value=1000.0, clamp_range=(-1000, 1000), max_length=4,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_speed)]
                bar:
                    value FieldValue(espe_editor_data, "p_max_y_speed", 2000.0, step=1.0,
                                    action=Function(espe_update_speed))
                    style "espe_property_bar"

                textbutton "Значение 2 Y: {:0.0f}".format(editor_data.psystem_object.min_y_speed) style "espe_button" text_style "espe_button_text_24":
                    sensitive editor_data.p_speed_accelerate_move_changer_type
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_min_y_speed", field_type=float, additional_value=1000.0, clamp_range=(-1000, 1000), max_length=4,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_speed)]
                
                if editor_data.p_speed_accelerate_move_changer_type:
                    bar:
                        value FieldValue(espe_editor_data, "p_min_y_speed", 2000.0, step=1.0,
                                        action=Function(espe_update_speed))
                        style "espe_property_bar"
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_min_y_speed, 2000.0)
                        style "espe_property_inactive_bar"
                
                text espe_properties_divider_huge style "espe_text_24"

                text "Ускорение" style "espe_text_heading_24"
                textbutton "Диапазон ускорения {}".format(espe_get_property_check(editor_data.p_acc_accelerate_move_changer_type)) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_move_accelerate_range"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [ToggleField(espe_editor_data, "p_acc_accelerate_move_changer_type"),
                            Function(espe_accelerate_move_update),
                            Hide("ESPE_editor_hint")
                            ]

                textbutton "{} X: {:0.0f}".format(if_range_string_acc, editor_data.psystem_object.max_x_accelerate) style "espe_button" text_style "espe_button_text_24":
                        action [Show("ESPE_editor_input", obj=editor_data, field="p_max_x_accelerate", field_type=float, additional_value=100.0, clamp_range=(-100, 100), max_length=4,
                                    exclude=espe_input_exclude_letters,
                                    force_update_attr_func=espe_update_accelerate)]
                bar:
                    value FieldValue(espe_editor_data, "p_max_x_accelerate", 200.0, step=1.0,
                                    action=Function(espe_update_accelerate))
                    style "espe_property_bar"

                textbutton "Значение 2 X: {:0.0f}".format(editor_data.psystem_object.min_x_accelerate) style "espe_button" text_style "espe_button_text_24":
                    sensitive editor_data.p_acc_accelerate_move_changer_type
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_min_x_accelerate", field_type=float, additional_value=100.0, clamp_range=(-100, 100), max_length=4,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_accelerate)]
                
                if editor_data.p_acc_accelerate_move_changer_type:
                    bar:
                        value FieldValue(espe_editor_data, "p_min_x_accelerate", 200.0, step=1.0,
                                        action=Function(espe_update_accelerate))
                        style "espe_property_bar"
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_min_x_accelerate, 200.0)
                        style "espe_property_inactive_bar"
                
                textbutton "{} Y: {:0.0f}".format(if_range_string_acc, editor_data.psystem_object.max_y_accelerate) style "espe_button" text_style "espe_button_text_24":
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_max_y_accelerate", field_type=float, additional_value=100.0, clamp_range=(-100, 100), max_length=4,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_accelerate)]
                bar:
                    value FieldValue(espe_editor_data, "p_max_y_accelerate", 200.0, step=1.0,
                                    action=Function(espe_update_accelerate))
                    style "espe_property_bar"

                textbutton "Значение 2 Y: {:0.0f}".format(editor_data.psystem_object.min_y_accelerate) style "espe_button" text_style "espe_button_text_24":
                    sensitive editor_data.p_acc_accelerate_move_changer_type
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_min_y_accelerate", field_type=float, additional_value=100.0, clamp_range=(-100, 100), max_length=4,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_accelerate)]
                
                if editor_data.p_acc_accelerate_move_changer_type:
                    bar:
                        value FieldValue(espe_editor_data, "p_min_y_accelerate", 200.0, step=1.0,
                                        action=Function(espe_update_accelerate))
                        style "espe_property_bar"
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_min_y_accelerate, 200.0)
                        style "espe_property_inactive_bar"
            
            add Null(width=480)

    vbar:
        value YScrollValue("accelerate_prop")
        style "espe_scrollbar"
        yalign 0.5

###############################################################################

screen ESPE_editor_extra_movement():
    tag espe_editor_main

    $ editor_data = espe_editor_data
    $ psystem = editor_data.psystem_object

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.125, 0.07)

        text "Дополнительное движение" xalign 0.5 style "espe_text_heading_36" size 32
        text espe_properties_divider_huge style "espe_text_24"

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.1

        textbutton "Отключить доп. движение" + espe_get_property_radiobutton(editor_data.p_move_extra_type, 0) style "espe_button" text_style "espe_button_text_24":
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_move_extra_type", 0),
                    Function(espe_update_extra_move)]

        textbutton "Колебательное движение" + espe_get_property_radiobutton(editor_data.p_move_extra_type, 1) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_move_extra_oscillatory"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_move_extra_type", 1),
                    Function(espe_update_extra_move)]
    
    if editor_data.p_move_extra_type == 1:
        use ESPE_extra_move_oscillatory_subscreen()
    
    textbutton "Назад" style "espe_button" text_style "espe_button_text_36" at fast_pos_05anchor(0.125, 0.95):
        mouse "ESPE_cursor_choice"
        action [Show("ESPE_editor_movement_properties"),
                SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_movement_properties")]
    
screen ESPE_extra_move_oscillatory_subscreen():
    tag espe_pos_subscreen
    zorder 10

    $ editor_data = espe_editor_data
    $ if_range_string_speed = "Значение" if not editor_data.p_speed_extra_changer_type else "Значение 1"
    $ if_range_string_radius = "Значение" if not editor_data.p_radius_oscillatory_changer_type else "Значение 1"


    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.39

        text espe_properties_divider_huge style "espe_text_24"
    
    fixed:
        area (0.0, 0.46, 0.25, 0.436)
        viewport id "oscillatory_prop":
            draggable True
            mousewheel True
            scrollbars None

            has grid 1 23:
                spacing -5

                text "Скорость колебания" style "espe_text_heading_24"
                textbutton "Диапазон скорости {}".format(espe_get_property_check(editor_data.p_speed_extra_changer_type)) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_extra_move_oscillatory_speed_range"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [ToggleField(espe_editor_data, "p_speed_extra_changer_type"),
                            Function(espe_update_oscillatory_speed_changer),
                            Hide("ESPE_editor_hint")
                            ]
                textbutton "{}: {:0.0f}".format(if_range_string_speed, editor_data.psystem_object.max_speed_oscillatory) style "espe_button" text_style "espe_button_text_24":
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_max_speed_oscillatory", field_type=float, additional_value=1000.0, clamp_range=(-1000, 1000), max_length=4,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_extra_speed_oscillatory)]
                bar:
                    value FieldValue(espe_editor_data, "p_max_speed_oscillatory", 2000.0, step=1.0,
                                    action=Function(espe_update_extra_speed_oscillatory))
                    style "espe_property_bar"

                textbutton "Значение 2: {:0.0f}".format(editor_data.psystem_object.min_speed_oscillatory) style "espe_button" text_style "espe_button_text_24":
                    sensitive editor_data.p_speed_extra_changer_type
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_min_speed_oscillatory", field_type=float, additional_value=1000.0, clamp_range=(-1000, 1000), max_length=4,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_extra_speed_oscillatory)]
                
                if editor_data.p_speed_extra_changer_type:
                    bar:
                        value FieldValue(espe_editor_data, "p_min_speed_oscillatory", 2000.0, step=1.0,
                                        action=Function(espe_update_extra_speed_oscillatory))
                        style "espe_property_bar"
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_min_speed_oscillatory, 2000.0)
                        style "espe_property_inactive_bar"
                
                text espe_properties_divider_huge style "espe_text_24"

                text "Радиус" style "espe_text_heading_24"
                textbutton "Диапазон радиуса {}".format(espe_get_property_check(editor_data.p_radius_oscillatory_changer_type)) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_extra_move_oscillatory_radius_range"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [ToggleField(espe_editor_data, "p_radius_oscillatory_changer_type"),
                            Function(espe_update_oscillatory_radius_changer),
                            Hide("ESPE_editor_hint")
                            ]

                textbutton "{} X: {:0.0f}".format(if_range_string_radius, editor_data.psystem_object.max_x_oscillatory) style "espe_button" text_style "espe_button_text_24":
                        action [Show("ESPE_editor_input", obj=editor_data, field="p_max_x_oscillatory", field_type=float, clamp_range=(0.0, 1080.0), max_length=5,
                                    exclude=espe_input_exclude_letters,
                                    force_update_attr_func=espe_update_extra_radius_oscillatory)]
                bar:
                    value FieldValue(espe_editor_data, "p_max_x_oscillatory", 1080.0, step=1.0,
                                    action=Function(espe_update_extra_radius_oscillatory))
                    style "espe_property_bar"

                textbutton "Значение 2 X: {:0.0f}".format(editor_data.psystem_object.min_x_oscillatory) style "espe_button" text_style "espe_button_text_24":
                    sensitive editor_data.p_radius_oscillatory_changer_type
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_min_x_oscillatory", field_type=float, clamp_range=(0.0, 1080.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_extra_radius_oscillatory)]
                
                if editor_data.p_radius_oscillatory_changer_type:
                    bar:
                        value FieldValue(espe_editor_data, "p_min_x_oscillatory", 1080.0, step=1.0,
                                        action=Function(espe_update_extra_radius_oscillatory))
                        style "espe_property_bar"
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_min_x_oscillatory, 1080.0)
                        style "espe_property_inactive_bar"
                
                textbutton "{} Y: {:0.0f}".format(if_range_string_radius, editor_data.psystem_object.max_y_oscillatory) style "espe_button" text_style "espe_button_text_24":
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_max_y_oscillatory", field_type=float, clamp_range=(0.0, 1080.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_extra_radius_oscillatory)]
                bar:
                    value FieldValue(espe_editor_data, "p_max_y_oscillatory", 1080.0, step=1.0,
                                    action=Function(espe_update_extra_radius_oscillatory))
                    style "espe_property_bar"

                textbutton "Значение 2 Y: {:0.0f}".format(editor_data.psystem_object.min_y_oscillatory) style "espe_button" text_style "espe_button_text_24":
                    sensitive editor_data.p_radius_oscillatory_changer_type
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_min_y_oscillatory", field_type=float, clamp_range=(0.0, 1080.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_extra_radius_oscillatory)]
                
                if editor_data.p_radius_oscillatory_changer_type:
                    bar:
                        value FieldValue(espe_editor_data, "p_min_y_oscillatory", 1080.0, step=1.0,
                                        action=Function(espe_update_extra_radius_oscillatory))
                        style "espe_property_bar"
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_min_y_oscillatory, 1080.0)
                        style "espe_property_inactive_bar"
            
                text espe_properties_divider_huge style "espe_text_24"

                text "Начальная фаза" style "espe_text_heading_24"
                textbutton "Случайная фаза {}".format(espe_get_property_check(editor_data.p_random_start_phase)) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_extra_move_oscillatory_random_phase"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [ToggleField(espe_editor_data, "p_random_start_phase"),
                            Function(espe_update_oscillatory_phase_changer),
                            Hide("ESPE_editor_hint")
                            ]

                textbutton "Значение: {:0.0f}°".format(editor_data.psystem_object.extra_move_phase) style "espe_button" text_style "espe_button_text_24":
                    sensitive not editor_data.p_random_start_phase
                    action [Show("ESPE_editor_input", obj=editor_data, field="p_extra_phase", field_type=float, clamp_range=(0.0, 360.0), max_length=5,
                                exclude=espe_input_exclude_letters,
                                force_update_attr_func=espe_update_extra_phase_oscillatory)]
                
                if not editor_data.p_random_start_phase:
                    bar:
                        value FieldValue(espe_editor_data, "p_extra_phase", 360.0, step=1.0,
                                        action=Function(espe_update_extra_phase_oscillatory))
                        style "espe_property_bar"
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_extra_phase, 360.0)
                        style "espe_property_inactive_bar"

            add Null(width=480)
    
    vbar:
        value YScrollValue("oscillatory_prop")
        style "espe_scrollbar"
        yalign 0.5
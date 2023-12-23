##Экраны раздела "Позиционирование".##
screen ESPE_editor_position_properties():
    tag espe_editor_main

    add Solid("#000", xsize=0.2, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.1, 0.07)

        text "Позиционирование" xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"
    
    vbox:
        at fast_pos_05anchor(0.1, 0.5)

        textbutton "Зона появления" style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_spawn_area_main"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Show("ESPE_editor_spawn_area"),
                    Hide("ESPE_editor_hint"),
                    SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_spawn_area")]

        #text espe_properties_divider style "espe_text_24"

        #textbutton "Привязка" style "espe_button" text_style "espe_button_text_24":
        #    #sensitive espe_editor_data.psystem_type == "complex"
        #    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_anchor_main"]))
        #    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
        #    action [Show("ESPE_editor_anchor_properties"),
        #            Hide("ESPE_editor_hint"),
        #            SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_anchor_properties")]
    
    textbutton "Назад" style "espe_button" text_style "espe_button_text_36" at fast_pos_05anchor(0.1, 0.95):
        mouse "ESPE_cursor_choice"
        action [Show("ESPE_editor_main_menu"),
                SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_main_menu")]

screen ESPE_editor_spawn_area():
    tag espe_editor_main

    $ editor_data = espe_editor_data

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.125, 0.07)

        text "Зона появления" xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.1
        spacing -7

        textbutton "Точка " + espe_get_property_radiobutton(editor_data.p_spawn_area_type, 0) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_spawn_area_dot"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_spawn_area_type", 0),
                    Function(espe_set_dot_emitter_pos)]
        
        text espe_properties_divider style "espe_text_24"

        textbutton "Прямоугольная зона " + espe_get_property_radiobutton(editor_data.p_spawn_area_type, 1) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_spawn_area_rectangle"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_spawn_area_type", 1),
                    Function(espe_set_rectangle_emitter_pos)]
        
        text espe_properties_divider style "espe_text_24"

        textbutton "Радиальная зона " + espe_get_property_radiobutton(editor_data.p_spawn_area_type, 2) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_spawn_area_circle"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_spawn_area_type", 2),
                    Function(espe_set_radial_emitter_pos)]
        
        text espe_properties_divider style "espe_text_24"

        textbutton "Видимый экран " + espe_get_property_radiobutton(editor_data.p_spawn_area_type, 3) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_spawn_area_screen"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_spawn_area_type", 3),
                    Function(espe_set_screen_emitter_pos)]
        
        text espe_properties_divider style "espe_text_24"

        textbutton "От краёв экрана " + espe_get_property_radiobutton(editor_data.p_spawn_area_type, 4) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_spawn_area_sides"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [Hide("ESPE_editor_hint"),
                    SetField(editor_data, "p_spawn_area_type", 4),
                    Function(espe_set_sides_emitter_pos)]
        
        text espe_properties_divider style "espe_text_24"

    if editor_data.p_spawn_area_type == 0:
        use ESPE_dot_emitter_subscreen()
    elif editor_data.p_spawn_area_type == 1:
        use ESPE_rectangle_emitter_subscreen()
    elif editor_data.p_spawn_area_type == 2:
        use ESPE_radial_emitter_subscreen()
    elif editor_data.p_spawn_area_type == 3:
        use ESPE_screen_emitter_subscreen()
    elif editor_data.p_spawn_area_type == 4:
        use ESPE_sides_emitter_subscreen()
    
    textbutton "Назад" style "espe_button" text_style "espe_button_text_36" at fast_pos_05anchor(0.125, 0.95):
        mouse "ESPE_cursor_choice"
        action [Show("ESPE_editor_position_properties"),
                SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_position_properties")]

screen ESPE_dot_emitter_subscreen():
    tag espe_pos_subscreen
    zorder 10

    $ editor_data = espe_editor_data
    $ emitter_pos = editor_data.p_emitter_pos

    add "espe_dot_pointer" at fast_pos_05anchor_tint(emitter_pos[0], emitter_pos[1], "#b90000")

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.39

        text "Точечный испускатель" xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"

    grid 1 6:
        xanchor 0.5
        xpos 0.125
        ypos 0.475

        text "Позиция испускания" style "espe_text_heading_24"
        textbutton "X: {}".format(editor_data.p_emitter_pos[0]) style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_editor_input_collections", obj=editor_data, field="p_emitter_pos", field_type=int, index=0, clamp_range=(0, config.screen_width), max_length=4,
                        exclude=espe_input_exclude_letters + ".",
                        force_update_attr_func=espe_update_dot_emitter_pos)]
        bar:
            value FieldValueCollection(espe_editor_data, "p_emitter_pos", 0, config.screen_width,
                            action=Function(espe_update_dot_emitter_pos))
            style "espe_property_bar"
            xsize 0.18


        text espe_properties_divider style "espe_text_24"

        textbutton "Y: {}".format(editor_data.p_emitter_pos[1]) style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_editor_input_collections", obj=editor_data, field="p_emitter_pos", field_type=int, index=1, clamp_range=(0, config.screen_height), max_length=4,
                        exclude=espe_input_exclude_letters + ".",
                        force_update_attr_func=espe_update_dot_emitter_pos)]
        bar:
            value FieldValueCollection(espe_editor_data, "p_emitter_pos", 1, config.screen_height,
                            action=Function(espe_update_dot_emitter_pos))
            style "espe_property_bar"
            xsize 0.18

screen ESPE_rectangle_emitter_subscreen():
    tag espe_pos_subscreen
    zorder 10

    $ editor_data = espe_editor_data
    $ rectangle_emitter_pos = editor_data.p_rectangle_emitter_pos
    $ rectangle_spawn_area = editor_data.p_rectangle_spawn_area

    add Solid("#b9000066", xsize=rectangle_spawn_area[0], ysize=rectangle_spawn_area[1]) at fast_pos_05anchor(rectangle_emitter_pos[0], rectangle_emitter_pos[1])
    add "espe_dot_pointer" at fast_pos_05anchor_tint(rectangle_emitter_pos[0], rectangle_emitter_pos[1], "#b90000")

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.39

        text "Прямоугольная зона испускания" xmaximum 0.24 xalign 0.5 style "espe_text_heading_24"
        text espe_properties_divider_huge style "espe_text_24"

    grid 1 13:
        xanchor 0.5
        xpos 0.125
        ypos 0.456
        spacing -5

        text "Позиция зоны" style "espe_text_heading_24"
        textbutton "X: {}".format(editor_data.p_rectangle_emitter_pos[0]) style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_editor_input_collections", obj=editor_data, field="p_rectangle_emitter_pos", field_type=int, index=0, clamp_range=(0, config.screen_width), max_length=4,
                        exclude=espe_input_exclude_letters + ".",
                        force_update_attr_func=espe_update_rectangle_emitter_pos)]
        bar:
            value FieldValueCollection(espe_editor_data, "p_rectangle_emitter_pos", 0, config.screen_width,
                            action=Function(espe_update_rectangle_emitter_pos))
            style "espe_property_bar"
            xsize 0.18

        text espe_properties_divider style "espe_text_24"

        textbutton "Y: {}".format(editor_data.p_rectangle_emitter_pos[1]) style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_editor_input_collections", obj=editor_data, field="p_rectangle_emitter_pos", field_type=int, index=1, clamp_range=(0, config.screen_height), max_length=4,
                        exclude=espe_input_exclude_letters + ".",
                        force_update_attr_func=espe_update_rectangle_emitter_pos)]
        bar:
            value FieldValueCollection(espe_editor_data, "p_rectangle_emitter_pos", 1, config.screen_height,
                            action=Function(espe_update_rectangle_emitter_pos))
            style "espe_property_bar"
            xsize 0.18
        
        text espe_properties_divider style "espe_text_24"

        text "Размер зоны" style "espe_text_heading_24"
        textbutton "X: {}".format(editor_data.p_rectangle_spawn_area[0]) style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_editor_input_collections", obj=editor_data, field="p_rectangle_spawn_area", field_type=int, index=0, clamp_range=(0, config.screen_width), max_length=4,
                        exclude=espe_input_exclude_letters + ".",
                        force_update_attr_func=espe_update_rectangle_spawn_area)]
        bar:
            value FieldValueCollection(espe_editor_data, "p_rectangle_spawn_area", 0, config.screen_width,
                            action=Function(espe_update_rectangle_spawn_area))
            style "espe_property_bar"
            xsize 0.18

        text espe_properties_divider style "espe_text_24"

        textbutton "Y: {}".format(editor_data.p_rectangle_spawn_area[1]) style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_editor_input_collections", obj=editor_data, field="p_rectangle_spawn_area", field_type=int, index=1, clamp_range=(0, config.screen_height), max_length=4,
                        exclude=espe_input_exclude_letters + ".",
                        force_update_attr_func=espe_update_rectangle_spawn_area)]
        bar:
            value FieldValueCollection(espe_editor_data, "p_rectangle_spawn_area", 1, config.screen_height,
                            action=Function(espe_update_rectangle_spawn_area))
            style "espe_property_bar"
            xsize 0.18

screen ESPE_radial_emitter_subscreen():
    tag espe_pos_subscreen
    zorder 10

    $ editor_data = espe_editor_data
    $ radial_emitter_pos = editor_data.p_radial_emitter_pos
    $ radius_emitter = editor_data.p_emitter_radius
    $ radial_area = float(radius_emitter) * 2.0 / float(config.screen_height)

    add "espe_radial_area1080" at fast_pos_05anchor_alpha_zoom_tint(radial_emitter_pos[0], radial_emitter_pos[1], 0.4, radial_area, "#b90000")
    add "espe_dot_pointer" at fast_pos_05anchor_tint(radial_emitter_pos[0], radial_emitter_pos[1], "#b90000")

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.39

        text "Радиальная зона испускания" xmaximum 0.24 xalign 0.5 style "espe_text_heading_24"
        text espe_properties_divider_huge style "espe_text_24"

    grid 1 10:
        xanchor 0.5
        xpos 0.125
        ypos 0.46
        spacing -5

        text "Центр окружности" style "espe_text_heading_24"
        textbutton "X: {}".format(editor_data.p_radial_emitter_pos[0]) style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_editor_input_collections", obj=editor_data, field="p_radial_emitter_pos", field_type=int, index=0, clamp_range=(0, config.screen_width), max_length=4,
                        exclude=espe_input_exclude_letters + ".",
                        force_update_attr_func=espe_update_radial_emitter_pos)]
        bar:
            value FieldValueCollection(espe_editor_data, "p_radial_emitter_pos", 0, config.screen_width,
                            action=Function(espe_update_radial_emitter_pos))
            style "espe_property_bar"
            xsize 0.18

        text espe_properties_divider style "espe_text_24"

        textbutton "Y: {}".format(editor_data.p_radial_emitter_pos[1]) style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_editor_input_collections", obj=editor_data, field="p_radial_emitter_pos", field_type=int, index=1, clamp_range=(0, config.screen_height), max_length=4,
                        exclude=espe_input_exclude_letters + ".",
                        force_update_attr_func=espe_update_radial_emitter_pos)]
        bar:
            value FieldValueCollection(espe_editor_data, "p_radial_emitter_pos", 1, config.screen_height,
                            action=Function(espe_update_radial_emitter_pos))
            style "espe_property_bar"
            xsize 0.18
        
        text espe_properties_divider style "espe_text_24"

        text "Радиус" style "espe_text_heading_24"
        textbutton "{}".format(editor_data.p_emitter_radius) style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_editor_input", obj=editor_data, field="p_emitter_radius", field_type=int, clamp_range=(0, config.screen_height), max_length=4,
                        exclude=espe_input_exclude_letters + ".",
                        force_update_attr_func=espe_update_emitter_radius_pos)]
        bar:
            value FieldValue(espe_editor_data, "p_emitter_radius", config.screen_height,
                            action=Function(espe_update_emitter_radius_pos))
            style "espe_property_bar"
            xsize 0.18

screen ESPE_screen_emitter_subscreen():
    tag espe_pos_subscreen
    zorder 10

    add "espe_screen_area" matrixcolor TintMatrix("#b90000") alpha 0.4
    add "espe_dot_pointer" at fast_pos_05anchor_tint(0.5, 0.5, "#b90000")

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.39

        text "Испускание по всему экрану" xmaximum 0.24 xalign 0.5 style "espe_text_heading_24"
        text espe_properties_divider_huge style "espe_text_24"

    vbox:
        at fast_pos_05anchor(0.125, 0.6)

        text espe_properties_divider style "espe_text_24"
        text "Не настраивается" xalign 0.5 xmaximum 0.24 style "espe_text_heading_24"
        text espe_properties_divider style "espe_text_24"

screen ESPE_sides_emitter_subscreen():
    tag espe_pos_subscreen
    zorder 10

    $ editor_data = espe_editor_data
    $ bounds_counter = sum(value is True for value in editor_data.p_out_of_bounds_spawn_dict.values())

    if editor_data.p_out_of_bounds_spawn_dict["Top"]:
        add "espe_side_topbottom_area" matrixcolor TintMatrix("#b90000") alpha 0.4
    if editor_data.p_out_of_bounds_spawn_dict["Bottom"]:
        add "espe_side_topbottom_area" matrixcolor TintMatrix("#b90000") alpha 0.4 yzoom -1.0
    if editor_data.p_out_of_bounds_spawn_dict["Left"]:
        add "espe_side_leftright_area" matrixcolor TintMatrix("#b90000") alpha 0.4
    if editor_data.p_out_of_bounds_spawn_dict["Right"]:
        add "espe_side_leftright_area" matrixcolor TintMatrix("#b90000") alpha 0.4 xzoom -1.0
    
    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.39

        text "Испускание за границами" xmaximum 0.24 xalign 0.5 style "espe_text_heading_24"
        text espe_properties_divider_huge style "espe_text_24"
    
    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.475
        spacing -5

        textbutton "Верх: {}".format(espe_get_property_check(editor_data.p_out_of_bounds_spawn_dict["Top"])) style "espe_button" text_style "espe_button_text_24":
            sensitive not editor_data.p_out_of_bounds_spawn_dict["Top"] or bounds_counter > 1
            action [ToggleFieldCollection(editor_data, "p_out_of_bounds_spawn_dict", "Top"),
                    Function(espe_update_sides_emitter)]
        
        text espe_properties_divider style "espe_text_24"

        textbutton "Низ: {}".format(espe_get_property_check(editor_data.p_out_of_bounds_spawn_dict["Bottom"])) style "espe_button" text_style "espe_button_text_24":
            sensitive not editor_data.p_out_of_bounds_spawn_dict["Bottom"] or bounds_counter > 1
            action [ToggleFieldCollection(editor_data, "p_out_of_bounds_spawn_dict", "Bottom"),
                    Function(espe_update_sides_emitter)]
        
        text espe_properties_divider style "espe_text_24"

        textbutton "Лево: {}".format(espe_get_property_check(editor_data.p_out_of_bounds_spawn_dict["Left"])) style "espe_button" text_style "espe_button_text_24":
            sensitive not editor_data.p_out_of_bounds_spawn_dict["Left"] or bounds_counter > 1
            action [ToggleFieldCollection(editor_data, "p_out_of_bounds_spawn_dict", "Left"),
                    Function(espe_update_sides_emitter)]
        
        text espe_properties_divider style "espe_text_24"

        textbutton "Право: {}".format(espe_get_property_check(editor_data.p_out_of_bounds_spawn_dict["Right"])) style "espe_button" text_style "espe_button_text_24":
            sensitive not editor_data.p_out_of_bounds_spawn_dict["Right"] or bounds_counter > 1
            action [ToggleFieldCollection(editor_data, "p_out_of_bounds_spawn_dict", "Right"),
                    Function(espe_update_sides_emitter)]

########################################################################################
##.*НЕ РАБОТАЕТ :(*.##
screen ESPE_editor_anchor_properties():
    tag espe_editor_main

    $ editor_data = espe_editor_data

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.125, 0.07)

        text "Привязка" xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"
    
    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.4

        textbutton "X: {:0.2f}".format(editor_data.psystem_object.particle_anchor[0]) style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_editor_input_collections", obj=editor_data, field="p_anchor", field_type=float, index=0, clamp_range=(0.0, 1.0), max_length=4,
                        exclude=espe_input_exclude_letters,
                        force_update_attr_func=espe_update_anchor)]
        bar:
            value FieldValueCollection(espe_editor_data, "p_anchor", 0, 1.0,
                            action=Function(espe_update_anchor))
            style "espe_property_bar"
            xsize 0.18


        text espe_properties_divider style "espe_text_24"

        textbutton "Y: {:0.2f}".format(editor_data.psystem_object.particle_anchor[1]) style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_editor_input_collections", obj=editor_data, field="p_anchor", field_type=float, index=1, clamp_range=(0.0, 1.0), max_length=4,
                        exclude=espe_input_exclude_letters,
                        force_update_attr_func=espe_update_anchor)]
        bar:
            value FieldValueCollection(espe_editor_data, "p_anchor", 1, 1.0,
                            action=Function(espe_update_anchor))
            style "espe_property_bar"
            xsize 0.18

    add Solid("#fff0eb", xsize=0.1, ysize=0.1) at fast_pos_05anchor(0.125, 0.65)
    add "espe_dot_pointer" at fast_pos_05anchor_tint(0.075 + 0.1 * editor_data.p_anchor[0], 0.6 + 0.1 * editor_data.p_anchor[1], "#b90000")
    
    textbutton "Назад" style "espe_button" text_style "espe_button_text_36" at fast_pos_05anchor(0.125, 0.95):
        mouse "ESPE_cursor_choice"
        action [Show("ESPE_editor_position_properties"),
                SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_position_properties")]
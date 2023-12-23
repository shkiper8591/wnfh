##Экраны раздела "Основные свойства".##
screen ESPE_editor_main_properties():
    tag espe_editor_main

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.055

        text "Основные свойства" style "espe_text_heading_36" 
        text espe_properties_divider_huge style "espe_text_24"

    fixed:
        area (0.0, 0.15, 0.25, 0.8)
        viewport id "main_prop":
            draggable True
            mousewheel True
            scrollbars None

            has grid 1 31:
                yspacing None

                text "Название системы" style "espe_text_24"
                textbutton espe_editor_data.psystem_name style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_name"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [Show("ESPE_editor_input", obj=espe_editor_data, field="psystem_name", field_type=str, exclude="{}"),
                            Hide("ESPE_editor_hint")]

                text espe_properties_divider style "espe_text_24"
                
                text "Используемые спрайт/спрайты" style "espe_text_24" size 20
                textbutton "Выбрать/посмотреть" style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_sprite"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [Show("ESPE_editor_displayables_choice", particle_list=espe_template_sprites_list),
                            Hide("ESPE_editor_hint")]
                
                text espe_properties_divider style "espe_text_24"
                
                text "Количество частиц" style "espe_text_24"
                textbutton "Значение: {}".format(espe_editor_data.p_amount) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_amount"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [Show("ESPE_editor_input", obj=espe_editor_data, field="p_amount", field_type=int, max_length=3,
                                psystem_object=espe_editor_data.psystem_object, psystem_field="amount", exclude=espe_input_exclude_letters + "."),
                            Hide("ESPE_editor_hint")]

                text espe_properties_divider style "espe_text_24"
                
                text "Время жизни частицы" style "espe_text_24"
                textbutton str(espe_editor_data.p_lifetime) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_lifetime"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [Show("ESPE_editor_input", obj=espe_editor_data, field="p_lifetime", field_type=float, max_length=5,
                                psystem_object=espe_editor_data.psystem_object, psystem_field="lifetime", exclude=espe_input_exclude_letters),
                            Hide("ESPE_editor_hint")]

                text espe_properties_divider style "espe_text_24"
                
                text "Случайное время жизни" style "espe_text_24"
                textbutton espe_get_property_check(espe_editor_data.p_lifetime_random_enable) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_lifetime_random_enable"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [ToggleField(espe_editor_data, "p_lifetime_random_enable"),
                            Function(espe_setattr_safe, field="p_lifetime_random_enable", object_to_update=espe_editor_data.psystem_object, attr_to_update="lifetime_random_enable", field_type=bool),
                            Hide("ESPE_editor_hint")]
                text "Значение: {:0.0f}%".format(espe_editor_data.p_lifetime_random * 100) style "espe_text_24"
                if espe_editor_data.p_lifetime_random_enable:
                    bar:
                        value FieldValue(espe_editor_data, "p_lifetime_random", 1.0,
                                        action=Function(espe_update_value, object_to_update=espe_editor_data.psystem_object, field="lifetime_random", value=espe_editor_data.p_lifetime_random))
                        style "espe_property_bar"
                        hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_lifetime_random"]))
                        unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_lifetime_random, 1.0)
                        style "espe_property_inactive_bar"
                        
                text espe_properties_divider style "espe_text_24"
                
                text "Время задержки появления" style "espe_text_24"
                textbutton "Значение: {}".format(espe_editor_data.p_lifetime_spread) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_lifetime_spread"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [Show("ESPE_editor_input", obj=espe_editor_data, field="p_lifetime_spread", max_length=4,
                                psystem_object=espe_editor_data.psystem_object, psystem_field="lifetime_spread", field_type=float, exclude=espe_input_exclude_letters, force_update_attr_func=espe_editor_psystem_lifetime_spread_update),
                            Hide("ESPE_editor_hint")]

                text espe_properties_divider style "espe_text_24"

                text "Случайный разброс задержки появления" style "espe_text_24" size 18
                textbutton espe_get_property_check(espe_editor_data.p_lifetime_random_spread_enable) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_lifetime_random_spread_enable"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [ToggleField(espe_editor_data, "p_lifetime_random_spread_enable"),
                            Function(espe_setattr_safe, field="p_lifetime_random_spread_enable", object_to_update=espe_editor_data.psystem_object, attr_to_update="lifetime_spread_random_enable", field_type=bool),
                            Hide("ESPE_editor_hint")]
                text "Значение: {:0.0f}%".format(espe_editor_data.p_lifetime_spread_random * 100) style "espe_text_24"
                if espe_editor_data.p_lifetime_random_spread_enable:
                    bar:
                        value FieldValue(espe_editor_data, "p_lifetime_spread_random", 1.0,
                                        action=Function(espe_update_value, object_to_update=espe_editor_data.psystem_object, field="lifetime_spread_random", value=espe_editor_data.p_lifetime_spread_random))
                        style "espe_property_bar"
                        hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_lifetime_spread_random"]))
                        unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_lifetime_spread_random, 1.0)
                        style "espe_property_inactive_bar"
                
                
                text espe_properties_divider style "espe_text_24"

                text "Взрывчатость" style "espe_text_24"
                textbutton espe_get_property_check(espe_editor_data.p_is_explosiveness) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_explosiveness_enable"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [ToggleField(espe_editor_data, "p_is_explosiveness"),
                            Function(espe_setattr_safe, field="p_is_explosiveness", object_to_update=espe_editor_data.psystem_object, attr_to_update="is_explosiveness", field_type=bool),
                            Hide("ESPE_editor_hint")]
                text "Значение: {:0.0f}%".format(espe_editor_data.p_explosiveness_factor * 100) style "espe_text_24"
                if espe_editor_data.p_is_explosiveness:
                    bar:
                        value FieldValue(espe_editor_data, "p_explosiveness_factor", 1.0,
                                        action=Function(espe_set_explosiveness))
                        style "espe_property_bar"
                        hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_explosiveness_factor"]))
                        unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                else:
                    bar:
                        value StaticValue(espe_editor_data.p_explosiveness_factor, 1.0)
                        style "espe_property_inactive_bar"
                
                
                text espe_properties_divider style "espe_text_24"

            add Null(width=480) #1920*0.25 = 480
        
    vbar:
        value YScrollValue("main_prop")
        style "espe_scrollbar"
        yalign 0.5

    textbutton "Назад" xmaximum 0.2 yalign 1.0 xalign 0.09 style "espe_button" text_style "espe_button_text_36":
        mouse "ESPE_cursor_choice"
        action [Show("ESPE_editor_main_menu"),
                SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_main_menu")]

screen ESPE_editor_displayables_choice(particle_list):
    tag espe_editor_main

    default section_index = -1
    default current_section_name = "Не выбран"
    default selected_sprites = set(zip(espe_editor_data.p_displayable_names, espe_editor_data.p_displayable_list))
    default selected_amount = len(selected_sprites)

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        xanchor 0.5
        xpos 0.125
        yoffset 10

        text "Изображение частиц" xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"
        text "Раздел: {}".format(current_section_name) xalign 0.5 style "espe_text_heading_24_0xalign"
        text espe_properties_divider_huge style "espe_text_24"

    fixed:
        area (0.0, 0.25, 0.25, 0.65)
        viewport id "particle_section":
            draggable True
            mousewheel True
            scrollbars None

            has vbox:
                spacing 5

                for index, section in enumerate(particle_list):
                    textbutton section[0] style "espe_button" text_style "espe_button_text_24":
                        sensitive section_index != index
                        action [SetScreenVariable("section_index", index), SetScreenVariable("current_section_name", section[0])]
            
            add Null(width=480)
    
    if section_index > -1:
        $ section_length = len(particle_list[section_index])

        add Solid("#000", xsize=0.2, ysize=0.96) at fast_pos_alpha(0.28, 0.04, 0.4)

        vbox:
            at fast_pos_05anchor(0.38, 0.154)

            text espe_properties_divider_huge style "espe_text_24"
            text "Невыбранные".format(current_section_name) xalign 0.5 style "espe_text_heading_24_0xalign"
            text espe_properties_divider_huge style "espe_text_24"

        fixed:
            area (0.28, 0.25, 0.2, 0.65)
            viewport id "particle_displ":
                draggable True
                mousewheel True
                scrollbars None

                has vbox:
                    spacing 5

                    for index in range(1, section_length):
                        $ prt_name = particle_list[section_index][index][0]
                        $ prt_source = particle_list[section_index][index][1]
                        textbutton espe_sprite_left_right_arrow(prt_name, True) style "espe_button" text_style "espe_button_text_24":
                            hovered [Show("ESPE_particle_displayable_subscreen", displayable=prt_source)]
                            unhovered Hide("ESPE_particle_displayable_subscreen")
                            sensitive not espe_sprite_in_selected(prt_name, selected_sprites)
                            action [AddToSet(selected_sprites, (prt_name, prt_source)),
                                    SetScreenVariable("selected_amount", selected_amount + 1),
                                    Hide("ESPE_particle_displayable_subscreen")]
                
                add Null(width=384)

        vbar:
            value YScrollValue("particle_displ")
            style "espe_scrollbar"
            xalign 0.265
            yalign 0.5

    add Solid("#000", xsize=0.2, ysize=0.96) at fast_pos_alpha(0.51, 0.04, 0.4)

    vbox:
        at fast_pos_05anchor(0.61, 0.154)

        text espe_properties_divider_huge style "espe_text_24"
        text "Выбранные".format(current_section_name) xalign 0.5 style "espe_text_heading_24_0xalign"
        text espe_properties_divider_huge style "espe_text_24"

    fixed:
        area (0.51, 0.25, 0.2, 0.65)
        viewport id "particle_selected":
            draggable True
            mousewheel True
            scrollbars None

            has vbox:
                spacing 5

                for prt_name, prt_source in selected_sprites:
                    textbutton espe_sprite_left_right_arrow(prt_name, False) style "espe_button" text_style "espe_button_text_24":
                        hovered Show("ESPE_particle_displayable_subscreen", displayable=prt_source)
                        unhovered Hide("ESPE_particle_displayable_subscreen")
                        action [RemoveFromSet(selected_sprites, (prt_name, prt_source)), SetScreenVariable("selected_amount", selected_amount - 1),
                                Hide("ESPE_particle_displayable_subscreen")]
            
            add Null(width=384)

    textbutton "Завершить выбор" style "espe_button" text_style "espe_button_text_36" at fast_pos_05anchor(0.61, 0.976):
        sensitive selected_amount > 0
        action [Show("ESPE_editor_main_properties"),
                Function(espe_set_sprite_list, editor_data=espe_editor_data, sprite_list=selected_sprites)]
        
    vbar:
        value YScrollValue("particle_selected")
        style "espe_scrollbar"
        xalign 0.498
        yalign 0.5

    vbar:
        value YScrollValue("particle_section")
        style "espe_scrollbar"
        yalign 0.5

    textbutton "Назад" xmaximum 0.2 yalign 1.0 xalign 0.09 style "espe_button" text_style "espe_button_text_36":
        action Show("ESPE_editor_main_properties")
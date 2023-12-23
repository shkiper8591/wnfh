screen ESPE_editor_optimization_properties():
    tag espe_editor_main

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.125, 0.07)

        text "Оптимизация" xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"

    vbox:
        at fast_pos_05anchor(0.125, 0.5)

        textbutton "Максимальное быстродействие {}".format(espe_get_property_check(espe_editor_data.p_inner_frame_check)) style "espe_button" text_style "espe_button_text_24" text_size 22:
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_inner_frame_check_opt"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [ToggleField(espe_editor_data, "p_inner_frame_check"),
                    Function(espe_update_dtime_func),
                    Hide("ESPE_editor_hint")
                    ]
        textbutton "Значение: {:0.3f} секунд.".format(espe_editor_data.p_update_time) style "espe_button" text_style "espe_button_text_24":
                    hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_update_time_opt"]))
                    unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                    action [Show("ESPE_editor_input", obj=espe_editor_data, field="p_update_time", max_length=5,
                                field_type=float, clamp_range=(0.0, 1.0), exclude=espe_input_exclude_letters, force_update_attr_func=espe_update_update_time),
                            Hide("ESPE_editor_hint")]
        bar:
            value FieldValue(espe_editor_data, "p_update_time", 1.0,
                            action=Function(espe_update_update_time))
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_update_time_opt"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            style "espe_property_bar"
            xsize 0.18
        
        text espe_properties_divider style "espe_text_24"

        textbutton "Гибель за экраном {}".format(espe_get_property_check(espe_editor_data.p_is_screen_bounded)) style "espe_button" text_style "espe_button_text_24":
            hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["p_out_of_bounds_opt"]))
            unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
            action [ToggleField(espe_editor_data, "p_is_screen_bounded"),
                    Function(espe_update_screen_bounded_property),
                    Hide("ESPE_editor_hint")
                    ]
        
        text espe_properties_divider style "espe_text_24"
    
    textbutton "Назад" style "espe_button" text_style "espe_button_text_36" at fast_pos_05anchor(0.125, 0.95):
        mouse "ESPE_cursor_choice"
        action [Show("ESPE_editor_main_menu"),
                SetField(espe_scene_editor_data, "last_p_editor_screen", "ESPE_editor_main_menu")]
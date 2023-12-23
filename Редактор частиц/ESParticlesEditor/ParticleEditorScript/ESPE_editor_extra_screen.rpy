screen ESPE_editor_extra(minimized):
    tag espe_editor_extra

    $ enable_particles_text = "Отключить частицы" if espe_particles_show else "Включить частицы"

    fixed:
        xalign 1.0
        add Solid("#000", ysize=0.04) alpha 0.4
        
        hbox:
            xalign 1.0
            yalign 0.0
            spacing 20

            textbutton "Открыть папку с утилитой" style "espe_button" text_style "espe_button_text_24":
                action Function(espe_open_mod_directory)

            textbutton "Главное меню" style "espe_button" text_style "espe_button_text_24":
                action Show("ESPE_go_to_main_menu_caution")

            textbutton enable_particles_text style "espe_button" text_style "espe_button_text_24":
                sensitive espe_editor_data.psystem_screen is not None
                action Function(espe_show_particles)

            textbutton "Перезагрузить частицы" style "espe_button" text_style "espe_button_text_24":
                sensitive espe_editor_data.psystem_object is not None and espe_particles_show
                hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["psystem_force_update"]))
                unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                action Function(espe_editor_psystem_force_update)

            textbutton "Редактор частиц" style "espe_button" text_style "espe_button_text_24":
                sensitive espe_scene_editor_data.is_scene_editor is True
                action [Show(espe_scene_editor_data.last_p_editor_screen), ToggleField(espe_scene_editor_data, "is_scene_editor")]

            textbutton "Редактор сцены" style "espe_button" text_style "espe_button_text_24":
                action [Show(espe_scene_editor_data.last_scene_editor_screen), ToggleField(espe_scene_editor_data, "is_scene_editor")]
                sensitive espe_scene_editor_data.is_scene_editor is False

            textbutton "Дополнительно" style "espe_button" text_style "espe_button_text_24":
                action Show("ESPE_editor_extra", minimized=not minimized)

    if not minimized:
        add Solid("#000", xsize=0.2, ysize=0.3) at fast_align_alpha(1.0, 0.057, 0.4)

        grid 2 3:
            xalign 1.0
            yalign 0.0
            yoffset 50
            xoffset 140
            xspacing -161
            yspacing 20

            textbutton "Подсказки........................" style "espe_button" text_style "espe_button_text_24":
                action ToggleVariable("persistent.enable_hints")
            text espe_get_property_check(persistent.enable_hints) yoffset 5 style "espe_text_24"

            textbutton "Узнать позицию................" style "espe_button" text_style "espe_button_text_24":
                hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["position_picker"]))
                unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                action Function(espe_enable_position_picker)
            text espe_get_property_check(espe_position_picker_enable) yoffset 5 style "espe_text_24"

            textbutton "Счётчик кадров................" style "espe_button" text_style "espe_button_text_24":
                action Function(espe_enable_fps_counter)
            text espe_get_property_check(espe_fps_counter_enable) yoffset 5 style "espe_text_24"

screen ESPE_go_to_main_menu_caution():
    modal True
    tag got_main_menu_caution

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)
    add Solid ("#000", xsize=0.25, ysize=0.35) at fast_align_alpha(0.5, 0.5, 0.4)

    text "Вы уверены, что хотите выйти в главное меню? Система останется прежней, пока вы не выйдете из игры или не загрузите другую. Однако рекомендуется сохранить систему." xmaximum 0.24 style "espe_text_24" at fast_pos_05anchor(0.5, 0.5)

    text espe_properties_divider_huge yalign 0.7 xalign 0.5 style "espe_text_heading_36"

    hbox:
        xalign 0.5
        yalign 0.73
        spacing 10

        textbutton "Выйти" xmaximum 0.3 style "espe_button" text_style "espe_button_text_36":
            action [Hide("ESPE_editor_extra"),
                    Hide("ESPE_go_to_main_menu_caution"),
                    Jump("smooth_exit_to_main_menu"),
                    Return(True), With(Dissolve(0.5))]

        textbutton "Назад" xmaximum 0.3 style "espe_button" text_style "espe_button_text_36":
            action Hide("ESPE_go_to_main_menu_caution")
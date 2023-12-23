
screen ESPE_scene_editor_main():
    tag espe_editor_main
    
    add Solid("#000", xsize=0.2, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.1, 0.07)
        text "Сцена" style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"

    vbox:
        at fast_pos_05anchor(0.1, 0.5)

        spacing 20

        textbutton "Фон" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_scene_editor_background"),
                    SetField(espe_scene_editor_data, "last_scene_editor_screen", "ESPE_scene_editor_background")]
        textbutton "Спрайты" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_scene_editor_sprites_main"),
                    SetField(espe_scene_editor_data, "last_scene_editor_screen", "ESPE_scene_editor_sprites_main")]
        
        text espe_properties_divider style "espe_text_24"

        textbutton "Звуковая сцена" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_scene_editor_sounds_main"),
                    SetField(espe_scene_editor_data, "last_scene_editor_screen", "ESPE_scene_editor_sounds_main")]

        text espe_properties_divider style "espe_text_24"

        textbutton "Информация о сцене" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            action Show("ESPE_scene_general_data")

        text espe_properties_divider style "espe_text_24"

        textbutton "Сохранить сцену" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            action Show("ESPE_save_scene_input")
        
        textbutton "Загрузить сцену" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            action [Function(espe_list_scenes_files), Show("ESPE_load_scene_choice")]

    
screen ESPE_scene_editor_background():
    tag espe_editor_main

    $ background = espe_scene_editor_data.background

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.125, 0.07)
        text "Фон сцены" xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"

    fixed:
        area (0.0, 0.13, 0.25, 0.7)
        viewport id "background_prop":
            draggable True
            mousewheel True
            scrollbars None
        
            has grid 1 31:
                yspacing None

                text "Изображение" style "espe_text_24"
                textbutton background.displayable style "espe_button" text_style "espe_button_text_24" text_size 18:
                        action [Show("ESPE_scene_editor_background_cg_choice_start"),
                                SetField(espe_scene_editor_data, "last_scene_editor_screen", "ESPE_scene_editor_background_cg_choice_start")]

                text espe_properties_divider style "espe_text_24"

                textbutton "Сбросить настройки" style "espe_button" text_style "espe_button_text_24":
                        action Function(background.reset_transform)
                
                text espe_properties_divider style "espe_text_24"

                text "Горизонтальное смещение" style "espe_text_24" size 22
                text "Значение: {}".format(background.xoffset - config.screen_width) style "espe_text_24"
                bar:
                    value FieldValue(background, "xoffset", range=config.screen_width * 2)
                    style "espe_property_bar"
                textbutton "Сбросить горизонтальное смещение" style "espe_button" text_style "espe_button_text_24" text_size 18:
                        action SetField(background, "xoffset", config.screen_width)
                
                text espe_properties_divider style "espe_text_24"

                text "Вертикальное смещение" style "espe_text_24" size 22
                text "Значение: {}".format(background.yoffset - config.screen_height) style "espe_text_24"
                bar:
                    value FieldValue(background, "yoffset", range=config.screen_height * 2)
                    style "espe_property_bar"
                textbutton "Сбросить вертикальное смещение" style "espe_button" text_style "espe_button_text_24" text_size 18:
                        action SetField(background, "yoffset", config.screen_height)
                
                text espe_properties_divider style "espe_text_24"

                text "Непрозрачность" style "espe_text_24"
                textbutton "Значение: {:0.3}".format(background.alpha) style "espe_button" text_style "espe_button_text_24":
                        action Show("ESPE_scene_editor_input", obj=background, field="alpha", field_type=float, clamp_range=(0.0, 1.0), max_length=3, exclude=espe_input_exclude_letters)
    
                bar:
                    value FieldValue(background, "alpha", range=1.0, action=Show("ESPE_scene", data=espe_scene_editor_data))
                    style "espe_property_bar"
                textbutton "Сбросить непрозрачность" style "espe_button" text_style "espe_button_text_24" text_size 20:
                        action SetField(background, "alpha", 1.0)

                text espe_properties_divider style "espe_text_24"

                text "Масштаб" style "espe_text_24"
                textbutton "Значение: {:0.3}".format(background.zoom) style "espe_button" text_style "espe_button_text_24":
                        action Show("ESPE_scene_editor_input", obj=background, field="zoom", field_type=float, clamp_range=(0.0, 10.0), max_length=3, exclude=espe_input_exclude_letters)
                bar:
                    value FieldValue(background, "zoom", range=10.0)
                    style "espe_property_bar"
                textbutton "Сбросить масштаб" style "espe_button" text_style "espe_button_text_24" text_size 20:
                        action SetField(background, "zoom", 1.0)
                
                text espe_properties_divider style "espe_text_24"

                text "Угол" style "espe_text_24"
                textbutton "Значение: {}°".format(background.rotate) style "espe_button" text_style "espe_button_text_24":
                        action Show("ESPE_scene_editor_input", obj=background, field="rotate", field_type=int, clamp_range=(0, 360), max_length=3, exclude=espe_input_exclude_letters + ".")
                bar:
                    value FieldValue(background, "rotate", range=360, action=Show("ESPE_scene", data=espe_scene_editor_data))
                    style "espe_property_bar"
                textbutton "Сбросить угол" style "espe_button" text_style "espe_button_text_24":
                        action SetField(background, "rotate", 0)
                
                text espe_properties_divider style "espe_text_24"

            add Null(width=480)

    vbar:
        value YScrollValue("background_prop")
        style "espe_scrollbar"
        yalign 0.5

    textbutton "Назад" yalign 1.0 xalign 0.09 style "espe_button" text_style "espe_button_text_36":
        action [Show("ESPE_scene_editor_main"),
                SetField(espe_scene_editor_data, "last_scene_editor_screen", "ESPE_scene_editor_main")]

screen ESPE_scene_editor_background_cg_choice_start():
    tag espe_editor_main
    
    add Solid("#000", xsize=0.2, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.1, 0.5)


        first_spacing 100
        spacing 20

        text "Выбор заднего фона" style "espe_text_heading_36" size 34

        textbutton "Фоны" style "espe_button" text_style "espe_button_text_24":
            action Show("ESPE_scene_editor_background_cg_choice", cg_bg_list=ESPE_static_bg_list)
        textbutton "Иллюстрации" style "espe_button" text_style "espe_button_text_24":
            action Show("ESPE_scene_editor_background_cg_choice", cg_bg_list=ESPE_static_cg_list, cg=True)
    
    textbutton "Назад" yalign 1.0 xalign 0.09 style "espe_button" text_style "espe_button_text_36":
        action [Show("ESPE_scene_editor_background"),
                SetField(espe_scene_editor_data, "last_scene_editor_screen", "ESPE_scene_editor_background")]

screen ESPE_scene_editor_background_cg_choice(cg_bg_list, cg=False):
    tag espe_editor_main

    $ background = espe_scene_editor_data.background

    if cg is False:
        $ section_offset = 55
        $ choice_yalign = 0.34
    else:
        $ section_offset = 155
        $ choice_yalign = 0.34

    default section_index = -1
    default section_page_index = 0
    default current_section_name = "Не выбран"

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)
    add Solid("#000", xsize=0.735, ysize=0.3) at fast_align_alpha(1.0, 0.5, 0.4)

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.07

        text "Выбор изображения фона" style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"
        text "Раздел: {}".format(current_section_name) style "espe_text_heading_24"
        text espe_properties_divider_huge style "espe_text_24"

    fixed:
        area (0.0, 0.25, 1.0, 0.65)
        viewport id "cg_bg_section":
            xalign 0.05
            xoffset section_offset
            draggable True
            mousewheel True
            scrollbars None

            has vbox:
                spacing 5

                for index, section in enumerate(cg_bg_list):
                    textbutton section[0] style "espe_button" text_style "espe_button_text_24":
                        sensitive section_index != index
                        action [SetScreenVariable("section_index", index), SetScreenVariable("current_section_name", section[0]),
                                SetScreenVariable("section_page_index", 0)]
        
        if section_index >= 0:
            hbox:
                xoffset 577
                yalign choice_yalign

                spacing 15

                $ list_len = len(cg_bg_list[section_index][1])
                $ first_cg_bg_ind_on_page = section_page_index * 3
                for index in range(first_cg_bg_ind_on_page, espe_simple_min(first_cg_bg_ind_on_page + 3, list_len)):
                    if espe_get_elem_by_index_safe(cg_bg_list[section_index][1] , index) is not None:
                        vbox:
                            spacing 5
                            add cg_bg_list[section_index][1][index][1] zoom 0.215
                            textbutton cg_bg_list[section_index][1][index][0] xmaximum 0.3 style "espe_button" text_style "espe_button_text_24":
                                action [SetField(background, "displayable", cg_bg_list[section_index][1][index][1]), Show("ESPE_scene_editor_background")]
            
            textbutton "❮" style "espe_button" text_style "espe_button_text_36" xalign 0.27 yalign 0.36 text_size 72:
                sensitive section_page_index > 0
                action (SetScreenVariable("section_page_index", section_page_index - 1))

            textbutton "❯" style "espe_button" text_style "espe_button_text_36" xalign 1.0 yalign 0.36 text_size 72:
                sensitive section_page_index < (list_len + 2) // 3 - 1
                action (SetScreenVariable("section_page_index", section_page_index + 1))
    
    vbar:
        value YScrollValue("cg_bg_section")
        style "espe_scrollbar"
        yalign 0.6

    textbutton "Назад" style "espe_button" text_style "espe_button_text_36" at fast_pos_05anchor(0.1, 0.973):
        action Show("ESPE_scene_editor_background_cg_choice_start")

screen ESPE_scene_editor_sprites_main():
    tag espe_editor_main

    $ espe_scene_editor = espe_scene_editor_data
    $ sprite_list = espe_scene_editor_data.sprite_list

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.125, 0.07)

        text "Активные спрайты" xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.1

        text espe_properties_divider style "espe_text_24"

        textbutton "Добавить новый спрайт" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            action [Function(espe_scene_editor.add_sprite), Function(espe_scene_editor.sort_by_zorder)]

        text espe_properties_divider style "espe_text_24"

        text "Список спрайтов" xalign 0.5 style "espe_text_heading_36"

    fixed:
        area (0.0, 0.26, 0.25, 0.8)
        viewport id "sprites":
            draggable True
            mousewheel True
            scrollbars None

            has vbox:
                if not sprite_list:
                    text "Спрайтов ещё нет..." style "espe_text_24"
                else:
                    for spr in sprite_list:
                        textbutton spr.special_name style "espe_button" text_style "espe_button_text_24":
                            hovered Function(spr.hovered)
                            unhovered Function(spr.unhovered)
                            action [Show("ESPE_scene_editor_sprite", chosen_sprite=spr), Function(spr.unhovered)]

            add Null(width=480)

    vbar:
        value YScrollValue("sprites")
        style "espe_scrollbar"
        yalign 0.5
    
    textbutton "Назад" yalign 1.0 xalign 0.09 style "espe_button" text_style "espe_button_text_36":
        action [Show("ESPE_scene_editor_main"),
                SetField(espe_scene_editor_data, "last_scene_editor_screen", "ESPE_scene_editor_main")]

screen ESPE_scene_editor_sprite(chosen_sprite=None):
    tag espe_editor_main

    $ espe_scene_editor = espe_scene_editor_data
    default spr = chosen_sprite

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.125, 0.07)

        text "Свойства: {}".format(spr.special_name) xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"

    fixed:
        area (0.0, 0.15, 0.25, 0.75)
        viewport id "sprite_prop":
            draggable True
            mousewheel True
            scrollbars None
        
            has grid 1 43:
                yspacing None

                text espe_properties_divider style "espe_text_24"

                textbutton "Удалить спрайт" style "espe_button" text_style "espe_button_text_24":
                        action Function(espe_scene_editor.remove_sprite, spr_obj=spr), Show("ESPE_scene_editor_sprites_main")

                text espe_properties_divider style "espe_text_24"

                textbutton "Сбросить настройки" style "espe_button" text_style "espe_button_text_24":
                        action Function(spr.reset_transform)

                text espe_properties_divider style "espe_text_24"

                text "Имя" style "espe_text_24"
                textbutton spr.special_name style "espe_button" text_style "espe_button_text_24":
                        action Show("ESPE_scene_editor_input", obj=spr, field="special_name", field_type=str, max_length=24)

                text espe_properties_divider style "espe_text_24"

                text "Изображение" style "espe_text_24"
                textbutton spr.displayable style "espe_button" text_style "espe_button_text_24":
                        action Show("ESPE_sprite_selector", chosen_sprite=chosen_sprite)

                text espe_properties_divider style "espe_text_24"

                text "Цветокоррекция" style "espe_text_24"
                textbutton espe_sprite_tint_list[spr.tint_index][0] style "espe_button" text_style "espe_button_text_24":
                        action Function(spr.set_tint_cycle)

                text espe_properties_divider style "espe_text_24"

                text "Горизонтальное смещение" style "espe_text_24" size 22
                text "Значение: {}".format(spr.xoffset - config.screen_width) style "espe_text_24"
                bar:
                    value FieldValue(spr, "xoffset", range=config.screen_width * 2)
                    style "espe_property_bar"
                textbutton "Сбросить горизонтальное смещение" style "espe_button" text_style "espe_button_text_24" text_size 18:
                        action SetField(spr, "xoffset", config.screen_width)
                
                text espe_properties_divider style "espe_text_24"

                text "Вертикальное смещение" style "espe_text_24" size 22
                text "Значение: {}".format(spr.yoffset - config.screen_height) style "espe_text_24"
                bar:
                    value FieldValue(spr, "yoffset", range=config.screen_height * 2)
                    style "espe_property_bar"
                textbutton "Сбросить вертикальное смещение" style "espe_button" text_style "espe_button_text_24" text_size 18:
                        action SetField(spr, "yoffset", config.screen_height)
                
                text espe_properties_divider style "espe_text_24"

                text "Непрозрачность" style "espe_text_24"
                textbutton "Значение: {:0.3}".format(spr.alpha) style "espe_button" text_style "espe_button_text_24":
                        action Show("ESPE_scene_editor_input", obj=spr, field="alpha", field_type=float, clamp_range=(0.0, 1.0), max_length=3, exclude=espe_input_exclude_letters)
                bar:
                    value FieldValue(spr, "alpha", range=1.0)
                    style "espe_property_bar"
                textbutton "Сбросить непрозрачность" style "espe_button" text_style "espe_button_text_24" text_size 20:
                        action SetField(spr, "alpha", 1.0)

                text espe_properties_divider style "espe_text_24"

                text "Масштаб" style "espe_text_24"
                textbutton "Значение: {:0.3}".format(spr.zoom) style "espe_button" text_style "espe_button_text_24":
                        action Show("ESPE_scene_editor_input", obj=spr, field="zoom", field_type=float, clamp_range=(0.0, 10.0), max_length=3, exclude=espe_input_exclude_letters)    
                bar:
                    value FieldValue(spr, "zoom", range=10.0, action=Show("ESPE_scene", data=espe_scene_editor_data))
                    style "espe_property_bar"
                textbutton "Сбросить масштаб" style "espe_button" text_style "espe_button_text_24" text_size 20:
                        action SetField(spr, "zoom", 1.0)
                
                text espe_properties_divider style "espe_text_24"

                text "Угол" style "espe_text_24"
                textbutton "Значение: {}°".format(spr.rotate) style "espe_button" text_style "espe_button_text_24":
                        action Show("ESPE_scene_editor_input", obj=spr, field="rotate", field_type=int, clamp_range=(0, 360), max_length=3, exclude=espe_input_exclude_letters + ".")
                bar:
                    value FieldValue(spr, "rotate", range=360, action=Show("ESPE_scene", data=espe_scene_editor_data))
                    style "espe_property_bar"
                textbutton "Сбросить угол" style "espe_button" text_style "espe_button_text_24":
                        action SetField(spr, "rotate", 0)
                
                text espe_properties_divider style "espe_text_24"

                text "Порядок наложения" style "espe_text_24"
                textbutton "Значение: {}".format(spr.zorder) style "espe_button" text_style "espe_button_text_24":
                        hovered If(persistent.enable_hints, true=Show("ESPE_editor_hint", hint=ESPE_hints_describe_dict["scene_zorder"]))
                        unhovered If(persistent.enable_hints, true=Hide("ESPE_editor_hint"))
                        action [Show("ESPE_scene_editor_input", obj=spr, field="zorder", field_type=int, clamp_range=(-100, 100), max_length=4, exclude=espe_input_exclude_letters + ".", update_func=espe_scene_editor.sort_by_zorder),
                                Hide("ESPE_editor_hint")]
                
                text espe_properties_divider style "espe_text_24"
            
            add Null(width=480)

    vbar:
        value YScrollValue("sprite_prop")
        style "espe_scrollbar"
        yalign 0.5

    textbutton "Назад" yalign 1.0 xalign 0.09 style "espe_button" text_style "espe_button_text_36":
        action Show("ESPE_scene_editor_sprites_main")
    
screen ESPE_sprite_selector(chosen_sprite):
    tag espe_editor_main

    default sprite_index = -1
    default sprite_emote_index = 1
    default sprite_emote_page_index = 0
    default sprite_page_index = 0
    default current_sprite_name = "Не выбран"

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)
    add Solid("#000", xsize=0.75, ysize=0.04) at fast_align_alpha(1.0, 0.397, 0.4)
    add Solid("#000", xsize=0.735, ysize=0.55) at fast_align_alpha(1.0, 1.0, 0.4)

    text "Выбор изображения спрайта" style "espe_text_heading_36" size 30 at fast_pos_05anchor(0.125, 0.07)

    text "Спрайт: {}".format(current_sprite_name) style "espe_text_heading_36" at fast_pos_05anchor(0.125, 0.193)

    fixed:
        area (0.0, 0.25, 1.0, 0.65)
        viewport id "sprite_selector":
            xalign 0.05
            xoffset 155
            draggable True
            mousewheel True
            scrollbars None

            has vbox:
                spacing 5

                for index, name in enumerate(ESPE_static_sprites_list):
                    textbutton name[0] style "espe_button" text_style "espe_button_text_24":
                        sensitive sprite_index != index
                        action [SetScreenVariable("sprite_index", index), SetScreenVariable("current_sprite_name", name[0]), SetScreenVariable("sprite_emote_index", 1),
                                SetScreenVariable("sprite_emote_page_index", 0), SetScreenVariable("sprite_page_index", 0)]

    if sprite_index >= 0:
        hbox:
            xalign 0.74
            yalign 0.395
            spacing 25

            $ list_len_emotes = len(ESPE_static_sprites_list[sprite_index])
            $ first_emote_ind_on_page = sprite_emote_page_index * 6
            for index in range(first_emote_ind_on_page + 1, espe_simple_min(first_emote_ind_on_page + 7, list_len_emotes)):
                textbutton ESPE_static_sprites_list[sprite_index][index][0] xmaximum 0.3 style "espe_button" text_style "espe_button_text_24":
                    sensitive sprite_emote_index != index
                    action [SetScreenVariable("sprite_emote_index", index), SetScreenVariable("sprite_page_index", 0)]

        
        textbutton "❮" style "espe_button" text_style "espe_button_text_36" xalign 0.251 yalign 0.392:
            sensitive sprite_emote_page_index > 0
            action (SetScreenVariable("sprite_emote_page_index", sprite_emote_page_index - 1))

        textbutton "❯" style "espe_button" text_style "espe_button_text_36" xalign 1.0 yalign 0.392:
            sensitive sprite_emote_page_index < (list_len_emotes // 7)
            action (SetScreenVariable("sprite_emote_page_index", sprite_emote_page_index + 1))     
                
    if sprite_index >= 0:
        hbox:
            xoffset 562
            yalign 1.0

            spacing -50

            $ list_len = len(ESPE_static_sprites_list[sprite_index][sprite_emote_index][1])
            $ first_sprite_ind_on_page = sprite_page_index * 3
            for index in range(first_sprite_ind_on_page, espe_simple_min(first_sprite_ind_on_page + 3, list_len)):
                if espe_get_elem_by_index_safe(ESPE_static_sprites_list[sprite_index][sprite_emote_index][1] , index) is not None:
                    vbox:
                        spacing -250
                        add Crop((0.0, 0.0, 850, 1080), ESPE_static_sprites_list[sprite_index][sprite_emote_index][1][index][1]) zoom 0.55
                        textbutton ESPE_static_sprites_list[sprite_index][sprite_emote_index][1][index][0] style "espe_button" text_style "espe_button_text_36":
                            action [SetField(chosen_sprite, "displayable", ESPE_static_sprites_list[sprite_index][sprite_emote_index][1][index][1]), Show("ESPE_scene_editor_sprite", chosen_sprite=chosen_sprite)]
        
        textbutton "❮" style "espe_button" text_style "espe_button_text_36" xalign 0.27 yalign 0.75 text_size 72:
            sensitive sprite_page_index > 0
            action (SetScreenVariable("sprite_page_index", sprite_page_index - 1))

        textbutton "❯" style "espe_button" text_style "espe_button_text_36" xalign 1.0 yalign 0.75 text_size 72:
            sensitive sprite_page_index < (len(ESPE_static_sprites_list[sprite_index][sprite_emote_index][1]) + 2) // 3 - 1
            action (SetScreenVariable("sprite_page_index", sprite_page_index + 1))

    vbar:
        value YScrollValue("sprite_selector")
        style "espe_scrollbar"
        yalign 0.5
    

    textbutton "Назад" yalign 1.0 xalign 0.09 style "espe_button" text_style "espe_button_text_36":
        action Show("ESPE_scene_editor_sprite", chosen_sprite=chosen_sprite)

screen ESPE_scene_editor_sounds_main():
    tag espe_editor_main

    $ data = espe_scene_editor_data
    
    add Solid("#000", xsize=0.2, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.1, 0.07)
        text "Звуковая сцена" xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"

    vbox:
        at fast_pos_05anchor(0.1, 0.5)
        spacing 10

        textbutton "Отключить всё" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            sensitive data.is_music_ambience_active() is True
            action Function(data.turn_off_music_ambience)

        textbutton "Музыка" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            action Show("ESPE_scene_editor_audio_choice", audio_dict=espe_music_list, channel_name="music", section_name="Список музыки")

        textbutton "Пользовательская музыка" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            sensitive persistent.custom_music_dict
            action Show("ESPE_scene_editor_audio_choice", audio_dict=persistent.custom_music_dict, channel_name="music", section_name="Список пользовательской музыки")

        text espe_properties_divider style "espe_text_24"
        
        textbutton "Окружение" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            action Show("ESPE_scene_editor_audio_choice", audio_dict=espe_ambience_list, channel_name="ambience", section_name="Список окружения")

        textbutton "Пользовательское Окружение" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            sensitive persistent.custom_ambience_dict
            action Show("ESPE_scene_editor_audio_choice", audio_dict=persistent.custom_ambience_dict, channel_name="ambience", section_name="Список пользовательского окружения")
        
    textbutton "Назад" yalign 1.0 xalign 0.065 style "espe_button" text_style "espe_button_text_36":
        action [Show("ESPE_scene_editor_main"),
                SetField(espe_scene_editor_data, "last_scene_editor_screen", "ESPE_scene_editor_main")]

screen ESPE_scene_editor_audio_choice(audio_dict, channel_name, section_name):
    tag espe_editor_main

    $ espe_scene_editor = espe_scene_editor_data

    if section_name == "Список музыки":
        $ section_offset = 20
    elif section_name == "Список пользовательской музыки":
        $ section_offset = -20
    elif section_name == "Список окружения":
        $ section_offset = -10
    else:
        $ section_offset = -20

    add Solid("#000", xsize=0.25, ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.4)

    vbox:
        at fast_pos_05anchor(0.125, 0.07)
        
        text section_name xalign 0.5 style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_24"

    vbox:
        xanchor 0.5
        xpos 0.125
        ypos 0.15

        text espe_properties_divider style "espe_text_24"
        
        textbutton "Прекратить воспроизведение" xalign 0.5 style "espe_button" text_style "espe_button_text_24":
            action Function(espe_scene_editor.stop_channel, channel_name=channel_name)

        text espe_properties_divider style "espe_text_24"

    fixed:
        area (0.0, 0.3, 0.25, 0.6)
        viewport id "audio_data":
            draggable True
            mousewheel True
            scrollbars None

            has vbox:
                for name, src in audio_dict.items():
                    $ beautiful_name = beautifuly_string(name)
                    textbutton beautiful_name style "espe_button" text_style "espe_button_text_24" text_size 18:
                        action Function(espe_scene_editor.play_channel, src=src, channel_name=channel_name, audio_name=beautiful_name)

            add Null(width=480)

    vbar:
        value YScrollValue("audio_data")
        style "espe_scrollbar"
        yalign 0.7
    
    textbutton "Назад" yalign 1.0 xalign 0.09 style "espe_button" text_style "espe_button_text_36":
        action Show("ESPE_scene_editor_sounds_main")

screen ESPE_save_scene_input(def_name="Моя сцена"):
    modal True
    tag espe_editor_main

    default filename_value = def_name

    $ data = espe_scene_editor_data
    $ background = espe_scene_editor_data.background

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)
    add Solid("#000", xsize=0.3, ysize=0.2) at fast_align_alpha(0.5, 0.9, 0.5)
    add Solid("#000", xsize=0.5, ysize=0.5) at fast_align_alpha(0.5, 0.25, 0.5)

    vbox:
        xalign 0.5
        yalign 0.05

        text "Параметры сцены" style "espe_text_heading_36"
        text espe_properties_divider_huge style "espe_text_heading_36"

    fixed:
        area (0.25, 0.125, 0.6, 0.48)
        viewport id "scene_save_info":
            xalign 0.05
            xoffset 10
            draggable True
            mousewheel True
            scrollbars None

            has vbox:
                text "Фон" xalign 0.1 style "espe_text_heading_36"
                text "Название фона: {}.".format(background.displayable) style "espe_text_24_0align"
                text "Горизонтальное смещение фона: {} пикселей.".format(background.xoffset - config.screen_width) style "espe_text_24_0align"
                text "Вертикальное смещение фона: {} пикселей.".format(background.yoffset - config.screen_height) style "espe_text_24_0align"
                text "Непрозрачность: {}%.".format(int(background.alpha * 100)) style "espe_text_24_0align"
                text "Масштаб: {}.".format(background.zoom) style "espe_text_24_0align"
                text "Угол поворота: {}°.".format(background.rotate) style "espe_text_24_0align"

                text "Звуковая сцена" xalign 0.1 style "espe_text_heading_36"
                text "Музыка: {}.".format(data.get_sound_name("music")) style "espe_text_24_0align"
                text "Окружение: {}.".format(data.get_sound_name("ambience")) style "espe_text_24_0align"

                text "Спрайты" xalign 0.1 style "espe_text_heading_36"
                text "Количество спрайтов: {}.".format(data.get_sprite_list_length()) style "espe_text_24_0align"
                
                if data.sprite_list:
                    text "Список спрайтов" style "espe_text_heading_36" xalign 0.1
                    text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                    for spr in data.sprite_list:
                        text "Название спрайта: {}.".format(spr.special_name) style "espe_text_24_0align"
                        text "Изображение спрайта: {}.".format(spr.displayable) style "espe_text_24_0align"
                        text "Цветокоррекция: {}.".format(spr.get_tint_name()) style "espe_text_24_0align"
                        text "Горизонтальное смещение спрайта: {} пикселей.".format(spr.xoffset - config.screen_width) style "espe_text_24_0align"
                        text "Вертикальное смещение спрайта: {} пикселей.".format(spr.yoffset - config.screen_height) style "espe_text_24_0align"
                        text "Непрозрачность: {}%.".format(int(spr.alpha * 100)) style "espe_text_24_0align"
                        text "Масштаб: {}.".format(spr.zoom) style "espe_text_24_0align"
                        text "Угол поворота: {}°.".format(spr.rotate) style "espe_text_24_0align"
                        text "Порядок наложения: {}.".format(spr.zorder) style "espe_text_24_0align"
                        text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

    vbar:
        value YScrollValue("scene_save_info")
        style "espe_scrollbar"
        yalign 0.4
        xalign 0.77
    
    text espe_properties_divider_huge yalign 0.65 xalign 0.5 style "espe_text_heading_36"

    vbox:
        xalign 0.5
        yalign 0.8
        first_spacing 50
        spacing 20

        text "Введите название сцены" xmaximum 0.3 style "espe_text_heading_36"

        input:
            value AdvancedScreenVariableInputValue(variable="filename_value", var_type=str, exclude=None, returnable=False)
            length 24
            xmaximum 0.3
            size 24
            xalign 0.5
            yoffset 60

        textbutton "Сохранить" xmaximum 0.3 yoffset 90 style "espe_button" text_style "espe_button_text_36":
            action [Hide("ESPE_save_scene_input"),
                    If(espe_check_file_on_exist(filename_value, espe_scene_saves_dict),
                        true=Show("ESPE_save_scene_exist_caution", stored_name=filename_value),
                        false=[Function(espe_save_scene, filename=filename_value), Show("ESPE_scene_editor_main"), Show("ESPE_saved_loaded_notify", is_save=True)])]
        
    textbutton "Назад" yalign 0.98 style "espe_button" text_style "espe_button_text_36":
        action Show("ESPE_scene_editor_main")

screen ESPE_save_scene_exist_caution(stored_name):
    modal True
    tag espe_editor_main

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)
    add Solid("#000", xsize=0.3, ysize=0.2) at fast_align_alpha(0.5, 0.5, 0.5)

    text "Такое название сцены уже используется! Перезаписать файл?" xmaximum 0.3 xalign 0.5 yalign 0.5 style "espe_text_heading_36"

    text espe_properties_divider_huge yalign 0.625 xalign 0.5 style "espe_text_heading_36"

    hbox:
        xalign 0.5
        yalign 0.655
        spacing 10

        textbutton "Перезаписать" xmaximum 0.3 style "espe_button" text_style "espe_button_text_36":
            action [Function(espe_save_scene, filename=stored_name), Show("ESPE_scene_editor_main"), Show("ESPE_saved_loaded_notify", is_save=True)]

        textbutton "Назад" xmaximum 0.3 style "espe_button" text_style "espe_button_text_36":
            action Show("ESPE_save_scene_input", def_name=stored_name)

screen ESPE_load_scene_choice():
    tag espe_editor_main

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)
    add Solid("#000", xsize=0.5, ysize=0.5) at fast_align_alpha(0.5, 0.5, 0.4)

    vbox:
        xalign 0.5
        yalign 0.125

        text "Сохранённые сцены" style "espe_text_heading_36"

        text espe_properties_divider_huge style "espe_text_heading_36"

        textbutton "Обновить список" xmaximum 0.3 style "espe_button" text_style "espe_button_text_36":
            action Function(espe_list_scenes_files)
    
    fixed:
        area (0.25, 0.26, 0.49, 0.48)
        viewport id "scene_files":
            xalign 0.05
            xoffset 10
            draggable True
            mousewheel True
            scrollbars None

            has vbox:
                for filename, filepath in espe_scene_saves_dict.items():
                    hbox:
                        spacing 5
                        text filename style "espe_text_24"
                        text ">>" style "espe_text_24"
                        textbutton "Загрузить" style "espe_button" text_style "espe_button_text_24":
                            action [SetVariable("espe_special_label_data", filepath), Jump("ESPE_load_scene_from_file")]
                        text "|" style "espe_text_24"
                        textbutton "Информация" style "espe_button" text_style "espe_button_text_24":
                            action Show("ESPE_load_scene_view", file_data=espe_get_data_from_scene_file(filepath=filepath))
    
    vbar:
        value YScrollValue("scene_files")
        style "espe_scrollbar"
        yalign 0.5
        xalign 0.77

    text espe_properties_divider_huge yalign 0.79 xalign 0.5 style "espe_text_heading_36"

    textbutton "Назад" yalign 0.83 xalign 0.5 style "espe_button" text_style "espe_button_text_36":
        action Show("ESPE_scene_editor_main")

screen ESPE_load_scene_view(file_data):
    tag espe_editor_main

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)

    if file_data is None:
        add Solid("#000", xsize=0.5, ysize=0.2) at fast_align_alpha(0.5, 0.5, 0.4)

        text "Не удалось прочитать файл!" xalign 0.5 yalign 0.5 style "espe_text_heading_36"

        textbutton "Назад" xalign 0.5 yalign 0.6 style "espe_button" text_style "espe_button_text_36":
                action Show("ESPE_load_scene_choice")

    else:
        $ data = file_data
        $ filename = data[0]
        $ background_data = data[1]
        $ audio_data = data[2]
        $ general_srpites_data = data[3]
        $ sprites_data = data[4]

        add Solid("#000", xsize=0.5, ysize=0.5) at fast_align_alpha(0.5, 0.5, 0.4)

        vbox:
            xalign 0.5
            yalign 0.18

            text "Параметры сцены" style "espe_text_heading_36"
            text espe_properties_divider_huge style "espe_text_heading_36"

        fixed:
            area (0.25, 0.26, 0.49, 0.48)
            viewport id "scene_general_data":
                xalign 0.05
                xoffset 10
                draggable True
                mousewheel True
                scrollbars None

                has vbox:
                    text "Файл сцены" xalign 0.1 style "espe_text_heading_36"
                    text "Сцена: {}.".format(filename) style "espe_text_24_0align"
                    text "Фон" xalign 0.1 style "espe_text_heading_36"
                    text "Название фона: {}.".format(background_data[0]) style "espe_text_24_0align"
                    text "Горизонтальное смещение фона: {} пикселей.".format(background_data[1]) style "espe_text_24_0align"
                    text "Вертикальное смещение фона: {} пикселей.".format(background_data[2]) style "espe_text_24_0align"
                    text "Непрозрачность: {}%.".format(int(background_data[3] * 100)) style "espe_text_24_0align"
                    text "Масштаб: {}.".format(background_data[4]) style "espe_text_24_0align"
                    text "Угол поворота: {}°.".format(background_data[5]) style "espe_text_24_0align"

                    text "Звуковая сцена" xalign 0.1 style "espe_text_heading_36"
                    text "Музыка: {}.".format(audio_data[0]) style "espe_text_24_0align"
                    text "Окружение: {}.".format(audio_data[2]) style "espe_text_24_0align"

                    text "Спрайты" xalign 0.1 style "espe_text_heading_36"
                    if general_srpites_data[0] > 0:
                        text "Количество спрайтов: {}.".format(general_srpites_data[0]) style "espe_text_24_0align"
                    else: 
                        text "Спрайтов на сцене нет." style "espe_text_24_0align"
                    
                    if sprites_data:
                        text "Список спрайтов" style "espe_text_heading_36" xalign 0.1
                        text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

                        for spr in sprites_data:
                            text "Название спрайта: {}.".format(spr[0]) style "espe_text_24_0align"
                            text "Изображение спрайта: {}.".format(spr[1]) style "espe_text_24_0align"
                            text "Цветокоррекция: {}.".format(spr[2]) style "espe_text_24_0align"
                            text "Горизонтальное смещение спрайта: {} пикселей.".format(spr[4]) style "espe_text_24_0align"
                            text "Вертикальное смещение спрайта: {} пикселей.".format(spr[5]) style "espe_text_24_0align"
                            text "Непрозрачность: {}%.".format(int(spr[6] * 100)) style "espe_text_24_0align"
                            text "Масштаб: {}.".format(spr[7]) style "espe_text_24_0align"
                            text "Угол поворота: {}°.".format(spr[8]) style "espe_text_24_0align"
                            text "Порядок наложения: {}.".format(spr[9]) style "espe_text_24_0align"
                            text espe_properties_divider_huge style "espe_text_heading_36" xalign 0.1

        vbar:
            value YScrollValue("scene_general_data")
            style "espe_scrollbar"
            yalign 0.5
            xalign 0.77
        
        text espe_properties_divider_huge yalign 0.79 xalign 0.5 style "espe_text_heading_36"

        hbox:
            xalign 0.5
            yalign 0.83
            spacing 10

            textbutton "Загрузить сцену" style "espe_button" text_style "espe_button_text_36":
                action [Show("ESPE_scene_editor_main"), Function(espe_load_scene_from_data, data=data, _update_screens=False),
                        Show("ESPE_saved_loaded_notify", is_save=False)]

            textbutton "Назад" style "espe_button" text_style "espe_button_text_36":
                action Show("ESPE_load_scene_choice")

screen ESPE_load_scene_fail():
    tag espe_editor_main

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)
    add Solid("#000", xsize=0.5, ysize=0.96) at fast_align_alpha(0.5, 1.0, 0.5)

    text "Не удалось открыть файл сцены!\nФайл повреждён или содержит неправильный синтаксис для анализа." xmaximum 0.5 style "espe_text_heading_36" at fast_align(0.5, 0.5)

    textbutton "Назад" yalign 0.96 xalign 0.5 style "espe_button" text_style "espe_button_text_36":
        action Show("ESPE_load_scene_choice")

screen ESPE_scene(data):
    layer "master"
    tag espe_scene

    add data.background.displayable:
        xalign 0.5
        yalign 0.5

        xoffset data.background.xoffset - config.screen_width
        yoffset data.background.yoffset - config.screen_height

        alpha data.background.alpha
        zoom data.background.zoom

        rotate data.background.rotate
            
    
    for spr in data.sprite_list:
        add spr.displayable:
            xalign 0.5
            yalign 0.5

            matrixcolor spr.tint

            xoffset spr.xoffset - config.screen_width
            yoffset spr.yoffset - config.screen_height

            alpha spr.alpha
            zoom spr.zoom

            rotate spr.rotate               

screen ESPE_scene_editor_input(obj, field, field_type, clamp_range=None, max_length=24, exclude=None, offset=0, update_func=None):
    modal True
    tag espe_input

    default field_value = str(getattr(obj, field))

    on 'hide' action If(espe_input_safe_check(field_value, field_type, obj, field),
                        true=[SetField(obj, field, espe_clamp(espe_field_type_safe(field_value, field_type), clamp_range)), Show("ESPE_scene", data=espe_scene_editor_data)])
    

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)
    add Solid("#000", xsize=0.3, ysize=0.2) at fast_align_alpha(0.5, 0.5, 0.5)
    vbox:
        xalign 0.5
        yalign 0.5
        first_spacing 50
        spacing 20

        text "Введите значение аттрибута" xmaximum 0.3 style "espe_text_heading_36"

        input:
            value AdvancedScreenVariableInputValue(variable="field_value", var_type=str, exclude=exclude, returnable=False)
            length max_length
            xmaximum 0.3
            size 24
            at fast_align(0.5, 0.5)

        textbutton "Завершить редактирование" xmaximum 0.3 style "espe_button" text_style "espe_button_text_24" at fast_align(0.5, 0.5):
            action [Hide("ESPE_scene_editor_input"),
                    If(update_func is not None, true=Function(update_func))]
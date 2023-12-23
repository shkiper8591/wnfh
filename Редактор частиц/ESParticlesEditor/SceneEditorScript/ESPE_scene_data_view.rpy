
screen ESPE_scene_general_data():
    tag espe_editor_main

    $ data = espe_scene_editor_data
    $ background = espe_scene_editor_data.background

    add Solid("#000", ysize=0.96) at fast_align_alpha(0.0, 1.0, 0.2)
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
        value YScrollValue("scene_general_data")
        style "espe_scrollbar"
        yalign 0.5
        xalign 0.77
    
    text espe_properties_divider_huge yalign 0.79 xalign 0.5 style "espe_text_heading_36"

    textbutton "Назад" xmaximum 0.2 yalign 0.83 xalign 0.5 style "espe_button" text_style "espe_button_text_36":
        action [Show("ESPE_scene_editor_main"),
                SetField(espe_scene_editor_data, "last_scene_editor_screen", "ESPE_scene_editor_main")]
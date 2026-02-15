screen wnfh_load(main_menu = False):

    #modal True

    $ debug_frame = {
        "black":     frame_black      if persistent.wnfh_debug_color else frame_transparent,
        "red":       frame_red        if persistent.wnfh_debug_color else frame_transparent,
        "green":     frame_green      if persistent.wnfh_debug_color else frame_transparent,
        "blue":      frame_blue       if persistent.wnfh_debug_color else frame_transparent,
        "purple":    frame_purpl      if persistent.wnfh_debug_color else frame_transparent,
        "yellow":    frame_yellow     if persistent.wnfh_debug_color else frame_transparent,
        "turquoise": frame_turquoise  if persistent.wnfh_debug_color else frame_transparent,
    }

    default wnfh_button_states = [False for i in range(1)]

    python:
        wnfh_bars = {
            "tumb": [im.MatrixColor(wnfh_frames_elements["settings_bar_tumb"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["settings_bar_tumb"][4], renpy.store.wnfh_tymeofday)))],

            "bar_full": [im.Composite(
                (25, 25),
                (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_full"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["settings_bar_full"][4], renpy.store.wnfh_tymeofday))),
                (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_null"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["settings_bar_null"][4], renpy.store.wnfh_tymeofday))),
                )],
            "bar_null": [im.Composite(
                (25, 25),
                (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_bg"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["settings_bar_bg"][4], renpy.store.wnfh_tymeofday))),
                (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_null"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["settings_bar_null"][4], renpy.store.wnfh_tymeofday))),
                )],
        }
        save_load_elements = [
            ["chapter"  ,"Глава 1"          ],
            ["date"     ,"12 июля 1989г"    ],
            ["filetime" ,"04/05/2025 15:12" ]
        ]
        if main_menu:
            wnfh_preferences_button = [
                ["back", "Назад", [ShowMenu('main_menu'), Hide('load')]]
            ]
        else:
            wnfh_preferences_button = [
                ["back", "Назад", [ShowMenu('game_menu_selector'), Hide('load')]]
            ]

        mm_backgrounds = {
            "night":  wnfh_gui["main_menu"]["mm_bg_night"],
            "sunset": wnfh_gui["main_menu"]["mm_bg_sunset"],
            "day":    wnfh_gui["main_menu"]["mm_bg_day"],
        }

    if main_menu:
        default current_hour = wnfh_get_usertime("hour") # ======================= Главное меню подстраивается под время суток компьютера

        default time_period = (
            "night"  if (current_hour >= 22 or current_hour < 8) else
            "sunset" if (current_hour < 12)                      else
            "day"    if (current_hour < 19)                      else
            "sunset"
        )

        frame:
            background mm_backgrounds[time_period] # ================== Фон в главном меню
            area(0.0, 0.0, 1.0, 1.0)

    if main_menu:
        add wnfh_gui["main_menu"]["vignette"]
        for index, button in enumerate(wnfh_preferences_button[0:1]): # ================================================ Кнопка Назад
            frame:
                area(0.1, 0.08, 150, 60)
                xanchor 0.5 yanchor 0.5
                background debug_frame["blue"] 
                vbox: # ================================================ Вбокс кнопок
                    pos (0.5, 0.5)
                    xanchor 0.5 yanchor 0.5
                    spacing 0
                    for element in ["back_button_line", "back_button_bg", "back_button_line"]:
                        frame:
                            if persistent.wnfh_debug_color:
                                background wnfh_frames_elements[element][5]
                            else:
                                background frame_transparent 
                            area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                            add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
        
                frame: # ================================================ Тонировка при наведении
                    if wnfh_button_states[index]:
                        add Frame(wnfh_frames_elements["back_button_gradient"][0], left=wnfh_frames_elements["back_button_gradient"][3], top=0):
                            xalign 0.5 yalign 0.5 alpha 0.6
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["back_button_gradient"][4]])
                        add Frame(wnfh_frames_elements["back_button_gradient"][0], left=wnfh_frames_elements["back_button_gradient"][3], top=0):
                            xalign 0.5 yalign 0.5 alpha 0.1
                    else:
                        null height 20
                    area(0.5, 0.5, wnfh_frames_elements["back_button_bg"][1], wnfh_frames_elements["back_button_bg"][2]) padding(0, 0) xanchor 0.5 yanchor 0.5
                    background debug_frame["purple"]
        
                    textbutton button[1]: # ================================================ Текст кнопок
                        style "wnfh_buttons"
                        text_style "wnfh_text_" + renpy.store.wnfh_tymeofday
                        hovered ToggleDict(wnfh_button_states, index)
                        unhovered ToggleDict(wnfh_button_states, index)
                        action button[2]
                        at wnfh_mm_button_hover_atl()
        
        frame at atl_wnfh_widget_lp_down: # ============================ Заголовок
            area(0.5, 0.08, wnfh_frames_elements["settings_main_title_bg"][1] + 40, wnfh_frames_elements["settings_main_title_bg"][2] + 20)
            xanchor 0.5 yanchor 0.5
            background debug_frame["black"]
            vbox: # ================================================ Фон таблички из трёх кусков
                pos (0.5, 0.5)
                xanchor 0.5 yanchor 0.5
                spacing 0
                for element in ["settings_main_title_line", "settings_main_title_bg", "settings_main_title_line"]:
                    frame:
                        if persistent.wnfh_debug_color:
                            background wnfh_frames_elements[element][5]
                        else:
                            background frame_transparent 
                        area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]]) 
        
            text "Загрузить":
                style "wnfh_title_1_" + renpy.store.wnfh_tymeofday

        frame at govno_ebanoe2:
            area(0.5, 0.97, 1.0, 0.8)
            xanchor 0.5 yanchor 1.0
            background debug_frame["black"]
            vbox: # ================================================ Фон таблички из трёх кусков
                pos (0.5, 0.5)
                xanchor 0.5 yanchor 0.5
                spacing 0
                for element in ["save_load_box_line", "save_load_box_bg", "save_load_box_line"]:
                    frame at wnfh_frames_elements[element][6]:
                    #frame:
                        if persistent.wnfh_debug_color:
                            background wnfh_frames_elements[element][5]
                        else:
                            background frame_transparent
                        area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
    frame at wjuh_bg:
        area(0.5, 0.11, 0.98, 0.85)
        xanchor 0.5 yanchor 0.0
        background debug_frame["black"]
        viewport id "load":
            draggable True
            mousewheel True
            scrollbars None
            vbox:
                pos (0.5, 0.5)
                xanchor 0.5 yanchor 0.5
                spacing 5
                for slot_num in range(10):
                    $ slot_info = wnfh_get_slot_extra_data("{}-{}".format("WNFH_Saves", slot_num))
                    button:
                        background "#0000"
                        action FileLoad(name = slot_num, page = "WNFH_Saves")
                        frame:
                            area (0.5, 0.0, wnfh_frames_elements["save_load_element_bg"][1] + 40, wnfh_frames_elements["save_load_element_bg"][2] + 20)
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["purple"]
                            if slot_info:
                                imagebutton:
                                    pos (0.99, 0.5)
                                    xanchor 0.0 yanchor 0.5
                                    idle Transform(wnfh_gui["tint_elements"]["trash"],  matrixcolor = TintMatrix(wnfh_tint_color[ renpy.store.wnfh_tymeofday][0]))
                                    hover Transform(wnfh_gui["tint_elements"]["trash"], matrixcolor = TintMatrix(wnfh_tint_color[ renpy.store.wnfh_tymeofday][1]))
                                    action FileDelete(name = slot_num, page = "WNFH_Saves")
                            else:
                                text str(slot_num + 1) + ". Пустой слот":
                                    style "wnfh_text_" + renpy.store.wnfh_tymeofday
                            vbox: # ================================================ Фон таблички из трёх кусков
                                pos (0.5, 0.5)
                                xanchor 0.5 yanchor 0.5
                                spacing 0
                                for element in ["save_load_element_line", "save_load_element_bg", "save_load_element_line"]:
                                    frame at wnfh_frames_elements[element][6]:
                                    #frame:
                                        if persistent.wnfh_debug_color:
                                            background wnfh_frames_elements[element][5]
                                        else:
                                            background frame_transparent
                                        area (0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
                            
                            vbox:
                                pos (0.03, 0.5)
                                xanchor 0.0 yanchor 0.5
                                spacing 1
                                if not slot_info:
                                    frame:
                                        area (0.5, 0.5, 300, wnfh_frames_elements["save_load_element_bg"][2]/3)
                                        xanchor 0.5 yanchor 0.5
                                        background debug_frame["blue"]
                                else:
                                    frame:
                                        area (0.5, 0.5, 300, wnfh_frames_elements["save_load_element_bg"][2]/3)
                                        xanchor 0.5 yanchor 0.5
                                        background debug_frame["blue"]
                                        text slot_info["chapter"]:
                                            style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                    frame:
                                        area (0.5, 0.5, 300, wnfh_frames_elements["save_load_element_bg"][2]/3)
                                        xanchor 0.5 yanchor 0.5
                                        background debug_frame["blue"]
                                        text slot_info["game_date"]:
                                            style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                    frame:
                                        area (0.5, 0.5, 300, wnfh_frames_elements["save_load_element_bg"][2]/3)
                                        xanchor 0.5 yanchor 0.5
                                        background debug_frame["blue"]
                                        text FileTime(name = str(slot_num), format = '%d/%m/%y | %H:%M', page = "WNFH_Saves"):
                                            style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                            #size 10
                            frame:
                                area (0.97, 0.5, 300, wnfh_frames_elements["save_load_element_bg"][2])
                                xanchor 1.0 yanchor 0.5
                                background debug_frame["red"]
                                if renpy.store.wnfh_tymeofday == "day":
                                    add FileScreenshot(slot_num, page="WNFH_Saves"):
                                        xoffset -6 yoffset -6
                                        size (300, 162)
                                else:
                                    add FileScreenshot(slot_num, page="WNFH_Saves"):
                                        xoffset -6 yoffset -6
                                        size (300, 162)
                                        matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][3])
                            vbox:
                                pos (0.5, 0.5)
                                xanchor 0.5 yanchor 0.5
                                spacing 2
                                if not slot_info:
                                    frame:
                                        area (0.5, 0.5, 1000, wnfh_frames_elements["save_load_element_bg"][2] * 1/3)
                                        xanchor 0.5 yanchor 0.5
                                        background debug_frame["green"]
                                        
                                else:
                                    frame:
                                        area (0.5, 0.5, 1000, wnfh_frames_elements["save_load_element_bg"][2] * 1/3)
                                        xanchor 0.5 yanchor 0.5
                                        background debug_frame["green"]
                                        if len(str(slot_info["scene"])) < 45:
                                            text slot_info["scene"]:
                                                style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                        elif len(str(slot_info["scene"])) >= 45:
                                            text slot_info["scene"]:
                                                style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                                size 20
                                if not slot_info:
                                    frame:
                                        area (0.5, 1.0, 1000, wnfh_frames_elements["save_load_element_bg"][2] * 2/3)
                                        xanchor 0.5 yanchor 1.0
                                        background debug_frame["purple"]
                                else:
                                    if persistent.wnfh_widget_lp == 0:
                                        frame:
                                            area (0.5, 1.0, 1000, wnfh_frames_elements["save_load_element_bg"][2] * 2/3)
                                            xanchor 0.5 yanchor 1.0
                                            background debug_frame["purple"]
                                            text "Виджет лавпоинтов отключен":
                                                style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                                size 20
                                    else:
                                        frame:
                                            area (0.5, 1.0, 1000, wnfh_frames_elements["save_load_element_bg"][2] * 2/3)
                                            xanchor 0.5 yanchor 1.0
                                            background debug_frame["purple"]
                                            hbox: # ================================================ Ебальники с очками
                                                spacing 5
                                                anchor (0.5, 0.5) pos (0.5, 0.5)
                                                
                                                $ character_with_img = [character for character in wnfh_character_order]
                                                for index, character in enumerate(character_with_img, start = 21 - len(character_with_img)):
                                                    frame:
                                                        background debug_frame["black"]
                                                        area(0.5, 0.5, 90, wnfh_frames_elements["widget_lp_box_bg"][2])
                                                        xanchor 0.5 yanchor 0.5
                                                        hbox: # ================================================ Ебальники с очками
                                                            spacing 0
                                                            anchor (0.5, 0.5) pos (0.5, 0.5)
                                                            frame: # ================================================ Ебальники
                                                                if persistent.wnfh_debug_color:
                                                                    background wnfh_characters[character][1]
                                                                else:
                                                                    background frame_transparent
                                                                area(0.0, 0.5, 40, 70)
                                                                xanchor 0.0 yanchor 0.5
                                                                if renpy.store.wnfh_tymeofday == "day":
                                                                    add (wnfh_gui["avatars"][character]):
                                                                        xalign 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
                                                                        zoom 0.05
                                                                else:
                                                                    add (wnfh_gui["avatars"][character]):
                                                                        matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][3])
                                                                        xalign 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
                                                                        zoom 0.05
                                
                                                            frame: # ================================================ Очки
                                                                background debug_frame["blue"]
                                                                area(1.0, 0.5, 40, 70)
                                                                xanchor 1.0 yanchor 0.5
                                                                text slot_info["lp_info"][character]:
                                                                    style "wnfh_lp_counter"
                                                                    color wnfh_characters[character][1]
                                                                    size 30
        frame:
            background debug_frame["green"]
            area(0.95, 0.5, 50, 1.0)
            xanchor 0.0 yanchor 0.5
            vbar value YScrollValue("load"):
                top_bar Frame(wnfh_bars["bar_null"][0], wnfh_frames_elements["logbook_vbar_null"][1], wnfh_frames_elements["logbook_vbar_null"][1])
                bottom_bar Frame(wnfh_bars["bar_null"][0], wnfh_frames_elements["logbook_vbar_null"][1], wnfh_frames_elements["logbook_vbar_null"][1])
                thumb wnfh_bars["tumb"][0]
                hover_thumb wnfh_bars["tumb"][0]
                xmaximum 33 ymaximum 1.0
                pos (0.5, 0.5)
                anchor (0.5, 0.5)
                
screen wnfh_save(main_menu = False):

    #modal True

    $ debug_frame = {
        "black":     frame_black      if persistent.wnfh_debug_color else frame_transparent,
        "red":       frame_red        if persistent.wnfh_debug_color else frame_transparent,
        "green":     frame_green      if persistent.wnfh_debug_color else frame_transparent,
        "blue":      frame_blue       if persistent.wnfh_debug_color else frame_transparent,
        "purple":    frame_purpl      if persistent.wnfh_debug_color else frame_transparent,
        "yellow":    frame_yellow     if persistent.wnfh_debug_color else frame_transparent,
        "turquoise": frame_turquoise  if persistent.wnfh_debug_color else frame_transparent,
    }

    default wnfh_button_states = [False for i in range(1)]

    python:
        wnfh_bars = {
            "tumb": [im.MatrixColor(wnfh_frames_elements["settings_bar_tumb"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["settings_bar_tumb"][4], renpy.store.wnfh_tymeofday)))],

            "bar_full": [im.Composite(
                (25, 25),
                (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_full"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["settings_bar_full"][4], renpy.store.wnfh_tymeofday))),
                (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_null"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["settings_bar_null"][4], renpy.store.wnfh_tymeofday))),
                )],
            "bar_null": [im.Composite(
                (25, 25),
                (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_bg"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["settings_bar_bg"][4], renpy.store.wnfh_tymeofday))),
                (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_null"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["settings_bar_null"][4], renpy.store.wnfh_tymeofday))),
                )],
        }
        save_load_elements = [
            ["chapter"  ,"Глава 1"          ],
            ["date"     ,"12 июля 1989г"    ],
            ["filetime" ,"04/05/2025 15:12" ]
        ]
        if main_menu:
            wnfh_preferences_button = [
                ["back", "Назад", [ShowMenu('main_menu'), Hide('save')]]
            ]
        else:
            wnfh_preferences_button = [
                ["back", "Назад", [ShowMenu('game_menu_selector'), Hide('save')]]
            ]

        mm_backgrounds = {
            "night":  wnfh_gui["main_menu"]["mm_bg_night"],
            "sunset": wnfh_gui["main_menu"]["mm_bg_sunset"],
            "day":    wnfh_gui["main_menu"]["mm_bg_day"],
        }

    if main_menu:
        default current_hour = wnfh_get_usertime("hour") # ======================= Главное меню подстраивается под время суток компьютера

        default time_period = (
            "night"  if (current_hour >= 22 or current_hour < 8) else
            "sunset" if (current_hour < 12)                      else
            "day"    if (current_hour < 19)                      else
            "sunset"
        )

        frame:
            background mm_backgrounds[time_period] # ================== Фон в главном меню
            area(0.0, 0.0, 1.0, 1.0)

    if main_menu:
        add wnfh_gui["main_menu"]["vignette"]
        for index, button in enumerate(wnfh_preferences_button[0:1]): # ================================================ Кнопка Назад
            frame:
                area(0.1, 0.08, 150, 60)
                xanchor 0.5 yanchor 0.5
                background debug_frame["blue"] 
                vbox: # ================================================ Вбокс кнопок
                    pos (0.5, 0.5)
                    xanchor 0.5 yanchor 0.5
                    spacing 0
                    for element in ["back_button_line", "back_button_bg", "back_button_line"]:
                        frame:
                            if persistent.wnfh_debug_color:
                                background wnfh_frames_elements[element][5]
                            else:
                                background frame_transparent 
                            area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                            add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
        
                frame: # ================================================ Тонировка при наведении
                    if wnfh_button_states[index]:
                        add Frame(wnfh_frames_elements["back_button_gradient"][0], left=wnfh_frames_elements["back_button_gradient"][3], top=0):
                            xalign 0.5 yalign 0.5 alpha 0.6
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["back_button_gradient"][4]])
                        add Frame(wnfh_frames_elements["back_button_gradient"][0], left=wnfh_frames_elements["back_button_gradient"][3], top=0):
                            xalign 0.5 yalign 0.5 alpha 0.1
                    else:
                        null height 20
                    area(0.5, 0.5, wnfh_frames_elements["back_button_bg"][1], wnfh_frames_elements["back_button_bg"][2]) padding(0, 0) xanchor 0.5 yanchor 0.5
                    background debug_frame["purple"]
        
                    textbutton button[1]: # ================================================ Текст кнопок
                        style "wnfh_buttons"
                        text_style "wnfh_text_" + renpy.store.wnfh_tymeofday
                        hovered ToggleDict(wnfh_button_states, index)
                        unhovered ToggleDict(wnfh_button_states, index)
                        action button[2]
                        at wnfh_mm_button_hover_atl()
        
        frame at atl_wnfh_widget_lp_down: # ============================ Заголовок
            area(0.5, 0.08, wnfh_frames_elements["settings_main_title_bg"][1] + 40, wnfh_frames_elements["settings_main_title_bg"][2] + 20)
            xanchor 0.5 yanchor 0.5
            background debug_frame["black"]
            vbox: # ================================================ Фон таблички из трёх кусков
                pos (0.5, 0.5)
                xanchor 0.5 yanchor 0.5
                spacing 0
                for element in ["settings_main_title_line", "settings_main_title_bg", "settings_main_title_line"]:
                    frame:
                        if persistent.wnfh_debug_color:
                            background wnfh_frames_elements[element][5]
                        else:
                            background frame_transparent 
                        area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]]) 
        
            text "Загрузить":
                style "wnfh_title_1_" + renpy.store.wnfh_tymeofday

        frame at govno_ebanoe2:
            area(0.5, 0.97, 1.0, 0.8)
            xanchor 0.5 yanchor 1.0
            background debug_frame["black"]
            vbox: # ================================================ Фон таблички из трёх кусков
                pos (0.5, 0.5)
                xanchor 0.5 yanchor 0.5
                spacing 0
                for element in ["save_load_box_line", "save_load_box_bg", "save_load_box_line"]:
                    frame at wnfh_frames_elements[element][6]:
                    #frame:
                        if persistent.wnfh_debug_color:
                            background wnfh_frames_elements[element][5]
                        else:
                            background frame_transparent
                        area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
    frame at wjuh_bg:
        area(0.5, 0.11, 0.98, 0.85)
        xanchor 0.5 yanchor 0.0
        background debug_frame["black"]
        viewport id "save":
            draggable True
            mousewheel True
            scrollbars None
            vbox:
                pos (0.5, 0.5)
                xanchor 0.5 yanchor 0.5
                spacing 5
                for slot_num in range(10):
                    $ slot_info = wnfh_get_slot_extra_data("{}-{}".format("WNFH_Saves", slot_num))
                    button:
                        background "#0000"
                        action wnfh_FileSave(name = slot_num, extra_info = wnfh_create_slot_extra_data(), page = "WNFH_Saves")
                        frame:
                            area (0.5, 0.0, wnfh_frames_elements["save_load_element_bg"][1] + 40, wnfh_frames_elements["save_load_element_bg"][2] + 20)
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["purple"]
                            if slot_info:
                                imagebutton:
                                    pos (0.99, 0.5)
                                    xanchor 0.0 yanchor 0.5
                                    idle Transform(wnfh_gui["tint_elements"]["trash"],  matrixcolor = TintMatrix(wnfh_tint_color[ renpy.store.wnfh_tymeofday][0]))
                                    hover Transform(wnfh_gui["tint_elements"]["trash"], matrixcolor = TintMatrix(wnfh_tint_color[ renpy.store.wnfh_tymeofday][1]))
                                    action FileDelete(name = slot_num, page = "WNFH_Saves")
                            else:
                                text str(slot_num + 1) + ". Пустой слот":
                                    style "wnfh_text_" + renpy.store.wnfh_tymeofday
                            vbox: # ================================================ Фон таблички из трёх кусков
                                pos (0.5, 0.5)
                                xanchor 0.5 yanchor 0.5
                                spacing 0
                                for element in ["save_load_element_line", "save_load_element_bg", "save_load_element_line"]:
                                    frame at wnfh_frames_elements[element][6]:
                                    #frame:
                                        if persistent.wnfh_debug_color:
                                            background wnfh_frames_elements[element][5]
                                        else:
                                            background frame_transparent
                                        area (0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
                            
                            vbox:
                                pos (0.03, 0.5)
                                xanchor 0.0 yanchor 0.5
                                spacing 1
                                if not slot_info:
                                    frame:
                                        area (0.5, 0.5, 300, wnfh_frames_elements["save_load_element_bg"][2]/3)
                                        xanchor 0.5 yanchor 0.5
                                        background debug_frame["blue"]
                                else:
                                    frame:
                                        area (0.5, 0.5, 300, wnfh_frames_elements["save_load_element_bg"][2]/3)
                                        xanchor 0.5 yanchor 0.5
                                        background debug_frame["blue"]
                                        text slot_info["chapter"]:
                                            style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                    frame:
                                        area (0.5, 0.5, 300, wnfh_frames_elements["save_load_element_bg"][2]/3)
                                        xanchor 0.5 yanchor 0.5
                                        background debug_frame["blue"]
                                        text slot_info["game_date"]:
                                            style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                    frame:
                                        area (0.5, 0.5, 300, wnfh_frames_elements["save_load_element_bg"][2]/3)
                                        xanchor 0.5 yanchor 0.5
                                        background debug_frame["blue"]
                                        text FileTime(name = str(slot_num), format = '%d/%m/%y | %H:%M', page = "WNFH_Saves"):
                                            style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                            #size 10
                            frame:
                                area (0.97, 0.5, 300, wnfh_frames_elements["save_load_element_bg"][2])
                                xanchor 1.0 yanchor 0.5
                                background debug_frame["red"]
                                add FileScreenshot(slot_num, page="WNFH_Saves"):
                                    xoffset -6 yoffset -6
                                    size (300, 162)
                            vbox:
                                pos (0.5, 0.5)
                                xanchor 0.5 yanchor 0.5
                                spacing 2
                                if not slot_info:
                                    frame:
                                        area (0.5, 0.5, 1000, wnfh_frames_elements["save_load_element_bg"][2] * 1/3)
                                        xanchor 0.5 yanchor 0.5
                                        background debug_frame["green"]
                                else:
                                    frame:
                                        area (0.5, 0.5, 1000, wnfh_frames_elements["save_load_element_bg"][2] * 1/3)
                                        xanchor 0.5 yanchor 0.5
                                        background debug_frame["green"]
                                        if len(str(slot_info["scene"])) < 45:
                                            text slot_info["scene"]:
                                                style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                        elif len(str(slot_info["scene"])) >= 45:
                                            text slot_info["scene"]:
                                                style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                                size 20
                                if not slot_info:
                                    frame:
                                        area (0.5, 1.0, 1000, wnfh_frames_elements["save_load_element_bg"][2] * 2/3)
                                        xanchor 0.5 yanchor 1.0
                                        background debug_frame["purple"]
                                else:
                                    if persistent.wnfh_widget_lp == 0:
                                        frame:
                                            area (0.5, 1.0, 1000, wnfh_frames_elements["save_load_element_bg"][2] * 2/3)
                                            xanchor 0.5 yanchor 1.0
                                            background debug_frame["purple"]
                                            text "Виджет лавпоинтов отключен":
                                                style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                                size 20
                                    else:
                                        frame:
                                            area (0.5, 1.0, 1000, wnfh_frames_elements["save_load_element_bg"][2] * 2/3)
                                            xanchor 0.5 yanchor 1.0
                                            background debug_frame["purple"]
                                            hbox: # ================================================ Ебальники с очками
                                                spacing 5
                                                anchor (0.5, 0.5) pos (0.5, 0.5)
                                                
                                                $ character_with_img = [character for character in wnfh_character_order]
                                                for index, character in enumerate(character_with_img, start = 21 - len(character_with_img)):
                                                    frame:
                                                        background debug_frame["black"]
                                                        area(0.5, 0.5, 90, wnfh_frames_elements["widget_lp_box_bg"][2])
                                                        xanchor 0.5 yanchor 0.5
                                                        hbox: # ================================================ Ебальники с очками
                                                            spacing 0
                                                            anchor (0.5, 0.5) pos (0.5, 0.5)
                                                            frame: # ================================================ Ебальники
                                                                if persistent.wnfh_debug_color:
                                                                    background wnfh_characters[character][1]
                                                                else:
                                                                    background frame_transparent
                                                                area(0.0, 0.5, 40, 70)
                                                                xanchor 0.0 yanchor 0.5
                                                                if renpy.store.wnfh_tymeofday == "day":
                                                                    add (wnfh_gui["avatars"][character]):
                                                                        xalign 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
                                                                        zoom 0.05
                                                                else:
                                                                    add (wnfh_gui["avatars"][character]):
                                                                        matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][3])
                                                                        xalign 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
                                                                        zoom 0.05
                                
                                                            frame: # ================================================ Очки
                                                                background debug_frame["blue"]
                                                                area(1.0, 0.5, 40, 70)
                                                                xanchor 1.0 yanchor 0.5
                                                                text slot_info["lp_info"][character]:
                                                                    style "wnfh_lp_counter"
                                                                    color wnfh_characters[character][1]
                                                                    size 30
        frame:
            background debug_frame["green"]
            area(0.95, 0.5, 50, 1.0)
            xanchor 0.0 yanchor 0.5
            vbar value YScrollValue("save"):
                top_bar Frame(wnfh_bars["bar_null"][0], wnfh_frames_elements["logbook_vbar_null"][1], wnfh_frames_elements["logbook_vbar_null"][1])
                bottom_bar Frame(wnfh_bars["bar_null"][0], wnfh_frames_elements["logbook_vbar_null"][1], wnfh_frames_elements["logbook_vbar_null"][1])
                thumb wnfh_bars["tumb"][0]
                hover_thumb wnfh_bars["tumb"][0]
                xmaximum 33 ymaximum 1.0
                pos (0.5, 0.5)
                anchor (0.5, 0.5)    



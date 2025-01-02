init 2:
    $ wnft_user_time = wnfh_get_usertime()

    screen wnfh_game_menu_selector():

        modal True tag menu

        $ debug_frame = {
            "black":  frame_black  if persistent.wnfh_debug_color else frame_transparent,
            "red":    frame_red    if persistent.wnfh_debug_color else frame_transparent,
            "green":  frame_green  if persistent.wnfh_debug_color else frame_transparent,
            "blue":   frame_blue   if persistent.wnfh_debug_color else frame_transparent,
            "purple": frame_purpl  if persistent.wnfh_debug_color else frame_transparent
        }

        default wnfh_button_states = [False for i in range(6)]

        on "show" action Function(update_usertime)
        
        python:
            wnfh_game_menu_selector_buttons = [
                ["В главное меню мода", [MainMenu(), SetDict(wnfh_button_states, 0, False)]                                           ],
                ["Схема",               [ShowMenu('wnfh_schematic')]                           ],
                ["Сохранить",           [ShowMenu('save')]                                     ],
                ["Загрузить",           [ShowMenu('load')]                                     ],
                ["Настройки",           [ShowMenu('preferences'), Hide('game_menu_selector')]  ],
                ["Выход из игры",       [ShowMenu('quit')]                                     ],
            ]

        add wnfh_gui["tint_elements"]["vignette"]

        if persistent.wnfh_widget_clock:
            frame at atl_wnfh_widget_clock: # =============================================== Часики
                background debug_frame["black"]
                area(0.9, 0.2, wnfh_frames_elements["widget_clock_box_bg"][1] + 40, wnfh_frames_elements["widget_clock_box_bg"][2] + 20)
                xanchor 0.5 yanchor 0.5
                vbox: # ================================================ Фон таблички из трёх кусков
                    pos (0.5, 0.5)
                    xanchor 0.5 yanchor 0.5
                    spacing 0
                    for element in ["widget_clock_box_line", "widget_clock_box_bg", "widget_clock_box_line"]:
                        #frame at wnfh_frames_elements[element][6]:
                        frame:
                            if persistent.wnfh_debug_color:
                                background wnfh_frames_elements[element][5]
                            else:
                                background frame_transparent
                            area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                            add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
                hbox:
                    spacing 5
                    anchor (0.5, 0.5) pos (0.5, 0.5)
                    for element in ["hour", "separator", "mins"]:
                        frame:
                            background debug_frame["black"]
                            area(0.0, 0.5, 22, 40)
                            xanchor 0.0 yanchor 0.5
                            text str(wnfh_get_usertime(element)):
                                xalign 0.5
                                style "wnfh_choice_" + renpy.store.wnfh_tymeofday
                                size 30
        
            timer 1:
                repeat True
                action Function(update_usertime)

        if persistent.wnfh_widget_music_player:
            frame at atl_wnfh_widget_music: # =============================================== Музыка
                background debug_frame["black"]
                area(0.286, 0.2, wnfh_frames_elements["widget_music_box_bg"][1] + 40, wnfh_frames_elements["widget_music_box_bg"][2] + 20)
                xanchor 0.5 yanchor 0.5
                vbox: # ================================================ Фон таблички из трёх кусков
                    pos (0.5, 0.5)
                    xanchor 0.5 yanchor 0.5
                    spacing 0
                    for element in ["widget_music_box_line", "widget_music_box_bg", "widget_music_box_line"]:
                        #frame at wnfh_frames_elements[element][6]:
                        frame:
                            if persistent.wnfh_debug_color:
                                background wnfh_frames_elements[element][5]
                            else:
                                background frame_transparent
                            area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                            add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
                text getMusicName():
                    xmaximum wnfh_frames_elements["widget_music_box_bg"][1]
                    xalign 0.5
                    style "wnfh_choice_" + renpy.store.wnfh_tymeofday
                    size 30
                    yoffset 2

        if persistent.wnfh_widget_lp:

            frame at atl_wnfh_widget_lp_down: # ================================================ Фрейм таблички
            #frame: # ================================================ Фрейм таблички
                area(0.5, 0.08, wnfh_frames_elements["widget_lp_box_bg"][1] + 40, wnfh_frames_elements["widget_lp_box_bg"][2] + 20)
                xanchor 0.5 yanchor 0.5
                background debug_frame["black"]
                vbox: # ================================================ Фон таблички из трёх кусков
                    pos (0.5, 0.5)
                    xanchor 0.5 yanchor 0.5
                    spacing 0
                    for element in ["widget_lp_box_line", "widget_lp_box_bg", "widget_lp_box_line"]:
                        #frame at wnfh_frames_elements[element][6]:
                        frame:
                            if persistent.wnfh_debug_color:
                                background wnfh_frames_elements[element][5]
                            else:
                                background frame_transparent
                            area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                            add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
                hbox: # ================================================ Ебальники с очками
                    spacing 5
                    anchor (0.5, 0.5) pos (0.5, 0.5)
                    $ character_order = ["kat", "un", "mi", "dv", "usw", "sl", "mt", "din", "sv", "mz"]
                    $ character_with_img = [character for character in character_order]
                    for index, character in enumerate(character_with_img, start = 21 - len(character_with_img)):
                        #frame at wnfh_frames_elements["widget_lp_box_bg"][6]:
                        frame:
                            background debug_frame["black"]
                            area(0.5, 0.5, 160, wnfh_frames_elements["widget_lp_box_bg"][2])
                            xanchor 0.5 yanchor 0.5
                            hbox: # ================================================ Ебальники с очками
                                spacing 0
                                anchor (0.5, 0.5) pos (0.5, 0.5)
                                frame: # ================================================ Ебальники
                                    if persistent.wnfh_debug_color:
                                        background wnfh_characters[character][1]
                                    else:
                                        background frame_transparent
                                    area(0.0, 0.5, 70, 90)
                                    xanchor 0.0 yanchor 0.5
                                    if renpy.store.wnfh_tymeofday == "day":
                                        add (wnfh_gui["avatars"][character]):
                                            xalign 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
                                            zoom 0.1
                                    else:
                                        add (wnfh_gui["avatars"][character]):
                                            matrixcolor TintMatrix(wnfh_choice_tint_color[renpy.store.wnfh_tymeofday][3])
                                            xalign 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
                                            zoom 0.1
                                frame: # ================================================ Очки
                                    background debug_frame["blue"]
                                    area(1.0, 0.5, 60, 90)
                                    xanchor 1.0 yanchor 0.5
                                    text str(wnfh_Data.getChoice_points_sum(character)):
                                        text_align 0.5
                                        xalign 0.5 yanchor 0.5 ypos 0.5
                                        style "wnfh_lp_counter"
                                        size 70
                                        color wnfh_characters[character][1]

        frame at govno_ebanoe: # ================================================ Фрейм кнопок
            area(0.5, 0.5, 600, 600)
            xanchor 0.5 yanchor 0.5
            background debug_frame["black"]
            vbox: # ================================================ Вбокс блока кнопок
                pos (0.5, 0.5)
                xanchor 0.5 yanchor 0.5
                spacing 5
                for index, button in enumerate(wnfh_game_menu_selector_buttons[0:6]):
                    frame at atl_wnfh_game_menu_selector(index): # ================================================ Фрейм, как один элемент вбокса
                        area(0.5, 0.5, 300, 60)
                        xanchor 0.5 yanchor 0.5
                        background debug_frame["blue"] 
                        vbox: # ================================================ Вбокс кнопок
                            pos (0.5, 0.5)
                            xanchor 0.5 yanchor 0.5
                            spacing 0
                            for element in ["game_menu_selector_button_line", "game_menu_selector_button_bg", "game_menu_selector_button_line"]:
                                frame:
                                    if persistent.wnfh_debug_color:
                                        background wnfh_frames_elements[element][5]
                                    else:
                                        background frame_transparent
                                    area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                                    add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                        matrixcolor TintMatrix(wnfh_choice_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])

                        frame: # ================================================ Тонировка при наведении
                            if wnfh_button_states[index]:
                                add Frame(wnfh_frames_elements["game_menu_selector_button_gradient"][0], left=wnfh_frames_elements["game_menu_selector_button_gradient"][3], top=0):
                                    xalign 0.5 yalign 0.5 alpha 0.6
                                    matrixcolor TintMatrix(wnfh_choice_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["game_menu_selector_button_gradient"][4]])
                                add Frame(wnfh_frames_elements["game_menu_selector_button_gradient"][0], left=wnfh_frames_elements["game_menu_selector_button_gradient"][3], top=0):
                                    xalign 0.5 yalign 0.5 alpha 0.1
                            else:
                                null height 20

                            area(0.5, 0.5, wnfh_frames_elements["game_menu_selector_button_bg"][1], wnfh_frames_elements["game_menu_selector_button_bg"][2]) padding(0, 0) xanchor 0.5 yanchor 0.5
                            background debug_frame["purple"]
                            textbutton button[0]: # ================================================ Текст кнопок
                                xalign 0.5 yanchor 0.5 ypos 0.5
                                text_line_leading 5 text_line_spacing 3
                                text_min_width 390
                                text_text_align 0.5
                                text_style "wnfh_choice_" + renpy.store.wnfh_tymeofday
                                yoffset 2
                                background None
                                hover_sound wnfh_gui["sound"]["plimp"]
                                hovered ToggleDict(wnfh_button_states, index)
                                unhovered ToggleDict(wnfh_button_states, index)
                                action button[1]
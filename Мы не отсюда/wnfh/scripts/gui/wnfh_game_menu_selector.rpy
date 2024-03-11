init 2:
    screen wnfh_game_menu_selector():

        modal True tag menu

        default wnfh_screen_1 = False
        default wnfh_screen_2 = False
        default wnfh_screen_3 = False
        default wnfh_screen_4 = False
        default wnfh_screen_5 = False
        default wnfh_screen_6 = False

        python:
            wnfh_screen_variable = [
                wnfh_screen_1,
                wnfh_screen_2,
                wnfh_screen_3,
                wnfh_screen_4,
                wnfh_screen_5,
                wnfh_screen_6,
            ]
            wnfh_screen_variable_string = list('wnfh_screen_' + str(i) for i in range(1, 7))

            wnfh_game_menu_selector_buttons = [
                ["В главное меню мода", [MainMenu()]                                           ],
                ["Схема",               [ShowMenu('wnfh_schematic')]                           ],
                ["Сохранить",           [ShowMenu('save')]                                     ],
                ["Загрузить",           [ShowMenu('load')]                                     ],
                ["Настройки",           [ShowMenu('preferences'), Hide('game_menu_selector')]  ],
                ["Выход из игры",       [ShowMenu('quit')]                                     ],
     
            ]
        #frame: # =============================================== Часики
        #    background background_color
        #    area(0.5, 0.03, 120, 40)
        #    xanchor 0.5 yanchor 0.5
        #    text wnfh_get_usertime():
        #        xalign 0.5
        #        style "wnfh_choice_" + persistent.timeofday
        #        size 30
        add wnfh_gui["tint_elements"]["vignette"]

        if persistent.wnfh_widget_lp:

            frame at atl_wnfh_widget_lp_down:
                background "#0000"
                area(0.5, 0.08, 1500, 100)
                xanchor 0.5 yanchor 0.5
                grid 1 3:
                    anchor (0.5, 0.5) pos (0.5, 0.5)
                    add (wnfh_gui["tint_elements"]["wl_line"]):
                        matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                        xalign 0.5 yanchor 1.0 ypos 1.0 xzoom 1.1
                    add (wnfh_gui["tint_elements"]["wl_bg"]):
                        matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][2])
                        xalign 0.5 xzoom 1.1
                    add (wnfh_gui["tint_elements"]["wl_line"]):
                        matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                        xalign 0.5 xzoom 1.1
                grid 10 1:
                    anchor (0.5, 0.5) pos (0.5, 0.5)
                    $ character_order = ["kat", "un", "mi", "dv", "usw", "sl", "mt", "din", "sv", "mz"]
                    $ character_with_img = [character for character in character_order]
                    for index, character in enumerate(character_with_img, start = 21 - len(character_with_img)):
                        frame:
                            background "#0000"
                            area(0.5, 0.5, 160, 80)
                            xanchor 0.5 yanchor 0.5
                            frame:
                                background "#0000"
                                area(0.0, 0.5, 80, 80)
                                xanchor 0.0 yanchor 0.5
                                if persistent.timeofday == "day":
                                    add (wnfh_gui["avatars"][character]):
                                        xalign 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
                                        zoom 0.1
                                else:
                                    add (wnfh_gui["avatars"][character]):
                                        matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][3])
                                        xalign 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
                                        zoom 0.1
                            frame:
                                background "#0000"
                                area(1.0, 0.5, 60, 80)
                                xanchor 1.0 yanchor 0.5
                                text str(wnfh_Data.getChoice_points_sum(character)):
                                    text_align 0.5
                                    xalign 0.5 yanchor 0.5 ypos 0.5
                                    style "wnfh_lp_counter"
                                    size 70
                                    color wnfh_characters[character][1]
                                #ui.text("%s: %d" % (wnfh_characters[character][0], wnfh_Data.getChoice_points_sum(character)), style="wnfh_lp_counter", color=wnfh_characters[character][1])
        frame:
            background "#0000"
            area(0.5, 0.5, 0.3, 0.5)
            xanchor 0.5 yanchor 0.5
            grid 1 6:
                anchor (0.5, 0.5) pos (0.5, 0.5)
                spacing 2

                for index, i in enumerate(wnfh_game_menu_selector_buttons[0:6]):
                        frame at atl_wnfh_game_menu_selector(index):
                            background "#0000"
                            area(0.5, 0.5, 1.0, 65)
                            #xanchor 0.5 yanchor 0.5

                            add (wnfh_gui["tint_elements"]["im_bg"]):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][2])
                                xalign 0.5
    
                            if wnfh_screen_variable[index]:

                                add (wnfh_gui["tint_elements"]["im_gradient"]):
                                    xalign 0.5 alpha 0.6
                                    matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][0])

                                add (wnfh_gui["tint_elements"]["im_gradient"]):
                                    xalign 0.5 alpha 0.1
                            else:
                                null height 20

                            add (wnfh_gui["tint_elements"]["im_line"]):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                                xalign 0.5 yanchor 1.0
        
                            add (wnfh_gui["tint_elements"]["im_line"]):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                                xalign 0.5 ypos 1.0 yanchor 0.0
    
                            textbutton i[0]:
                                text_line_leading 5 text_line_spacing 3
                                text_min_width 550
                                text_text_align 0.5
                                xalign 0.5 yanchor 0.5 ypos 0.5
                                text_style "wnfh_choice_" + persistent.timeofday
                                background None
                                hover_sound wnfh_gui["sound"]["plimp"]
                                hovered ToggleScreenVariable(wnfh_screen_variable_string[index])
                                unhovered ToggleScreenVariable(wnfh_screen_variable_string[index])
                                action (i[1])


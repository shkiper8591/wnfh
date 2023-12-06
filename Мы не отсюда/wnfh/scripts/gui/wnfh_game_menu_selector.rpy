init 2:
    screen wnfh_game_menu_selector():

        modal True tag menu

        default wnfh_screen_1 = False
        default wnfh_screen_2 = False
        default wnfh_screen_3 = False
        default wnfh_screen_4 = False
        default wnfh_screen_5 = False

        python:
            wnfh_screen_variable = [
                wnfh_screen_1,
                wnfh_screen_2,
                wnfh_screen_3,
                wnfh_screen_4,
                wnfh_screen_5,
            ]
            wnfh_screen_variable_string = list('wnfh_screen_' + str(i) for i in range(1, 6))

            wnfh_game_menu_selector_buttons = [
                ["В главное меню", [MainMenu()]                                           ],
                ["Сохранить",      [ShowMenu('save')]                                     ],
                ["Загрузить",      [ShowMenu('load')]                                     ],
                ["Настройки",      [ShowMenu('preferences'), Hide('game_menu_selector')]  ],
                ["Выход",          [ShowMenu('quit')]                                     ],
     
            ]
        frame:
                background background_color
                area(0.5, 0.03, 120, 40)
                xanchor 0.5 yanchor 0.5
                text wnfh_get_usertime():
                    xalign 0.5
                    style "wnfh_choice_" + persistent.timeofday
                    size 30
        frame:
            background #0000
            area(0.5, 0.5, 0.7, 0.8)
            xanchor 0.5 yanchor 0.5
            grid 1 5:
                anchor (0.5, 0.5) pos (0.5, 0.5)
                spacing 2

                for index,i in enumerate(wnfh_game_menu_selector_buttons[0:5]):
                    frame:
                        background #0000
                        area(0.5, 0.5, 1.0, 65)
                        xanchor 0.5 yanchor 0.5
    
                        add (wnfh_gui["ingame_menu"]["line"]):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                            xalign 0.5 yanchor 1.0
    
                        add (wnfh_gui["ingame_menu"]["bg"]):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][2])
                            xalign 0.5
    
                        if wnfh_screen_variable[index]:
                            add (wnfh_gui["ingame_menu"]["gradient"]):
                                xalign 0.5 alpha 0.6
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][0])
                            add (wnfh_gui["ingame_menu"]["gradient"]):
                                xalign 0.5 alpha 0.1
                        else:
                            null height 20
    
                        add (wnfh_gui["ingame_menu"]["line"]):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                            xalign 0.5 ypos 1.0 yanchor 0.0

                        textbutton i[0]:
                            text_line_leading 16 text_line_spacing 11
                            text_min_width 1100
                            text_text_align 0.5
                            xalign 0.5 yanchor 0.5 ypos 0.5
                            text_style "wnfh_choice_" + persistent.timeofday
                            background None
                            hover_sound wnfh_gui["sound"]["plimp"]
                            hovered ToggleScreenVariable(wnfh_screen_variable_string[index])
                            unhovered ToggleScreenVariable(wnfh_screen_variable_string[index])
                            action (i[1])

        add wnfh_gui["ingame_menu"]["vignette"]
        #button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()
    #
        #add get_image("gui/ingame_menu/"+timeofday+"/ingame_menu.png") xalign 0.5 yalign 0.5
        #imagemap:
        #    if _preferences.language == None:
        #        auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_%s.png") xalign 0.5 yalign 0.5
        #    elif _preferences.language == "spanish":
        #        auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_es_%s.png") xalign 0.5 yalign 0.5
        #    elif _preferences.language == "italian":
        #        auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_it_%s.png") xalign 0.5 yalign 0.5
        #    elif _preferences.language == "english":
        #        auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_en_%s.png") xalign 0.5 yalign 0.5
        #    elif _preferences.language == "chinese":
        #        auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_ch_%s.png") xalign 0.5 yalign 0.5
        #    elif _preferences.language == "japanese":
        #        auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_en_%s.png") xalign 0.5 yalign 0.5
        #    hotspot (0, 83, 660, 65) focus_mask None clicked MainMenu()
        #    hotspot (0, 148, 660, 65) focus_mask None clicked ShowMenu('save')
        #    hotspot (0, 213, 660, 65) focus_mask None clicked ShowMenu('load')
        #    hotspot (0, 278, 660, 65) focus_mask None clicked (ShowMenu('preferences'), Hide('game_menu_selector'))
        #    hotspot (0, 343, 660, 65) focus_mask None clicked ShowMenu('quit')
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
    default wnfh_button_states = [False for i in range(7)]
    

    
    python:
        wnfh_game_menu_selector_buttons = [
            
            ['wnfh_logbook'      ,"Дневник"      ,[ToggleScreen('wnfh_logbook')]                     ],
            ['wnfh_schematic'    ,"Схема"        ,[ToggleScreen('wnfh_schematic')]                   ],
            ['save'              ,"Сохранить"    ,[ToggleScreen('save')]                             ],
            ['load'              ,"Загрузить"    ,[ToggleScreen('load')]                             ],
            ['preferences'       ,"Настройки"    ,[ToggleScreen('preferences')]                      ],
            #['quit'              ,"Выход"       ,[ToggleScreen('quit')]                             ],
            ['yesno_prompt'      ,"Выход"        ,[MainMenu(), SetDict(wnfh_button_states, 0, False)]],
        ]

    add wnfh_gui["main_menu"]["vignette"]

    
    on "show" action ToggleScreen('wnfh_logbook')

    frame at govno_ebanoe2:
        area(0.5, 0.5, 1.0, 0.95)
        xanchor 0.5 yanchor 0.5
        background debug_frame["black"]
        frame:
            pos(0.5, 0.5)
            xanchor 0.5 yanchor 0.5
            xysize(wnfh_frames_elements["logbook_box_bg"][1], wnfh_frames_elements["logbook_box_bg"][2])
            background Frame(Transform(wnfh_frames_elements["logbook_box_bg"][0], matrixcolor = TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["logbook_box_bg"][4]])) , left = wnfh_frames_elements["logbook_box_bg"][3], top=0)
            foreground Frame(Transform(wnfh_frames_elements["logbook_box_double_line"][0], matrixcolor = TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["logbook_box_double_line"][4]])) , left = wnfh_frames_elements["logbook_box_double_line"][3], top=6)

        frame at govno_ebanoe: # ================================================ Фрейм кнопок
            area(0.5, 0.0, 1920, 80)
            xanchor 0.5 yanchor 0.0
            background debug_frame["black"]
            hbox: # ================================================ Хбокс блока кнопок
                pos (0.5, 0.5)
                xanchor 0.5 yanchor 0.5
                spacing 5
                for index, button in enumerate(wnfh_game_menu_selector_buttons[0:7]):
                    frame at atl_wnfh_game_menu_selector(index): # ================================================ Фрейм, как один элемент вбокса
                        area(0.5, 0.5, 300, 60)
                        xanchor 0.5 yanchor 0.5
                        background debug_frame["blue"] 

                        button:
                            pos(0.5, 0.5)
                            xysize(wnfh_frames_elements["game_menu_selector_button_bg"][1], wnfh_frames_elements["game_menu_selector_button_bg"][2])
                            text button[1]:
                                style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                at wnfh_mm_button_hover_atl()
                                if renpy.get_screen(button[0]) != None:
                                    color wnfh_tint_color[renpy.store.wnfh_tymeofday][1]
                            style "wnfh_buttons"
                            background Frame(
                                Transform(
                                    wnfh_frames_elements["game_menu_selector_button_bg"][0],
                                    matrixcolor = TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["game_menu_selector_button_bg"][4]])
                                    ),
                                left = wnfh_frames_elements["game_menu_selector_button_bg"][3],
                                top = 0
                                )
                            foreground Frame(
                                Transform(
                                    wnfh_frames_elements["game_menu_selector_button_double_line"][0],
                                    matrixcolor = TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["game_menu_selector_button_double_line"][4]])
                                    ),
                                left = wnfh_frames_elements["game_menu_selector_button_double_line"][3],
                                top = 6
                                )
                            hover_background Fixed(
                                Frame(
                                    Transform(
                                        wnfh_frames_elements["game_menu_selector_button_bg"][0],
                                        matrixcolor = TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["game_menu_selector_button_bg"][4]])
                                        ),
                                    left = wnfh_frames_elements["game_menu_selector_button_bg"][3],
                                    top = 0
                                    ),
                                Frame(
                                    Transform(
                                        wnfh_frames_elements["game_menu_selector_button_gradient"][0],
                                        matrixcolor = TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["game_menu_selector_button_gradient"][4]]),
                                        alpha = 0.6
                                        ),
                                    left = wnfh_frames_elements["game_menu_selector_button_gradient"][3],
                                    top = 0
                                    ),
                                Frame(
                                    Transform(
                                        wnfh_frames_elements["game_menu_selector_button_gradient"][0],
                                        alpha = 0.1
                                        ),
                                    left = wnfh_frames_elements["game_menu_selector_button_gradient"][3],
                                    top = 0
                                    )
                                )
                            action [Hide(list[0]) for list in wnfh_game_menu_selector_buttons] + button[2] + [SetDict(wnfh_button_states, index, False)]
                            sensitive renpy.get_screen(button[0]) == None
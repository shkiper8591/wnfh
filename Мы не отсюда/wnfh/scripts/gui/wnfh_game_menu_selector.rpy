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
            
            ['wnfh_logbook'      ,"Дневник"      ,[ToggleScreen('wnfh_logbook')]                      ],
            ['wnfh_schematic'    ,"Схема"        ,[ToggleScreen('wnfh_schematic')]                    ],
            ['save'              ,"Сохранить"    ,[ToggleScreen('save')]                              ],
            ['load'              ,"Загрузить"    ,[ToggleScreen('load')]                              ],
            ['preferences'       ,"Настройки"    ,[ToggleScreen('preferences')]                       ],
            #['quit'              ,"Выход"        ,[ToggleScreen('quit')]                              ],
            ['yesno_prompt'      ,"Выход" ,[MainMenu(), SetDict(wnfh_button_states, 0, False)] ],
        ]

    add wnfh_gui["main_menu"]["vignette"]

    
    on "show" action ToggleScreen('wnfh_logbook')

    frame at govno_ebanoe2:
        area(0.5, 0.5, 1.0, 0.95)
        xanchor 0.5 yanchor 0.5
        background debug_frame["black"]
        vbox: # ================================================ Фон таблички из трёх кусков
            pos (0.5, 0.5)
            xanchor 0.5 yanchor 0.5
            spacing 0
            for element in ["logbook_box_line", "logbook_box_bg", "logbook_box_line"]:
                frame at wnfh_frames_elements[element][6]:
                #frame:
                    if persistent.wnfh_debug_color:
                        background wnfh_frames_elements[element][5]
                    else:
                        background frame_transparent
                    area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                    add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                        matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
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
                                    add Frame(wnfh_frames_elements[element][0], left = wnfh_frames_elements[element][3], top = 0):
                                        matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
        
                        frame: # ================================================ Тонировка при наведении
                            if wnfh_button_states[index]:
                                add Frame(wnfh_frames_elements["game_menu_selector_button_gradient"][0], left=wnfh_frames_elements["game_menu_selector_button_gradient"][3], top=0):
                                    xalign 0.5 yalign 0.5 alpha 0.6
                                    matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["game_menu_selector_button_gradient"][4]])
                                    at wnfh_gradient
                                add Frame(wnfh_frames_elements["game_menu_selector_button_gradient"][0], left=wnfh_frames_elements["game_menu_selector_button_gradient"][3], top=0):
                                    xalign 0.5 yalign 0.5 alpha 0.1
                                    at wnfh_gradient
                            else:
                                null height 20
                            area(0.5, 0.5, wnfh_frames_elements["game_menu_selector_button_bg"][1], wnfh_frames_elements["game_menu_selector_button_bg"][2]) padding(0, 0) xanchor 0.5 yanchor 0.5
                            background debug_frame["purple"]
        
                            textbutton button[1]: # ================================================ Текст кнопок
                                text_style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                style "wnfh_buttons"
                                text_min_width 290
                                hovered ToggleDict(wnfh_button_states, index)
                                unhovered ToggleDict(wnfh_button_states, index)
                                action [Hide(list[0]) for list in wnfh_game_menu_selector_buttons] + button[2]
                                at wnfh_mm_button_hover_atl()
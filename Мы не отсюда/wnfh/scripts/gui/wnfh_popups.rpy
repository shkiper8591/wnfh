init 2:
    screen wnfh_yesno_prompt:
        modal True

        default wnfh_screen_1 = False
        default wnfh_screen_2 = False

        python:
            wnfh_screen_variable = [
                wnfh_screen_1,
                wnfh_screen_2,
            ]
            wnfh_screen_variable_string = list('wnfh_screen_' + str(i) for i in range(1, 3))

            wnfh_yesno_prompt_buttons = [
                ["Да", yes_action],
                ["Нет", no_action]
            ]

        frame at wnfh_dissolve: # ================================== Фрейм затемнящий экран
            area(0.5, 0.5, 1.0, 1.0)
            xanchor 0.5 yanchor 0.5
            background "#000000AA"
        vbox: # ================================================ Главный вбокс              
            pos (0.5, 0.5)
            xanchor 0.5 yanchor 0.5
            spacing 5
            frame: # ================================================ Фрейм таблички    
                area(0.5, 0.5, 1100, 210)
                xanchor 0.5 yanchor 0.5
                if persistent.wnfh_debug_color:
                    background frame_black
                else:
                    background frame_transparent
                vbox: # ================================================ Фон таблички из трёх кусков
                    pos (0.5, 0.5)
                    xanchor 0.5 yanchor 0.5
                    spacing 0
                    for i in ["yesno_prompt_box_line", "yesno_prompt_box_bg", "yesno_prompt_box_line"]:
                        frame at wnfh_frames_elements[i][6]:
                            if persistent.wnfh_debug_color:
                                background wnfh_frames_elements[i][5]
                            else:
                                background frame_transparent
                            area(0.5, 0.0, wnfh_frames_elements[i][1], wnfh_frames_elements[i][2]) padding(0, 0) xanchor 0.5
                            add Frame(wnfh_frames_elements[i][0], left=wnfh_frames_elements[i][3], top=0):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][wnfh_frames_elements[i][4]])
                frame at wjuh_bg: # ================================================ Текст таблички
                    area(0.5, 0.5, 1000, 190)
                    xanchor 0.5 yanchor 0.5
                    if persistent.wnfh_debug_color:
                        background frame_purpl
                    else:
                        background frame_transparent
                    text "Вы действительно хотите выйти в главное меню?\nНесохранённые данные будут потеряны.":
                        xalign 0.5 yanchor 0.5 ypos 0.5
                        line_leading 5 line_spacing 3
                        min_width 390
                        text_align 0.5
                        style "wnfh_choice_" + persistent.timeofday
            frame: # ================================================ Фрейм кнопок
                area(0.5, 0.5, 1100, 100)
                xanchor 0.5 yanchor 0.5
                if persistent.wnfh_debug_color:
                    background frame_black
                else:
                    background frame_transparent
                hbox: # ================================================ Хбокс кнопок
                    pos (0.5, 0.5)
                    xanchor 0.5 yanchor 0.5
                    spacing 400
                    for index, button in enumerate(wnfh_yesno_prompt_buttons[0:2]):
                        frame: # ================================================ Фрейм, как один элемент хбокса
                            area(0.5, 0.5, 300, 70)
                            xanchor 0.5 yanchor 0.5
                            if persistent.wnfh_debug_color:
                                background frame_blue
                            else:
                                background frame_transparent 
                            vbox: # ================================================ Вбокс кнопок
                                pos (0.5, 0.5)
                                xanchor 0.5 yanchor 0.5
                                spacing 0
                                for element in ["yesno_prompt_button_line", "yesno_prompt_button_bg", "yesno_prompt_button_line"]:
                                    frame at wnfh_frames_elements[element][6]:
                                        if persistent.wnfh_debug_color:
                                            background wnfh_frames_elements[element][5]
                                        else:
                                            background frame_transparent
                                        area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][wnfh_frames_elements[element][4]])
                            frame at wjuh_bg: # ================================================ Тонировка при наведении
                                if wnfh_screen_variable[index]:
                                    add Frame(wnfh_frames_elements["yesno_prompt_button_gradient"][0], left=wnfh_frames_elements["yesno_prompt_button_gradient"][3], top=0):
                                        xalign 0.5 yalign 0.5 alpha 0.6
                                        matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][wnfh_frames_elements["yesno_prompt_button_gradient"][4]])
                                    add Frame(wnfh_frames_elements["yesno_prompt_button_gradient"][0], left=wnfh_frames_elements["yesno_prompt_button_gradient"][3], top=0):
                                        xalign 0.5 yalign 0.5 alpha 0.1
                                else:
                                    null height 20
                                area(0.5, 0.5, wnfh_frames_elements["yesno_prompt_button_bg"][1], wnfh_frames_elements["yesno_prompt_button_bg"][2]) padding(0, 0) xanchor 0.5 yanchor 0.5
                                if persistent.wnfh_debug_color:
                                    background frame_purpl
                                else:
                                    background frame_transparent
                                textbutton button[0]: # ================================================ Текст кнопок
                                    xalign 0.5 yanchor 0.5 ypos 0.5
                                    text_line_leading 5 text_line_spacing 3
                                    text_min_width 390
                                    text_text_align 0.5
                                    text_style "wnfh_choice_" + persistent.timeofday
                                    background None
                                    hover_sound wnfh_gui["sound"]["plimp"]
                                    hovered ToggleScreenVariable(wnfh_screen_variable_string[index])
                                    unhovered ToggleScreenVariable(wnfh_screen_variable_string[index])
                                    action button[1]
                    
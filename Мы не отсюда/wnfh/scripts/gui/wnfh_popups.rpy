screen wnfh_yesno_prompt:
    $ debug_frame = {
        "black":  frame_black                if persistent.wnfh_debug_color else frame_transparent,
        "red":    frame_red                  if persistent.wnfh_debug_color else frame_transparent,
        "green":  frame_green                if persistent.wnfh_debug_color else frame_transparent,
        "blue":   frame_blue                 if persistent.wnfh_debug_color else frame_transparent,
        "purple": frame_purpl                if persistent.wnfh_debug_color else frame_transparent,
    }
    modal True

    default wnfh_button_states = [False for i in range(2)]

    python:

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
            background debug_frame["black"]
            vbox: # ================================================ Фон таблички из трёх кусков
                pos (0.5, 0.5)
                xanchor 0.5 yanchor 0.5
                spacing 0
                for element in ["yesno_prompt_box_line", "yesno_prompt_box_bg", "yesno_prompt_box_line"]:
                    frame at wnfh_frames_elements[element][6]:
                        if persistent.wnfh_debug_color:
                            background wnfh_frames_elements[element][5]
                        else:
                            background frame_transparent 
                        area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])

            frame at wjuh_bg: # ================================================ Текст таблички
                area(0.5, 0.5, 1000, 190)
                xanchor 0.5 yanchor 0.5
                background debug_frame["purple"]
                text _(message):
                    style "wnfh_text_" + renpy.store.wnfh_tymeofday

        frame: # ================================================ Фрейм кнопок
            area(0.5, 0.5, 1100, 100)
            xanchor 0.5 yanchor 0.5
            background debug_frame["black"]
            hbox: # ================================================ Хбокс кнопок
                pos (0.5, 0.5)
                xanchor 0.5 yanchor 0.5
                spacing 400
                for index, button in enumerate(wnfh_yesno_prompt_buttons[0:2]):
                    frame: # ================================================ Фрейм, как один элемент хбокса
                        area(0.5, 0.5, 300, 70)
                        xanchor 0.5 yanchor 0.5
                        background debug_frame["blue"]
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
                                        matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])

                        frame at wjuh_bg: 
                            if wnfh_button_states[index]: # ================================================ Тонировка при наведении
                                add Frame(wnfh_frames_elements["yesno_prompt_button_gradient"][0], left=wnfh_frames_elements["yesno_prompt_button_gradient"][3], top=0):
                                    xalign 0.5 yalign 0.5 alpha 0.6
                                    matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["yesno_prompt_button_gradient"][4]])
                                add Frame(wnfh_frames_elements["yesno_prompt_button_gradient"][0], left=wnfh_frames_elements["yesno_prompt_button_gradient"][3], top=0):
                                    xalign 0.5 yalign 0.5 alpha 0.1
                            else:
                                null height 20
                            area(0.5, 0.5, wnfh_frames_elements["yesno_prompt_button_bg"][1], wnfh_frames_elements["yesno_prompt_button_bg"][2]) padding(0, 0) xanchor 0.5 yanchor 0.5
                            background debug_frame["purple"]

                            textbutton button[0]: # ================================================ Текст кнопок
                                text_style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                style "wnfh_buttons" 
                                hovered ToggleDict(wnfh_button_states, index)
                                unhovered ToggleDict(wnfh_button_states, index)
                                action button[1]
                                at wnfh_mm_button_hover_atl()
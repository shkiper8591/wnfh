screen wnfh_choice(*args):
    modal True
    $ debug_frame = {
        "black":  frame_black  if persistent.wnfh_debug_color else frame_transparent,
        "red":    frame_red    if persistent.wnfh_debug_color else frame_transparent,
        "green":  frame_green  if persistent.wnfh_debug_color else frame_transparent,
        "blue":   frame_blue   if persistent.wnfh_debug_color else frame_transparent,
        "purple": frame_purpl  if persistent.wnfh_debug_color else frame_transparent
    }
    
    default wnfh_button_states = [False for i in range(len(args))]

    key 'K_PAGEDOWN':
        action NullAction()
    key 'mousedown_5':
        action NullAction()
    python:
        def  wnfh_add_to_bd(data):
            data_set = wnfh_find_Operand(data,"prod",str(data[1][0]))
            wnfh_Data.write(str(data[1][0]),{"type":"choice","Название выбора":str(data[1][1]),"Выбранно":data[2]+1,"Текст выбора":data[0][1],"Влияние на персонажей":data_set,"rollback":False})
    frame:
        background debug_frame["black"]
        area(0.5, 0.5, 0.7, 0.8)
        xanchor 0.5 yanchor 0.5
        vbox:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            spacing 5
            
            for index in range(len(args) - 1):
                if index == "test":
                    pass
                else:
                    frame:
                        background debug_frame["black"]
                        area(0.5, 0.5, 1.0, 80)
                        xanchor 0.5 yanchor 0.5

                        vbox: # ================================================ Вбокс кнопок
                            pos (0.5, 0.5)
                            xanchor 0.5 yanchor 0.5
                            spacing 0
                            for element in ["choice_button_line", "choice_button_bg", "choice_button_line"]:
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
                                add Frame(wnfh_frames_elements["choice_button_gradient"][0], left=wnfh_frames_elements["choice_button_gradient"][3], top=0):
                                    xalign 0.5 yalign 0.5 alpha 0.9
                                    matrixcolor TintMatrix(wnfh_characters[args[index][0]][1])
                                    at wnfh_gradient
                            else:
                                null height 20
                            area(0.5, 0.5, wnfh_frames_elements["choice_button_bg"][1], wnfh_frames_elements["choice_button_bg"][2]) padding(0, 0) xanchor 0.5 yanchor 0.5
                            background debug_frame["purple"]

                        if wnfh_button_states[index]:
                            textbutton args[index][2]:
                                text_style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                style "wnfh_buttons"
                                text_min_width 1100
                                text_line_leading 16 text_line_spacing 11
                                hovered SetDict(wnfh_button_states, index, True)
                                unhovered SetDict(wnfh_button_states, index, False)
                                action (Hide("wnfh_choice_0", dissolve), Function(wnfh_add_to_bd, [args[index], args[len(args) -1], index]), Jump(args[index][3]))
                        else:
                            textbutton args[index][1]:
                                text_style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                style "wnfh_buttons"
                                text_min_width 1100
                                text_line_leading 16 text_line_spacing 11
                                hovered SetDict(wnfh_button_states, index, True)
                                unhovered SetDict(wnfh_button_states, index, False)
                                action (Hide("wnfh_choice_0", dissolve), Function(wnfh_add_to_bd, [args[index], args[len(args) -1], index]), Jump(args[index][3]))

    add wnfh_gui["main_menu"]["vignette"]
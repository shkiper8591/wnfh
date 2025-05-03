init 2:
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
            wnfh_Data.display("Окно выборов ")
            if args[-1] == "test":
                Test_wr = True
            else:
                Test_wr = False
            def  wnfh_add_to_bd(data):
                data_set = wnfh_find_Operand(data,"prod",str(data[1][0]))
                wnfh_Data.write(str(data[1][0]),{"type":"choice","Название выбора":str(data[1][1]),"Выбранно":data[2]+1,"Текст выбора":data[0][1],"Влияние на персонажей":data_set,"rollback":False})
            def  wnfh_add_to_bd_test(data):
                data_set = wnfh_find_Operand(data,"test",str(data[1][0]))
                wnfh_Data_test.write(str(data[1][0]),{"type":"choice","Название выбора":str(data[1][1]),"Выбранно":data[2]+1,"Текст выбора":data[0][1],"Влияние на персонажей": data_set,"rollback":False})
            
        frame:
            background debug_frame["black"]
            area(0.5, 0.5, 0.7, 0.8)
            xanchor 0.5 yanchor 0.5
            #grid 1 len(args)-1:
            grid 1 len(args) - int(Test_wr):
                anchor (0.5, 0.5) pos (0.5, 0.5)
                spacing -6
                
                for i in range(len(args) - 1 - int(Test_wr)):
                    if i == "test":
                        pass
                    else:
                        frame:
                            background debug_frame["black"]
                            area(0.5, 0.5, 1.0, 80)
                            xanchor 0.5 yanchor 0.5

                            add (wnfh_gui["choice"]["line"]):
                                matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][1])
                                xalign 0.5 yanchor 1.0
                            add (wnfh_gui["choice"]["bg"]):
                                matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][2])
                                xalign 0.5
                            if wnfh_button_states[i]:
                                add (wnfh_gui["choice"]["gradient"]):
                                    xalign 0.5
                                    matrixcolor TintMatrix(wnfh_characters[args[i][0]][1])
                            else:
                                null height 20

                            if wnfh_button_states[i]:
                                textbutton args[i][2]:
                                    text_style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                    style "wnfh_buttons"
                                    text_min_width 1100
                                    hovered ToggleDict(wnfh_button_states, i)
                                    unhovered ToggleDict(wnfh_button_states, i)
                                    if not Test_wr:
                                        action (Hide("wnfh_choice_0", dissolve), Function(wnfh_add_to_bd, [args[i], args[len(args) -1- int(Test_wr)], i]), Jump(args[i][3]))
                                    else:
                                        action (Hide("wnfh_choice_0", dissolve), Function(wnfh_add_to_bd_test, [args[i], args[len(args) -1- int(Test_wr)], i]), Jump(args[i][3]))
                            else:
                                textbutton args[i][1]:
                                    text_style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                    style "wnfh_buttons"
                                    text_min_width 1100
                                    hovered ToggleDict(wnfh_button_states, i)
                                    unhovered ToggleDict(wnfh_button_states, i)
                                    if not Test_wr:
                                        action (Hide("wnfh_choice_0", dissolve), Function(wnfh_add_to_bd, [args[i], args[len(args) -1- int(Test_wr)], i]), Jump(args[i][3]))
                                    else:
                                        action (Hide("wnfh_choice_0", dissolve), Function(wnfh_add_to_bd_test, [args[i], args[len(args) -1- int(Test_wr)], i]), Jump(args[i][3]))
                add (wnfh_gui["choice"]["line"]):
                    matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][1])
                    xalign 0.5 yanchor 0.0

        add wnfh_gui["choice"]["vignette"]
init 2:
    screen wnfh_choice(*args):
        modal True tag menu
        default wnfh_screen_1 = False
        default wnfh_screen_2 = False
        default wnfh_screen_3 = False
        default wnfh_screen_4 = False
        default wnfh_screen_5 = False
        default wnfh_screen_6 = False
        default wnfh_screen_7 = False
        default wnfh_screen_8 = False
        default wnfh_screen_9 = False
        default wnfh_screen_10 = False
        default wnfh_screen_11 = False
        default wnfh_screen_12 = False
        default wnfh_screen_13 = False
        default wnfh_screen_14 = False
        default wnfh_screen_15 = False
        default wnfh_screen_16 = False
        default wnfh_screen_17 = False
        default wnfh_screen_18 = False
        default wnfh_screen_19 = False

        python:
        #   for i in range(1,20):
        #       locals()["wnfh_screen_"+str(i)]=False

            def  wnfh_add_to_bd(data):
                data_set = wnfh_find_Operand(data,"prod",str(data[1][0]))
                wnfh_Data.write(str(data[1][0]),{"type":"choice","Название выбора":str(data[1][1]),"Выбранно":data[2]+1,"Текст выбора":data[0][1],"Влияние на персонажей":data_set})
            def  wnfh_add_to_bd_test(data):
                data_set = wnfh_find_Operand(data,"test",str(data[1][0]))
                wnfh_Data_test.write(str(data[1][0]),{"type":"choice","Название выбора":str(data[1][1]),"Выбранно":data[2]+1,"Текст выбора":data[0][1],"Влияние на персонажей": data_set})
            
            #wnfh_screen_variable = list(locals()['wnfh_screen_'+str(i)] for i in range(1,20))
            wnfh_screen_variable =[
                wnfh_screen_1,
                wnfh_screen_2,
                wnfh_screen_3,
                wnfh_screen_4,
                wnfh_screen_5,
                wnfh_screen_6,
                wnfh_screen_7,
                wnfh_screen_8,
                wnfh_screen_9,
                wnfh_screen_10,
                wnfh_screen_11,
                wnfh_screen_12,
                wnfh_screen_13,
                wnfh_screen_14,
                wnfh_screen_15,
                wnfh_screen_16,
                wnfh_screen_17,
                wnfh_screen_18,
                wnfh_screen_19
            ]
            wnfh_screen_variable_string=list('wnfh_screen_'+str(i) for i in range(1,20))

        #add (wnfh_gui["choice"]["line_" + str(len(args)-1)]) matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
        #for i in range(len(args)-1):
        #    if wnfh_screen_variable[i]:
        #        add (wnfh_gui["choice"][str(len(args)-1) + "_" + wnfh_screen_cordinates[str(len(args)-1)][i][3] + "_" + args[i][0]]) xzoom wnfh_screen_cordinates[str(len(args)-1)][i][1][0] yzoom wnfh_screen_cordinates[str(len(args)-1)][i][1][1]
        #        text args[i][2]:
        #            style "wnfh_choice_text_" + persistent.timeofday
        #            align (wnfh_screen_cordinates[str(len(args)-1)][i][0][0], wnfh_screen_cordinates[str(len(args)-1)][i][0][1])
        #    else:
        #        null height 20
        #
       #     textbutton args[i][1]:
       #         text_style "wnfh_choice_" + persistent.timeofday
       #         background None align (wnfh_screen_cordinates[str(len(args)-1)][i][2][0], wnfh_screen_cordinates[str(len(args)-1)][i][2][1])
       #         hover_sound wnfh_gui["sound"]["plimp"] 
       #         hovered ToggleScreenVariable(wnfh_screen_variable_string[i])
       #         unhovered ToggleScreenVariable(wnfh_screen_variable_string[i])
       #         action (Hide("wnfh_choice_0", dissolve),Function(add_to_bd,[args[i],args[len(args)-1],i]),Jump(args[i][3]))
        
        if args[-1] == "test":
            $ Test_wr = True
        else:
            $ Test_wr = False
        frame:
            background #0000
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
                            background #0000
                            area(0.5, 0.5, 1.0, 80)
                            xanchor 0.5 yanchor 0.5

                            add (wnfh_gui["choice"]["line"]):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                                xalign 0.5 yanchor 1.0
                            add (wnfh_gui["choice"]["bg"]):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][2])
                                xalign 0.5
                            if wnfh_screen_variable[i]:
                                add (wnfh_gui["choice"]["gradient"]):
                                    xalign 0.5
                                    matrixcolor TintMatrix(wnfh_characters[args[i][0]][1])
                                #text args[i][2]:
                                #    style "wnfh_choice_text_" + persistent.timeofday
                                #    align (wnfh_screen_cordinates[str(len(args)-1)][i][0][0], wnfh_screen_cordinates[str(len(args)-1)][i][0][1])
                            else:
                                null height 20
                            #add (wnfh_gui["choice"]["line"]):
                            #    matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][2])
                            #    xalign 0.5 ypos 1.0 yanchor 0.0
                            textbutton args[i][1]:
                                text_line_leading 16 text_line_spacing 11
                                text_min_width 1100
                                text_text_align 0.5
                                xalign 0.5 yanchor 0.5 ypos 0.5
                                text_style "wnfh_choice_" + persistent.timeofday
                                background None #align (wnfh_screen_cordinates[str(len(args)-1)][i][2][0], wnfh_screen_cordinates[str(len(args)-1)][i][2][1])
                                hover_sound wnfh_gui["sound"]["plimp"]
                                hovered ToggleScreenVariable(wnfh_screen_variable_string[i])
                                unhovered ToggleScreenVariable(wnfh_screen_variable_string[i])
                                if not Test_wr:
                                    action (Hide("wnfh_choice_0", dissolve),Function( wnfh_add_to_bd,[args[i],args[len(args)-1- int(Test_wr)],i]),Jump(args[i][3]))
                                else:
                                    action (Hide("wnfh_choice_0", dissolve),Function( wnfh_add_to_bd_test,[args[i],args[len(args)-1- int(Test_wr)],i]),Jump(args[i][3]))
                add (wnfh_gui["choice"]["line"]):
                    matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                    xalign 0.5 yanchor 0.0

        add wnfh_gui["choice"]["vignette"]

#


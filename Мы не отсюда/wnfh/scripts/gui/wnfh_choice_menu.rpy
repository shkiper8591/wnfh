init 2:
    screen wnfh_choice(*args):
        modal True tag menu
        default wnfh_screen_1 = False
        default wnfh_screen_2 = False
        default wnfh_screen_3 = False
        default wnfh_screen_4 = False
        
        python:
            wnfh_choice_tint_color = {
                #timeset    #цветокор кнопок #палка
                "day":      ["#FFF"         ,"#E2C778"],
                "sunset":   ["#FFF"         ,"#DCD168"],
                "night":    ["#A8A8A8"      ,"#3CCFA2"],
                "prologue": ["#A8A8A8"      ,"#98D8DA"],
            }
            wnfh_screen_variable = [
                wnfh_screen_1,
                wnfh_screen_2,
                wnfh_screen_3,
                wnfh_screen_4
            ]
            wnfh_screen_variable_string=[
               "wnfh_screen_1",
               "wnfh_screen_2",
               "wnfh_screen_3",
               "wnfh_screen_4",
            ]
            wnfh_screen_cordinates={
                "1":[[0.1, 0.7]],
                "2":[[(0.1, 0.7), (1, 1), (0.25, 0.5),"flang"], [(0.9, 0.7), (-1,-1), (0.75,0.5),"flang"]],
                "3":[[(0.05, 0.1), (1, 1), (0.2, 0.45),"flang"], [(0.95, 0.1), (-1, 1), (0.8,0.45),"flang"], [(0.5, 0.85), (1, 1), (0.5,0.65),"mid"]],
                "4":[[0.1, 0.7],[0.9,0.7],[0.1, 0.7],[0.9,0.7]],
                "5":[],
            }  

        add (wnfh_gui["choice"]["line_" + str(len(args))]) matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
        for i in range(len(args)):
            if wnfh_screen_variable[i]:
                add (wnfh_gui["choice"][str(len(args)) + "_" + wnfh_screen_cordinates[str(len(args))][i][3] + "_" + args[i][0]]) xzoom wnfh_screen_cordinates[str(len(args))][i][1][0] yzoom wnfh_screen_cordinates[str(len(args))][i][1][1]
                text args[i][2]:
                    style "wnfh_choice_text_" + persistent.timeofday
                    align (wnfh_screen_cordinates[str(len(args))][i][0][0], wnfh_screen_cordinates[str(len(args))][i][0][1])
            else:
                null height 20

            textbutton args[i][1]:
                text_style "wnfh_choice_" + persistent.timeofday
                background None align (wnfh_screen_cordinates[str(len(args))][i][2][0], wnfh_screen_cordinates[str(len(args))][i][2][1])
                hover_sound wnfh_gui["sound"]["plimp"] 
                hovered ToggleScreenVariable(wnfh_screen_variable_string[i])
                unhovered ToggleScreenVariable(wnfh_screen_variable_string[i])
                action (Hide("wnfh_choice_0", dissolve), Jump(args[i][3]))

            for j in range(4):
                pass 

        #add wnfh_gui["choice"]["vignette"]

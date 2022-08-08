init 2:

    #screen blwnfh_timer(lose_label):
    #    timer 1 repeat True action If(blwnfh_time > 0, SetVariable("blwnfh_time", blwnfh_time-1.0), (SetVariable("blwnfh_silence_points", blwnfh_silence_points+1), (Hide("blwnfh_timer", dissolve), Jump(lose_label))))
    #    bar value blwnfh_time range blwnfh_time_range left_bar blwnfh_u_path + "blwnfh_baro_left.png" right_bar blwnfh_u_path + "blwnfh_baro_right.png" thumb blwnfh_a_path + "blwnfh_fireflyes.png" thumb_offset 19 align (.5, .9) xmaximum 668 ymaximum 40 at blwnfh_smooth_map

    screen blwnfh_double_choice(button_1, button_2, text_1, text_2, variant_1, variant_2, label_1, label_2, timeset):
        modal True tag menu
        python:
            if timeset == "day":
                button_tint_color = "#fff"
                
            elif timeset == "sunset":
                button_tint_color = "#fff"
                
            elif timeset == "night":
                button_tint_color = "#A8A8A8"
                
            elif timeset == "prologue":
                button_tint_color = "#A8A8A8"
            
            if timeset == "day":
                line_tint_color = "#E2C778"
                
            elif timeset == "sunset":
                line_tint_color = "#DCD168"
                
            elif timeset == "night":
                line_tint_color = "#3CCFA2"
                
            elif timeset == "prologue":
                line_tint_color = "#98D8DA"
        
        default blwnfh_screen_1 = False
        default blwnfh_screen_2 = False
        
        add blwnfh_gui["choice"]["vignette"]
    
        if blwnfh_screen_1:
            add (blwnfh_gui["choice"]["2_flang_" + button_1])
            text text_1 style "blwnfh_choice_text_" + timeset align (.1, .7)
    
        else:
            null height 20
    
        if blwnfh_screen_2:
            add (blwnfh_gui["choice"]["2_flang_" + button_2]) xzoom -1 yzoom -1
            text text_2 style "blwnfh_choice_text_" + timeset align (.9, .7)
    
        else:
            null height 20
    
        textbutton variant_1:
            text_style "blwnfh_choice_" + timeset
            background None align (.25, .5)
            hover_sound blwnfh_gui["sound"]["plimp"]
            hovered ToggleScreenVariable("blwnfh_screen_1")
            unhovered ToggleScreenVariable("blwnfh_screen_1")
            action (Hide("blwnfh_choice_0", dissolve), Jump(label_1))
            
        textbutton variant_2:
            text_style "blwnfh_choice_" + timeset
            background None align (.75, .5)
            hover_sound blwnfh_gui["sound"]["plimp"]
            hovered ToggleScreenVariable("blwnfh_screen_2")
            unhovered ToggleScreenVariable("blwnfh_screen_2")
            action (Hide("blwnfh_choice_0", dissolve), Jump(label_2))
        
        add (blwnfh_gui["choice"]["line_3"]) matrixcolor TintMatrix(line_tint_color)
        

        #use blwnfh_timer(s1)
        
    screen blwnfh_triple_choice(button_1, button_2, button_3, text_1, text_2, text_3, variant_1, variant_2, variant_3, label_1, label_2, label_3, timeset):
        modal True tag menu
        python:
            if timeset == "day":
                button_tint_color = "#fff"
                
            elif timeset == "sunset":
                button_tint_color = "#fff"
                
            elif timeset == "night":
                button_tint_color = "#A8A8A8"
                
            elif timeset == "prologue":
                button_tint_color = "#A8A8A8"
            
            if timeset == "day":
                line_tint_color = "#E2C778"
                
            elif timeset == "sunset":
                line_tint_color = "#DCD168"
                
            elif timeset == "night":
                line_tint_color = "#3CCFA2"
                
            elif timeset == "prologue":
                line_tint_color = "#98D8DA"
        
        #E2C778 день
        #DCD168 вечер
        #3CCFA2 ночь
        #98D8DA пролог
    
        default blwnfh_screen_1 = False
        default blwnfh_screen_2 = False
        default blwnfh_screen_3 = False
    
        add blwnfh_gui["choice"]["vignette"]
        
        if blwnfh_screen_1:
            add (blwnfh_gui["choice"]["3_flang_" + button_1]) matrixcolor TintMatrix(button_tint_color)
            text text_1 style "blwnfh_choice_text_" + timeset align (.05, .1)
    
        else:
            null height 20
    
        if blwnfh_screen_2:
            add (blwnfh_gui["choice"]["3_flang_" + button_2]) xzoom -1 matrixcolor TintMatrix(button_tint_color)
            text text_2 style "blwnfh_choice_text_" + timeset align (.95, .1)
    
        else:
            null height 20
            
        if blwnfh_screen_3:
            add (blwnfh_gui["choice"]["3_mid_" + button_3]) matrixcolor TintMatrix(button_tint_color)
            text text_3 style "blwnfh_choice_text_" + timeset align (.5, .85)
    
        else:
            null height 20
    
        textbutton variant_1:
            text_style "blwnfh_choice_" + timeset #Стиль текста
            background None align (.2, .45) #Положение заголовка
            hover_sound blwnfh_gui["sound"]["plimp"] #Звук наведения
            hovered ToggleScreenVariable("blwnfh_screen_1")
            unhovered ToggleScreenVariable("blwnfh_screen_1")
            action (Hide("blwnfh_choice_0", dissolve), Jump(label_1)) #Действие
            
        textbutton variant_2:
            text_style "blwnfh_choice_" + timeset
            background None align (.8, .45)
            hover_sound blwnfh_gui["sound"]["plimp"]
            hovered ToggleScreenVariable("blwnfh_screen_2")
            unhovered ToggleScreenVariable("blwnfh_screen_2")
            action (Hide("blwnfh_choice_0", dissolve), Jump(label_2))
            
        textbutton variant_3:
            text_style "blwnfh_choice_" + timeset
            background None align (.5, .65)
            hover_sound blwnfh_gui["sound"]["plimp"]
            hovered ToggleScreenVariable("blwnfh_screen_3")
            unhovered ToggleScreenVariable("blwnfh_screen_3")
            action (Hide("blwnfh_choice_0", dissolve), Jump(label_3))

        add (blwnfh_gui["choice"]["line_3"]) matrixcolor TintMatrix(line_tint_color)
        #use blwnfh_timer(s1)
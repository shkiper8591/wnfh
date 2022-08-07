init 2:

    #screen blwnfh_timer(lose_label):
    #    timer 1 repeat True action If(blwnfh_time > 0, SetVariable("blwnfh_time", blwnfh_time-1.0), (SetVariable("blwnfh_silence_points", blwnfh_silence_points+1), (Hide("blwnfh_timer", dissolve), Jump(lose_label))))
    #    bar value blwnfh_time range blwnfh_time_range left_bar blwnfh_u_path + "blwnfh_baro_left.png" right_bar blwnfh_u_path + "blwnfh_baro_right.png" thumb blwnfh_a_path + "blwnfh_fireflyes.png" thumb_offset 19 align (.5, .9) xmaximum 668 ymaximum 40 at blwnfh_smooth_map

    screen blwnfh_choice(button1, button2, text1, text2, variant1, variant2, label1, label2):
        modal True tag menu
    
        default blwnfh_screen1 = False
        default blwnfh_screen2 = False
    
        #add blwnfh_a_path + "blwnfh_vignette.png"
        add blwnfh_CHOICE + "line_2.png"
    
        if blwnfh_screen1:
            add (blwnfh_gui["choice"][button1])
            text text1 style "blwnfh_menu" align (.1, .7)
    
        else:
            null height 20
    
        if blwnfh_screen2:
            add (blwnfh_gui["choice"][button2]) xzoom -1 yzoom -1
            text text2 style "blwnfh_menu" align (.9, .7)
    
        else:
            null height 20
    
        textbutton variant1 text_style "blwnfh_menu" background None align (.25, .5) hover_sound blwnfh_gui["sound"]["plimp"] hovered ToggleScreenVariable("blwnfh_screen1") unhovered ToggleScreenVariable("blwnfh_screen1") action (Hide("blwnfh_choice_0", dissolve), Jump(label1))
        textbutton variant2 text_style "blwnfh_menu" background None align (.75, .5) hover_sound blwnfh_gui["sound"]["plimp"] hovered ToggleScreenVariable("blwnfh_screen2") unhovered ToggleScreenVariable("blwnfh_screen2") action (Hide("blwnfh_choice_0", dissolve), Jump(label2))
    
        #use blwnfh_timer(s1)
init 2:
    screen wnfh_say:
    
        window background None id "window":
    
            $ timeofday = persistent.timeofday
    
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/backward_%s.png") xpos 38 ypos 949 action ShowMenu("text_history")

            if persistent.font_size == "small":
                frame: # ======================== Главный блок
                    area(0.5, 1.0, 1555, 150)
                    xanchor 0.5 yanchor 1.0
                    if persistent.wnfh_debug_color:
                        background frame_black
                    else:
                        background frame_transparent
                    grid 1 3:
                        anchor (0.5, 0.5) pos (0.5, 0.5)
                        add (wnfh_gui["tint_elements"]["db_line_upper"]):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                            xalign 0.5 yanchor 1.0 ypos 1.235
                        add (wnfh_gui["tint_elements"]["db_bg"]):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][2])
                            xalign 0.5
                        add (wnfh_gui["tint_elements"]["db_line_lower"]):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                            xalign 0.5

                    frame: # ======================== Текст
                        area(0.5, 1.0, 1543, 105)
                        xanchor 0.5 yanchor 1.0
                        if persistent.wnfh_debug_color:
                            background frame_red
                        else:
                            background frame_transparent
                        text what id "what":
                            anchor (0.0, 0.0) pos (10, 0.0)
                            xmaximum 1540
                            size 28
                            line_spacing 2

                    frame: # ======================== Имя
                        area(0.0, 0.0, 260, 30)
                        if persistent.wnfh_debug_color:
                            background frame_green
                        else:
                            background frame_transparent
                        if who:
                            text who id "who":
                                anchor (0.0, 0.0) pos (10, 0.0)
                                size 28
                                line_spacing 2

                    frame: # ======================== Кнопочки
                        area(1.0, 0.0, 260, 30)
                        xanchor 1.0 yanchor 0.0
                        if persistent.wnfh_debug_color:
                            background frame_green
                        else:
                            background frame_transparent
                        grid 4 1:
                            anchor (0.5, 0.5) pos (0.5, 0.5)
                            spacing 20
                            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/hide_%s.png"):
                                action HideInterface()
                            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/save_%s.png"):
                                action ShowMenu('save')
                            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/menu_%s.png"):
                                action ShowMenu('game_menu_selector')
                            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/load_%s.png"):
                                action ShowMenu('load')

            elif persistent.font_size == "large":
                frame: # ======================== Главный блок
                    area(0.5, 1.0, 1555, 200)
                    xanchor 0.5 yanchor 1.0
                    if persistent.wnfh_debug_color:
                        background frame_black
                    else:
                        background frame_transparent
                    grid 1 3:
                        anchor (0.5, 0.5) pos (0.5, 0.5)

                        add (wnfh_gui["tint_elements"]["db_line_upper_large"]):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                            xalign 0.5 yanchor 1.0 ypos 1.178
                        add (wnfh_gui["tint_elements"]["db_bg_large"]):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][2])
                            xalign 0.5
                            
                        add (wnfh_gui["tint_elements"]["db_line_lower"]):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                            xalign 0.5

                    frame: # ======================== Текст
                        area(0.5, 1.0, 1543, 155)
                        xanchor 0.5 yanchor 1.0
                        if persistent.wnfh_debug_color:
                            background frame_red
                        else:
                            background frame_transparent
                        text what id "what":
                            anchor (0.0, 0.0) pos (10, 0.0)
                            xmaximum 1540
                            size 35
                            line_spacing 1
                        
    
                    frame: # ======================== Имя
                        area(0.0, 0.0, 260, 30)
                        if persistent.wnfh_debug_color:
                            background frame_green
                        else:
                            background frame_transparent
                        if who:
                            text who id "who":
                                anchor (0.0, 0.0) pos (10, 0.0)
                                size 35
                                line_spacing 1
                    frame: # ======================== Кнопочки
                        area(1.0, 0.0, 260, 30)
                        xanchor 1.0 yanchor 0.0
                        if persistent.wnfh_debug_color:
                            background frame_green
                        else:
                            background frame_transparent
                        grid 4 1:
                            anchor (0.5, 0.5) pos (0.5, 0.5)
                            spacing 20
                            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/hide_%s.png"):
                                action HideInterface()
                            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/save_%s.png"):
                                action ShowMenu('save')
                            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/menu_%s.png"):
                                action ShowMenu('game_menu_selector')
                            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/load_%s.png"):
                                action ShowMenu('load')   

                            
                        

                        
                        
    
                
    
            if not config.skipping:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/forward_%s.png") xpos 1768 ypos 949 action Skip()
            else:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/fast_forward_%s.png") xpos 1768 ypos 949 action Skip()
    
                
                
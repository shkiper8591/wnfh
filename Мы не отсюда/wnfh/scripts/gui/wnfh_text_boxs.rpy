init 2:
    screen wnfh_say:
        python:
            wnfh_say_buttons = {
                "backward": [im.Flip(im.Composite( # idle
                                (73, 83),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_bg_1"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                ), horizontal=True),
                            im.Flip(im.Composite( # hover
                                (73, 83),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_bg_1"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_hover"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 0, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                ), horizontal=True)
                            ],
                "forward": [im.Composite( # idle
                                (73, 83),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_bg_1"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                ),
                            im.Composite( # hover
                                (73, 83),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_bg_1"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_hover"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 0, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                )
                            ],
                "fast_forward": [im.Composite( # idle
                                (95, 83),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_bg_2"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                (20, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                ),
                            im.Composite( # hover
                                (95, 83),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_bg_2"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_hover"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 0, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                (20, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                )
                            ]

            }
        #frame: # ======================== Главный фрейм
        #    if persistent.font_size == "small":
        #        area(0.5, 0.5, 1500, 150)
        #    elif persistent.font_size == "large":
        #        area(0.5, 0.5, 1500, 200)
#
        #    xanchor 0.5 yanchor 0.5
        #    if persistent.wnfh_debug_color:
        #        background frame_black
        #    else:
        #        background frame_transparent
        vbox:
            xanchor 0.5 yanchor 1.0
            xpos 0.5 ypos 0.5
            spacing 0
            hbox:
                xanchor 1.0 yanchor 0.5
                xpos 1.0 ypos 0.5
                frame: # ======================== Кнопки
                    if persistent.font_size == "small":
                        at wnfh_db_blue_small
                    elif persistent.font_size == "large":
                        at wnfh_db_blue_large
                    area(0.5, 0.5, 300, 50)
                    xanchor 0.5 yanchor 0.5
                    
                    if persistent.wnfh_debug_color:
                        background frame_blue
                    else:
                        background frame_transparent
                frame: # ======================== Кнопки
                    if persistent.font_size == "small":
                        at wnfh_db_green_small
                    elif persistent.font_size == "large":
                        at wnfh_db_green_large
                    area(0.5, 1.0, 900, 4)
                    xanchor 0.5 yanchor 1.0
                    
                    if persistent.wnfh_debug_color:
                        background frame_green
                    else:
                        background frame_transparent
                frame: # ======================== Кнопки
                    area(0.5, 0.5, 300, 50)
                    xanchor 0.5 yanchor 0.5
                    
                    if persistent.wnfh_debug_color:
                        background frame_blue
                    else:
                        background frame_transparent
            frame: # ======================== Кнопки
                if persistent.font_size == "small":
                    at wnfh_db_red_small
                elif persistent.font_size == "large":
                    at wnfh_db_red_large
                area(0.5, 0.5, 1480, 150)
                xanchor 0.5 yanchor 0.5
                
                if persistent.wnfh_debug_color:
                    background frame_red
                else:
                    background frame_transparent
            frame: # ======================== Кнопки
                area(0.5, 1.0, 1500, 4)
                xanchor 0.5 yanchor 0.5
                
                if persistent.wnfh_debug_color:
                    background frame_green
                else:
                    background frame_transparent

        frame: # ======================== Кнопки
            area(0.5, 0.7, 100, 50)
            xanchor 0.5 yanchor 0.5
            if persistent.wnfh_debug_color:
                background frame_black
            else:
                background frame_transparent
            grid 2 1:
                anchor (0.5, 0.5) pos (0.5, 0.5)
                spacing 20
                textbutton "+":
                    action SetField(persistent, "font_size", "large")
                textbutton "-":
                    action SetField(persistent, "font_size", "small")



        $ timeofday = persistent.timeofday
        frame: # ======================== Главный фрейм
            if persistent.font_size == "small":
                area(0.5, 1.0, 1.0, 150)
            elif persistent.font_size == "large":
                area(0.5, 1.0, 1.0, 200)
            xanchor 0.5 yanchor 1.0
            if persistent.wnfh_debug_color:
                background frame_black
            else:
                background frame_transparent

            frame: # ======================== Кнопка логов
                area(0.0, 0.5, 0.07, 1.0)
                xanchor 0.0 yanchor 0.5
                if persistent.wnfh_debug_color:
                    background frame_blue
                else:
                    background frame_transparent

                imagebutton:
                    idle wnfh_say_buttons["backward"][0]
                    hover wnfh_say_buttons["backward"][1]
                    xanchor 1.0 yanchor 0.5 
                    xpos 1.0 ypos 0.5
                    action ShowMenu("text_history")
            frame: # ======================== Кнопка перемотки
                area(1.0, 0.5, 0.07, 1.0)
                xanchor 1.0 yanchor 0.5 
                if persistent.wnfh_debug_color:
                    background frame_blue
                else:
                    background frame_transparent

                if not config.skipping:
                    imagebutton:
                        idle wnfh_say_buttons["forward"][0]
                        hover wnfh_say_buttons["forward"][1]
                        xanchor 0.0 yanchor 0.5
                        xpos 0.0 ypos 0.5
                        action Skip()
                else:
                    imagebutton:
                        idle wnfh_say_buttons["fast_forward"][0]
                        hover wnfh_say_buttons["fast_forward"][1]
                        xanchor 0.0 yanchor 0.5
                        xpos 0.0 ypos 0.5
                        action Skip()

            if persistent.font_size == "small":
                frame: # ======================== Главный блок
                    area(0.5, 1.0, 1555, 150)
                    xanchor 0.5 yanchor 1.0
                    if persistent.wnfh_debug_color:
                        background frame_black
                    else:
                        background frame_transparent
                    vbox:
                        anchor (0.5, 1.0) pos (0.5, 1.0)
                        add (wnfh_gui["tint_elements"]["db_line_upper"]):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                            xalign 0.5 yanchor 1.0 ypos 1.92
                        add (wnfh_gui["tint_elements"]["db_bg"]):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][2])
                            xalign 0.5
                        add (wnfh_gui["tint_elements"]["db_line_lower"]):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                            xalign 0.5
                    frame: # ======================== Текст
                        area(0.5, 1.0, 1.0, 110)
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
    
                            # Это говно Ритана, лень переписывать, просто спиздил. Может быть, когда-нибудь и переделаю.
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
                    vbox:
                        anchor (0.5, 1.0) pos (0.5, 1.0)
                        add (wnfh_gui["tint_elements"]["db_line_upper_large"]):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                            xalign 0.5 yanchor 1.0 ypos 1.92
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
                        area(0.0, 0.0, 350, 30)
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
    
                            # Это говно Ритана, лень переписывать, просто спиздил. Может быть, когда-нибудь и переделаю.
                            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/hide_%s.png"):
                                action HideInterface()
                            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/save_%s.png"):
                                action ShowMenu('save')
                            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/menu_%s.png"):
                                action ShowMenu('game_menu_selector')
                            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/load_%s.png"):
                                action ShowMenu('load')   

        
    
    screen wnfh_nvl:
        python:
            wnfh_say_buttons = {
                "backward": [im.Flip(im.Composite( # idle
                                (73, 83),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_bg_1"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                ), horizontal=True),
                            im.Flip(im.Composite( # hover
                                (73, 83),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_bg_1"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_hover"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 0, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                ), horizontal=True)
                            ],
                "forward": [im.Composite( # idle
                                (73, 83),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_bg_1"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                ),
                            im.Composite( # hover
                                (73, 83),
                                (0, 0),  im.MatrixColor(wnfh_gui["tint_elements"]["button_bg_1"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_hover"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 0, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                )
                            ],
                "fast_forward": [im.Composite( # idle
                                (95, 83),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_bg_2"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                (20, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                ),
                            im.Composite( # hover
                                (95, 83),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_bg_2"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_hover"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 0, persistent.timeofday))),
                                (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                (20, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_line"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                                )
                            ]

            }
        $ timeofday = persistent.timeofday
        frame: # ======================== Главный фрейм
            if persistent.font_size == "small":
                area(0.5, 1.0, 1.0, 150)
            if persistent.font_size == "large":
                area(0.5, 1.0, 1.0, 200)
            xanchor 0.5 yanchor 1.0
            if persistent.wnfh_debug_color:
                background frame_black
            else:
                background frame_transparent
            frame: # ======================== Кнопочки
                area(0.0, 0.5, 0.07, 1.0)
                xanchor 0.0 yanchor 0.5
                if persistent.wnfh_debug_color:
                    background frame_blue
                else:
                    background frame_transparent

                imagebutton:
                    idle wnfh_say_buttons["backward"][0]
                    hover wnfh_say_buttons["backward"][1]
                    xanchor 1.0 yanchor 0.5 
                    xpos 1.0 ypos 0.5
                    action ShowMenu("text_history")
            frame: # ======================== Кнопочки
                area(1.0, 0.5, 0.07, 1.0)
                xanchor 1.0 yanchor 0.5
                if persistent.wnfh_debug_color:
                    background frame_blue
                else:
                    background frame_transparent

                if not config.skipping:
                    imagebutton:
                        idle wnfh_say_buttons["forward"][0]
                        hover wnfh_say_buttons["forward"][1]
                        xanchor 0.0 yanchor 0.5
                        xpos 0.0 ypos 0.5
                        action Skip()
                else:
                    imagebutton:
                        idle wnfh_say_buttons["fast_forward"][0]
                        hover wnfh_say_buttons["fast_forward"][1]
                        xanchor 0.0 yanchor 0.5
                        xpos 0.0 ypos 0.5
                        action Skip()  

            frame: # ======================== Главный блок
                area(0.5, 1.0, 1555, 1080)
                xanchor 0.5 yanchor 1.0
                if persistent.wnfh_debug_color:
                    background frame_green
                else:
                    background frame_transparent
                vbox:
                    anchor (0.5, 1.0) pos (0.5, 1.0)
                    add (wnfh_gui["tint_elements"]["db_line_lower"]):
                        matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                        xalign 0.5 yanchor 1.0 ypos 1.0
                    add (wnfh_gui["tint_elements"]["nvl_bg"]):
                        matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][2])
                        xalign 0.5 yzoom 10.0
                    add (wnfh_gui["tint_elements"]["db_line_lower"]):
                        matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                        xalign 0.5
    
                frame: # ======================== Текст
                    if persistent.wnfh_debug_color:
                        background frame_red
                    else:
                        background frame_transparent
                    area(0.5, 1.0, 0.96, 0.96)
                    xanchor 0.5 yanchor 1.0 
                    vbox:
                        for who, what, who_id, what_id, window_id in dialogue:
                            window:
                                id window_id
                                has hbox:
                                    spacing 10
                                if persistent.font_size == "large":
                                    if who is not None:
                                        text who id who_id size 35
                                    text what id what_id size 35
                                elif persistent.font_size == "small":
                                    if who is not None:
                                        text who id who_id size 28
                                    text what id what_id size 28
                        if items:
                            vbox:
                                id "menu"
                                for caption, action, chosen in items:
                                    if action:
                                        button:
                                            style "nvl_menu_choice_button"
                                            action action
                                            text caption style "nvl_menu_choice"
                                    else:
                                        text caption style "nvl_dialogue"
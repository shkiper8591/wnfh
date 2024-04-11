init 2:  
    screen wnfh_say: 
        default wnfh_play_animation= False      
        python:
            global wnfh_test_1
            wnfh_test_1 = wnfh_play_animation
            def say_anim():     
                amd = int(persistent.font_size <= "large") if wnfh_test_1 else 2
                return amd
            def say_size():
                return int(persistent.font_size <= "large")
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
            wnfh_db_buttons = {
                "minus": [wnfh_gui["tint_elements"]["db_button_minus"]  ,[SetScreenVariable("wnfh_play_animation", True),SetField(persistent, "font_size", "small")]  ],
                "plus":  [wnfh_gui["tint_elements"]["db_button_plus"]   ,[SetScreenVariable("wnfh_play_animation", True),SetField(persistent, "font_size", "large")]  ],
                "save":  [wnfh_gui["tint_elements"]["db_button_save"]   ,ShowMenu('save')                                                                             ],
                "load":  [wnfh_gui["tint_elements"]["db_button_load"]   ,ShowMenu('load')                                                                      ],
                "menu":  [wnfh_gui["tint_elements"]["db_button_menu"]   ,ShowMenu('game_menu_selector')                                                               ],
                "hide":  [wnfh_gui["tint_elements"]["db_button_hide"]   ,HideInterface()                                                                              ],
            }
        frame:
            area(0.5, 0.99, 1.0, 185)
            if persistent.wnfh_debug_color:
                background frame_black
            else:
                background frame_transparent
            xanchor 0.5 yanchor 1.0 padding(0, 0)

            frame: # ======================== Диалоговое окно
                if persistent.font_size == "small":
                    area(0.5, 1.0, 1500, 135)
                elif persistent.font_size == "large":
                    area(0.5, 1.0, 1500, 185)
    
                xanchor 0.5 yanchor 1.0 padding(0, 0)
                if persistent.wnfh_debug_color:
                    background frame_black
                else:
                    background frame_transparent
                vbox:
                    xanchor 0.5 yanchor 1.0
                    xpos 0.5 ypos 1.0
                    spacing 0
                    
                    hbox:
                        xanchor 0.0 yanchor 0.0
                        xpos 0.0 ypos 1.0
                        frame:
                            area(0.0, 0.5, wnfh_frames_elements["db_brow_bg1"][1], wnfh_frames_elements["db_brow_bg1"][2])
                            xanchor 0.0 yanchor 0.5 padding(0, 0)
                            
                            if persistent.wnfh_debug_color:
                                background frame_blue
                            else:
                                background frame_transparent
                            add Frame(wnfh_frames_elements["db_brow_bg1"][0], left=wnfh_frames_elements["db_brow_bg1"][3], top=0):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][wnfh_frames_elements["db_brow_bg1"][4]])
                            add Frame(wnfh_frames_elements["db_brow_line1"][0], left=wnfh_frames_elements["db_brow_line1"][3], top=0):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][wnfh_frames_elements["db_brow_line1"][4]])
                            
                        frame:
                            at (wnfh_frames_elements["db_brow_bg2"][6])[say_anim()]
                            area(0.0, 0.5, (wnfh_frames_elements["db_brow_bg2"][1], wnfh_frames_elements["db_brow_bg2"][1]+100)[say_size()], wnfh_frames_elements["db_brow_bg2"][2])
                            xanchor 0.0 yanchor 0.5 padding(0, 0)
                            
                            if persistent.wnfh_debug_color:
                                background frame_blue
                            else:
                                background frame_transparent
                            add Frame(wnfh_frames_elements["db_brow_bg2"][0], left=wnfh_frames_elements["db_brow_bg2"][3], top=0):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][wnfh_frames_elements["db_brow_bg2"][4]])
                            add Frame(wnfh_frames_elements["db_brow_line2"][0], left=wnfh_frames_elements["db_brow_line2"][3], top=0):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][wnfh_frames_elements["db_brow_line2"][4]])
                            frame: # ======================== Имя
                                area(0.0, 0.0, (wnfh_frames_elements["db_brow_line"][1]-40, wnfh_frames_elements["db_brow_line"][1]+50)[say_size()], wnfh_frames_elements["db_brow_line"][2])
                                if persistent.wnfh_debug_color:
                                    background frame_green
                                else:
                                    background frame_transparent
                                if who:
                                    text who id "who":
                                        anchor (0.0, 0.0) pos (-5, 0.0)
                                        size (28, 35)[say_size()]
                                        line_spacing 1
                        frame:
                            area(0.0, 0.5, wnfh_frames_elements["db_brow_bg3"][1], wnfh_frames_elements["db_brow_bg3"][2])
                            xanchor 0.0 yanchor 0.5 padding(0, 0)
                            
                            if persistent.wnfh_debug_color:
                                background frame_blue
                            else:
                                background frame_transparent
                            add Frame(wnfh_frames_elements["db_brow_bg3"][0], left=wnfh_frames_elements["db_brow_bg3"][3], top=0):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][wnfh_frames_elements["db_brow_bg3"][4]])
                            add Frame(wnfh_frames_elements["db_brow_line3"][0], left=wnfh_frames_elements["db_brow_line3"][3], top=0):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][wnfh_frames_elements["db_brow_line3"][4]])
                    hbox:
                        xanchor 1.0 yanchor 0.5
                        xpos 1.0 ypos 0.5        
                        frame:
                            at (wnfh_frames_elements["db_mid_line"][6])[say_anim()]
                            area(1.0, 1.0, (wnfh_frames_elements["db_mid_line"][1], wnfh_frames_elements["db_mid_line"][1]-100)[say_size()], wnfh_frames_elements["db_mid_line"][2])
                            xanchor 1.0 yanchor 1.0 padding(0, 0)
                            
                            if persistent.wnfh_debug_color:
                                background frame_green
                            else:
                                background frame_transparent
                            add Frame(wnfh_frames_elements["db_mid_line"][0], left=wnfh_frames_elements["db_mid_line"][3], right=55, top=0):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][wnfh_frames_elements["db_mid_line"][4]])
                        frame: # ======================== Кнопки
                            area(1.0, 0.5, wnfh_frames_elements["db_brow_line"][1], wnfh_frames_elements["db_brow_line"][2])
                            xanchor 1.0 yanchor 0.5 padding(0, 0)
                            
                            if persistent.wnfh_debug_color:
                                background frame_blue
                            else:
                                background frame_transparent
                            add Frame(wnfh_frames_elements["db_brow_bg"][0], left=wnfh_frames_elements["db_brow_bg"][3], right=55, top=0):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][wnfh_frames_elements["db_brow_bg"][4]])
                                xzoom -1.0
                            add Frame(wnfh_frames_elements["db_brow_line"][0], left=wnfh_frames_elements["db_brow_line"][3], right=55, top=0):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][wnfh_frames_elements["db_brow_line"][4]])
                                xzoom -1.0
                            hbox:
                                anchor (0.5, 0.5) pos (0.5, 0.5)
                                spacing 20
                                # Это говно Ритана, лень переписывать, просто спиздил. Может быть, когда-нибудь и переделаю.
                                for i in ["hide", "save", "menu", "load"]:
                                    imagebutton:
                                        idle im.MatrixColor(wnfh_db_buttons[i][0], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 0, persistent.timeofday)))
                                        hover im.MatrixColor(wnfh_db_buttons[i][0], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday)))
                                        action wnfh_db_buttons[i][1]
                                if persistent.font_size == "small":
                                    imagebutton:
                                        idle im.MatrixColor(wnfh_db_buttons["plus"][0], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 0, persistent.timeofday)))
                                        hover im.MatrixColor(wnfh_db_buttons["plus"][0], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday)))
                                        action wnfh_db_buttons["plus"][1]
                                elif persistent.font_size == "large":
                                    imagebutton:
                                        idle im.MatrixColor(wnfh_db_buttons["minus"][0], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 0, persistent.timeofday)))
                                        hover im.MatrixColor(wnfh_db_buttons["minus"][0], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday)))
                                        action wnfh_db_buttons["minus"][1] 

                    frame:
                        at (wnfh_frames_elements["db_bg"][6])[say_anim()]
                        area(0.5, 0.5, wnfh_frames_elements["db_bg"][1], (wnfh_frames_elements["db_bg"][2], wnfh_frames_elements["db_bg"][2]+50)[say_size()]) 
                        xanchor 0.5 yanchor 0.5 padding(0, 0)
                        
                        if persistent.wnfh_debug_color:
                            background frame_red
                        else:
                            background frame_transparent
                        add Frame(wnfh_frames_elements["db_bg"][0], left=wnfh_frames_elements["db_bg"][3], top=0):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][wnfh_frames_elements["db_bg"][4]])
        
                    frame:
                        area(0.5, 0.5, wnfh_frames_elements["db_line_lower"][1], wnfh_frames_elements["db_line_lower"][2])
                        xanchor 0.5 yanchor 0.5 padding(0, 0)
                        
                        if persistent.wnfh_debug_color:
                            background frame_green
                        else:
                            background frame_transparent
                        add Frame(wnfh_frames_elements["db_line_lower"][0], left=wnfh_frames_elements["db_line_lower"][3], top=0):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][wnfh_frames_elements["db_line_lower"][4]])
                frame: # ======================== Текст
                    at (wnfh_frames_elements["db_bg"][6])[say_anim()]
                    area(0.5, 1.0, wnfh_frames_elements["db_bg"][1], (wnfh_frames_elements["db_bg"][2]+5, wnfh_frames_elements["db_bg"][2]+55)[say_size()])
                    xanchor 0.5 yanchor 1.0
                    if persistent.wnfh_debug_color:
                        background frame_red
                    else:
                        background frame_transparent
                    text what id "what":
                        anchor (0.0, 0.0) pos (20, 0.0)
                        xmaximum wnfh_frames_elements["db_bg"][1]-40
                        size (28, 35)[say_size()]
                        line_spacing 1
            frame: # ======================== Кнопка логов
                at (wnfh_db_buttons_small, wnfh_db_buttons_large, None)[say_anim()]
                area(0.0, (0.65, 0.5)[say_size()], 0.07, 0.5)
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
                at (wnfh_db_buttons_small, wnfh_db_buttons_large, None)[say_anim()]
                area(1.0, (0.65, 0.5)[say_size()], 0.07, 0.5)
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
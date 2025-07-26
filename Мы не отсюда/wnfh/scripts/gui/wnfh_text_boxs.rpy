screen wnfh_say(who, what, two_windows = False):
    $ debug_frame = {
            "black":  frame_black  if persistent.wnfh_debug_color else frame_transparent,
            "red":    frame_red    if persistent.wnfh_debug_color else frame_transparent,
            "green":  frame_green  if persistent.wnfh_debug_color else frame_transparent,
            "blue":   frame_blue   if persistent.wnfh_debug_color else frame_transparent,
            "purple": frame_purpl  if persistent.wnfh_debug_color else frame_transparent
        }

    default wnfh_play_animation = False
    
    python:
        persistent.sprite_time = renpy.store.wnfh_spritetime  #проверить
        global wnfh_test_1
        wnfh_test_1 = wnfh_play_animation
        wnfh_say_buttons  = MatrixConverter({
            "backward":
                [
                    [(73, 83), [[(0, 0), "button_bg_1", 2], [(0, 0), "button_line", 1]],True],
                    [(73, 83), [[(0, 0), "button_bg_1", 2], [(0, 0), "button_hover", 0],[(0, 0), "button_line", 1]],True]
                ],
            "forward":
                [
                    [(73, 83), [[(0, 0), "button_bg_1", 2], [(0, 0), "button_line", 1]]],
                    [(73, 83), [[(0, 0), "button_bg_1", 2], [(0, 0), "button_hover", 0],[(0, 0), "button_line", 1]]]
                ],
            "fast_forward":
                [
                    [(95, 83), [[(0, 0), "button_bg_2", 2], [(0, 0), "button_line", 1], [(20, 0), "button_line", 1]]],
                    [(95, 83), [[(0, 0), "button_bg_2", 2], [(0, 0), "button_hover", 0], [(0, 0), "button_line", 1],[(20, 0), "button_line", 1]]],
                ],
        })
        wnfh_db_buttons = {
            "minus": [wnfh_gui["tint_elements"]["db_button_minus"]    ,[SetScreenVariable("wnfh_play_animation", True),SetField(persistent, "font_size", "small")]  ],
            "plus":  [wnfh_gui["tint_elements"]["db_button_plus"]     ,[SetScreenVariable("wnfh_play_animation", True),SetField(persistent, "font_size", "large")]  ],
            "mute":  [wnfh_gui["tint_elements"]["db_button_mute"]     ,[Preference("all mute", "enable"),  SetField(persistent, "all_sound", "unmute")]               ],
            "unmute":[wnfh_gui["tint_elements"]["db_button_unmute"]   ,[Preference("all mute", "disable"), SetField(persistent, "all_sound", "mute")]             ],
            "save":  [wnfh_gui["tint_elements"]["db_button_save"]     ,ShowMenu('save')                                                                             ],
            "load":  [wnfh_gui["tint_elements"]["db_button_load"]     ,ShowMenu('load')                                                                             ],
            "menu":  [wnfh_gui["tint_elements"]["db_button_menu"]     ,ShowMenu('game_menu_selector')                                                               ],
            "hide":  [wnfh_gui["tint_elements"]["db_button_hide"]     ,HideInterface()                                                                              ],
        }
    frame:
        area(0.5, 0.99, 1.0, 185)
        background debug_frame["black"]
        xanchor 0.5 yanchor 1.0 padding(0, 0)
        frame: # ======================== Диалоговое окно
            if persistent.font_size == "small":
                area(0.5, 1.0, 1500, 135)
            elif persistent.font_size == "large":
                area(0.5, 1.0, 1500, 185)

            xanchor 0.5 yanchor 1.0 padding(0, 0)
            background debug_frame["black"]
            vbox:
                xanchor 0.5 yanchor 1.0
                xpos 0.5 ypos 1.0
                spacing 0
                box_reverse True
                frame:
                    area(0.5, 0.5, wnfh_frames_elements["db_line_lower"][1], wnfh_frames_elements["db_line_lower"][2])
                    xanchor 0.5 yanchor 0.5 padding(0, 0)
                    background debug_frame["green"]
                    add Frame(wnfh_frames_elements["db_line_lower"][0], left=wnfh_frames_elements["db_line_lower"][3], top=0):
                        matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["db_line_lower"][4]])
                frame:
                    at (wnfh_frames_elements["db_bg"][6])[say_anim()]
                    area(0.5, 0.5, wnfh_frames_elements["db_bg"][1], (wnfh_frames_elements["db_bg"][2], wnfh_frames_elements["db_bg"][2]+50)[say_size()]) 
                    xanchor 0.5 yanchor 0.5 padding(0, 0)
                    background debug_frame["red"]
                    add Frame(wnfh_frames_elements["db_bg"][0], left=wnfh_frames_elements["db_bg"][3], top=0):
                        matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["db_bg"][4]])
                hbox:
                    xanchor 1.0 yanchor 0.5
                    xpos 1.0 ypos 0.5        
                    frame:
                        at (wnfh_frames_elements["db_mid_line"][6])[say_anim()]
                        area(1.0, 1.0, (wnfh_frames_elements["db_mid_line"][1], wnfh_frames_elements["db_mid_line"][1]-90)[say_size()], wnfh_frames_elements["db_mid_line"][2])
                        xanchor 1.0 yanchor 1.0 padding(0, 0)
                        background debug_frame["green"]
                        add Frame(wnfh_frames_elements["db_mid_line"][0], left=wnfh_frames_elements["db_mid_line"][3], right=55, top=0):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["db_mid_line"][4]])
                    frame: # ======================== Кнопки
                        area(1.0, 0.5, wnfh_frames_elements["db_brow_line"][1], wnfh_frames_elements["db_brow_line"][2])
                        xanchor 1.0 yanchor 0.5 padding(0, 0)
                        background debug_frame["blue"]
                        add Frame(wnfh_frames_elements["db_brow_bg"][0], left=wnfh_frames_elements["db_brow_bg"][3], right=55, top=0):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["db_brow_bg"][4]])
                            xzoom -1.0
                        add Frame(wnfh_frames_elements["db_brow_line"][0], left=wnfh_frames_elements["db_brow_line"][3], right=55, top=0):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["db_brow_line"][4]])
                            xzoom -1.0
                        hbox:
                            anchor (0.5, 0.5) pos (0.5, 0.5)
                            spacing 20
                            for i in ["hide", "save", "menu", "load"]:
                                imagebutton:
                                    idle Transform(wnfh_db_buttons[i][0],  matrixcolor = TintMatrix(wnfh_tint_color[ renpy.store.wnfh_tymeofday][0]))
                                    hover Transform(wnfh_db_buttons[i][0], matrixcolor = TintMatrix(wnfh_tint_color[ renpy.store.wnfh_tymeofday][1]))
                                    action wnfh_db_buttons[i][1]
                            if persistent.all_sound == "mute":
                                imagebutton:
                                    idle Transform(wnfh_db_buttons["mute"][0],  matrixcolor = TintMatrix(wnfh_tint_color[ renpy.store.wnfh_tymeofday][0]))
                                    hover Transform(wnfh_db_buttons["mute"][0], matrixcolor = TintMatrix(wnfh_tint_color[ renpy.store.wnfh_tymeofday][1]))
                                    action wnfh_db_buttons["mute"][1]
                            elif persistent.all_sound == "unmute":
                                imagebutton:
                                    idle Transform(wnfh_db_buttons["unmute"][0],  matrixcolor = TintMatrix(wnfh_tint_color[ renpy.store.wnfh_tymeofday][0]))
                                    hover Transform(wnfh_db_buttons["unmute"][0], matrixcolor = TintMatrix(wnfh_tint_color[ renpy.store.wnfh_tymeofday][1]))
                                    action wnfh_db_buttons["unmute"][1]
                            
                            if persistent.font_size == "small":
                                imagebutton:
                                    idle Transform(wnfh_db_buttons["plus"][0],  matrixcolor = TintMatrix(wnfh_tint_color[ renpy.store.wnfh_tymeofday][0]))
                                    hover Transform(wnfh_db_buttons["plus"][0], matrixcolor = TintMatrix(wnfh_tint_color[ renpy.store.wnfh_tymeofday][1]))
                                    action wnfh_db_buttons["plus"][1]
                            elif persistent.font_size == "large":
                                imagebutton:
                                    idle Transform(wnfh_db_buttons["minus"][0],  matrixcolor = TintMatrix(wnfh_tint_color[ renpy.store.wnfh_tymeofday][0]))
                                    hover Transform(wnfh_db_buttons["minus"][0], matrixcolor = TintMatrix(wnfh_tint_color[ renpy.store.wnfh_tymeofday][1]))
                                    action wnfh_db_buttons["minus"][1]
                            
                hbox:
                    xanchor 0.0 yanchor 0.0
                    xpos 0.0 ypos 1.0
                    box_reverse True
                    frame:
                        area(0.0, 0.5, wnfh_frames_elements["db_brow_bg3"][1], wnfh_frames_elements["db_brow_bg3"][2])
                        xanchor 0.0 yanchor 0.5 padding(0, 0)
                        background debug_frame["blue"]
                        add Frame(wnfh_frames_elements["db_brow_bg3"][0], left=wnfh_frames_elements["db_brow_bg3"][3], top=0):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["db_brow_bg3"][4]])
                        add Frame(wnfh_frames_elements["db_brow_line3"][0], left=wnfh_frames_elements["db_brow_line3"][3], top=0):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["db_brow_line3"][4]])
                    frame:
                        at (wnfh_frames_elements["db_brow_bg2"][6])[say_anim()]
                        area(0.0, 0.5, (wnfh_frames_elements["db_brow_bg2"][1], wnfh_frames_elements["db_brow_bg2"][1]+90)[say_size()], wnfh_frames_elements["db_brow_bg2"][2])
                        xanchor 0.0 yanchor 0.5 padding(0, 0)
                        background debug_frame["blue"]
                        add Frame(wnfh_frames_elements["db_brow_bg2"][0], left=wnfh_frames_elements["db_brow_bg2"][3], top=0):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["db_brow_bg2"][4]])
                        add Frame(wnfh_frames_elements["db_brow_line2"][0], left=wnfh_frames_elements["db_brow_line2"][3], top=0):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["db_brow_line2"][4]])
                    frame:
                        area(0.0, 0.5, wnfh_frames_elements["db_brow_bg1"][1], wnfh_frames_elements["db_brow_bg1"][2])
                        xanchor 0.0 yanchor 0.5 padding(0, 0)
                        background debug_frame["blue"]
                        add Frame(wnfh_frames_elements["db_brow_bg1"][0], left=wnfh_frames_elements["db_brow_bg1"][3], top=0):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["db_brow_bg1"][4]])
                        add Frame(wnfh_frames_elements["db_brow_line1"][0], left=wnfh_frames_elements["db_brow_line1"][3], top=0):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["db_brow_line1"][4]])
                        frame: # ======================== Имя
                            area(0.0, 0.0, (wnfh_frames_elements["db_brow_line"][1]-40, wnfh_frames_elements["db_brow_line"][1]+50)[say_size()], wnfh_frames_elements["db_brow_line"][2])
                            background debug_frame["green"]
                            if who:
                                text who id "who":
                                    #anchor (0.0, 0.0) pos (-(wnfh_frames_elements["db_brow_bg2"][1]+5, wnfh_frames_elements["db_brow_bg2"][1]+105)[say_size()], 0.0)
                                    anchor (0.0, 0.0) pos (20, 0.0)
                                    size (28, 35)[say_size()]
                                    line_spacing 1
            frame: # ======================== Текст
                at (wnfh_frames_elements["db_bg"][6])[say_anim()]
                area(0.5, 1.0, wnfh_frames_elements["db_bg"][1], (wnfh_frames_elements["db_bg"][2]+5, wnfh_frames_elements["db_bg"][2]+55)[say_size()])
                xanchor 0.5 yanchor 1.0
                background debug_frame["red"]
                text what id "what":
                    anchor (0.0, 0.0) pos (20, 0.0)
                    xmaximum wnfh_frames_elements["db_bg"][1]-40
                    size (28, 35)[say_size()]
                    line_spacing 1
        frame: # ======================== Кнопка логов
            at (wnfh_db_buttons_small, wnfh_db_buttons_large, None)[say_anim()]
            area(0.0, (0.65, 0.5)[say_size()], 0.07, 0.5)
            xanchor 0.0 yanchor 0.5
            background debug_frame["blue"]
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
            background debug_frame["blue"]
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
        def MatrixConverter(dictionary_obj):
            main_dick={}
            for button in dictionary_obj:
                temp_array=[]
                for obj in dictionary_obj[button]:
                    compozite = []
                    compozite.append(obj[0])
                    for obj_index in range(len(obj[1])):
                        compozite.append(obj[1][obj_index][0])
                        compozite.append(im.MatrixColor(wnfh_gui["tint_elements"][obj[1][obj_index][1]], im.matrix.tint(*converter_hex('wnfh_tint_color', obj[1][obj_index][2], renpy.store.wnfh_tymeofday))))
                    compozite_obj = im.Composite(*compozite)
                    try:
                        if obj[-1] is True:
                            flip_args = True
                        else:
                            flip_args=None
                    except Exception as E:
                        flip_args = None
                    if flip_args != None:
                        temp_array.append(im.Flip(compozite_obj,flip=True,horizontal=True))
                    else:
                        temp_array.append(compozite_obj)
                main_dick[button]=temp_array
            return main_dick
        wnfh_say_buttons  = MatrixConverter({
            "backward":
                [
                    [(73, 83), [[(0, 0), "button_bg_1", 2], [(0, 0), "button_line", 1]],True],
                    [(73, 83), [[(0, 0), "button_bg_1", 2], [(0, 0), "button_hover", 0],[(0, 0), "button_line", 1]],True]
                ],
            "forward":
                [
                    [(73, 83), [[(0, 0), "button_bg_1", 2], [(0, 0), "button_line", 1]]],
                    [(73, 83), [[(0, 0), "button_bg_1", 2], [(0, 0), "button_hover", 0],[(0, 0), "button_line", 1]]]
                ],
            "fast_forward":
                [
                    [(95, 83), [[(0, 0), "button_bg_2", 2], [(0, 0), "button_line", 1], [(20, 0), "button_line", 1]]],
                    [(95, 83), [[(0, 0), "button_bg_2", 2], [(0, 0), "button_hover", 0], [(0, 0), "button_line", 1],[(20, 0), "button_line", 1]]],
                ],
        })
    frame: # ======================== Главный фрейм
        if persistent.font_size == "small":
            area(0.5, 1.0, 1.0, 150)
        if persistent.font_size == "large":
            area(0.5, 1.0, 1.0, 200)
        xanchor 0.5 yanchor 1.0
        background debug_frame["black"]
        frame: # ======================== Кнопочки
            area(0.0, 0.5, 0.07, 1.0)
            xanchor 0.0 yanchor 0.5
            background debug_frame["blue"]
            imagebutton:
                idle wnfh_say_buttons["backward"][0]
                hover wnfh_say_buttons["backward"][1]
                xanchor 1.0 yanchor 0.5 
                xpos 1.0 ypos 0.5
                action ShowMenu("text_history")
        frame: # ======================== Кнопочки
            area(1.0, 0.5, 0.07, 1.0)
            xanchor 1.0 yanchor 0.5
            background debug_frame["blue"]
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
            background debug_frame["green"]
            vbox:
                anchor (0.5, 1.0) pos (0.5, 1.0)
                add Frame(wnfh_frames_elements["db_line_lower"][0], left=wnfh_frames_elements["db_line_lower"][3], top=0):
                    matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["db_line_lower"][4]])
                    xalign 0.5 yanchor 1.0 ypos 1.0
                add (wnfh_gui["tint_elements"]["frame_bg"]):
                    matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][2])
                    xalign 0.5 yzoom 10.0
                add Frame(wnfh_frames_elements["db_line_lower"][0], left=wnfh_frames_elements["db_line_lower"][3], top=0):
                    matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["db_line_lower"][4]])
                    xalign 0.5

            frame: # ======================== Текст
                background debug_frame["red"]
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
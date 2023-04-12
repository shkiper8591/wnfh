init 2:
    
    screen blwnfh_preferences():
        modal True tag menu
        $ bar_full = Frame(blwnfh_gui["settings"]["bar_full"], 73, 73)
        $ bar_null = Frame(blwnfh_gui["settings"]["bar_null"], 73, 73)
        $ htumb    = blwnfh_gui["settings"]["htumb"]
        key "game_menu":
            action NullAction()
        
        key "screenshot":
            action NullAction()
                
        python:
            def menu_img_status(imgf, condition="hover"):
                if condition == "hover":
                    return im.MatrixColor(imgf, im.matrix.contrast(1.7))
                if condition == "insensitive":
                    return im.Alpha(imgf, 0.38)
                    
            blwnfh_preferences_button = [
                
                 #Тег кнопки    #Изображение кнопки                               #Действие кнопки
                ["return"      ,blwnfh_gui["settings"]["return"]               ,[Return()]                                           ],
                
            ]
            blwnfh_preferences_bar = [
                
                 #Тег бара           #Название бара                       #Действие ,fhf
                ["music"            ,"Музыка"              ,Preference("music volume")                                       ],
                ["sound"            ,"Звуки"               ,Preference("sound volume")                                       ],
                ["ambience"         ,"Эмбиент"             ,Preference("voice volume")                                       ],
                ["text_speed"       ,"Скорость текста"     ,Preference("text speed")                                         ],
                ["autoforward_time" ,"Время автопереходов" ,Preference("auto-forward time")                                  ],
            ]
        #$ background_color = "#0000"
        #$ button_red =       "#0000"
        #$ button_green =     "#0000"
        #$ button_blue =      "#0000"

        $ background_color = "#0005"
        $ button_red =       "#F005"
        $ button_green =     "#0F05"
        $ button_blue =      "#00F5"
        
        frame:
            background im.MatrixColor(im.Blur(blwnfh_gui["main_menu"]["mm_bg"], 3.0), im.matrix.tint(0.7, 0.7, 0.7))
            area(0.0, 0.0, 1.0, 1.0)
        frame:
            background blwnfh_gui["settings"]["base"]
            area(0.5, 0.0, 1461, 1080)
            xanchor 0.5
            
            frame:
                background background_color
                area(0.5, 0.0, 1.0, 0.15)
                xanchor 0.5
            
                frame: # ======================================================= # Выход
                    background background_color
                    area(0.0, 0.0, 200, 100)
                    xanchor 0.0 yanchor 0.0
                    for button in blwnfh_preferences_button[0:1]:
                        frame:
                            xmargin 5
                            background button_blue
                            area(0.0, 0.5, 1.0, 1.0)
                            xanchor 0.0 yanchor 0.5
                            imagebutton:
                                action [button[2]]
                                idle button[1]
                                hover button[1]
                                hover_sound blwnfh_gui["sound"]["plimp"]
                                at blwnfh_mm_button_hover_atl()
                                
                add blwnfh_gui["settings"]["pref_title"]:
                    pos(0.5, 0.0)
                    xanchor 0.5
            
            frame:
                background background_color
                area(0.5, 0.16, 1.0, 0.84)
                xanchor 0.5
                grid 1 3:
                    for bar in blwnfh_preferences_bar[0:3]:
                        frame:
                            background background_color
                            area(0.0, 0.0, 1.0, 120)
                            frame:
                                background button_red
                                area(0.0, 0.5, 0.2, 1.0)
                                yanchor 0.5
                                text bar[1]:
                                    pos(0.5, 0.5)
                                    style "blwnfh_settings"
                                    xanchor 0.5
                                    size 70
                                    kerning 1
                                    min_width 200
                                    layout "tex"
                                    #action Play("sound", blwnfh_gui["sound"]["plimp"]) 
                            frame:
                                background button_green
                                area(0.95, 0.5, 0.75, 0.8)
                                xanchor 1.0 yanchor 0.5
                                bar value bar[2]:
                                    left_bar bar_full
                                    right_bar bar_null
                                    thumb htumb
                                    hover_thumb htumb
                                    xmaximum 1.0 ymaximum 73 yanchor 0.5 ypos 0.5
                                
                add blwnfh_gui["settings"]["line"]:
                    pos(0.5, 0.41)
                    xanchor 0.5
                grid 1 2:
                    pos(0.5, 0.42)
                    xanchor 0.5
                    for bar in blwnfh_preferences_bar[3:5]:
                        frame:
                            background background_color
                            area(0.0, 0.0, 1.0, 120)
                            frame:
                                background button_red
                                area(0.0, 0.5, 0.2, 1.0)
                                yanchor 0.5
                                text bar[1]:
                                    pos(0.5, 0.5)
                                    style "blwnfh_settings"
                                    xanchor 0.5
                                    size 50
                                    kerning 1
                                    min_width 200
                                    layout "tex"
                            frame:
                                background button_green
                                area(0.95, 0.5, 0.75, 0.8)
                                xanchor 1.0 yanchor 0.5
                                bar value bar[2]:
                                    left_bar bar_full
                                    right_bar bar_null
                                    thumb htumb
                                    hover_thumb htumb
                                    xmaximum 1.0 ymaximum 73 yanchor 0.5 ypos 0.5
                add blwnfh_gui["settings"]["line"]:
                    pos(0.5, 0.695)
                    xanchor 0.5
                frame:
                    background background_color
                    area(0.5, 1.0, 1.0, 0.3)
                    xanchor 0.5 yanchor 1.0
                    frame:
                        background background_color
                        area(0.5, 0.0, 300, 100)
                        xanchor 0.5 yanchor 0.0
                    frame:
                        background background_color
                        area(0.0, 0.0, 500, 100)
                        xanchor 0.0 yanchor 0.0
                        frame:
                            background button_blue
                            area(1.0, 0.5, 100, 55)
                            xanchor 1.0 yanchor 0.5
                            if _preferences.fullscreen:
                                imagebutton:
                                    idle blwnfh_gui["settings"]["on"]
                                    hover blwnfh_gui["settings"]["on"]
                                    action Preference("display", "window")
                            if not _preferences.fullscreen:
                                imagebutton:
                                    idle blwnfh_gui["settings"]["off"]
                                    hover blwnfh_gui["settings"]["off"]
                                    action Preference("display", "fullscreen")
                        frame:
                            background button_red
                            area(0.0, 0.5, 380, 55)
                            xanchor 0.0 yanchor 0.5
                            text "Полный экран":
                                pos(0.5, 0.5)
                                style "blwnfh_settings"
                                xanchor 0.5
                                text_align 1.0
                                size 50
                                kerning 1
                                min_width 200
                                layout "tex"

            

















screen settings_widget_sukablyat_on_blwnfh():
    text "Маты будут выглядеть так: блять" xpos 0.653 ypos 0.6:
        style "blwnfh_settings"
screen settings_widget_sukablyat_off_blwnfh():
    text "Выключить матфильтр" xpos 0.653 ypos 0.6:
        style "blwnfh_settings"   
screen settings_widget_sukablyat_type_censor_blwnfh():
    text "Маты будут выглядеть так: @%#$!" xpos 0.653 ypos 0.6:
        style "blwnfh_settings"
screen settings_widget_sukablyat_type_change_blwnfh():
    text "Маты будут выглядеть так: блин" xpos 0.653 ypos 0.6:
        style "blwnfh_settings"

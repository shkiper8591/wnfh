init 2:
    
    screen wnfh_menu():
        modal True tag menu
        
        key "game_menu":
            action NullAction()
        
        key "screenshot":
            action NullAction()

        python:
            from random import randrange
            
            def menu_img_status(imgf, condition="hover"):
                if condition == "hover":
                    return im.MatrixColor(imgf, im.matrix.contrast(1.7))
                if condition == "insensitive":
                    return im.Alpha(imgf, 0.38)
            
            wnfh_mm_left_buttons = [
                ["achievements" ,"Достижения" ,[ShowMenu("wnfh_achievements", _transition=dissolve)]  ],
                ["galary"  ,"Галерея"   ,[Jump("technical_chocolatki")]                     ],
                ["scheme"  ,"Схема"     ,[ShowMenu("wnfh_schematic", _transition=dissolve)] ],
            ]
            wnfh_mm_right_buttons = [
                ["credits" ,"Создатели" ,[Jump("technical_chocolatki")]                     ],
                ["saves"        ,"Загрузить"  ,[ShowMenu("wnfh_load_screen", _transition=dissolve)]   ],
                ["preferences"  ,"Настройки"  ,[ShowMenu("wnfh_preferences", _transition=dissolve)]   ],
                
            ]

            wnfh_mm_mid_buttons = [
                ["play"    ,"Начать историю"    ,[Hide("wnfh_menu", transition=dissolve), Jump("wnfh_prologue")]  ],
            ]

            

            wnfh_mm_links_buttons = [
                ["vk"      , "{image=wnfh_vk_icon}"        ,[Jump("technical_chocolatki")]                     ],
                ["steam"   , "{image=wnfh_steam_icon}"     ,[Jump("technical_chocolatki")]                     ],
                ["discord" , "{image=wnfh_discord_icon}"   ,[Jump("technical_chocolatki")]                     ],
            ]


            wnfh_main_menu_button = [
            
                 #Тег кнопки     #Изображение кнопки                               #Действие кнопки
                
                #["red"          ,im.Scale(wnfh_gui["poligon"]["red"], 100, 100)   ,[Jump("wnfh_test")]                                                      ],
                ["achievements" ,"Достижения"                                     ,[ShowMenu("wnfh_achievements", _transition=dissolve)]                    ],
                ["exit"         ,"Выход"                                          ,[Return()]                                                               ],
                ["dlc"          ,"DLC"                                            ,[Jump("technical_chocolatki")]                                           ],
            ]
       
            menu_hovered_action_cat = Play("sound", wnfh_SFX + "meow" + str(randrange(6)) + ".ogg")

        frame:
            background wnfh_gui["main_menu"]["mm_bg2"]
            area(0.0, 0.0, 1.0, 1.0)
            at wnfh_bg_spawn_atl
        frame:
            background wnfh_gui["main_menu"]["gradient"]
            area(0.0, 0.0, 1.0, 1.0)
            
            #frame:
            #    background background_color
            #    area(0.9, 0.9, 100, 40)
            #    xanchor 0.5 yanchor 0.5
            #    text wnfh_get_usertime():
            #        style "wnfh_menu"
            #        size 30
            
    

            frame: # ======================================================= # Сплэши
                background background_color
                area(0.65, 0.05, 0.45, 50)
                xanchor 0.5 yanchor 0.0
                text wnfh_splash():
                    style "wnfh_splashes"
                    at wnfh_splash_anim(0.5, 0.0, -3.0)
            
            frame: # ======================================================= # Выход
                background background_color
                area(0.0, 0.0, 200, 100)
                xanchor 0.0 yanchor 0.0
                for button in wnfh_main_menu_button[9:10]:
                    frame:
                        xmargin 5
                        background button_blue
                        area(0.0, 0.5, 1.0, 1.0)
                        xanchor 0.0 yanchor 0.5
                        textbutton button[1]:
                            background None
                            text_style "wnfh_choice_" + persistent.timeofday
                            action [button[2]]
                            hover_sound wnfh_gui["sound"]["plimp"]
                            at wnfh_mm_button_hover_atl()

            #if debag_switch:
            #    frame: # ======================================================= # Амогус
            #        background background_color
            #        area(0.0, 0.5, 100, 100)
            #        xanchor 0.0 yanchor 0.5
            #        frame:
            #            xmargin 5
            #            background button_blue
            #            area(0.5, 0.5, 1.0, 1.0)
            #            xanchor 0.5 yanchor 0.5
            #            imagebutton:
            #                action wnfh_main_menu_button[7][2]
            #                idle wnfh_main_menu_button[7][1]
            #                hover wnfh_main_menu_button[7][1]
            #                hover_sound wnfh_gui["sound"]["plimp"]
            #                at wnfh_mm_button_hover_atl()
                            
            frame: # ======================================================= # Нижняя панель
                background background_color
                area(0.5, 1.0, 1.0, 0.2)
                xanchor 0.5 yanchor 1.0
                
                frame: # ======================================================= # Левый блок
                    background background_color
                    area(0.0, 0.6, 0.42, 0.8)
                    xanchor 0.0 yanchor 0.5
                    grid 2 1:
                        xalign 1.0
                        for button in wnfh_mm_left_buttons[1:3]:
                            frame:
                                xmargin 5
                                background button_red
                                area(1.0, 0.0, 0.33, 0.5)
                                xanchor 1.0 yanchor 0.0
                                textbutton button[1]:
                                    background None
                                    text_style "wnfh_choice_" + persistent.timeofday
                                    action [button[2]]
                                    hover_sound wnfh_gui["sound"]["plimp"]
                                    at wnfh_mm_button_hover_atl()

                    frame:
                        xmargin 5
                        background button_red
                        area(1.0, 1.0, 0.33, 0.5)
                        xanchor 1.0 yanchor 1.0
                        textbutton wnfh_mm_left_buttons[0][1]:
                            background None
                            text_style "wnfh_choice_" + persistent.timeofday
                            action wnfh_mm_left_buttons[0][2]
                            hover_sound wnfh_gui["sound"]["plimp"]
                            at wnfh_mm_button_hover_atl()
                
                frame: # ======================================================= # Центральный блок
                    background background_color
                    area(0.5, 0.5, 250, 1.0)
                    xanchor 0.5 yanchor 0.5
                    yalign 0.5
                    frame:
                        xmargin 5
                        background button_red
                        area(0.5, 0.0, 1.0, 0.7)
                        xanchor 0.5 yanchor 0.0
                        textbutton wnfh_mm_mid_buttons[0][1]:
                            background None
                            text_style "wnfh_choice_" + persistent.timeofday
                            action wnfh_mm_mid_buttons[0][2]
                            hover_sound wnfh_gui["sound"]["plimp"]
                            at wnfh_mm_button_hover_atl()
                    frame:
                        background background_color
                        area(0.5, 1.0, 1.0, 0.3)
                        xanchor 0.5 yanchor 1.0
                        yalign 0.5
                        grid 3 1:
                            xalign 0.5
                            for button in wnfh_mm_links_buttons[0:3]:
                                frame:
                                    xmargin 5
                                    background button_blue
                                    area(0.5, 0.5, 0.33, 1.0)
                                    xanchor 0.5 yanchor 0.5
                                    textbutton button[1]:
                                        background None
                                        text_style "wnfh_choice_" + persistent.timeofday
                                        action [button[2]]
                                        hover_sound wnfh_gui["sound"]["plimp"]
                                        at wnfh_mm_button_hover_atl()


                
                frame: # ======================================================= # Правый блок
                    background background_color
                    area(1.0, 0.6, 0.42, 0.8)
                    xanchor 1.0 yanchor 0.5
                    
                    grid 2 1:
                        xalign 0.0
                        for button in wnfh_mm_right_buttons[1:3]:
                            frame:
                                xmargin 5
                                background button_red
                                area(0.0, 0.5, 0.33, 0.5)
                                xanchor 0.0 yanchor 0.5
                                textbutton button[1]:
                                    background None
                                    text_style "wnfh_choice_" + persistent.timeofday
                                    action [button[2]]
                                    hover_sound wnfh_gui["sound"]["plimp"]
                                    at wnfh_mm_button_hover_atl()
                    frame:
                        xmargin 5
                        background button_red
                        area(0.0, 1.0, 0.33, 0.5)
                        xanchor 0.0 yanchor 1.0
                        textbutton wnfh_mm_right_buttons[0][1]:
                            background None
                            text_style "wnfh_choice_" + persistent.timeofday
                            action wnfh_mm_right_buttons[0][2]
                            hover_sound wnfh_gui["sound"]["plimp"]
                            at wnfh_mm_button_hover_atl()
    #screen wnfh_news():
    #    frame:
    #        background wnfh_gui["main_menu"]["gradient2"] 
    #        area(0.0, 0.0, 1.0, 1.0)
    #    frame:
    #        background im.Alpha(im.Blur(wnfh_gui["main_menu"]["mm_bg"], 1.5), 0.1)
    #        area(0.0, 0.0, 1.0, 1.0)
    #    modal True
    #    
    #    #$ background_color = "#0000"
    #    #$ button_red =       "#0000"
    #    #$ button_green =     "#0000"
    #    #$ button_blue =      "#0000"
#
    #    $ background_color = "#0005"
    #    $ button_red =       "#F005"
    #    $ button_green =     "#0F05"
    #    $ button_blue =      "#00F5"
    #    
    #    frame:
    #        background background_color
    #        area(0.6, 0.58, 800, 800)
    #        xanchor 0.5 yanchor 0.5
    #        at frame_spawn()
    #            
    #        textbutton "X":
    #            action [Hide("wnfh_news", transition=Dissolve(1.0))]
    #            background button_red
    #            text_style "wnfh_title"
    #            text_size 80
    #            hover_sound wnfh_gui["sound"]["plimp"]
    #        
    #        frame:
    #            background background_color
    #            area(0.5, 0.0, 750, 100)
    #            xanchor 0.5
    #            text "Новости-хуёвости":
    #                style "wnfh_title"
    #                min_width 750
    #                text_align 0.5
    #        frame:
    #            background background_color
    #            area(0.5, 0.15, 750, 650)
    #            xanchor 0.5
    #            viewport id "menu_ach_list":
    #                draggable True
    #                mousewheel True
    #                scrollbars "vertical"
    #                grid 1 13:
    #                    text "Я заебался"
    #                    text "Я тоже"
    #                    text "АААААААААААААААААААААААА"
    #                    text "АААААААААААААААААААААААА"
    #                    text "АААААААААААААААААААААААА"
    #                    text "АААААААААААААААААААААААА"
    #                    text "АААААААААААААААААААААААА"
    #                    text "АААААААААААААААААААААААА"
    #                    text "АААААААААААААААААААААААА"
    #                    text "АААААААААААААААААААААААА"
    #                    text "АААААААААААААААААААААААА"
    #                    text "АААААААААААААААААААААААА"
    #                    text "АААААААААААААААААААААААА"
                    
                    
        
    


label wnfh_main:
    scene bg disclaimer_wnfh with dissolve
    $ renpy.pause(100)
    jump wnfh_main_menu
label wnfh_main_menu:
    scene cg d2_me_kat_boathouse_wnfh with dissolve
    $ renpy.pause(2)
    $ init_splash()
    #$ wnfh_Data = BD("./game/saves/wnfh_database.json")
    #$ wnfh_Data_test = BD("./game/saves/wnfh_database_test.json")
    call screen wnfh_menu with dissolve
init -1000:
    label null_ellement:
        $ wnfh_Data = wnfh_BD("./game/saves/wnfh_database.json")
        $ wnfh_Data_test = wnfh_BD("./game/saves/wnfh_database_test.json")
    
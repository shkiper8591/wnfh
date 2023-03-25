init 2:
    
    screen blwnfh_menu():
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
            
            blwnfh_menu_button = [
            
                 #Тег кнопки     #Текст кнопки
                ["credits"      , blwnfh_gui["main_menu"]["credits"]               ,[Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_day_1_dream")]   ],
                ["galary"       , blwnfh_gui["main_menu"]["galary"]                ,[Jump("technical_chocolatki")]                                           ],
                ["news"         , blwnfh_gui["main_menu"]["news"]                  ,[ShowMenu("blwnfh_achievements", _transition=dissolve)]                  ],
                ["play"         , blwnfh_gui["main_menu"]["play"]                  ,[Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_day_1_dream")]   ],
                ["saves"        , blwnfh_gui["main_menu"]["saves"]                 ,[Jump("technical_chocolatki")]                                           ],
                ["scheme"       , blwnfh_gui["main_menu"]["scheme"]                ,[Jump("technical_chocolatki")]                                           ],
                ["settings"     , blwnfh_gui["main_menu"]["settings"]              ,[Jump("technical_chocolatki")]                                           ],
                ["red"          , im.Scale(blwnfh_gui["poligon"]["red"], 100, 100) ,[Jump("blwnfh_test")]                                                    ],
                ["achievements" , blwnfh_gui["main_menu"]["achievements"]          ,[Jump("technical_chocolatki")]                                           ],
                ["exit"         , blwnfh_gui["main_menu"]["exit"]                  ,[Return()]                                                               ],
            ]
       
            menu_hovered_action_cat = Play("sound", blwnfh_SFX + "meow" + str(randrange(6)) + ".ogg")
        
        $ background_color = "#0000"
        $ button_red =       "#0000"
        $ button_green =     "#0000"
        $ button_blue =      "#0000"

        #$ background_color = "#0005"
        #$ button_red =       "#F005"
        #$ button_green =     "#0F05"
        #$ button_blue =      "#00F5"
        
        
        frame:
            background blwnfh_gui["main_menu"]["fon2"]
            area(0.0, 0.0, 1.0, 1.0)
            at blwnfh_bg_spawn_atl
        frame:
            background blwnfh_gui["main_menu"]["gradient"]
            area(0.0, 0.0, 1.0, 1.0)
            
            #frame:
            #    background background_color
            #    area(0.9, 0.9, 100, 40)
            #    xanchor 0.5 yanchor 0.5
            #    text blwnfh_get_usertime():
            #        style "blwnfh_menu"
            #        size 30
            
            frame: # ======================================================= # Выход
                background background_color
                area(0.65, 0.05, 0.45, 50)
                xanchor 0.5 yanchor 0.0
                text blwnfh_splash():
                    style "blwnfh_splashes"
                    at blwnfh_splash_anim(0.5, 0.0, -3.0)
            
            frame: # ======================================================= # Выход
                background background_color
                area(0.0, 0.0, 200, 100)
                xanchor 0.0 yanchor 0.0
                for button in blwnfh_menu_button[9:10]:
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
            #frame: # ======================================================= # Амогус
            #    background background_color
            #    area(0.0, 0.5, 100, 100)
            #    xanchor 0.0 yanchor 0.5
            #    for button in blwnfh_menu_button[7:8]:
            #        frame:
            #            xmargin 5
            #            background button_blue
            #            area(0.5, 0.5, 1.0, 1.0)
            #            xanchor 0.5 yanchor 0.5
            #            imagebutton:
            #                action [button[2]]
            #                idle button[1]
            #                hover button[1]
            #                hover_sound blwnfh_gui["sound"]["plimp"]
            #                at blwnfh_mm_button_hover_atl()
                            
            frame: # ======================================================= # Нижняя панелья
                background background_color
                area(0.5, 1.0, 1.0, 0.2)
                xanchor 0.5 yanchor 1.0
                
                frame: # ======================================================= # Левый блок
                    background background_color
                    area(0.0, 0.4, 0.42, 0.4)
                    xanchor 0.0 yanchor 0.5
                    
                    grid 3 1:
                        xalign 0.5
                        for button in blwnfh_menu_button[0:3]:
                            frame:
                                xmargin 5
                                background button_red
                                area(0.5, 0.5, 0.33, 1.0)
                                xanchor 0.5 yanchor 0.5
                                imagebutton:
                                    action [button[2]]
                                    idle button[1]
                                    hover button[1]
                                    hover_sound blwnfh_gui["sound"]["plimp"]
                                    at blwnfh_mm_button_hover_atl()
                
                frame: # ======================================================= # Центральный блок
                    background background_color
                    area(0.5, 0.4, 250, 0.7)
                    xanchor 0.5 yanchor 0.5
                    yalign 0.5
                    for button in blwnfh_menu_button[3:4]:
                        frame:
                            xmargin 5
                            background button_red
                            area(0.5, 0.5, 1.0, 1.0)
                            xanchor 0.5 yanchor 0.5
                            imagebutton:
                                action [button[2]]
                                idle button[1]
                                hover button[1]
                                hover_sound blwnfh_gui["sound"]["plimp"]
                                at blwnfh_mm_button_hover_atl()
                                
                frame: # ======================================================= # Центральный нижний блок
                    background background_color
                    area(0.5, 1.0, 250, 0.3)
                    xanchor 0.5 yanchor 1.0
                    for button in blwnfh_menu_button[8:9]:
                        frame:
                            xmargin 5
                            background button_red
                            area(0.5, 0.5, 1.0, 1.0)
                            xanchor 0.5 yanchor 0.5
                            imagebutton:
                                action [button[2]]
                                idle button[1]
                                hover button[1]
                                hover_sound blwnfh_gui["sound"]["plimp"]
                                at blwnfh_mm_button_hover_atl()
                
                frame: # ======================================================= # Правый блок
                    background background_color
                    area(1.0, 0.4, 0.42, 0.4)
                    xanchor 1.0 yanchor 0.5
                    
                    grid 3 1:
                        xalign 0.5
                        for button in blwnfh_menu_button[4:7]:
                            frame:
                                xmargin 5
                                background button_red
                                area(0.5, 0.5, 0.33, 1.0)
                                xanchor 0.5 yanchor 0.5
                                imagebutton:
                                    action [button[2]]
                                    idle button[1]
                                    hover button[1]
                                    hover_sound blwnfh_gui["sound"]["plimp"]
                                    at blwnfh_mm_button_hover_atl()

    screen blwnfh_news():
        frame:
            background blwnfh_gui["main_menu"]["gradient2"] 
            area(0.0, 0.0, 1.0, 1.0)
        frame:
            background im.Alpha(im.Blur(blwnfh_gui["main_menu"]["fon"], 1.5), 0.1)
            area(0.0, 0.0, 1.0, 1.0)
        modal True
        
        #$ background_color = "#0000"
        #$ button_red =       "#0000"
        #$ button_green =     "#0000"
        #$ button_blue =      "#0000"

        $ background_color = "#0005"
        $ button_red =       "#F005"
        $ button_green =     "#0F05"
        $ button_blue =      "#00F5"
        
        frame:
            background background_color
            area(0.6, 0.58, 800, 800)
            xanchor 0.5 yanchor 0.5
            at frame_spawn()
                
            textbutton "X":
                action [Hide("blwnfh_news", transition=Dissolve(1.0))]
                background button_red
                text_style "blwnfh_title"
                text_size 80
                hover_sound blwnfh_gui["sound"]["plimp"]
            
            frame:
                background background_color
                area(0.5, 0.0, 750, 100)
                xanchor 0.5
                text "Новости-хуёвости":
                    style "blwnfh_title"
                    min_width 750
                    text_align 0.5
            frame:
                background background_color
                area(0.5, 0.15, 750, 650)
                xanchor 0.5
                viewport id "menu_ach_list":
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    grid 1 13:
                        text "Я заебался"
                        text "Я тоже"
                        text "АААААААААААААААААААААААА"
                        text "АААААААААААААААААААААААА"
                        text "АААААААААААААААААААААААА"
                        text "АААААААААААААААААААААААА"
                        text "АААААААААААААААААААААААА"
                        text "АААААААААААААААААААААААА"
                        text "АААААААААААААААААААААААА"
                        text "АААААААААААААААААААААААА"
                        text "АААААААААААААААААААААААА"
                        text "АААААААААААААААААААААААА"
                        text "АААААААААААААААААААААААА"
                    
                    
        
    transform blwnfh_bg_spawn_atl():
        subpixel True
        truecenter
        on show:
            alpha 0.0
            ease 4.0 alpha 1.0

    transform blwnfh_news_spawn_atl():
        zoom 0.0
        ease 0.5 zoom 1.2
        ease 0.2 zoom 1.0

    transform blwnfh_mm_button_hover_atl(z = 1.0):
        pos(0.5, 0.5)
        anchor(0.5, 0.5)
        on hover:
            ease 0.15 zoom (z - 0.15)
            ease 0.15 zoom (z - 0.02)
        on idle:
            ease 0.15 zoom z
            
    transform blwnfh_splash_anim(x, y, rot):
        block:
            rotate rot
            pos(x, y)
            anchor(0.5, 0.5)
        block:
            ease 0.25 zoom 1.30
            ease 0.20 zoom 1.25
        repeat
    
    
    
    ## Временное говно ##
    transform blwnfh_menu_pos_atl(z, x, y, rot):
        zoom z
        pos(x, y)
        anchor(0.5, 0.5)
        rotate rot
        blwnfh_menu_hover_atl(z, rot)
        
    transform blwnfh_menu_hover_atl(z, rot):
        on hover:
            ease 0.1 zoom (z - 0.15) rotate 0.0
            ease 0.1 zoom (z - 0.02)
        on idle:
            ease 0.1 zoom z rotate rot


label blwnfh_main:
    scene bg disclaimer with dissolve
    $ renpy.pause(100)
    jump blwnfh_main_menu
label blwnfh_main_menu:
    scene cg d2_me_kat_boathouse with dissolve
    $ renpy.pause(2)
    $ init_splash()
    call screen blwnfh_menu with dissolve
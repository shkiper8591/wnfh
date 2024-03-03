init 2:
    
    screen wnfh_main_menu():
        modal True tag menu

        python:
            from random import randrange

            def menu_img_status(imgf, condition="hover"):
                if condition == "hover":
                    return im.MatrixColor(imgf, im.matrix.contrast(1.7))
                if condition == "insensitive":
                    return im.Alpha(imgf, 0.38)
            
            wnfh_mm_left_buttons = [
                ["galary"  ,"Галерея"   ,[Jump("technical_chocolatki")]                        ],
                ["scheme"  ,"Схема"     ,[ShowMenu("wnfh_schematic", _transition=dissolve)]    ],
                ["exit"    ,"Выход"     ,[Start("wnfh_exit")]                                  ],
            ]
            wnfh_mm_right_buttons = [
                ["saves"        ,"Загрузить"  ,[ShowMenu("wnfh_load", _transition=dissolve)]   ],
                ["preferences"  ,"Настройки"  ,[ShowMenu("wnfh_preferences", _transition=dissolve)]   ],
            ]

            wnfh_mm_mid_buttons = [
                ["play"    ,"Начать историю"    ,[Hide("wnfh_menu", transition=dissolve), Start("wnfh_prologue")]  ],
            ]
            
            wnfh_mm_down_buttons = [
                ["vk", im.Scale(im.Composite(
                    (130, 130),
                    (6, 6), im.MatrixColor(wnfh_gui["main_menu"]["vk"], im.matrix.tint(0.0, 0.0, 0.0,)),
                    (0, 0), im.MatrixColor(wnfh_gui["main_menu"]["vk"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color',0,persistent.timeofday)))
                    ), 60, 60),
                [OpenURL("https://vk.com/blwnfh")]],

                ["steam", im.Scale(im.Composite(
                    (130, 130),
                    (6, 6), im.MatrixColor(wnfh_gui["main_menu"]["steam"], im.matrix.tint(0.0, 0.0, 0.0,)),
                    (0, 0), im.MatrixColor(wnfh_gui["main_menu"]["steam"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color',0,persistent.timeofday)))
                    ), 60, 60),
                [OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=2986236115")]],

                ["discord", im.Scale(im.Composite(
                    (130, 130),
                    (6, 6), im.MatrixColor(wnfh_gui["main_menu"]["discord"], im.matrix.tint(0.0, 0.0, 0.0,)),
                    (0, 0), im.MatrixColor(wnfh_gui["main_menu"]["discord"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color',0,persistent.timeofday)))
                    ), 60, 60),
                [OpenURL("https://discord.gg/KfaK7pmRSK")]],

                ["achievements", im.Scale(im.Composite(
                    (130, 130),
                    (6, 6), im.MatrixColor(wnfh_gui["main_menu"]["achievements"], im.matrix.tint(0.0, 0.0, 0.0,)),
                    (0, 0), im.MatrixColor(wnfh_gui["main_menu"]["achievements"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color',0,persistent.timeofday)))
                    ), 60, 60), 
                [ShowMenu("wnfh_achievements", _transition=dissolve)]],

                ["seledka", im.Scale(im.Composite(
                    (130, 130),
                    (6, 6), im.MatrixColor(wnfh_gui["main_menu"]["seledka"], im.matrix.tint(0.0, 0.0, 0.0,)),
                    (0, 0), im.MatrixColor(wnfh_gui["main_menu"]["seledka"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color',0,persistent.timeofday)))
                    ), 60, 60),
                [Jump("technical_chocolatki")]],
            ]
            wnfh_main_menu_button = [
            
                 #Тег кнопки     #Изображение кнопки                               #Действие кнопки
                
                ["red", im.Scale(wnfh_gui["poligon"]["red"], 100, 100), [Start("wnfh_test")]],
                
            ]
       
            menu_hovered_action_cat = Play("sound", wnfh_SFX + "meow" + str(randrange(6)) + ".ogg")

        frame:
            background wnfh_gui["main_menu"]["mm_bg2"]
            area(0.0, 0.0, 1.0, 1.0)
            at wnfh_bg_spawn_atl
        frame:
            background wnfh_gui["main_menu"]["gradient"]
            area(0.0, 0.0, 1.0, 1.0)
            
            #frame: # ======================================================= # Часики
            #    background background_color
            #    area(0.5, 0.03, 120, 40)
            #    xanchor 0.5 yanchor 0.5
            #    text wnfh_get_usertime():
            #        xalign 0.5
            #        style "wnfh_choice_" + persistent.timeofday
            #        size 30
            
    

            frame: # ======================================================= # Сплэши
                if persistent.wnfh_debug_color:
                    background frame_black
                else:
                    background frame_transparent
                area(0.65, 0.05, 0.45, 50)
                xanchor 0.5 yanchor 0.0
                text init_splash():
                    style "wnfh_splashes"
                    at wnfh_splash_anim(0.5, 0.0, -3.0)
            if debag_switch:
                frame: # ======================================================= # Амогус
                    if persistent.wnfh_debug_color:
                        background frame_black
                    else:
                        background frame_transparent
                    area(0.0, 0.5, 100, 100)
                    xanchor 0.0 yanchor 0.5
                    frame:
                        xmargin 5
                        if persistent.wnfh_debug_color:
                            background frame_blue
                        else:
                            background frame_transparent
                        area(0.5, 0.5, 1.0, 1.0)
                        xanchor 0.5 yanchor 0.5
                        imagebutton:
                            action wnfh_main_menu_button[0][2]
                            idle wnfh_main_menu_button[0][1]
                            hover wnfh_main_menu_button[0][1]
                            hover_sound wnfh_gui["sound"]["plimp"]
                            at wnfh_mm_button_hover_atl()
                            
            frame: # ======================================================= # Нижняя панель
                if persistent.wnfh_debug_color:
                    background frame_black
                else:
                    background frame_transparent
                area(0.5, 1.0, 1.0, 0.2)
                xanchor 0.5 yanchor 1.0
                
                frame: # ======================================================= # Левый блок
                    if persistent.wnfh_debug_color:
                        background frame_black
                    else:
                        background frame_transparent
                    area(0.0, 0.4, 0.42, 0.4)
                    xanchor 0.0 yanchor 0.5
                    grid 2 1:
                        xalign 1.0
                        for button in wnfh_mm_left_buttons[0:2]:
                            frame:
                                xmargin 5
                                if persistent.wnfh_debug_color:
                                    background frame_red
                                else:
                                    background frame_transparent
                                area(0.5, 0.5, 0.33, 1.0)
                                xanchor 0.5 yanchor 0.5
                                textbutton button[1]:
                                    background None
                                    text_style "wnfh_choice_" + persistent.timeofday
                                    action [button[2]]
                                    hover_sound wnfh_gui["sound"]["plimp"]
                                    at wnfh_mm_button_hover_atl()
                frame:
                    if persistent.wnfh_debug_color:
                        background frame_black
                    else:
                        background frame_transparent
                    area(0.0, 1.0, 0.1, 0.3)
                    xanchor 0.0 yanchor 1.0
                    yalign 0.5
                    frame:
                        xmargin 5
                        if persistent.wnfh_debug_color:
                            background frame_red
                        else:
                            background frame_transparent
                        area(0.5, 0.5, 0.5, 1.0)
                        xanchor 0.5 yanchor 0.5
                        textbutton wnfh_mm_left_buttons[2][1]:
                            background None
                            text_style "wnfh_choice_" + persistent.timeofday
                            action wnfh_mm_left_buttons[2][2]
                            hover_sound wnfh_gui["sound"]["plimp"]
                            at wnfh_mm_button_hover_atl()
                
                frame: # ======================================================= # Центральный блок
                    if persistent.wnfh_debug_color:
                        background frame_black
                    else:
                        background frame_transparent
                    area(0.5, 0.5, 250, 1.0)
                    xanchor 0.5 yanchor 0.5
                    yalign 0.5
                    frame:
                        xmargin 5
                        if persistent.wnfh_debug_color:
                            background frame_red
                        else:
                            background frame_transparent
                        area(0.5, 0.0, 1.0, 0.7)
                        xanchor 0.5 yanchor 0.0
                        textbutton wnfh_mm_mid_buttons[0][1]:
                            background None
                            text_style "wnfh_choice_" + persistent.timeofday
                            action wnfh_mm_mid_buttons[0][2]
                            hover_sound wnfh_gui["sound"]["plimp"]
                            at wnfh_mm_button_hover_atl()
                    frame:
                        if persistent.wnfh_debug_color:
                            background frame_black
                        else:
                            background frame_transparent
                        area(0.5, 1.0, 1.0, 0.3)
                        xanchor 0.5 yanchor 1.0
                        yalign 0.5
                        grid 2 1:
                            xalign 0.5
                            for button in wnfh_mm_down_buttons[3:5]:
                                frame:
                                    xmargin 5
                                    if persistent.wnfh_debug_color:
                                        background frame_red
                                    else:
                                        background frame_transparent
                                    area(0.5, 0.5, 0.5, 1.0)
                                    xanchor 0.5 yanchor 0.5
                                    imagebutton:
                                        idle button[1]
                                        hover button[1]
                                        action button[2]
                                        hover_sound wnfh_gui["sound"]["plimp"]
                                        at wnfh_mm_button_hover_atl()

                
                
                frame: # ======================================================= # Правый блок
                    if persistent.wnfh_debug_color:
                        background frame_black
                    else:
                        background frame_transparent
                    area(1.0, 0.4, 0.42, 0.4)
                    xanchor 1.0 yanchor 0.5
                    
                    grid 2 1:
                        xalign 0.0
                        for button in wnfh_mm_right_buttons[0:2]:
                            frame:
                                xmargin 5
                                if persistent.wnfh_debug_color:
                                    background frame_red
                                else:
                                    background frame_transparent
                                area(0.5, 0.5, 0.33, 1.0)
                                xanchor 0.5 yanchor 0.5
                                textbutton button[1]:
                                    background None
                                    text_style "wnfh_choice_" + persistent.timeofday
                                    action [button[2]]
                                    hover_sound wnfh_gui["sound"]["plimp"]
                                    at wnfh_mm_button_hover_atl()
                frame:
                    if persistent.wnfh_debug_color:
                        background frame_black
                    else:
                        background frame_transparent
                    area(1.0, 1.0, 0.17, 0.3)
                    xanchor 1.0 yanchor 1.0
                    yalign 0.5
                    grid 3 1:
                        xalign 0.5
                        for button in wnfh_mm_down_buttons[0:3]:
                            frame:
                                xmargin 5
                                if persistent.wnfh_debug_color:
                                    background frame_red
                                else:
                                    background frame_transparent
                                area(0.5, 0.5, 0.33, 1.0)
                                xanchor 0.5 yanchor 0.5
                                imagebutton:
                                    idle button[1]
                                    hover button[1]
                                    action button[2]
                                    hover_sound wnfh_gui["sound"]["plimp"]
                                    at wnfh_mm_button_hover_atl()

label wnfh_main:
    window hide
    stop music fadeout 3 # Останавливаем музыку.
    scene bg black with fade2 # Переходим на сцену с чёрным экраном.
    $ wnfh_screens_save_act() # Сохраняем экраны из оригинала и заменяем на собственные.
    return # С помощью return попадаем в главное меню игры.
    #scene cg d8_me_kat_boathouse_wnfh with dissolve
    $ renpy.pause(2)
    $ init_splash()


label wnfh_exit:
    window hide # Скрываем текстбокс.
    stop music fadeout 3 # Останавливаем музыку.
    scene black with fade # Переходим на сцену с чёрным экраном.
    $ wnfh_screens_diact() # Делаем обратную замену экранов мода на оригинальные.
    $ MainMenu(confirm=False)() # Выходим в главное меню.

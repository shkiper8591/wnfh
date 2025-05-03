screen wnfh_main_menu():
    modal True tag menu
    $ debug_frame = {
        "black":  frame_black  if persistent.wnfh_debug_color else frame_transparent,
        "red":    frame_red    if persistent.wnfh_debug_color else frame_transparent,
        "green":  frame_green  if persistent.wnfh_debug_color else frame_transparent,
        "blue":   frame_blue   if persistent.wnfh_debug_color else frame_transparent,
        "purple": frame_purpl  if persistent.wnfh_debug_color else frame_transparent
    }
    python:
        #from random import randrange

        def menu_img_status(imgf, condition="hover"):
            if condition == "hover":
                return im.MatrixColor(imgf, im.matrix.contrast(1.7))
            if condition == "insensitive":
                return im.Alpha(imgf, 0.38)
        

        wnfh_mm_left_buttons = [
            ["galary"  ,"Галерея"   ,[Jump("technical_chocolatki")]                        ],
            ["scheme"  ,"Схема"     ,[ShowMenu("wnfh_schematic", _transition=dissolve)]    ],
            ["exit"    ,"Выход в БЛ"     ,[Start("wnfh_exit")]                                  ],
        ]

        wnfh_mm_right_buttons = [
            ["saves"        ,"Загрузить"  ,[ShowMenu("load", main_menu = True), Hide('main_menu')]   ],
            ["preferences"  ,"Настройки"  ,[ShowMenu("preferences", main_menu = True), Hide('main_menu')]   ],
        ]

        wnfh_mm_mid_buttons = [
            ["play"    ,"Начать историю"    ,[Hide("main_menu", transition=dissolve), Start("wnfh_prologue")]  ],
        ]
        
        wnfh_mm_down_buttons = [
            ["vk", im.Scale(im.Composite(
                (130, 130),
                (6, 6), im.MatrixColor(wnfh_gui["main_menu"]["vk"], im.matrix.tint(0.0, 0.0, 0.0,)),
                (0, 0), im.MatrixColor(wnfh_gui["main_menu"]["vk"], im.matrix.tint(*converter_hex('wnfh_tint_color', 0, renpy.store.wnfh_tymeofday)))
                ), 60, 60),
            [OpenURL("https://vk.com/blwnfh")]],

            ["telegramm", im.Scale(im.Composite(
                (130, 130),
                (6, 6), im.MatrixColor(wnfh_gui["main_menu"]["telegramm"], im.matrix.tint(0.0, 0.0, 0.0,)),
                (0, 0), im.MatrixColor(wnfh_gui["main_menu"]["telegramm"], im.matrix.tint(*converter_hex('wnfh_tint_color', 0, renpy.store.wnfh_tymeofday)))
                ), 60, 60),
            [OpenURL("https://t.me/blwnfh")]],

            ["steam", im.Scale(im.Composite(
                (130, 130),
                (6, 6), im.MatrixColor(wnfh_gui["main_menu"]["steam"], im.matrix.tint(0.0, 0.0, 0.0,)),
                (0, 0), im.MatrixColor(wnfh_gui["main_menu"]["steam"], im.matrix.tint(*converter_hex('wnfh_tint_color', 0, renpy.store.wnfh_tymeofday)))
                ), 60, 60),
            [OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=2986236115")]],

            ["discord", im.Scale(im.Composite(
                (130, 130),
                (6, 6), im.MatrixColor(wnfh_gui["main_menu"]["discord"], im.matrix.tint(0.0, 0.0, 0.0,)),
                (0, 0), im.MatrixColor(wnfh_gui["main_menu"]["discord"], im.matrix.tint(*converter_hex('wnfh_tint_color', 0, renpy.store.wnfh_tymeofday)))
                ), 60, 60),
            [OpenURL("https://discord.gg/KfaK7pmRSK")]],

            ["achievements", im.Scale(im.Composite(
                (130, 130),
                (6, 6), im.MatrixColor(wnfh_gui["main_menu"]["achievements"], im.matrix.tint(0.0, 0.0, 0.0,)),
                (0, 0), im.MatrixColor(wnfh_gui["main_menu"]["achievements"], im.matrix.tint(*converter_hex('wnfh_tint_color', 0, renpy.store.wnfh_tymeofday)))
                ), 60, 60), 
            [ShowMenu("wnfh_achievements", _transition=dissolve)]],

            ["seledka", im.Scale(im.Composite(
                (130, 130),
                (6, 6), im.MatrixColor(wnfh_gui["main_menu"]["seledka"], im.matrix.tint(0.0, 0.0, 0.0,)),
                (0, 0), im.MatrixColor(wnfh_gui["main_menu"]["seledka"], im.matrix.tint(*converter_hex('wnfh_tint_color', 0, renpy.store.wnfh_tymeofday)))
                ), 60, 60),
            [Jump("technical_chocolatki")]],
        ]
        wnfh_main_menu_button = [
        
             #Тег кнопки     #Изображение кнопки                               #Действие кнопки
            
            ["red", im.Scale(wnfh_gui["poligon"]["red"], 100, 100), [Start("wnfh_test")]],
            
        ]

        mm_backgrounds = {
            "night":  wnfh_gui["main_menu"]["mm_bg_night"],
            "sunset": wnfh_gui["main_menu"]["mm_bg_sunset"],
            "day":    wnfh_gui["main_menu"]["mm_bg_day"],
        }
   
        #menu_hovered_action_cat = Play("sound", wnfh_SFX + "meow" + str(randrange(6)) + ".ogg")
    
    default current_hour = wnfh_get_usertime("hour") # ======================= Главное меню подстраивается под время суток компьютера
    
    default time_period = (
        "night"  if (current_hour >= 22 or current_hour < 8) else
        "sunset" if (current_hour < 12)                      else
        "day"    if (current_hour < 19)                      else
        "sunset"
    )
    $ renpy.store.wnfh_tymeofday = time_period

    default splash = random.choice(wnfh_splashes) # =============== Для сплешей

    frame:
        background mm_backgrounds[time_period] # ================== Фон в главном меню
        area(0.0, 0.0, 1.0, 1.0)
        frame: # ======================================================= # Сплэши
            background debug_frame["black"]
            area(0.65, 0.05, 0.45, 50)
            xanchor 0.5 yanchor 0.0
            text splash:
                style "wnfh_text_" + time_period
                size 20
                at wnfh_splash_anim(0.5, 0.0, -3.0)

        if debug_switch:
            frame: # ======================================================= # Амогус
                background debug_frame["black"]
                area(0.0, 0.5, 100, 100)
                xanchor 0.0 yanchor 0.5
                frame:
                    xmargin 5
                    background debug_frame["blue"]
                    area(0.5, 0.5, 1.0, 1.0)
                    xanchor 0.5 yanchor 0.5
                    imagebutton:
                        action wnfh_main_menu_button[0][2]
                        idle wnfh_main_menu_button[0][1]
                        hover wnfh_main_menu_button[0][1]
                        hover_sound wnfh_gui["sound"]["plimp"]
                        at wnfh_mm_button_hover_atl()
                        
        frame: # ======================================================= # Нижняя панель
            background debug_frame["black"]
            area(0.5, 1.0, 1.0, 0.2)
            xanchor 0.5 yanchor 1.0
            
            frame: # ======================================================= # Левый блок
                background debug_frame["black"]
                area(0.0, 0.4, 0.42, 0.4)
                xanchor 0.0 yanchor 0.5
                grid 2 1:
                    xalign 1.0
                    for button in wnfh_mm_left_buttons[0:2]:
                        frame:
                            xmargin 5
                            background debug_frame["red"]
                            area(0.5, 0.5, 0.33, 1.0)
                            xanchor 0.5 yanchor 0.5
                            textbutton button[1]:
                                style "wnfh_buttons"
                                text_style "wnfh_text_" + time_period
                                action [button[2]]
                                at wnfh_mm_button_hover_atl()

            frame:
                background debug_frame["black"]
                area(0.0, 1.0, 0.15, 0.3)
                xanchor 0.0 yanchor 1.0
                yalign 0.5
                frame:
                    xmargin 5
                    background debug_frame["red"]
                    area(0.5, 0.5, 1.0, 1.0)
                    xanchor 0.5 yanchor 0.5
                    textbutton wnfh_mm_left_buttons[2][1]:
                        style "wnfh_buttons"
                        text_style "wnfh_text_" + time_period
                        action wnfh_mm_left_buttons[2][2]
                        at wnfh_mm_button_hover_atl()
            
            frame: # ======================================================= # Центральный блок
                background debug_frame["black"]
                area(0.5, 0.5, 250, 1.0)
                xanchor 0.5 yanchor 0.5
                yalign 0.5
                frame:
                    xmargin 5
                    background debug_frame["red"]
                    area(0.5, 0.0, 1.0, 0.7)
                    xanchor 0.5 yanchor 0.0
                    textbutton wnfh_mm_mid_buttons[0][1]:
                        style "wnfh_buttons"
                        text_style "wnfh_text_" + time_period
                        action wnfh_mm_mid_buttons[0][2]
                        at wnfh_mm_button_hover_atl()

                frame:
                    background debug_frame["black"]
                    area(0.5, 1.0, 1.0, 0.3)
                    xanchor 0.5 yanchor 1.0
                    yalign 0.5
                    grid 2 1:
                        xalign 0.5
                        for button in wnfh_mm_down_buttons[4:6]:
                            frame:
                                xmargin 5
                                background debug_frame["red"]
                                area(0.5, 0.5, 0.5, 1.0)
                                xanchor 0.5 yanchor 0.5
                                imagebutton:
                                    idle button[1]
                                    hover button[1]
                                    action button[2]
                                    hover_sound wnfh_gui["sound"]["plimp"]
                                    at wnfh_mm_button_hover_atl()
            
            
            frame: # ======================================================= # Правый блок
                background debug_frame["black"]
                area(1.0, 0.4, 0.42, 0.4)
                xanchor 1.0 yanchor 0.5
                
                grid 2 1:
                    xalign 0.0
                    for button in wnfh_mm_right_buttons[0:2]:
                        frame:
                            xmargin 5
                            background debug_frame["red"]
                            area(0.5, 0.5, 0.33, 1.0)
                            xanchor 0.5 yanchor 0.5
                            textbutton button[1]:
                                style "wnfh_buttons"
                                text_style "wnfh_text_" + time_period
                                action [button[2]]
                                at wnfh_mm_button_hover_atl()

            frame:
                background debug_frame["black"]
                area(1.0, 1.0, 440, 0.3)
                xanchor 1.0 yanchor 1.0
                yalign 0.5
                grid 4 1:
                    xalign 0.5
                    for button in wnfh_mm_down_buttons[0:4]:
                        frame:
                            xmargin 5
                            background debug_frame["red"]
                            area(0.5, 0.5, 0.25, 1.0)
                            xanchor 0.5 yanchor 0.5
                            imagebutton:
                                idle button[1]
                                hover button[1]
                                action button[2]
                                hover_sound wnfh_gui["sound"]["plimp"]
                                at wnfh_mm_button_hover_atl()

label wnfh_main:
    window hide
    stop ambience fadeout 3
    stop sound fadeout 3
    stop sound_loop fadeout 3
    stop music fadeout 3 # Останавливаем музыку.
    scene bg black with fade2 # Переходим на сцену с чёрным экраном.
    $ wnfh_screens_save_act() # Сохраняем экраны из оригинала и заменяем на собственные.
    return # С помощью return попадаем в главное меню игры.
    #scene cg d8_me_kat_boathouse_wnfh with dissolve
    $ renpy.pause(2)


label wnfh_exit:
    window hide # Скрываем текстбокс.
    stop music fadeout 3 # Останавливаем музыку.
    scene black with fade # Переходим на сцену с чёрным экраном.
    $ wnfh_screens_diact() # Делаем обратную замену экранов мода на оригинальные.
    $ MainMenu(confirm=False)() # Выходим в главное меню.

init 1000 python:
    if debag_switch:
        config.developer = True
init -5:
    $ global frame_transparent
    $ global frame_black
    $ global frame_red
    $ global frame_green
    $ global frame_blue
    $ global frame_purpl

    $ global debag_switch

    $ frame_transparent = "#0000"
    $ frame_black       = "#0005"
    $ frame_red         = "#F005"
    $ frame_green       = "#0F05"
    $ frame_blue        = "#00F5"
    $ frame_purpl       = "#F0F5"

    $ debag_switch = 1 

    if persistent.wnfh_mat_filter == None:
        $ persistent.wnfh_mat_filter = 0

    if persistent.wnfh_hentai_mod == None:
        $ persistent.wnfh_hentai_mod = 0

    if persistent.wnfh_widget_lp == None:
        $ persistent.wnfh_widget_lp = 0

    if persistent.wnfh_debug_color == None:
        $ persistent.wnfh_debug_color = 0
    

init 2:
    screen wnfh_preferences():

        modal True tag menu

        default wnfh_screen_1 = False
        default wnfh_screen_2 = False
        default wnfh_screen_3 = False
        default wnfh_screen_4 = False

        default wnfh_preferences_1 = False
        default wnfh_preferences_2 = False
        default wnfh_preferences_3 = False
                
        python:

            wnfh_screen_variable = [
                wnfh_screen_1,
                wnfh_screen_2,
                wnfh_screen_3,
                wnfh_screen_4,
            ]
            wnfh_screen_variable_string = list('wnfh_screen_' + str(i) for i in range(1, 5))

            wnfh_preferences_variable = [
                wnfh_preferences_1,
                wnfh_preferences_2,
                wnfh_preferences_3,
            ]
            wnfh_preferences_variable_string = list('wnfh_preferences_' + str(i) for i in range(1, 4))

            def menu_img_status(imgf, condition="hover"):
                if condition == "hover":
                    return im.MatrixColor(imgf, im.matrix.contrast(1.7))
                if condition == "insensitive":
                    return im.Alpha(imgf, 0.38)

            wnfh_underwrites = {
                "skip": [_preferences.skip_unseen, "Прочитанное", "Всё"],
                "font": [persistent.font_size == "large", "Обычный", "Жирный"]
            }

            wnfh_bars = {
                "htumb": [im.MatrixColor(wnfh_gui["tint_elements"]["bar_htumb"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday)))],
                
                "bar_full": [im.Composite(
                    (473, 37),
                    (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["bar_full"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 0, persistent.timeofday))),
                    (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["bar_null"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                    )],

                "bar_null": [im.Composite(
                    (473, 37),
                    (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["bar_bg"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
                    (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["bar_null"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                    )],

                "button_bar_full": [im.Composite(
                    (145, 35),
                    (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_bar_full"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 0, persistent.timeofday))),
                    (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_bar_null"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                    )],

                "button_bar_null": [im.Composite(
                    (145, 35),
                    (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_bar_bg"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
                    (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["button_bar_null"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                    )],

                "multibutton_bar_full": [im.Composite(
                    (248, 35),
                    (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["multibutton_bar_full"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 0, persistent.timeofday))),
                    (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["multibutton_bar_null"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                    )],

                "multibutton_bar_null": [im.Composite(
                    (248, 35),
                    (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["multibutton_bar_bg"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
                    (0, 0), im.MatrixColor(wnfh_gui["tint_elements"]["multibutton_bar_null"], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
                    )],
            }

            wnfh_preferences_button = [
                ["Интерфейс"             ,[ToggleScreenVariable(wnfh_preferences_variable_string[0], True), ToggleScreenVariable(wnfh_preferences_variable_string[1], False), ToggleScreenVariable(wnfh_preferences_variable_string[2], False)]],
                ["Аудио"                 ,[ToggleScreenVariable(wnfh_preferences_variable_string[1], True), ToggleScreenVariable(wnfh_preferences_variable_string[0], False), ToggleScreenVariable(wnfh_preferences_variable_string[2], False)]],
                ["Для разработчиков"     ,[ToggleScreenVariable(wnfh_preferences_variable_string[2], True), ToggleScreenVariable(wnfh_preferences_variable_string[1], False), ToggleScreenVariable(wnfh_preferences_variable_string[0], False)]],
                ["Назад"                 ,[Return()]   ],
     
            ]
            wnfh_preferences_bar = [
                
                 #Тег бара           #Название бара                       #Действие
                ["music"            ,"Музыка"              ,Preference("music volume")       ],
                ["sound"            ,"Звуки"               ,Preference("sound volume")       ],
                ["ambience"         ,"Эмбиент"             ,Preference("voice volume")       ],
                ["text_speed"       ,"Скорость текста"     ,Preference("text speed")         ],
                ["autoforward_time" ,"Время автопереходов" ,Preference("auto-forward time")  ],
            ]
            wnfh_preferences_switch = [
                 #Тег переключалки   #Текст кнопки        #Вкл.                                                                                                             #Выкл.
                #["fullscreen"       ,"Полный экран"               ,[Preference("display", "fullscreen"),              Play("sound", wnfh_sfx_list["plimp2"])]           ,  Preference("display", "window")                                                              , _preferences.fullscreen         ],
                #["autoforward"      ,"Автопереход"                ,[Preference("auto-forward after click", "enable"), Play("sound", wnfh_sfx_list["plimp2"])]           ,  [Preference("auto-forward time", 0), Preference("auto-forward after click", "disable")]      , _preferences.afm_time != 0     ],
                #["skip"             ,"Пропускать"                 ,[Preference("skip", "all"),                        Play("sound", wnfh_sfx_list["plimp2"])]           ,  Preference("skip", "seen")                                                                   , _preferences.skip_unseen        ],                                                                             , NullAction()        ],
                #["font"             ,"Шрифт"                      ,[SetField(persistent, "font_size", "large"),       Play("sound", wnfh_sfx_list["plimp2"])]           ,  SetField(persistent, "font_size", "small")                                                   , persistent.font_size == "large" ],
                
                #["time_of_day"      ,"Время суток"         ,FieldValue(persistent, "wnfh_mat_filter", 3, step=1)    ,wnfh_bars["multibutton_bar_full"][0]  ,wnfh_bars["multibutton_bar_null"][0], 248  ],
                ["mat_filter"       ,"Мат-фильтр"          ,FieldValue(persistent, "wnfh_mat_filter", 2, step=1)    ,wnfh_bars["multibutton_bar_full"][0]  ,wnfh_bars["multibutton_bar_null"][0], 248  ],
                ["hentai_mod"       ,"Отображение хентая"  ,FieldValue(persistent, "wnfh_hentai_mod", 1, step=1)    ,wnfh_bars["button_bar_full"][0]  ,wnfh_bars["button_bar_null"][0], 145  ],
                ["widget_lp"        ,"Виджет очков"        ,FieldValue(persistent, "wnfh_widget_lp", 1, step=1)     ,wnfh_bars["button_bar_full"][0]  ,wnfh_bars["button_bar_null"][0], 145  ],

                ["debug_color"      ,"Цветовая индикация"  ,FieldValue(persistent, "wnfh_debug_color", 1, step=1)   ,wnfh_bars["button_bar_full"][0]  ,wnfh_bars["button_bar_null"][0], 145  ],

            ]

        frame:
            if persistent.wnfh_debug_color:
                background frame_black
            else:
                background frame_transparent
            area(0.5, 0.0, 1.0, 0.15)
            xanchor 0.5
            
            frame:
                if persistent.wnfh_debug_color:
                    background frame_black
                else:
                    background frame_transparent
                area(0.5, 0.0, 0.7, 1.0)
                xanchor 0.5             
                text "Настройки":
                    pos(0.5, 0.5)
                    style "wnfh_choice_" + persistent.timeofday
                    xanchor 0.5
                    size 100
                    kerning 1
                    min_width 200
                    layout "tex"
        frame:
            if persistent.wnfh_debug_color:
                background frame_black
            else:
                background frame_transparent
            area(0.5, 0.16, 1.0, 0.85)
            xanchor 0.5
            frame:
                if persistent.wnfh_debug_color:
                    background frame_black
                else:
                    background frame_transparent
                area(0.0, 0.3, 500, 300)
                yanchor 0.5
                grid 1 4:
                    anchor (0.5, 0.5) pos (0.5, 0.5)
                    spacing 2
    
                    for index, i in enumerate(wnfh_preferences_button[0:4]):
                        frame:
                            background frame_transparent
                            area(0.5, 0.5, 1.0, 65)
                            xanchor 0.5 yanchor 0.5
        
                            add (wnfh_gui["tint_elements"]["im_line"]):
                                xzoom 0.7
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                                xalign 0.5 yanchor 1.0
        
                            add (wnfh_gui["tint_elements"]["im_bg"]):
                                xzoom 0.7
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][2])
                                xalign 0.5
        
                            if wnfh_screen_variable[index]:
                                add (wnfh_gui["tint_elements"]["im_gradient"]):
                                    xzoom 0.7
                                    xalign 0.5 alpha 0.6
                                    matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][0])
                                add (wnfh_gui["tint_elements"]["im_gradient"]):
                                    xzoom 0.7
                                    xalign 0.5 alpha 0.1
                            else:
                                null height 20
        
                            add (wnfh_gui["tint_elements"]["im_line"]):
                                xzoom 0.7
                                matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                                xalign 0.5 ypos 1.0 yanchor 0.0
    
                            textbutton i[0]:
                                text_line_leading 5 text_line_spacing 3
                                text_min_width 390
                                text_text_align 0.5
                                xalign 0.5 yanchor 0.5 ypos 0.5
                                text_style "wnfh_choice_" + persistent.timeofday
                                background None
                                hover_sound wnfh_gui["sound"]["plimp"]
                                hovered ToggleScreenVariable(wnfh_screen_variable_string[index])
                                unhovered ToggleScreenVariable(wnfh_screen_variable_string[index])
                                action (i[1])

            if wnfh_preferences_variable[0]: # ===================== Интерфейс
                frame:
                    if persistent.wnfh_debug_color:
                        background frame_black
                    else:
                        background frame_transparent
                    area(0.5, 0.0, 0.46, 1.0)
                    xanchor 0.5

                    add (wnfh_gui["tint_elements"]["pr_big_frame_bg"]):
                        matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][2])
                        xalign 0.5
                    add (wnfh_gui["tint_elements"]["pr_big_frame"]):
                        matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                        xalign 0.5
                    grid 1 5:
                        for bar in wnfh_preferences_bar[3:5]:
                            frame:
                                if persistent.wnfh_debug_color:
                                    background frame_black
                                else:
                                    background frame_transparent
                                area(0.0, 0.0, 1.0, 60)
                                frame:
                                    if persistent.wnfh_debug_color:
                                        background frame_red
                                    else:
                                        background frame_transparent
                                    area(0.0, 0.5, 350, 1.0)
                                    yanchor 0.5
                                    text bar[1]:
                                        pos(0.5, 0.5)
                                        style "wnfh_choice_" + persistent.timeofday
                                        xanchor 0.5
                                        size 20
                                        kerning 1
                                        min_width 200
                                        layout "tex"
                                        #action Play("sound", wnfh_gui["sound"]["plimp"]) 
                                frame:
                                    if persistent.wnfh_debug_color:
                                        background frame_green
                                    else:
                                        background frame_transparent
                                    area(1.0, 0.5, 485, 1.0)
                                    xanchor 1.0 yanchor 0.5
                                    bar value bar[2]:
                                        left_bar wnfh_bars["bar_full"][0]
                                        right_bar wnfh_bars["bar_null"][0]
                                        thumb wnfh_bars["htumb"][0]
                                        hover_thumb wnfh_bars["htumb"][0]
                                        xmaximum 1.0 ymaximum 37 yanchor 0.5 ypos 0.5
                        for bar in wnfh_preferences_switch[0:3]:                    
                            frame:
                                if persistent.wnfh_debug_color:
                                    background frame_black
                                else:
                                    background frame_transparent
                                area(0.0, 0.0, 1.0, 60)
                                frame:
                                    if persistent.wnfh_debug_color:
                                        background frame_red
                                    else:
                                        background frame_transparent
                                    area(0.0, 0.5, 350, 1.0)
                                    yanchor 0.5
                                    text bar[1]:
                                        pos(0.5, 0.5)
                                        style "wnfh_choice_" + persistent.timeofday
                                        xanchor 0.5
                                        size 20
                                        kerning 1
                                        min_width 200
                                        layout "tex"
                                        #action Play("sound", wnfh_gui["sound"]["plimp"]) 
                                frame:
                                    if persistent.wnfh_debug_color:
                                        background frame_blue
                                    else:
                                        background frame_transparent
                                    area(0.6, 0.5, 150, 1.0)
                                    xanchor 1.0 yanchor 0.5
                                frame:
                                    if persistent.wnfh_debug_color:
                                        background frame_green
                                    else:
                                        background frame_transparent
                                    area(0.6, 0.5, bar[5]+12, 1.0)
                                    xanchor 0.0 yanchor 0.5
                                    bar value bar[2]:
                                        left_bar bar[3]
                                        right_bar bar[4]
                                        thumb wnfh_bars["htumb"][0]
                                        hover_thumb wnfh_bars["htumb"][0]
                                        xmaximum 1.0 ymaximum 35 yanchor 0.5 ypos 0.5

            elif wnfh_preferences_variable[1]: # ===================== Аудио
                frame:
                    if persistent.wnfh_debug_color:
                        background frame_black
                    else:
                        background frame_transparent
                    area(0.5, 0.0, 0.46, 1.0)
                    xanchor 0.5

                    add (wnfh_gui["tint_elements"]["pr_big_frame_bg"]):
                        matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][2])
                        xalign 0.5
                    add (wnfh_gui["tint_elements"]["pr_big_frame"]):
                        matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                        xalign 0.5

                    grid 1 3:
                        for bar in wnfh_preferences_bar[0:3]:
                            frame:
                                if persistent.wnfh_debug_color:
                                    background frame_black
                                else:
                                    background frame_transparent
                                area(0.0, 0.0, 1.0, 60)
                                frame:
                                    if persistent.wnfh_debug_color:
                                        background frame_red
                                    else:
                                        background frame_transparent
                                    area(0.0, 0.5, 0.2, 1.0)
                                    yanchor 0.5
                                    text bar[1]:
                                        pos(0.5, 0.5)
                                        style "wnfh_choice_" + persistent.timeofday
                                        xanchor 0.5
                                        size 30
                                        kerning 1
                                        min_width 200
                                        layout "tex"
                                        #action Play("sound", wnfh_gui["sound"]["plimp"]) 
                                frame:
                                    if persistent.wnfh_debug_color:
                                        background frame_green
                                    else:
                                        background frame_transparent
                                    area(1.0, 0.5, 485, 1.0)
                                    xanchor 1.0 yanchor 0.5
                                    bar value bar[2]:
                                        left_bar wnfh_bars["bar_full"][0]
                                        right_bar wnfh_bars["bar_null"][0]
                                        thumb wnfh_bars["htumb"][0]
                                        hover_thumb wnfh_bars["htumb"][0]
                                        xmaximum 1.0 ymaximum 37 yanchor 0.5 ypos 0.5

            elif wnfh_preferences_variable[2]: # ===================== Амогус
                frame:
                    if persistent.wnfh_debug_color:
                        background frame_black
                    else:
                        background frame_transparent
                    area(0.5, 0.0, 0.46, 1.0)
                    xanchor 0.5

                    add (wnfh_gui["tint_elements"]["pr_big_frame_bg"]):
                        matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][2])
                        xalign 0.5
                    add (wnfh_gui["tint_elements"]["pr_big_frame"]):
                        matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][1])
                        xalign 0.5
                    
                    grid 1 1:
                        for bar in wnfh_preferences_switch[3:4]:                    
                            frame:
                                if persistent.wnfh_debug_color:
                                    background frame_black
                                else:
                                    background frame_transparent
                                area(0.0, 0.0, 1.0, 60)
                                frame:
                                    if persistent.wnfh_debug_color:
                                        background frame_red
                                    else:
                                        background frame_transparent
                                    area(0.0, 0.5, 350, 1.0)
                                    yanchor 0.5
                                    text bar[1]:
                                        pos(0.5, 0.5)
                                        style "wnfh_choice_" + persistent.timeofday
                                        xanchor 0.5
                                        size 20
                                        kerning 1
                                        min_width 200
                                        layout "tex"
                                        #action Play("sound", wnfh_gui["sound"]["plimp"]) 
                                frame:
                                    if persistent.wnfh_debug_color:
                                        background frame_blue
                                    else:
                                        background frame_transparent
                                    area(0.6, 0.5, 150, 1.0)
                                    xanchor 1.0 yanchor 0.5
                                frame:
                                    if persistent.wnfh_debug_color:
                                        background frame_green
                                    else:
                                        background frame_transparent
                                    area(0.6, 0.5, bar[5]+12, 1.0)
                                    xanchor 0.0 yanchor 0.5
                                    bar value bar[2]:
                                        left_bar bar[3]
                                        right_bar bar[4]
                                        thumb wnfh_bars["htumb"][0]
                                        hover_thumb wnfh_bars["htumb"][0]
                                        xmaximum 1.0 ymaximum 35 yanchor 0.5 ypos 0.5

                


            frame:
                if persistent.wnfh_debug_color:
                    background frame_black
                else:
                    background frame_transparent
                area(1.0, 0.3, 500, 200)
                xanchor 1.0 yanchor 0.5
            frame:
                if persistent.wnfh_debug_color:
                    background frame_black
                else:
                    background frame_transparent
                area(1.0, 0.7, 500, 500)
                xanchor 1.0 yanchor 0.5
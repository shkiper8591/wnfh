init 1000 python:
    if debug_switch:
        config.developer = True
init -5:
    $ global frame_transparent
    $ global frame_black
    $ global frame_red
    $ global frame_green
    $ global frame_blue
    $ global frame_purpl

    $ global debug_switch

    $ frame_transparent = "#0000"
    $ frame_black       = "#0005"
    $ frame_red         = "#F005"
    $ frame_green       = "#0F05"
    $ frame_blue        = "#00F5"
    $ frame_purpl       = "#F0F5"

    $ debug_switch = 1 

    if persistent.wnfh_mat_filter == None:
        $ persistent.wnfh_mat_filter = 0

    if persistent.all_sound == None:
        $ persistent.all_sound = "mute"

    if persistent.wnfh_hentai_mod == None:
        $ persistent.wnfh_hentai_mod = 0

    if persistent.wnfh_widget_lp == None:
        $ persistent.wnfh_widget_lp = 0

    if persistent.wnfh_widget_clock == None:
        $ persistent.wnfh_widget_clock = 0

    if persistent.wnfh_widget_music_player == None:
        $ persistent.wnfh_widget_music_player = 0

    if persistent.wnfh_debug_color == None:
        $ persistent.wnfh_debug_color = 0
    

init 2:
    screen wnfh_preferences:

        modal True #tag menu

        $ debug_frame = {
            "black":  frame_black  if persistent.wnfh_debug_color else frame_transparent,
            "red":    frame_red    if persistent.wnfh_debug_color else frame_transparent,
            "green":  frame_green  if persistent.wnfh_debug_color else frame_transparent,
            "blue":   frame_blue   if persistent.wnfh_debug_color else frame_transparent,
            "purple": frame_purpl  if persistent.wnfh_debug_color else frame_transparent
        }
        
        default wnfh_button_states = [False for i in range(1)]

        python:

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
                "tumb": [im.MatrixColor(wnfh_frames_elements["settings_bar_tumb"][0], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', wnfh_frames_elements["settings_bar_tumb"][4], renpy.store.wnfh_tymeofday)))],
                
                "bar_full": [im.Composite(
                    (25, 25),
                    (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_full"][0], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', wnfh_frames_elements["settings_bar_full"][4], renpy.store.wnfh_tymeofday))),
                    (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_null"][0], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', wnfh_frames_elements["settings_bar_null"][4], renpy.store.wnfh_tymeofday))),
                    )],

                "bar_null": [im.Composite(
                    (25, 25),
                    (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_bg"][0], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', wnfh_frames_elements["settings_bar_bg"][4], renpy.store.wnfh_tymeofday))),
                    (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_null"][0], im.matrix.tint(*converter_hex('wnfh_choice_tint_color', wnfh_frames_elements["settings_bar_null"][4], renpy.store.wnfh_tymeofday))),
                    )],
            }
            wnfh_preferences_other_buttons = [
                ["fullscreen" ,"Полный экран"       ,Preference("display", "fullscreen"),  Preference("display", "window"), _preferences.fullscreen],
                ["hentai_mod" ,"Отображение хентая" ,AnimatedValue(value=persistent.wnfh_hentai_mod, range=1.0, delay=0.1)   ,wnfh_bars["bar_full"][0]       ,wnfh_bars["bar_null"][0]        ,145      ,1    ],
            ]
            wnfh_preferences_audio_bars = [
                ["music"   ,"Музыка"          ,Preference("music volume"), wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 500, 1],
                ["sfx"     ,"Звуки"           ,Preference("sound volume"), wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 500, 1],
                ["voice"   ,"Эмбиент"         ,Preference("voice volume"), wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 500, 1],
            ]
            wnfh_preferences_audio_buttons = [
                ["ap_misic"            ,"///"  ,AnimatedValue(value=persistent.wnfh_ap_misic, range=1.0, delay=0.1) ,wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 145, 1],
            ]
            wnfh_preferences_widget_buttons = [
                ["widget_lp"           ,"Очки персонажей"     ,AnimatedValue(value=persistent.wnfh_widget_lp, range=1.0, delay=0.1)           ,wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 145, 1],
                ["widget_clock"        ,"Часы"                ,AnimatedValue(value=persistent.wnfh_widget_clock, range=1.0, delay=0.1)        ,wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 145, 1],
                ["widget_music_player" ,"Текущий трек"        ,AnimatedValue(value=persistent.wnfh_widget_music_player, range=1.0, delay=0.1) ,wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 145, 1],
                ["debug_color"         ,"Цветовая индикация"  ,AnimatedValue(value=persistent.wnfh_debug_color, range=1.0, delay=0.1)         ,wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 145, 1],
            ]
            wnfh_preferences_text_bars = [
                ["text_speed"       ,"Скорость текста"     ,Preference("text speed")         ],
                ["autoforward_time" ,"Время автопереходов" ,Preference("auto-forward time")  ],
            ]
            wnfh_preferences_text_buttons = [
                ["autoforward" ,"Автопереход"  ,[Preference("auto-forward after click", "enable"),  [Preference("auto-forward time", 0), Preference("auto-forward after click", "disable")]      , _preferences.afm_time != 0     ]],
                ["skip"        ,"Пропускать"   ,[Preference("skip", "all"),                         Preference("skip", "seen")                                                                   , _preferences.skip_unseen        ], NullAction()        ],
                ["font"        ,"Шрифт"        ,[SetField(persistent, "font_size", "large"),        SetField(persistent, "font_size", "small")                                                   , persistent.font_size == "large" ]],
                ["mat_filter"  ,"Мат-фильтр"   ,AnimatedValue(value=persistent.wnfh_mat_filter, range=2.0, delay=0.1)   ,wnfh_bars["bar_full"][0]       ,wnfh_bars["bar_null"][0]        ,248      ,2    ],
            ]

            wnfh_preferences_button = [
                ["back", "Назад", [ShowMenu('game_menu_selector'), Hide('preferences')]]
            ]
        add wnfh_gui["tint_elements"]["vignette"]

        for index, button in enumerate(wnfh_preferences_button[0:1]):
            frame:
                area(0.1, 0.08, 150, 60)
                xanchor 0.5 yanchor 0.5
                background debug_frame["blue"] 
                vbox: # ================================================ Вбокс кнопок
                    pos (0.5, 0.5)
                    xanchor 0.5 yanchor 0.5
                    spacing 0
                    for element in ["back_button_line", "back_button_bg", "back_button_line"]:
                        frame:
                            if persistent.wnfh_debug_color:
                                background wnfh_frames_elements[element][5]
                            else:
                                background frame_transparent
                            area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                            add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                matrixcolor TintMatrix(wnfh_choice_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
                frame: # ================================================ Тонировка при наведении
                    if wnfh_button_states[index]:
                        add Frame(wnfh_frames_elements["back_button_gradient"][0], left=wnfh_frames_elements["back_button_gradient"][3], top=0):
                            xalign 0.5 yalign 0.5 alpha 0.6
                            matrixcolor TintMatrix(wnfh_choice_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["back_button_gradient"][4]])
                        add Frame(wnfh_frames_elements["back_button_gradient"][0], left=wnfh_frames_elements["back_button_gradient"][3], top=0):
                            xalign 0.5 yalign 0.5 alpha 0.1
                    else:
                        null height 20
                    area(0.5, 0.5, wnfh_frames_elements["back_button_bg"][1], wnfh_frames_elements["back_button_bg"][2]) padding(0, 0) xanchor 0.5 yanchor 0.5
                    background debug_frame["purple"]
                    textbutton button[1]: # ================================================ Текст кнопок
                        xalign 0.5 yanchor 0.5 ypos 0.5
                        text_line_leading 5 text_line_spacing 3
                        text_min_width 390
                        text_text_align 0.5
                        text_style "wnfh_choice_" + renpy.store.wnfh_tymeofday
                        yoffset 2
                        background None
                        hover_sound wnfh_gui["sound"]["plimp"]
                        hovered ToggleDict(wnfh_button_states, index)
                        unhovered ToggleDict(wnfh_button_states, index)
                        action button[2]
                        at wnfh_mm_button_hover_atl()

        frame at atl_wnfh_widget_lp_down:
            area(0.5, 0.08, wnfh_frames_elements["settings_main_title_bg"][1] + 40, wnfh_frames_elements["settings_main_title_bg"][2] + 20)
            xanchor 0.5 yanchor 0.5
            background debug_frame["black"]
            vbox: # ================================================ Фон таблички из трёх кусков
                pos (0.5, 0.5)
                xanchor 0.5 yanchor 0.5
                spacing 0
                for element in ["settings_main_title_line", "settings_main_title_bg", "settings_main_title_line"]:
                    #frame at wnfh_frames_elements[element][6]:
                    frame:
                        if persistent.wnfh_debug_color:
                            background wnfh_frames_elements[element][5]
                        else:
                            background frame_transparent
                        area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])             
            text "Настройки":
                pos(0.5, 0.55)
                style "wnfh_choice_" + renpy.store.wnfh_tymeofday
                xanchor 0.5
                size 100
                kerning 1
                min_width 200
                layout "tex"
        frame at govno_ebanoe2:
            area(0.5, 0.97, 1.0, 0.8)
            xanchor 0.5 yanchor 1.0
            background debug_frame["black"]
            vbox: # ================================================ Фон таблички из трёх кусков
                pos (0.5, 0.5)
                xanchor 0.5 yanchor 0.5
                spacing 0
                for element in ["settings_box_line", "settings_box_bg", "settings_box_line"]:
                    frame at wnfh_frames_elements[element][6]:
                    #frame:
                        if persistent.wnfh_debug_color:
                            background wnfh_frames_elements[element][5]
                        else:
                            background frame_transparent
                        area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]]) 
            frame at wjuh_bg:
                area(0.5, 0.5, 0.98, 1.0)
                xanchor 0.5 yanchor 0.5
                background debug_frame["black"]
                 
                frame: # ============================ Левый блок
                    area(0.0, 0.5, 0.5, 0.5)
                    xanchor 0.0 yanchor 1.0
                    background debug_frame["green"]
                    vbox:
                        pos (0.5, 0.0)
                        xanchor 0.5 yanchor 0.0
                        spacing 0

                        frame:
                            area(0.5, 0.0, 0.9, 80)
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["black"]

                        frame: # ======================== Заголовок "Аудио"
                            area(0.5, 0.0, wnfh_frames_elements["settings_title_bg"][1] + 40, wnfh_frames_elements["settings_title_bg"][2] + 10)
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["black"]
                            vbox: # ================================================ Фон таблички из трёх кусков
                                pos (0.5, 0.5)
                                xanchor 0.5 yanchor 0.5
                                spacing 0
                                for element in ["settings_title_line", "settings_title_bg", "settings_title_line"]:
                                    frame at wnfh_frames_elements[element][6]:
                                    #frame:
                                        if persistent.wnfh_debug_color:
                                            background wnfh_frames_elements[element][5]
                                        else:
                                            background frame_transparent
                                        area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                            matrixcolor TintMatrix(wnfh_choice_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
                            text "Аудио":
                                pos(0.5, 0.55)
                                style "wnfh_choice_" + renpy.store.wnfh_tymeofday
                                xanchor 0.5
                                size 50
                                kerning 1
                                min_width 200
                                layout "tex"
                        frame: # ====================== Кнопки ползунки и кнопки аудио
                            area(0.5, 0.0, 0.9, 250)
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["black"]
                            vbox:
                                pos (0.5, 0.0)
                                xanchor 0.5 yanchor 0.0
                                spacing 2
                                for element in range(len(wnfh_preferences_audio_bars)): # + len(wnfh_preferences_audio_buttons)):
                                    frame:
                                        area(0.5, 0.5, 1.0, 230/4)
                                        xanchor 0.5 yanchor 0.5
                                        background debug_frame["black"]
                                        frame:
                                            background debug_frame["red"]
                                            area(0.0, 0.5, 200, 1.0)
                                            xanchor 0.0 yanchor 0.5
                                            text wnfh_preferences_audio_bars[element][1]:
                                                pos(0.0, 0.5)
                                                style "wnfh_choice_" + renpy.store.wnfh_tymeofday
                                                xanchor 0.0
                                                size 30
                                                kerning 1
                                                xmaximum 600
                                                layout "tex"
                                        frame:
                                            background debug_frame["blue"]
                                            area(200, 0.5, 90, 1.0)
                                            xanchor 0.0 yanchor 0.5
                                            text "{}%".format(int(preferences.get_volume(wnfh_preferences_audio_bars[element][0]) * 100.0)):
                                                pos(1.0, 0.5)
                                                style "wnfh_choice_" + renpy.store.wnfh_tymeofday
                                                xanchor 1.0
                                                size 30
                                                kerning 1
                                                xmaximum 600
                                                layout "tex"

                                        frame:
                                            background debug_frame["green"]
                                            area(1.0, 0.5, wnfh_preferences_audio_bars[element][5]+12, 1.0)
                                            xanchor 1.0 yanchor 0.5
                                            bar value wnfh_preferences_audio_bars[element][2]:
                                                left_bar Frame(wnfh_bars["bar_full"][0], wnfh_frames_elements["settings_bar_full"][1], wnfh_frames_elements["settings_bar_full"][1])
                                                right_bar Frame(wnfh_bars["bar_null"][0], wnfh_frames_elements["settings_bar_null"][1], wnfh_frames_elements["settings_bar_null"][1])
                                                thumb wnfh_bars["tumb"][0]
                                                hover_thumb wnfh_bars["tumb"][0]
                                                xmaximum 1.0 ymaximum 39
                                                yanchor 0.5 ypos 0.5

                frame: # ============================ Правый блок
                    area(1.0, 0.5, 0.5, 0.5)
                    xanchor 1.0 yanchor 1.0
                    background debug_frame["blue"]
                    vbox:
                        pos (0.5, 0.0)
                        xanchor 0.5 yanchor 0.0
                        spacing 0
                        frame:
                            area(0.5, 0.0, 0.9, 80)
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["black"]
                        frame: # ======================== Заголовок "Виджеты"
                            area(0.5, 0.0, wnfh_frames_elements["settings_title_bg"][1] + 40, wnfh_frames_elements["settings_title_bg"][2] + 10)
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["black"]
                            vbox: # ================================================ Фон таблички из трёх кусков
                                pos (0.5, 0.5)
                                xanchor 0.5 yanchor 0.5
                                spacing 0
                                for element in ["settings_title_line", "settings_title_bg", "settings_title_line"]:
                                    frame at wnfh_frames_elements[element][6]:
                                        if persistent.wnfh_debug_color:
                                            background wnfh_frames_elements[element][5]
                                        else:
                                            background frame_transparent
                                        area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                            matrixcolor TintMatrix(wnfh_choice_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
                            text "Виджеты": # ============================ Виджеты
                                pos(0.5, 0.55)
                                style "wnfh_choice_" + renpy.store.wnfh_tymeofday
                                xanchor 0.5
                                size 50
                                kerning 1
                                min_width 200
                                layout "tex"
                        frame:
                            area(0.5, 0.0, 0.9, 250)
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["black"]
                            vbox:
                                pos (0.5, 0.0)
                                xanchor 0.5 yanchor 0.0
                                spacing 2
                                for element in range(len(wnfh_preferences_widget_buttons)):
                                    frame:
                                        area(0.5, 0.5, 1.0, 230/4)
                                        xanchor 0.5 yanchor 0.5
                                        background debug_frame["black"]
                                        frame:
                                            background debug_frame["red"]
                                            area(0.0, 0.5, 600, 1.0)
                                            xanchor 0.0 yanchor 0.5
                                            text wnfh_preferences_widget_buttons[element][1]:
                                                pos(0.0, 0.5)
                                                style "wnfh_choice_" + renpy.store.wnfh_tymeofday
                                                xanchor 0.0
                                                size 30
                                                kerning 1
                                                xmaximum 600
                                                layout "tex"
                                        frame:
                                            background debug_frame["green"]
                                            area(1.0, 0.5, wnfh_preferences_widget_buttons[element][5]+12, 1.0)
                                            xanchor 1.0 yanchor 0.5
                                            bar value wnfh_preferences_widget_buttons[element][2]:
                                                left_bar Frame(wnfh_bars["bar_full"][0], wnfh_frames_elements["settings_bar_full"][1], wnfh_frames_elements["settings_bar_full"][1])
                                                right_bar Frame(wnfh_bars["bar_null"][0], wnfh_frames_elements["settings_bar_null"][1], wnfh_frames_elements["settings_bar_null"][1])
                                                thumb wnfh_bars["tumb"][0]
                                                hover_thumb wnfh_bars["tumb"][0]
                                                xmaximum 1.0 ymaximum 39
                                                yanchor 0.5 ypos 0.5
                                            frame:
                                                background debug_frame["black"]
                                                area(0.0, 0.5, 1.0, 1.0)
                                                xanchor 0.0 yanchor 0.5
                                                padding(0, 0)
                                                hbox:
                                                    for i in range(wnfh_preferences_widget_buttons[element][6]+1):
                                                        button:
                                                            area(0.5, 0.5, (wnfh_preferences_widget_buttons[element][5]) / (wnfh_preferences_widget_buttons[element][6]+1), 1.0)
                                                            xanchor 0.5 yanchor 0.5
                                                            padding(0, 0)
                                                            action SetField(persistent, "wnfh_" + wnfh_preferences_widget_buttons[element][0], i)
                                                            background debug_frame["red"]
                                                            if persistent.wnfh_debug_color:
                                                                text str(i) align (0.5, 0.5)
                frame: # ============================ Центральный блок
                    area(0.5, 1.0, 1.0, 0.5)
                    xanchor 0.5 yanchor 1.0
                    background debug_frame["purple"]
                    vbox:
                        pos (0.5, 0.0)
                        xanchor 0.5 yanchor 0.0
                        spacing 0
                        frame: # ======================== Заголовок "Текст"
                            area(0.5, 0.0, wnfh_frames_elements["settings_title_bg"][1] + 40, wnfh_frames_elements["settings_title_bg"][2] + 10)
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["black"]
                            vbox: # ================================================ Фон таблички из трёх кусков
                                pos (0.5, 0.5)
                                xanchor 0.5 yanchor 0.5
                                spacing 0
                                for element in ["settings_title_line", "settings_title_bg", "settings_title_line"]:
                                    frame at wnfh_frames_elements[element][6]:
                                    #frame:
                                        if persistent.wnfh_debug_color:
                                            background wnfh_frames_elements[element][5]
                                        else:
                                            background frame_transparent
                                        area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                            matrixcolor TintMatrix(wnfh_choice_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])

                            text "Текст":
                                pos(0.5, 0.55)
                                style "wnfh_choice_" + renpy.store.wnfh_tymeofday
                                xanchor 0.5
                                size 50
                                kerning 1
                                min_width 200
                                layout "tex"
                        frame:
                            area(0.5, 0.0, 0.8, 335)
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["black"]
                            vbox:
                                pos (0.5, 0.0)
                                xanchor 0.5 yanchor 0.0
                                spacing 2
                                for element in range(len(wnfh_preferences_text_bars) + len(wnfh_preferences_text_buttons)):
                                    frame:
                                        area(0.5, 0.0, 1.0, 315/6)
                                        xanchor 0.5 yanchor 0.0
                                        background debug_frame["black"]
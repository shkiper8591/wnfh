init 1000 python:
    if debug_switch:
        config.developer = True
        persistent.wnfh_var_debug["enabled"] = True
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

    if persistent.wnfh_copyright_misic == None:
        $ persistent.wnfh_copyright_misic = 0

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

    if persistent.wnfh_quality_settings == None:
        $ persistent.wnfh_quality_settings = 0 # 1 высокое качество, 0 низкое качетсво
    

screen wnfh_preferences(main_menu = False):

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
        wnfh_bars = {
            "tumb": [im.MatrixColor(wnfh_frames_elements["settings_bar_tumb"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["settings_bar_tumb"][4], renpy.store.wnfh_tymeofday)))],

            "bar_full": [im.Composite(
                (25, 25),
                (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_full"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["settings_bar_full"][4], renpy.store.wnfh_tymeofday))),
                (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_null"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["settings_bar_null"][4], renpy.store.wnfh_tymeofday))),
                )],
            "bar_null": [im.Composite(
                (25, 25),
                (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_bg"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["settings_bar_bg"][4], renpy.store.wnfh_tymeofday))),
                (0, 0), im.MatrixColor(wnfh_frames_elements["settings_bar_null"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["settings_bar_null"][4], renpy.store.wnfh_tymeofday))),
                )],
        }
        
        wnfh_preferences_audio_bars = [
            ["music"   ,"Музыка"          ,Preference("music volume"), wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 500, 1],
            ["sfx"     ,"Звуки"           ,Preference("sound volume"), wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 500, 1],
            ["voice"   ,"Эмбиент"         ,Preference("voice volume"), wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 500, 1],
        ]
        wnfh_preferences_audio_buttons = [
            ["copyright_misic"     ,"Режим стримера"      ,[SetField(persistent, "whfh_copyright_misic", 0)  ,SetField(persistent, "whfh_copyright_misic", 1)]  ,wnfh_bars["bar_full"][0]   ,wnfh_bars["bar_null"][0]   ,145  ,1],
        ]
        wnfh_preferences_widget_buttons = [
            ["widget_lp"           ,"Очки персонажей"     ,AnimatedValue(value=persistent.wnfh_widget_lp, range=1.0, delay=0.1)           ,wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 145, 1],
            ["widget_clock"        ,"Часы"                ,AnimatedValue(value=persistent.wnfh_widget_clock, range=1.0, delay=0.1)        ,wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 145, 1],
            ["widget_music_player" ,"Текущий трек"        ,AnimatedValue(value=persistent.wnfh_widget_music_player, range=1.0, delay=0.1) ,wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 145, 1],
            ["debug_color"         ,"Цветовая индикация"  ,AnimatedValue(value=persistent.wnfh_debug_color, range=1.0, delay=0.1)         ,wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 145, 1],
        ]
        wnfh_preferences_text_bars = [
            ["text_speed"        ,preferences.text_cps  ,"Скорость текста"     , "символов/сек" ,Preference("text speed")         ,wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 500, 1],
            ["auto_forward_time" ,preferences.afm_time  ,"Время автопереходов" , "сек"          ,Preference("auto-forward time")  ,wnfh_bars["bar_full"][0], wnfh_bars["bar_null"][0], 500, 1],
        ]
        wnfh_preferences_text_buttons = [
            ["autoforward" ,"Автопереход"  ,[Preference("auto-forward after click", "enable")  ,[Preference("auto-forward time", 0), Preference("auto-forward after click", "disable")]]  ,wnfh_bars["bar_full"][0]       ,wnfh_bars["bar_null"][0]   ,145  ,1],
            ["skip"        ,"Пропускать"   ,[Preference("skip", "all")                         ,Preference("skip", "seen")                                                             ]  ,wnfh_bars["bar_full"][0]       ,wnfh_bars["bar_null"][0]   ,145  ,1],
            ["font"        ,"Шрифт"        ,[SetField(persistent, "font_size", "large")        ,SetField(persistent, "font_size", "small")                                             ]  ,wnfh_bars["bar_full"][0]       ,wnfh_bars["bar_null"][0]   ,145  ,1],
            ["mat_filter"  ,"Мат-фильтр"   ,[SetField(persistent, "whfh_mat_filter", 0)        ,SetField(persistent, "whfh_mat_filter", 1) ,SetField(persistent, "whfh_mat_filter", 2) ]  ,wnfh_bars["bar_full"][0]       ,wnfh_bars["bar_null"][0]   ,248  ,2],
        ]
        wnfh_preferences_other_buttons = [
            #["fullscreen" ,"Полный экран"       ,Preference("display", "fullscreen"),  Preference("display", "window"), _preferences.fullscreen],
            #["hentai_mod" ,"Отображение хентая" ,AnimatedValue(value=persistent.wnfh_hentai_mod, range=1.0, delay=0.1)   ,wnfh_bars["bar_full"][0]       ,wnfh_bars["bar_null"][0]        ,145      ,1    ],
            ["gaphics_mod" ,"Крутая графика"     ,[SetField(persistent, "wnfh_quality_settings", 0)        ,SetField(persistent, "wnfh_quality_settings", 1) ,SetField(persistent, "wnfh_quality_settings", 2) ]  ,wnfh_bars["bar_full"][0]       ,wnfh_bars["bar_null"][0]   ,145  ,1],
        ]
        wnfh_preferences_text_buttons_states = {
            "autoforward":  [preferences, "afm_enable",     {False:   0      ,True:    1}],
            "skip":         [preferences, "skip_unseen",    {False:   0      ,True:    1}],
            "font":         [persistent, "font_size",       {"small": 0      ,"large": 1}], # ГОВНО КАКОЕ-ТО! persistent.font_size
            "mat_filter":   [persistent, "wnfh_mat_filter", {0:       0      ,1:       1        ,2: 2}]
        }
        wnfh_preferences_other_buttons_states = {
            "gaphics_mod":   [persistent, "wnfh_quality_settings", {0: 0, 1: 1, 2: 2}]
        }
        wnfh_preferences_audio_buttons_states = {
            "copyright_misic":   [persistent, "wnfh_copyright_misic", {0: 0, 1: 1}]
        }
        wnfh_preferences_display_labels = {
            "autoforward":     { 0: "ВЫКЛ",           1: "ВКЛ"              },
            "skip":            { 0: "Виденное ранее", 1: "Всё"   },
            "font":            { 0: "Обычный",        1: "Крупный"          },
            "mat_filter":      { 0: "Без цензуры",    1: "Цензура", 2: "Литературная замена" },
            "gaphics_mod":     { 0: "Хуёвый графон",  1: "База",    2: "Ультра HD 4К пожар RTX 5090" },
            "copyright_misic": { 0: "Любая музыка",   1: "Безопасная"          },
        }

        wnfh_button_tits = {
            "music":               ["Крутилка для саундтрека. Не регулирует качество, только громкость"],
            "sfx":                 ["Здесь живут всякие «дзынь», «хлоп» и иже с ними. Хотите тишины? Сдвиньте в ноль и игра внезапно станет артхаусом"],
            "voice":               ["Тут регулируется «атмосфера». Хотите нормально слышать окружение — выкрутите в максимум, хотите PowerPoint-презентацию — в минимум"],
            "copyright_misic":     ["Режим музыки без авторских прав. Отключает всю музыку, которая может повредить стримерам и контент мейкерам", "Останется только наша собственная музыка и та, на которую не будут ругаться площадки"],
            "widget_lp":           ["текст1", "текст2"],       
            "widget_clock":        ["текст1", "текст2"],    
            "widget_music_player": ["текст1", "текст2"],
            "debug_color":         ["текст1", "текст2"],
            "text_speed":          ["текст1", "текст2"],
            "auto_forward_time":   ["текст1", "текст2"],
            "autoforward":         ["автопереход", "текст2"],
            "skip":                ["пропуск", "текст2"],
            "font":                ["шрифт", renpy.displayable(wnfh_gui["achievements"]["handass"]), "текст2"],
            "mat_filter":          ["мат фильтр", "текст2"],
            "gaphics_mod":         ["текст1", "текст2"],
        }

        if main_menu:
            wnfh_preferences_button = [
                ["back", "Назад", [ShowMenu('main_menu'), Hide('preferences'), Hide('wnfh_preferences_tits')]]
            ]
        else:
            wnfh_preferences_button = [
                ["back", "Назад", [ShowMenu('game_menu_selector'), Hide('preferences'), Hide('wnfh_preferences_tits')]]
            ]
        mm_backgrounds = {
            "night":  wnfh_gui["main_menu"]["mm_bg_night"],
            "sunset": wnfh_gui["main_menu"]["mm_bg_sunset"],
            "day":    wnfh_gui["main_menu"]["mm_bg_day"],
        }

    if main_menu:
        default current_hour = wnfh_get_usertime("hour") # ======================= Главное меню подстраивается под время суток компьютера

        default time_period = (
            "night"  if (current_hour >= 22 or current_hour < 8) else
            "sunset" if (current_hour < 12)                      else
            "day"    if (current_hour < 19)                      else
            "sunset"
        )

        frame:
            background mm_backgrounds[time_period] # ================== Фон в главном меню
            area(0.0, 0.0, 1.0, 1.0)

    default wnfh_preferences_text_buttons_states_current = {
        "autoforward":  wnfh_preferences_text_buttons_states["autoforward"][2][preferences.afm_enable],
        "skip":         wnfh_preferences_text_buttons_states["skip"][2][preferences.skip_unseen],
        "font":         wnfh_preferences_text_buttons_states["font"][2][persistent.font_size],
        "mat_filter":   wnfh_preferences_text_buttons_states["mat_filter"][2][persistent.wnfh_mat_filter]
    }
    default wnfh_preferences_other_buttons_states_current = {
        "gaphics_mod":   wnfh_preferences_other_buttons_states["gaphics_mod"][2][persistent.wnfh_quality_settings]
    }

    default wnfh_preferences_audio_buttons_states_current = {
        "copyright_misic":   wnfh_preferences_audio_buttons_states["copyright_misic"][2][persistent.wnfh_copyright_misic]
    }

    add wnfh_gui["tint_elements"]["vignette"]

    for index, button in enumerate(wnfh_preferences_button[0:1]): # ================================================ Кнопка Назад
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
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])

            frame: # ================================================ Тонировка при наведении
                if wnfh_button_states[index]:
                    add Frame(wnfh_frames_elements["back_button_gradient"][0], left=wnfh_frames_elements["back_button_gradient"][3], top=0):
                        xalign 0.5 yalign 0.5 alpha 0.6
                        matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["back_button_gradient"][4]])
                    add Frame(wnfh_frames_elements["back_button_gradient"][0], left=wnfh_frames_elements["back_button_gradient"][3], top=0):
                        xalign 0.5 yalign 0.5 alpha 0.1
                else:
                    null height 20
                area(0.5, 0.5, wnfh_frames_elements["back_button_bg"][1], wnfh_frames_elements["back_button_bg"][2]) padding(0, 0) xanchor 0.5 yanchor 0.5
                background debug_frame["purple"]
                textbutton button[1]: # ================================================ Текст кнопок
                    style "wnfh_buttons"
                    text_style "wnfh_text_" + renpy.store.wnfh_tymeofday
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
                        matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])

        text "Настройки":
            style "wnfh_title_1_" + renpy.store.wnfh_tymeofday

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
                        matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
        frame at wjuh_bg:
            area(0.5, 0.5, 0.98, 1.0)
            xanchor 0.5 yanchor 0.5
            background debug_frame["black"]
            frame:
                area(0.01, 0.0, 1100, 0.98)
                xanchor 0.0 yanchor 0.0
                background debug_frame["black"]
                viewport id "settings_list":
                    draggable True
                    mousewheel True
                    scrollbars None
                    vbox:
                        pos (0.5, 0.5)
                        xanchor 0.5 yanchor 0.5
                        spacing 0
                 
                        frame: # ============================ Первый блок
                            area(0.5, 0.0, 1.0, (wnfh_frames_elements["settings_title_bg"][2] + 10) + len(wnfh_preferences_audio_bars) * 65 + len(wnfh_preferences_audio_buttons) * 65)
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["green"]
                            vbox:
                                pos (0.5, 0.0)
                                xanchor 0.5 yanchor 0.0
                                spacing 0
                                frame: # ======================== Заголовок "Аудио"
                                    area(0.5, 0.0, wnfh_frames_elements["settings_title_bg"][1] + 40, wnfh_frames_elements["settings_title_bg"][2] + 20)
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
                                                    matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
            
                                    text "Аудио":
                                        style "wnfh_title_2_" + renpy.store.wnfh_tymeofday
            
                                frame: # ====================== Кнопки ползунки и кнопки аудио
                                    area(0.5, 0.0, 0.9, len(wnfh_preferences_audio_bars) * 60 + len(wnfh_preferences_audio_buttons) * 60)
                                    xanchor 0.5 yanchor 0.0
                                    background debug_frame["black"]
                                    vbox:
                                        pos (0.5, 0.0)
                                        xanchor 0.5 yanchor 0.0
                                        spacing 0
                                        for element in range(len(wnfh_preferences_audio_bars)): # + len(wnfh_preferences_audio_buttons)):
                                            frame:
                                                area(0.5, 0.5, 1.0, 228/4)
                                                xanchor 0.5 yanchor 0.5
                                                background debug_frame["black"]
                                                frame:
                                                    background debug_frame["red"]
                                                    area(0.0, 0.5, 200, 1.0)
                                                    xanchor 0.0 yanchor 0.5
                                                    text wnfh_preferences_audio_bars[element][1]:
                                                        style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                                        text_align 0.0
                                                frame:
                                                    background debug_frame["blue"]
                                                    area(200, 0.5, 90, 1.0)
                                                    xanchor 0.0 yanchor 0.5
                                                    text "{}%".format(int(preferences.get_volume(wnfh_preferences_audio_bars[element][0]) * 100.0)):
                                                        style "wnfh_text_" + renpy.store.wnfh_tymeofday
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
                                                        hovered Show("wnfh_preferences_tits", dick = wnfh_button_tits[wnfh_preferences_audio_bars[element][0]])

                                        for element in range(len(wnfh_preferences_audio_buttons)):
                                            frame:
                                                area(0.5, 0.5, 1.0, 57)
                                                xanchor 0.5 yanchor 0.5
                                                background debug_frame["black"]
                                                frame:
                                                    background debug_frame["red"]
                                                    area(0.0, 0.5, 0.4, 1.0)
                                                    xanchor 0.0 yanchor 0.5
                                                    text wnfh_preferences_audio_buttons[element][1]:
                                                        style "wnfh_text_" + renpy.store.wnfh_tymeofday
            
                                                $ pref_current_value = getattr(wnfh_preferences_audio_buttons_states[wnfh_preferences_audio_buttons[element][0]][0], wnfh_preferences_audio_buttons_states[wnfh_preferences_audio_buttons[element][0]][1])
                                                $ pref_integer_value = wnfh_preferences_audio_buttons_states[wnfh_preferences_audio_buttons[element][0]][2][pref_current_value]
                                                frame:
                                                    background debug_frame["blue"]
                                                    area(0.5, 0.5, 0.3, 1.0)
                                                    xanchor 0.5 yanchor 0.5
                                                    text wnfh_preferences_display_labels[wnfh_preferences_audio_buttons[element][0]][pref_integer_value]:
                                                        style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                                        size 20
            
                                                frame:
                                                    background debug_frame["green"]
                                                    area(1.0, 0.5, wnfh_preferences_audio_buttons[element][5]+12, 1.0)
                                                    xanchor 1.0 yanchor 0.5
                                                    bar value AnimatedValue(pref_integer_value, len(wnfh_preferences_audio_buttons_states[wnfh_preferences_audio_buttons[element][0]][2]) - 1, 0.1): # wnfh_preferences_audio_buttons[element][2]:
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
                                                            for i in range(wnfh_preferences_audio_buttons[element][6]):
                                                                button:
                                                                    area(0.5, 0.5, (wnfh_preferences_audio_buttons[element][5]) / (wnfh_preferences_audio_buttons[element][6]), 1.0)
                                                                    xanchor 0.5 yanchor 0.5
                                                                    padding(0, 0)
                                                                    action [wnfh_CycleField(wnfh_preferences_audio_buttons_states[wnfh_preferences_audio_buttons[element][0]][0], wnfh_preferences_audio_buttons_states[wnfh_preferences_audio_buttons[element][0]][1], wnfh_preferences_audio_buttons_states[wnfh_preferences_audio_buttons[element][0]][2].keys()), ]
                                                                    background debug_frame["red"]
                                                                    hovered Show("wnfh_preferences_tits", dick = wnfh_button_tits[wnfh_preferences_audio_buttons[element][0]])

                        frame: # ============================ Второй блок
                            area(0.5, 0.0, 1.0, (wnfh_frames_elements["settings_title_bg"][2] + 10) + len(wnfh_preferences_text_bars) * 65 + len(wnfh_preferences_text_buttons) * 65)
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["purple"]
                            vbox:
                                pos (0.5, 0.0)
                                xanchor 0.5 yanchor 0.0
                                spacing 0
                                frame: # ======================== Заголовок "Текст"
                                    area(0.5, 0.0, wnfh_frames_elements["settings_title_bg"][1] + 40, wnfh_frames_elements["settings_title_bg"][2] + 20)
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
                                                    matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
            
                                    text "Текст":
                                        style "wnfh_title_2_" + renpy.store.wnfh_tymeofday
            
                                frame:
                                    area(0.5, 0.0, 1.0, 370)
                                    xanchor 0.5 yanchor 0.0
                                    background debug_frame["black"]
                                    vbox:
                                        pos (0.5, 0.0)
                                        xanchor 0.5 yanchor 0.0
                                        spacing 0
                                        for element in range(len(wnfh_preferences_text_bars)): #+ len(wnfh_preferences_text_buttons)):
                                            frame:
                                                area(0.5, 0.5, 1.0, 342/6) #+ len(wnfh_preferences_text_buttons))
                                                xanchor 0.5 yanchor 0.5
                                                background debug_frame["black"]
                                                frame:
                                                    background debug_frame["red"]
                                                    area(0.0, 0.5, 0.4, 1.0)
                                                    xanchor 0.0 yanchor 0.5
                                                    text wnfh_preferences_text_bars[element][2]:
                                                        style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                                        text_align 0.0
                                                        #size 25
                                                frame:
                                                    background debug_frame["blue"]
                                                    area(0.5, 0.5, 60, 1.0)
                                                    xanchor 1.0 yanchor 0.5
                                                    text "{}".format(int(wnfh_preferences_text_bars[element][1])):
                                                        style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                                frame:
                                                    background debug_frame["purple"]
                                                    area(0.5, 0.5, 200, 1.0)
                                                    xanchor 0.0 yanchor 0.5
                                                    text wnfh_preferences_text_bars[element][3]:
                                                        style "wnfh_measure_unit_" + renpy.store.wnfh_tymeofday
            
                                                frame:
                                                    background debug_frame["green"]
                                                    area(1.0, 0.5, wnfh_preferences_text_bars[element][7]+12, 1.0)
                                                    xanchor 1.0 yanchor 0.5
                                                    bar value wnfh_preferences_text_bars[element][4]:
                                                        left_bar Frame(wnfh_bars["bar_full"][0], wnfh_frames_elements["settings_bar_full"][1], wnfh_frames_elements["settings_bar_full"][1])
                                                        right_bar Frame(wnfh_bars["bar_null"][0], wnfh_frames_elements["settings_bar_null"][1], wnfh_frames_elements["settings_bar_null"][1])
                                                        thumb wnfh_bars["tumb"][0]
                                                        hover_thumb wnfh_bars["tumb"][0]
                                                        xmaximum 1.0 ymaximum 39
                                                        yanchor 0.5 ypos 0.5
                                                        hovered Show("wnfh_preferences_tits", dick = wnfh_button_tits[wnfh_preferences_text_bars[element][0]])
            
                                        for element in range(len(wnfh_preferences_text_buttons)):
                                            frame:
                                                area(0.5, 0.5, 1.0, 342/6)
                                                xanchor 0.5 yanchor 0.5
                                                background debug_frame["black"]
                                                frame:
                                                    background debug_frame["red"]
                                                    area(0.0, 0.5, 0.4, 1.0)
                                                    xanchor 0.0 yanchor 0.5
                                                    text wnfh_preferences_text_buttons[element][1]:
                                                        style "wnfh_text_" + renpy.store.wnfh_tymeofday
            
                                                $ pref_current_value = getattr(wnfh_preferences_text_buttons_states[wnfh_preferences_text_buttons[element][0]][0], wnfh_preferences_text_buttons_states[wnfh_preferences_text_buttons[element][0]][1])
                                                $ pref_integer_value = wnfh_preferences_text_buttons_states[wnfh_preferences_text_buttons[element][0]][2][pref_current_value]
                                                frame:
                                                    background debug_frame["blue"]
                                                    area(0.5, 0.5, 0.3, 1.0)
                                                    xanchor 0.5 yanchor 0.5
                                                    text wnfh_preferences_display_labels[wnfh_preferences_text_buttons[element][0]][pref_integer_value]:
                                                        style "wnfh_text_" + renpy.store.wnfh_tymeofday
            
                                                frame:
                                                    background debug_frame["green"]
                                                    area(1.0, 0.5, wnfh_preferences_text_buttons[element][5]+12, 1.0)
                                                    xanchor 1.0 yanchor 0.5
                                                    bar value AnimatedValue(pref_integer_value, len(wnfh_preferences_text_buttons_states[wnfh_preferences_text_buttons[element][0]][2]) - 1, 0.1): # wnfh_preferences_text_buttons[element][2]:
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
                                                            for i in range(wnfh_preferences_text_buttons[element][6]):
                                                                button:
                                                                    area(0.5, 0.5, (wnfh_preferences_text_buttons[element][5]) / (wnfh_preferences_text_buttons[element][6]), 1.0)
                                                                    xanchor 0.5 yanchor 0.5
                                                                    padding(0, 0)
                                                                    action [wnfh_CycleField(wnfh_preferences_text_buttons_states[wnfh_preferences_text_buttons[element][0]][0], wnfh_preferences_text_buttons_states[wnfh_preferences_text_buttons[element][0]][1], wnfh_preferences_text_buttons_states[wnfh_preferences_text_buttons[element][0]][2].keys()), ]
                                                                    background debug_frame["red"]
                                                                    hovered Show("wnfh_preferences_tits", dick = wnfh_button_tits[wnfh_preferences_text_buttons[element][0]])
                                                                    
    
                        frame: # ============================ Третий блок
                            area(0.5, 0.0, 1.0, (wnfh_frames_elements["settings_title_bg"][2] + 10) + len(wnfh_preferences_widget_buttons) * 65)
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["blue"]
                            vbox:
                                pos (0.5, 0.0)
                                xanchor 0.5 yanchor 0.0
                                spacing 0
                                frame: # ======================== Заголовок "Виджеты"
                                    area(0.5, 0.0, wnfh_frames_elements["settings_title_bg"][1] + 40, wnfh_frames_elements["settings_title_bg"][2] + 20)
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
                                                    matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
            
                                    text "Виджеты": # ============================ Виджеты
                                        style "wnfh_title_2_" + renpy.store.wnfh_tymeofday
            
                                frame:
                                    area(0.5, 0.0, 0.9, 250)
                                    xanchor 0.5 yanchor 0.0
                                    background debug_frame["black"]
                                    vbox:
                                        pos (0.5, 0.0)
                                        xanchor 0.5 yanchor 0.0
                                        spacing 0
                                        for element in range(len(wnfh_preferences_widget_buttons)):
                                            frame:
                                                area(0.5, 0.5, 1.0, 57)
                                                xanchor 0.5 yanchor 0.5
                                                background debug_frame["black"]
                                                frame:
                                                    background debug_frame["red"]
                                                    area(0.0, 0.5, 600, 1.0)
                                                    xanchor 0.0 yanchor 0.5
                                                    text wnfh_preferences_widget_buttons[element][1]:
                                                        style "wnfh_text_" + renpy.store.wnfh_tymeofday
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
                                                            for i in range(wnfh_preferences_widget_buttons[element][6]):
                                                                button:
                                                                    area(0.5, 0.5, (wnfh_preferences_widget_buttons[element][5]) / (wnfh_preferences_widget_buttons[element][6]), 1.0)
                                                                    xanchor 0.5 yanchor 0.5
                                                                    padding(0, 0)
                                                                    action ToggleField(persistent, "wnfh_" + wnfh_preferences_widget_buttons[element][0], i, i+1)
                                                                    background debug_frame["red"]
                                                                    hovered Show("wnfh_preferences_tits", dick = wnfh_button_tits[wnfh_preferences_widget_buttons[element][0]])
            
                        
            
                        frame: # ============================ Четвёртый блок
                            area(0.5, 0.0, 1.0, (wnfh_frames_elements["settings_title_bg"][2] + 10) + len(wnfh_preferences_other_buttons) * 65 + 100) 
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["red"]
                            vbox:
                                pos (0.5, 0.0)
                                xanchor 0.5 yanchor 0.0
                                spacing 0
                                frame: # ======================== Заголовок "Прочее"
                                    area(0.5, 0.0, wnfh_frames_elements["settings_title_bg"][1] + 40, wnfh_frames_elements["settings_title_bg"][2] + 20)
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
                                                    matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
            
                                    text "Прочее":
                                        style "wnfh_title_2_" + renpy.store.wnfh_tymeofday
            
                                frame:
                                    area(0.5, 0.0, 0.9, 250)
                                    xanchor 0.5 yanchor 0.0
                                    background debug_frame["black"]
                                    vbox:
                                        pos (0.5, 0.0)
                                        xanchor 0.5 yanchor 0.0
                                        spacing 0
                                        for element in range(len(wnfh_preferences_other_buttons)):
                                            frame:
                                                area(0.5, 0.5, 1.0, 57)
                                                xanchor 0.5 yanchor 0.5
                                                background debug_frame["black"]
                                                frame:
                                                    background debug_frame["red"]
                                                    area(0.0, 0.5, 0.4, 1.0)
                                                    xanchor 0.0 yanchor 0.5
                                                    text wnfh_preferences_other_buttons[element][1]:
                                                        style "wnfh_text_" + renpy.store.wnfh_tymeofday
            
                                                $ pref_current_value = getattr(wnfh_preferences_other_buttons_states[wnfh_preferences_other_buttons[element][0]][0], wnfh_preferences_other_buttons_states[wnfh_preferences_other_buttons[element][0]][1])
                                                $ pref_integer_value = wnfh_preferences_other_buttons_states[wnfh_preferences_other_buttons[element][0]][2][pref_current_value]
                                                frame:
                                                    background debug_frame["blue"]
                                                    area(0.5, 0.5, 0.3, 1.0)
                                                    xanchor 0.5 yanchor 0.5
                                                    text wnfh_preferences_display_labels[wnfh_preferences_other_buttons[element][0]][pref_integer_value]:
                                                        style "wnfh_text_" + renpy.store.wnfh_tymeofday
                                                        size 20
            
                                                frame:
                                                    background debug_frame["green"]
                                                    area(1.0, 0.5, wnfh_preferences_other_buttons[element][5]+12, 1.0)
                                                    xanchor 1.0 yanchor 0.5
                                                    bar value AnimatedValue(pref_integer_value, len(wnfh_preferences_other_buttons_states[wnfh_preferences_other_buttons[element][0]][2]) - 1, 0.1): # wnfh_preferences_other_buttons[element][2]:
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
                                                            for i in range(wnfh_preferences_other_buttons[element][6]):
                                                                button:
                                                                    area(0.5, 0.5, (wnfh_preferences_other_buttons[element][5]) / (wnfh_preferences_other_buttons[element][6]), 1.0)
                                                                    xanchor 0.5 yanchor 0.5
                                                                    padding(0, 0)
                                                                    action [wnfh_CycleField(wnfh_preferences_other_buttons_states[wnfh_preferences_other_buttons[element][0]][0], wnfh_preferences_other_buttons_states[wnfh_preferences_other_buttons[element][0]][1], wnfh_preferences_other_buttons_states[wnfh_preferences_other_buttons[element][0]][2].keys()), ]
                                                                    background debug_frame["red"]
                                                                    hovered Show("wnfh_preferences_tits", dick = wnfh_button_tits[wnfh_preferences_other_buttons[element][0]])
                frame:
                    background debug_frame["green"]
                    area(1.0, 0.5, 50, 1.0)
                    xanchor 0.0 yanchor 0.5
                    vbar value YScrollValue("settings_list"):
                        top_bar Frame(wnfh_bars["bar_null"][0], wnfh_frames_elements["achievements_vbar_null"][1], wnfh_frames_elements["achievements_vbar_null"][1])
                        bottom_bar Frame(wnfh_bars["bar_null"][0], wnfh_frames_elements["achievements_vbar_null"][1], wnfh_frames_elements["achievements_vbar_null"][1])
                        thumb wnfh_bars["tumb"][0]
                        hover_thumb wnfh_bars["tumb"][0]
                        xmaximum 33 ymaximum 1.0
                        pos (0.5, 0.5)
                        anchor (0.5, 0.5)
            frame: # ================================================ ПОДСКАЗКИ
                area (0.811, 0.0, wnfh_frames_elements["achievements_char_list_bg_2"][1] + 40, wnfh_frames_elements["achievements_char_list_bg_2"][2] + 20)
                xanchor 0.5 yanchor 0.0
                background debug_frame["blue"]
                vbox: # ================================================ Фон таблички из трёх кусков
                    pos (0.5, 0.5)
                    xanchor 0.5 yanchor 0.5
                    spacing 0
                    for element in ["achievements_char_list_line", "achievements_char_list_bg_2", "achievements_char_list_line"]:
                        frame at wnfh_frames_elements[element][6]:
                        #frame:
                            if persistent.wnfh_debug_color:
                                background wnfh_frames_elements[element][5]
                            else:
                                background frame_transparent
                            area (0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                            add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
                text "Подсказки":
                    style "wnfh_text_" + renpy.store.wnfh_tymeofday

screen wnfh_preferences_tits(dick):

    $ debug_frame = {
        "black":  frame_black  if persistent.wnfh_debug_color else frame_transparent,
        "red":    frame_red    if persistent.wnfh_debug_color else frame_transparent,
        "green":  frame_green  if persistent.wnfh_debug_color else frame_transparent,
        "blue":   frame_blue   if persistent.wnfh_debug_color else frame_transparent,
        "purple": frame_purpl  if persistent.wnfh_debug_color else frame_transparent
    }

    frame:
        background debug_frame["green"]
        area(0.80, 0.236, 600, 0.702)
        xanchor 0.5 yanchor 0.0
        has vbox
        xalign 0.5
        for part in dick:
            if type(part) is str:
                frame:
                    background debug_frame["red"]
                    xpos 0.5 ypos 0.0
                    xsize 550
                    xanchor 0.5 yanchor 0.0
                    text part:
                        style "wnfh_text_" + renpy.store.wnfh_tymeofday
                        size 15
                        text_align 0.0
                        xalign 0.0
                        
                        
            else:
                add part:
                    xalign 0.5

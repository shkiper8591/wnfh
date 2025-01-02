init -4 python:
    ## Создание листов ##
    
    def wnfh_form_files_list(path):
        return {i[len(path):i.rfind(".")]:i for i in renpy.list_files() if i.startswith(path)}
    
    wnfh_gui = dict()

    """
    Для удобства я разбил список GUI на несколько частей,
    каждая для своего экрана меню.
    
    img - для главного меню
    achievements - меню ачивок
    gallery - галерея
    settings - настройки
    
    Так же в этот список я засунул звук,
    который будет воспроизводиться при наведении на кнопку.
    
    Ну и ссылки сюда же засунул
    """
    wnfh_choice_tint_color = {
        #timeset      #0 текст   #1 рамки   #2 фон     #3 спрайты
        "day":      ["#FFDD7D", "#80A055", "#000000",   None    ], 
        "sunset":   ["#DCD168", "#CDAF69", "#150A0B", "#EFD1FF" ],
        "night":    ["#3CCFA2", "#36B198", "#000A20", "#A1C7D1" ],
        "prologue": ["#98D8DA", "#BEE8E9", "#000A20", "#A1C7D1" ], 
    }
    
    

    #wnfh_gui["frames"] {
    #    #Тег              #Элементы
    #    "yesno_box" [wnfh_gui["frames_elements"]["frame_line"], wnfh_gui["frames_elements"]["frame_bg"], wnfh_gui["frames_elements"]["frame_line"]]
    #}

    wnfh_gui["tint_elements"] = {img:(wnfh_TINT_ELEMENTS + img + ".png") for img in [

        #Элементы кнопок гейм селектора
        "im_bg",
        "im_line",
        "im_gradient",
        #Кнопки
        "button_bg_1",
        "button_bg_2",
        "button_line",
        "button_hover",
        "db_button_mute",
        "db_button_unmute",
        "db_button_minus",
        "db_button_plus",
        "db_button_save",
        "db_button_load",
        "db_button_menu",
        "db_button_hide",
        #Виньетка
        "vignette",
        "frame_bg",
        "frame_line",
        "frame_gradient",
        "frame_db_mid_line",
        "frame_db_brow_line",
        "frame_db_brow_line1",
        "frame_db_brow_line2",
        "frame_db_brow_line3",
        "frame_db_brow_bg",
        "frame_db_brow_bg1",
        "frame_db_brow_bg2",
        "frame_db_brow_bg3",
        "frame_bar_null",
        "frame_bar_full",
        "frame_bar_bg",
        "frame_bar_tumb",
        #Серп и молот и звезда
        "indicator_star",
        "indicator_molot",
        "indicator_serp",

    ]}

    wnfh_frames_elements = {
        #Тег                                      #0 Файл                                           #1 Ширина      #В2 высота   #3 Отступ слева    #4 Цветокор    #5 Цвет фрейма    #6 Анимация
        "yesno_prompt_box_bg":                    [wnfh_gui["tint_elements"]["frame_bg"]            ,1000          ,200         ,25                ,2             ,frame_red        ,wjuh_bg],
        "yesno_prompt_box_line":                  [wnfh_gui["tint_elements"]["frame_line"]          ,1020          ,4           ,22                ,1             ,frame_green      ,wjuh_line],
        "yesno_prompt_button_bg":                 [wnfh_gui["tint_elements"]["frame_bg"]            ,250           ,60          ,25                ,2             ,frame_red        ,wjuh_bg],
        "yesno_prompt_button_line":               [wnfh_gui["tint_elements"]["frame_line"]          ,270           ,4           ,22                ,1             ,frame_green      ,wjuh_line],
        "yesno_prompt_button_gradient":           [wnfh_gui["tint_elements"]["frame_gradient"]      ,250           ,60          ,25                ,0             ,frame_red        ,wjuh_bg],
        "game_menu_selector_button_bg":           [wnfh_gui["tint_elements"]["frame_bg"]            ,480           ,50          ,25                ,2             ,frame_red        ,wjuh_bg],
        "game_menu_selector_button_line":         [wnfh_gui["tint_elements"]["frame_line"]          ,500           ,4           ,22                ,1             ,frame_green      ,wjuh_line],
        "game_menu_selector_button_gradient":     [wnfh_gui["tint_elements"]["frame_gradient"]      ,480           ,50          ,25                ,0             ,frame_red        ,wjuh_bg],
        "widget_lp_box_bg":                       [wnfh_gui["tint_elements"]["frame_bg"]            ,1700          ,100         ,25                ,2             ,frame_red        ,wjuh_bg],
        "widget_lp_box_line":                     [wnfh_gui["tint_elements"]["frame_line"]          ,1720          ,4           ,22                ,1             ,frame_green      ,wjuh_line],
        "widget_clock_box_bg":                    [wnfh_gui["tint_elements"]["frame_bg"]            ,140           ,50          ,25                ,2             ,frame_red        ,wjuh_bg],
        "widget_clock_box_line":                  [wnfh_gui["tint_elements"]["frame_line"]          ,160           ,4           ,22                ,1             ,frame_green      ,wjuh_line],
        "widget_music_box_bg":                    [wnfh_gui["tint_elements"]["frame_bg"]            ,860           ,50          ,25                ,2             ,frame_red        ,wjuh_bg],
        "widget_music_box_line":                  [wnfh_gui["tint_elements"]["frame_line"]          ,880           ,4           ,22                ,1             ,frame_green      ,wjuh_line],
        "ach_box_bg":                             [wnfh_gui["tint_elements"]["frame_bg"]            ,820           ,100         ,25                ,2             ,frame_red        ,wjuh_bg],
        "ach_box_line":                           [wnfh_gui["tint_elements"]["frame_line"]          ,840           ,4           ,22                ,1             ,frame_green      ,wjuh_line],
        "db_line_lower":                          [wnfh_gui["tint_elements"]["frame_line"]          ,1500          ,4           ,22                ,1             ,frame_green      ,wjuh_line],
        "db_bg":                                  [wnfh_gui["tint_elements"]["frame_bg"]            ,1500          ,100         ,25                ,2             ,frame_green      ,[wnfh_db_red_small,wnfh_db_red_large,None]],
        "db_mid_line":                            [wnfh_gui["tint_elements"]["frame_db_mid_line"]   ,840           ,4           ,22                ,1             ,frame_green      ,[wnfh_db_green_small,wnfh_db_green_large,None]],
        "db_brow_line":                           [wnfh_gui["tint_elements"]["frame_db_brow_line"]  ,360           ,35          ,25                ,1             ,frame_green      ,wnfh_pass],
        "db_brow_line1":                          [wnfh_gui["tint_elements"]["frame_db_brow_line1"] ,25            ,35          ,0                 ,1             ,frame_green      ,wnfh_pass],
        "db_brow_line2":                          [wnfh_gui["tint_elements"]["frame_db_brow_line2"] ,300           ,35          ,2                 ,1             ,frame_green      ,wnfh_pass],
        "db_brow_line3":                          [wnfh_gui["tint_elements"]["frame_db_brow_line3"] ,55            ,35          ,0                 ,1             ,frame_green      ,wnfh_pass],
        "db_brow_bg":                             [wnfh_gui["tint_elements"]["frame_db_brow_bg"]    ,360           ,35          ,25                ,2             ,frame_green      ,wnfh_pass],
        "db_brow_bg1":                            [wnfh_gui["tint_elements"]["frame_db_brow_bg1"]   ,25            ,35          ,0                 ,2             ,frame_green      ,wnfh_pass],
        "db_brow_bg2":                            [wnfh_gui["tint_elements"]["frame_db_brow_bg2"]   ,220           ,35          ,2                 ,2             ,frame_green      ,[wnfh_db_blue_small,wnfh_db_blue_large,None]],
        "db_brow_bg3":                            [wnfh_gui["tint_elements"]["frame_db_brow_bg3"]   ,55            ,35          ,0                 ,2             ,frame_green      ,wnfh_pass],
        "back_button_line":                       [wnfh_gui["tint_elements"]["frame_line"]          ,170           ,4           ,22                ,1             ,frame_red        ,wnfh_pass],
        "back_button_bg":                         [wnfh_gui["tint_elements"]["frame_bg"]            ,150           ,50          ,25                ,2             ,frame_green      ,wnfh_pass],
        "back_button_gradient":                   [wnfh_gui["tint_elements"]["frame_bg"]            ,150           ,50          ,25                ,0             ,frame_red        ,wnfh_pass],
        
        "settings_bar_null":                      [wnfh_gui["tint_elements"]["frame_bar_null"]      ,40            ,40          ,13                ,1             ,frame_green      ,wnfh_pass],
        "settings_bar_full":                      [wnfh_gui["tint_elements"]["frame_bar_full"]      ,40            ,40          ,13                ,0             ,frame_green      ,wnfh_pass],
        "settings_bar_bg":                        [wnfh_gui["tint_elements"]["frame_bar_bg"]        ,40            ,40          ,13                ,2             ,frame_green      ,wnfh_pass],
        "settings_bar_tumb":                      [wnfh_gui["tint_elements"]["frame_bar_tumb"]      ,40            ,40          ,5                 ,1             ,frame_green      ,wnfh_pass],
        "settings_main_title_bg":                 [wnfh_gui["tint_elements"]["frame_bg"]            ,880           ,140         ,25                ,2             ,frame_red        ,wnfh_pass],
        "settings_main_title_line":               [wnfh_gui["tint_elements"]["frame_line"]          ,900           ,4           ,22                ,1             ,frame_green      ,wnfh_pass],
        "settings_box_bg":                        [wnfh_gui["tint_elements"]["frame_bg"]            ,1860          ,850         ,25                ,2             ,frame_black      ,wjuh_bg],
        "settings_box_line":                      [wnfh_gui["tint_elements"]["frame_line"]          ,1880          ,4           ,22                ,1             ,frame_green      ,wjuh_line],
        "settings_title_bg":                      [wnfh_gui["tint_elements"]["frame_bg"]            ,660           ,70          ,25                ,2             ,frame_red        ,wnfh_pass],
        "settings_title_line":                    [wnfh_gui["tint_elements"]["frame_line"]          ,680           ,4           ,22                ,1             ,frame_green      ,wnfh_pass],
        









    }
    wnfh_frames_size = {
        "test_frame": [1000]  
    }
    # Для главного меню
    wnfh_gui["main_menu"] = {img:(wnfh_MAIN_MENU + img + ".png") for img in [
        "mm_bg",
        "mm_bg2",
        "mm_bg4",
        "gradient",
        "achievements",
        "discord",
        "seledka",
        "steam",
        "vk",
        "exit"
        ]}
    
    # Для главного меню
    wnfh_gui["save_load"] = {img:(wnfh_SAVELOAD + img + ".png") for img in [
        "back_idle",
        "back_hover",
        "delete_idle",
        "delete_hover",
        "load_game_idle",
        "load_game_hover",
        "load_logo",
        "load_button_idle",
        "load_button_hover",
        "load_button_selected",
        "saves_idle",
        "saves_hover",
        "settings_idle",
        "settings_hover",
        "auto_idle",
        "auto_hover",
        "1_idle",
        "1_hover",
        "2_idle",
        "2_hover",
        "3_idle",
        "3_hover",
        "4_idle",
        "4_hover",
        "5_idle",
        "5_hover",
        "6_idle",
        "6_hover",
        "7_idle",
        "7_hover",
        "8_idle",
        "8_hover",
        "9_idle",
        "9_hover",
    ]}

    wnfh_gui["settings"] = {img:(wnfh_SETTINGS + img + ".png") for img in [
        "return",
        "base",
        "pref_title",
        "bar_full",
        "bar_null",
        "htumb",
        "line",
        "on",
        "off",
        "triple_off",
        "triple_on1",
        "triple_on2",
        "hentai",
        "hentai_off",
        "hentai_on",
    ]}
    
    wnfh_gui["poligon"] = {img:(wnfh_IMAGES + "hentai/" + img + ".png") for img in [
        "red",
    ]}
    
    wnfh_gui["achievements"] = {img:(wnfh_ACHIEVEMENTS + img + ".png") for img in [
        "back",
        "payday",
        "spirt",
        "bkrr",
        "alpha-0.1",
        "post",
        "zgdun",
        "alarm",
        "zaebist",
        "handass",
    ]}

    

    characters_banners_idle = [
        "ach_kat_idle",
        "ach_un_idle",
        "ach_mi_idle",
        "ach_usw_idle",
        "ach_dv_idle",
        "ach_sl_idle",
        "ach_sv_idle",
        "ach_mt_idle",
        "ach_me_idle"
    ]
    characters_banners_hover = [
        "ach_kat_hover",
        "ach_un_hover",
        "ach_mi_hover",
        "ach_usw_hover",
        "ach_dv_hover",
        "ach_sl_hover",
        "ach_sv_hover",
        "ach_mt_hover",
        "ach_me_hover",
    ]
    wnfh_gui["banners"] = {img:(wnfh_BANNERS + img + ".png") for img in [
        
        "relation_frame",
        "relation_up",
        "relation_down",
        "relation_neutral",
        "ach_frame",
        "ach_frame_1_1",
        "ach_frame_1_2",
        "ach_menu_frame",
        "ach_menu_frame_lock",
        "trophy_bronz",
        "trophy_silver",
        "trophy_gold",
        "trophy_platina",
        "trophy_white",
        "kit"
        
        #Тут срез для ачивок в файле wnfh_achievements_menu
        ] + characters_banners_idle + characters_banners_hover
        }
    wnfh_ach_list = {
        #Тэг ачивки  #0 Иконка                              #1 Заголовк              #2 Подпись                          #3 Трофей                                #4 Персонаж
        "payday":   [wnfh_gui["achievements"]["payday"]    ,"Конфетный вор"         ,"Было весело"                      ,wnfh_gui["banners"]["trophy_silver"]    ,"usw"           ],
        "spirt":    [wnfh_gui["achievements"]["spirt"]     ,"Где мне найти спирт?"  ,"Живая вода"                       ,wnfh_gui["banners"]["trophy_silver"]    ,"usw"           ],   
        "bkrr":     [wnfh_gui["achievements"]["bkrr"]      ,"Да, это именно то, о чём ты подумал"            ,"Это отсылка на\n«Булки, Кефир, Рок-н-ролл»"              ,wnfh_gui["banners"]["trophy_bronz"]     ,"kat"           ],     
        "post":     [wnfh_gui["achievements"]["post"]      ,"Груз доставлен"        ,"Почти без повреждений"            ,wnfh_gui["banners"]["trophy_bronz"]     ,"kat"           ],       
        "alarm":    [wnfh_gui["achievements"]["alarm"]     ,"Das Boot"              ,"Доплавался, блин"                 ,wnfh_gui["banners"]["trophy_silver"]    ,"kat"           ],
        "zaebist":  [wnfh_gui["achievements"]["zaebist"]   ,"Всё идёт по плану"     ,"При коммунизме всё будет заебись" ,wnfh_gui["banners"]["trophy_silver"]    ,"kat"           ],
        "handass":  [wnfh_gui["achievements"]["handass"]   ,"Рукожоп"               ,"Ну как так-то?"                   ,wnfh_gui["banners"]["trophy_bronz"]     ,"kat"           ],
    }
    # Аватарки
    wnfh_gui["avatars"] = {img:(wnfh_AVATARS + img + ".png") for img in [
        "me",
        "mi",
        "usw",
        "dv",
        "mt",
        "mz",
        "sh",
        "sl",
        "el",
        "un",
        "din",
        "kat",
        "sv",
    ]}

    # Для галереи
    wnfh_gui["gallery"] = {img:(wnfh_GALLERY + img + ".png") for img in [
        "back",
    ]}
    
    # Звук кнопки
    wnfh_gui["sound"] = {
        "plimp": wnfh_SFX + "plimp.ogg",
    }

    # Ссылки в Сибирь
    wnfh_gui["hyperlinks"] = {
        "vk":"https://vk.com/wnfh",
        #"steam":""
        #"discord":""
    }
    
    
    """
    Тут у нас всё в тот же список пихаются уже транзиты.
    Это специальные градиенты, за счёт которых работают переходы между фонами.
    
    Если кому-то интересно как это работает:
    Находишь в папке мода, папку transitions (надеюсь ты не тупой, найдёшь)
    В ней лежат градиенты.
    Переход работает от белого к чёрному. Там валяется ещё пара эксперементальных переходов.
    Можно насрать абсолютно любыми Ч/Б картинками и сделать из этого переход, тут ограничивает только фантазия.
    
    А сами переходы прописаны уже в файле wnfh_transitions.rpy
    """
    
    # Транзиты
    wnfh_gui["transit"] = {img:(wnfh_TRANSITIONS + img + ".png") for img in [
        "slide_left",
        "slide_right",
        "slide_up",
        "slide_down",
        "sphere",
        "sphere_invert",
        "door",
        "door_invert",
        "clock_r",
        "slide_diagonal",
        "santa_barbara_in",
        "santa_barbara_out",
        "exp1",
        "exp2",
        "exp3",
        "ecstrusion",
        "bibl_entrance",
        "dnr_entrance",
        "001",
        "005",
        "007",
        "008",
        "009",
        "011",
        "015",
        "016",
        "017",
        "018",
        "020",
        "021",
        "024",
        "030",
        "032",
        "033",
        "034",
        "037",
        "039",
        "040"
    ]}
    
    ## Это элементы меню воборов ##
    
    wnfh_gui["choice"] = {img:(wnfh_CHOICE + img + ".png") for img in [
        "vignette",
        "bg",
        "line",
        "gradient"
    ]}

    

init 1:
    
    
    ## Видео Лист
    $ wnfh_video_list = {
        "intro":wnfh_VIDEO + "intro.webm",
        "pegi":wnfh_VIDEO + "pegi.webm",
    }
    
    $ wnfh_video_list["backdrop"] = {dn:(wnfh_VIDEO + "backdrop_day_" + str(dn) + ".webm") for dn in range(1, 14)}
    $ wnfh_video_list["backdrop"]["test"] = wnfh_VIDEO + "backdrop_test.webm"
    
    image null = Null(0, 0) # Я не ебу что это, не помню нахуй это писал, но пусть будет

    $ wnfh_sfx_list = wnfh_form_files_list(wnfh_SFX)
    $ wnfh_music_list = wnfh_form_files_list(wnfh_MUSIC)
    $ wnfh_ambience_list = wnfh_form_files_list(wnfh_AMBIENCE)
    
    # SFX Лист   
    $ wnfh_sfx_list["ps4_ach"]                                  = wnfh_SFX + "ps4_ach.ogg"
    $ wnfh_sfx_list["plimp"]                                    = wnfh_SFX + "plimp.ogg"
    $ wnfh_sfx_list["plimp2"]                                   = wnfh_SFX + "plimp2.ogg"
    $ wnfh_sfx_list["nya"]                                      = wnfh_SFX + "nya.ogg"
    $ wnfh_sfx_list["nos"]                                      = wnfh_SFX + "nos.ogg"
    $ wnfh_sfx_list["guitar_hit"]                               = wnfh_SFX + "guitar_hit.ogg"
    $ wnfh_sfx_list["samogonshiki"]                             = wnfh_SFX + "samogonshiki.ogg"
    $ wnfh_sfx_list["meow_yes"]                                 = wnfh_SFX + "meow yes.ogg"
    $ wnfh_sfx_list["meow_no"]                                  = wnfh_SFX + "meow no.ogg"
    $ wnfh_sfx_list["murchanie"]                                = wnfh_SFX + "murchanie.ogg"
    $ wnfh_sfx_list["raschyoska"]                               = wnfh_SFX + "brushing-hair.ogg"
    $ wnfh_sfx_list["udarch"]                                   = wnfh_SFX + "udarch.ogg"
    $ wnfh_sfx_list["pickup_sound"]                             = wnfh_SFX + "pickup sound.ogg"
    $ wnfh_sfx_list["hrust_vetki"]                              = wnfh_SFX + "hrust_vetki.ogg"
    $ wnfh_sfx_list["pechka"]                                   = wnfh_SFX + "furnace_loop.ogg"
    $ wnfh_sfx_list["apchhi"]                                   = wnfh_SFX + "apchhi.ogg"
    $ wnfh_sfx_list["oskolki"]                                  = wnfh_SFX + "oskolki.ogg"
    $ wnfh_sfx_list["zastelayut"]                               = wnfh_SFX + "bed-sheet-movement.ogg"
    $ wnfh_sfx_list["postavilichtoto"]                          = wnfh_SFX + "postavilichtoto.ogg"
    $ wnfh_sfx_list["perelistovanie"]                           = wnfh_SFX + "perelistovanie.ogg"
    $ wnfh_sfx_list["microphone"]                               = wnfh_SFX + "micro.ogg"
    $ wnfh_sfx_list["pogrom"]                                   = wnfh_SFX + "zvuk-padeniya-na-mebel-i-pogrom.ogg"
    $ wnfh_sfx_list["selyodka_po_steklu"]                       = wnfh_SFX + "tryot-po-steklu.ogg"
    $ wnfh_sfx_list["stuk_po_steklu"]                           = wnfh_SFX + "glazed_knock_x1.ogg"
    $ wnfh_sfx_list["vsplesk_vodi"]                             = wnfh_SFX + "silnyiy-vsplesk-ot-nyiryaniya-cheloveka.ogg"
    $ wnfh_sfx_list["vsplesk_vodi_2"]                           = wnfh_SFX + "mgnovennyiy-nezametnyiy-vsplesk.ogg"
    $ wnfh_sfx_list["vsplesk_vodi_3"]                           = wnfh_SFX + "kratkiy-tyajelyiy-vsplesk-vodyi.ogg"
    $ wnfh_sfx_list["vibili_steklo"]                            = wnfh_SFX + "vibili steklo.ogg"
    $ wnfh_sfx_list["otryahivanie"]                             = wnfh_SFX + "cloth-fluff-pillow_mkznd5vd.ogg"
    $ wnfh_sfx_list["stop_magnitofon"]                          = wnfh_SFX + "stop_magnitofon.ogg"
    $ wnfh_sfx_list["bucket_water_hit"]                         = wnfh_SFX + "bucket_water_hit.ogg"
    $ wnfh_sfx_list["cardboard_box_drop"]                       = wnfh_SFX + "cardboard-box-drop.ogg"
    $ wnfh_sfx_list["slow_helicopter_loop"]                     = wnfh_SFX + "slow-helicopter-loop.ogg"
    $ wnfh_sfx_list["budilnik"]                                 = wnfh_SFX + "budilnik.ogg"
    #$ wnfh_sfx_list[""] = wnfh_SFX + ".ogg"
    
    
    # MUSIC Лист
    $ wnfh_music_list["technical_chocolatki"]                   = wnfh_MUSIC + "technical_chocolatki.mp3"
    $ wnfh_music_list["angus_climbs_the_hill"]                  = wnfh_MUSIC + "Alec Holowka - Angus Climbs the Hill.mp3"
    $ wnfh_music_list["church_hill"]                            = wnfh_MUSIC + "Alec Holowka - Church Hill.mp3"
    $ wnfh_music_list["crimes"]                                 = wnfh_MUSIC + "Alec Holowka - Crimes.mp3"
    $ wnfh_music_list["crimes_2"]                               = wnfh_MUSIC + "Alec Holowka - Crimes2.mp3"
    $ wnfh_music_list["greggs_woods"]                           = wnfh_MUSIC + "Alec Holowka - Gregg's Woods.mp3"
    $ wnfh_music_list["im_going_to_break_something"]            = wnfh_MUSIC + "Alec Holowka - I'm Going to Break Something.mp3"
    $ wnfh_music_list["library_investigations"]                 = wnfh_MUSIC + "Alec Holowka - Library Investigations.mp3"
    $ wnfh_music_list["lori_m"]                                 = wnfh_MUSIC + "Alec Holowka - Lori M.mp3"
    $ wnfh_music_list["lost_woods"]                             = wnfh_MUSIC + "Alec Holowka - Lost Woods.mp3"
    $ wnfh_music_list["maes_house_2"]                           = wnfh_MUSIC + "Alec Holowka - Mae's House 2.mp3"
    $ wnfh_music_list["mystery"]                                = wnfh_MUSIC + "Alec Holowka - Mystery.mp3"
    $ wnfh_music_list["outskirts"]                              = wnfh_MUSIC + "Alec Holowka - Outskirts.mp3"
    $ wnfh_music_list["the_bridge"]                             = wnfh_MUSIC + "Alec Holowka - The Bridge.mp3"
    $ wnfh_music_list["waking_up"]                              = wnfh_MUSIC + "Wnfh - Sunrise.mp3"                                                  ## НАШЕ ##
    $ wnfh_music_list["waking_up_2"]                            = wnfh_MUSIC + "Alec Holowka - Waking up 2.mp3"
    $ wnfh_music_list["fireflies_on_the_porch"]                 = wnfh_MUSIC + "Alec Holowka - Fireflies on the Porch.mp3"
    $ wnfh_music_list["the_cars_you_might_think"]               = wnfh_MUSIC + "The Cars - You Might Think.ogg"
    $ wnfh_music_list["proximity"]                              = wnfh_MUSIC + "Alec Holowka - Proximity.mp3"
    $ wnfh_music_list["we_dont_care"]                           = wnfh_MUSIC + "We Dont Care.ogg"
    $ wnfh_music_list["sharkle_dream"]                          = wnfh_MUSIC + "Alec Holowka - Sharkle Dream.mp3"
    $ wnfh_music_list["the_hole_at_the_center_of_everything"]   = wnfh_MUSIC + "Alec Holowka - The Hole At The Center Of Everything.mp3"
    $ wnfh_music_list["major_grom"]                             = wnfh_MUSIC + "Move Like A Devil.mp3"
    $ wnfh_music_list["ratne_igre"]                             = wnfh_MUSIC + "Kerber - Ratne Igre.mp3"
    $ wnfh_music_list["international"]                          = wnfh_MUSIC + "international.mp3"
    $ wnfh_music_list["strange"]                                = wnfh_MUSIC + "strange.ogg"
    $ wnfh_music_list["major_grom_2"]                           = wnfh_MUSIC + "ya znayu kto ti.mp3"
    $ wnfh_music_list["santa_barbara"]                          = wnfh_MUSIC + "santa barbara music.mp3"
    $ wnfh_music_list["back_in_black"]                          = wnfh_MUSIC + "AC-DC - Back in black.mp3"
    $ wnfh_music_list["dance_of_the_moonlight_jellies"]         = wnfh_MUSIC + "ConcernedApe - Dance of the Moonlight Jellies.mp3"
    $ wnfh_music_list["distant_banjo"]                          = wnfh_MUSIC + "ConcernedApe - Distant Banjo.mp3"
    $ wnfh_music_list["in_the_deep_woods"]                      = wnfh_MUSIC + "ConcernedApe - In the Deep Woods.mp3"
    $ wnfh_music_list["pleasant_memory"]                        = wnfh_MUSIC + "ConcernedApe - Pleasant Memory (Penny's Theme).mp3"
    $ wnfh_music_list["tropicala"]                              = wnfh_MUSIC + "ConcernedApe - Summer (Tropicala).mp3"
    $ wnfh_music_list["schabernack"]                            = wnfh_MUSIC + "Laryssa Okada - Dorfromantik - Schabernack.mp3"
    $ wnfh_music_list["schoneweide"]                            = wnfh_MUSIC + "Laryssa Okada - Dorfromantik - Schöneweide.mp3"
    $ wnfh_music_list["big_fish"]                               = wnfh_MUSIC + "Max LL - Big Fish.mp3"
    $ wnfh_music_list["crows_end"]                              = wnfh_MUSIC + "Max LL - Crow's End.mp3"
    $ wnfh_music_list["northern_waters"]                        = wnfh_MUSIC + "Max LL - Northern Waters (Night).mp3"
    $ wnfh_music_list["pulsar_pursuit"]                         = wnfh_MUSIC + "Max LL - Pulsar Pursuit.mp3"
    $ wnfh_music_list["rain"]                                   = wnfh_MUSIC + "Max LL - Rain.mp3"
    $ wnfh_music_list["shallow_waters_night"]                   = wnfh_MUSIC + "Max LL - Shallow Waters (Night).mp3"
    $ wnfh_music_list["the_swarms_of_hades"]                    = wnfh_MUSIC + "Max LL - The Swarms of Hades.mp3"
    $ wnfh_music_list["razbor_poletov"]                         = wnfh_MUSIC + "razbor poletov - svati.mp3"                                  
    $ wnfh_music_list["trevoga_1"]                              = wnfh_MUSIC + "Wnfh - Sense of anxiety.mp3"                                         ## НАШЕ ##
    $ wnfh_music_list["sport2"]                                 = wnfh_MUSIC + "sport2 - svati.mp3"
    $ wnfh_music_list["estafeta"]                               = wnfh_MUSIC + "estafeta - svati.mp3" 
    $ wnfh_music_list["country_shop"]                           = wnfh_MUSIC + "ConcernedApe - Country Shop.mp3"
    $ wnfh_music_list["ya_znayu_kto_ti"]                        = wnfh_MUSIC + "ya znayu kto ti.mp3"
    $ wnfh_music_list["candy_store"]                            = wnfh_MUSIC + "Candy_store.mp3"
    $ wnfh_music_list["hide_and_seek"]                          = wnfh_MUSIC + "Sergey Eybog - Hide and Seek.mp3"
    $ wnfh_music_list["warm_evening"]                           = wnfh_MUSIC + "Sergey Eybog - Warm Evening.mp3"
    $ wnfh_music_list["paranoid"]                               = wnfh_MUSIC + "Black Sabbath - Paranoid.mp3"
    $ wnfh_music_list["rainy_day"]                              = wnfh_MUSIC + "Alec Holowka - Rainy Day.mp3"
    $ wnfh_music_list["god"]                                    = wnfh_MUSIC + "Alec Holowka - God.mp3"
    $ wnfh_music_list["lost_man"]                               = wnfh_MUSIC + "_Blacksmith_ - The Lost Man.mp3"
    $ wnfh_music_list["old_manor"]                              = wnfh_MUSIC + "_Blacksmith_ - The Old Manor.mp3"
    $ wnfh_music_list["hill_camp"]                              = wnfh_MUSIC + "_Blacksmith_ - The Hill Camp.mp3"
    $ wnfh_music_list["friends_of_the_deceased_moon"]           = wnfh_MUSIC + "_Blacksmith_ - Friends of the Deceased Moon.mp3"
    $ wnfh_music_list["angus_at_home"]                          = wnfh_MUSIC + "Alec Holowka - Angus at Home.mp3"
    $ wnfh_music_list["the_hill_camp_morning"]                  = wnfh_MUSIC + "_Blacksmith_ - The Hill Camp Morning.mp3"
    $ wnfh_music_list["clean_up"]                               = wnfh_MUSIC + "Clean up.mp3"
    $ wnfh_music_list["dealing_with_destruction"]               = wnfh_MUSIC + "Dealing With Destruction.mp3"
    $ wnfh_music_list["corridors"]                              = wnfh_MUSIC + "Corridors.mp3"
    $ wnfh_music_list["violin_solo"]                            = wnfh_MUSIC + "ConcernedApe - Violin Solo.mp3"
    $ wnfh_music_list["the_valley_comes_alive"]                 = wnfh_MUSIC + "ConcernedApe - Spring (The Valley Comes Alive).mp3"
    $ wnfh_music_list["the_sun_can_bend_an_orange_sky"]         = wnfh_MUSIC + "ConcernedApe - Summer (The Sun Can Bend an Orange Sky).mp3"
    $ wnfh_music_list["greenhouse"]                             = wnfh_MUSIC + "_Blacksmith_ - The Greenhouse.mp3"
    $ wnfh_music_list["magicians_assistant"]                    = wnfh_MUSIC + "_Blacksmith_ - Magicians Assistant.mp3"
    $ wnfh_music_list["kat_theme_background"]                   = wnfh_MUSIC + "Wnfh - Katya theme(background).mp3"
    $ wnfh_music_list["kat_theme_orchestra"]                    = wnfh_MUSIC + "Wnfh - Katya theme(orchestra).mp3"
    $ wnfh_music_list["kat_theme_retro"]                        = wnfh_MUSIC + "Wnfh - Katya theme(retro).mp3"
    $ wnfh_music_list["emotional_indie_guitar"]                 = wnfh_MUSIC + "_Blacksmith_ - Emotional Indie Guitar Chords.mp3"
    $ wnfh_music_list["wnfh_morning_1"]                         = wnfh_MUSIC + "Wnfh - Morning in Sovyonok.mp3"
    $ wnfh_music_list["wnfh_early_awakening_1"]                 = wnfh_MUSIC + "Wnfh - Early Awakening1.mp3"
    $ wnfh_music_list["time_to_say_goodbye"]                    = wnfh_MUSIC + "Wnfh - Time to say goodbye.mp3"
    $ wnfh_music_list["good_morning_1"]                         = wnfh_MUSIC + "Wnfh - Good morning!1.mp3"
    $ wnfh_music_list["the_historical_society"]                 = wnfh_MUSIC + "Alec Holowka - The Historical Society.mp3"
    $ wnfh_music_list["i_wanna_rock"]                           = wnfh_MUSIC + "Twisted_Sister_-_I_Wanna_Rock.mp3"
    $ wnfh_music_list["kinda_scary"]                            = wnfh_MUSIC + "Kinda Scary(1).mp3"
    $ wnfh_music_list["emotional_one"]                          = wnfh_MUSIC + "Such an emotional one.mp3"
    $ wnfh_music_list["chilling_out"]                           = wnfh_MUSIC + "Chillin' Out.mp3"
    $ wnfh_music_list["chill_morning_1"]                        = wnfh_MUSIC + "Wnfh - that is what weekday mornings feel like.mp3"
    $ wnfh_music_list["this_one_sounds_sad"]                    = wnfh_MUSIC + "Wnfh - this one sounds sad.mp3"
    $ wnfh_music_list["argument"]                               = wnfh_MUSIC + "Wnfh - argument.mp3"
    #$ wnfh_music_list[""] = wnfh_MUSIC + ".mp3"
    
    
    # AMBIENCE Лист
    $ wnfh_ambience_list["thunder1"]                            = wnfh_AMBIENCE + "back_ambience_litethunders1.mp3"
    $ wnfh_ambience_list["thunder2"]                            = wnfh_AMBIENCE + "back_ambience_litethunders2.mp3"
    $ wnfh_ambience_list["underwater1"]                         = wnfh_AMBIENCE + "ambience_int_silence.mp3"
    $ wnfh_ambience_list["underwater2"]                         = wnfh_AMBIENCE + "koshmar_water.mp3"
    $ wnfh_ambience_list["beach1"]                              = wnfh_AMBIENCE + "beach_1_6.mp3"
    $ wnfh_ambience_list["beach_children"]                      = wnfh_AMBIENCE + "beach_children.mp3"
    $ wnfh_ambience_list["water_stream"]                        = wnfh_AMBIENCE + "water_stream_closer.mp3"
    $ wnfh_ambience_list["water_drop"]                          = wnfh_AMBIENCE + "water_drop.mp3"
    $ wnfh_ambience_list["rain_night"]                          = wnfh_AMBIENCE + "ambience_rain_night.mp3"
    $ wnfh_ambience_list["rain"]                                = wnfh_AMBIENCE + "rain.mp3"
    $ wnfh_ambience_list["rain_in_building"]                    = wnfh_AMBIENCE + "rain_in_building.mp3"
    $ wnfh_ambience_list["dush"]                                = wnfh_AMBIENCE + "ambience_showers.mp3"
    $ wnfh_ambience_list["heartbeating"]                        = wnfh_AMBIENCE + "heartbeating.mp3"
    $ wnfh_ambience_list["skvoznyak"]                           = wnfh_AMBIENCE + "skvoznyak.mp3"
    $ wnfh_ambience_list["salute"]                              = wnfh_AMBIENCE + "ambience_salute.mp3"
    $ wnfh_ambience_list["veter_v_pole"]                        = wnfh_AMBIENCE + "veter-v-pole.mp3"
    $ wnfh_ambience_list["ambience_int_old_building"]           = wnfh_AMBIENCE + "ambience_int_old_building.mp3"
    #$ wnfh_ambience_list[""] = wnfh_AMBIENCE + ".mp3"
    
    ## Рандомизация мявков
    $ wnfh_meow_list = [wnfh_sfx_list[i] for i in wnfh_sfx_list.keys() if i.startswith("meow")]
    
    image cg d12_guitar_hit_wnfh:
        contains:
            "bg int_musclub_day"
        contains:
            "bg int_musclub_day_blur_wnfh"
            alpha 0.0
            linear 2.0 alpha 1.0
        contains:
            (wnfh_OTHER + "d12_mi_hit_wnfh.png")
            pos(0.75, 0.5)
            anchor(0.5, 0.5)
            linear 3.4 pos(0.5, 0.5)
            linear 0.1 zoom 1.33
        contains:
            "white"
            alpha 0.0
            pause 3.45
            linear 0.05 alpha 1.0

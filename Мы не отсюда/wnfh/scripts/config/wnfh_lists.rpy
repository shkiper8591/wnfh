init 1000 python:
    if debag_switch:
        config.developer = True

init -2 python:

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
        #timeset      #текст     #рамки     #фон
        "day":      ["#FFDD7D", "#80A055", "#000000" ], 
        "sunset":   ["#DCD168", "#CDAF69", "#150A0B" ],
        "night":    ["#3CCFA2", "#36B198", "#000A20" ],
        "prologue": ["#98D8DA", "#BEE8E9", "#000A20" ], 
    }
    
    # Для главного меню
    wnfh_gui["main_menu"] = {img:(wnfh_MAIN_MENU + img + ".png") for img in [
        "mm_bg",
        "mm_bg2",
        "gradient",
        "achievements",
        "discord",
        "seledka",
        "steam",
        "vk",
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
        ]}  
    # Всплывашки
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
        "trophy_white"
        
        #Тут срез для ачивок в файле wnfh_achievements_menu
        ] + characters_banners_idle + characters_banners_hover
        }
    
    
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
        "clock_l",
        "clock_r",
        "slide_diagonal",
        "santa_barbara_in",
        "santa_barbara_out",
        "exp1",
        "exp2",
        "exp3",
        "ecstrusion",
        "bibl_entrance",
        "dnr_entrance"
        ]}
    
    ## Это элементы меню воборов ##
    
    wnfh_gui["choice"] = {img:(wnfh_CHOICE + img + ".png") for img in [
        "vignette",
        "bg",
        "line",
        "gradient"
        ]}

init 2:
    
    
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
    $ wnfh_sfx_list["ps4_ach"] = wnfh_SFX + "ps4_ach.ogg"
    $ wnfh_sfx_list["plimp"] = wnfh_SFX + "plimp.ogg"
    $ wnfh_sfx_list["plimp2"] = wnfh_SFX + "plimp2.ogg"
    $ wnfh_sfx_list["nya"] = wnfh_SFX + "nya.ogg"
    $ wnfh_sfx_list["nos"] = wnfh_SFX + "nos.ogg"
    $ wnfh_sfx_list["guitar_hit"] = wnfh_SFX + "guitar_hit.ogg"
    $ wnfh_sfx_list["samogonshiki"] = wnfh_SFX + "samogonshiki.ogg"
    $ wnfh_sfx_list["meow_yes"] = wnfh_SFX + "meow yes.ogg"
    $ wnfh_sfx_list["meow_no"] = wnfh_SFX + "meow no.ogg"
    $ wnfh_sfx_list["murchanie"] = wnfh_SFX + "murchanie.ogg"
    $ wnfh_sfx_list["raschyoska"] = wnfh_SFX + "brushing-hair.ogg"
    $ wnfh_sfx_list["udarch"] = wnfh_SFX + "udarch.ogg"
    $ wnfh_sfx_list["pickup_sound"] = wnfh_SFX + "pickup sound.ogg"
    $ wnfh_sfx_list["hrust_vetki"] = wnfh_SFX + "hrust_vetki.ogg"
    $ wnfh_sfx_list["pechka"] = wnfh_SFX + "furnace_loop.ogg"
    $ wnfh_sfx_list["apchhi"] = wnfh_SFX + "apchhi.ogg"
    $ wnfh_sfx_list["oskolki"] = wnfh_SFX + "oskolki.ogg"
    $ wnfh_sfx_list["zastelayut"] = wnfh_SFX + "bed-sheet-movement.ogg"
    $ wnfh_sfx_list["postavilichtoto"] = wnfh_SFX + "postavilichtoto.ogg"
    $ wnfh_sfx_list["perelistovanie"] = wnfh_SFX + "perelistovanie.ogg"
    $ wnfh_sfx_list["microphone"] = wnfh_SFX + "micro.ogg"
    $ wnfh_sfx_list["pogrom"] = wnfh_SFX + "zvuk-padeniya-na-mebel-i-pogrom.ogg"
    $ wnfh_sfx_list["selyodka_po_steklu"] = wnfh_SFX + "tryot-po-steklu.ogg"
    $ wnfh_sfx_list["stuk_po_steklu"] = wnfh_SFX + "glazed_knock_x1.ogg"
    $ wnfh_sfx_list["vsplesk_vodi"] = wnfh_SFX + "silnyiy-vsplesk-ot-nyiryaniya-cheloveka.ogg"
    $ wnfh_sfx_list["vsplesk_vodi_2"] = wnfh_SFX + "mgnovennyiy-nezametnyiy-vsplesk.ogg"
    $ wnfh_sfx_list["vsplesk_vodi_3"] = wnfh_SFX + "kratkiy-tyajelyiy-vsplesk-vodyi.ogg"
    $ wnfh_sfx_list["vibili_steklo"] = wnfh_SFX + "vibili steklo.ogg"
    $ wnfh_sfx_list["otryahivanie"] = wnfh_SFX + "cloth-fluff-pillow_mkznd5vd.ogg"
    $ wnfh_sfx_list["stop_magnitofon"] = wnfh_SFX + "stop_magnitofon.ogg"
    $ wnfh_sfx_list["bucket_water_hit"] = wnfh_SFX + "bucket_water_hit.ogg"
    #$ wnfh_sfx_list[""] = wnfh_SFX + ".ogg"
    
    # MUSIC Лист
    $ wnfh_music_list["technical_chocolatki"] = wnfh_MUSIC + "technical_chocolatki.mp3"
    $ wnfh_music_list["angus_climbs_the_hill"] = wnfh_MUSIC + "Alec Holowka - Angus Climbs the Hill.mp3"
    $ wnfh_music_list["church_hill"] = wnfh_MUSIC + "Alec Holowka - Church Hill.mp3"
    $ wnfh_music_list["crimes"] = wnfh_MUSIC + "Alec Holowka - Crimes.mp3"
    $ wnfh_music_list["crimes_2"] = wnfh_MUSIC + "Alec Holowka - Crimes2.mp3"
    $ wnfh_music_list["greggs_woods"] = wnfh_MUSIC + "Alec Holowka - Gregg's Woods.mp3"
    $ wnfh_music_list["im_going_to_break_something"] = wnfh_MUSIC + "Alec Holowka - I'm Going to Break Something.mp3"
    $ wnfh_music_list["library_investigations"] = wnfh_MUSIC + "Alec Holowka - Library Investigations.mp3"
    $ wnfh_music_list["lori_m"] = wnfh_MUSIC + "Alec Holowka - Lori M.mp3"
    $ wnfh_music_list["lost_woods"] = wnfh_MUSIC + "Alec Holowka - Lost Woods.mp3"
    $ wnfh_music_list["maes_house_2"] = wnfh_MUSIC + "Alec Holowka - Mae's House 2.mp3"
    $ wnfh_music_list["mystery"] = wnfh_MUSIC + "Alec Holowka - Mystery.mp3"
    $ wnfh_music_list["outskirts"] = wnfh_MUSIC + "Alec Holowka - Outskirts.mp3"
    $ wnfh_music_list["the_bridge"] = wnfh_MUSIC + "Alec Holowka - The Bridge.mp3"
    $ wnfh_music_list["waking_up"] = wnfh_MUSIC + "Alec Holowka - Waking up.mp3"
    $ wnfh_music_list["waking_up_2"] = wnfh_MUSIC + "Alec Holowka - Waking up 2.mp3"
    $ wnfh_music_list["fireflies_on_the_porch"] = wnfh_MUSIC + "Alec Holowka - Fireflies on the Porch.mp3"
    $ wnfh_music_list["the_cars_you_might_think"] = wnfh_MUSIC + "The Cars - You Might Think.ogg"
    $ wnfh_music_list["test_song"] = wnfh_MUSIC + "testsong.mp3"
    $ wnfh_music_list["cyberpunk"] = wnfh_MUSIC + "rebelpath.mp3"
    $ wnfh_music_list["proximity"] = wnfh_MUSIC + "Alec Holowka - Proximity.mp3"
    $ wnfh_music_list["we_dont_care"] = wnfh_MUSIC + "We Dont Care.ogg"
    $ wnfh_music_list["sharkle_dream"] = wnfh_MUSIC + "Alec Holowka - Sharkle Dream.mp3"
    $ wnfh_music_list["the_hole_at_the_center_of_everything"] = wnfh_MUSIC + "Alec Holowka - The Hole At The Center Of Everything.mp3"
    $ wnfh_music_list["major_grom"] = wnfh_MUSIC + "Move Like A Devil.mp3"
    $ wnfh_music_list["ratne_igre"] = wnfh_MUSIC + "Kerber - Ratne Igre.mp3"
    $ wnfh_music_list["international"] = wnfh_MUSIC + "international.mp3"
    $ wnfh_music_list["strange"] = wnfh_MUSIC + "strange.ogg"
    $ wnfh_music_list["major_grom_2"] = wnfh_MUSIC + "ya znayu kto ti.mp3"
    $ wnfh_music_list["santa_barbara"] = wnfh_MUSIC + "santa barbara music.mp3"
    $ wnfh_music_list["back_in_black"] = wnfh_MUSIC + "AC-DC - Back in black.mp3"
    $ wnfh_music_list["dance_of_the_moonlight_jellies"] = wnfh_MUSIC + "ConcernedApe - Dance of the Moonlight Jellies.mp3"
    $ wnfh_music_list["distant_banjo"] = wnfh_MUSIC + "ConcernedApe - Distant Banjo.mp3"
    $ wnfh_music_list["the_smell_of_mushroom"] = wnfh_MUSIC + "ConcernedApe - Fall (The Smell of Mushroom).mp3"
    $ wnfh_music_list["in_the_deep_woods"] = wnfh_MUSIC + "ConcernedApe - In the Deep Woods.mp3"
    $ wnfh_music_list["pleasant_memory"] = wnfh_MUSIC + "ConcernedApe - Pleasant Memory (Penny's Theme).mp3"
    $ wnfh_music_list["tropicala"] = wnfh_MUSIC + "ConcernedApe - Summer (Tropicala).mp3"
    $ wnfh_music_list["schabernack"] = wnfh_MUSIC + "Laryssa Okada - Dorfromantik - Schabernack.mp3"
    $ wnfh_music_list["schoneweide"] = wnfh_MUSIC + "Laryssa Okada - Dorfromantik - Schöneweide.mp3"
    $ wnfh_music_list["big_fish"] = wnfh_MUSIC + "Max LL - Big Fish.mp3"
    $ wnfh_music_list["crows_end"] = wnfh_MUSIC + "Max LL - Crow's End.mp3"
    $ wnfh_music_list["northern_waters"] = wnfh_MUSIC + "Max LL - Northern Waters (Night).mp3"
    $ wnfh_music_list["pulsar_pursuit"] = wnfh_MUSIC + "Max LL - Pulsar Pursuit.mp3"
    $ wnfh_music_list["rain"] = wnfh_MUSIC + "Max LL - Rain.mp3"
    $ wnfh_music_list["shallow_waters_night"] = wnfh_MUSIC + "Max LL - Shallow Waters (Night).mp3"
    $ wnfh_music_list["the_swarms_of_hades"] = wnfh_MUSIC + "Max LL - The Swarms of Hades.mp3"
    $ wnfh_music_list["razbor_poletov"] = wnfh_MUSIC + "razbor poletov - svati.mp3"
    $ wnfh_music_list["trevoga_1"] = wnfh_MUSIC + "trevoga - svati.mp3"
    $ wnfh_music_list["sport2"] = wnfh_MUSIC + "sport2 - svati.mp3"
    $ wnfh_music_list["country_shop"] = wnfh_MUSIC + "ConcernedApe - Country Shop.mp3"
    $ wnfh_music_list["ya_znayu_kto_ti"] = wnfh_MUSIC + "ya znayu kto ti.mp3"
    $ wnfh_music_list["candy_store"] = wnfh_MUSIC + "Candy_store.mp3"
    $ wnfh_music_list["hide_and_seek"] = wnfh_MUSIC + "Sergey Eybog - Hide and Seek.mp3"
    $ wnfh_music_list["warm_evening"] = wnfh_MUSIC + "Sergey Eybog - Warm Evening.mp3"
    $ wnfh_music_list["paranoid"] = wnfh_MUSIC + "Black Sabbath - Paranoid.mp3"
    $ wnfh_music_list["rainy_day"] = wnfh_MUSIC + "Alec Holowka - Rainy Day.mp3"
    $ wnfh_music_list["god"] = wnfh_MUSIC + "Alec Holowka - God.mp3"
    $ wnfh_music_list["lost_man"] = wnfh_MUSIC + "_Blacksmith_ - The Lost Man.mp3"
    $ wnfh_music_list["old_manor"] = wnfh_MUSIC + "_Blacksmith_ - The Old Manor.mp3"
    $ wnfh_music_list["hill_camp"] = wnfh_MUSIC + "_Blacksmith_ - The Hill Camp.mp3"
    $ wnfh_music_list["friends_of_the_deceased_moon"] = wnfh_MUSIC + "_Blacksmith_ - Friends of the Deceased Moon.mp3"
    #$ wnfh_music_list[""] = wnfh_MUSIC + ".mp3"
    
    
    # AMBIENCE Лист
    $ wnfh_ambience_list["thunder1"] = wnfh_AMBIENCE + "back_ambience_litethunders1.mp3"
    $ wnfh_ambience_list["thunder2"] = wnfh_AMBIENCE + "back_ambience_litethunders2.mp3"
    $ wnfh_ambience_list["underwater1"] = wnfh_AMBIENCE + "ambience_int_silence.mp3"
    $ wnfh_ambience_list["underwater2"] = wnfh_AMBIENCE + "koshmar_water.mp3"
    $ wnfh_ambience_list["beach1"] = wnfh_AMBIENCE + "beach_1_6.mp3"
    $ wnfh_ambience_list["beach_children"] = wnfh_AMBIENCE + "beach_children.mp3"
    $ wnfh_ambience_list["water_stream"] = wnfh_AMBIENCE + "water_stream_closer.mp3"
    $ wnfh_ambience_list["water_drop"] = wnfh_AMBIENCE + "water_drop.mp3"
    $ wnfh_ambience_list["rain_night"] = wnfh_AMBIENCE + "ambience_rain_night.mp3"
    $ wnfh_ambience_list["rain"] = wnfh_AMBIENCE + "rain.mp3"
    $ wnfh_ambience_list["rain_in_building"] = wnfh_AMBIENCE + "rain_in_building.mp3"
    $ wnfh_ambience_list["dush"] = wnfh_AMBIENCE + "ambience_showers.mp3"
    $ wnfh_ambience_list["heartbeating"] = wnfh_AMBIENCE + "heartbeating.mp3"
    $ wnfh_ambience_list["skvoznyak"] = wnfh_AMBIENCE + "skvoznyak.mp3"
    $ wnfh_ambience_list["salute"] = wnfh_AMBIENCE + "ambience_salute.mp3"
    $ wnfh_ambience_list["veter_v_pole"] = wnfh_AMBIENCE + "veter-v-pole.mp3"
    #$ wnfh_ambience_list[""] = wnfh_AMBIENCE + ".mp3"
    
    ## Рандомизация мявков
    $ wnfh_meow_list = [wnfh_sfx_list[i] for i in wnfh_sfx_list.keys() if i.startswith("meow")]
    
    image cg d12_guitar_hit:
        contains:
            "bg int_musclub_day"
        contains:
            "bg int_musclub_day_blur"
            alpha 0.0
            linear 2.0 alpha 1.0
        contains:
            (wnfh_OTHER + "d12_mi_hit.png")
            pos(0.75, 0.5)
            anchor(0.5, 0.5)
            linear 3.4 pos(0.5, 0.5)
            linear 0.1 zoom 1.33
        contains:
            "white"
            alpha 0.0
            pause 3.45
            linear 0.05 alpha 1.0
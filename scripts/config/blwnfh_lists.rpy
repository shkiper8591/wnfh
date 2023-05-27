init 1000 python:
    config.developer = True

init -2 python:

    ## Создание листов ##
    
    def blwnfh_form_files_list(path):
        return {i[len(path):i.rfind(".")]:i for i in renpy.list_files() if i.startswith(path)}
    
    blwnfh_gui = dict()

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
    
    
    
    # Для главного меню
    blwnfh_gui["main_menu"] = {img:(blwnfh_MAIN_MENU + img + ".png") for img in [
        "mm_bg",
        "mm_bg2",
        "logo",
        "18",
        "gradient",
        "credits",
        "galary",
        "news",
        "play",
        "saves",
        "scheme",
        "preferences",
        "achievements",
        "exit",
        "dlc",
        ]}
        
    blwnfh_gui["settings"] = {img:(blwnfh_SETTINGS + img + ".png") for img in [
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
    
    blwnfh_gui["poligon"] = {img:(blwnfh_IMAGES + "hentai/" + img + ".png") for img in [
        "red",
        ]}
    
    blwnfh_gui["achievements"] = {img:(blwnfh_ACHIEVEMENTS + img + ".png") for img in [
        "back",
        ]}  
    # Всплывашки
    characters_banners_idle = [
        "ach_kat_idle",
        "ach_un_idle",
        "ach_mi_idle",
        "ach_us_idle",
        "ach_dv_idle",
        "ach_sl_idle",
        "ach_me_idle"
        ]
    characters_banners_hover = [
        "ach_kat_hover",
        "ach_un_hover",
        "ach_mi_hover",
        "ach_us_hover",
        "ach_dv_hover",
        "ach_sl_hover",
        "ach_me_hover",
    ]
    blwnfh_gui["banners"] = {img:(blwnfh_BANNERS + img + ".png") for img in [
        
        "relation_frame",
        "relation_up",
        "relation_down",
        "relation_neutral",
        "ach_frame",
        "ach_menu_frame",
        "ach_menu_frame_lock",
        "trophy_bronz",
        "trophy_silver",
        "trophy_gold",
        "trophy_platina",
        "trophy_white"
        
        #Тут срез для ачивок в файле blwnfh_achievements_menu
        ] + characters_banners_idle + characters_banners_hover
        }
    
    
    # Для галереи
    blwnfh_gui["gallery"] = {img:(blwnfh_GALLERY + img + ".png") for img in [
        "back",
        ]}
    
    # Звук кнопки
    blwnfh_gui["sound"] = {
        "plimp": blwnfh_SFX + "plimp.ogg",
    }

    # Ссылки в Сибирь
    blwnfh_gui["hyperlinks"] = {
        "vk":"https://vk.com/blwnfh",
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
    
    А сами переходы прописаны уже в файле blwnfh_transitions.rpy
    """
    
    # Транзиты
    blwnfh_gui["transit"] = {img:(blwnfh_TRANSITIONS + img + ".png") for img in [
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
    
    blwnfh_gui["choice"] = {img:(blwnfh_CHOICE + img + ".png") for img in [
        "2_flang_bad",
        "2_flang_dv",
        "2_flang_kat",
        "2_flang_mi",
        "2_flang_mt",
        "2_flang_neutral",
        "2_flang_sl",
        "2_flang_un",
        "2_flang_us",
        "3_flang_bad",
        "3_flang_dv",
        "3_flang_kat",
        "3_flang_mi",
        "3_flang_mt",
        "3_flang_neutral",
        "3_flang_sl",
        "3_flang_un",
        "3_flang_us",
        "3_mid_bad",
        "3_mid_dv",
        "3_mid_kat",
        "3_mid_mi",
        "3_mid_mt",
        "3_mid_neutral",
        "3_mid_sl",
        "3_mid_un",
        "3_mid_us",
        "line_2",
        "line_3",
        "vignette",
        "vignette_night",
        "line_2_day",
        "line_2_sunset",
        "line_2_night",
        "line_2_prologue",
        "line_3_day",
        "line_3_sunset",
        "line_3_night",
        "line_3_prologue",
        ]}

init 2:
    
    
    ## Видео Лист
    $ blwnfh_video_list = {
        "intro":blwnfh_VIDEO + "intro.webm",
        "pegi":blwnfh_VIDEO + "pegi.webm",
    }
    
    $ blwnfh_video_list["backdrop"] = {dn:(blwnfh_VIDEO + "backdrop_day_" + str(dn) + ".webm") for dn in range(1, 14)}
    $ blwnfh_video_list["backdrop"]["test"] = blwnfh_VIDEO + "backdrop_test.webm"
    
    image null = Null(0, 0) # Я не ебу что это, не помню нахуй это писал, но пусть будет

    $ blwnfh_sfx_list = blwnfh_form_files_list(blwnfh_SFX)
    $ blwnfh_music_list = blwnfh_form_files_list(blwnfh_MUSIC)
    $ blwnfh_ambience_list = blwnfh_form_files_list(blwnfh_AMBIENCE)
    
    # SFX Лист
    $ blwnfh_sfx_list["ps4_ach"] = blwnfh_SFX + "ps4_ach.ogg"
    $ blwnfh_sfx_list["plimp"] = blwnfh_SFX + "plimp.ogg"
    $ blwnfh_sfx_list["plimp2"] = blwnfh_SFX + "plimp2.ogg"
    $ blwnfh_sfx_list["nya"] = blwnfh_SFX + "nya.ogg"
    $ blwnfh_sfx_list["nos"] = blwnfh_SFX + "nos.ogg"
    $ blwnfh_sfx_list["guitar_hit"] = blwnfh_SFX + "guitar_hit.ogg"
    $ blwnfh_sfx_list["samogonshiki"] = blwnfh_SFX + "samogonshiki.ogg"
    $ blwnfh_sfx_list["meow_yes"] = blwnfh_SFX + "meow yes.ogg"
    $ blwnfh_sfx_list["meow_no"] = blwnfh_SFX + "meow no.ogg"
    $ blwnfh_sfx_list["murchanie"] = blwnfh_SFX + "murchanie.ogg"
    $ blwnfh_sfx_list["raschyoska"] = blwnfh_SFX + "brushing-hair.ogg"
    $ blwnfh_sfx_list["udarch"] = blwnfh_SFX + "udarch.ogg"
    $ blwnfh_sfx_list["pickup_sound"] = blwnfh_SFX + "pickup sound.ogg"
    $ blwnfh_sfx_list["hrust_vetki"] = blwnfh_SFX + "hrust_vetki.ogg"
    $ blwnfh_sfx_list["pechka"] = blwnfh_SFX + "furnace_loop.ogg"
    $ blwnfh_sfx_list["apchhi"] = blwnfh_SFX + "apchhi.mp3"
    $ blwnfh_sfx_list["oskolki"] = blwnfh_SFX + "oskolki.ogg"
    $ blwnfh_sfx_list["zastelayut"] = blwnfh_SFX + "bed-sheet-movement.ogg"
    $ blwnfh_sfx_list["postavilichtoto"] = blwnfh_SFX + "postavilichtoto.ogg"
    $ blwnfh_sfx_list["perelistovanie"] = blwnfh_SFX + "perelistovanie.ogg"
    $ blwnfh_sfx_list["microphone"] = blwnfh_SFX + "micro.ogg"
    $ blwnfh_sfx_list["pogrom"] = blwnfh_SFX + "zvuk-padeniya-na-mebel-i-pogrom.ogg"
    $ blwnfh_sfx_list["selyodka_po_steklu"] = blwnfh_SFX + "tryot-po-steklu.ogg"
    $ blwnfh_sfx_list["stuk_po_steklu"] = blwnfh_SFX + "glazed_knock_x1.ogg"
    $ blwnfh_sfx_list["vsplesk_vodi"] = blwnfh_SFX + "silnyiy-vsplesk-ot-nyiryaniya-cheloveka.ogg"
    $ blwnfh_sfx_list["vsplesk_vodi_2"] = blwnfh_SFX + "mgnovennyiy-nezametnyiy-vsplesk.ogg"
    $ blwnfh_sfx_list["vsplesk_vodi_3"] = blwnfh_SFX + "kratkiy-tyajelyiy-vsplesk-vodyi.ogg"
    $ blwnfh_sfx_list["vibili_steklo"] = blwnfh_SFX + "vibili steklo.ogg"
    #$ blwnfh_sfx_list[""] = blwnfh_SFX + ".ogg"
    
    # MUSIC Лист
    $ blwnfh_music_list["technical_chocolatki"] = blwnfh_MUSIC + "technical_chocolatki.mp3"
    $ blwnfh_music_list["angus_climbs_the_hill"] = blwnfh_MUSIC + "Alec Holowka - Angus Climbs the Hill.mp3"
    $ blwnfh_music_list["church_hill"] = blwnfh_MUSIC + "Alec Holowka - Church Hill.mp3"
    $ blwnfh_music_list["crimes"] = blwnfh_MUSIC + "Alec Holowka - Crimes.mp3"
    $ blwnfh_music_list["crimes_2"] = blwnfh_MUSIC + "Alec Holowka - Crimes2.mp3"
    $ blwnfh_music_list["greggs_woods"] = blwnfh_MUSIC + "Alec Holowka - Gregg's Woods.mp3"
    $ blwnfh_music_list["im_going_to_break_something"] = blwnfh_MUSIC + "Alec Holowka - I'm Going to Break Something.mp3"
    $ blwnfh_music_list["library_investigations"] = blwnfh_MUSIC + "Alec Holowka - Library Investigations.mp3"
    $ blwnfh_music_list["lori_m"] = blwnfh_MUSIC + "Alec Holowka - Lori M.mp3"
    $ blwnfh_music_list["lost_woods"] = blwnfh_MUSIC + "Alec Holowka - Lost Woods.mp3"
    $ blwnfh_music_list["maes_house_2"] = blwnfh_MUSIC + "Alec Holowka - Mae's House 2.mp3"
    $ blwnfh_music_list["mystery"] = blwnfh_MUSIC + "Alec Holowka - Mystery.mp3"
    $ blwnfh_music_list["outskirts"] = blwnfh_MUSIC + "Alec Holowka - Outskirts.mp3"
    $ blwnfh_music_list["the_bridge"] = blwnfh_MUSIC + "Alec Holowka - The Bridge.mp3"
    $ blwnfh_music_list["waking_up"] = blwnfh_MUSIC + "Alec Holowka - Waking up.mp3"
    $ blwnfh_music_list["waking_up_2"] = blwnfh_MUSIC + "Alec Holowka - Waking up 2.mp3"
    $ blwnfh_music_list["fireflies_on_the_porch"] = blwnfh_MUSIC + "Alec Holowka - Fireflies on the Porch.mp3"
    $ blwnfh_music_list["the_cars_you_might_think"] = blwnfh_MUSIC + "The Cars - You Might Think.ogg"
    $ blwnfh_music_list["test_song"] = blwnfh_MUSIC + "testsong.mp3"
    $ blwnfh_music_list["cyberpunk"] = blwnfh_MUSIC + "rebelpath.mp3"
    $ blwnfh_music_list["proximity"] = blwnfh_MUSIC + "Alec Holowka - Proximity.mp3"
    $ blwnfh_music_list["we_dont_care"] = blwnfh_MUSIC + "We Dont Care.ogg"
    $ blwnfh_music_list["sharkle_dream"] = blwnfh_MUSIC + "Alec Holowka - Sharkle Dream.mp3"
    $ blwnfh_music_list["the_hole_at_the_center_of_everything"] = blwnfh_MUSIC + "Alec Holowka - The Hole At The Center Of Everything.mp3"
    $ blwnfh_music_list["kate_acoustic"] = blwnfh_MUSIC + "Kate - Acoustic.mp3"
    $ blwnfh_music_list["kate_orchestra"] = blwnfh_MUSIC + "Kate - Orchestra.mp3"
    $ blwnfh_music_list["kate_piano"] = blwnfh_MUSIC + "Kate - Piano.mp3"
    $ blwnfh_music_list["major_grom"] = blwnfh_MUSIC + "Move Like A Devil.mp3"
    $ blwnfh_music_list["ratne_igre"] = blwnfh_MUSIC + "Kerber - Ratne Igre.mp3"
    $ blwnfh_music_list["international"] = blwnfh_MUSIC + "international.mp3"
    $ blwnfh_music_list["strange"] = blwnfh_MUSIC + "strange.ogg"
    $ blwnfh_music_list["major_grom_2"] = blwnfh_MUSIC + "ya znayu kto ti.mp3"
    $ blwnfh_music_list["santa_barbara"] = blwnfh_MUSIC + "santa barbara music.mp3"
    $ blwnfh_music_list["back_in_black"] = blwnfh_MUSIC + "AC-DC - Back in black.mp3"
    $ blwnfh_music_list["a_dark_corner_of_the_past"] = blwnfh_MUSIC + "ConcernedApe - A Dark Corner of the Past.mp3"
    $ blwnfh_music_list["a_golden_star_is_born"] = blwnfh_MUSIC + "ConcernedApe - A Golden Star Is Born.mp3"
    $ blwnfh_music_list["calico_desert"] = blwnfh_MUSIC + "ConcernedApe - Calico Desert.mp3"
    $ blwnfh_music_list["dance_of_the_moonlight_jellies"] = blwnfh_MUSIC + "ConcernedApe - Dance of the Moonlight Jellies.mp3"
    $ blwnfh_music_list["distant_banjo"] = blwnfh_MUSIC + "ConcernedApe - Distant Banjo.mp3"
    $ blwnfh_music_list["ghost_synth"] = blwnfh_MUSIC + "ConcernedApe - Fall (Ghost Synth).mp3"
    $ blwnfh_music_list["the_smell_of_mushroom"] = blwnfh_MUSIC + "ConcernedApe - Fall (The Smell of Mushroom).mp3"
    $ blwnfh_music_list["in_the_deep_woods"] = blwnfh_MUSIC + "ConcernedApe - In the Deep Woods.mp3"
    $ blwnfh_music_list["load_game"] = blwnfh_MUSIC + "ConcernedApe - Load Game.mp3"
    $ blwnfh_music_list["cloth"] = blwnfh_MUSIC + "ConcernedApe - Mines (Cloth).mp3"
    $ blwnfh_music_list["icicles"] = blwnfh_MUSIC + "ConcernedApe - Mines (Icicles).mp3"
    $ blwnfh_music_list["star_lumpy"] = blwnfh_MUSIC + "ConcernedApe - Mines (Star Lumpy).mp3"
    $ blwnfh_music_list["the_lava_dwellers"] = blwnfh_MUSIC + "ConcernedApe - Mines (The Lava Dwellers).mp3"
    $ blwnfh_music_list["visitor_to_the_unknown"] = blwnfh_MUSIC + "ConcernedApe - Mines (Visitor to the Unknown).mp3"
    $ blwnfh_music_list["music_box_song"] = blwnfh_MUSIC + "ConcernedApe - Music Box Song.mp3"
    $ blwnfh_music_list["playful"] = blwnfh_MUSIC + "ConcernedApe - Playful.mp3"
    $ blwnfh_music_list["pleasant_memory"] = blwnfh_MUSIC + "ConcernedApe - Pleasant Memory (Penny's Theme).mp3"
    $ blwnfh_music_list["its_a_big_world_outside"] = blwnfh_MUSIC + "ConcernedApe - Spring (It's a Big World Outside).mp3"
    $ blwnfh_music_list["the_valley_comes_alive"] = blwnfh_MUSIC + "ConcernedApe - Spring (The Valley Comes Alive).mp3"
    $ blwnfh_music_list["wild_horseradish_jam"] = blwnfh_MUSIC + "ConcernedApe - Spring (Wild Horseradish Jam).mp3"
    $ blwnfh_music_list["natures_crescendo"] = blwnfh_MUSIC + "ConcernedApe - Summer (Nature's Crescendo).mp3"
    $ blwnfh_music_list["the_sun_can_bend_an_orange_sky"] = blwnfh_MUSIC + "ConcernedApe - Summer (The Sun Can Bend an Orange Sky).mp3"
    $ blwnfh_music_list["tropicala"] = blwnfh_MUSIC + "ConcernedApe - Summer (Tropicala).mp3"
    $ blwnfh_music_list["the_adventure_guild"] = blwnfh_MUSIC + "ConcernedApe - The Adventure Guild.mp3"
    $ blwnfh_music_list["violin_solo"] = blwnfh_MUSIC + "ConcernedApe - Violin Solo.mp3"
    $ blwnfh_music_list["the_wind_can_be_still"] = blwnfh_MUSIC + "ConcernedApe - Winter (The Wind Can Be Still).mp3"
    $ blwnfh_music_list["winter_festival"] = blwnfh_MUSIC + "ConcernedApe - Winter Festival.mp3"
    $ blwnfh_music_list["the_80_hs"] = blwnfh_MUSIC + "the_80_hs.mp3"
    $ blwnfh_music_list["beerenweg"] = blwnfh_MUSIC + "Laryssa Okada - Dorfromantik - Beerenweg.mp3"
    $ blwnfh_music_list["fasanengarten"] = blwnfh_MUSIC + "Laryssa Okada - Dorfromantik - Fasanengarten.mp3"
    $ blwnfh_music_list["pleasant_hill"] = blwnfh_MUSIC + "Laryssa Okada - Dorfromantik - Pleasant Hill.mp3"
    $ blwnfh_music_list["schabernack"] = blwnfh_MUSIC + "Laryssa Okada - Dorfromantik - Schabernack.mp3"
    $ blwnfh_music_list["schoneweide"] = blwnfh_MUSIC + "Laryssa Okada - Dorfromantik - Schöneweide.mp3"
    $ blwnfh_music_list["at_night"] = blwnfh_MUSIC + "Max LL - At Night.mp3"
    $ blwnfh_music_list["at_sea"] = blwnfh_MUSIC + "Max LL - At Sea.mp3"
    $ blwnfh_music_list["big_fish"] = blwnfh_MUSIC + "Max LL - Big Fish.mp3"
    $ blwnfh_music_list["crows_end"] = blwnfh_MUSIC + "Max LL - Crow's End.mp3"
    $ blwnfh_music_list["dont_be_scared_stella"] = blwnfh_MUSIC + "Max LL - Don't Be Scared Stella.mp3"
    $ blwnfh_music_list["dust_bunnies"] = blwnfh_MUSIC + "Max LL - Dust Bunnies.mp3"
    $ blwnfh_music_list["falling_stars"] = blwnfh_MUSIC + "Max LL - Falling Stars.mp3"
    $ blwnfh_music_list["freeing_the_dragon"] = blwnfh_MUSIC + "Max LL - Freeing the Dragon.mp3"
    $ blwnfh_music_list["furogawa"] = blwnfh_MUSIC + "Max LL - Furogawa.mp3"
    $ blwnfh_music_list["gurenu_fields"] = blwnfh_MUSIC + "Max LL - Gurenu Fields.mp3"
    $ blwnfh_music_list["hummingberg"] = blwnfh_MUSIC + "Max LL - Hummingberg.mp3"
    $ blwnfh_music_list["into_the_mines"] = blwnfh_MUSIC + "Max LL - Into the Mines.mp3"
    $ blwnfh_music_list["last_voyage"] = blwnfh_MUSIC + "Max LL - Last Voyage.mp3"
    $ blwnfh_music_list["meteoroids"] = blwnfh_MUSIC + "Max LL - Meteoroids.mp3"
    $ blwnfh_music_list["mind_palace"] = blwnfh_MUSIC + "Max LL - Mind Palace.mp3"
    $ blwnfh_music_list["northern_waters"] = blwnfh_MUSIC + "Max LL - Northern Waters (Night).mp3"
    $ blwnfh_music_list["pulsar_pursuit"] = blwnfh_MUSIC + "Max LL - Pulsar Pursuit.mp3"
    $ blwnfh_music_list["rain"] = blwnfh_MUSIC + "Max LL - Rain.mp3"
    $ blwnfh_music_list["revelation"] = blwnfh_MUSIC + "Max LL - Revelation.mp3"
    $ blwnfh_music_list["shallow_waters_night"] = blwnfh_MUSIC + "Max LL - Shallow Waters (Night).mp3"
    $ blwnfh_music_list["shallow_waters"] = blwnfh_MUSIC + "Max LL - Shallow Waters.mp3"
    $ blwnfh_music_list["shipyards"] = blwnfh_MUSIC + "Max LL - Shipyards.mp3"
    $ blwnfh_music_list["song_of_growth"] = blwnfh_MUSIC + "Max LL - Song of Growth.mp3"
    $ blwnfh_music_list["stellas_departure"] = blwnfh_MUSIC + "Max LL - Stella's Departure.mp3"
    $ blwnfh_music_list["stellas_lullaby"] = blwnfh_MUSIC + "Max LL - Stella's Lullaby.mp3"
    $ blwnfh_music_list["the_mist"] = blwnfh_MUSIC + "Max LL - The Mist.mp3"
    $ blwnfh_music_list["the_swarms_of_hades"] = blwnfh_MUSIC + "Max LL - The Swarms of Hades.mp3"
    $ blwnfh_music_list["thunder_harvest"] = blwnfh_MUSIC + "Max LL - Thunder Harvest.mp3"
    $ blwnfh_music_list["overgrowth"] = blwnfh_MUSIC + "Portal 2 OST - Overgrowth.mp3"
    $ blwnfh_music_list["fors_major"] = blwnfh_MUSIC + "fors major - dalnoboishiki.mp3"
    $ blwnfh_music_list["intriga"] = blwnfh_MUSIC + "intriga - svati.mp3"
    $ blwnfh_music_list["kilometri_leta"] = blwnfh_MUSIC + "kilometri leta - svati.mp3"
    $ blwnfh_music_list["leimotiv"] = blwnfh_MUSIC + "leimotiv - svati.mp3"
    $ blwnfh_music_list["summer_changed_geography"] = blwnfh_MUSIC + "leto pomenyalo geographiyu - svati.mp3"
    $ blwnfh_music_list["march_folk"] = blwnfh_MUSIC + "march folk - svati.mp3"
    $ blwnfh_music_list["pole"] = blwnfh_MUSIC + "pole - svati.mp3"
    $ blwnfh_music_list["razbor_poletov"] = blwnfh_MUSIC + "razbor poletov - svati.mp3"
    $ blwnfh_music_list["move_theme"] = blwnfh_MUSIC + "tema dvizjeniya - svati.mp3"
    $ blwnfh_music_list["joke_theme"] = blwnfh_MUSIC + "tema prikolov - dalnoboishiki.mp3"
    $ blwnfh_music_list["trevoga_1"] = blwnfh_MUSIC + "trevoga - svati.mp3"
    $ blwnfh_music_list["trevoga_2"] = blwnfh_MUSIC + "trevojnoya - dalnoboishiki.mp3"
    $ blwnfh_music_list["uhod_ot_pogoni"] = blwnfh_MUSIC + "uhod ot pogoni - dalnoboishiki.mp3"
    $ blwnfh_music_list["uverture"] = blwnfh_MUSIC + "uverture - ivan vasilech.mp3"
    $ blwnfh_music_list["volneniye"] = blwnfh_MUSIC + "volneniye - dalnoboishiki.mp3"
    $ blwnfh_music_list["pianino"] = blwnfh_MUSIC + "pianino - svati.mp3"
    $ blwnfh_music_list["pogonya_folk"] = blwnfh_MUSIC + "pogonya folk - svati.mp3"
    $ blwnfh_music_list["polka_folk"] = blwnfh_MUSIC + "polka folk - svati.mp3"
    $ blwnfh_music_list["sport1"] = blwnfh_MUSIC + "sport1 - svati.mp3"
    $ blwnfh_music_list["sport2"] = blwnfh_MUSIC + "sport2 - svati.mp3"
    $ blwnfh_music_list["sport3"] = blwnfh_MUSIC + "sport3 - svati.mp3"
    $ blwnfh_music_list["sport4"] = blwnfh_MUSIC + "sport4 - svati.mp3"
    $ blwnfh_music_list["v_gorode_vesna"] = blwnfh_MUSIC + "v gorode vesna - svati"
    $ blwnfh_music_list["march_soviet_union"] = blwnfh_MUSIC + "march soviet union - svati.mp3"
    $ blwnfh_music_list["guitar_svati"] = blwnfh_MUSIC + "guitar - svati.mp3"
    $ blwnfh_music_list["internet_inkognito"] = blwnfh_MUSIC + "internet_inkognito - svati.mp3"
    $ blwnfh_music_list["estafeta"] = blwnfh_MUSIC + "estafeta - svati.mp3"
    $ blwnfh_music_list["country_shop"] = blwnfh_MUSIC + "ConcernedApe - Country Shop.mp3"
    $ blwnfh_music_list["ya_znayu_kto_ti"] = blwnfh_MUSIC + "ya znayu kto ti.mp3"
    #$ blwnfh_music_list[""] = blwnfh_MUSIC + ".mp3"
    
    
    # AMBIENCE Лист
    $ blwnfh_ambience_list["thunder1"] = blwnfh_AMBIENCE + "back_ambience_litethunders1.mp3"
    $ blwnfh_ambience_list["thunder2"] = blwnfh_AMBIENCE + "back_ambience_litethunders2.mp3"
    $ blwnfh_ambience_list["underwater1"] = blwnfh_AMBIENCE + "ambience_int_silence.mp3"
    $ blwnfh_ambience_list["underwater2"] = blwnfh_AMBIENCE + "koshmar_water.mp3"
    $ blwnfh_ambience_list["beach1"] = blwnfh_AMBIENCE + "beach_1_6.mp3"
    $ blwnfh_ambience_list["beach_children"] = blwnfh_AMBIENCE + "beach_children.mp3"
    $ blwnfh_ambience_list["water_stream"] = blwnfh_AMBIENCE + "water_stream_closer.mp3"
    $ blwnfh_ambience_list["water_drop"] = blwnfh_AMBIENCE + "water_drop.mp3"
    $ blwnfh_ambience_list["rain_night"] = blwnfh_AMBIENCE + "ambience_rain_night.mp3"
    $ blwnfh_ambience_list["rain"] = blwnfh_AMBIENCE + "rain.mp3"
    $ blwnfh_ambience_list["rain_in_building"] = blwnfh_AMBIENCE + "rain_in_building.mp3"
    $ blwnfh_ambience_list["dush"] = blwnfh_AMBIENCE + "ambience_showers.mp3"
    $ blwnfh_ambience_list["heartbeating"] = blwnfh_AMBIENCE + "heartbeating.mp3"
    $ blwnfh_ambience_list["skvoznyak"] = blwnfh_AMBIENCE + "skvoznyak.mp3"
    $ blwnfh_ambience_list["salute"] = blwnfh_AMBIENCE + "ambience_salute.mp3"
    #$ blwnfh_ambience_list[""] = blwnfh_AMBIENCE + ".mp3"
    
    ## Рандомизация мявков
    $ blwnfh_meow_list = [blwnfh_sfx_list[i] for i in blwnfh_sfx_list.keys() if i.startswith("meow")]
    
    image cg d6_guitar_hit:
        contains:
            "bg int_musclub_day"
        contains:
            "bg int_musclub_day_blur"
            alpha 0.0
            linear 2.0 alpha 1.0
        contains:
            (blwnfh_OTHER + "d6_mi_hit.png")
            pos(0.75, 0.5)
            anchor(0.5, 0.5)
            linear 3.4 pos(0.5, 0.5)
            linear 0.1 zoom 1.33
        contains:
            "white"
            alpha 0.0
            pause 3.45
            linear 0.05 alpha 1.0
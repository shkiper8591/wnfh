init 1000 python:
    config.developer = True

init -1 python:

    ## Создание листов ##
    
    def blwnfh_form_files_list(path):
        return {i[len(path):i.rfind(".")]:i for i in renpy.list_files() if i.startswith(path)}
    
    blwnfh_gui = dict()
   
    
    ## Спсок персонажей ##
    
    
    
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
    blwnfh_gui["img"] = {img:(blwnfh_MAIN_MENU + img + ".png") for img in [
        "fish",
        "exit",
        "info",
        "dlc",
        "scheme",
        "achievements", 
        "gallery",
        "settings",
        "test_fon",
        "fon",
        "bg",
        "vbar_full",
        "vbar_null",
        "play",
        "blank2"
        ]}
    
    # Для меню ачивок
    blwnfh_gui["achievements"] = {img:(blwnfh_ACHIEVEMENTS + img + ".png") for img in [
        "lock",
        "idle_frame",
        "hover_frame",
        "back",
        "point",
        "rel_up",
        "rel_down",
        "rel_neutral",
        ]}
    
    # Для галереи
    blwnfh_gui["gallery"] = {img:(blwnfh_GALLERY + img + ".png") for img in [
        "left",
        "right",
        "lock",
        "idle_frame",
        "hover_frame",
        "back",
        "button_1_idle",
        "button_1_hover",
        "button_2",
        "cg",
        "bg"
        ]}
    
    # Для меню настроек
    blwnfh_gui["settings"] = {img:(blwnfh_SETTINGS + img + ".png") for img in [
        "on",
        "off"
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
    В ней лежать градиенты.
    Переход работает от белого к чёрному. Там валяется ещё пара эксперементальных переходов.
    Можно насрать абсолютно любыми Ч/Б картинками и сделать из этого переход, тут ограничивает только фантазия.
    """
    
    # Транзиты
    blwnfh_gui["transit"] = {img:(blwnfh_TRANSITIONS + img + ".png") for img in [
        "slide_left",
        "slide_right",
        "slide_up",
        "slide_down",
        "sphere",
        "sphere_invert",
        "clock_l",
        "clock_r",
        "slide_diagonal",
        "exp1",
        "exp2",
        "exp3",
        "ecstrusion"
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
    $ blwnfh_sfx_list["plimp"] = blwnfh_SFX + "ps4_ach.ogg"
    $ blwnfh_sfx_list["nos"] = blwnfh_SFX + "nos.ogg"
    $ blwnfh_sfx_list["guitar_hit"] = blwnfh_SFX + "guitar_hit.ogg"
    
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
    $ blwnfh_music_list["major_grom2"] = blwnfh_MUSIC + "Move Like a Devil cut 10 sec.mp3"
    
    # AMBIENCE Лист
    $ blwnfh_ambience_list["thunder"] = blwnfh_AMBIENCE + "back_ambience_litethunders1.mp3"
    
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
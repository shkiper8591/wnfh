init -1 python:
    wnfh_old_main_menu_music = config.main_menu_music
    
init python:
    SCREENS = [
        "main_menu",
        "game_menu_selector",
        "quit",
        "say",
        "preferences",
        #"save",
        "load",
        "nvl",
        #"choice",
        #"text_history_screen",
        "yesno_prompt",
        #"skip_indicator",
        #"history",
        #"help",
    ]
    def wnfh_screen_save():  # Функция сохранения экранов из оригинала.
        #global wnfh_old_main_menu_music
        for name in SCREENS:
            renpy.display.screen.screens[
                ("wnfh_old_" + name, None)
            ] = renpy.display.screen.screens[(name, None)]

        #wnfh_old_main_menu_music = config.main_menu_music


    def wnfh_screen_act():  # Функция замены экранов из оригинала на собственные.
        config.window_title = u"Мы не отсюда"  # Здесь вводите название Вашего мода.
        for (
            name
        ) in (
            SCREENS
        ):
            renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[
                ("wnfh_" + name, None)
            ]

        config.main_menu_music = (
            wnfh_music_list["this_one_sounds_sad"]  if (wnfh_get_usertime("hour") >= 22 or wnfh_get_usertime("hour") < 8) else
            wnfh_music_list["wnfh_morning_1"]       if (wnfh_get_usertime("hour") < 12)                                   else
            wnfh_music_list["day_1"]                if (wnfh_get_usertime("hour") < 19)                                   else
            wnfh_music_list["wnfh_morning_1"]
        )

    def wnfh_screens_diact():  # Функция обратной замены.
        # Пытаемся заменить экраны.
        global wnfh_old_main_menu_music
        try:
            config.window_title = u"Бесконечное лето"
            for name in SCREENS:
                renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[
                    ("wnfh_old_" + name, None)
                ]
            config.main_menu_music = wnfh_old_main_menu_music
            #config.mouse["default"] = [ ("images/misc/mouse/1.png", 0, 0) ]
            #default_mouse = "default"
            #config.main_menu_music = "sound/music/blow_with_the_fires.ogg"
        except Exception as e:  # Если возникают ошибки, то мы выходим из игры, чтобы избежать Traceback
            #renpy.quit()
            raise e
    # Функция для автоматического включения кастомного интерфейса при загрузке сохранения с названием Вашего мода
    def wnfh_activate_after_load():
        global save_name
        if "Мы не отсюда" in save_name:
            wnfh_screen_save()
            wnfh_screen_act()

    # Добавляем функцию в Callback
    config.after_load_callbacks.append(wnfh_activate_after_load)

    # Объединяем функцию сохранения экранов и замены в одну.
    def wnfh_screens_save_act():
        wnfh_screen_save()
        wnfh_screen_act()
label technical_chocolatki:
    $ wnfh_set_time()
    scene bg int_clubs_male_day
    show technical chocolatki at wnfh_technical_chocolatki
    show el grin pioneer at wnfh_technical_chocolatki:
        xcenter 0.25
    show sh normal_smile pioneer at wnfh_technical_chocolatki:
        xcenter 0.75
    play music wnfh_music_list["technical_chocolatki"] fadein 3
    "Ведутся работы"
    stop music
    #jump wnfh_main_menu



label wnfh_test:

    $ wnfh_set_time()
    stop music fadeout 1.0
    scene int_clubs_male_day with dissolve
    play music wnfh_music_list["chilling_out"] fadein 1.0
    
    "Добро пожаловать в клубную мастерскую!"
    "Что мы хотим отладить?"
    window hide
    jump wnfh_test_main_menu

label wnfh_test_main_menu:

    scene black
    
    menu:
        "Карту?":
            jump wnfh_map_test
        "Фоны?":
            jump wnfh_background
        "Анимации?":
            jump wnfh_test_anim
        "Спрайты?":
            jump wnfh_sprites_test
        "Музыку и звуки?":
            jump wnfh_test_music
        "Цензуру?":
            jump wnfh_test_matyki
        "NVL?":
            jump wnfh_test_nvl
        "Выборы?":
            jump wnfh_test_choice
        "Достижения?":
            jump wnfh_test_ach
        "Дни?":    
            jump wnfh_test_days
        "Карту?":
            jump wnfh_test_map
        "Переходы?":
            jump wnfh_test_transitions
        "Анимированные шейдеры?":
            jump wnfh_test_shaders
        "Покинуть меню отладки":
            return

label wnfh_test_sprites:
    
    "Какие именно нам нужно отладить спрайты?"
    
    menu:
        "Обыкновенные?":
            jump wnfh_spritestest2
        "Фоновые?":
            jump wnfh_background
        "Обеденный стол?":
            jump wnfh_stol
        "Вернутся назад.":
            jump wnfh_test_main_menu

    jump wnfh_test_main_menu
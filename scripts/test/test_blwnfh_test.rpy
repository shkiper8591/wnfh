label technical_chocolatki:
    $ blwnfh_set_time()
    scene bg int_clubs_male_day
    show technical chocolatki blwnfh_technical_chocolatki at blwnfh_technical_chocolatki
    show el grin pioneer at blwnfh_technical_chocolatki:
        xcenter 0.25
    show sh normal_smile pioneer at blwnfh_technical_chocolatki:
        xcenter 0.75
    play music blwnfh_music_list["technical_chocolatki"] fadein 3
    "Ведутся работы"
    stop music
    jump blwnfh_main_menu



label blwnfh_test:
    $ blwnfh_new_chapter("Тест")
    $ blwnfh_set_time()
    scene black
    
    "Добро пожаловать в полигон!"
    "Что мы хотим отладить?"
    jump blwnfh_test_main_menu

label blwnfh_test_main_menu:

    scene black
    
    menu:
        "Анимации":
            jump blwnfh_test_anim
        "Спрайты?":
            jump blwnfh_sprites_test
        "Музыку?":
            jump blwnfh_musictest
        "Цензуру?":
            jump blwnfh_matyki
        "NVL?":
            jump blwnfh_nvltest
        "Выборы?":
            jump blwnfh_continue
        "Достижения?":
            jump blwnfh_continue_4
        "Дни?":    
            jump blwnfh_daystest
        "Покинуть меню отладки":
            jump blwnfh_main_menu

label blwnfh_spritestest1:
    
    "Какие именно нам нужно отладить спрайты?"
    
    menu:
        "Обыкновенные?":
            jump blwnfh_spritestest2
        "Фоновые?":
            jump blwnfh_background
        "Обеденный стол?":
            jump blwnfh_stol
        "Вернутся назад?":
            jump blwnfh_test_main_menu
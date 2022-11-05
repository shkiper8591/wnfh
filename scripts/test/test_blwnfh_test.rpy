label technical_chocolatki:
    scene bg int_clubs_male_day
    show technical chocolatki blwnfh_technical_chocolatki at blwnfh_technical_chocolatki
    play music blwnfh_music_list["technical_chocolatki"] fadein 3
    "Ведутся работы"
    stop music
    jump blwnfh_main_menu



label blwnfh_test:
    $ blwnfh_new_chapter(13)
    $ blwnfh_set_time()
    scene black
    
    "Добро пожаловать в меню отладки!"
    "Что мы хотим отладить?"
    jump blwnfh_test_main_menu

label blwnfh_test_main_menu:

    scene black
    
    menu:
        "Анимации":
            jump blwnfh_test_anim
        "Спрайты?":
            jump blwnfh_spritestest1
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

label blwnfh_spritestest2:
    
    "Чей именно мы хотим отладить спрайт?"
    
    menu:
        "Катя? - Пока не работает.":
            jump blwnfh_spritestest2
        "Лена? - Пока не работает.":
            jump blwnfh_spritestest2
        "Мику? - Пока не работает.":
            jump blwnfh_spritestest2
        "Женя? - Пока не работает.":
            jump blwnfh_spritestest2
        "Славя? - Пока не работает.":
            jump blwnfh_spritestest2
        "Алиса? - Пока не работает.":
            jump blwnfh_spritestest2
        "Ульяна? - Пока не работает":
            jump blwnfh_spritestest2
        "Ольга Дмитриевна?":
            jump blwnfh_mttest
        "Виола?":
            jump blwnfh_cstest
        "Шурик? - Пока не работает.":
            jump blwnfh_spritestest2
        "Электроник? - Пока не работает.":
            jump blwnfh_spritestest2
        "Сергей Дмитриевич? - Пока не работает.":
            jump blwnfh_spritestest2
        "Поварихи? - Пока не работает.":
            jump blwnfh_spritestest2
        "Вернутся назад":
            jump blwnfh_spritestest1


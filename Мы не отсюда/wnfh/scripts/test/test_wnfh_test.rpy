label technical_chocolatki:
    $ wnfh_set_time()
    scene bg int_clubs_male_day
    show technical chocolatki at blwnfh_technical_chocolatki
    show el grin pioneer at blwnfh_technical_chocolatki:
        xcenter 0.25
    show sh normal_smile pioneer at blwnfh_technical_chocolatki:
        xcenter 0.75
    play music blwnfh_music_list["technical_chocolatki"] fadein 3
    "Ведутся работы"
    stop music
    jump blwnfh_main_menu



label wnfh_test:
    $ wnfh_new_chapter("Тест")
    $ wnfh_set_time()
    scene black
    
    "Добро пожаловать в полигон!"
    "Что мы хотим отладить?"
    window hide
    jump wnfh_test_main_menu

label wnfh_test_main_menu:

    scene black
    
    menu:
        "Анимации?":
            jump blwnfh_test_anim
        "Спрайты?":
            jump blwnfh_sprites_test
        "Музыку и звуки?":
            jump wnfh_test_music
        "Цензуру?":
            jump blwnfh_test_matyki
        "NVL?":
            jump blwnfh_test_nvl
        "Выборы?":
            jump blwnfh_test_choice
        "Достижения?":
            jump blwnfh_test_ach
        "Дни?":    
            jump blwnfh_test_days
        "Покинуть меню отладки":
            jump wnfh_main_menu

label blwnfh_test_sprites:
    
    "Какие именно нам нужно отладить спрайты?"
    
    menu:
        "Обыкновенные?":
            jump blwnfh_spritestest2
        "Фоновые?":
            jump blwnfh_background
        "Обеденный стол?":
            jump blwnfh_stol
        "Вернутся назад.":
            jump blwnfh_test_main_menu

    "База Данных сброшена! Кликни чтобы вернутся в тест меню."
    jump wnfh_test_main_menu
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
    jump wnfh_main_menu



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
        "Карта?":
            jump wnfh_test_map
        "Переходы":
            jump wnfh_test_transitions
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
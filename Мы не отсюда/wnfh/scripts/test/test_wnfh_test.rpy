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
        "Сбросить все переменные":
            jump blwnfh_test_drop_variables
        "Сбросить все лавпоинты":
            jump blwnfh_test_drop_lp
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

label blwnfh_test_drop_variables:

    "Это действие нельзя будет отменить. Вы уверены?"

    menu:
        "Нет":
            jump blwnfh_test_main_menu
        "Да":
            $ d6c_me_poshel_v_les        =       None
            $ d6c_me_poshel_po_beregu    =       None
            $ d6c_me_sovral              =       None
            $ d6c_el_videl_seregu        =       None
            $ d6c_mz_videl_jeny          =       None
            $ d6c_mz_pomog_jene          =       None
            $ d6c_kat_katya_prosipalas   =       None
    "Переменные сброшены! Кликни чтобы вернутся в тест меню."
    jump wnfh_test_main_menu

label blwnfh_test_drop_lp:

    "Это действие нельзя будет отменить. Вы уверены?"
    menu:
        "Нет":
            jump blwnfh_test_main_menu
        "Да":
            $ kat_lp     =       0
            $ dv_lp      =       0
            $ un_lp      =       0
            $ us_lp      =       0
            $ mi_lp      =       0
            $ mz_lp      =       0
    "Лавпоинты сброшены! Кликни чтобы вернутся в тест меню."
    jump wnfh_test_main_menu
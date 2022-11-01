label blwnfh_musictest:
    
    "Что конкретно мы хотим протестировать?"
    
    menu:
        "Музыку со всплывашкой?":
            jump blwnfh_brbrbrbr
        "Или просто музыку?":
            jump blwnfh_justmusic
        "Вернутся назад":
            jump blwnfh_test_main_menu

label blwnfh_brbrbrbr:
    
    scene bg ext_sky with dissolve2
    play music blwnfh_music_list["angus_climbs_the_hill"] fadein 3
    $ blwnfh_get_relation("void", "Alec Holowka - Angus Climbs the Hill", "None")
    $ renpy.pause(1.0)
    stop music fadeout 2
    
    "И это тоже вроде работает"
    "Возвращаемся в меню отладки?"
    
    menu: 
    
        "Да":
            jump blwnfh_test_main_menu 
            
label blwnfh_justmusic:

    "Тест зацикливания музыки."
    "Три. {w}Два. {w}Один."
    
    play music blwnfh_music_list["cyberpunk"] noloop 
    
    $ blwnfh_set_mode(nvl)
    nvl show
    
    me "«Доброе утрррооо «Совёнок»! Вчерашний подсчёт трупов закончился на крепкой тридцаточке! {w}Спонсор десятки — нестихающая жатва пионера в мультивселенных. Минус один лагерь, так что все готовьтесь! Вожатая по этому поводу не сделает ни хрена!»\n{w}«А вот в воркшопе полный отвал. Очевидно, трешмоддоделы снова резвятся в сети»\n{w}«На площади, выжившие в лагере отскребают от асфальта жертв очередной безумной Лены».\n«А Райцентр... Ну... {w}хех... Райцентр и есть Райцентр»\n«С вами, как всегда, был Семёоооон. Впереди новый день в лагере мечты!»"
    
    nvl hide
    $ blwnfh_set_mode()
    
    stop music
    
    "Возвращаемся в меню отладки?"
    
    menu: 
    
        "Да":
            jump blwnfh_test_main_menu
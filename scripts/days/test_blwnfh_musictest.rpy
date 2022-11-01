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
    "Ноль."
    
    play music blwnfh_music_list["test_song"] fadein 1
    
    "Кликни чтобы остановить музыку."
    
    stop music
    
    "Возвращаемся в меню отладки?"
    
    menu: 
    
        "Да":
            jump blwnfh_test_main_menu 
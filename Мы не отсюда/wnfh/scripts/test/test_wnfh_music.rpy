label wnfh_test_music:
    
    "Что конкретно мы хотим протестировать?"
    
    menu:
        "Музыку со всплывашкой?":
            jump wnfh_brbrbrbr
        "Просто музыку?":
            jump wnfh_justmusic
        "Звуки?":
            jump wnfh_sfx_test
        "Вернутся назад":
            jump blwnfh_test_main_menu

label wnfh_brbrbrbr:
    
    scene bg ext_sky with dissolve2
    play music wnfh_music_list["angus_climbs_the_hill"] fadein 3
    #$ blwnfh_get_relation("void", "Alec Holowka - Angus Climbs the Hill", "None")
    $ renpy.pause(1.0)
    stop music fadeout 2
    
    "И это тоже вроде работает"
    "Возвращаемся в меню отладки?"
    
    menu: 
    
        "Вернутся в меню отладки":
            jump blwnfh_test_main_menu 
        "Вернутся к выбору типа теста":    
            jump wnfh_test_music            

label wnfh_justmusic:

    "Тест музыки."
    "Три. {w}Два. {w}Один."
    
    play music wnfh_music_list["the_cars_you_might_think"] noloop
    
    "ткни чтобы остановить музыку."
    
    stop music
    
    menu: 
        
        "Вернутся в меню отладки":
            jump blwnfh_test_main_menu
        "Вернутся к выбору типа теста":    
            jump wnfh_test_music

label wnfh_sfx_test:

    "Тест звуков."
    "Два горна одновременно на разных дорожках с задержкой в 0.1"


    $ wnfh_set_volume(channel="sound", value=0.5)
    $ wnfh_set_volume(channel="sound2", value=0.5)
    play sound sfx_dinner_horn_processed
    $ renpy.pause (0.1)
    play sound2 sfx_dinner_horn_processed

    "Тест начался."

    menu: 
        
        "Вернутся в меню отладки":
            jump blwnfh_test_main_menu
        "Вернутся к выбору типа теста":    
            jump wnfh_test_music
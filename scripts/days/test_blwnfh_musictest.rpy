label blwnfh_musictest:
    
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
label blwnfh_test_ach:

    scene bg ext_square_day with dissolve2
    $ renpy.pause(1.0, hard=True)
    #"..."
    #$ blwnfh_reset_achievements()
    #$ blwnfh_get_achievement("payday")
    #$ renpy.pause(1.0, hard=True)
    
    "///"
    $ blwnfh_reset_achievements()
    $ blwnfh_get_achievement("zaebist")
    $ renpy.pause(1.0, hard=True)
    
    "==="
    $ blwnfh_reset_achievements()
    $ blwnfh_get_achievement("alarm")
    $ renpy.pause(1.0, hard=True)
    "Возвращаемся в меню отладки?"
    
    menu: 
    
        "Да":
            jump blwnfh_test_main_menu
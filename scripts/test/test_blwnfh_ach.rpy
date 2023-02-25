label blwnfh_test_ach:

    scene bg ext_square_day with dissolve2
    $ renpy.pause(1.0, hard=True)
    #"..."
    #$ blwnfh_reset_achievements()
    #$ blwnfh_get_achievement("payday")
    #$ renpy.pause(1.0, hard=True)
    
    
    
    "вор"
    $ blwnfh_get_achievement("payday")
    $ renpy.pause(1.0, hard=True)
    "альфа"
    $ blwnfh_get_achievement("alpha-0.1")
    $ renpy.pause(1.0, hard=True)
    
    jump blwnfh_test_ach_hui
    
label blwnfh_test_ach_hui:
    "бкрр"
    $ blwnfh_get_achievement("bkrr")
    $ renpy.pause(1.0, hard=True)
    
    "почта россии"
    $ blwnfh_get_achievement("post")
    $ renpy.pause(1.0, hard=True)
    "ждун"
    $ blwnfh_get_achievement("zgdun")
    $ renpy.pause(1.0, hard=True)
    "заебись"
    $ blwnfh_get_achievement("zaebist")
    $ renpy.pause(1.0, hard=True)
    "рукожоп"
    $ blwnfh_get_achievement("handass")
    $ renpy.pause(1.0, hard=True)
    
    "==="
    $ blwnfh_get_achievement("alarm")
    $ renpy.pause(1.0, hard=True)
    "Возвращаемся в меню отладки?"
    
    
    
    menu: 
    
        "Да":
            jump blwnfh_test_main_menu
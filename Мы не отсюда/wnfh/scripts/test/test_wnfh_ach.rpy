label wnfh_test_ach:
    $ wnfh_set_time("day")
    scene bg ext_square_night with dissolve2
    $ renpy.pause(1.0, hard=True)
    #"..."
    #$ wnfh_reset_achievements()
    #$ wnfh_get_achievement("payday")
    #$ renpy.pause(1.0, hard=True)
    
    
    window show
    "spirt"
    $ wnfh_get_achievement("spirt")
    $ renpy.pause(1.0, hard=True)
    "альфа"
    $ wnfh_get_achievement("alpha")
    $ renpy.pause(1.0, hard=True)
    "бкрр"
    $ wnfh_get_achievement("bkrr")
    $ renpy.pause(1.0, hard=True)
    
    "почта россии"
    $ wnfh_get_achievement("post")
    $ renpy.pause(1.0, hard=True)
    "ждун"
    $ wnfh_get_achievement("zgdun")
    $ renpy.pause(1.0, hard=True)
    "заебись"
    $ wnfh_get_achievement("zaebist")
    $ renpy.pause(1.0, hard=True)
    "рукожоп"
    $ wnfh_get_achievement("handass")
    $ renpy.pause(1.0, hard=True)
    
    "==="
    $ wnfh_get_achievement("alarm")
    $ renpy.pause(1.0, hard=True)
    "Возвращаемся в меню отладки?"
    
    
    
    menu: 
    
        "Да":
            jump wnfh_test_main_menu
init python:
    def ESPE_set_espe_settings():    
        config.window_title = u"Редактор частиц (MystiSs)"
        config.name = "ES Particle editor"
        config.version = "0.58"

        store._game_menu_screen = None

    def ESPE_set_es_settings():    
        config.window_title = u"Бесконечное лето"
        config.name = "Everlasting_Summer"
        config.version = "1.6"

        store._game_menu_screen = "game_menu_selector"
        
        renpy.free_memory()
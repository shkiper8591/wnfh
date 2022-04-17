## Тут лежат пути к файлам
init -4 python:
    blwnfh_IMAGES = "mods/blwnfh/images/"
    blwnfh_SPRITES_CLOSE = blwnfh_IMAGES + "sprites/close/"
    blwnfh_SPRITES_NORMAL = blwnfh_IMAGES + "sprites/normal/"
    blwnfh_SPRITES_FAR = blwnfh_IMAGES + "sprites/far/"

init -2 python:

    ## Инициализация спрайтов ##
    blwnfh_far_size = (675, 1080)
    blwnfh_normal_size = (900, 1080)
    blwnfh_close_size = (1125, 1080)
    
    kat_normal_pioneer = ["kat_1_body.png", "kat_1_pioneer.png", "kat_1_normal.png"]
    kat_gloomy_pioneer = ["kat_1_body.png", "kat_1_pioneer.png", "kat_1_gloomy.png"]
    

    blwnfh_add_character("kat", {
        "name": "Катя",
        "color": "#ff97bb",
        "variants": [
            
            #kat normal pioneer
            ("normal pioneer far", blwnfh_SPRITES_FAR, blwnfh_far_size, kat_normal_pioneer),
            ("normal pioneer", blwnfh_SPRITES_NORMAL, blwnfh_normal_size, kat_normal_pioneer),
            ("normal pioneer close", blwnfh_SPRITES_CLOSE, blwnfh_close_size, kat_normal_pioneer),
            
            #kat gloomy pioneer
            ("gloomy pioneer far", blwnfh_SPRITES_FAR, blwnfh_far_size, kat_gloomy_pioneer),
            ("gloomy pioneer", blwnfh_SPRITES_NORMAL, blwnfh_normal_size, kat_gloomy_pioneer),
            ("gloomy pioneer close", blwnfh_SPRITES_CLOSE, blwnfh_close_size, kat_gloomy_pioneer),
            
            
        ]
    })
    blwnfh_clone_character_as_unknown("kat", "Девушка")

    
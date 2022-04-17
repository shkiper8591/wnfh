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

    def make_variants(name, sprites):
        return [
            (name + " far", blwnfh_SPRITES_FAR, blwnfh_far_size, sprites),
            (name, blwnfh_SPRITES_NORMAL, blwnfh_normal_size, sprites),
            (name + " close", blwnfh_SPRITES_CLOSE, blwnfh_close_size, sprites),
        ]
    
    blwnfh_add_character("kat", "Катя", "Девушка", "#FF97BB")

    blwnfh_add_variants("kat", []
        + make_variants("normal pioneer", kat_normal_pioneer)
        + make_variants("gloomy pioneer", kat_gloomy_pioneer)
    )

    # blwnfh_add_variant("kat", ("gloomy pioneer close", blwnfh_SPRITES_CLOSE, blwnfh_close_size, kat_gloomy_pioneer));
    
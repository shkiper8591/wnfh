init 0:
    $ mods["blwnfh_main"]=u"Мы не отсюда"

## Тут лежат пути к файлам
init -4 python:
    blwnfh_SFX = "mods/blwnfh/sound/sfx/"
    blwnfh_IMAGES = "mods/blwnfh/images/"
    blwnfh_SPRITES_CLOSE = blwnfh_IMAGES + "sprites/close/"
    blwnfh_SPRITES_NORMAL = blwnfh_IMAGES + "sprites/normal/"
    blwnfh_SPRITES_FAR = blwnfh_IMAGES + "sprites/far/"
    blwnfh_MAIN_MENU = blwnfh_IMAGES + "gui/main_menu/"

init -2 python:

    ## Инициализация спрайтов ##
    blwnfh_far_size = (2250, 2160)
    blwnfh_normal_size = (2250, 2160)
    blwnfh_close_size = (2250, 2160)
    
    #blwnfh_far_size = (675, 1080)
    #blwnfh_normal_size = (900, 1080)
    #blwnfh_close_size = (1125, 1080)
    
    kat_1_pioneer_shocked = ["kat_1_body.png", "kat_1_pioneer.png", "kat_1_shocked.png"]
    #kat_2_pioneer = ["kat_2_body.png", "kat_2_pioneer.png"]
    #kat_3_pioneer = ["kat_3_body.png", "kat_3_pioneer.png"]
    #kat_1_kupalnik = ["kat_1_body.png", "kat_1_kupalnik.png"]
    #kat_2_kupalnik = ["kat_2_body.png", "kat_2_kupalnik.png"]
    #kat_3_kupalnik = ["kat_3_body.png", "kat_3_kupalnik.png"]
    #kat_1_povsedn = ["kat_1_body.png", "kat_1_povsedn.png"]
    #kat_2_povsedn = ["kat_2_body.png", "kat_2_povsedn.png"]
    #kat_3_povsedn = ["kat_3_body.png", "kat_3_povsedn.png"]
    #kat_1_povsedn_rubashka = ["kat_1_body.png", "kat_1_povsedn.png", "kat_1_rubashka.png"]
    #kat_2_povsedn_rubashka = ["kat_2_body.png", "kat_2_povsedn.png", "kat_2_rubashka.png"]
    #kat_3_povsedn_rubashka = ["kat_3_body.png", "kat_3_povsedn.png", "kat_3_rubashka.png"]
    #sl_1_upset_pioneer = ["sl_1_body.png", "sl_1_pioneer.png", "sl_1_upset.png"] 

    def make_variants(name, sprites):
        return [
            (name + " far", blwnfh_SPRITES_FAR, blwnfh_far_size, sprites),
            (name, blwnfh_SPRITES_NORMAL, blwnfh_normal_size, sprites),
            (name + " close", blwnfh_SPRITES_CLOSE, blwnfh_close_size, sprites),
        ]
    


    blwnfh_add_variants("kat", []
        + make_variants("shocked pioneer", kat_1_pioneer_shocked)
        #+ make_variants("2 pioneer", kat_2_pioneer)
        #+ make_variants("3 pioneer", kat_3_pioneer)
        #+ make_variants("1 kupalnik", kat_1_kupalnik)
        #+ make_variants("2 kupalnik", kat_2_kupalnik)
        #+ make_variants("3 kupalnik", kat_3_kupalnik)
        #+ make_variants("1 povsedn", kat_1_povsedn)
        #+ make_variants("2 povsedn", kat_2_povsedn)
        #+ make_variants("3 povsedn", kat_3_povsedn)
        #+ make_variants("1 povsedn rubashka", kat_1_povsedn_rubashka)
        #+ make_variants("2 povsedn rubashka", kat_2_povsedn_rubashka)
        #+ make_variants("3 povsedn rubashka", kat_3_povsedn_rubashka)
    )

    ## Звуковые эффекты ##
    
init 2:
    $ blwnfh_sfx_list = blwnfh_form_files_list(blwnfh_SFX)

    $ blwnfh_sfx_list["ps4_ach"] = blwnfh_SFX + "ps4_ach.ogg"

    # blwnfh_add_variant("kat", ("gloomy pioneer close", blwnfh_SPRITES_CLOSE, blwnfh_close_size, kat_gloomy_pioneer));
    
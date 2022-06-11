init 0:
    $ mods["blwnfh_main"]=u"Мы не отсюда"

##init с объявлением переменных
init -4 python:

    ## Тут лежат пути к файлам
    blwnfh_SFX = "mods/blwnfh/sound/sfx/"
    blwnfh_IMAGES = "mods/blwnfh/images/"
    blwnfh_SPRITES_CLOSE = blwnfh_IMAGES + "sprites/close/"
    blwnfh_SPRITES_NORMAL = blwnfh_IMAGES + "sprites/normal/"
    blwnfh_SPRITES_FAR = blwnfh_IMAGES + "sprites/far/"
    blwnfh_MAIN_MENU = blwnfh_IMAGES + "gui/main_menu/"

    
init 2:
    ## Звуковые эффекты ##
    $ blwnfh_sfx_list = blwnfh_form_files_list(blwnfh_SFX)

    $ blwnfh_sfx_list["ps4_ach"] = blwnfh_SFX + "ps4_ach.ogg"

    
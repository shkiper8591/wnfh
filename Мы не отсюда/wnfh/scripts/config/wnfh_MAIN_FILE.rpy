init 0:
    $ mods["wnfh_main"]=u"Мы не отсюда (В разработке)"
    #$ mods["wnfh_main"]=u"{font=wnfh/fonts/IntroDemo-BlackCAPS.otf}{color=#FF97BB}{size=50}Мы не отсюда{/size}{/color}{/font}"
    define config.image_cache_size_mb = 600

label wnfh_main:
    window hide
    $ wnfh_set_time()
    stop ambience fadeout 3
    stop sound fadeout 3
    stop sound_loop fadeout 3
    stop music fadeout 3 # Останавливаем музыку.
    scene bg black with fade2 # Переходим на сцену с чёрным экраном.
    $ wnfh_screens_save_act() # Сохраняем экраны из оригинала и заменяем на собственные.
    $ persistent._file_page = "WNFH_Saves" # Имена наших слотов сейвов
    return # С помощью return попадаем в главное меню игры.
    #scene cg d8_me_kat_boathouse_wnfh with dissolve
    $ renpy.pause(2)


label wnfh_exit:
    window hide # Скрываем текстбокс.
    $ config.mouse_displayable = None
    stop music fadeout 3 # Останавливаем музыку.
    scene black with fade # Переходим на сцену с чёрным экраном.
    $ wnfh_screens_diact() # Делаем обратную замену экранов мода на оригинальные.
    $ persistent._file_page = "1-1" # Возвращаем оригинальные слоты сейвов
    $ MainMenu(confirm=False)() # Выходим в главное меню.
    
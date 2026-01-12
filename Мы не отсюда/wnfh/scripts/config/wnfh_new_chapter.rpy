init 0:
    $ mods["wnfh_main"]=u"Мы не отсюда (В разработке)"
    #$ mods["wnfh_main"]=u"{font=wnfh/fonts/IntroDemo-BlackCAPS.otf}{color=#FF97BB}{size=50}Мы не отсюда{/size}{/color}{/font}"
    define config.image_cache_size_mb = 600
init python:
    def wnfh_set_time(time_of_day="day", sprite_time=None):
        if sprite_time == None:
            if time_of_day == "prologue":
                sprite_time = "night"
            else:
                sprite_time = time_of_day
        renpy.store.wnfh_spritetime = sprite_time
        renpy.store.wnfh_tymeofday = time_of_day
        wnfh_chars_define()

        for i in [("kat", "mi", adv), ("kat", "un", adv), ("me", "dv", nvl), ("me", "el", adv), ("me", "kat", adv), ("me", "el", adv)]:
            wnfh_double_char_define(i[0], i[1], i[2])

    def wnfh_new_chapter():
        #wnfh_set_mode()
        #wnfh_mute(1.0)

init -1 python:
    def wnfh_set_mode(mode=adv):
        nvl_clear()
        wnfh_chars_define(kind=mode)

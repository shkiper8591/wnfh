init 0:
    #$ mods["wnfh_main"]=u"Мы не отсюда (В разработке)"
    $ mods["wnfh_main"]=u"{font=wnfh/fonts/IntroDemo-BlackCAPS.otf}{color=#FF97BB}{size=50}Мы не отсюда{/size}{/color}{/font}"
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
    def wnfh_new_chapter(day):
        # renpy.block_rollback()
        wnfh_set_mode()
        wnfh_mute(1.0)
        for channel in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "music", "test_one", "test_two"):
            wnfh_set_volume(channel, 1.0, 0.0)
        wnfh_set_savename(day)
        renpy.scene()
        renpy.show("black")
        renpy.with_statement(Dissolve(2.0))
        wnfh_set_time()
        if day in range(0, 15):
            renpy.pause(1.0, hard=True)
            renpy.movie_cutscene(wnfh_video_list["backdrop"][day], delay=10.0)
        
        elif day == u"Тест":
            renpy.pause(1.0, hard=True)
            renpy.movie_cutscene(wnfh_video_list["backdrop"]["test"], delay=191.0)
            #renpy.movie_cutscene(wnfh_video_list["backdrop"]["test"], delay=7.0)
init -1 python:
    def wnfh_set_mode(mode=adv):
        nvl_clear()
        wnfh_chars_define(kind=mode)

    

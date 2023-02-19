init 0:
    $ mods["blwnfh_main"]=u"Мы не отсюда"
init python:
    def blwnfh_set_time(time_of_day="day", sprite_time=None):
        persistent.timeofday = time_of_day
        if sprite_time == None:
            if time_of_day == "prologue":
                sprite_time = "night"
            else:
                sprite_time = time_of_day
        persistent.sprite_time = sprite_time
    
    def blwnfh_new_chapter(day):
        # renpy.block_rollback()
        blwnfh_set_mode()
        blwnfh_mute(1.0)
        for channel in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "music", "test_one", "test_two"):
            blwnfh_set_volume(channel, 1.0, 0.0)
        blwnfh_set_savename(day)
        renpy.scene()
        renpy.show("black")
        renpy.with_statement(Dissolve(2.0))
        blwnfh_set_time()
        if day in range(0, 15):
            renpy.pause(1.0, hard=True)
            renpy.movie_cutscene(blwnfh_video_list["backdrop"][day], delay=10.0)
        
        elif day == u"Тест":
            renpy.pause(1.0, hard=True)
            renpy.movie_cutscene(blwnfh_video_list["backdrop"]["test"], delay=191.0)
            #renpy.movie_cutscene(blwnfh_video_list["backdrop"]["test"], delay=7.0)
init -1 python:
    def blwnfh_set_mode(mode=adv):
        nvl_clear()
        blwnfh_chars_define(kind=mode)

    

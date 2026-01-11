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

init python:
    
    ## Генератор названий для сохранений ##
    
    # Название мода для сохранений
    wnfh_title = [u"Мы не отсюда"]
    
    

    def wnfh_set_savename(day):
        chapters_list = {0: [0], 1:[1, 2], 2:[3, 4, 5, 6], 3:[7, 8, 9, 10], 4:[11, 12, 13, 14], 5:["Тест"]}
        
        for n,i in enumerate(chapters_list.values()):
            if day in i:
                chapter = n+1
        global save_name
        
        if chapter == 0:
            roman_chapter = "Пролог"
        elif chapter == 1:
            roman_chapter = "I"
        elif chapter == 2:
            roman_chapter = "II"
        elif chapter == 3:
            roman_chapter = "III"
        elif chapter == 4:
            roman_chapter = "IV"
        else:
            roman_chapter = "Тестовая"
        title = wnfh_title[0] + "\n"
        if day in range(0, 16):
            save_name = title + "Глава " + str(roman_chapter) + ". " + u"День № " + str(day)
        else:
            save_name = title + day
    

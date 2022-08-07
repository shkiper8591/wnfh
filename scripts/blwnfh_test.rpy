label blwnfh_test:

    $ new_chapter(2, u"Мы не отсюда. Тест.")
    $ persistent.sprite_time = "day"
    $ day_time()
    show bg int_dining_hall_day with dspr  
    #$ blwnfh_set_mode(nvl)
    #nvl show dissolve
    
    #"Довольно громко сказала Ульяна."
    #th "Бегунок нужно заполнить, я его дам"
    #voice "nigga nigga"
    #me "who?!"
    #
    #kat "Ты пойдёшь со мной?"
    #gp "Fuck you"
    #ukat "Asshole"
    #kat "Клуб любителей кожевного мастерства на один этаж ниже"
    #
    #
    #
    #
    #nvl hide dissolve
    #$ blwnfh_set_mode()
    #
    #$ blwnfh_thoughts_show("Пойти нахуй?", "Остаться здесь?", "Вернуться домой?", "А может, поиграть в дотку?", "Или подрочить?", "Или купить пивка?")
    
    
    
    "slide_diagonal"
    scene
    $ renpy.show("bg int_warehouse_night_lamp_off_light_on", what = "bg int_warehouse_night_lamp_off_light_on")
    with slide_diagonal
    
    "slide_diagonal_blure"
    scene
    $ renpy.show("bg int_warehouse_sunset", what = "bg int_warehouse_sunset")
    with slide_diagonal_blure
    
    "sphere_invert_blure_dissolve5"
    scene
    $ renpy.show("bg ext_music_club_sunset", what = "bg ext_music_club_sunset")
    with sphere_invert_blure_dissolve5
    
    "sphere_invert_blure_dissolve10"
    scene
    $ renpy.show("bg ext_clubs_sunset", what = "bg ext_clubs_sunset")
    with sphere_invert_blure_dissolve10
    
    #$ renpy.pause(1.0, hard=True)
    
    mt "Бегунок нужно заполнить, я его дам"
    mt "Карту лагеря нужно запомнить, её я не дам"
    
    hide mt with dspr
    
    show kat shocked pioneer close at right with dspr
    show kat shocked pioneer far at left with dspr
    show kat shocked pioneer at center with dspr
    
    hide kat with dspr
    
    $ renpy.pause(1.0, hard=True)
    
    show us laugh2 pioneer close at center with dspr
    us "Это было весело!"
    
    $ blwnfh_reset_achievements()
    $ blwnfh_get_achievement("payday")
    $ renpy.pause(1.0, hard=True)
    
    "Довольно громко сказала Ульяна."
    
    "Мы запускаем лохотрон"
    
    jump blwnfh_main
    

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
    
    
    
    "experemental1"
    scene
    $ renpy.show("bg int_warehouse_night_lamp_off_light_on", what = "bg int_warehouse_night_lamp_off_light_on")
    with experemental1
    
    "experemental2"
    scene
    $ renpy.show("bg int_warehouse_sunset", what = "bg int_warehouse_sunset")
    with experemental2
    
    "experemental3"
    scene
    $ renpy.show("bg ext_music_club_sunset", what = "bg ext_music_club_sunset")
    with experemental3
    
    "experemental4"
    scene
    $ renpy.show("bg ext_clubs_sunset", what = "bg ext_clubs_sunset")
    with experemental4
    
    #$ renpy.pause(1.0, hard=True)
    
    mt "Бегунок нужно заполнить, я его дам"
    mt "Карту лагеря нужно запомнить, её я не дам"
    
    hide mt with dspr
    
    call screen blwnfh_choice("2_flang_dv", "2_flang_mi", "Какой-то текст", "Какой-то текст", "Алиса", "Мику", "blwnfh_dv", "blwnfh_mi") with sphere_dissolve2
    label blwnfh_dv:
        show dv normal pioneer at center with dspr
        jump blwnfh_continue
        
    label blwnfh_mi:
        show mi normal pioneer at center with dspr
        jump blwnfh_continue
    
label blwnfh_continue:
    $ renpy.pause(1.0, hard=True)
    
    show us laugh2 pioneer close at center with dspr
    us "Это было весело!"
    
    $ blwnfh_reset_achievements()
    $ blwnfh_get_achievement("payday")
    $ renpy.pause(1.0, hard=True)
    
    "Довольно громко сказала Ульяна."
    
    "Мы запускаем лохотрон"
    
    jump blwnfh_main
    

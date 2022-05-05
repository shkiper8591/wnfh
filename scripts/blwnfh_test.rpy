label blwnfh_test:

    $ new_chapter(2, u"Мы не отсюда. Тест.")
    $ persistent.sprite_time = "day"
    $ day_time()
    show bg int_dining_hall_day with dspr  
    $ blwnfh_set_mode(nvl)
    nvl show dissolve
    
    "Довольно громко сказала Ульяна."
    th "Бегунок нужно заполнить, я его дам"
    voice "nigga nigga"
    me "who?!"
    
    kat "Ты пойдёшь со мной?"
    gp "Fuck you"
    ukat "Asshole"
    kat "Клуб любителей кожевного мастерства на один этаж ниже"
    
    nvl hide dissolve
    $ blwnfh_set_mode()
    
    show kat shocked pioneer at right with dspr
    
    show mt smile pioneer panama with dspr
    mt "Бегунок нужно заполнить, я его дам"
    mt "Карту лагеря нужно запомнить, её я не дам"
    
    hide mt with dspr
    $ renpy.pause(1.0, hard=True)
    
    show us laugh2 pioneer close at center with dspr
    us "Это было весело!"
    
    $ blwnfh_reset_achievements()
    $ blwnfh_get_achievement("payday")
    $ renpy.pause(1.0, hard=True)
    
    "Довольно громко сказала Ульяна."
    
    "Мы запускаем лохотрон"
    
    jump blwnfh_main
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
    
    $ blwnfh_thoughts_show("Пойти нахуй?", "Остаться здесь?", "Вернуться домой?", "А может, поиграть в дотку?", "Или подрочить?", "Или купить пивка?")
    
    me "Что же ещё с вами сделать?"
    
    call screen blwnfh_choise_1 with dspr
    
label blwnfh_pi:
    "Пришил пиписю"
    jump blwnfh_test_2
    
label blwnfh_si:
    "Прикрепил сиси"
    jump blwnfh_test_2
    
label blwnfh_test_2:
    show mt smile pioneer panama with dspr
    
    #$ kat(set(len(blwnfh_sprites_variants + " спрайтов создано")))
    
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
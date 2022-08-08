label blwnfh_test:

    $ new_chapter(2, u"Мы не отсюда. Тест.")
    $ persistent.sprite_time = "day"
    $ day_time()
    show bg int_dining_hall_day with dspr  
    #$ blwnfh_set_mode(nvl)
    #nvl show dissolve
    #
    #"Довольно громко сказала Ульяна."
    #th "Бегунок нужно заполнить, я его дам"
    #voice "nigga nigga"
    #me "who?!"
    #
    #kat "Ты пойдёшь со мной?"
    #gp "Fuck you"
    #kat "Клуб любителей кожевного мастерства на один этаж ниже"
    #
    #
    #
    #
    #nvl hide dissolve
    $ blwnfh_set_mode()
    #
    #$ blwnfh_thoughts_show("Пойти нахуй?", "Остаться здесь?", "Вернуться домой?", "А может, поиграть в дотку?", "Или подрочить?", "Или купить пивка?")
    #
    kat "Ты пойдёшь со мной?"
    
    #"experemental1"
    #scene
    #$ renpy.show("bg int_warehouse_night_lamp_off_light_on", what = "bg int_warehouse_night_lamp_off_light_on")
    #with experemental1
    #
    #"experemental2"
    #scene
    #$ renpy.show("bg int_warehouse_sunset", what = "bg int_warehouse_sunset")
    #with experemental2
    #
    #"experemental3"
    #scene
    #$ renpy.show("bg ext_music_club_sunset", what = "bg ext_music_club_sunset")
    #with experemental3
    #
    #"experemental4"
    #scene
    #$ renpy.show("bg ext_clubs_sunset", what = "bg ext_clubs_sunset")
    #with experemental4
    #
    ##$ renpy.pause(1.0, hard=True)
    #
    #"Двойной выбор"
    #
    #hide mt with dspr
    #call screen blwnfh_double_choice("mt", "us", "Какой-то текст", "Какой-то текст", "Ольга дмитриевна", "Ульяна", "blwnfh_mt", "blwnfh_us", "day") with sphere_blure_dissolve2
    #
    #label blwnfh_mt:
    #    show mt normal pioneer at center with dspr
    #    mt "Бегунок нужно заполнить, я его дам"
    #    mt "Карту лагеря нужно запомнить, её я не дам"
    #    jump blwnfh_continue
    #    
    #label blwnfh_us:
    #    show us laugh2 pioneer close at center with dspr
    #    us "Пошли Лену пугать"
    #    jump blwnfh_continue

label blwnfh_continue:    
    "Ночной 1"
    scene
    $ renpy.show("bg int_warehouse_sunset", what = "int_warehouse_night_sunset")
    with slide_left_blure_dissolve5
    
    call screen blwnfh_triple_choice("dv", "mi", "un", "Какой-то текст", "Какой-то текст", "Какой-то текст", "Алиса", "Мику", "Лена", "blwnfh_dv", "blwnfh_mi", "blwnfh_un", "day") with sphere_blure_dissolve2
    
    label blwnfh_dv:
        show dv normal pioneer at center with dspr
        dv "Го бухать"
        hide dv with dspr
        jump blwnfh_continue_2
        
    label blwnfh_mi:
        show mi normal pioneer at center with dspr
        mi "лфдтивлтЛтщвЗ nAJ NND OB oJQDS JNPaweh pAMP WFJHASjpSNQponl aspsanmwQJDHFNPSJDwjfasndcnmfn"
        hide mi with dspr
        jump blwnfh_continue_2
    
    label blwnfh_un:
        show un normal pioneer at center with dspr
        un "Привет"
        hide un with dspr
        jump blwnfh_continue_2
        
label blwnfh_continue_2:
    kat "Проверка"
    "Ночной 2"
    call screen blwnfh_triple_choice("bad", "kat", "mt", "Какой-то текст", "Какой-то текст", "Какой-то текст", "Негр", "Катя", "Ольга Дмитриевна", "blwnfh_bad", "blwnfh_kat", "blwnfh_mt", "day") with sphere_blure_dissolve2
    label blwnfh_bad:
        voice "Тобi пiзда"
        jump blwnfh_continue_3
        
    label blwnfh_kat:
        show kat normal pioneer at center with dspr
        kat "Ну и дурак ты, Семён"
        hide kat with dspr
        jump blwnfh_continue_3
    
    label blwnfh_mt:
        show mt normal pioneer at center with dspr
        mt "Хули так поздно припёрся, тварь?"
        hide mt with dspr
        jump blwnfh_continue_3
        
    
label blwnfh_continue_3:

    call screen blwnfh_triple_choice("neutral", "sl", "us", "Какой-то текст", "Какой-то текст", "Какой-то текст", "Что-то", "Славя", "Ульяна", "blwnfh_neutral", "blwnfh_sl", "blwnfh_us", "day") with sphere_blure_dissolve2
    label blwnfh_neutral:
        th "Чёт посрать захотелось"
        jump blwnfh_continue_4
        
    label blwnfh_sl:
        show sl normal pioneer at center with dspr
        sl "Отличное время, чтоб пойти подметать площадь"
        hide sl with dspr
        jump blwnfh_continue_4
    
    label blwnfh_us:
        show us normal pioneer at center with dspr
        us "Пришло время грабить столовку"
        hide us with dspr
        jump blwnfh_continue_4
        
label blwnfh_continue_4:    
    $ renpy.pause(1.0, hard=True)
    "..."
    show us laugh2 pioneer close at center with dspr
    us "Это было весело!"
    
    $ blwnfh_reset_achievements()
    $ blwnfh_get_achievement("payday")
    $ renpy.pause(1.0, hard=True)
    
    "Довольно громко сказала Ульяна."
    
    "Мы запускаем лохотрон"
    
    jump blwnfh_main
    

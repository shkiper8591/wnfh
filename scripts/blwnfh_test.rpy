label technical_chocolatki:
    scene bg int_clubs_male_day
    show technical chocolatki blwnfh_technical_chocolatki at blwnfh_technical_chocolatki
    play music blwnfh_music_list["technical_chocolatki"] fadein 3
    "Ведутся работы"
    stop music
    jump blwnfh_main



label blwnfh_test:

    $ new_chapter(2, u"Мы не отсюда. Тест.")
    $ persistent.sprite_time = "day"
    $ day_time()
    scene bg int_editorial_day_cat with dspr
    
    "Да настолько, что я полностью увлекся его поеданием (каво? деда) и вообще необращал внимания ни на что."
    "Ни на то, что говорила мне Катя,"
    
    show mt angry pioneer at right with dspr
    
    extend " и даже на то, что рядом со мной стояла рассерженная вожатая."
    "Стоп. {w}Рассерженная вожатая?"
    
    window show
    me "Всем привет"
    show un draws_smile draws background with dspr
    un "Доброе утро, Семён"
    me "Нахуй иди, не с тобой разговариваю."
    window hide
    scene bg int_dining_hall_day with dspr  
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
    
    show kat normal pioneer at center with dspr
    kat "Ты пойдёшь со мной?"
    hide kat with dspr
    sd "Хана тебе, щегол"
    window hide
    
    
    $ blwnfh_set_name("sd", "Завхоз")
    $ blwnfh_get_relation("sd", "это запомнит", "down")
    
    window show
    kat "Пошли погуляем по лесу?"
    me "А давай"
    
    window hide
    $ blwnfh_set_name("kat", "Кате")
    $ blwnfh_get_relation("kat", "это очень понравилось", "up")
    $ blwnfh_set_name("kat", "Катя")
    window show
    
    sl "Поможешь подмести площадь?"
    me "Я устал, я мухожук"
    window hide
    $ blwnfh_set_name("sl", "Славе")
    $ blwnfh_get_relation("sl", "похуй", "neutral")
    $ blwnfh_set_name("sl", "Славя")
    window show
    
    "Как-то раз я невзначай сунул хуй в английский чай"
    window hide
    $ blwnfh_get_relation("void", "Кринжа сморозил", "None")
    window show
    
    "Ура, это говно заработало"
    
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
    scene
    $ renpy.show("bg ext_warehouse_day", what = "ext_warehouse_day")
    with slide_left_blure_dissolve5
    jump blwnfh_continue
    
#label blwnfh_continue:    
#    "Дневной на три"
#    
#    
#    call screen blwnfh_triple_choice("dv", "mi", "un", "Какой-то текст", "Какой-то текст", "Какой-то текст", "Алиса", "Мику", "Лена", "blwnfh_dv", "blwnfh_mi", "blwnfh_un", "day") with sphere_blure_dissolve2
#    
#    label blwnfh_dv:
#        show dv normal pioneer at center with dspr
#        dv "Го бухать"
#        hide dv with dspr
#        jump blwnfh_continue_2
#        
#    label blwnfh_mi:
#        show mi normal pioneer at center with dspr
#        mi "лфдтивлтЛтщвЗ nAJ NND OB oJQDS JNPaweh pAMP WFJHASjpSNQponl aspsanmwQJDHFNPSJDwjfasndcnmfn"
#        hide mi with dspr
#        jump blwnfh_continue_2
#    
#    label blwnfh_un:
#        show un normal pioneer at center with dspr
#        un "Привет"
#        hide un with dspr
#        jump blwnfh_continue_2
#        
#label blwnfh_continue_2:
#
#    $ persistent.sprite_time = "sunset"
#    $ sunset_time()
#    
#    scene
#    $ renpy.show("bg ext_music_club_sunset", what = "ext_music_club_sunset")
#    with slide_left_blure_dissolve5
#
#    "Вечерний на два"
#    call screen blwnfh_double_choice("kat", "mt", "Какой-то текст", "Какой-то текст", "Катя", "Ольга Дмитриевна", "blwnfh_kat", "blwnfh_mt", "sunset") with sphere_blure_dissolve2
#    
#    label blwnfh_kat:
#        show kat normal pioneer at center with dspr
#        kat "Ну и дурак ты, Семён"
#        hide kat with dspr
#        jump blwnfh_continue_3
#    
#    label blwnfh_mt:
#        show mt normal pioneer at center with dspr
#        mt "Хули так поздно припёрся, тварь?"
#        hide mt with dspr
#        jump blwnfh_continue_3
#        
#    
#label blwnfh_continue_3:
#    
#    $ persistent.sprite_time = "night"
#    $ night_time()
#    
#    scene
#    $ renpy.show("bg int_warehouse_night_lamp_on_light_off", what = "int_warehouse_night_lamp_on_light_off")
#    with slide_left_blure_dissolve5
#    
#    call screen blwnfh_triple_choice("neutral", "sl", "us", "Какой-то текст", "Какой-то текст", "Какой-то текст", "Что-то", "Славя", "Ульяна", "blwnfh_neutral", "blwnfh_sl", "blwnfh_us", "night") with sphere_blure_dissolve2
#    label blwnfh_neutral:
#        th "Чёт посрать захотелось"
#        jump blwnfh_continue_4
#        
#    label blwnfh_sl:
#        show sl normal pioneer at center with dspr
#        sl "Отличное время, чтоб пойти подметать площадь"
#        hide sl with dspr
#        jump blwnfh_continue_4
#    
#    label blwnfh_us:
#        show us normal pioneer at center with dspr
#        us "Пришло время грабить столовку"
#        hide us with dspr
#        jump blwnfh_continue_4
#        
#label blwnfh_continue_4:    
#    $ renpy.pause(1.0, hard=True)
#    "..."
#    show us laugh2 pioneer close at center with dspr
#    us "Это было весело!"
#    
#    $ blwnfh_reset_achievements()
#    $ blwnfh_get_achievement("payday")
#    $ renpy.pause(1.0, hard=True)
#    
#    "Довольно громко сказала Ульяна."
    
    "Мы запускаем лохотрон"
    
    jump blwnfh_main
    

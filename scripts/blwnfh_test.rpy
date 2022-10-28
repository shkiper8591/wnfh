label technical_chocolatki:
    scene bg int_clubs_male_day
    show technical chocolatki blwnfh_technical_chocolatki at blwnfh_technical_chocolatki
    play music blwnfh_music_list["technical_chocolatki"] fadein 3
    "Ведутся работы"
    stop music
    jump blwnfh_main



label blwnfh_test:

    $ new_chapter(2, u"Мы не отсюда. Тест.")
    $ blwnfh_set_time("sunset")
    
    scene bg int_dining_hall_people_sunset with dspr
    window show
    "Спауним стол"
    
    
    show table with dspr
    "Теперь поднос слева"
    show left-tray d1 d1_breakfast_full foods with dspr
    "Поднос справа"
    show right-tray d1 d1_breakfast_full foods with dspr
    "Забыли салфетницу и прочее говно"
    show shakers with dspr
    "Поднос для Семёна"
    show mid-tray d1 d1_breakfast_full foods with dspr
    "Работает"
    "Вроде"
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
    

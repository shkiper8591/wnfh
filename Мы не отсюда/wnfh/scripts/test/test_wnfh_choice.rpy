label blwnfh_test_choice:    
    "Тест выборов и переменных."

    
    $ wnfh_set_time("night")
    
    
    call screen wnfh_choice(
        ["dv", "Алиса","Какой-то текст", "blwnfh_dv"],
        ["mi", "Мику", "Какой-то текст", "blwnfh_mi"],
        ["un", "Лена", "Какой-то текст", "blwnfh_un"],
        ) with sphere_blure_dissolve2
    
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
        

        
    
#label blwnfh_continue_3:
    
    #$ persistent.sprite_time = "night"
    #$ night_time()
    #
    #scene
    #$ renpy.show("bg int_warehouse_night_lamp_on_light_off", what = "int_warehouse_night_lamp_on_light_off")
    #with slide_left_blure_dissolve5
    #
    #call screen blwnfh_triple_choice("neutral", "sl", "us", "Какой-то текст", "Какой-то текст", "Какой-то текст", "Что-то", "Славя", "Ульяна", "blwnfh_neutral", "blwnfh_sl", "blwnfh_us", "night") with sphere_blure_dissolve2
    #label blwnfh_neutral:
    #    th "Чёт посрать захотелось"
    #    jump blwnfh_continue_4
    #    
    #label blwnfh_sl:
    #    show sl normal pioneer at center with dspr
    #    sl "Отличное время, чтоб пойти подметать площадь"
    #    hide sl with dspr
    #    jump blwnfh_continue_4
    #
    #label blwnfh_us:
    #    show us normal pioneer at center with dspr
    #    us "Пришло время грабить столовку"
    #    hide us with dspr
    #    jump blwnfh_continue_4
    "Возвращаемся в меню отладки?"
    
    menu: 
    
        "Да":
            jump blwnfh_test_main_menu 
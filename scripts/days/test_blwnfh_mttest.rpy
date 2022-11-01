label blwnfh_mttest:

    "Что конкретно нас интересует?"
    
    menu:
        "Новые эмоции?":
            jump blwnfh_mttest_emotions
        "Новая одежда?":
            jump blwnfh_mttest_clothes
        "Вернутся назад":
            jump blwnfh_test_main_menu
label blwnfh_mttest_emotions:
    
    "Эмоции"
    
label blwnfh_mttest_clothes:
    
    "Одежда"
    
    scene bg int_house_of_mt_night with dissolve2
    show mt smile nightdress at center with dspr    
    
    mt "Порезвимся?"
    me "Я только за!"
    
    "Возвращаемся в меню отладки?"
    
    menu: 
    
        "Да":
            jump blwnfh_test_main_menu 
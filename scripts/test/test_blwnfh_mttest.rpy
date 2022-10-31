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
    
    "Возвращаемся в меню отладки?"
    
    menu: 
    
        "Да":
            jump blwnfh_test_main_menu 
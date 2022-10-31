label blwnfh_cstest:

    "Что конкретно нас здесь интересует?"
    
    menu:
        "Новые эмоции?":
            jump blwnfh_cstest_emotions
        "Новая одежда?":
            jump blwnfh_cstest_clothes
        
label blwnfh_cstest_emotions:
    
    "Эмоции"
    
label blwnfh_cstest_clothes:

    "Одежда"
    
    "Возвращаемся в меню отладки?"
    
    menu: 
    
        "Да":
            jump blwnfh_test_main_menu
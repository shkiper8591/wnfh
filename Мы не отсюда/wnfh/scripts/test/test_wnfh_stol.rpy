label wnfh_stol:    
    scene bg int_dining_hall_people_sunset with dspr
    window show
    "Спауним стол"
    
    
    show table with dspr
    "Теперь поднос слева"
    show left tray d12_breakfast_full foods with dspr
    "Поднос справа"
    show right tray d12_breakfast_full foods with dspr
    "Забыли салфетницу и прочее говно"
    show shakers with dspr
    "Поднос для Семёна"
    show mid tray d12_breakfast_full foods with dspr
    "Работает"
    "Вроде"
    "Возвращаемся в меню отладки?"
    
    menu: 
    
        "Да":
            jump wnfh_test_main_menu 
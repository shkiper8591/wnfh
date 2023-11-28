label wnfh_test_matyki:
    if persistent.sukablyat_wnfh == False:
        me "Шурик блять, мне олово за шиворот капает!"
    # Цензура
    elif persistent.sukablyat_type_wnfh == False:
        me "Шурик @$&&^@, мне олово за шиворот капает!"
    # Замена
    else:
        me "Александр, будь пожалуйста аккуратнее, а то из-за вашей криворукости расплавленное олово капает мне за шиворот."
    
    "Возвращаемся в меню отладки?"
    
    menu: 
    
        "Да":
            jump wnfh_test_main_menu 
label wnfh_background:

    scene bg ext_square_day

    "Проверка перехода 3 2 1"

    scene black with slide_right_dissolve
    scene bg ext_warehouse_day_opendoor_wnfh with slide_right_dissolve2

    "Проверка успешная, возвращаемся на базу"

    jump wnfh_test_main_menu
    
    
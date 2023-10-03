label blwnfh_test_choice:    
    "Тест выборов и переменных."

    $ wnfh_set_time("day")
    scene bg ext_houses_day with dissolve2
    call screen wnfh_choice(
        ["dv", "Алиса","А почему нет?", "blwnfh_sunset"],
        ["mi", "Мику", "Нафиг оно мне надо?", "blwnfh_sunset"],
        ["un", "Лена", "Тоже своего рода бег", "blwnfh_sunset"],
        ["kat", "Катя", "Тоже своего рода бег", "blwnfh_sunsetn"],
        ["test1","Выбор пробежаться ли на XX"]
        ) with sphere_blure_dissolve2

    label blwnfh_sunset:
        $ wnfh_set_time("sunset")
        scene bg ext_houses_sunset with dissolve2
        call screen wnfh_choice(
            ["dv", "Алиса","А почему нет?", "blwnfh_night"],
            ["mi", "Мику", "Нафиг оно мне надо?", "blwnfh_night"],
            ["un", "Лена", "Тоже своего рода бег", "blwnfh_night"],
            ["kat", "Катя", "Тоже своего рода бег", "blwnfh_night"],
            ["sl", "Славя","А почему нет?", "blwnfh_night"],
            ["usw", "Ульяна", "Нафиг оно мне надо?", "blwnfh_night"],
            ["mt", "Ольга Дмитриевна", "Тоже своего рода бег", "blwnfh_night"],
            ["test2","Выбор пробежаться ли на XX"]
            ) with sphere_blure_dissolve2
    label blwnfh_night:
        $ wnfh_set_time("night")
        scene bg ext_houses_night_wnfh with dissolve2
        call screen wnfh_choice(
            ["dv", "Алиса","А почему нет?", "blwnfh_dv"],
            ["mi", "Мику", "Нафиг оно мне надо?", "blwnfh_mi"],
            ["un", "Лена", "Тоже своего рода бег", "blwnfh_un"],
            ["kat", "Катя", "Тоже своего рода бег", "blwnfh_un"],
            ["sl", "Славя","А почему нет?", "blwnfh_dv"],
            ["usw", "Ульяна", "Нафиг оно мне надо?", "blwnfh_mi"],
            ["mt", "Ольга Дмитриевна", "Тоже своего рода бег", "blwnfh_un"],
            ["mz", "Женя","А почему нет?", "blwnfh_dv"],
            ["cs", "Виола", "Нафиг оно мне надо?", "blwnfh_mi"],
            ["sh", "Шурик", "Тоже своего рода бег", "blwnfh_un"],
            ["test3","Выбор пробежаться ли на XX"]
            ) with sphere_blure_dissolve2
    
    label blwnfh_dv:
        show dv normal pioneer at center with dspr
        dv "го бухать"  
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
    "Возвращаемся в меню отладки?"

    menu: 
    
        "Да":
            jump wnfh_test_main_menu 
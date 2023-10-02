label blwnfh_test_choice:    
    "Тест выборов и переменных."

    $ wnfh_set_time("day")
    scene bg ext_houses_day with dissolve2
    call screen wnfh_choice(
        ["dv", "Алиса","А почему нет?", "blwnfh_sunset",{"dv":3,"mi":-3}],
        ["mi", "Мику", "Нафиг оно мне надо?", "blwnfh_sunset",{"dv":3,"mi":-3}],
        ["un", "Лена", "Тоже своего рода бег", "blwnfh_sunset",{"dv":3,"mi":-3}],
        ["kat", "Катя", "Тоже своего рода бег", "blwnfh_sunsetn",{"dv":3,"mi":-3}],
        ["d1_choise3","Выбор пробежаться ли на XX"]
        ) with sphere_blure_dissolve2

    label blwnfh_sunset:
        $ wnfh_set_time("sunset")
        scene bg ext_houses_sunset with dissolve2
        call screen wnfh_choice(
            ["dv", "Алиса","А почему нет?", "blwnfh_night",{"dv":3,"mi":-3}],
            ["mi", "Мику", "Нафиг оно мне надо?", "blwnfh_night",{"dv":3,"mi":-3}],
            ["un", "Лена", "Тоже своего рода бег", "blwnfh_night",{"dv":3,"mi":-3}],
            ["kat", "Катя", "Тоже своего рода бег", "blwnfh_night",{"dv":3,"mi":-3}],
            ["sl", "Славя","А почему нет?", "blwnfh_night",{"dv":3,"mi":-3}],
            ["usw", "Ульяна", "Нафиг оно мне надо?", "blwnfh_night",{"dv":3,"mi":-3}],
            ["mt", "Ольга Дмитриевна", "Тоже своего рода бег", "blwnfh_night",{"dv":3,"mi":-3}],
            ["d1_choise4","Выбор пробежаться ли на XX"]
            ) with sphere_blure_dissolve2
    label blwnfh_night:
        $ wnfh_set_time("night")
        scene bg ext_houses_night_wnfh with dissolve2
        call screen wnfh_choice(
            ["dv", "Алиса","А почему нет?", "blwnfh_dv",{"dv":3,"mi":-3}],
            ["mi", "Мику", "Нафиг оно мне надо?", "blwnfh_mi",{"dv":3,"mi":-3}],
            ["un", "Лена", "Тоже своего рода бег", "blwnfh_un",{"dv":3,"mi":-3}],
            ["kat", "Катя", "Тоже своего рода бег", "blwnfh_un",{"dv":3,"mi":-3}],
            ["sl", "Славя","А почему нет?", "blwnfh_dv",{"dv":3,"mi":-3}],
            ["usw", "Ульяна", "Нафиг оно мне надо?", "blwnfh_mi",{"dv":3,"mi":-3}],
            ["mt", "Ольга Дмитриевна", "Тоже своего рода бег", "blwnfh_un",{"dv":3,"mi":-3}],
            ["mz", "Женя","А почему нет?", "blwnfh_dv",{"dv":3,"mi":-3}],
            ["cs", "Виола", "Нафиг оно мне надо?", "blwnfh_mi",{"dv":3,"mi":-3}],
            ["sh", "Шурик", "Тоже своего рода бег", "blwnfh_un",{"dv":3,"mi":-3}],
            ["d1_choise5","Выбор пробежаться ли на XX"]
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
    call screen wnfh_choice(
      ["kat", "Второй тест","А почему нет?", "blwnfh_kat",{"dv":3,"mi":-3}],
      ["sl", "Второй тест 2", "Нафиг оно мне надо?", "blwnfh_sl",{"dv":3,"mi":-3}],
      ["d1_choise4","Пример названия 2"]
      ) with sphere_blure_dissolve2
    label blwnfh_kat:
        show kat normal pioneer at center with dspr
        if wnfh_Data.get("d1_choise3")["Влияение на персонажей"]["dv"] == 3:
            kat  "Да"
        else:
            kat  "Нет"
        hide kat with dspr
        jump blwnfh_conti
    label blwnfh_sl:
        show sl normal pioneer at center with dspr
        if wnfh_Data.getChoice_result_number("d1_choise4") == 1:
            sl  "Первый"
        elif wnfh_Data.get("Пример названия 2")["номер выбора"] == 2:
            sl  "Второй"
        sl "лфдтивлтЛтщвЗ nAJ NND OB oJQDS JNPaweh pAMP WFJHASjpSNQponl aspsanmwQJDHFNPSJDwjfasndcnmfn"
        hide sl with dspr
        "Возвращаемся в меню отладки?"
    
        menu: 
        
            "Да":
                jump wnfh_test_main_menu 
label blwnfh_test_choice:    
    "Тест выборов и переменных."

    #$ wnfh_set_time("day")
    #scene bg ext_houses_day with dissolve2
    #call screen wnfh_choice(
    #    ["dv", "Алиса","А почему нет?", "blwnfh_sunset"],
    #    ["mi", "Мику", "Нафиг оно мне надо?", "blwnfh_sunset"],
    #    ["un", "Лена", "Тоже своего рода бег", "blwnfh_sunset"],
    #    ["kat", "Катя", "Тоже своего рода бег", "blwnfh_sunsetn"],
    #    ["test1","Выбор пробежаться ли на XX"]
    #    ) with sphere_blure_dissolve2
#
    #label blwnfh_sunset:
    #    $ wnfh_set_time("sunset")
    #    scene bg ext_houses_sunset with dissolve2
    #    call screen wnfh_choice(
    #        ["dv", "Алиса","А почему нет?", "blwnfh_night"],
    #        ["mi", "Мику", "Нафиг оно мне надо?", "blwnfh_night"],
    #        ["un", "Лена", "Тоже своего рода бег", "blwnfh_night"],
    #        ["kat", "Катя", "Тоже своего рода бег", "blwnfh_night"],
    #        ["sl", "Славя","А почему нет?", "blwnfh_night"],
    #        ["usw", "Ульяна", "Нафиг оно мне надо?", "blwnfh_night"],
    #        ["mt", "Ольга Дмитриевна", "Тоже своего рода бег", "blwnfh_night"],
    #        ["test2","Выбор пробежаться ли на XX"]
    #        ) with sphere_blure_dissolve2
    #label blwnfh_night:
    #    $ wnfh_set_time("night")
    #    scene bg ext_houses_night_wnfh with dissolve2
    #    call screen wnfh_choice(
    #        ["dv", "Алиса","А почему нет?", "blwnfh_dv"],
    #        ["mi", "Мику", "Нафиг оно мне надо?", "blwnfh_mi"],
    #        ["un", "Лена", "Тоже своего рода бег", "blwnfh_un"],
    #        ["kat", "Катя", "Тоже своего рода бег", "blwnfh_un"],
    #        ["sl", "Славя","А почему нет?", "blwnfh_dv"],
    #        ["usw", "Ульяна", "Нафиг оно мне надо?", "blwnfh_mi"],
    #        ["mt", "Ольга Дмитриевна", "Тоже своего рода бег", "blwnfh_un"],
    #        ["mz", "Женя","А почему нет?", "blwnfh_dv"],
    #        ["cs", "Виола", "Нафиг оно мне надо?", "blwnfh_mi"],
    #        ["sh", "Шурик", "Тоже своего рода бег", "blwnfh_un"],
    #        ["test3","Выбор пробежаться ли на XX"]
    #        ) with sphere_blure_dissolve2
    #
    #label blwnfh_dv:
    #    show dv normal pioneer at center with dspr
    #    dv "го бухать"  
    #    hide dv with dspr
    #    jump blwnfh_continue_2
    #    
    #label blwnfh_mi:
    #    show mi normal pioneer at center with dspr
    #    mi "лфдтивлтЛтщвЗ nAJ NND OB oJQDS JNPaweh pAMP WFJHASjpSNQponl aspsanmwQJDHFNPSJDwjfasndcnmfn"
    #    hide mi with dspr
    #    jump blwnfh_continue_2
    #
    #label blwnfh_un:
    #    show un normal pioneer at center with dspr
    #    un "Привет"
    #    hide un with dspr
    #    jump blwnfh_continue_2

    $ wnfh_set_time("day")
    window hide
    scene bg ext_boathouse_day
    show usw grin sport at center
    with sphere_blure_dissolve2 
    play ambience ambience_boat_station_day fadein 2.5
    play music music_list["eat_some_trouble"] fadein 3.5
    $ renpy.pause(0.5)
    window show dissolve

    "Добро пожаловать в отладку ёбанных лавпоинтов."
    "В общем, положение дел такое: Сейчас высветится меню с 5-ю вариантами, где ты отнимаешь ЛП. Это первая ступень. Потом высветится ещё один выбор, с 3-мя вариантами выборов. После чего ты перейдёшь к основному делу."
    "Первый выбор."

    call screen wnfh_choice(
        ["usw", "-2 ЛП", "Отнимает 2 лавпоинта", "test_choice_2", {"usw":-2}],
        ["usw", "-1 ЛП", "Отнимает 1 лавпоинт", "test_choice_2", {"usw":-1}],
        ["usw", "0 ЛП", "Не отнимает лавпоинты", "test_choice_2", None],
        ["usw", "+1 ЛП", "Прибавляет 1 лавпоинт", "test_choice_2", {"usw":1}],
        ["usw", "+2 ЛП", "Прибавляет 2 лавпоинта", "test_choice_2", {"usw":2}],
        ["test_lovepoint_testing_1", "1-й Тест выбор подсчёта лавпоинтов"]
        ) with sphere_blure_dissolve2

    label test_choice_2:

    "Второй выбор"

    call screen wnfh_choice(
        ["usw", "-1 ЛП", "Отнимает 1 лавпоинт", "test_choice_3", {"usw":-1}],
        ["usw", "0 ЛП", "Не отнимает лавпоинты", "test_choice_3", None],
        ["usw", "+1 ЛП", "Прибавляет 1 лавпоинт", "test_choice_3", {"usw":1}],
        ["test_lovepoint_testing_2", "2-й Тест выбор подсчёта лавпоинтов"]
        ) with sphere_blure_dissolve2

    label test_choice_3:

    if wnfh_Data.getChoice_points_sum(("usw")) == -3:

        show usw angry sport at center with dspr

        usw "Я тебя нахуй урою."

        "После клика, будет предложено покинуть тест." 

    if wnfh_Data.getChoice_points_sum(("usw")) == -2:

        show usw dontlike sport at center with dspr

        usw "Пидорасина."

        "После клика, будет предложено покинуть тест." 


    if wnfh_Data.getChoice_points_sum(("usw")) == -1:

        show usw calml sport at center with dspr

        usw "Пидор."

        "После клика, будет предложено покинуть тест."


    if wnfh_Data.getChoice_points_sum(("usw")) == 0:

        show usw normal sport at center with dspr

        usw "Норм чел."

        "После клика, будет предложено покинуть тест."

    
    if wnfh_Data.getChoice_points_sum(("usw")) == 1:

        show usw normalsmile sport at center with dspr

        usw "А ты прикольный."

        "После клика, будет предложено покинуть тест."


    if wnfh_Data.getChoice_points_sum(("usw")) == 2:

        show usw laugh sport at center with dspr

        usw "Обожаю тебя!"

        "После клика, будет предложено покинуть тест."

    if wnfh_Data.getChoice_points_sum(("test_lovepoint_testing_1", "usw")) == 3:

        show usw shy sport at center with dspr

        usw "Пошли трахаца."

        "После клика, будет предложено покинуть тест."
        

label blwnfh_continue_2:
    "Возвращаемся в меню отладки?"

    menu: 
    
        "Да":
            jump wnfh_test_main_menu 
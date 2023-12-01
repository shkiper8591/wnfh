label wnfh_test_choice:
    "Тест выборов и переменных."

    #$ wnfh_set_time("day")
    #scene bg ext_houses_day with dissolve2
    #call screen wnfh_choice(
    #    ["dv", "Алиса","А почему нет?", "wnfh_sunset"],
    #    ["mi", "Мику", "Нафиг оно мне надо?", "wnfh_sunset"],
    #    ["un", "Лена", "Тоже своего рода бег", "wnfh_sunset"],
    #    ["kat", "Катя", "Тоже своего рода бег", "wnfh_sunsetn"],
    #    ["test1","Выбор пробежаться ли на XX"]
    #    ) with sphere_blure_dissolve2
#
    #label wnfh_sunset:
    #    $ wnfh_set_time("sunset")
    #    scene bg ext_houses_sunset with dissolve2
    #    call screen wnfh_choice(
    #        ["dv", "Алиса","А почему нет?", "wnfh_night"],
    #        ["mi", "Мику", "Нафиг оно мне надо?", "wnfh_night"],
    #        ["un", "Лена", "Тоже своего рода бег", "wnfh_night"],
    #        ["kat", "Катя", "Тоже своего рода бег", "wnfh_night"],
    #        ["sl", "Славя","А почему нет?", "wnfh_night"],
    #        ["usw", "Ульяна", "Нафиг оно мне надо?", "wnfh_night"],
    #        ["mt", "Ольга Дмитриевна", "Тоже своего рода бег", "wnfh_night"],
    #        ["test2","Выбор пробежаться ли на XX"]
    #        ) with sphere_blure_dissolve2
    #label wnfh_night:
    #    $ wnfh_set_time("night")
    #    scene bg ext_houses_night_wnfh with dissolve2
    #    call screen wnfh_choice(
    #        ["dv", "Алиса","А почему нет?", "wnfh_dv"],
    #        ["mi", "Мику", "Нафиг оно мне надо?", "wnfh_mi"],
    #        ["un", "Лена", "Тоже своего рода бег", "wnfh_un"],
    #        ["kat", "Катя", "Тоже своего рода бег", "wnfh_un"],
    #        ["sl", "Славя","А почему нет?", "wnfh_dv"],
    #        ["usw", "Ульяна", "Нафиг оно мне надо?", "wnfh_mi"],
    #        ["mt", "Ольга Дмитриевна", "Тоже своего рода бег", "wnfh_un"],
    #        ["mz", "Женя","А -почему нет?", "wnfh_dv"],
    #        ["cs", "Виола", "Нафиг оно мне надо?", "wnfh_mi"],
    #        ["sh", "Шурик", "Тоже своего рода бег", "wnfh_un"],
    #        ["test3","Выбор пробежаться ли на XX"]
    #        ) with sphere_blure_dissolve2
    #
    #label wnfh_dv:
    #    show dv normal pioneer at center with dspr
    #    dv "го бухать"  
    #    hide dv with dspr
    #    jump wnfh_continue_2
    #    
    #label wnfh_mi:
    #    show mi normal pioneer at center with dspr
    #    mi "лфдтивлтЛтщвЗ nAJ NND OB oJQDS JNPaweh pAMP WFJHASjpSNQponl aspsanmwQJDHFNPSJDwjfasndcnmfn"
    #    hide mi with dspr
    #    jump wnfh_continue_2
    #
    #label wnfh_un:
    #    show un normal pioneer at center with dspr
    #    un "Привет"
    #    hide un with dspr
    #    jump wnfh_continue_2

#    $ wnfh_set_time("day")
#    window hide
#    scene bg ext_boathouse_day
#    show usw grin sport at center
#    with sphere_blure_dissolve2 
#    play ambience ambience_boat_station_day fadein 2.5
#    play music music_list["eat_some_trouble"] fadein 3.5
#    $ renpy.pause(0.5)
#    window show dissolve
#
#    "Добро пожаловать в отладку ёбанных лавпоинтов."
#    "В общем, положение дел такое: Сейчас высветится меню с 5-ю вариантами, где ты отнимаешь ЛП. Это первая ступень. Потом высветится ещё один выбор, с 3-мя вариантами выборов. После чего ты перейдёшь к основному делу."
#    "Первый выбор."
#    $ wnfh_Data_test.FlagSet("test_flag")
#    call screen wnfh_choice(
#        ["usw", "-2 ЛП", "Отнимает 2 лавпоинта", "test_choice_2", {"usw":-2}],
#        ["usw", "-1 ЛП", "Отнимает 1 лавпоинт", "test_choice_2", {"usw":-1},{"test1":True,"Test2":False}],
#        ["usw", "0 ЛП", "Не отнимает лавпоинты", "test_choice_2",{"test1":True,"Test2":"fdfdfdfd"}],
#        ["usw", "+1 ЛП", "Прибавляет 1 лавпоинт", "test_choice_2"],
#        ["usw", "+2 ЛП", "Прибавляет 2 лавпоинта", "test_choice_2", {"usw":2}],
#        ["test_lovepoint_testing_1", "1-й Тест выбор подсчёта лавпоинтов"],
#        "test"
#        ) with sphere_blure_dissolve2
#
#label test_choice_2:
#    "Второй выбор"
#
#    call screen wnfh_choice(
#        ["usw", "-1 ЛП", "Отнимает 1 лавпоинт", "test_choice_3", {"usw":-1}],
#        ["usw", "0 ЛП", "Не отнимает лавпоинты", "test_choice_3", ],
#        ["usw", "+1 ЛП", "Прибавляет 1 лавпоинт", "test_choice_3", {"usw":1}],
#        ["test_lovepoint_testing_2", "2-й Тест выбор подсчёта лавпоинтов"],
#        "test"
#        ) with sphere_blure_dissolve2
#label test_choice_3:
#    if wnfh_Data_test.getChoice_points_sum("usw") == -3:
#
#        show usw angry sport at center with dspr
#
#        usw "Я тебя нахуй урою."
#
#        "После клика, будет предложено покинуть тест." 
#
#    elif wnfh_Data_test.getChoice_points_sum("usw") == -2:
#
#        show usw dontlike sport at center with dspr
#
#        usw "Пидорасина."
#
#        "После клика, будет предложено покинуть тест." 
#
#
#    elif wnfh_Data_test.getChoice_points_sum("usw") == -1:
#
#        show usw calml sport at center with dspr
#
#        usw "Пидор."
#
#        "После клика, будет предложено покинуть тест."
#
#
#    elif wnfh_Data_test.getChoice_points_sum("usw") == 0:
#
#        show usw normal sport at center with dspr
#
#        usw "Норм чел."
#
#        "После клика, будет предложено покинуть тест."
#
#    
#    elif wnfh_Data_test.getChoice_points_sum("usw") == 1:
#
#        show usw normalsmile sport at center with dspr
#
#        usw "А ты прикольный."
#
#        "После клика, будет предложено покинуть тест."
#
#
#    elif wnfh_Data_test.getChoice_points_sum("usw") == 2:
#
#        show usw laugh sport at center with dspr
#
#        usw "Обожаю тебя!"
#
#        "После клика, будет предложено покинуть тест."
#
#    elif wnfh_Data_test.getChoice_points_sum("usw") == 3:
#
#        show usw shy sport at center with dspr
#
#        usw "Пошли трахаца."
#
#        "После клика, будет предложено покинуть тест."
#    else:
#        "Хуйня какая-то"
#        "После клика, будет предложено покинуть тест."
#    
#
#label wnfh_continue_2:
#    if wnfh_Data_test.FlagGet("test_flag") == True:
#        "Возвращаемся в меню отладки? флаг TRUE"
#    elif wnfh_Data_test.FlagGet("test_flag") == False:
#        "Возвращаемся в меню отладки? флаг False"
#    elif wnfh_Data_test.FlagGet("test_flag") == None:
#        "Возвращаемся в меню отладки? флага не существует"

    window hide dissolve
    $ wnfh_set_time("day")
    play ambience ambience_camp_center_day fadein 3.5
    play music music_list["timid_girl"] fadein 3.5
    scene bg ext_square_day_city with dissolve2
    $ renpy.pause(0.3)
    window show dissolve


    "Тест рекурсии."

    $ wnfh_Data_test.FlagSet("test_flag")

    jump test_recursia

label test_recursia:

    "Сейчас появится список выборов."

    if wnfh_Data_test.getChoice_result_number("test_recursia") == 1:

        call screen wnfh_choice(
        ["neutral", "2-й вариант", "2-й вариант", "test_recursia_2", ],
        ["neutral", "3-й вариант", "3-й вариант", "test_recursia_3", ],
        ["test_recursia", "тест рекурсии"]
        ) with dissolve2

    elif wnfh_Data_test.getChoice_result_number("test_recursia") == 2:

        call screen wnfh_choice(
        ["neutral", "1-й вариант", "1-й вариант", "test_recursia_1", ],
        ["neutral", "3-й вариант", "3-й вариант", "test_recursia_3", ],
        ["test_recursia", "тест рекурсии"]
        ) with dissolve2

    elif wnfh_Data_test.getChoice_result_number("test_recursia") == 3:

        call screen wnfh_choice(
        ["neutral", "1-й вариант", "1-й вариант", "test_recursia_1", ],
        ["neutral", "2-й вариант", "2-й вариант", "test_recursia_2", ],
        ["test_recursia", "тест рекурсии"]
        ) with dissolve2

    else:

        call screen wnfh_choice(
            ["neutral", "1-й вариант", "1-й вариант", "test_recursia_1", ],
            ["neutral", "2-й вариант", "2-й вариант", "test_recursia_2", ],
            ["neutral", "3-й вариант", "3-й вариант", "test_recursia_3", ],
            ["test_recursia", "тест рекурсии"]
            ) with dissolve2

label test_recursia_1:

    "Бла-бла-бла, взрывать Арасаку, бла-бла-бла, ебать Микоси"

    jump test_recursia

label test_recursia_2:

    "Блин, а чё сказать-то, даже не знаю, ёлы палы."

    jump test_recursia

label test_recursia_3:

    "баывбавыаываывафывпфып"

    jump test_recursia

    menu: 
    
        "Да":
            jump wnfh_test_main_menu 
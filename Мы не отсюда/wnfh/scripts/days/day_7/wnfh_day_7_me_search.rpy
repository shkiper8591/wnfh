label d7_me_search:

    window hide dissolve
    stop ambience fadeout 3.5
    scene bg ext_lenin_square_day_wnfh with slide_right_blure_dissolve2
    play ambience ambience_camp_center_day fadein 3.5
    $ renpy.pause(0.5)
    window show dissolve

    "Выйдя на площадь, я стал раздумывать, где можно будет найти этих двух рыжих террористок."

    th "Возможно они у себя дома, хотя в такую жаркую погоду делать дома нечего."
    th "В таком случае, они могут быть либо на спортплощадке, ибо обе любительницы спорта."
    th "Либо же на пляже, где могут лежать и загорать или вообще купаться."
    th "Вообще они могут быть где угодно, но это три самых вероятных места их нахождения и их стоит проверить в первую очередь."

    ## Можно стилизовать под карту, но пока будет так

    window hide dissolve
    call screen wnfh_choice(
        ["dv", "Их домик", "Самое очевидное", "d7_me_search_dv_house"],
        ["dv", "Спортплощадка", "Чуть менее очевидно", "d7_me_search_dv_sport"],
        ["dv", "Пляж", "Совсем не очевидно", "d7_me_search_dv_beach"],
        ["d7_choice_n10", "Где искать рыжих"]
        ) with sphere_blure_dissolve2

label d7_me_search_2:

    window hide dissolve
    scene bg ext_lenin_square_day_wnfh with dissolve2
    $ renpy.pause(0.3)
    window show dissolve

    "Вернувшись на площадь, я стал раздумывать над оставшимися вариантами."

    if wnfh_Data.getChoice_result_number("d7_choice_n10") == 2:

        call screen wnfh_choice(
        ["dv", "Их домик", "Самое очевидное", "d7_me_search_dv_house"],
        ["dv", "Пляж", "Совсем не очевидно", "d7_me_search_dv_beach"],
        ["d7_choice_n12", "Где искать рыжих_2"]
        ) with sphere_blure_dissolve2        

    else:

        call screen wnfh_choice(
        ["dv", "Их домик", "Самое очевидное", "d7_me_search_dv_house"],
        ["dv", "Спортплощадка", "Чуть менее очевидно", "d7_me_search_dv_sport"],
        ["d7_choice_n13", "Где искать рыжих_3"]
        ) with sphere_blure_dissolve2

label d7_me_search_3:

    $ wnfh_Data.FlagSet("d7_search_3", True)

    "Изучив все варианты, мне остался только один, а именно их домик."
    "Куда я сразу же и направился."

    jump d7_me_search_dv_house

label d7_me_search_dv_beach:
    
    $ wnfh_Data.FlagSet("d7_beach_check", True)
    
    th "Вряд ли я их там найду, хотя в такую жаркую погоду искупаться самое то."
    th "А посему, думаю я могу их там найти[wp] Ну или хотя бы следы их пребывания."

    window hide dissolve
    stop ambience fadeout 3.5
    scene bg ext_beach_day with dissolve2
    play ambience ambience_lake_shore_day fadein 3.5
    window show dissolve
    # возможно стоит придумать что-то интересное на пляже, но мне как-то лень.

    "Придя на пляж, я ни сколько не удивился, не найдя здесь никого."
    "На пляже царила абсолютная тишина."

    me "Ну, что и следовало доказать, зря пришёл только."

    "Я постоял, посмотрел по сторонам, почесал репу и пошёл обратно."

    if wnfh_Data.FlagDataGet("d7_sport_check") == True:

        jump d7_me_search_3

    else:

        jump d7_me_search_2

label d7_me_search_dv_sport:
    
    $ wnfh_Data.FlagSet("d7_sport_check", True)

    th "Думаю там есть шансы их встретить, раз они так любят заниматься спортом."

    scene bg ext_playground_day with dissolve2
    stop music fadeout 3.5

    "Немного пройдясь, я пришёл к спортплощадке."
    "И, что не удивительно, народу здесь почти не было."
    "Почти. Кто-то тут всё же был."

    show sl normal sport at left
    show mi normal pioneer at right
    with dissolve
    play music music_list["timid_girl"] fadein 3.5

    "А именно Славя и Мику."
    "Славяна занималась разными спортивными упражнениями, приседания, бег на месте там и всякое такое."
    "Когда как Мику просто сидела на лавочке рядом и болтала со Славей."

    th "Интересно, какая дорога приключений привела сюда Мику?"

    me "Приветствую."

    "Сказал я, подойдя к девушкам поближе."
    "Славя прекратила упражняться, а Мику повернулась ко мне."

    show mi smile pioneer at right with dspr

    mi "Приветик, Семён. Ты тоже решил позаниматься спортом или просто понаблюдать за Славей? Знаешь, это так увлекательно! Она так много знает разных упражнений и так легко их выполняет!"
    me "Вообще нет, я сюда не за этим."
    sl "А зачем же ты тогда пришёл?"
    me "Ищу двух рыжих."

    show mi serious pioneer at right with dspr

    "Славя и Мику переглянулись."

    show sl smile2 sport at left with dspr

    sl "А по конкретнее можно?"
    me "Да ладно вам, будто вы тут много рыжих в лагере знаете."

    show mi grin pioneer at right with dspr

    mi "Ну мало ли, вдруг мы тебе дадим неправильную наводку, а потом все камни в нас полетят."
    me "Ладно, хорошо, я ищу Алису и Ульяну."
    sl "Это довольно распространённые имена, и я точно знаю несколько разных Алис и Ульян."

    show mi laugh pioneer at right with dspr

    "Мику не выдержала и рассмеялась во весь голос."

    show sl laugh sport at left with dspr

    "А немного погодя к ней присоединилась и Славя, только она не так громко смеялась."
    "Я же глядя на всё это, глубоко вздохнул."

    show mi normal pioneer at right
    show sl normal sport at left
    with dspr

    "Немного времени спустя и вдоволь насмеявшись они наконец успокоились."

    me "Всё?"
    mi "Ох, думаю да[wp]"
    sl "Давненько мы так не подшучивали, хе-хе."

    th "Шутники, блин."

    me "Ладно, раз вы закончили шутить надо мной, может скажете тогда, видели вы здесь Алису и Ульяну?"
    sl "Нет, не видела."
    mi "Тоже что-то не припомню их здесь."
    me "Спасибочки."

    stop music fadeout 3.56

    "Резко развернувшись на месте на 180, я зашагал обратно к площади."

    if wnfh_Data.FlagDataGet("d7_sport_check") == True:

        jump d7_me_search_3

    else:

        jump d7_me_search_2

label d7_me_search_dv_house:

    if wnfh_Data.getChoice_result_number("d7_choice_n10") == 1:

        th "Что ж, начну с самого очевидного варианта."

    scene bg ext_house_of_dv_day with dissolve2
    stop music fadeout 3.5

    "Спустя некоторое время, я стоял перед входом в их дом."
    "Занавеска на дверном окошке не была закрыта, и я аккуратно заглянул внутрь помещения."
    
    ##Тут должно быть ЦГ с переодевающимися Ульяной и Алисой
    
    play music music_list["eternal_longing"] fadein 3.5

    "И увидел то, чего не должен был видеть: Алиса и Ульяна стояли только в нижнем белье и переодевались."
    "К сожалению или счастью они стояли ко мне спиной, и поэтому не заметили меня."
    
    th "Вот чёрт, и что же теперь делать[wp]"
    
    window hide dissolve
    call screen wnfh_choice(
        ["dv", "Продолжить наблюдать", "Это точно ничем хорошим не кончится", "d7_me_peeking", {"dv":-1, "usw":-1}],
        ["dv", "Дать о себе знать", "Лучше мне не рисковать", "d7_me_knock", {"dv":1, "usw":1}],
        ["d7_choice_n11", "Подсмотреть за рыжими или нет"]
        ) with sphere_blure_dissolve2
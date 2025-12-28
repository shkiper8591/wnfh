label d7_me_search:

    window hide dissolve
    stop ambience fadeout 3.5
    scene bg ext_lenin_square_day_wnfh with slide_right_blure_dissolve2
    play ambience ambience_camp_center_day fadein 3.5
    $ renpy.pause(0.5)
    window show dissolve

    "Выйдя на площадь, я стал раздумывать: где стоит искать рыжих террористок?"

    th "Возможно, они у себя дома. Хотя вряд ли в такую погоду они дома сидят."
    th "В таком случае они могут быть либо на спортплощадке, ибо обе — любительницы спорта[wp]"
    th "Либо на пляже, где могут купаться и загорать."
    th "Вообще они могут быть где угодно, но в этих трёх местах шанс их нахождения больше всего, и их стоит проверить в первую очередь."

    ## Можно стилизовать под карту, но пока будет так

    window hide dissolve
    call screen wnfh_choice(
        ["neutral", "Их домик", "Самое очевидное", "d7_me_search_dv_house"],
        ["neutral", "Спортплощадка", "Чуть менее очевидное", "d7_me_search_dv_sport"],
        ["neutral", "Пляж", "Наименее очевидное", "d7_me_search_dv_beach"],
        ["d7_choice_n10", "Где искать рыжих"]
        ) with sphere_blure_dissolve2

label d7_me_search_2:

    window hide dissolve
    scene bg ext_lenin_square_day_wnfh with dissolve2
    $ renpy.pause(0.3)
    window show dissolve

    "Дорога снова привела меня в центр."

    th "Ну и хорошо, отсюда удобнее продолжить поиск. Вопрос в том, где их искать?"

    if wnfh_Data.getChoice_result_number("d7_choice_n10") == 2:

        call screen wnfh_choice(
        ["neutral", "Их домик", "Самое очевидное", "d7_me_search_dv_house"],
        ["neutral", "Пляж", "Наименее очевидное", "d7_me_search_dv_beach"],
        ["d7_choice_n12", "Где искать рыжих_2"]
        ) with sphere_blure_dissolve2        

    else:

        call screen wnfh_choice(
        ["neutral", "Их домик", "Самое очевидное", "d7_me_search_dv_house"],
        ["neutral", "Спортплощадка", "Чуть менее очевидное", "d7_me_search_dv_sport"],
        ["d7_choice_n13", "Где искать рыжих_3"]
        ) with sphere_blure_dissolve2

label d7_me_search_3:

    scene bg ext_lenin_square_day_wnfh with dissolve2

    "Так, остальные варианты я осмотрел. Остался один — их домик."
    "Куда я и направился."

    jump d7_me_search_dv_house

label d7_me_search_dv_beach:
    
    th "Вряд ли я их там найду[wp] Хотя в такую жаркую погоду искупаться — самое то."
    th "А посему, думаю, я могу их там найти[wp] Ну или хотя бы следы их пребывания."

    window hide dissolve
    stop ambience fadeout 3.5
    scene bg ext_beach_day with dissolve2
    play ambience ambience_lake_shore_day fadein 3.5
    window show dissolve

    "Придя на пляж, я нисколько не удивился, увидев отдыхающих на берегу."
    "Кто-то плескался, кто-то просто загорал. Говоря вкратце, пионеры наслаждались жарким летним днём."
    "Однако искомые рыжие макушки я так и не увидел."

    me "Ну, чего и следовало ожидать. Зря пришёл только."

    "Я постоял, посмотрел по сторонам, почесал репу и пошёл обратно."

    if wnfh_Data.getChoice_result_number("d7_choice_n10") == 2:

        jump d7_me_search_3

    else:

        jump d7_me_search_2

label d7_me_search_dv_sport:

    th "Думаю, есть шанс встретить их на площадке, раз они так любят заниматься спортом."

    scene bg ext_playground_day with dissolve2
    stop music fadeout 3.5

    "Спустя немного времени я пришёл к месту назначения."
    "И, что не удивительно, народу здесь почти не было."
    "Почти. Кто-то тут всё же был."

    show sl normal sport at left
    show mi normal pioneer at right
    with dissolve
    play music music_list["timid_girl"] fadein 3.5

    "А именно Славя и Мику."
    "Славяна выполняла разного рода упражнения: приседания, бег на месте и всякое такое."
    "В то время как Мику просто сидела на лавочке рядом и болтала со Славей."

    th "Интересно, какая дорога приключений привела сюда Мику?"

    "Я решил подойти к девушкам поближе."

    me "Приветствую."

    "Славя прекратила упражняться, а Мику повернулась ко мне."

    show mi smile pioneer at right with dspr

    mi "Приветик, Семён! Ты тоже решил позаниматься спортом? Или просто понаблюдать? Знаешь, это так увлекательно! Славя так много разных упражнений знает и так легко их выполняет!"
    me "Вообще нет, я здесь не за этим."
    sl "А зачем же ты тогда пришёл?"
    me "Ищу двух рыжих."

    show mi serious pioneer at right with dspr

    "Славя и Мику переглянулись."

    show sl smile2 sport at left with dspr

    sl "А поконкретнее можно?"
    me "Да ладно вам, будто вы тут много рыжих знаете."

    show mi grin pioneer at right with dspr

    mi "Ну мало ли, вдруг мы тебе дадим неправильную наводку, а потом все камни в нас полетят."
    me "Ладно, хорошо, я ищу Алису и Ульяну."
    sl "Это довольно распространённые имена. Я точно знаю несколько разных Алис и Ульян."

    show mi laugh pioneer at right with dspr

    "Мику не выдержала и рассмеялась во весь голос."

    show sl laugh sport at left with dspr

    "А немного погодя к ней присоединилась и Славя, разве что смеялась она не так громко."
    "Я же, глядя на всё это, глубоко вздохнул."

    show mi normal pioneer at right
    show sl normal sport at left
    with dspr

    "Вдоволь насмеявшись, они наконец успокоились."

    me "Всё?"
    mi "Ох, думаю да[wp]"
    sl "Хе-хе, давненько так подшутить не удавалось."

    th "Шутники, блин."

    me "Ладно, раз вы закончили смеяться надо мной[wp] Может, скажете тогда, видели вы здесь Алису и Ульяну?"
    sl "Я не видела."
    mi "Тоже что-то не припомню их здесь."
    me "Спасибочки."

    stop music fadeout 3.56

    "Резко развернувшись на месте на сто восемьдесят, я зашагал обратно."

    if wnfh_Data.getChoice_result_number("d7_choice_n10") == 3:

        jump d7_me_search_3

    else:

        jump d7_me_search_2

label d7_me_search_dv_house:

    if wnfh_Data.getChoice_result_number("d7_choice_n10") == 1:

        th "Что ж, начну с самого очевидного варианта."

    scene bg ext_house_of_dv_day with dissolve2
    stop music fadeout 3.5

    "Спустя некоторое время я стоял перед входом в их дом."
    "Занавеска на дверном окошке не была задёрнута, и я аккуратно заглянул внутрь помещения."
    
    ##Тут должно быть ЦГ с переодевающимися Ульяной и Алисой
    
    play music music_list["eternal_longing"] fadein 3.5

    "И увидел то, чего не должен был видеть: Алиса и Ульяна стояли в одном нижнем белье и переодевались."
    "К сожалению или счастью, они стояли ко мне спиной, поэтому не заметили меня."
    
    th "Вот чёрт[wp]"
    
    window hide dissolve
    call screen wnfh_choice(
        ["neutral", "Продолжить наблюдать", "Ничем хорошим это не кончится", "d7_me_peeking", {"dv":-1, "usw":-1}],
        ["dv", "Дать о себе знать", "Лучше не рисковать", "d7_me_knock", {"dv":1, "usw":1}],
        ["d7_choice_n11", "Подсмотреть за рыжими или нет"]
        ) with sphere_blure_dissolve2
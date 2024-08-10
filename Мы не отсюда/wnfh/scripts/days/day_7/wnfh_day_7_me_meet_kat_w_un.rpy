label d7_me_meet_kat_w_un:

    window hide dissolve
    $ wnfh_set_time()
    stop ambience fadeout 2.0
    scene bg ext_dining_hall_near_day
    show un smile pioneer 
    with dissolve2
    play ambience ambience_camp_center_day fadein 2.0
    play music music_list["timid_girl"] fadein 3.5
    $ wnfh_Data.FlagSet("d7_kat_oblivanie", "ne_oblil")
    $ renpy.pause(1)
    show bg ext_dining_hall_away_day with dissolve2 
    $ renpy.pause(1)
    show bg ext_lenin_square_day_wnfh with dissolve2
    window show dissolve    

    "Я направился в сторону площади, и в этот момент до меня дошла одна мысль."

    th "Подождите-ка, Ольга Дмитриевна сказала встретить пополнение, но не сказала, сколько именно людей меня там ждут!"
    th "А если там здоровенная толпа? Хотя вряд ли, конечно, всё же свободных домиков осталось не так уж и много. Но тем не менее!"
    th "И если там много народу, то даже вдвоём мы можем со всеми не справиться."
    th "Значит, нужно обдумать план действий."

    "Я медленно остановился."

    show un shy pioneer with dspr

    un "Семён, что-то случилось?"
    me "А? Да[wp] Нет[wp]"

    show un smile2 pioneer with dspr

    un "Так да или нет?"
    me "Нет, просто задумался[wp]"
    me "Что если там толпа? Как нам с ними управляться?"

    show un laugh pioneer with dspr

    "Лена рассмеялась."

    un "Так нам и не нужно с ними управляться, просто сопроводить к Ольге Дмитриевне!"
    me "Да, но их же придётся как-то организовать, чтобы сопроводить, верно?"

    show un smile3 pioneer with dspr

    un "Сомневаюсь, что нас ждёт особо большое пополнение."
    un "Три или четыре человека максимум."
    un "Мест свободных мало осталось."

    "Рассуждения Лены успокоили меня."

    me "Ну хорошо."
    un "Вот и всё. Идём скорее. Нас, небось, уже ждут."
    me "Да, ты права."

    "В ускоренном темпе мы отправились на остановку."

    window hide dissolve
    stop ambience fadeout 2.0
    stop music fadeout 3.5
    scene bg ext_bus
    show un smile pioneer at right
    show kat normal casual shirt far at left
    with santa_barbara_out_blure_dissolve2
    play ambience ambience_camp_entrance_day fadein 2.0
    window show dissolve
    $ wnfh_set_name("kat", "Новенькая")

    "Скоро мы пришли к пункту назначения."

    show un surprise pioneer at right with dspr

    "И были малость удивлены, обнаружив здесь только одного человека. {w}Девушку, если быть точнее."
    "Одета она была, мягко говоря, не по советским формальностям."
    "Джинсы, модная футболка с принтом. Только рубашка особо не выделялась."

    th "Может, дочка какого-нибудь члена партии? Вот и достал всё лучшее из-за границы."

    "Но Лену, похоже, совсем не смущал внешний вид новенькой."

    un "Только одна? Странно."
    me "А не странно ли она одета?"
    un "О чём ты?"
    me "Ну[wp]"

    show kat surprise casual shirt far at left with dspr 

    kat "Ой! П-Привет."

    "Не успел я договорить, как новенькая окликнула нас, помахав рукой."

    show un smile pioneer at right with dspr

    un "Здраствуй. Я так понимаю, ты и есть наше пополнение."
    kat "П-Получается так."

    "Стеснясь и немного запинаясь ответила она."

    th "Ещё одна стесняша в лагере, чудно."

    show kat normal casual shirt at left with dspr

    "Новенькая подошла ближе к нам."

    me "А с тобой в автобусе больше никого не было?"

    show kat confused casual shirt at left with dspr

    kat "Н-Нет, я одна приехала."
    me "Интересно."
    un "Ну, неважно. Тебя как зовут?"

    $ wnfh_set_name("kat", "Катя")

    kat "Катя."
    #kat "Но друзья зовут меня БМ-13"
    show un laugh pioneer at right with dspr

    un "Чудесное имя, а я Лена. Но если мы станем подругами, сможешь звать меня Ленкой!"

    show kat smile casual shirt at left with dspr

    "Слова Лены оказывали на новенькую какое-то особое влияние."
    "Было видно, что она стала немного увереннее в себе, даже улыбалась."

    kat "Хорошо, а[wp] Ты?"
    me "Семён. Главный парень на побегушках в этом лагере."

    show kat thinking casual shirt at left with dspr

    kat "Поняла[wp]"

    if wnfh_Data.getChoice_result_number("d7_choice_n1") == 1:

        "Новенькая бегло посмотрела на мои ранения."

        kat "Что с тобой случилось?"
        me "Несчастный случай."
        kat "Кошмар."

    show un smile3 pioneer at right with dspr

    un "Ну, не будем задерживаться здесь."
    un "Лучше проводим тебя к нашей вожатой."

    show kat happy casual shirt at left with dspr
    show un smile pioneer at right with dspr

    kat "Да, давайте." 

    stop ambience fadeout 2.0
    show bg ext_clubs_day with dissolve2
    play ambience ambience_camp_center_day fadein 2.0

    "Проходя мимо клубов, я вспомнил, что надо бы зайти и предупредить Шурика, что я немного задержусь."

    me "Так, извините, но мне надо на минутку забежать в клуб."

    show un normal pioneer at right with dspr

    un "А это подождать не может?"
    me "Нет."

    "Сказал я и без промедления направился в клуб."

    window hide
    stop ambience fadeout 2.0
    scene bg int_clubs_male_day
    show sh normal pioneer at cright
    show el sad pioneer at fright
    show sv angry pioneer glasses tablet at left
    with door_blure_dissolve2
    play ambience ambience_int_cabin_evening fadein 2.0

    "И как только я зашёл, так сразу мне захотелось выйти."
    "Ведь внутри была Света, которая как обычно песочила мозги моим товарищам."
    "Благо, она стояла ко мне спиной."
    "Видимо, она была ну очень увлечена процессом и не услышала, как я вошёл."

    sv "[wp]Сколько можно заниматься вот этими[wp]"

    "Говорила она, указывая взглядом на модели самолётов."

    sv "Вот этим вот?"
    sv "Нет бы чем-то полезным для лагерной жизни заняться!"

    "Шурик тяжело вздохнул. По его взгляду было видно, что он очень устал от этого диалога."

    sh "Свет[wp]"
    sv "Светлана Александровна."
    sh "Да, Светлана Александровна, если это единственная причина, по которой Вы нас попросили побыстрее закончить с завтраком, то мне нечего Вам сказать на этот счёт."
    sh "Лишь то, что мы вообще-то всегда готовы и участвуем в лагерной жизни!"
    sh "Но поскольку Ваше Высочество постоянно занято непонятно чем, Вы не замечаете нашей деятельности, без которой, поверьте уж, в лагере было бы тяжко."

    th "Охренеть, Сань, вот это ты вырыл себе могилу. Просто титанических масштабов."

    "Однако вместо ожидаемых криков и угроз отправки всего нашего дружного состава на лагерные исправительные работы Планшетик лишь грозно хмыкнула."

    #sv "Я тебя услышала, либерал"
    sv "Тоже мне, пионеры."

    show sv scared pioneer glasses tablet at left with dspr

    "Она резко развернулась и врезалась в меня, после чего упала."

    sv "Ау[wp]"

    show sv angry pioneer glasses tablet at left with dspr

    "Я попытался помочь ей встать, но она лишь отмахнулась от моей руки."

    sv "Ещё один явился."
    me "Да вот, хотел сказать Шурику, что буду в клубах чуть позже."
    sv "И по какому поводу?"
    sv "А хотя без разницы, мне до вашего клуба дела нет."
    me "Как скажешь."
    
    hide sv with dissolve
    show el normal pioneer at fright with dspr

    "Света вышла из здания клубов, громко хлопнув дверью."

    me "Ну, думаю, ты слышал. Я сегодня попозже приду."
    sh "Да без проблем. Только не сильно позже, ладно? Ты нам нужен сегодня."
    me "Так точно."

    stop ambience fadeout 2.0
    scene bg ext_clubs_day
    show un serious pioneer at cright
    show kat sad casual shirt at fright
    show sv angry pioneer glasses tablet at left
    with dissolve2
    play ambience ambience_camp_center_day fadein 2.0

    "Выйдя на улицу, я стал свидетелем ещё одного спора с участием Светы. На этот раз мурыжила она Лену."

    th "Да уж, Света, быстро ты находишь цель."

    un "Нет уж, мы сами справимся."
    sv "Да чего вы справитесь? Вы хоть знаете, где вожатая?"
    un "Как-нибудь разберёмся."

    th "Ладно, это всё, конечно, очень интересно, но время поджимает."

    me "Так, Светка, всё, дай другим тоже поучаствовать в лагерной жизни."
    sv "Как ты меня назвал?"
    me "Всё, пока-пока!"

    show un shy pioneer at cright with dspr

    "Я рефлекторно схватил Лену за запястье, а она взяла Катю, и такой цепочкой мы быстренько пошли прочь."

    scene bg ext_lenin_square_day_wnfh
    show un shy pioneer at right
    show kat normal casual shirt at left
    with dissolve2

    "Мы вышли на площадь, и я отпустил Лену."
    "Света же нас и не преследовала, оставшись далеко позади."

    me "Фух, пронесло."
    un "Д-Да, молодец, быстро сработал."
    me "Ага, спасибо."

    show un normal pioneer at right with dspr

    me "Но Света была права, где нам вожатую-то найти?"
    un "Может, она у себя в домике?"
    me "Или в адмнистрации[wp]"

    show kat serious casual shirt at left with dspr

    un "Или в столовой[wp]"
    me "Ну там вряд ли, скорее уж в спортзале."

    show kat rage casual shirt at left with dspr
    show un scared pioneer at right with dspr

    kat "Да определитесь вы уже!"

    "Неожиданно и грозно рявкнула Катя, от чего мы с Леной аж вздрогнули."

    show kat angry casual shirt at left with dspr

    kat "Слушать вас невозможно! Тоже мне, сопровождающие."

    show un shy pioneer at right with dspr

    un "И-Извини."
    me "Ладно, давай у домика проверим."
    un "Согласна."

    show kat obida casual shirt at left with dspr

    kat "Наконец-то."

    jump d7_me_kat_sdacha_kati_w_un
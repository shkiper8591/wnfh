label d7_me_meet_kat_w_un:

    window hide dissolve
    $ wnfh_set_time()
    stop ambience fadeout 2.0
    scene bg ext_dining_hall_near_day
    show un smile pioneer 
    with dissolve2
    play ambience ambience_camp_center_day fadein 2.0
    play music music_list["timid_girl"] fadein 3.5
    $ wnfh_Data.FlagSet("d7_kat_oblil_me", "ne_oblil")
    $ renpy.pause(1)
    show bg ext_dining_hall_away_day with dissolve2 
    $ renpy.pause(1)
    show bg ext_lenin_square_day_wnfh with dissolve2
    window show dissolve    

    "Выйдя из столовой и пройдя до площади, до меня дошла одна мысль."

    th "Подождите-ка, Ольга Дмитриевна сказала встретить пополнение, но не сказала сколько этого самого пополнения!"
    th "А если там толпа? Хотя, вряд ли конечно, всё же свободных домиков осталось не так уж и много. Но тем не менее!"
    th "И если там много пионеров, то мы, даже вдвоём, крайне маловероятно справимся."
    th "Значит нужно обдумать план действий."

    "Я медленно остановился."

    show un shy pioneer with dspr

    un "Семён, что-то случилось?"
    me "А? Да, нет."

    show un smile2 pioneer with dspr

    un "Так да или нет?"
    me "Нет, просто задумался."
    me "Что если там большая толпа пионеров, как нам с ними управляться?"

    show un laugh pioneer with dspr

    "Лена рассмеялась."

    un "Так нам и не нужно с ними управляться, просто сопроводить к Ольге Дмитриевной?"
    me "Да, но их же придётся как-то организовать, чтобы сопроводить, верно?"

    show un smile3 pioneer with dspr

    un "Сомневаюсь, что там особо большое пополнение."
    un "Может три или четыре пионера максимум."
    un "Мест свободных мало осталось же."

    "Рассуждение Лены успокоило меня по этому поводу."

    me "Ну хорошо."
    un "Вот и всё, идём скорее, нас небось уже ждут."
    me "Да, ты права."

    "В ускоренном темпе, мы отправились на остановку."

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

    "Скоро мы пришли в пункт назначения."

    show un surprise pioneer at right with dspr

    "И были малость удивлены, обнаружить здесь только одного пионера. {w}Вернее пионерку."
    "Которая ещё была одета мягко говоря не по советским формальностям."
    "Джинсы, модная футболка с принтом. Только рубашка особо не выделялась."

    th "Может дочка какого-нибудь члена партии? Вот и достал всё лучшее из-за границы."

    "Но Лену, похоже, совсем не смущал внешний вид новенькой."

    un "Только одна? Странно."
    me "А не странно ли она одета?"
    un "О чём ты?"
    me "Ну[wp]"

    show kat surprise casual shirt far at left with dspr 

    kat "Ой! П-Привет."

    "Не успел я договорить, как новенькая окликнула нас, помахав рукой."

    show un smile pioneer at right with dspr

    un "Здраствуй, я так понимаю ты у нас то самое пополнение."
    kat "П-Получается, что так."

    "Стеснясь и немного запинаясь говорила она."

    th "Ещё одна стесняша в лагере, чудно."

    show kat normal casual shirt at left with dspr

    "Новенькая подошла ближе к нам."

    me "А с тобой в автобусе больше никого не было?"

    show kat confused casual shirt at left with dspr

    kat "Н-Нет, я одна приехала."
    me "Интересно."
    un "Ну да неважно. Тебя как зовут?"

    $ wnfh_set_name("kat", "Катя")

    kat "Катя."
    #kat "Но друзья зовут меня БМ-13"
    show un laugh pioneer at right with dspr

    un "Чудесное имя, а я Лена. Но если мы станем подругами, сможешь звать меня Ленкой."

    show kat smile casual shirt at left with dspr

    "Слова Лены испытывали на новенькую какое-то особое влияние."
    "Было видно, что она стала более уверенная в себе и даже улыбалась."

    kat "Хорошо, а[wp] ты?"
    me "Семён. Главный парень на побегушках в этом лагере."

    show kat thinking casual shirt at left with dspr

    kat "Поняла[wp]"

    if wnfh_Data.getChoice_result_number("d7_choice_n1") == 1:

        "Новенькая бегло посмотрела на мои ранения."

        kat "Что с тобой случилось?"
        me "Несчастный случай."
        kat "Кошмар."

    show un smile3 pioneer at right with dspr

    un "Ну не будем задерживаться здесь."
    un "Лучше сопроводим тебя к нашей вожатой."

    show kat happy casual shirt at left with dspr
    show un smile pioneer at right with dspr

    kat "Да, давайте." 

    stop ambience fadeout 2.0
    show bg ext_clubs_day with dissolve2
    play ambience ambience_camp_center_day fadein 2.0

    "Вернувшись на территорию лагеря и проходя мимо клубов, я вспомнил, что надо бы зайти и предупредить Шурика, что я немного задержусь."

    me "Так извините, но мне надо на минутку забежать в клуб."

    show un normal pioneer at right with dspr

    un "А это подождать не может?"
    me "Нет."

    "Сказал я и мигом отправился в клуб."

    window hide
    stop ambience fadeout 2.0
    scene bg int_clubs_male_day
    show sh normal pioneer at cright
    show el sad pioneer at fright
    show sv angry pioneer glasses tablet at left
    with door_blure_dissolve2
    play ambience ambience_int_cabin_evening fadein 2.0

    "И как только я зашел, так сразу мне захотелось выйти."
    "Ведь внутри была Света, которая как обычно песочила мозги моим товарищам."
    "Благо, она стояла ко мне спиной."
    "А ещё, она видимо была очень увлечена процессом и не услышала как я вошёл."

    sv "[wp]Сколько можно заниматься вот этими[wp]"

    "Говорила она указывая взглядом на авиамодели."

    sv "Вот этим вот."
    sv "Нет бы чем-то полезным заняться для лагерной жизни."

    "Шурик тяжело вздохнул. В его взгляде читалась сильная усталость от этого диалога."

    sh "Свет[wp]"
    sv "Светлана Александровна."
    sh "Да, Светлана Александровна, если это единственная причина по которой Вы нас попросили побыстрее закончить с завтраком."
    sh "То мне нечего Вам сказать на этот счёт, разве то, что мы вообще-то всегда готовы и участвуем в лагерной жизне!"
    sh "Но поскольку, Ваше высочество постоянно занято непонятно чем, Вы не замечаете нашей дейятельности, без которой, поверьте уж, здесь, в лагере, было бы тяжко."

    th "Ахренеть, вот это он вырыл себе могилу просто титанических масштабов."

    "Однако, вместо ожидаемых криков и угроз, что весь наш состав будет отправлен на некие лагерные исправительные работы, Планшетик лишь грозно хмыкнула."

    #sv "Я тебя услышала, либерал"
    sv "Тоже мне, пионеры."

    show sv scared pioneer glasses tablet at left with dspr

    "Она резко развернулась и врезалась в меня и упала."

    sv "Ау[wp]"

    show sv angry pioneer glasses tablet at left with dspr

    "Я попытался ей помочь встать, но она лишь отодвинула мои руки."

    sv "Ещё один явился."
    me "Да вот, хотел сказать Шурику что буду в клубах чуть позже."
    sv "И по какому этому поводу?"
    sv "А хотя без разницы, всё равно мне на ваш клуб."
    me "Как скажешь."
    
    hide sv with dissolve
    show el normal pioneer at fright with dspr

    "Света покинула клубы, громко хлопнув дверью."

    me "Ну, думаю ты слышал Шурик, я сегодня позже приду."
    sh "Да без проблем. Только особо ненадолго, ладно? Ты нам нужен сегодня."
    me "Так точно."

    stop ambience fadeout 2.0
    scene bg ext_clubs_day
    show un serious pioneer at cright
    show kat sad casual shirt at fright
    show sv angry pioneer glasses tablet at left
    with dissolve2
    play ambience ambience_camp_center_day fadein 2.0

    "Выйдя на улицу я стал свидетелем другого спора Светы, но уже с Леной."

    th "Да уж Света, быстрый поиск целей у тебя."

    un "Нет уж, мы сами справимся."
    sv "Да чего вы справитесь, вы хоть знаете где вожатая?"
    un "С этим как-то да разберёмся."

    th "Ладно, это конечно всё весело, но время поджимает."

    me "Так, Светка, всё дай другим тоже поучаствовать в лагерной жизни."
    sv "Как ты меня назвал?"
    me "Всё, пока-пока."

    show un shy pioneer at cright with dspr

    "Я рефлекторно схватил Лену за запястье, а она взяла Катю, и такой цепочкой мы быстренько ушли прочь."

    scene bg ext_lenin_square_day_wnfh
    show un shy pioneer at right
    show kat normal casual shirt at left
    with dissolve2

    "Выйдя на площадь я отпустил Лену."
    "Света же нас особо и не преследовала, оставшись далеко позади."

    me "Фух, пронесло."
    un "Д-Да, молодец, быстро сработал."
    me "Ага, спасибо."

    show un normal pioneer at right with dspr

    me "Но Света была права, где нам вожатую-то найти?"
    un "Может она у себя в домике?"
    me "Или может в адмнистрации[wp]"

    show kat serious casual shirt at left with dspr

    un "Или в столовой."
    me "Ну там вряд ли, скорее уж в спортзале."

    show kat rage casual shirt at left with dspr
    show un scared pioneer at right with dspr

    kat "Да определитесь вы уже!"

    "Неожиданно и грозно рявкнула Катя, что мы аж с Леной перепугались."

    show kat angry casual shirt at left with dspr

    kat "Слушать вас невозможно, тоже мне сопроводители."

    show un shy pioneer at right with dspr

    un "И-Извини."
    me "Ладно, давай у домика проверим."
    un "Согласна."

    show kat obida casual shirt at left with dspr

    kat "Наконец-то[wp]"

    jump d7_me_kat_sdacha_kati_w_un
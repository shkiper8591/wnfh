label d8_zavtrak:

    window hide
    stop ambience fadeout 0.5
    scene bg ext_dining_hall_near_sunset with slide_right_blure_dissolve2
    $ renpy.pause(1.0)    
    scene bg int_dining_hall_people_sunset_wnfh 
    show kat normal pioneer:
        xalign 0.5
    with dnr_entrance  
    play ambience ambience_dining_hall_full fadein 3
    
    window show
    
    ## Завтрак
    "Войдя в столовую, я стал думать, куда бы сесть."

    if wnfh_Data.getChoice_points_sum("un") <= 2:

        show un smile pioneer:
            xcenter 1.2
            ease_quart 2.0 xcenter 0.72

        "И пока думал, к нам подошла Лена."
        
        un "Семен, я заберу Катю к себе, надеюсь ты не против, а то мне нужно кое что с ней обсудить."
        
        show un smile pioneer behind kat:
            ease_quart 1.5 xcenter 0.64
        
        "Не успев ничего ответить, Лена уже потащила Катю, к себе."
    
        window hide
        $ renpy.pause(1.0)
        
        show un smile pioneer:
            ease_quart 2.0 xcenter 1.2
        show kat normal pioneer:
            ease_quart 2.0 xcenter 1.2
    
        $ renpy.pause(1.5)
        window show
        
        "Пожав плечами, я ещё раз окинул столовую взглядом." 
        "И обнаружил свободное место рядом со своими товарищами из клубов."
        "Но было и ещё одно рядом с главной музыканткой всея лагеря — Мику."

        th "Диллема[wp] {w}С одной стороны братва, а с другой, можно наконец нормально поговорить с Мику."
        th "А то за всё время у меня это так и не получалось[wp] По ряду причин."

        window hide dissolve
        $ renpy.pause(0.2)
        call screen wnfh_choice(
            ["mi", "Сесть с Мику", "я хуй знает что тут написать", "d8_zavtrak_s_miku", {"mi":1}],
            ["neutral", "Сесть с товарищами", "Пожалуй сяду с товарищами", "d8_zavtrak_s_el_sh"],
            ["d8_choice_n1", "С кем сесть в столовой. Завтрак. Д2"]
            ) with sphere_blure_dissolve2

    elif wnfh_Data.getChoice_points_sum("un") == 3:
        
        jump d8_zavtrak_w_un

label d8_zavtrak_w_un:

    $ wnfh_Data.FlagSet("dinner_w_un") 
    
    show un smile pioneer:
        xcenter 1.2
        ease_quart 2.0 xcenter 0.72
    show kat normal pioneer:
        ease_quart 1.5 xcenter 0.28 

    "И пока думал, к нам подошла Лена."
    
    un "Приветик."
    
    "Весёлым голоском поздоровалась с нами Лена."

    show kat smile pioneer with dspr

    kat "Здравствуй."
    me "Привет."
    un "Я тут гляжу, вы выбираете местечко где бы сесть."
    kat "Верно."
    me "Можешь с нами сесть, если хочешь."

    show un smile2 pioneer at right with dspr

    "На моё предложение Лена слегка усмехнулась."
    un "Хах, я как раз хотела об этом спросить."
    me "Ну вот такой я экстрасенс."
    me "Ладно, дамочки, хватит терять время и пойдём сядем уже куда-нибудь."

    show kat upset pioneer with dspr

    kat "Согласна, кушать-то хочется."
    me "Тогда идём, сейчас втиснемся куда-нибудь[wp]"

    show kat normal pioneer 
    show un smile pioneer at right
    with dspr

    "Пробираясь сквозь толпу пионеров, мы вышли к столу, где, на удивление, сидело не так много людей."
    "Здесь мы и расположились, аккуратно поставив свои подносы."
    #короче копчённый (стас), я тебе сценарий написал и в благородство играть не буду. Расставишь для меня столы с едой и мы в расчёте. 
    "Бегло осмотрев "
    me "Ну что, Кать, как вчера прошёл первый день в лагере?"

    show kat thinking with dspr

    "Она глубоко вздохнула."
    kat "Эх, ну как-как."

    show kat upset pioneer with dspr

    kat "Обычно, наверное?"
    kat "Показали мне домик, где и просидела некоторое время, обживаясь."

    show un grin pioneer at right with dspr

    un "А потом пришла я, и вытащила её погулять и, заодно получше познакомиться."

    show un smile3 pioneer at right with dspr

    un "Хочу сказать, что это было довольно сложной задачей."
    me "Ха, и почему же?"

    show kat obida pioneer
    show un laugh pioneer
    with dspr

    "Лена рассмеялась, а Катя сделала обиженную мину."

    un "Потому-что Катя та ещё домоседка."
    kat "А то что, я даже толком свои вещи распределить по местам не успела, это не?"
    un "У тебя было много времени на это."
    kat "Двадцать минут?"

    show un grin pioneer at right with dspr

    un "Целых двадцать минут!"

    show un smile pioneer at right with dspr

    "Тихонько посмеявшись, Лена легко похлопала Катю по плечу."

    un "Ну чего ты обижаешься-то?"

    show kat confused pioneer with dspr

    kat "Я? Я не обижаюсь."

    show mt normal pioneer:
        xcenter 1.2
        ease_quart 2.0 xcenter 0.88
    show kat normal pioneer
    show un normal pioneer at right
    with dspr

    "Тут к нам подошла наша вожатая."

    mt "Вот где вы."
    mt "И меня очень интересует, почему же вы всё ещё тут, а не ходите по лагерю и собираете подписи."
    me "Так мы завтракаем."

    show mt angry with dspr

    mt "Ну так побыстрее давайте. Чем раньше вы сдадите мне этот лист, тем лучше будет для и меня и вас."
    mt "Намёк ясен, Семён?"

    "Я грустно и глубоко вздохнул."

    me "Ясен."

    show mt grin with dspr

    mt "Вот и славно."

    show mt grin pioneer:
        ease_quart 1.5 xcenter 1.2

    "Злорадоно похихикав на прощание, Ольга Дмитриевна быстро удалилась вглубь столовой."

    me "Ну что ж, Кать, ты слышала её. Так что давай, ускоряемся."

    "Не желая терять ни минуты, я моментально стал уплетать завтрак, расправившись с ним чуть менее чем за три минуты."
    "После чего я с облегчением вздохнул и посмотрел на Катину тарелку[wp] Которая была ещё на половину полна[wp]"
    th "М-да[wp]"

    show un smile pioneer at right with dspr

    un "Кстати, Семён[wp]"
    me "Что?"
    un "А можно с вами за компанию? А то дел у меня пока-что нет, а занять себя как-то хочется."

    window hide dissolve
    $ renpy.pause(0.2)
    call screen wnfh_choice(
        ["un", "Разумеется", "Чем больше компания, тем веселее", "d8_un_yes_1", {"un":1}],
        ["kat", "Не, мы быстро", "Тут делов на пять минут, особо не повеселишься", "d8_un_no_1", {"kat":1, "un":-1}],
        ["d8_choice_n3", "Лена хочет пойти вместе Катей и Семёном за компанию."]
        ) with sphere_blure_dissolve2

label d8_un_yes_1:

    window show dissolve

    me "Да, конечно, думаю никто против не будет."
    kat "Не будет."

    "Моментом сказала Катя."

    un "Отлично, спасибо вам."
    me "Та пожалуйста"

    "Как только Катя закончила с завтраком, мы отправились на выход из столовой."
    
    jump d8_begunok

label d8_un_no_1:

    window show dissolve

    me "Не стоит, мы быстро заполним этот лист, даже глазом моргнуть не успеешь."

    show un shy pioneer at right with dspr

    un "Вот как[wp] Ну ладно тогда, может потом повезёт прогуляться нам вместе[wp]"
    me "Несомненно."

    "Дождавшись, когда Катя закочила с завтраком, мы покинули столовую."

    jump d8_begunok

label d8_zavtrak_s_miku:
    
    th "Посижу-ка с Мику. С парнями я всегда успею поговорить, а вот с нашей музыканткой мне довольно редко доводиться пообщаться."

    th "А так, может чего интересного расскажет. А то одну и ту же бурду про самолёты, аэродинамику и подобную фигню уже тошно слушать."
    
    "Взяв поднос с едой, я направился к Мику, которая грустно ковырялась ложкой в еде."

    show mi upset pioneer at center with dissolve
    
    me "Не занято?"
    
    "Спросил я, подойдя к ней."
    "Мику подняла на меня сонный взгляд и сильно зевнув ответила."
    
    mi "А? Привет Семён, да конечно садись."
    
    "Поставив поднос на стол, я сел за него."

    show mi sad pioneer at center with dspr
    
    me "Я так понимаю, кто-то сегодня плохо спал."
    mi "Да, именно так."
    me "Можно узнать как так вышло?"

    show mi upset pioneer at center with dspr

    mi "Ну, ничего такого уж интересного[wp] Кошмары просто снились и всё."
    mi "Правда их содержание всё никак не отпустит меня[wp]"
    me "Ох, и, если не секрет, что тебе такого приснилось?"
    
    show mi shocked with dspr
    $ renpy.pause(0.2)
    show mi upset with dspr

    "Мику мимолётно бросила на меня испуганный взгляд."

    show mi sad pioneer at center with dspr
    
    mi "Мне снились[wp] {w}Ужасные вещи[wp]"
    mi "Как меня и всю мою семью окружили американские солдаты в родном Киото[wp] {w}Их расстреляли, а мне удалось убежать. Солдаты заливались дьявольским смехом и отправились искать меня."

    show mi sad_cry pioneer at center with dspr

    mi "И когда они меня нашли и наставили оружие, я вскрикнула и очнулась за мгновение до выстрела, вся в холодном поту."
    
    "По её щеке пробежало пару слёз."
    
    th "Да уж, не этого я ожидал[wp]"
    
    me "Слушай, не думай об этом. Это всего лишь кошмар, отпусти его, пусть мозг сотрёт его."

    show mi sad pioneer at center with dspr

    mi "Да, думаю это будет верным решением."

    show mi normal pioneer at center with dspr

    mi "Ну, а у тебя как дела?"
    
    "Резко переменилась в настроении Мику и весёлым голоском спросила меня."
    
    me "Да всё нормально в общем-то. Буду провожатым для новенькой, хотя ты это и так знаешь."
    
    show mi grin pioneer at center with dspr

    mi "О, о! Да знаю это раз, и два, можно с вами? За компанию и заодно покажу и расскажу ей о всех достопримечательностях нашего лагеря, и заранее отвечая на твой вопрос: да, их больше чем статуя Ленина."
    
    th "Ну тут даже не прикопаться, уделала меня так уделала. Вот только нужна ли нам компания?"
    
    window hide dissolve
    $ renpy.pause(0.2)
    call screen wnfh_choice(
        ["mi", "Почему бы и нет", "Пополнение в команде не повредит", "d8_mi_yes_1", {"mi":1}],
        ["mi", "Пожалуй нет", "Не вижу особого смысла в этом", "d8_mi_no_1", {"mi":-1}],
        ["d8_choice_n2", "Мику хочет пойти вместе Катей и Семёном за компанию."]
        ) with sphere_blure_dissolve2
    
label d8_mi_yes_1:
    
    show mi smile pioneer at center with dspr
    show mt normal pioneer:
        xcenter 1.2
    window show dissolve
    
    mi "Отличненько! Со мной вы точно не заскучаете."
    me "Чудесно, а хочешь сказать, что в моей компании Катя заскучает?"
    mi "Я имею ввиду, что втроём всяко будет веселее, чем вдвоём."
    me "Ну, тут даже не поспорить."

    show mt normal pioneer:
        ease_quart 2.0 xcenter 0.78

    "В это же время, к нашему столу подошла вожатая."
    
    mt "Вот ты где, давай быстрее заканчивай с завтраком и на выход, тебя уже ждут."
    me "Понял, принял."

    show mt normal pioneer:
        ease_quart 2.0 xcenter 1.2
    
    "После моего ответа, Ольга Дмитриевна тут же удалилась обратно вглубь столовой, а я же активно принялся за свой завтрак."
    
    mi "Фи-и-и, как ты можешь есть эту гадость?"
    me "А мне очень даже нравится."
    mi "Фи."
    
    "Закончив с завтраком, я и Мику отнесли свои подносы с едой и пошли на выход из столовой."
    
    jump d8_begunok

    label d8_mi_no_1:
    
    me "Да хватит тебе, Мику, мы быстренько справимся, даже как-либо поболтать или повеселится не успеем, как бегунок будет уже заполнен."

    show mi sad pioneer at center with dspr

    mi "Эх, ну ладненько, хотя бы навестите меня в музыкальном кружке."
    me "Обязательно."
    
    "Мику грустно вздохнула, а я активно принялся уплетать свой завтрак."
    
    show mi upset pioneer at center with dspr

    mi "И как только ты можешь есть эту гадость?"
    me "О чём ты? Вкусно же."
    mi "Ну не знаю, мне вообще не понравилось."
    me "Без обид конечно, но у тебя просто, как у японки, вкусы другие вот и всё."
    mi "Возможно[wp]"
    
    hide mi with dissolve

    "Закончив с завтраком, я попрощался с музыканткой и, отнесся поднос, вышел из столовой."

    jump d8_begunok

label d8_zavtrak_s_el_sh:

    window show dissolve
    th "Пожалуй пойду к своим ребятам, с ними как-то поуютнее будет."
    "Взяв поднос с завтраком, я отправился к ним."

    window hide dissolve
    show chair_l behind el
    show chair_r behind sh
    show table
    show shakers
    show left d8_breakfast_full tray foods behind shakers
    show el normal pioneer at wnfh_sit_left behind table
    show right d8_breakfast_half tray foods behind shakers
    show sh normal pioneer at wnfh_sit_right behind table
    with dissolve
    $ renpy.pause(1.0, hard=True)
    window show
    
    me "Доброе утро товарищи, есть место свободное?"
    sh "Да, садись."
    
    show mid d8_breakfast_full tray spoon foods with dissolve

    "И усевшись, я только сейчас осмотрел свой завтрак" 
    "Он представлял из себя кашу манную, да чай с булкой. {w}Но на сей раз булка была, похоже, с яблочным повидло."
    
    show mid d8_breakfast_full tray foods with dspr

    me "Как идут у вас дела? {w}Придумали что-нибудь как добыть детали?"
    
    "Последние слова я сказал чуть тише."
    
    show left d8_breakfast_half tray foods behind shakers with dspr

    show el sad with dspr 
    show sh upset with dspr
    
    "После моего вопроса, ребята немного пали духом. {w}Стало ясно, что они ничего не придумали."
    
    me "Что, ничего?"
    el "Ага[wp]"
    sh "Ну, не совсем. {w}Есть одна идея, но она довольно рисковая."
    me "Выкладывай всё равно."
    
    "Шурик огляделся по сторонам и, видимо удостоверившись, что никто не будет подслушивать, вернул свой взгляд обратно на меня."
    
    show el normal with dspr
    show sh serious with dspr

    show mid d8_breakfast_half tray foods with dspr
    
    sh "И так, я предлагаю сходить в старый лагерь."
    me "Но[wp] {w}Если вожатая узнает, то нам голову оторвут."
    sh "Я так тоже подумал."
    sh "Поэтому мы конечно же пойдем без её спроса." 
    sh "А для этого[wp]"
    me "Шурик стой!"
    
    "Через шепот прошипел я."
    "Краем глаза, я заметил, что к нашему столу идет вожатая." 
    "И крайне не хотелось бы, чтобы она услышала наши разговоры о старом лагере."
    
    show sh normal with dspr
    
    window hide
    show mt normal pioneer behind chair_r:
        xcenter 1.2
        ease_quart 3.0 xcenter 0.5
    $ renpy.pause(1.5)
    window show

    "Вскоре она подошла к нам."
    
    mt "Семён, давай скорее доедай и марш на выход, там тебя уже ждут!"
    
    th "И снова вы меня дёргаете по среди завтрака!"
    th "Видимо, всё же у вас нет совести."
    
    me "Да, хорошо." 
    
    "Как скоро вожатая пришла, также скоро она и ушла."
    
    window hide
    show mt normal pioneer behind chair_r:
        ease_quart 3.0 xcenter 1.2
    $ renpy.pause(1.5)
    window show
    
    me "После обеда расскажешь, а то меня вожатая опять на фронт отправляет."
    sh "Будем ждать."
    
    show mid d8_breakfast_empty tray foods with dissolve

    "Быстренько всё доев, я пошел на выход из столовой."
    
    jump d8_begunok
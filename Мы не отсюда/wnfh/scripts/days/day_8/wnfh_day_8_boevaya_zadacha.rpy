label d8_boevaya_zadacha:

    play music wnfh_music_list["magicians_assistant"] fadein 5.0

    "Я глубоко вздохнул и грустно поглядел на кровать."

    th "Покой мне только снится[wp]"

    me "Я весь во внимании."
    mt "И так, Семён, нам нужно будет сейчас сходить и забрать документы."
    me "Моя дедукция мне подсказывает, что их там чуть больше одной тонкой папки."

    show mt grin pioneer at center with dspr

    mt "Верно подмечено!"

    show mt normal pioneer at center with dspr

    mt "Так что давай пойдём, чем раньше начнём тем раньше закончим."

    "Я ещё раз бросил свой грустный и сонливый взгляд на кровать."

    th "Ну, может оно и к лучшему, может ночью спать буду нормально."

    stop ambience fadeout 3.5
    show bg ext_house_of_mt_day with dissolve
    play ambience ambience_camp_center_day fadein 3.5

    "Выйдя на улицу, вожатая закрыла за собой дом."

    me "Можно вопрос?"
    mt "Слушаю."
    me "А что за документы если не секрет?"
    mt "Да так, разные лагерные."
    mt "Почему-то администрация решила, что я главный доставщик у них тут."

    "Крайне недовольным голосом проговорила она."

    show bg ext_houses_day with dissolve

    me "Я так понимаю, это уже не первый раз так[wp]"
    mt "Правильно понимаешь. Мужа уже замучала посылать в райцентр за ними."
    me "А почему именно так?"

    "Вожатая пожала плечами."

    mt "Чёрт его знает."
    mt "Просто, им же ещё и не откажешь, обидется и навялят разной рутиной."
    me "И как же вы эти документы носили?"
    mt "Муж помогал, но сейчас у меня есть образцовый пионер, который всем ребятам пример, верно?"
    me "[wp]Верно."

    show bg ext_lenin_square_day_wnfh with dissolve2

    "Проходя через площадь, там меня завидели Алиса с Ульяной, который позвали меня к себе."
    "Но когда они поняли, что я с вожатой, они резко притихли."

    me "Ольга Дмитриевна, разрешите отойти к товарищам на минутку?"
    mt "Ох, давай быстрее."

    hide mt
    show dv normal pioneer2 at left
    show usw normalsmile pioneer at right
    with dissolve

    me "Что такое?"
    dv "Да вот, хотели позвать тебя в сто одно сыграть."

    show usw grin pioneer at right with dspr

    usw "Но, похоже кто-то сегодня провинился!"

    show dv smile pioneer2 at left with dspr

    "Девушки усмехнулись с меня."

    me "Ну знаете ли, вообще-то я не провинился, а просто помогаю вожатой." 

    show usw surp1 pioneer at right with dspr

    usw "Да ладно, чтобы ты по своей воле помогал, не верю!"
    dv "И в чём помогаешь?"
    me "А вот секрет!"

    show usw laugh2 pioneer at right with dspr

    usw "Да ладно, от близких товарищей секретов нет!"
    dv "Секрет значит[wp]"

    "Тихо пробубнила себе под нос Алиса."

    me "М?"
    dv "Да неважно."

    show dv normal pioneer2 at left with dspr

    dv "Ладно, не будем тебя задерживать, а то наругают ещё."
    me "Ага, спасибо."

    hide dv
    hide usw
    show mt normal pioneer at center
    with dissolve

    "Оставив свой подруг, которые моментом стали заговорщицки перешептываться, я вернулся к Ольге."

    mt "Угораздило же меня забыть панамку свою[wp]"
    me "А вот и я."
    mt "Отлично, пойдём скорее."

    stop music fadeout 5.0
    stop ambience fadeout 3.5
    scene bg ext_camp_entrance_car_wnfh
    show mt smile pioneer at right
    with dissolve2
    play ambience ambience_camp_entrance_day fadein 3.5
    $ wnfh_set_time("voice", "Николай")
    $ renpy.notify("В идеале, тут должен быть спрайт мужа ОД, но, пока-что, вместо него целое нихуя")
    "На лагерной остановке, кто бы сомневался, стоял автомобиль."
    "Рядом с ним стоял мужчина, который смотрел куда-то вдаль от лагеря и курил."

    mt "Здравствуй, Коленька."
    voice "Привет, дорогая."

    "Вожатая подошла к своему супргу и приобняла его."

    voice "Слушай, твои эти директора совсем с дубу рухнули."
    mt "Что такое?"
    voice "Да блин, три коробки заполненные бумагой, каждая, наверное, кило пять."

    th "Ёлки палки, во что меня ввязали[wp]"

    show mt grin pioneer at right with dspr

    mt "Как хорошо, что у меня есть пионер, который поможет мне."
    voice "Эксплуатацией занимаешься?"
    me "Да вообще жуть."

    show mt angry pioneer at right with dspr

    mt "Так!"

    "Вожатая приняла свою недовольную позу и уставилась на нас."

    mt "Давай документы уже, и мы пойдём."

    show mt normal pioneer at right with dspr

    "Коля, докурив сигарету, протянул мне руку."
    "Я даже удивился сначала, но руку всё же пожал."

    voice "Николай."
    me "Семён."
    voice "Ну, крепись, Семён."

    "Он открыл заднюю дверь и вытащил оттуда три коробки, которые поставил на землю."

    voice "Ну всё, я поехал, а то майор мне[wp]"

    show mt smile pioneer at right with dspr

    mt "Не будем говорить, что майор тебе. Спасибо тебе огромное!"

    show bg ext_no_bus with dissolve

    "Ольга и Николай чмокнулись на прощание, после чего он сел в авто и уехал."

    show mt sad pioneer at center with dspr

    mt "Так, теперь нужно придумать как это всё дотащить."

    "Я попробовал приподнять всю стопку коробок разом."
    "Оказалось, что это было не так тяжело и я разом их все поднял."

    show mt surprise pioneer at center with dspr

    mt "Надо же[wp]"
    me "Ну-с, осталось самое сложное."

    window hide dissolve
    stop ambience fadeout 3.5
    scene bg ext_clubs_day with dissolve2
    play ambience ambience_camp_center_day fadein 3.5
    play music music_list["always_ready"] fadein 5.0
    window show dissolve

    "Как только я вышел из-за ворот, меня тут же обдали водой."
    "А если быть точным, вода, по большей части, коснулась только коробок с документами."
    "Я был настолько удивлен произошедшим, что даже не знал как быть, поэтому просто встал."
    "Наконец я выглянул из-за коробок и посмотрел, кто же является виновником торжества."

    show kat scared pioneer at left with dissolve

    "На своё удивление, я обнаружил там стоящую Катю, а немного поодаль были, уже убегали, две рыжие."
    "Увидев, что её заметили, Катя решила попытаться ретироваться, но тут вмешалась вожатая."

    show mt rage pioneer close at right with dissolve

    mt "Это что тут творится?! Тайнаковская, а ну стоять!"

    "После грозных слов Ольги Дмитриевны, Катя, в ещё большем ужасе, остановилась и смотрела прямо на вожатую."
    "Я же поставил коробки с документами и осмотрел их."

    th "Кажется, вода не сильно повредила их[wp] Видимо, картон поглотил весь урон. Разве что верхней, ничем не прикрытой, нормально так досталось[wp] Ну, надеюсь они были не слишком важными."

    show mt angry pioneer close at right with dspr

    mt "Иди-ка сюда."
    #mt "Ком цу мир."

    show kat sad pioneer close at left with dspr 

    "Медленно и неохотно Катя подошла к нам."

    stop music fadeout 5.0
    play music music_list["my_daily_life"] fadein 5.0

    kat "О-Ольга Д-Д-Дмитриевна, это н-не я!"

    "Катя тараторила и запиналась, пытаясь доказать свою невиновность."

    mt "Уж очень надеюсь, что не ты! Потому-что у меня, пока-что, хорошее мнение о тебе!"

    kat "Я-Я[wp] Ну в общем[wp]"

    "Было видно, что от сильного переживания у неё не хватало словарного запаса."

    th "Думаю, надо вступиться за девушку."

    if wnfh_Data.FlagGet("d7_kat_oblivanie") == "me_oblil":

        th "Тем более, я, в каком-то роде, в одной лодке с ней."

    me "Ольга Дмитриевна, очевидно это рыжие устроили, я вон видел как они убегали."
    me "А Катю крайней сделали, может она вообще случайно тут проходила."

    if wnfh_Data.FlagGet("d7_kat_oblivanie") == "me_oblil":

        me "К тому же, я сам в такой ситуации буквально вчера был, и понимаю что она имеет ввиду."
        $ wnfh_Data.AddLove_points({"kat":1})

    show kat smile pioneer close at left
    show mt normal pioneer close at right
    with dspr

    mt "Что ж, звучит складно[wp]"

    show kat guilty pioneer close at left with dspr

    kat "Правда, я не совсем случайно проходила[wp] Вернее, случайно, но не случайно."

    "Мы переглянулись с вожатой непонимающим взглядом."

    kat "В общем, я шла через площадь в муз клуб, а там меня позвали Алиса с Ульяной."
    kat "Сказали, не хочу ли я понаблюдать за одной старой пионерской традицией."
    kat "А я, дура, и согласилась. Любопытно же."
    kat "А дальше как бы вот."

    "Вожатая внимательно слушала Катю, попутно, судя по её виду, выстраивая картину событий у себя в голове."

    mt "Так, а кто облил?"

    show kat thinking pioneer close at left with dspr

    kat "Алиса окатила из ведра, после чего она что-то сказала[wp]"

    "Она призадумалась."

    kat "Вроде — «кажется ошибочка вышла», и, всучив ведро мне в руки, убежала вместе с Ульяной."

    show kat sad pioneer close at left with dspr

    kat "Так вот всё и было[wp]"

    "Ольга Дмитриевна посмотрела на меня подозрительным взглядом."

    mt "Что скажешь, Семён. Верим?"
    me "Думаю верим."

    $ wnfh_Data.AddLove_points({"kat":1})

    mt "В таком случае, меняем план."
    mt "Ты и Катя отнесёте коробки в администрацию."
    mt "А я[wp]"

    show mt angry pioneer close at right with dspr

    mt "Я выхожу на тропу войны! Ух я им устрою!"

    show mt normal pioneer close at right with dspr

    mt "Кстати, там документы не пострадали?"
    me "Не особо, кроме верхних[wp]"

    "Вожатая подошла к коробкам и посмотрела на документы в верхней коробке."

    mt "М-да[wp] Хреново, тут были нужные[wp] Но, думаю они ещё годные."
    mt "Ладно, давайте несите их, а я пошла."

    hide mt 
    show kat sad pioneer close at center
    with dissolve
    stop music fadeout 5.0

    "Ольга Дмитриевна вручила Кате коробку с документами, после чего лёгким бегом, ушла в сторону площади."
    "Я же взял свои коробки обратно. Теперь, когда они были слегка размокшимы, держаться за них было не очень удобно."

    me "Тебе там не тяжело?"
    kat "Нет, всё нормально, донесу думаю."
    me "Ну-с, тогда в путь дорогу."

    "Катя, грустно хмыкнув, медленно последовала за мной."

    window hide dissolve
    scene bg ext_admin_day_wnfh with santa_barbara_in_blure_dissolve2
    $ renpy.pause(0.5)
    stop ambience fadeout 2.0
    scene bg int_admin_day_wnfh
    show kat sad pioneer at center
    with slide_right_blure_dissolve2
    play ambience ambience_int_cabin_day fadein 2.0
    $ renpy.pause(0.5)
    play sound wnfh_sfx_list["cardboard_box_drop"]
    show bg int_admin_boxes_day_wnfh with dspr

    "Наконец, мы тотащили коробки."
    "Хоть они и были лёгкими, на дистанции их вес был ощутимым."
    "Особенно устала Катя, что было видно по её виду."

    me "Давай присядем, отдохнём немного."

    show kat thinking pioneer at center with dspr

    kat "А если кто-нибудь придёт?"
    me "И что? Думаю, мы заслужили пять минут отдыха."

    show kat normal pioneer at center with dspr

    kat "Ну, пять минут, наверное, и можно."

    "Катя заняла дальний стул, скромно сев на его краю и уставив свой взгляд себе под ноги."
    "Я же расположился на стуле более вольяжно. Всё-таки я уже был тут не первый раз и знал, что сюда очень редко заходят."

    play music music_list["confession"] fadein 5.0

    if wnfh_Data.FlagGet("d7_kat_oblivanie") == "me_oblil":

        jump d8_boevaya_zadacha_1

    else:

        jump d8_boevaya_zadacha_2

label d8_boevaya_zadacha_1:

    show kat guilty pioneer at center with dspr

    kat "Знаешь, я немного наврала тебе с вожатой[wp]"
    me "Всмысле?"

    "Она задумчиво поглядело в окно."

    kat "Всё-таки это я облила тебя, а не Алиса."
    kat "Просто, знаешь, было такое чувство[wp] Обиды чтоле?"
    kat "Меня облили, а я ничего в ответ не сделала[wp]"

    if wnfh_Data.getChoice_result_number("d7_choice_n9") == 1:

        kat "И даже после твоих извинений в глубине души осталась некая неприязнь[wp]"

    kat "А Алиса с Ульяной воспользовались моими обидами на тебя, и подначили меня на обливание."
    kat "Но после того, как я сделала это, обида пусть и ушла, её заменило чувство стыда. {w=0.5}Мне очень стыдно[wp]"

    show kat sad pioneer at center with dspr

    "Катя посмотрела широкими глазами на меня."

    kat "Прости меня, пожалуйста."

    "Вся эта история из уст Кати умилила меня."

    show kat sad pioneer close at center with dspr

    "С легкой улыбкой, я встал и подошел к ней. Она же неотрывно смотрела на меня."

    me "Думаю, за искренность, можно и простить тебя."

    show kat smile pioneer close at center with dspr

    kat "П-Правда?"
    me "Правда. Я не умею долго держать обиды за пустяки."
    kat "Спасибо тебе."

    "Я усмехнулся."

    me "Да не за что в общем[wp]"
    kat "Слушай, раз уж такое дело[wp]"

    jump d8_boevaya_zadacha_3

label d8_boevaya_zadacha_2:

    show kat thinking pioneer at center with dspr

    kat "Наверное, я вынуждена просить прощения[wp]"
    me "Это ещё почему?"

    show kat guilty pioneer at center with dspr

    kat "Ну, я немного соврала, что это Алиса облила."
    me "Значит это была Ульяна?"
    kat "Нет, это была[wp]"

    "Она сделала глубокий вдох и выдох."

    kat "Это была я."
    me "Вот оно что[wp]"
    kat "Я просто наивная дурочка, и повелась на стандартные уговоры."
    kat "А они ещё так заливали красиво, что вот, лагерная традиция, все дела."

    show kat obida pioneer at center with dspr

    kat "Им, видите ли, казалось, что пополнение приехало очередное, а по итогу у меня сильное чувство стыда!"

    "Катя перевела свой взгляд на меня."

    show kat smile pioneer at center with dspr

    kat "Я немного ушла от темы."
    kat "Семён, я прошу у тебя прощения за мой необдуманный поступок!"

    show kat smile pioneer close at center with dspr

    "Усмехнувшись, я встал со стула и подошёл к ней."
    "Она же не отрывала от меня взгляда."

    me "Ладно, прощаю."

    show kat joy pioneer close at center with dspr

    kat "Правда?"
    me "Правда. Я не умею долго держать обиды. {w=0.5}Тем более на такую фигню."

    show kat smile pioneer close at center with dspr

    kat "Спасибо! Прям камень с плеч!"
    me "Та не за что."
    kat "Ну слушай, раз уж мы все помирились."

    jump d8_boevaya_zadacha_3

label d8_boevaya_zadacha_3:

    "Она встала со стула."

    kat "Не хочешь пойти со мной к Мику?"

    if wnfh_Data.FlagGet("d8_obed_me_kat_mi") == True:

        kat "Тем более она тебя приглаша к нам, а ты, вроде как, согласился."
        jump d8_boevaya_zadacha_3_yes

    window hide dissolve
    call screen wnfh_choice(
        ["kat", "Да, почему бы и нет", "Нет ничего лучше музыки для души", "d8_boevaya_zadacha_3_yes", {"kat":1, "mi":1}],
        ["neutral", "Думаю откажусь", "Я даже не помню как играть на гитаре!", "d8_boevaya_zadacha_3_no", {"kat":-1, "mi":-1}],
        ["d8_choice_n10", "Катя зовёт в музклуб"]
        ) with sphere_blure_dissolve2

label d8_boevaya_zadacha_3_yes:

    window show dissolve
    if wnfh_Data.FlagGet("d8_obed_me_kat_mi") == True:

        me "Что ж, раз дел у меня никаких нет[wp]"

    me "Хорошо, пойдём побренчим, благо идти тут недалеко."

    show kat joy pioneer close at center with dspr 

    kat "Превосходно!"

    show kat smile pioneer close at center with dspr

    kat "Тогда, давай не будем терять времени."
    kat "А то Мику меня уже заждалась небось."

    window hide dissolve
    jump d8_kat_mi_musclub
        
label d8_boevaya_zadacha_3_no:

    stop music fadeout 5.0
    window show dissolve

    me "Ты уж извини, но у меня сейчас другие дела."

    show kat upset pioneer close at center with dspr

    kat "Жаль[wp]"

    show kat happy pioneer close at center with dspr

    kat "Но, может быть в следующий раз получится к нам зайти?"
    me "Поживём увидем."

    window hide dissolve
    jump d8_male_clubs
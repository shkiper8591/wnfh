label d9_lineika:

    scene bg ext_lenin_square_sunset_wnfh
    show mt normal pioneer panama at left
    show sl normal pioneer at fright
    show usw normal pioneer at right
    show mz normal pioneer glasses at cright
    with dissolve
    $ renpy.pause(0.3)
    window show dissolve

    "К нашему приходу, на площади уже почти все собрались и построились."
    "Мы встали в строй и принялись ожидать начала объявления."

    mt "Доброе утро, товарищи пионеры."

    "Пионеры хором также пожелали доброго утра вожатой."

    mt "Сегодня я вас собрала, для важного объявления."

    show mt smile pioneer panama at left with dspr

    mt "Сперва наперва, сегодня починили душ."
    mt "Теперь вы не сваритесь заживо пока моетесь."

    "Говоря про душ, вожатая укоризненно смотрела на меня, и на позади стояющую Алису."

    mt "Помимо этого, у многоуважаемой Евгении есть сообщение для всех вас."

    show mz normal pioneer glasses at cleft with dspr

    "Посли этих слов, Женя вышла из строя и встала рядом с вожатой."

    mz "Товарищи, хочу сказать, что у нас с сегодняшнего дня свою работу начинает клуб журналистики."
    mz "Поэтому, нам очень нужны ответственные пионеры, которые умеют грамотно писать и фотографировать."
    mz "И у нас уже есть один участник, ещё вчера записавшийся."

    "Заявление Жени было встречено без особого энтузиазма со стороны народа."
    "Все просто стояли и переглядывались."

    show mz bukal pioneer glasses at cleft with dspr

    mz "В общем, если есть желающие, приходите в библиотеку. {w=0.5}На этом у меня всё."

    show mz bukal pioneer glasses at cright with dspr

    "Закончив, она вернулась обратно в строй."

    if wnfh_Data.FlagGet("mt_angry") == True:

        mt "Помимо этого, вызываю из строя Семёна и Ульяну!"

        show usw normal pioneer at cleft with dspr

        "Улька без промедлений вышла из строя."
        "Я же сначала немного потоптался на месте, после чего подошёл."

        mt "И так, Ульяна, сегодня Семён будет помогать тебе на складе."
        mt "Он в полном твоём подчинении."

        th "Вот ещё чего не хватало[wp]"

        show usw laugh pioneer at cleft with dspr

        usw "Есть, гржнинначаник!"

        "Радостно ответила она и отсалютовала."
        "На такой ответ, вожатая недовольно фыркнула, но ничего не сказала."

        mt "Можете возвращаться в строй."

        "Мы вернулись на свои места."

    mt "Что же! На этом у меня всё. Можете отправляться в столовую."

    hide sl
    hide mz
    hide usw
    hide mt
    with dissolve

    "Как только пионеры заслышали про столовую, те мигом повернулись и отправились за завтраком."

    if wnfh_Data.FlagGet("mt_angry") == True:

        jump d9_lineika_w_usw

    else: 

        jump d9_zavtrak

label d9_lineika_w_usw:

    show usw normalsmile pioneer at center with dissolve

    "В этот момент ко мне подошла Ульяна."

    usw "Ну давай, рассказывай, в чём виноват будешь?"
    me "У меня тот же самый вопрос к тебе."

    show usw laugh2 pioneer at center with dspr

    "Улька громко усмехнулась."

    show usw grin pioneer at center with dspr

    usw "Я-то по своей инициативе, а ты давай от темы не увиливай."

    "Я тяжело вздохул."

    me "Да свалил порученное мне задание на другого человека."
    me "Вот и получил по шапке."

    if wnfh_Data.getChoice_result_number("d8_choice_n11") == 1:

        show usw smile pioneer at center with dspr

        usw "А я думала за ночные игры на эстраде."
        me "Алиса уже успела проболтаться?"
        usw "Да тут и ежу понятно, кто за этим стоит."
        me "Ну, за это тоже я отдуваюсь."
        me "Видимо, об участии Алисы никто, кроме нас, не знает."

        show usw grin pioneer at center with dspr

        usw "Будет чем шантажировать!"

    show usw normalsmile pioneer at center with dspr

    me "Ты кстати говорила, что на складе по собственной инициативе."

    "Она быстро закивала головой."

    usw "Верно-верно."
    me "Странно, я думал там только Славя помогает."
    usw "Она сегодня другим занята, а дедушке всё ещё плохо."
    usw "Вот и выручаю."
    me "Не проще тогда просто склад закрыть?"

    show usw upset pioneer at center with dspr

    "Ульяна развела руками в сторону."

    usw "Не знаю, видимо нет."

    jump d9_zavtrak_w_usw_dv
label d9_lineika:

    scene bg ext_lenin_square_sunset_wnfh
    show mt normal pioneer panama at left
    show sl normal pioneer at fright
    show usw normal pioneer at right
    show mz normal pioneer glasses at cright
    with dissolve
    $ renpy.pause(0.3)
    window show dissolve

    "К нашему приходу на площади уже почти все собрались и построились."
    "Мы встали в строй и принялись ожидать начала объявления."

    mt "Доброе утро, товарищи пионеры!"

    "Пионеры хором пожелали доброго утра вожатой."

    mt "Сегодня я собрала вас для важного объявления."

    show mt smile pioneer panama at left with dspr

    mt "Сперва-наперво, сегодня починили душ."
    mt "Теперь можно мыться, не боясь свариться заживо."

    "Говоря про душ, вожатая укоризненно посмотрела на меня и на стоящую позади Алису."

    mt "Помимо этого, у многоуважаемой Евгении есть сообщение для всех вас."

    show mz normal pioneer glasses at cleft with dspr

    "После этих слов Женя вышла из строя и встала рядом с вожатой."

    mz "Товарищи, хочу сказать, что у нас с сегодняшнего дня свою работу начинает клуб журналистики."
    mz "Нам очень нужны ответственные пионеры, которые умеют грамотно писать и фотографировать."
    mz "Ещё вчера к нам записался первый участник."

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
        "Я же сначала немного потоптался на месте, после чего вышел."

        mt "Итак, Ульяна, сегодня Семён будет помогать тебе на складе."
        mt "Он в полном твоём подчинении."

        th "Этого только не хватало[wp]"

        show usw laugh pioneer at cleft with dspr

        usw "Есть, гржнинначаник!"

        "Радостно ответила она и отсалютовала."
        "Вожатая недовольно фыркнула, но ничего не сказала."

        mt "Можете возвращаться в строй."

        "Мы вернулись на свои места."

    mt "Что ж, на этом у меня всё. Можете отправляться в столовую."

    hide sl
    hide mz
    hide usw
    hide mt
    with dissolve

    "Как только пионеры заслышали про столовую, они мигом повернулись и отправились за завтраком."

    window hide dissolve

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

    usw "Я-то по своей инициативе, а ты давай от темы не увиливай!"

    "Я тяжело вздохул."

    me "Да свалил порученное мне задание на другого человека."
    me "Вот и получил по шапке."

    if wnfh_Data.getChoice_result_number("d8_choice_n11") == 1:

        show usw smile pioneer at center with dspr

        usw "А я думала, что за ночные игры на эстраде."
        me "Алиса проболталась?"
        usw "Да тут и ежу понятно, кто за этим стоит!"
        me "Ну, за это тоже я отдуваюсь."
        me "Видимо, об участии Алисы не знает никто, кроме нас."

        show usw grin pioneer at center with dspr

        usw "Будет чем шантажировать!"

    show usw normalsmile pioneer at center with dspr

    me "Ты, кстати, говорила, что на складе по собственной инициативе."

    "Она быстро закивала головой."

    usw "Верно, верно."
    me "Странно, я думал, там только Славя помогает."
    usw "Она сегодня другим занята, а дедушке всё ещё плохо."
    usw "Вот и выручаю."
    me "Не проще тогда просто закрыть склад?"

    show usw upset pioneer at center with dspr

    "Ульяна развела руками в сторону."

    usw "Не знаю. Видимо, нет."

    "Она остановилась."

    usw "Так, ты иди, а мне надо быстренько кое-куда отойти."
    usw "Если что, в столовой пересечёмся."

    hide usw with dissolve

    "Ульяна ловко вырвалась вперёд и ускакала куда-то в сторону спортплощадки."
    "Пожав плечами, я продолжил свой путь."

    window hide dissolve
    jump d9_zavtrak
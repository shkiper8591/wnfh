label d9_evening:

    scene bg ext_lenin_square_sunset_wnfh with Dissolve(5.0)
    play ambience ambience_camp_center_evening fadein 5.0
    $ renpy.pause(0.3)
    play music music_list["reflection_on_water"] fadein 5.0
    window show dissolve

    "Поужинав в компании товарищей моделистов, мы разошлись по свои сторонам."
    "Моя сторона вывела меня к площади."

    th "Если все дороги ведут в Рим, то в «Совёнке» все дороги ведут к Ленину."

    if wnfh_Data.FlagGet("d9_zavtrak_w_dv_usw") == True:

        jump d9_evening_w_dv

    else:

        jump d9_evening_cont

label d9_evening_w_dv:

    th "Надо бы присесть где-нибудь, и подождать Алису."
    th "Странно, что я не встретил её в столовой. В прочем, там была такая толкучка, что её и сова не заметила бы."

    "Упав на ближайшую лавочку, я стал ждать."

    show dv smile pioneer at center with dissolve

    "Но, не успел я сесть, как ко мне подошла моя подруга."

    dv "А вот и я."
    me "Приветик."

    "Сказал я довольно безынициативно."

    show dv normal pioneer at center with dspr

    dv "Эй, ты чего раскис?"

    if wnfh_Data.FlagGet("mt_angry") == True:

        me "Не знаю, на складе устал наверное."
        me "Да и наёлся ещё вот."

    else:

        me "Объелся походу."

    show dv guilty pioneer at center with dspr

    dv "Тогда, получается, прогулка отменяется?"
    me "Не, не, всё в силе."

    show dv smile pioneer at center with dspr

    dv "О, это просто прекрасно!"

    "Я протянул руку Алисе."

    me "Поможешь встать?"

    "Медленно взявшись за мою руку, одним резким движением она подняла меня на ноги."

    me "Ну не так же резко!"

    show dv grin pioneer at center with dspr

    dv "Извини, но ты не уточнял этого."
    me "Справедливо[wp] Ну так что, куда мы отправляемся?"

    show dv smile pioneer at center with dspr

    dv "Следуй за мной."

    window hide dissolve
    $ renpy.pause(0.3)
    jump d9_me_dv_date

label d9_evening_w_kat:

    window hide dissolve
    scene bg ext_houses_sunset
    show kat normal pioneer at center
    with santa_barbara_out_blure_dissolve2
    $ renpy.pause(0.3)
    window show dissolve

    "Шагали мы неспеша. В прочем, это из-за меня, наш темп был столь медленным."
    "Всё-таки, пробежать марафон с целым человеком на себе, это то ещё испытание."
    "Так что идти мне было немного[wp] Затруднительно."

    kat "Ты там как, в порядке? А то еле-еле идёшь."
    me "Да-да, ноги просто немного устали."

    show kat thinking pioneer at center with dspr

    kat "Да уж, представляю[wp]{nw=2}"

    show kat joy pioneer at center with dspr

    extend " Зато ты у нас прям герой!"

    "Я слегка усмехнулся."

    me "Медали или грамоты только не хватает."

    show kat smile pioneer at center with dspr

    "Катя посмеялась с моей шутки."

    show kat happy pioneer at center with dspr

    kat "Думаю, Мику что-нибудь придумает тебе в благодарность."
    
    "На это я только пожал плечами."

    show kat upset pioneer at center with dspr

    kat "Интересно, как она будет себя чувствовать."
    me "Я уверен что более чем нормально."

    show kat sad pioneer at center with dspr

    kat "Не знаю, ожоги это вещь серьёзная."
    me "Это правда, да, но у неё точно ничего серьёзного."
    me "Завтра очнётся, мы утром навестим её и уже будем со смехом вспоминать эту ситуацию."

    show kat smile pioneer at center with dspr

    kat "Да, пожалуй ты прав."

    "Между нами повисла пауза."
    "Но длилась она недолго, когда Катя её нарушила."

    show kat normal pioneer at center with dspr

    kat "Слушай, а ты сейчас занят будешь?"
    me "Да вроде нет."
    
    show kat smile pioneer at center with dspr

    kat "Может тогда немного погуляем?"
    kat "Просто я подумала, что мне очень сильно нужно развеяться по всего этого."
    kat "И лучше это сделать где-нибудь за пределами лагеря."

    "Я посмотрел на солнце, пытаясь оценить примерное время."

    me "Идея конечно неплохая, но солнце уже близко к закату."
    kat "Так я и говорю же немного. От силы часик, может полтора."

    "В целом я против не был. Погулять по лесу всегда было моим любимым занятием, особенно летом."
    "С другой стороны, меня сильно беспокоило уже позднее время. В лесу темнее гораздо раньше, и остаться там в темноте, такая себе перспектива."
    "В прочем[wp]{nw=2.0}"

    me "Хорошо, давай погуляем, только не будем уходить далеко."

    show kat joy pioneer at center with dspr

    kat "Добро!"
    me "Тогда следуй за мной."

    "Ускорив шаг, мы свернули в сторону леса."

    jump d9_me_walk_w_kat

label d9_evening_cont:

    "Делать было нечего, но делать что-то хотелось."
    "Я смотрел на Ленина, а он, как будто бы, смотрел на меня."

    th "Товарищ Ильич, может подскажете, может озарите путь?"

    "Но, памятник оставался безмолвным."

    th "На что я рассчитывал? Похоже уже совсем скоро кукухой поеду, так что скоро заведу себе шизофрению и буду общаться с ней."
    th "Хотя, боюсь оно не выдержит моей компании и съедет куда подальше."

    jump d9_me_un_evening
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

label d9_evening_cont:

    "Делать было нечего, но делать что-то хотелось."
    "Я смотрел на Ленина, а он, как будто бы, смотрел на меня."

    th "Товарищ Ильич, может подскажете, может озарите путь?"

    "Но, памятник оставался безмолвным."

    th "На что я рассчитывал? Похоже уже совсем скоро кукухой поеду, так что скоро заведу себе шизофрению и буду общаться с ней."
    th "Хотя, боюсь оно не выдержит моей компании и съедет куда подальше."

    jump d9_me_un_evening
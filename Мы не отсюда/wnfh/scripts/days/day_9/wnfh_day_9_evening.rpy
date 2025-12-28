label d9_evening:

    $ wnfh_set_time("sunset")
    scene bg ext_lenin_square_sunset_wnfh with Dissolve(5.0)
    play ambience ambience_camp_center_evening fadein 5.0
    $ renpy.pause(0.3)
    play music music_list["reflection_on_water"] fadein 5.0
    window show dissolve

    "Поужинав в компании товарищей-моделистов, я попрощался с ними и пошёл своей дорогой."
    "И — кто бы мог подумать — вышел на площадь."

    th "Если все дороги ведут в Рим, то в «Совёнке» все дороги ведут к Ленину."

    if wnfh_Data.FlagGet("d9_zavtrak_w_dv_usw") == True:

        jump d9_evening_w_dv

    else:

        jump d9_evening_cont

label d9_evening_w_dv:

    th "Пока присяду где-нибудь и подожду Алису."
    th "Странно, что я не встретил её в столовой. Впрочем, там была такая толкучка, что её и сова не заметила бы."

    "Упав на ближайшую лавочку, я стал ждать."

    show dv smile pioneer at center with dissolve

    "Но не успел я сесть, как моя подруга тут же нарисовалась передо мной."

    dv "А вот и я."
    me "Приветик."

    "Ответ мой прозвучал несколько вяло, что не прошло мимо ушей Алисы."

    show dv normal pioneer at center with dspr

    dv "Эй, ты чего раскис?"

    if wnfh_Data.FlagGet("mt_angry") == True:

        me "Не раскис, просто несколько устал после дня на складе."
        me "Да и наелся к тому же."

    else:

        me "Да я не раскис, просто переел, походу."

    show dv guilty pioneer at center with dspr

    dv "Тогда, получается, прогулка отменяется?"
    me "Не-не, всё в силе."

    show dv smile pioneer at center with dspr

    dv "Прекрасно!"

    "Я протянул руку Алисе."

    me "Поможешь встать?"

    show dv smile pioneer close at center with dspr

    "Медленно взявшись за мою руку, она подняла меня на ноги одним резким движением."

    me "Ну не так же резко!"

    show dv grin pioneer at center with dspr

    dv "Извини, надо было уточнять!"
    me "Справедливо[wp] Ну так что, куда мы отправляемся?"

    show dv smile pioneer at center with dspr

    dv "Пошли, сам всё увидишь."

    window hide dissolve
    $ renpy.pause(0.3)
    jump d9_me_dv_date

label d9_evening_cont:

    "Делать было нечего. А хотелось."
    "Я смотрел на Ленина, а он, в свою очередь, будто бы смотрел на меня."

    th "Товарищ Ильич, может, подскажете? Озарите путь, так сказать."

    "Но памятник оставался безмолвным."

    th "Совсем уже кукуха едет. Такими темпами я правда придумаю себе шизотоварища и буду с ним трепаться."
    th "Хотя, боюсь, он не выдержит моей компании и съедет куда подальше."

    jump d9_me_un_evening
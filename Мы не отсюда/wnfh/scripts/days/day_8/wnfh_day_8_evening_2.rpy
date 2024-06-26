label d8_evening_2:

    scene bg ext_lenin_square_sunset_wnfh with slide_up_blure_dissolve2
    play ambience ambience_camp_center_evening fadein 2.0
    play music music_list["dance_of_fireflies"] fadein 5.0

    if wnfh_Data.getChoice_result_number("d8_choice_n10") == 1:

        "Вернувшись на площадь, Катя помахала мне на прощание и ушла к домикам."

        if wnfh_Data.getChoice_result_number("d8_choice_n11") == 1:

            jump d8_evening_2_w_dv
    
        else:

            jump d8_ending

    else:

        "Вернувшись в лагерь, я вышел на площадь."
        "Дело медленно шло к ночи, поэтому пионеров тут особо не было."
        "Да и мне в целом тут делать было нечего, посему я направился к себе домой."

        jump d8_ending

label d8_evening_2_w_dv:

    "Я же уселся на первой попавшейся лавочке, и стал дожидаться своей рыжей подруги."

    th "Надеюсь, мне не придётся ждать до следующего утра."

    window hide dissolve
    stop ambience fadeout 2.0
    scene bg ext_lenin_square_night_wnfh with dissolve2
    play ambience ambience_camp_center_night fadein 2.0
    $ wnfh_set_time("night")
    $ renpy.pause(0.2)
    window show dissolve

    "А тем временем, на лагерь спустилась ночь."
    "На площади остался только я один."

    show dv normal pioneer at center with dissolve

    "Я уже собирался уходить, но тут всё же подошла Алиса."

    me "Долго же тебя не было."

    show dv smile pioneer at center with dspr

    dv "Извини, Ульяна не может уснуть без сказки на ночь."
    me "Смешно."

    show dv laugh pioneer at center with dspr

    dv "А-то!"

    "Она посмеялась со своей же шутки и легонько стукнула меня в плечо."

    show dv smile pioneer at center with dspr

    dv "Ну что, пошли на сцену?"
    me "Ага[wp] Только у меня гитар нет."

    show dv angry pioneer at center with dspr

    dv "Как это нет?"

    "Алиса моментально переменилась в лице, а её голосе слышалась злоба."

    th "Возможно, я зря сказал это[wp] С другой стороны, как долго бы ещё продержался мой обман? Секунд десять?"

    me "Ну вот, нет. Мику подслушала наш диалог и отказалась давать гитары."
    dv "Зараза она мелкая[wp]"

    "Прошипела сквозь зубы она."

    show dv normal pioneer at center with dspr

    dv "Ладно, поступим по другому."
    me "Пойдём спать?"

    show dv grin pioneer at center with dspr

    dv "Пойдём и просто возьмём гитары у неё. Прямо сейчас."

    "Я непонимающе посмотрел на Алису."

    me "Ты хочешь ограбить музклуб?"
    dv "Ну почему сразу ограбить-то? Мы поиграем и вернём на место, всего-то делов."
    me "А может лучше спать?"

    show dv angry pioneer at center with dspr

    dv "Ты уже дал своё согласие."

    "Тяжело вздохнув, я отмахнулся рукой."

    me "Ладно, давай по быстрому сделаем это уже."

    show dv smile pioneer at center with dspr

    dv "Отлично! Идём скорее."

    window hide dissolve
    show bg ext_music_club_night_wnfh 
    show dv normal pioneer at center
    with dissolve
    window show dissolve

    "Быстрым шагом, мы вышли к музклубу."

    me "Слушай, а как ты собираешься проникнуть внутрь?"
    me "Дверь и окна, наверняка, закрыты."

    show dv smile pioneer at center with dspr

    dv "О, это вовсе не проблема."

    "Она достала из кармана рубашки заколку."

    me "Этим дверь не откроешь[wp]"
    dv "Хочешь фокус покажу?"
    me "Ч-Что? Сейчас же не до этого."
    dv "Отвернись быстренько."
    me "Ты шутишь?"

    show dv angry pioneer at center with dspr

    dv "Отвернись."

    hide dv with dspr

    "Я развел рукам и отвернулся."

    dv "Теперь можешь поворачиватся."

    show dv normal pioneer at center with dspr

    "Когда я повернулся, Алиса держала в руке и заколку, и отвёртку."
    "Я решил не спрашивать откуда она её достала, и, цокнув языком, просто пошёл к музклубу."

    dv "Ой, какой ты скучный."

    show bg ext_musclub_verandah_night_wnfh with dissolve

    "Подойдя к двери, я аккуратно дернул ручку. Дабы удостверится, точно ли она закрыта."
    "А то зная неряшливость Мику, всякое может случится."
    "Но нет, дверь была точно закрыта."

    me "Ну давай, взламывай."

    show dv smile pioneer at center with dspr

    "Ехидно усмехнувшись, Алиса подошла к двери и принялась ковырится в дверном замке."

    play sound sfx_alisa_picklock loop fadein 2.0

    me "И как много времени это займёт."
    dv "Замок старый, наверное, не очень много."

    play sound sfx_click_2
    show dv normal pioneer at center with dspr

    "В этот же момент, послышался некий тихий звук."

    dv "Зараза[wp]"
    me "Что такое?"
    dv "Заколку сломала."
    me "Ну, похоже, не поиграем сегодня."

    "Сказал я, и уже стал спускатся с крыльца музклуба."

    dv "Не-не-не, погоди, меня так просто не победить."

    "Глубоко вздохнув, я остановился и продолжил наблюдать за ней."

    me "Ну, а как ты её откроешь-то?"
    dv "Легко!"

    "Одним сильным ударом, она загнала отвёртку в защелку и стала водить инструмент туда сюда."

    me "Сломаешь же."
    dv "Ну да, в этом и цель."
    me "Ох, блин, на что я подписался[wp]"

    "Пока-что, на этом повествование обрывается."
    "Дальнейший клик отправит вас в главное меню игры."
    "Я вас предупредил!"

    #play music wnfh_music_list["the_historical_society"] fadein 5.0
label d7_ending:

    window hide dissolve
    stop ambience fadeout 0.5
    scene bg ext_lenin_square_night_wnfh with slide_left_blure_dissolve2
    play ambience ambience_camp_center_night fadein 3

    if wnfh_Data.getChoice_result_number("d7_choice_n8") == 1:

        jump d7_ending_un

    elif wnfh_Data.getChoice_result_number("d7_choice_n8") == 2:

        jump d7_ending_dv

    else:

        jump d7_ending_main

label d7_ending_un:
    
    window show dissolve

    "Проходя через площадь, я всё же решил обдумать произошедшее на пляже."
    
    th "Никогда бы не подумал, что Лена сделает что-то подобное."
    th "Обычно она такая стеснительная вся[wp] молчаливая."
    th "Только краем глаза посмотришь на неё, так она сразу вся заминается."
    th "И двух слов связать не может, взгляд в сторону уводит. "
    th "А тут[wp]"
    
    show bg ext_houses_night_wnfh with dissolve2

    th "Не верю я, что это просто так[wp]"
    th "В прочем[wp] {w}Пофигу как-то, наверное."
    th "Может если дел завтра не будет особо и я смогу выцепить Лену, то поинтересуюсь у неё."

    window hide dissolve
    jump d7_ending_main

label d7_ending_dv:
 
    window show dissolve

    "Выйдя на площадь, я задумался над встречей с Алисой на сцене."

    th "Какая-то она странная была[wp]"
    th "Как бы вела себя как обычно, но при этом вот что-то не то."
    th "Будто желала что-то сказать, помимо предложения посидеть под гитарку."
    th "Но либо не стала, либо не хотела. {w}В прочем, завтра вероятнее всего я всё сам узнаю, если соглашусь разумеется."

    show bg ext_houses_night_wnfh with dissolve2

    th "А пока мне бы придумать, что такого сказать Ольге Дмитриевне."
    th "Какая на сей раз у меня будет отмазка[wp]"
    th "Хотя[wp] Пофигу, так и скажу ей, что гулял, всё равно она и так понимает, что все мои отмазки это враньё."

    window hide dissolve
    jump d7_ending_main

label d7_ending_main:
   
    scene bg ext_house_of_mt_night_without_light with slide_right_blure_dissolve2
    window show dissolve

    "Некоторое время спустя, я дошел до дома, в котором свет не горел."
    "Это было одновременно хорошей и плохой новостью."
    "Хорошо, ибо не придется устраивать тёрки с вожатой по вопросу ночных прогулок."
    "А плохо то, что не видно не зги, как бы ноги не переломать"
    
    window hide dissolve
    $ wnfh_set_volume("sound", 0.3)
    play sound sfx_open_door_1
    scene bg int_house_of_mt_night2 with door_blure_dissolve2
    stop ambience fadeout 1
    play ambience ambience_int_cabin_night fadein 3
    window show dissolve

    "Аккуратно войдя во внутрь, я тихонько подошел к своей кровати."
    "Быстренько разделся и наконец лег на мягкую постель."
    "Это было прекрасное чувство."
    
    show blink
    stop ambience fadeout 3
    
    "И сон быстро утащил меня в свой мир[wp]"
    
    window hide dissolve
    $ renpy.pause(1.5, hard=True)
    
    jump wnfh_day_8
label d7_ending:

    window hide dissolve
    stop ambience fadeout 0.5
    scene bg ext_lenin_square_night_wnfh with slide_left_blure_dissolve2
    play ambience ambience_camp_center_night fadein 3

    if wnfh_Data.getChoice_result_number("d7_choice_n8") == 2:

        jump d7_ending_un

    elif wnfh_Data.getChoice_result_number("d7_choice_n8") == 1:

        jump d7_ending_dv

    else:

        jump d7_ending_main

label d7_ending_un:
    
    window show dissolve

    "Проходя через площадь, я обдумывал произошедшее на пляже."
    
    th "Никогда бы не подумал, что Лена сделает что-то подобное."
    th "Обычно она такая стеснительная вся, молчаливая[wp]"
    th "Только краем глаза посмотришь на неё, так она сразу чуть ли не в комок съёживается."
    th "И двух слов связать не может, взгляд в сторону уводит[wp]"
    th "А тут[wp]"
    #КОСЯК: вариация, где Лена не обнимает Семёна, и тот ничем особо не удивлён. Или можно если ЛП Лены меньше 4 сразу перекинуть на мейн-эндинг.
    
    show bg ext_houses_night_wnfh with dissolve2

    th "Не верю я, что это просто так."
    th "Впрочем[wp] {w}Не так это и важно, наверное."
    th "Может, если дел завтра особо не будет и я смогу выцепить Лену, то поинтересуюсь у неё."

    window hide dissolve
    jump d7_ending_main

label d7_ending_dv:
 
    window show dissolve

    "Выйдя на площадь, я задумался над встречей с Алисой на сцене."

    th "Как-то она странно себя вела[wp]"
    th "Вроде как обычно, но при этом[wp] Что-то вот не то."
    th "Будто желала что-то сказать помимо предложения посидеть под гитарку."
    th "Но либо не стала, либо расхотела. {w}Впрочем, завтра, вероятнее всего, я всё сам узнаю. Если соглашусь, разумеется."

    show bg ext_houses_night_wnfh with dissolve2

    th "А пока мне бы придумать, что бы такого сказать Ольге Дмитриевне."
    th "Какая на сей раз у меня будет отмазка?"
    th "Хотя[wp] Пофигу, так и скажу ей, мол, гулял. Всё равно она и так понимает, что все мои отмазки — враньё."

    window hide dissolve
    jump d7_ending_main

label d7_ending_main:
   
    scene bg ext_house_of_mt_night_without_light with slide_right_blure_dissolve2
    window show dissolve

    "Некоторое время спустя я дошёл до домика. Свет не горел."
    "Это было одновременно хорошей и плохой новостью."
    "Хорошо, ибо не придётся устраивать тёрки с вожатой по вопросу ночных прогулок."
    "А плохо то, что не видно ни зги. Ноги бы не переломать[wp]"
    
    window hide dissolve
    $ wnfh_set_volume("sound", 0.3)
    play sound sfx_open_door_1
    scene bg int_house_of_mt_night2 with door_blure_dissolve2
    stop ambience fadeout 1
    play ambience ambience_int_cabin_night fadein 3
    window show dissolve

    "Аккуратно войдя внутрь, я тихонько подошёл к своей кровати."
    "Быстренько разделся и, наконец, лёг в мягкую постель."
    "Прекрасное чувство[wp]"
    
    show blink
    stop ambience fadeout 3
    
    "Объятий сна долго ждать не пришлось — я почти сразу же отправился в мир сновидений."
    
    window hide dissolve
    $ renpy.pause(1.5, hard=True)
    
    jump wnfh_day_8
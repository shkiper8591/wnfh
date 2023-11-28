label d7_ending:

    window hide
    stop ambience fadeout 0.5
    scene bg ext_lenin_square_night_wnfh with slide_left_blure_dissolve2
    play ambience ambience_camp_center_night fadein 3
    window show
    
    #if wnfh_Data.getChoice_result_number("d7_choice_n8") == 1:

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

    #if wnfh_Data.getChoice_result_number("d7_choice_n8") == 2:

        #"placeholder"
        ##я короче это дело всё закоментил до тех времён, когда начну писать рут Алисы. А то сейчас писать эту херню толку мало.
    
    window hide dissolve
    scene bg ext_house_of_mt_night_without_light with slide_right_blure_dissolve2
    window show dissolve

    "Тем временем я дошел до дома, в котором свет не горел."
    "Это было одновременно хорошей и плохой новостью."
    "Хорошо, ибо не придется устраивать тёрки с вожатой по вопросу ночных прогулок."
    "А плохо то, что не видно не зги, как бы ноги не переломать"
    
    window hide
    $ wnfh_set_volume("sound", 0.3)
    play sound sfx_open_door_1
    scene bg int_house_of_mt_night2 with door_blure_dissolve2
    stop ambience fadeout 1
    play ambience ambience_int_cabin_night fadein 3
    window show

    "Аккуратно войдя во внутрь, я тихонько подошел к своей кровати."
    "Быстренько разделся и наконец лег на мягкую постель."
    "Это было прекрасное чувство."
    
    show blink
    stop ambience fadeout 3
    
    "И сон быстро утащил меня в свой мир[wp]"
    
    window hide dissolve
    $ renpy.pause(1.5, hard=True)
    
    jump wnfh_day_8
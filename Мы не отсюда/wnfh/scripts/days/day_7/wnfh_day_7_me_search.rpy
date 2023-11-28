label d7_me_search:

    window hide dissolve
    stop ambience fadeout 3.5
    scene bg ext_lenin_square_day_wnfh with slide_right_blure_dissolve2
    play ambience ambience_camp_center_day fadein 3.5
    $ renpy.pause(0.5)
    window show dissolve

    "Выйдя на площадь, я стал раздумывать, где можно будет найти этих двух рыжих террористок."

    th "Возможно они у себя дома, хотя в такую жаркую погоду делать дома нечего."
    th "В таком случае, они могут быть либо на спортплощадке, ибо обе любительницы спорта."
    th "Либо же на пляже, где могут лежать и загорать или вообще купаться."
    th "Вообще они могут быть где угодно, но это три самых вероятных места их нахождения и их стоит проверить в первую очередь."

    ## Можно стилизовать под карту, но пока будет так

    window hide dissolve
    call screen wnfh_choice(
        ["dv", "Их домик", "Самое очевидное", "d7_me_search_dv_house"],
        ["dv", "Спортплощадка", "Чуть менее очевидно", "d7_me_search_dv_sport"],
        ["dv", "Пляж", "Совсем не очевидно", "d7_me_search_dv_beach"],
        ["d7_choice_n10", "Где искать рыжих"]
        ) with sphere_blure_dissolve2

label d7_me_search_dv_house:

    th "Ладно, начну с самого очевидного и пойду проверю их домик."

    scene bg ext_house_of_dv_day with dissolve2
    stop music fadeout 3.5

    "Спустя некоторое время, я стоял перед входом в их дом."
    "Занавеска на дверном окошке не была закрыта, и я аккуратно заглянул внутрь помещения."
    
    ##Тут должно быть ЦГ с переодевающимися Ульяной и Алисой
    
    play music music_list["eternal_longing"] fadein 3.5

    "И увидел то, чего не должен был видеть: Алиса и Ульяна стояли только в нижнем белье и переодевались."
    "К сожалению или счастью они стояли ко мне спиной, и поэтому не заметили меня."
    
    th "Вот чёрт, и что же теперь делать[wp]"
    
    window hide dissolve
    call screen wnfh_choice(
        ["dv", "Продолжить наблюдать", "Это точно ничем хорошим не кончится", "d7_me_peeking", {"dv":-1, "usw":-1}],
        ["dv", "Дать о себе знать", "Лучше мне не рисковать", "d7_me_knock", {"dv":1, "usw":1}],
        ["d7_choice_n11", "Подсмотреть за рыжими или нет"]
        ) with sphere_blure_dissolve2
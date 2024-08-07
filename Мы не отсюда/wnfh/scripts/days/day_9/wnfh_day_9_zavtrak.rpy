label d9_zavtrak:

    scene bg ext_dining_hall_near_sunset with dissolve2
    $ renpy.pause(0.3)
    scene ext_dining_hall_near_sunset with dissolve
    $ renpy.pause(0.3)
    stop ambience fadeout 2.0
    stop music fadeout 5.0
    scene bg int_dining_hall_people_sunset_wnfh with dissolve2
    play ambience ambience_dining_hall_full fadein 2.0
    $ renpy.pause(0.3)
    window show dissolve

    # с Мику, на данный момент, невозможно набрать 4 и более очка ЛП, но тем не менее на будущее это здесь останется
    if wnfh_Data.getChoice_points_sum("kat") or wnfh_Data.getChoice_points_sum("mi") >= 4:

        jump d9_zavtrak_w_kat_mi

    # С Ульяной та же песня, что и с Мику
    elif wnfh_Data.getChoice_points_sum("dv") or wnfh_Data.getChoice_points_sum("usw") >= 4:

        jump d9_zavtrak_w_dv_usw

    else:

        jump d9_zavtrak_w_un

label d9_zavtrak_w_kat_mi:

    "Зайдя в столовую, я, как обычно, взял себе поесть и стал искать, куда куда бы усесться."

    if wnfh_Data.getChoice_points_sum("kat") >= 4:

        "Как заметил машущую мне Катю, что сидела рядом с Мику. Намёк был ясен."

    else:

        "Как заметил машущую мне Мику, что сидела рядом с Катей. Намёк был ясен."

    # тут надо поставить завтрак и подстроить под это спрайты.
    show kat normal pioneer at left
    show mi normal pioneer at right
    with dissolve

    "Подойдя к столу, я расположился напротив них."

    me "Доброе утро, Мику. И снова здравствуй, Катя."
    mi "Приветик."

    show kat smile pioneer at left with dspr

    kat "Здравствуйте, ваше величество."

    "С нескрываемой насмешкой сказала она."

    show mi upset pioneer at right with dspr

    "Мику же, словно услышав что-то пошлое, непонимающе посмотрела на Катю."

    mi "«Ваше величество»?"
    me "Давайте не будем об этом."

    "Хитро похихикав, Катя угукнула."

    show mi sad pioneer at right with dspr

    mi "Ну вот, а мне теперь любопытно!"

    show kat normal pioneer at left 
    show mi normal pioneer at right
    with dspr

    kat "Потом как-нибудь расскажу."
    me "А лучше вовсе не рассказывать."
    me "В любом случае, я, так понимаю, вам нужен, раз махали мне."

    "Девушки синхроно отрицательно покачали головой."

    show mi smile pioneer at right with dspr

    mi "Просто хотели позвать тебя к нам в музклуб после завтрака."
    mi "У меня столько планов на сегодня! А ещё есть одна идея, о которой я хочу вам поведать, но[wp]"

    show mi grin pioneer at right with dspr

    mi "Пожалуй, подержу немного интригу, хи-хи-хи."
    kat "Ну так что, согласен?"

    if wnfh_Data.FlagGet("mt_angry") == True:

        "Я покачал головой."

        me "Вы на линейке были? Я же наказан."

        show kat upset pioneer at left
        show mi sad pioneer at right
        with dspr

        "Подружки тут же упали духом."

        mi "Ну во-о-от[wp]"

        show kat happy pioneer at left with dspr

        kat "А может, ты просто сбежишь к нам?"

        "Очевидно в шутку сказала Катя."

        me "Боюсь, за такое меня будет ждать уже высшая мера наказания."

        show kat upset pioneer at left with dspr

        "Она грустно вздохнула."

        mi "Ну, может быть, в следующий раз получится?"
        me "Посмотрим."

        # Надо раскоментить когда функцию починят
        #$ wnfh_Data.addLovePoints({"kat":-1})
        #$ wnfh_Data.addLovePoints({"mi":-1})

        "Без особого энтузиазма мы доели свои порции."
        "И, распрощавшись с девочками, я покинул столовую, отправившись к складу."

        jump d9_warehouse

    else:
        
        me "Ну, дел на сегодня особо нет, так что[wp] Почему бы и нет?"

        show kat smile pioneer at left
        show mi happy pioneer at right
        with dspr

        mi "Превосходно!"

        if wnfh_Data.getChoice_result_number("d8_choice_n10") == 1:

            kat "Надеюсь, посидим так же хорошо, как вчера."
            me "Согласен."

        show mi normal pioneer at right with dspr

        mi "Ну что ж, в таком случае предлагаю прислушаться к поговорке «Когда я ем, я глух и нем»!"
        #me "Погоди-погоди, а попиздеть?"

        show kat grin pioneer at left with dspr

        kat "Поддерживаю!"

        "Я же молча согласился с девушками, и мы принялись уплетать завтрак."

        jump d9_musclub

label d9_zavtrak_w_dv_usw:

    "Тут ничего пока нет, и неизвестно как скоро появиться."
    "Дальнейший клик отправит вас в соседний лейбл, но и там тоже ничего нет."
    "Я вас предупредил!"

label d9_zavtrak_w_un:

    "Тут ничего пока нет, и неизвестно как скоро появиться."
    "Дальнейший клик отправит вас в главное меню игры."
    "Я вас предупредил!"
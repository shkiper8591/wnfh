label d9_morning:

    $ wnfh_new_chapter(3)
    $ wnfh_set_time("sunset")
    scene bg int_house_of_mt_sunset
    show unblink
    with None
    $ renpy.pause(1.0)
    play ambience ambience_int_cabin_evening fadein 2.0
    window show dissolve

    "Люблю сладкий и тихий сон."
    "Если позволяла наша биология, то только бы и спал, да наблюдал чудесные сновидения."

    if wnfh_Data.getChoice_result_number("d8_choice_n11") == 1:

        "Хотя, сегодня, мне снилась какая-то ерунда, будто я заяц косящий ту самую трын-траву на поляне."

    play sound wnfh_sfx_list["budilnik"] fadein 1.5

    "Но, разумеется, хорошее не может длиться вечно."
    "И этот проклятый будильник своим противным звоном выбил из меня весь сон."
    "Немного перевернувшись, я посмотрел на то, сколько времени на часах."

    th "Чёрт, побери, восемь утра, куда Ольга Дмитриевна так торопится?"

    play music wnfh_music_list["good_morning_1"] fadein 2.0

    "Тем временем с постели вставала и сама вожатая"

    mt "Доброе утро, Семён."
    me "Доброе[wp] А куда так рано вставать?"
    mt "Одется, умыться и пойти собирать пионеров на площадь."
    me "Зачем?"
    mt "Важное объявление. Присутствовать должны все."

    th "Ну да, конечно, как же иначе."

    "Я тяжело вздохнул. Сегодня в мои планы не входило идти куда-то с утра и слушать какие-то важные объявления."

    if wnfh_Data.FlagGet("mt_angry") == True:

        mt "Ты тем более обязан присутствовать."

        if wnfh_Data.getChoice_result_number("d8_choice_n11") == 1:

            mt "Особенно после вчерашней ночи!"

        #jump d9_morning_2

    elif wnfh_Data.getChoice_result_number("d8_choice_n11") == 1:

        mt "Бла-бла-бла"

        #jump d9_morning_2

    else:

        me "Бла-бла-бла"

        #jump d9_morning_2

    "Дальнейший клик отправит вас в главное меню"
    "Я вас предупредил!"
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

    kat "Здравствуйте, Ваше Величество."

    "С нескрываемой насмешкой сказала она."

    show mi upset pioneer at right with dspr

    "Мику же, словно услышав что-то пошлое, непонимающе посмотрела на Катю."

    mi "«Ваше Величество»?"
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

    "Зайдя в столовую, я, как обычно, взял себе поесть и стал искать, куда куда бы усесться."
    "И обнаружил взглядом Алису, которая хитро мне улыбалась и приглашающе махала."

    show dv smile pioneer at right with dissolve

    "Собственно, к ней я и сел, за не имением альтернатив."

    dv "Снова здравствуй, больной ты наш."
    me "Привет-привет."

    if wnfh_Data.FlagGet("d9_tabletochki") == True:

        dv "Ну что, помогли тебе таблетки?"
        me "А, да, спасибо тебе ещё раз."

        "Я как-то и не сразу сообразил о каких таблетках идёт речь."

        dv "Пустяки."

    "Будучи сильно голодным, я принялся сразу уплетать завтрак."

    show dv normal pioneer at right with dspr

    dv "И так[wp]"

    show dv grin pioneer at right with dspr

    dv "Какие планы на сегодня?"

    if wnfh_Data.FlagGet("mt_angry") == True:

        "Я слегка усмехнулся."

        show dv normal pioneer at right with dspr

        me "Полагаю, что отрабатывать на складе."
        me "Ты разве не слышала? Об этом же на всю округу объявили."

        "Она отрицательно покачала головой."

        if wnfh_Data.getChoice_result_number("d8_choice_n11") == 1:
            # Тут надо сделать +1 к ЛП Алисы
            dv "Я тогда была немного занята разговором с Мику."
            dv "Ну как, разговором, скорее ссорой на пониженных тонах."
            dv "Как можешь догадаться, она недовольна вчерашним поступком."

            "Я хмыкнул."

            me "Этого следовало ожидать."
            dv "Да уж[wp]"

            show dv guilty pioneer at right with dspr

            dv "Теперь меня гложит чувство стыда[wp]"

            show dv shy pioneer at right with dspr

            "Отложив столовые приборы, я положил свою руку на ладонь Алисы."

            me "Быть может я как-то могу помочь вам помириться?"
            me "В конце-концов, вы мои товарищи, и я не могу просто так стоять в стороне и наблюдать."

            "Алиса стеснительно отвела взгляд и медленно вытащила свою ладонь."

            dv "Не знаю[wp] Мы, вроде как, ненавидим друг друга."
            me "А почему?"

            show dv guilty pioneer at right with dspr

            dv "Как я говорила возле музклуба, — это личное."
            me "Прости, но тогда я и не смогу помочь не зная корней конфликта."

            show normal pioneer at right with dspr

            dv "Ты парень умный, придумаешь что-нибудь другое."

            "Тяжело вздохнув, я погрузился в поедание завтрака"

        else:

            dv "Я тогда увлечённо болтала со Славей."
            me "Интересно о чём[wp]"
            dv "Да так, о всякой всячине."
            dv "О спорте там, о его полезности для здоровья."

            if wnfh_Data.getChoice_result_number("d7_choice_n1") == 1:

                show dv grin pioneer at right with dspr
    
                dv "О том, что кое-кому непомешало бы им заняться на регулярной основе."
                dv "Хотя, у меня такое ощущение, что ты просто на кое-что загляделся."

                "Алиса ехидно захихикала, а я закатил глаза."

                me "Ой, да иди ты со своими шуточками."

                show dv laugh pioneer at right with dspr

                dv "Да ладно тебе, Семён, все мы тут взрослые."
                dv "Я бы тоже не устояла перед жопой Слави."

                "Моя подруга рассмеялась с самой себя, а я же залился красной краской."

                show dv smile pioneer at right with dspr

                "Через некоторое время, она закончила смеяться."
    
            dv "Ладно, занят так занят."

    else:

        "Я слегка задумался на этот счёт."

        me "Вроде не имеется никаких планов."

        show dv laugh pioneer at right with dspr

        "Лицо Алисы тут же расплылось в её фирменной широкой улыбке."
        "Сразу можно было заподозрить что-то не ладное."

        show dv smile pioneer at right with dspr

        dv "Не хочешь немного прогуляться?"

        if wnfh_Data.getChoice_result_number("d8_choice_n6") == 1:

            me "Опять к яблоням твоим?"
            dv "Не-е-е."

        me "А куда?"
        dv "А вот это уже сюрприз!"
        dv "Могу сразу сказать, что тебе беспокоиться не о чем."
        dv "И это не будет очередная авантюра с печальными последствиями."
        me "Да неужели?"

        "Она радостно закивала головой."

        dv "Сама в шоке."

        th "С одной стороны, она моя подруга и ничего плохого от неё в принципе не стоит ожидать."
        th "С другой стороны[wp]"

        "Я внимательно осмотрел хитрую Алису, что неотрывно наблюдала за мной и моим движениями."

        me "Хорошо, я согласен."

        "Недоверчивым голосом сказал я."

        dv "Замечательно! Тогда, вечером на площади встретимся."
        me "А я думал, что после завтрака."

        "Она грустно вздохнула."

        show dv normal pioneer at right with dspr

        dv "Я бы рада так поступить, но у меня есть некоторые дела."
        dv "И мне необходимо их решить до середины дня."
        me "Понятно."

    show usw normal pioneer at left with dissolve
    show dv surprise pioneer at right with dspr

    "В это время к нашему столу подбежала вся запыхавшаяся Ульяна."
    "Поставив поднос на стол, она изнемождёно уселась на стул и глубоко вздохнула."

    dv "Улька, ты чего, марафон бежала?"

    show dv normal pioneer at right with dspr

    usw "Да[wp] То есть нет[wp] Но почти."
    usw "Неважно в общем. А вы тут чем маетесь."
    me "Завтракаем."

    show usw normalsmile pioneer at left with dspr

    "Она хлопнула себя по лбу."

    usw "Как же я сама недогадалась."
    dv "А ты куда так спешила?"

    show usw sad pioneer at left with dspr

    "Улька тяжело вздохнула."

    usw "Долго рассказывать, но мне нужно было метнуться сначала туда, потом обратно, а затем снова туда."
    usw "И при этом ещё успеть на завтрак."

    show usw upset pioneer at left with dspr

    usw "В прочем, я сама виновата, могла ещё вчера всё сделать и бегать не пришлось бы."
    me "Так и зачем это всё?"

    show usw normalsmile pioneer at left with dspr

    usw "Чтобы зарегистрировать своё участие в футбольном матче."

    "Самодовольно она сказала и ткнула Алису в бок."
    "Алиса же что-то недовольно буркнула и продолжила есть."

    me "Звучит весело, и когда всё это дело будет?"

    show usw normal pioneer at left with dspr

    usw "Через два дня."
    usw "А завтра будет день интенсивных тренировок."

    "В это время Алиса встала из-за стола."

label d9_zavtrak_w_un:

    "Тут ничего пока нет, и неизвестно как скоро появиться."
    "Дальнейший клик отправит вас в главное меню игры."
    "Я вас предупредил!"
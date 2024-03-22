label d8_posle_obeda:

    window hide dissolve
    stop ambience fadeout 3.5
    scene bg ext_dining_hall_near_day with slide_right_blure_dissolve2
    play ambience ambience_camp_center_day fadein 3.5
    $ renpy.pause(0.5)
    window show dissolve
    
    "Выйдя на улицу, я вдохнул свежего летнего воздуха."
    "Самое то, после тесной и душной столовой, где не продохнуть от смешавшихся запахов еды и[wp] Человеческого пота, наверное?"
    "В любом случае, на этом я зацикливаться больше не хотел."
    
    th "Больше всего я хочу пойти сейчас и отдохнуть, а потом можно было бы заняться полезной деятельностью."
    th "Например[wp] Не знаю, мусор пособирать, хотя тут в лагере и так чисто."

    show ext_dining_hall_away_day with dissolve2

    "Медленной и непринуждённой походкой, я пошёл домой."

    play music wnfh_music_list["the_hill_camp_morning"] fadein 5.0

    window hide dissolve
    scene bg ext_lenin_square_day_wnfh with dissolve2
    window show dissolve

    th "Люблю время жора в лагере. Людей на улице нет, тихо и спокойно."
    th "А ещё ветерок такой приятный, обдувает со всех сторон, от чего жара совсем не чувствуется."
    th "Конечно, на солнце припекает, но не так сильно, как если бы без ветра."
    th "М-да[wp] Интересно, как там сейчас дома? Наверное, всё также сыро холодно, северная столица же."

     show bg ext_houses_day with dissolve

    "Я грустно вздохнул."

    th "Надо что-то делать с моим положением, ведь не может это вечно продолжаться."
    th "Да и рано или поздно меня поймают, и что тогда? Что я скажу? «Здрасьте, я гость из будущего»?"
    th "Меня же никто не поймёт, и в лучшем случае посмеются. В худшем[wp] В психиатрическую лечебницу отправят, наверное."

    window hide dissolve
    scene bg ext_house_of_mt_day with dissolve2
    window show dissolve

    "Вскоре, я дошёл до дома, куда подниматься сил уже не было."
    "Но, всё же кровать куда удобнее шезлонга. Так что преодолевая изнеможение, я смог забраться внутрь дома."

    stop ambience fadeout 3.5
    stop music fadeout 5.0
    scene bg int_house_of_mt_day with dissolve2
    play ambience ambience_int_cabin_day fadein 3.5

    "Вожатой, что не удивительно, внутри не было."

    th "Видимо, ещё в столовой, а значит смогу спокойно полежать."

    if wnfh_Data.FlagGet("d8_begunok") == False:

        jump d8_posle_obeda_lp_un_check

    show mt sad pioneer panama at center with dissolve

    "В это же время пришла и сама Ольга Дмитриевна."

    th "Странно, я как-то не слышал её за собой[wp] Ну да ладно, я, наверное, сильно устал просто."

    "Вид у вожатой был усталый, поэтому без особых разговоров она обошла меня и улеглась спать на кровать даже не раздеваясь."
    "Пожав плечами, я подошёл к своей кровати, переоделся и лёг отдыхать."

    window hide dissolve
    show blink
    $ renpy.pause(0.5)
    scene black
    jump d8_afternoon

label d8_posle_obeda_lp_un_check:

    if wnfh_Data.getChoice_points_sum("un") <= 5:

        jump d8_posle_obeda_mt_angry

    else:

        jump d8_posle_obeda_mt_normal

label d8_posle_obeda_mt_angry:

    "В это же время пришла и сама Ольга Дмитриевна."

    show mt angry pioneer panama at center with dspr

    "И в ту же секунду, как она завидела меня, её лицо резко изменилось на недовольное."

    mt "Ага, вот и наш герой!"
    mt "Злостный нарушитель моих поручений."
    mt "Надо же отлынить от дела."
    mt "А что я тебе говорила вчера?"

    "С каждым предложением, тон вожатой становился всё злее и злее."

    show mt rage pioneer panama at center with dspr
    # надо бы сделать анимацию мол камера пошатнулась
    mt "И ТОЛЬКО ПОПРОБУЙ СВАЛИТЬ ЗАДАНИЕ НА КОГО-НИБУДЬ ДРУГОГО!"

    "Во весь голос заорала она, да так, что небось на другом конце лагеря было слышно."
    "Ольга Дмитриевна сделала шаг в мою сторону."
    "Было ясно, дело набирает нехороший оборот и нужно бежать, вот только был один нюанс, — вожатая закрывала собой проход."

    th "Твою же мать, думай-думай, Семён, давай[wp] Как там говорится-то[wp]"

    "Пока я стоял столбом и думал что делать, вожатая успела сделать ещё один шаг ко мне и приблизиться на опасно близкую дистанцию."

    play music wnfh_music_list["estafeta"] fadein 5.0

    th "Когда закрывается одна дверь, открывается другая[wp] Например, окно!"

    "Я быстренько обернулся назад. Окно было открыто, а значит, набрав достаточно скорости можно было перелететь стол и выпрыгнуть на улицу."

    th "Главное не сломать себе что-нибудь."

    "Резко развернувшись на месте, я сорвался с места и успешно выпрыгнул в окно."

    stop ambience fadeout 0.5
    scene bg ext_after_house_wnfh with dspr
    play ambience ambience_camp_center_day fadein 0.5
    play sound sfx_bodyfall_1

    "Вылетев на улицу, я немного кубырем перевернулся по земле, но быстро поднялся на ноги и побежал вокруг дома."

    scene bg ext_house_of_mt_day 
    show mt rage pioneer panama far at center
    with dspr

    "Оббежав дом, я увидел как на крыльце стоит разъярённая вожатая[wp] {w}С молотом в руках!"

    mt "Ну-ка стой!"
    me "Сами стойте!"

    scene bg ext_houses_day with dspr

    "Я разогнался как только мог и побежал на площадь, надеясь найти там своё спасение."
    "Позади же я чётко слышал как бежала за мной вожатая. И самое что страшное, она меня уверенно так догоняла."

    th "Ну почему я не занимаюсь спортом?!"

    scene bg ext_lenin_square_day_wnfh
    show sh smile pioneer far at fright
    show sv happy pioneer glasses far at cright
    with dissolve

    "Выбежав на площадь, я увидел стоящего там Шурика со Светой."
    "Почему они были сейчас вместе, и почему Шурик был красный как помидор, меня сейчас не волновало."
    "Главное, что он был здесь и мог меня выручить из такой ситуации."

    show sh smile pioneer at fright
    show sv happy pioneer glasses at cright

    "Я подбежал к ним и попыхах протараторил."

    show sv scared pioneer glasses at cright
    show sh scared pioneer at fright
    with dspr

    me "Шурик, спасай меня!"
    mt "Я же тебя предупреждала!"

    "Донеслось очень рядом из-за спины."
    "Сил и вариантов куда бежать не оставалось."
    "Так что, из последних сил, я залез к дедушке Ленину."

    show mt angry pioneer panama at left with dissolve
    show sv angry pioneer glasses at cright
    show sh normal pioneer at fright
    with dspr
    stop music fadeout 5.0

    mt "Думаешь спрячешься от меня? Я же такое тебе устрою."

    "Тут на выручку подоспели Шурик со Светой."
    "Планшетик просто стояла в сторонке, а Шурик стал останавливать пытающуюся залезть ко мне вожатую."

    sh "Тихо, спокойно Ольга Дмитриевна, не надо тут устраивать экзекуцию пионерам."
    sh "К тому же, за такое поведение, администрация вас точно не поблагодарит."

    "После слов Шурика, вожатая остановилась, но всё ещё держала на мне свой злой взгляд."

    play music music_list["my_daily_life"] fadein 5.0
    show mt sad pioneer panama at left with dspr

    "А спустя ещё пару секунд, по всей видимости, она полностью успокоилась и положила молот на плечо."

    mt "Давай слезай, молотом бить не буду."

    show mt angry pioneer panama at left with dspr

    mt "Но разбор полётов устрою тот ещё!"

    show sv happy pioneer glasses at cright with dspr

    sv "О, а можно мне их устроить? Люблю таким заниматься."

    show mt normal pioneer panama at left with dspr

    mt "Свет, я ценю твой интузиазм, но это наше личное дело."

    show sv sad pioneer glasses at cright with dspr

    sv "Ну вот[wp]"

    "Света, чуть ли не по театральному, изобразила расстройство."

    show sv angry pioneer glasses at cright with dspr

    sv "Ну ладно, Шурик, пойдём, продолжим нашу беседу."
    sh "Я тебя спас и в благородств[wp]"

    hide sv
    hide sh
    with dissolve
    $ renpy.notify("Тут надо анимацию того, как Шурик и Света уходят вправо")
    # надо анимацию того как они уходят

    "Договорить он не успел, так как Планшетик утащила его в сторону."

    "To be continued"

label d8_posle_obeda_mt_normal:

    "placeholder"
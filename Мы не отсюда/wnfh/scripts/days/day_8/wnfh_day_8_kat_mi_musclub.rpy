label d8_kat_mi_musclub:

    stop music fadeout 5.0
    stop ambience fadeout 2.0
    scene bg ext_admin_day_wnfh with santa_barbara_in_blure_dissolve2
    play ambience ambience_camp_center_day fadein 2.0
    $ renpy.pause(0.5)
    scene bg ext_musclub_day with slide_left_blure_dissolve2
    $ renpy.pause(0.5)
    scene bg ext_musclub_verandah_day_wnfh
    show kat normal pioneer at center
    with sphere_blure_dissolve2
    play music music_list["memories_piano_outdoors"] fadein 5.0
    $ renpy.notify("МУЗЫКА МАКСИМАЛЬНО УСЛОВНАЯ, ТУТ НУЖНА БУДЕТ ДРУГАЯ, БОЛЕЕ ВЕСЁЛАЯ! А ЕЩЁ ЖЕЛАТЕЛЬНО СОБСТВЕННОГО ПРОИЗВОДСТВА (импортозамещение лол)")
    $ renpy.pause(0.5)
    window show dissolve

    "Подойдя к музклубу, мы услышали доносящуюся оттуда музыку."

    me "Похоже, Мику коротает время в ожидании тебя."
    kat "А, это Мику? Красиво играет."
    me "Ну, в конце концов она половину жизни посвятила музыке."

    show kat confused pioneer at center with dspr

    kat "Серьёзно?"
    me "По крайней мере сама так говорит."

    show kat normal pioneer at center with dspr

    kat "Надо же[wp]"

    window hide dissolve
    stop music fadeout 5.0
    stop ambience fadeout 2.0
    scene bg int_musclub_day
    show kat smile pioneer close at left
    show mi normal pioneer at right
    with slide_right_blure_dissolve2
    play ambience ambience_music_club_day fadein 2.0
    play music music_list["so_good_to_be_careless"] fadein 5.0
    $ renpy.notify("Надо бы другую музыку для музклуба в общем и Мику в частности, а то со гуд ту би керлесс заебала. Желательно собственного производства.")
    $ renpy.pause(0.3)
    window show dissolve

    "Когда мы вошли внутрь, Мику прекратила игру и перевела взгляд на нас."

    mi "Ух ты, даже вдвоём пришли! Неожиданно, а я уже думала, что про меня позабыли."
    me "Дела у нас были."

    show mi grin pioneer at right with dspr

    mi "А я знаю, что у вас дела были."

    "Мы с Катей переглянулись."

    kat "Кто-то рассказал?"

    show mi smile pioneer at right with dspr

    "Мику захихикала и махнула в сторону окна."

    mi "У меня же вон какие окна! Не трудно было заметить вас с какими-то коробками."

    show mi surprise pioneer at right with dspr

    mi "Кстати, что это были за коробки? А то я сижу тут голову ломаю, размышляя над этим, прям покоя мне не даёт."

    show kat smile pioneer close at left with dspr

    "Катя усмехнулась."

    kat "Боюсь тебя разочаровывать, но там были всего лишь лагерные документы."

    show mi upset pioneer at right with dspr

    mi "Ну, в общем-то, я так и думала."

    show mi grin pioneer at right with dspr

    mi "Хотя в душе я надеялась, что вы несёте какие-нибудь вкусняшки для празднества."
    mi "Правда, я прекрасно понимала, что вряд ли этот день празднуют у вас."

    "Я на секунду призадумался."
    "Мне не совсем было понятно, о каком празднике вообще может идти речь."

    show kat confused pioneer close at left with dspr

    kat "А что за праздник?"

    th "Похоже, я не один не в курсе."

    show mi serious pioneer at right with dspr
    stop music fadeout 5.0

    mi "Завтра ровно двадцать лет как закончилась американская оккупация Японии."
    mi "И в тот же день Япония стала членом советского блока. {w=0.5}Для нас, японцев, это воистину великий день!"
    
    show kat normal pioneer close at left with dspr

    kat "Радостный день."
    mi "Очень[wp]"

    "Я попытался переварить только что услышанную информацию."

    th "Япония — член соцблока? Да и разве оккупация не закончилась в пятидесятые?"

    "В моей голове возник конфликт историй."
    "И, видимо, из-за этого конфликта у меня знатно так разболелась голова."

    th "Вот же зараза, как не вовремя-то!"

    "Боль была адская, но я постарался сдерживать себя, а также как можно скорее переключить свои мысли на что-нибудь другое."
    "Вот только меня полностью поглотила эта мысль. Боль стала усиливаться."
    "Но я решил не подавать виду и как ни в чём не бывало прошёл дальше внутрь."

    th "Что ж, Семён, придётся потерпеть. Боль адская, но бывало и хуже, верно?"

    show mi normal pioneer at right with dspr

    mi "Ну да ладно, вы пришли сюда сыграть со мной, так ведь?"

    show kat joy pioneer at left with dspr

    kat "Именно так!"
    me "Поддерживаю[wp] Правда, я даже не помню, как на гитаре играть[wp]"

    show mi shocked pioneer at right
    show kat normal pioneer at left 
    with dspr

    mi "Ты умеешь играть на гитаре?"

    "Мику, похоже, была сильно удивлена этому факту."

    show mi dontlike pioneer at right with dspr

    mi "И за всё это время ни разу не решился зайти, чтобы сыграть?"
    me "Так я же не помню[wp]"
    mi "А мы напомним!"

    hide mi with dspr
    $ renpy.notify("Тут надо анимацию того, как Мику уходит в левую часть экрана")

    "Недовольно фыркнув, Мику быстрым шагом удалилась в подсобку."

    show kat interested pioneer at left with dspr

    kat "Правда, а почему?"
    me "Что почему?"
    kat "Ну, ты не заходил к ней. Вы же друзья."

    "Я невольно усмехнулся от такого заявления."

    me "По правде говоря, мы с Мику не более чем знакомые."
    me "Она просто дружелюбна ко всем, и я, в общем-то, тоже."
    me "Вот и получается, что со стороны это может выглядеть как дружба."

    show kat thinking pioneer at left with dspr

    kat "Понятненько[wp]"

    show kat upset pioneer at left with dspr

    "Она грустно вздохнула."

    kat "Как-то это печально выходит. Она явно хороший человек, а ты не дружишь с ней."

    "На это я только пожал плечами."

    me "Возможно."

    th "Ещё бы давалась мне эта самая дружба[wp]"

    $ renpy.notify("Тут надо анимацию того, как Мику приходит из правой части экрана")
    show mi normal pioneer at right
    show kat normal pioneer at left
    with dissolve

    "В скором времени возвратилась наша музыкантша с гитарой в одной руке и скрипкой со смычком в другой."
    "Соответственно гитару она вручила мне, а скрипку Кате."
    "Несмотря на то, что мой (да и Катин) инструмент явно долгое время лежал в подсобке, он был идеально чистым."

    th "Вот это я понимаю — уход за вещами!"

    "Мику же взяла из угла другую гитару, куда более модную и красивую."

    me "Вот значит как[wp] Нам старьё какое-то, а у тебя вон какой агрегат."

    "В шутку сказал я."

    show mi sad pioneer at right with dspr

    mi "Чего старьё-то сразу? Просто другого нет! Да и я ухаживаю за ними, протираю от пыли, струны подтягиваю[wp]"
    
    show kat serious pioneer at left with dspr

    kat "Да, Семён, она вон как старается."
    me "Дамы, что вам известно о таком понятии как Ю-М-О-Р?"

    show kat thinking pioneer at left
    show mi upset pioneer at right
    with dspr

    "Девушки быстро переглянулись между собой."

    th "М-да, шутки у меня так себе. Ну, значит, не быть мне комедиантом."

    show mi normal pioneer at right
    show kat normal pioneer at left
    with dspr

    mi "Ладно, проехали. Давайте уже играть, принимаю любые предложения!"

    show kat thinking pioneer at left with dspr

    kat "Ух[wp] Даже не знаю[wp] Может, что-нибудь спокойное?"

    show kat normal pioneer at left with dspr

    mi "Хорошо. Семён, а у тебя какие мысли?"

    "В это время я пытался поудобнее взяться за гитару."

    me "У меня одна мысль — я ничерта не помню."
    me "Последний раз я на гитаре играл, наверное, лет в пятнадцать."
    
    show mi serious pioneer at right with dspr

    mi "Давай помогу тебе."

    show mi upset pioneer at right with dspr

    "Мику сделала шаг в мою сторону, но жестом я остановил её."
 
    me "Я сам."

    show mi normal pioneer at right with dspr

    stop music fadeout 2.5

    "Взявшись как можно удобнее, я решил сыграть что-нибудь незамысловатое."

    play music wnfh_music_list["emotional_indie_guitar"] noloop fadein 2.5
    $ renpy.notify("Условная гитарка, нужно будет заменить на трек собственного производства")

    "И, к моему же удивлению, у меня что-то да получилось. Вроде даже неплохо!"

    th "Ха, а руки-то помнят!"

    "Всё моё внимание было сосредоточено на игре. Но даже так я чувствовал на себе заворожённые взгляды девушек."
    "Данный факт заставил меня немного застесняться."

    th "Как же звёзды, собирающие целые стадионы, не волнуются, что могут опозориться на огромную аудиторию?"
    th "Хотя, наверное, у звёзд уже достаточно опыта, чтобы не волноваться о таких пустяках."

    stop music fadeout 5.0

    "Вскоре я доиграл. Руки немного побаливали, особенно пальцы, хотя я даже не напрягался толком."
    
    show kat smile pioneer at left with dspr

    "И меня встретили аплодисменты, от которых даже стало тепло на душе."

    me "Ещё никто не аплодировал моей плохой игре на гитаре."
    kat "Плохой? Ты очень даже хорошо сыграл."
    mi "Ага! Так даже и не скажешь, что ты позабыл это дело."

    show mi dontlike pioneer at right
    show kat serious pioneer at left
    with dspr

    mi "Может ты нас обманывал, чтобы ничего не делать, и при этом просто так послушать музыку?"
    kat "Да!"

    "Звонко поддержала Катя свою подругу."

    me "Чего? Делать мне, по-вашему, больше нечего?"

    show mi grin pioneer at right
    show kat smile pioneer at left
    with dspr

    mi "Эх, Семён, что тебе известно о таком понятии как Ю-М-О-Р?"

    "Неожиданно мне отплатили той же монетой."

    me "Умно, умно, ничего не скажешь."
    kat "Что ж, а теперь давайте все вместе попробуем!"

    $ renpy.notify("Тут надобно вставить арт, а пока опирайтесь на текстовое описание")
    window hide dissolve
    stop ambience fadeout 2.0
    scene black with dissolve
    window show dissolve
    play music wnfh_music_list["friends_of_the_deceased_moon"] fadein 3.0

    "А потом мы играли и играли, даже пели песни."
    "Я и знать не знал, что у меня столько задора на исполнение музыки."
    $ renpy.notify("Тут стоит проверка ЛП. Там довольно условные числа, которые нужно будет скорректировать исходя из баланса.")

    if wnfh_Data.getChoice_points_sum("kat") >= 4:
        show cg d8_me_dance_musclub_w_kat
        "Даже с Катей потанцевал по её инициативе. {w=0.5}Хотя танцор из меня такой себе, и мои движения больше походили на пьяную пляску."

    elif wnfh_Data.getChoice_points_sum("mi") >= 4:
        show cg d8_me_dance_musclub_w_mi
        "Ещё я немного потанцевал с Мику. {w=0.5}Впрочем, мне было о-о-очень далеко до Мику и грации её движений."

    else:
        show cg d8_me_dance_musclub_alone
        "Я даже немного потанцевал под музыку. {w=0.5}Правда, танцем это было сложно назвать, но меня никто и не учил танцевать!"


    "Время пролетело незаметно."
    "Сначала десять минут, потом двадцать, и вот мы не заметили, как прошёл уже целый час."
    "За это время мы сильно вымотались, и Мику предложила по чашечке чая. Отказаться от такого было невозможно."

    window hide dissolve
    $ renpy.pause(0.2)
    stop music fadeout 2.0
    play ambience ambience_music_club_day fadein 2.0
    scene bg int_musclub_day
    show mi normal pioneer at right
    show kat smile pioneer at left
    with dissolve
    $ renpy.pause(0.2)
    window show dissolve

    "Мику расстелила посреди помещения плед, на котором мы с Катей расположились в ожидании чая."
    "Кажется, здесь были все удобства: электрочайник (очевидно, японский), чашки, чаи разных сортов и куча заморских сладостей."
    "Вскоре чайник вскипел, и наша хозяюшка вернулась с подносом, который поставила посреди пледа."

    mi "Вот, угощайтесь."

    show mi upset pioneer at right with dspr

    mi "Я только не знаю, кто с сахаром пьёт, кто нет, да и вроде конфеты сладкие, но на всякий случай, если что, сахар тут."

    show mi serious pioneer at right with dspr

    "Она указала не небольшую фарфоровую вазу."

    show kat joy pioneer at left with dspr

    kat "Вкусно!"

    "Сказала Катя, уже потягивая чай."

    show mi happy pioneer at right with dspr

    mi "На здоровье!"

    "Я же замешал в чай четыре ложки сахара."

    show mi shocked pioneer at right with dspr

    mi "Семён, куда ты столько сыпешь?!"
    me "Люблю сладкий чай."
    mi "Кошма-а-ар[wp]"

    "Так мы чаёвничали на протяжении минут десяти или пятнадцати."
    "Мику подливала нам чай, угощала сладостями и рассказывала всякие интересности."
    "Ну, интересно это было Кате. {w=0.5}Меня же как-то не особо интересовало, как устроены гитарные струны и какой там состав в японском шампуне."
    "А посему я просто сидел и пил чай, раздумывая о всяком."
    "И под всяким я подразумеваю смысл своего пребывания здесь."

    th "Уже который раз я задумываюсь: что если я просто уйду? Будут ли меня искать?"
    th "Или, может, просто ликвидируют, как только я перейду за условную черту?"

    if wnfh_Data.getChoice_result_number("d8_choice_n6") == 1:

        th "Тем более после того, как мы с Алисой видели тех людей в химзащите[wp]"
        
        if wnfh_Data.getChoice_result_number("d8_choice_n8") == 1:

            th "И тем более после того, как стало ясно, что это военные[wp] {w=0.5}Интересно, что они тут искали?"

    th "Да и даже если ничего со мной не случится, куда я пойду-то?"
    th "Получается, только и остаётся мне сидеть на попе ровно и надеяться на чудо[wp]"

    kat "[wp]Семён, вот скажи, кто появился раньше: единороги или драконы?"

    "Несколько секунд я с серьёзным видом размышлял над этим вопросом, пока не задумался над его абсурдностью."

    me "Чё?"

    show kat laugh pioneer at left
    show mi laugh pioneer at right
    with dspr

    "Девушки моментом засмеялись."

    show mi normal pioneer at right with dspr

    kat "Да ничего, просто ты какой-то[wp]"

    show kat thinking pioneer at left
    show mi serious pioneer at right
    with dspr

    kat "Загадочный, наверное?"
    kat "Сидишь, смотришь в одну точку, бубнишь что-то себе под нос[wp]"
    kat "И на друзей не реагируешь."

    show mi grin pioneer at right with dspr

    mi "Разве что на вот такие глупые вопросы реагируешь!"

    show kat smile pioneer at left with dspr

    kat "Это точно."

    "Я почесал затылок."

    th "Сколько раз самому себе говорил не увлекаться подобными мыслями? Каждый раз плохо заканчивается."

    show kat normal pioneer at left
    show mi normal pioneer at right
    with dspr
    show dv normal pioneer2 far at center with dissolve

    "В это время в дверь постучали, и к нам вошла Алиса."

    dv "Привет-привет, товарищи музыканты."
    mi "Приветик!"

    if wnfh_Data.FlagGet("d7_kat_oblivanie") == "dv_oblila":

        show kat pockerface pioneer at left with dspr

        "Катя же не поздоровалась с Алисой, лишь мельком глянув на неё."

    else:

        kat "Здравствуй."

    dv "Так-с, мне нужно украсть у вас Семёна на пару слов."
    mi "Хорошо, мы тут всё равно пока что ничего не делаем."

    hide dv with dspr

    "Алиса поманила меня пальцем за собой и вышла на улицу."

    th "Ох, блин[wp] Надеюсь, меня не ждёт очередной план ограбления Монте-Карло."

    "Встав, я последовал на улицу."

    window hide dissolve
    stop ambience fadeout 2.0
    scene bg ext_musclub_verandah_day_wnfh
    show dv smile pioneer2 at center
    with dissolve2 
    play ambience ambience_camp_center_day fadein 2.0
    $ renpy.pause(0.3)
    window show dissolve

    me "Что такое?"
    dv "Мне нужно, чтобы ты достал две гитары."

    "Прямолинейность Алисы настолько меня поразила, что я первые пару секунд даже не знал, как ответить."

    me "Что, прям вот так сразу?"

    show dv grin pioneer2 at center with dspr

    dv "Ах да, чуть не забыла. Хочешь сходить сегодня вечером на сцену поиграть?"

    if wnfh_Data.getChoice_result_number("d7_choice_n8") == 2:

        dv "Между прочим, сам просил тебя спросить завтра. Ну, то есть, уже сегодня, хех."

    show dv normal pioneer2 at center with dspr

    dv "Ну так что?"

    window hide dissolve
    call screen wnfh_choice(
        ["dv", "А давай!", "Я как раз вспомнил, как играть", "d8_me_dv_yes_near_musclub", {"dv":1}],
        ["neutral", "О, нет-нет-нет!", "Это точно закончится проблемами для меня", "d8_me_dv_no_near_musclub", {"dv":-1}],
        ["d8_choice_n11", "Алиса зовёт Семёна на сцену"]
        ) with sphere_blure_dissolve2

label d8_me_dv_yes_near_musclub:

    if wnfh_Data.FlagGet("mt_angry") == True:

        $ wnfh_Data.FlagSet("double_nakazanie") == True

    me "Всё равно вечером делать будет нечего."
    me "Поэтому, думаю, можно немного дать року."

    show dv laugh pioneer2 at center with dspr

    dv "Вот это по-нашему!"

    show dv smile pioneer2 at center with dspr

    dv "Что же, тогда организуй пару гитар нам."
    me "А почему я?"

    show dv normal pioneer2 at center with dspr

    "Она медленно оглядела меня с ног до головы."

    show dv shy pioneer2 at center with dspr

    dv "У тебя уже налажены связи."

    "Сказала она, уводя взгляд куда-то в сторону."
    "Тут и ежу было понятно, что у неё есть какая-то причина не делать этого лично."

    me "У тебя что-то случилось?"
    dv "Ну[wp]"

    show dv sad pioneer2 at center with dspr

    dv "С Мику поссорились немного."

    "Меня эта весть шокировала."

    th "Да чтобы Мику поссорилась с кем-то? Неужели скоро град пойдёт?"

    me "Странно, она тебя, вроде как, по-дружески встретила."

    show dv guilty pioneer2 at center with dspr

    dv "Она — человек добрый, но обиды держать умеет, поверь мне."
    me "Не верю."
    dv "Да я тоже не верила, пока сама не столкнулась."
    me "А как так у вас вышло?"
    dv "Это личное."

    show dv normal pioneer2 at center with dspr

    "Алиса прошла пару шагов вперёд."

    dv "В общем, пожалуйста, договорись, а с меня зачтётся."
    me "Да? И как же?"

    show dv smile pioneer2 at center with dspr
    $ renpy.pause(0.2)
    hide dv with dspr

    "Ничего не ответив, только сверкнув улыбкой на прощание, Алиса удалилась вглубь лагеря."

    th "Что ж, ладно, это было странно[wp]"

    jump d8_kat_mi_musclub_continue

label d8_me_dv_no_near_musclub:

    me "Ты уж прости, но у меня другие дела будут вечером."

    show dv sad pioneer2 at center with dspr

    dv "Блин, ну вот[wp]"

    show dv guilty pioneer2 at center with dspr

    dv "А от этих дел никак нельзя отвертеться?"
    me "Боюсь, за такое мне отвертят голову."

    show dv sad pioneer2 at center with dspr

    dv "Понятно[wp]"

    "Она глубоко вздохнула."

    show dv normal pioneer2 at center with dspr

    dv "Ну ладно, дела так дела, счастливо тебе."

    hide dv with dissolve

    "Алиса потрепыхала мне волосы и медленным шагом удалилась вглубь лагеря."

    me "А причёску портить было лишним."

    "Пробубнил я себе под нос."

label d8_kat_mi_musclub_continue:

    window hide dissolve
    stop ambience fadeout 2.0
    scene bg int_musclub_day
    show mi surprise pioneer far at right
    show kat surprise pioneer far at left
    with dissolve2
    play ambience ambience_int_cabin_day fadein 2.0

    "Как только я зашёл обратно внутрь, от двери врассыпную разбежались Мику и Катя."
    "Они остановились в дальней части комнаты и смотрели на меня ошарашенным взглядом."
    "Я же смотрел на них с кривой ухмылкой."

    me "Подслушивали, значит?"

    show kat smile pioneer far at left with dspr

    kat "Мы? Да ни в коем случае! Правда, Мику?"

    show mi shy pioneer far at right
    show kat guilty pioneer far at left
    with dspr

    mi "Ну, вообще чуть-чуть подслушали, интересно просто стало, что Алисе могло потребоваться от тебя."

    "Обломала Мику Катю своей честностью."

    show mi angry pioneer far at right with dspr

    if wnfh_Data.getChoice_result_number("d8_choice_n11") == 1:
       
        mi "И гитары я не дам, даже тебе в руки. Уж прости, Семён."

    else:

        mi "Кстати, правильно сделал, что отказался идти с ней на сцену! Она такая[wp] Такая[wp] Плохая, в общем!"

    show mi angry pioneer at right
    show kat normal pioneer at left
    with dspr

    "Я прошёл дальше внутрь и уселся обратно на плед."
    "Девушки же, секунду погодя, также подошли и сели рядом."

    me "Что такого случилось между вами?"
    kat "Да, кстати, почему вы в обиде?"

    if wnfh_Data.FlagGet("d7_kat_oblivanie") == "dv_oblila":

        kat "Конечно, Алиса и со мной некрасиво поступила, облив на входе, но даже я так не обижаюсь." 

    show mi serious pioneer at right with dspr

    mi "Сами спросите у неё, я даже говорить об этом не хочу."

    "Мы с Катей переглянулись."
    
    th "Как бы то ни было, а если даже Мику обиделась, значит это что-то серьёзное."
    th "И есть у меня ощущение, что во всём этом виновата сама Алиса."
    th "С другой стороны, она бы не стала так просто ссориться с человеком-синонимом к слову «доброта»."

    show kat thinking pioneer at left with dspr

    kat "Ну, раз не хочешь, не будем выпытывать."
    me "Да, по себе знаю, как неприятно от такого."

    show mi shy pioneer at right with dspr

    mi "Спасибо вам, ребята."

    "Мику быстренько оглянулась на часы."

    show mi shocked pioneer at right with dspr

    mi "Вот это да, уже ужин скоро!"

    show mi smile pioneer at right with dspr

    mi "Действительно время быстро течёт, когда сидишь с товарищами!"

    show mi sad pioneer at right with dspr

    mi "Жаль только то, что нам нужно сворачиваться[wp]"

    show kat sad pioneer at left with dspr

    kat "И не поспоришь."

    "Катя грустно вздохнула."

    kat "А я хотела бы ещё сыграть[wp]"

    show mi normal pioneer at right with dspr

    mi "Завтра можно."

    show mi laugh pioneer at right with dspr

    mi "Ну, или ночью!"

    show mi upset pioneer at right with dspr

    mi "Только тогда, скорее всего, мы всему лагерю спать не дадим, и потом Ольга Дмитриевна мне такое устроит[wp]"

    show mi normal pioneer at right with dspr

    mi "Ну, вы идите, я тут быстренько приберусь и догоню вас!"

    "Синхронно угукнув, мы с Катей отправились на выход."

    jump d8_evening
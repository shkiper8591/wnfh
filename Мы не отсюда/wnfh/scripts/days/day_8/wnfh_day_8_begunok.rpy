label d8_begunok:

    window hide dissolve
    hide mid d8_breakfast_empty with dissolve
    $ renpy.pause(1.0)
    stop ambience fadeout 2.5
    
    scene bg ext_dining_hall_near_day with slide_right_blure_dissolve2
    play ambience ambience_camp_center_evening fadein 3
    play music music_list["dance_of_fireflies"] fadein 5
    $ renpy.pause(1.0)
    window show

    if wnfh_Data.getChoice_result_number("d8_choice_n2") == 1:

        jump d8_begunok_w_mi

    elif wnfh_Data.getChoice_result_number("d8_choice_n3") == 1:

        jump d8_begunok_w_un

    else:

        jump d8_begunok_canon

label d8_begunok_w_mi:
    
    $ wnfh_set_time()
    show kat thinking pioneer at right
    show mi normal pioneer at left
    with dissolve

    "Выйдя с Мику из столовой, мы обнаружили одиноко сидящую Катю, которая грустно уставилась в пол."

    me "А вот и я, вернее, мы."
    kat "Мы?"
    
    "Катя озадаченно повернулась на нас."
    
    show mi happy pioneer at left with dspr

    mi "Да, я с вами за компанию прогуляюсь, благо, никто не запрещает так делать, заодно лучше познакомимся, я вот Мику Хатсунова."
    kat "Катя Та[wp]"
    
    "Тихо начала проговаривать она, но Мику перебила её."
    
    show mi grin pioneer at left with dspr

    mi "Занимаюсь здесь, в лагере то есть, музыкой, которую просто обожаю, думаю, что это дело всей моей жизни, ведь это так прекрасно! Звучание нот, что разносится по муз кружку[wp]"
    me "Ладно, Мику, думаю, тебе стоит придержать слова, чтобы было о чём поболтать во время заполнение листа."
    
    show kat interested pioneer at right with dspr

    "Катя встала с лавочки и подошла поближе к нам."
    
    kat "Что ж, с чего тогда нам лучше начать?"
    me "Ну, зависит от того, какие позиции нам нужно посетить."
    
    "Она достала аккуратно сложенный листок и, развернув его, стала рассматривать."
    
    kat "Музыкальный кружок, клуб авиамоделирования, медпункт и библиотека[wp]"

    show mi smile pioneer at left with dspr

    mi "О, муз кружок есть, здорово! А то его не всегда дают пионерам, по итогу я всё ещё одна единственная в нём состою[wp]"

    show kat happy pioneer at right with dspr

    kat "Вот как[wp] Ну, мне музыка тоже нравится, так что может и будет пополнение у тебя."

    show mi laugh pioneer at left
    show kat confused pioneer at right
    with dspr

    mi "Здорово-здорово-здорово!"
    
    "Такие новости явно очень обрадовали Мику, что она аж запрыгала и захлопала в ладоши."
    
    me "Та-а-к[wp] Хорошо, давайте тогда начнём издалека, и пойдём к муз кружку и клубам, чтобы по лагерю туда сюда не бегать."
    
    show mi grin pioneer at left with dspr

    mi "Согласна, а посему пойдёмте сразу ко мне, всё покажу и расскажу как у меня классно!"
    
    "Мику схватила удивлённую этому Катю под локоть, и повела в сторону муз клуба."
    
    # Тут надо бы анимацию того как Катя и Мику быстро уходят за правый край экрана 

    th "Да уж, с ней точно не заскучаем[wp]"
    
    "Постояв пару секунд и пронаблюдав за этой забавной картиной, я пошёл за ними."
    
    stop music fadeout 3.5
    window hide dissolve
    scene bg ext_lenin_square_day_wnfh
    show kat normal pioneer at right
    show mi normal pioneer at left
    with dissolve2
    window show dissolve
    play music music_list["get_to_know_me_better"] fadein 3.5
    
    "Быстренько догнав их, я просто молча шёл за ними, слушая рассказы Мику о своём кружке."
    
    mi "[wp]А ещё, у нас там полно разного реквизита! Правда, собран он в тесной подсобке, в которой чёрт ногу сломит, но да неважно! Важно что его много!"
    kat "И что там за реквизит?"
    mi "Самый разный! От пиратов, до космонавтов. В прошлом году вот выступали пираты. Даже сцену тематически оформили!"
    kat "Выступали? То есть ты была не одна?"
    mi "Нет, тогда в этом согласилась участвовать Алиса и Ульяна. Хоть последняя не очень хотела участвовать, но всё же согласилась. Ну и басиста нам тогда найти не удалось, так что вышло не идеально, но людям всё равно понравилось!"
    
    th "У меня сейчас голова лопнет всё это слушать, когда мы уже дойдём там?"
    
    "Я быстренько глянул вперёд и ужаснулся, что идти ещё как минимум несколько минут."
    
    th "Казалось бы, несколько минут, не так уж и много."
    th "Но когда Мику прорывает на поговорить, голову забивает бесконечный поток мыслей, которые ещё не всегда связаны между собой."
    th "Однако, стоит отметить, что сам голос у неё приятный на слух."
    th "Вот нужно только решить ей проблему эту с невозможностью остановить свой поток слов."
    th "Вообще, очевидно, на это есть объективные причины, почему она так себя ведёт[wp] Только я их не знаю[wp] В прочем, всё равно как-то."

    show bg ext_musclub_day with dissolve2
    
    "Спустя ещё пару минут невыносимой болтовни, мы наконец-то дошли до муз клуба."
    
    mi "А вот и оно! Главное сердце музыки в этом месте."
    kat "Ха, выглядит очень уютно."
    mi "О, это ты ещё внутри не была!"
    
    "Мику отпустила попутчицу и радостно попрыгала к дверям музклуба."
    
    hide mi with dissolve

    me "Ну что, не утомила она тебя своими разговорами?"
    
    show kat joy pioneer at right with dspr

    "Спросил я, подойдя к Кате."
    
    kat "Ни сколько."
    me "Удивительно[wp]"
    mi "Чего вы там стоите, идёмте!"
    
    "Крикнула нам музыкантка и убежала внутрь муз клуба."
    
    me "Давай, идём."
    
    stop music fadeout 4.5
    stop ambience fadeout 3.0
    window hide dissolve
    scene bg int_musclub_day
    show kat normal pioneer at left
    show mi normal pioneer at right
    with dissolve2
    window show dissolve
    play ambience ambience_music_club_day fadein 3.0
    play music music_list["so_good_to_be_careless"] fadein 4.5
    
    mi "Милости прошу, мой дом!"

    show kat smile2 pioneer at left with dspr

    kat "В-а-а-у[wp]"
    
    "Удивлённо протянула Катя, разглядывая музыкальные инструменты в дальней части помещения."
    "И в целом её можно было понять, ведь наблюдение за красиво блестящими на свету инструментами, к которым ещё и бережно относятся, вызывает удивление."
    "Хотя, учитывая какая бережливая Мику насчёт музыкальных инструментов, то нет, не вызывает удивления."
    
    show mi grin pioneer at right with dspr

    mi "И это только малая часть нашего ассортимента! Просто это те инструменты, на которых я чаще всего играю."
    mi "Но ещё у меня есть, укулеле, тромбон, саксофон, контрабас, разного рода электрогитары, басс-гитары[wp]"
    
    # Тут надо бы какой-нибудь таймскип а-ля из спанчбоба "Некоторое время спустя"
    
    show mi happy pioneer at right with dspr

    mi "[wp]Мой личный Сямисэн, разные флейты и парочка скрипок."
    
    show kat interested at left with dspr

    "Когда Мику упомянула скрипки, «слегка» утомившаяся Катя резко приободрилась."
    
    kat "Скрипки говоришь?"

    show mi surprise pioneer at right with dspr

    mi "Ага, одна поломанная немного, а другая совершенно целая."

    show kat grin pioneer at left with dspr

    kat "Знаешь, а я ведь умею играть на скрипке[wp]"
    
    show mi surprise pioneer at right with dspr

    mi "П-Правда?"

    show mi shy pioneer at right with dspr

    mi "А сыграешь сейчас?"

    show kat happy pioneer at left with dspr

    kat "Да, почему бы и н[wp]"
    me "Кхм."
    
    "Вмешался я в их милый диалог."

    show mi sad pioneer at right
    show kat normal pioneer at left
    with dspr
    
    me "Это конечно всё очень хорошо, но, Катя, обходный лист нужно вообще-то в срок сдать."
    kat "Оу, точно, я совсем забыла про него[wp]"

    show mi normal pioneer at right with dspr

    mi "Давай, я распишусь, что ты у меня была."
    
    "Катя отдала лист музыкантке и та ускакала к подоконнику подписывать его."
    
    show mi serious pioneer at right with dspr

    mi "Кстати, не хочешь ко мне вступить? Будем вместе музыку сочинять, играть и пить чай с конфетами."

    show kat smile pioneer at left with dspr

    kat "Ты знаешь, а давай!"
    mi "Отлично[wp]"
    
    # надо сделать анимацию того как мику отходит в сторону потом возвращается

    "Мику с особым усердием поставила подписи в обходном листе и, прибежав обратно к нам, вернула его Кате."
    
    show kat normal pioneer at left with dspr

    me "Так, теперь клубы"
    me "Вернее, клуб[wp]"

    show mi smile pioneer at right with dspr

    mi "О, давно хотела заглянуть к вам, но боялась потревожить, у вы же постоянно что-то делаете там у себя, если судить по доносящимся звукам активной работы."
    me "Да, мы постоянно чем-то заняты, но навещать нас можно, не сильно потревожит."
    me "Это вот плотники не любят когда их тревожат, сразу агрессия начинается."
    
    show mi happy pioneer at right with dspr

    mi "Хорошо, я это тогда запомню!"
    me "Ну что ж, на выход получается[wp]"

    window hide dissolve
    stop music fadeout 4.5
    stop ambience fadeout 3.0
    scene bg ext_musclub_verandah_day_wnfh
    show kat normal pioneer at left
    show mi normal pioneer at right
    with dissolve2
    play ambience ambience_camp_center_day fadein 3.0
    window show dissolve
    # хз какую тут музыку поставить, так что пооооооооох

    "Выйдя из музклуба, Мику быстренько заперла за нами дверь."

    show kat confused pioneer at left with dspr
    
    kat "Ух ты, у вас ещё и плотники тут есть?"
    me "Да, напротив нашего клуба авиамоделирования, Стас и Сергей."
    me "Странные ребята, если честно[wp]"

    show mi upset pioneer at right with dspr

    mi "По правде говоря, впервые слышу вообще о них."
    me "Ну, неудивительно, они же из другого отряда, и почти безвылазно сидят у себя."

    show bg ext_clubs_day with dissolve2

    "Быстренько сократив через пролесок, мы вышли к зданию клуба."

    # надо потом доделать это всё, щас лень

    stop ambience fadeout 3.5
    scene bg int_clubs_male_day
    show el normal pioneer at fleft
    show sh normal at cleft
    show kat normal pioneer at cright
    show mi normal pioneer at fright
    with dissolve2
    play ambience ambience_clubs_inside_day fadein 3.5

    "Зайдя внутрь, тут уже были Сергей и Шурик, которые что-то подкручивали на корпусе самолёта"

    me "Привет парни, чё как тут у вас?"
    sh "Да так, фигнёй маемся пока деталей не хватает."
    
    "Шурик оторвался от стола и перевёл свой взгляд на нас."
    
    show sh surprise pioneer at cleft with dspr

    sh "Ого, да ты не один я гляжу, а с целой делегацией[wp]"
    
    show mi grin pioneer at fright with dspr

    mi "Да, я тут к Семёну и Кате заделалась в компаньоны, чтобы им скучно не было, пока бегунок заполняют."
    
    show sh normal at cleft with dspr

    sh "Да я уж понял."
    
    "Тем временем Сергей вообще не обращал на нас никакого внимания, и увлечённо что-то крутил отвёрткой."
    "За это Шурик дал ему легкий подзатыльник."
    
    sh "Серый, у нас гости, поприветствуй хотя бы."
    
    show el smile pioneer at fleft with dspr

    el "А, что? Ой. Здарова Семён, привет Мику и здравствуй э-э[wp]"
    
    show el surprise pioneer at fleft with dspr

    "Глядя на Катю, Сергей сильно задумался."
    
    show kat interested pioneer at cright with dspr

    kat "Катя."

    show el laugh pioneer at fleft with dspr

    el "Катя! Приятно познакомиться, я Серый."

    show kat grin pioneer at cright with dspr

    kat "А я розовая!"
    
    "Хихикая ответила Катя."
    
    show mi grin pioneer at fright with dspr

    mi "А я, аквамаринованая!"
    
    "Также хихикая сказала Мику."
    
    me "Мику, правильно аквамариновая."

    show mi shy pioneer at fright with dspr

    mi "Ой[wp]"
    
    show kat laugh pioneer at cright
    show mi laugh pioneer at fright
    show sh laugh at cleft
    with dspr

    "Секунду спустя, все присутствующие в помещении, включая Мику, посмеялись с такой нелепой ошибки, после чего продолжили общение."
    
    show kat normal pioneer at cright
    show mi normal pioneer at fright
    show sh normal at cleft
    show el normal pioneer fleft
    with dspr

    kat "Мне тоже приятно познакомиться."
    
    "Сказала она и протянула руку Сергею, которую он и пожал, после чего протянула Шурику."
    
    sh "Шурик."
    
    "Произнёс он и легонько пожал руку."
    
    me "Что ж, вот вы и познакомились, прекрасно."
    me "Но, времени у нас, к сожалению, в обрез, так что, Шурик."
    sh "Да-да?"
    me "Будь так добр, подпиши нашей новенькой бегунок."
    
    "После моих слов, Катя протянула этот самый листок."
    
    sh "Хорошо-хорошо[wp]"
    
    "Взяв листок, Шурик отошёл в дальнюю часть помещения."

    show mi upset pioneer at fright with dspr
    
    mi "Ребята, а вот помимо самолёта, чем вы ещё занимаетесь?"

    show el grin pioneer at fleft with dspr

    el "Компьютеры ломаем."
    sh "Буквально."
    
    show mi serious pioneer at fright with dspr

    "Мику оглядела кусок платы подсоединённый к монитору."
    
    mi "И-и-и, зачем?"
    
    show sh upset at cleft
    show el surprise pioneer at fleft
    with dspr

    "Этот вопрос ввёл в ступор парней."
    "Они отвлеклись от своих дел, переглянулись между собой и глядя на Мику пожали плечами, после чего каждый вернулся к своим делам."
    
    show el normal pioneer at fleft
    show sh normal at cleft
    with dspr

    th "Интересно, чего там Шурик так долго? Опять что ли ручку потерял? Постоянно же ей пользуется, и постоянно её теряет."
    
    show kat thinking pioneer at cright with dspr

    kat "Ну а если серьёзно, то зачем? Так просто переводите ещё работоспособные вещи."

    "В это время к нам вернулся Шурик, и вручая бегунок Кате, поправляя очки, сказал."
    
    show sh normal_smile at cleft with dspr

    sh "Наверное стоит разъяснить, что мы не ломаем ещё дееспособные платы, а добиваем уже то, что изжило себя и со дня на день сгорит."
    kat "А, вот оно что[wp] Резонно[wp]"

    show sh normal at cleft with dspr

    sh "Вот и мы так думаем. Ладно, не буду вас более задерживать."
    
    hide kat
    hide mi
    with dissolve
    # тут надо бы звук открытия двери мб

    "Девушки вышли первыми из здания, я же немного задержался."

    me "Че, я сильно нужен буду сегодня?"
    sh "Не знаю, по обстоятельствам смотреть будем."
    me "Ладно, тогда увидимся когда увидимся."

    stop ambience fadeout 3.5
    scene bg ext_clubs_day
    show kat normal pioneer at left
    show mi normal pioneer at right
    with dissolve2
    play ambience ambience_camp_center_day fadein 3.5

    me "Ну что ж, теперь в медпункт."
    mi "Ой, не люблю посещать медпункты, да и больницы в целом."
    
    show kat confused pioneer at left with dspr

    kat "Хм? Почему?"

    show mi sad pioneer at right with dspr

    mi "Не люблю запах лекарст, очень тошнить начинает от него."

    show kat upset pioneer at left with dspr

    kat "Да уж, тут не поспорить, аромат лекарств не самый приятный."
    
    show mi upset pioneer at right with dspr

    mi "Да, поэтому я вас снаружи подожду, ладно? В конце-концов, я же просто ваша, так сказать, попутчица, и мне не обязательно заходить с вами, и[wp]"
    
    show mi normal pioneer at right
    show kat normal pioneer at left
    with dspr

    me "Да, хорошо, Мику, можешь подождать нас снаружи."
    mi "Отлично."
    
    window hide dissolve
    scene bg ext_aidpost_day 
    show kat normal pioneer at center
    with dissolve2
    window show dissolve

    "Придя к медпункту, Мику осталась немного поодаль от здания, а я с Катей подошли, собственно, к главному входу и постучались."
    
    cs "Входите!"
    
    "Громко раздалось изнутри и мы вошли внутрь."
    
    stop ambience fadeout 3.5
    scene bg int_aidpost_day
    show kat normal pioneer at left
    show cs normal glasses far at right 
    play ambience ambience_medstation_inside_day fadein 3.5
    play music music_list["eternal_longing"] fadein 4.5

    "Внутри медпункта, как не неожиданно, сидела наша медсестра."
    th "Хотя, в её отношении, справедливо медтётя какая-нибудь, ей же явно за тридцатник, ну или около того."
    
    cs "Так-так-так, что мы имеем. Семён, один из главных любителей встрять в неприятности."
    
    "Говорила она указывая на меня ручкой."
    
    cs "И неизвестная мне девушка[wp]"

    "Сказала она указав ручкой уже на Катю."

    cs "У тебя, Семён, во взгляде читается некая[wp] Подавленность."
    cs "В то время как у девушки радостный взгляд[wp]"
    cs "Складываем два и два[wp]"
    
    th "Только бы обошлось без пошлостей. Я не хочу сегодня краснеть перед кем либо."
    
    if wnfh_Data.FlagGet("d7_kat_oblil_me") == True:
    
        th "Тем более, после того как облил её, это же вообще будет полное добивание меня."
    
    show cs normal glasses at right with dspr

    "Виола медленно встала со стула и подошла к нам."    

    cs "Вы пришли заполнить обходной лист."
    kat "Да, именно так."
    
    "Я демонстративно утёр пот со лба."
    
    cs "Семён, ты какой-то сам не свой, случилось что-то? Может приболел?"
    me "Нет-нет, всё в порядке."
    cs "Ну-ну, если что, в этом помещении тебя за один день на ноги поставят."
    
    "В это время Катя протянула руки с листом нашей медсестре."
    
    show kat smile pioneer at left with dspr

    kat "Здравствуйте, я новенькая здесь, меня зовут Катя!"
    cs "Очень приятно, я Виолетта, но лучше зови меня и Виола, так даже благозвучнее."
    cs "Что ж, как я уже говорила, это то место, где всё вылечат в максимально короткие сроки."
    
    show kat grin pioneer at left with dspr

    kat "Что, даже перелом какой-нибудь?"

    show cs smile glasses at right with dspr

    "Виола усмехнулась с такого вопроса."

    cs "Даже перелом[wp] {w}В травмпункте города Гравипадово."

    show kat smile2 pioneer at left with dspr

    kat "Ха, а говорите всё лечат у вас!"
    cs "Ну, я медсестра, а не волшебница в конце концов."
    cs "Ладненько, не буду вас долго задерживать."

    "Взяв лист, который Катя всё ещё тянула медсестре, Виола прямо на месте поставила подпись и вернула его обратно."

    cs "Всё, можете шагать спокойно, пионеры."
    kat "Спасибо, до свидания!"

    "На прощание Виола подмигнула нам и вернулась на своё место."

    stop music fadeout 4.5
    stop ambience fadeout 3.5
    scene bg ext_aidpost_day
    show kat normal pioneer at left
    with dissolve2
    play ambience ambience_camp_center_day fadein 3.5

    "Мы вышли на улицу, однако, нигде рядом не обнаружили нашу попутчицу."

    me "Дела[wp]"

    show kat interested at left with dspr

    kat "По делам ушла наверное."

    "И только мы сделали шаг, как я заметил, что вдалеке кто-то сидит за деревом."
    "Вероятнее всего, это и была наша Мику."

    me "Наверное, там она."

    "Сказал я указав в сторону дерева."

    show kat thinking at left with dspr

    kat "Хм, возможно."

    "Тихонько подойдя поближе, мы увидели Мику, которая радостно, словно мелкое дитё, легонько тыкала палкой муравейник."
    "И наблюдение за реакцией муравьёв на столь вопиющее нападение, её очень даже забавляло."

    th "Бедные создания, ну ничего, сейчас мы вас спасём от этого изверга!"

    me "Кхм, Мику, мы всё."

    "Мику немного испугалась и дёрнулась."

    show mi shy pioneer at right with dspr

    mi "Ой, напугал."

    show kat grin pioneer at left with dspr

    kat "Что, мурашей мучаешь?"

    show mi normal pioneer at right with dspr

    mi "Ну[wp] Так, самую малость, особо не мешая им при этом."

    show kat smile pioneer at left with dspr

    kat "Так, что нам осталось ещё?"
    me "Получается, только библиотека и всё."
    kat "Хорошо, веди тогда."
    me "Ага, веди, она же вот напротив."

    "Я рукой указал на соседнее здание через небольшой пролесок."

    show kat thinking at left with dspr

    kat "Ха, довольно компактно у вас тут."
    
    show mi grin pioneer at right with dspr

    mi "А то, зато всё в шаговой доступности!"
    me "Ну да ладно, не будем задерживаться на одном месте."
    
    show kat normal pioneer at left with dspr

    kat "Точно."

    show bg ext_library_day with dissolve2

    "Пройдя буквально шагов десять, мы уже были перед зданием библиотеки."

    me "Собственно вот он, главный бастион знаний и просто художественной литературы в этом лагере."

    show kat interested at left with dspr

    kat "Интересно, какие там книжки есть."
    me "Такое ощущение, что все на этом свете[wp]"

    "Проговорил я себе под нос и зашёл внутрь."

    stop ambience fadeout 3.5
    scene bg int_library_day
    show kat normal pioneer at right
    show mi normal pioneer at fright
    show mz normal pioneer glasses at left
    with dissolve2
    play ambience ambience_library_day fadein 3.5

    "В библиотеке было, как обычно, немноголюдно."
    "Только одна Женя сидела за своим рабочим местом и внимательно глазела на нас."

    show mi upset pioneer at fright with dspr

    "Особенно она сверлила взглядом Мику, но та лишь стеснительно уводила взгляд."

    mz "Много же вас."
    me "И тебе привет."
    me "Слушай, нам тут это[wp]"

    show mz bukal pioneer glasses at left with dspr

    mz "Обходной лист, да-да, я была на линейке, Семён."
    mz "И более того, я даже знаю как зовут нашу новенькую."

    show kat joy pioneer at right with dspr

    kat "Ого, значит не нужно представляться, отлично, а то я уже устала немного."

    show kat normal at right
    show mz smile pioneer glasses at left
    with dspr

    mz "Тебе нет, а мне вот следовало бы."

    show mz normal pioneer glasses at left with dspr

    "Она встала из-за своего рабочего места и подошла к нам, при этом всё также не спуская взгляда с Мику."

    th "Да что такое? Может они повздорили? Хотя, это вздор какой-то, что самая дружелюбная девушка с кем-то поругалась."

    "Видимо, не выдержав отсутствия инициативы со стороны Мику, Женя решила взять дело в свои руки."

    show mz angry pioneer glasses at left with dspr

    mz "Мику, а Мику. Ты мне когда книги вернёшь?"
    mz "Хотя какой там книги, хотя бы одну книжку верни, уже хорошо будет!"

    show kat confused pioneer at right with dspr

    kat "Ого, Мику, а ты любительница литературы?"

    show mz confused pioneer glasses at left with dspr

    mz "О, ещё какая[wp]"

    show mz angry pioneer glasses at left with dspr

    mz "Правда, читает дрянь всякую зарубежную!"

    show mi shy pioneer at fright with dspr

    "Тем временем сама Мику вся залилась красным."

    mi "Верну я тебе, верну, честное пионерское."
    mz "Интересно, сколько я это выслушивать буду[wp]"

    show mz normal pioneer glasses at left with dspr

    mz "Короче говоря, чтобы через пару дней вернула всё что взяла, и не дай Бог я не досчитаюсь хоть одной, а иначе[wp]"

    "Женя призадумывалась, выдумывая наказание для нашей музыкантки."

    show mz excitement pioneer glasses at left with dspr

    mz "Пороть тебя буду! Долго и нещадно!"

    "Смешливым тоном сказала она."

    show mi sad pioneer at fright with dspr

    mi "Ну не надо, я правда всё принесу, честно-честно!"

    show mz bukal pioneer glasses at left with dspr

    mz "Смотри у меня[wp]"
    mz "Ой, ладно, давай сюда бумажку эту свою."

    "Женя вырвала обходный лист из рук Кати и, быстренько поставив там свою подпись, вернула его обратно."

    mz "Вот, можете идти."
    mz "Кстати, совсем забылась, я Женя."

    show kat upset pioneer at right with dspr

    kat "Очень приятно[wp]"

    "Без особой радости в голосе пробурчала Катя."

    mz "И ещё одно кстати. Семён."

    th "Вот же блин, я уже думал, что она про меня забыла."

    me "Да-да?"

    show mz angry pioneer glasses at left with dspr

    mz "С тобой как-нибудь отдельный разговор устроим!"

    "Эти слова звучали не просто по злодейски, а по супер злодейски."

    me "Х-Хорошо[wp]"

    show mz laugh pioneer glasses at left with dspr

    mz "Вот и славно."

    show mz bukal pioneer glasses at left with dspr

    mz "А теперь, пожалуйста, покиньте помещение."

    "Услышал приказ библиотекарши, все мы без лишних раздумий, с радостью, покинули библиотеку."

    window hide dissolve
    stop ambience fadeout 3.5
    stop music fadeout 4.5
    scene bg ext_library_day
    show kat normal pioneer at left
    show mi upset pioneer at right
    with dissolve2
    play ambience ambience_camp_center_day fadein 3.5
    window show dissolve

    kat "Да уж[wp]"
    me "Что?"

    show kat interested pioneer at left with dspr

    kat "Она всегда такая злюка?"
    me "За частую."

    "Я легонько похлопал Мику по плечу."

    me "Не грусти ты так из-за этого, просто верни книги ей и всё."
    mi "Было бы это ещё так просто[wp]"
    me "В каком смысле?"
    mi "В таком, что я их потеряла!"
    
    show kat confused pioneer at left with dspr

    kat "Как же ты так умудрилась?"

    show mi cry pioneer at right with dspr

    mi "Не знаю!"

    "Заливаясь слезами и дрожжащим голосом ответила она."

    th "Надо же, как сильно она переживает по такому пустяку. Как будто, Женя что-то страшное с ней сделает."

    show kat smile pioneer at left with dspr

    kat "Ну-ну, рыдать-то из-за книжек зачем. Давай, я тебе помогу их поискать после обеда, хорошо?"

    show mi sad pioneer at right with dspr

    "Предложение немного успокоило нашу музыкантку и та утерла слёзы."

    mi "Хорошо[wp] Спасибо тебе."

    show kat joy pioneer at left with dspr

    kat "Не нужно благодарности."

    show kat normal pioneer at left 
    show mi serious pioneer at right
    with dpsr

    kat "А теперь, давайте уже сдадим этот обходной лист."
    me "Прямо с языка сняла."

    window hide dissolve
    scene bg ext_houses_day with dissolve2
    window show dissolve

    "Я шёл немного впереди всей нашей группы."
    "И лишь краем уха мне слышалось, как Катя и Мику обсуждали книги."
    "В основном, они обсуждали романы про любовь. Видимо, ничего другого их не интересовало."

    th "Как же хорошо, что они не мучают меня своими книгами для девочек."

    kat "Семён!"

    "И словно услышав мои мысли, меня окликнули позади."

    th "Похоже, всё же замучают меня[wp]"

    show mi normal pioneer at right
    show kat smile pioneer at left
    with dissolve

    "Я немного замедлился и сравнялся с девушками."

    me "Да?"

    show kat joy pioneer at left with dspr

    kat "А вот какая у тебя любимая книга?"

    show mi grin pioneer at right with dspr

    mi "И вообще, любишь ли ты читать?"
    kat "А если любишь, то сколько книг прочитал?"
    mi "И какой жанр тебе больше всего по душе?"

    "Вопросы сыпались один за другим и я ни на один не успевал отвечать."

    th "Сговорились походу."

    if wnfh_Data.FlagGet("d7_kat_oblil_me") == True:

        th "Видать, Катя, хочет в отместку за обливание замучать меня вопросами. Но я так просто не сдамся на этом поле боя."

    me "Так, придержите коней и дайте мне ответить хоть на один вопрос."
    kat "Так ты успевай отвечать!"
    mi "Да-да! Это вообще-то быстрый опрос."

    show kat grin pioneer at left with dspr

    kat "Ладно, шутим мы. Какой там был первый вопрос[wp]"

    show mi normal pioneer at right with dspr

    mi "Какая любимая книга."
    me "Автостопом по галактике."

    "Особо даже не думая ответил я."

    show mi upset pioneer at right
    show kat thinking pioneer at left
    with dspr

    "Однако, на мой, казалось бы, просто ответ, девушки задумчиво переглянулись между собой."

    me "Что, никогда не слышали о такой?"
    kat "Честно говоря нет."
    mi "Да, я тоже не слышала[wp]"
    me "Ну вот значит когда из лагеря вернётесь, поищите как-нибудь на досуге."

    scene bg ext_house_of_mt_day
    show mi normal pioneer at right
    show kat normal pioneer at left
    with santa_barbara_out_blure_dissolve2

    "Спустя около пяти минут разговора о книгах, мы наконец дошли до дома вожатой."
    "На удивление, Ольга Дмитриевна не лежала на шезлонге, наслаждаясь прекрасным солнышком, пока её пионеры пахают."
    
    mi "Я вас, наверное, снаружи подожду."

    show mi grin pioneer at right with dspr

    mi "В конце-концов, мне же не зачем туда идти."

    "Одновременно с Катей кивнув, мы поднявшись к входу и, постучавшись вошли внутрь."

    stop ambience fadeout 3.5
    scene bg int_house_of_mt_day 
    show kat normal pioneer at left
    show mt normal pioneer at right
    with door_blure_dissolve
    play ambience ambience_int_cabin_day fadein 3.5

    "Ольга Дмитриевна тихо мирно сидела за столом и сортировала документы, попутно делая записи в какой-то журнал."

    me "Вот и мы."
    mt "Отлично."

    "Катя подошла к вожатой и протянула его вожатой."
    "Но, та лишь убрала его в кучу к другим документам."

    show mt sad pioneer at center with dspr

    mt "Потом посмотрю[wp]"
    mt "А пока, вы свободны."
    kat "До свидания!"

    stop ambience fadeout 3.5
    scene bg ext_house_of_mt_day
    show kat normal pioneer at left
    show mi normal pioneer at right
    with dissolve2
    play ambience ambience_camp_center_day fadein 3.5
    play music wnfh_music_list["the_bridge"] fadein 5.0

    "Когда мы вышли из домика, Мику уже успела занять шезлонг."

    mi "О, вы быстро довольно, даже заскучать не успела."
    me "Да там же делов на минуту от силы."

    "Спустившись по ступенькам я уселся на самую нижнюю."

    show kat confused pioneer at left with dspr

    kat "И что дальше?"
    mi "Дальше только ждать."
    kat "Ждать чего?"
    me "Обеда. Как раз время уже подходит к нему."

    show kat thinking pioneer at left with dspr

    "Катя оглядела нас задумчивым взглядом."

    kat "Тогда, может сразу к столовой пойти, если обед скоро?"
    me "Блин, я так устал, что мне лень куда-то идти сейчас."
    mi "И мне тоже[wp]"

    "Полусонным голосом проговорила Мику."

    me "Ты там давай не засыпай."

    hide mi with dissolve

    "На моё замечание, она только лишь угукнула и кое-как отвернулась от нас."

    show kat normal pioneer close at center with dissolve

    "В то время как Катя села рядом со мной."

    me "Ну, что скажешь?"
    kat "М? В плане?"
    me "Как тебе это место?"

    show kat smile pioneer close at center with dspr

    kat "Знаешь, здесь довольно хорошо."
    kat "И люди хорошие[wp]"

    show kat upset pioneer at center with dspr

    kat "Кроме тех двух рыжих[wp]"

    if wnfh_Data.FlagGet("d7_kat_oblil_me") == True:

        jump d8_begunok_w_mi_choices

    me "Ха, зря ты на них обижаешься, на самом деле."
    me "Они хорошие ребята, просто иногда любят почудить[wp]"

    show kat sad pioneer close at center with dspr

    kat "Я уж заметила[wp]"

    "Она грустно вздохнула."

    show kat thinking pioneer close at center with dspr

    kat "Но всё это как-то неправильно[wp]"
    me "Не бери в голову, всё это пустяки."
    kat "Хорошо, я подумаю над этим[wp]"

    jump d8_begunok_w_mi_ending

label d8_begunok_w_mi_choices:

    show kat obida pioneer close at center with dspr

    kat "[wp]И тебя тоже."
    kat "Нет, ну зачем обливать-то было."

    if wnfh_Data.getChoice_result_number("d7_choice_n9") == 1:
        
        call screen wnfh_choice(
            ["kat", "Извиниться. Ещё раз", "В этот раз надо быть искреннее", "d8_me_kat_appologize_1", {"kat": 1}],
            ["neutral", "Промолчать", "Всё таки я уже извинялся", "d8_me_kat_silent_1", {"kat": -1}],
            ["d8_choice_n4", "Катя намекает на извинение V1"]
            ) with sphere_blure_dissolve2

    else:

        call screen wnfh_choice(
            ["kat", "Всё таки извиниться", "Не быть же мне мудаком", "d8_me_kat_appologize_2", {"kat": 1}],
            ["neutral", "Промолчать", "Меня подставили!", "d8_me_kat_silent_2", {"kat": -1}],
            ["d8_choice_n5", "Катя намекает на извинение V2"]
            ) with sphere_blure_dissolve2

label d8_me_kat_appologize_1:

    "Собравшись с мыслями, я решил попытаться извиниться куда более искреннее, чем в прошлый раз."

    show kat normal pioneer close at center with dspr

    me "Слушай, прости меня, пожалуйста."
    me "Я правда не хотел никого обливать, но вышло то что вышло."
    me "И тут я сам виноват, что согласился на всю эту авантюру."
    me "Мне следовало предвидеть, что эти рыжие удумают что-нибудь."

    "Катя внимательно всматривалась в меня, видимо пытаясь понять, насколько я честен перед ней."

    kat "Хм[wp] Что ж, хорошо, прощаю."
    me "Спасибо, прямо камень с души упал."
    kat "Та не за что."

    jump d8_begunok_w_mi_ending

label d8_me_kat_silent_1:

    show kat pockerface pioneer close at center with dspr

    "Катя сверлила меня своим взглядом, видимо, ожидая что-то от меня услышать."

    th "Чего ей нужно от меня? Чтобы я ещё раз извинился или что? Неужели одного раза было недостаточно[wp]"

    kat "Хорошо, я поняла тебя."

    "Сказала она и отвернулась от меня."

    th "Чёрт, она телепатка?!"

    jump d8_begunok_w_mi_ending
    
label d8_me_kat_appologize_2:

    th "Пусть меня и действительно подставили, всё же, это я косяк впорол, а значит и мне приносить извинения."

    "Собравшись с мыслями, я постарался выдать самое искреннее извинение, какое только мог."

    me "Кать, мне конечно следовало ещё тогда это сказать, но[wp]"

    show kat normal pioneer close at center with dspr

    me "Ты уж прости меня за обливание это."
    me "Дурак я, что согласился на всю эту идею, и не подумал, что меня так вот подставят."
    me "У меня и в мыслях не было кого-либо сегодня обливать."

    "Она внимательно осмотрела меня всего и, по всей видимости, задумалась над тем, насколько искренни слова мои."

    kat "Ладно, прощаю, но только, чтобы такого больше не было ни в отношении меня, ни в отношении других пионеров."
    me "Разумеется."

    jump d8_begunok_w_mi_ending

label d8_me_kat_silent_2:

    show kat pockerface pioneer close at center with dspr

    "Моя собеседница уставилась на меня своим пустым взглядом, будто ожидая что-то услышать от меня."
    "Но я и не знал, что ей сказать на этот счёт."

    th "Неужели не понятно, что меня подставили и я тут вообще не при делах?"
    th "И вообще, судить нужно тех кто приказы отдавал, а не исполнял! Тем более меня заставили чуть ли не насильно."

    kat "Ну хорошо-хорошо[wp]"

    "Безэмоционально сказала она и отвернулась от меня."

    th "Она что, мысли мои читает?!"

    jump d8_begunok_w_mi_ending

label d8_begunok_w_mi_ending:

    stop music fadeout 4.5
    play sound sfx_dinner_horn_processed

    "Наконец, прозвучал горн призывающий пионеров на обед."
    "От этого звука, тихо спящая Мику не на шутку испугалась, чуть не выпав из шезлонга."

    me "Мику, острожнее нужно быть."

    show mi shy pioneer at right
    show kat normal pioneer at left
    with dissolve

    mi "Ой, я уснула чтоли?"
    kat "Да, не надолго."

    show mi normal pioneer at right with dspr

    mi "И как я так умудряюсь[wp]"
    me "Ладно, пойдёмте на обед."

    jump d8_obed_me_kat_mi

label d8_begunok_w_un:
    $ wnfh_set_time()
    show kat normal pioneer at left
    show un smile pioneer at right
    with dissolve

    me "Так, какие там места нам нужно посетить?"

    "Катя поднесла листок поближе к себе и стала читать вслух."

    kat "Музыкальный кружок, клубы, медпункт и библиотека."

    show un normal pioneer at right with dspr

    "Лена наклонилась над листком и, сделала вид, что понимает всё вверх ногами."
    
    un "Что ж, медпунт и библиотека тут по близости, можем туда сходить сразу."

    "У меня в голове сразу возникла карта лагеря."

    # возможно тут следует показать карту под какой-нибудь смешной звук
    # а потом сделать анимацию как Семён представляет себе путь по лагерю

    show black with dissolve
    $ renpy.notify("Тут должна быть карта с анимацией ЧИТАЙ коммент day_8_begunok line 1133")
    th "Если так прикинуть, то эффективнее выйдет начать с дальнего края «Совёнка»."
    th "И потом если двигаться зигзагообразно от муз клуба[wp] Да[wp]"
    th "После чего посетим клубы, пройдёмся через площадь, вот мы уже в библиотеке и медпункте."
    th "А оттуда прямо к домику вожатой! По моему всё идеально складывается."

    hide black
    show kat smile pioneer far at left
    show un smile pioneer far at right
    with sphere_blure_dissolve2

    "Пока я стоял и раздумывал маршрут, Лена и Катя, явно заболтавшись, успели уже отойти на небольшое расстояние от столовой."

    me "Так, подождите меня!"

    show kat smile pioneer at left
    show un smile2 pioneer at right
    with dissolve

    "Перемахнув через перила, я подбежал к девушкам, которые тихонько хихикали надо мной."

    me "Чего смеётесь, хоть бы предупредили."

    show un smile pioneer at right with dspr

    un "Меньше в облаках летать надо!"
    me "Куда вы идти решили-то?"

    show un grin pioneer at right
    show kat normal pioneer at left
    with dspr

    un "Грызть гранит науки!"

    "Шутливо ответила мне она."

    me "Ага, то есть в библиотеку."

    show kat thinking pioneer at left with dspr

    kat "Мы же надеемся ты не против?"

    show un shy pioneer at right with dspr

    un "Да[wp]"
    me "Та как бы нет, просто у меня в голове есть более эффективный маршрут но[wp]"

    "Я отмахнулся рукой."

    me "Ай пофиг, идёмте."

    show kat normal pioneer at left
    show un smile pioneer at right
    show bg ext_library_day
    with dissolve2

    "И вот снова я стоял перед этим логовом дракона."
    "С библиотекой меня связывал один неприятный инцидент, о котором я не очень-то и хотел вспоминать."

    me "Так, с библиотекой давайте зашли и вышли."

    show kat confused pioneer at left with dspr

    kat "А к чему такая спешка в отношение библиотеки?"

    show un normal pioneer at right with dspr

    un "Да Семён, может она хочет получше осмотреться?"

    "Глядя прямо на Лену я глубоко вздохнул."

    show un laugh pioneer at right with dspr

    "И тут она, по всей видимости, вспомнила об этой «занимательной» истории."

    un "Ах да, точно[wp]"

    "Через смех сказала она, вгоняя нашу новенькую в полный ступор."
    "Катя смотрела то на Лену, то на Меня, и так по кругу."

    kat "Мне кто-нибудь расскажет в чём дело?"
    me "Ну сейчас она остановится и пояснит тебе."

    show un smile3 pioneer at right with dspr

    "Через некоторое время Лена успокоилась."

    show kat interested pioneer at left with dspr

    un "Коротко говоря, Семён по своей невнимательности обвалил все полки в библиотеке и сбежал с места преступления."
    un "За это его недолюбливает наша библиотекарша."

    show kat smile2 pioneer at left with dspr

    kat "Забавная история."
    me "Да-да, давайте уже заходить."

    window hide dissolve
    stop ambience fadeout 3.5
    scene bg int_library_day
    show un smile pioneer at fright
    show kat normal pioneer at cright
    show mz bukal pioneer glasses at left
    with santa_barbara_out_blure_dissolve2
    play ambience ambience_library_day fadein 3.5
    $ renpy.pause(0.5)
    window show dissolve

    "И внутри как обычно сидела Женя, которая с усталым видом заполняла какой-то журнал."
    "Завидев нас, она медленно подняла свой взгляд."

    mz "Ого, вас тут целая группа."
    mz "Что, обходной лист подписать, да?"

    "Катя быстро одобрительно закивала."
    "Цокнув языком, Женя протянула руку, как бы прося бегунок."
    "Благо, наша новенькая была соображающая и поняла что делать."

    kat "Меня Катей звать кстати говоря."

    "Сказала она вручая лист, который библиотекарша тут же принялась подписывать."

    mz "Я знаю[wp]"

    "Безэмоционально ответила Женя."
    "Но после этого остановилась на полпути росписи."

    mz "В смысле, я Евгения, но можешь звать Женей."

    "placeholder"

label d8_begunok_canon:
    $ wnfh_set_time()
    ## Семён и Катя отправляются заполнять бегунок
    "Я вышел из столовой, и позвал сидящую на лавочке Катю." 
    "Посмотрев на меня, она неспешно поднялась с лавочки и подошла ко мне."
    
    show kat normal pioneer at center with dissolve
    
    kat "Ну что, куда пойдем в первую очередь?"
    me "Смотря, что тебе интереснее."
    
    "Девушка стала разглядывать именования мест в листе."
    
    show kat thinking with dspr
    
    kat "Я[wp] Не знаю, тут всё интересно в целом."
    me "Ладно, допустим."
    me "Давай разберемся сначала с клубами и муз кружком, чтобы потом не надо было туда сюда ходить по лагерю."
    me "А потом надо будет выполнить задание по поимке неуловимой вожатой."
    
    show kat grin with dspr
    
    "Катя усмехнулась"
    
    kat "И где же мы будет её искать, раз она неуловимая?"
    me "На месте разберемся."
    
    show kat smile2 with dspr
    
    kat "Ладно, пойдем уже."
    
    "Скомандовала она и мы быстрым шагом отправились в сторону клубов."
    
    window hide
    scene bg ext_clubs_day with dissolve2
    $ renpy.pause(1.0)
    window show
    
    "Вскоре мы подошли к клубам, и отворив дверь вошли во внутрь."
    
    window hide
    stop ambience fadeout 0.5
    #34 крутой переход
    play sound sfx_open_door_1
    scene bg int_clubs_male_day with door_blure_dissolve2
    #33 звук открытия двери
    play ambience ambience_medstation_inside_day fadein 3
    show kat normal pioneer at center with dissolve
    window show

    ## В клубах
    kat "Но, тут же никого нет[wp] {w}Кто подписывать-то будет?"
    
    "Я мягко отнял у Кати бегунок и, взяв ручку со стола, подписал его."
    #33 звук подписывания бумаги
    show kat surprise with dspr
    
    kat "А так разве можно?"
    me "Мне как члену клуба можно."
    
    "Положив ручку на место, я отдал Кате её бегунок."
    
    me "Вот и всё, идём дальше."
    
    window hide
    stop ambience fadeout 0.5
    scene bg ext_clubs_day with door_invert_blure_dissolve2
    play sound sfx_close_door_1
    play ambience ambience_camp_center_day fadein 3
    window show
    
    "Закрыв клубы, мы направились в сторону муз кружка."
    
    window hide
    scene bg ext_musclub_day with slide_left_blure_dissolve2
    show kat normal pioneer with dissolve
    window show
    ## В музкружке
    "Сократив путь через небольшой пролесок, мы дошли до муз кружка, откуда доносилась музыка на пианино."
    
    # Какая-нибудь пианинко на фоне (может кавер хатсуне мику?)))))))
    kat "Красиво играет."
    me "Да, это наша девочка-оркестр. {w}Мику зовут."
    kat "Наверное это о ней мне Лена рассказывала."
    kat "Это же она с длинными аквамариновыми волосами?"
    me "Да-да-да, всё верно."
    me "А ещё, тебе Лена рассказывала, что она очень любит тараторить?"
    
    window hide
    hide kat with dissolve
    $ renpy.pause(1.0)
    scene bg ext_musclub_verandah_day_wnfh with santa_barbara_in_blure_dissolve2
    show kat normal pioneer at left with dissolve
    window show
    
    kat "Вроде как, но я думаю она сильно преувеличивает."
    th "Хо, девочка, как же ты ошибаешься[wp] Как же ошибаешься."
    
    "Я постучался в дверь, и мы вошли внутрь."
    
    window hide
    hide kat with dissolve
    play sound sfx_open_door_clubs
    scene bg int_musclub_day with door_blure_dissolve
    stop ambience fadeout 0.5
    stop music fadeout 0.5
    play ambience ambience_music_club_day fadein 3
    play music music_list["so_good_to_be_careless"] fadein 5
    window show
    
    "Войдя внутрь, мы застали Мику играющей на пианино[wp] Или рояле? Неважно в общем."
    "Главное, что это было нисколечко ни удивительно."
    "Но продлилось это не долго, ведь она тут же обратила на нас внимание. А вот это уже было даже удивительно."
    
    show mi normal pioneer at left with dissolve
    show kat thinking pioneer at center with dissolve
    
    mi "Приветик, какими судьбами пожаловали к нам, ну то есть ко мне, я тут только одна, но надеюсь скоро будет больше!"
    
    "Мику настолько быстро протараторила, что Катя аж немного удивилась."
    
    kat "И тебе привет."
    
    show mi grin with dspr
    
    mi "А ты у нас новенькая значит, да? {w}Тогда давай знакомиться, я Мику! Нет, честно-честно! Никто не верит, а меня правда так зовут. Просто у меня мама из Японии. Папа с ней познакомился, когда строил там[wp] Ну, то есть не строил – он у меня инженер[wp]"
    mi "Короче, атомную станцию! Или плотину[wp] Или мост[wp] Ну, неважно!"
    
    "Мику говорила с такой скоростью, что половину слов просто проглатывала."
    
    th "Девочка-пулемет, вот твоё настоящее имя, поэтому никто и не верит в твою историю."
    
    "Бедная Катя похоже ещё сильнее удивилась тому, с какой скоростью говорила Мику."
    
    kat "А я Катя."
    
    "Тихо проговорила девочка."
    
    mi "Приятно познакомиться! Не хочешь вступить ко мне в музыкальный кружок? А то мне здесь очень грустно одной. Ты кстати умеешь на чём-нибудь играть?"
    
    "Наша новенькая немного призадумалась, видимо обдумывая тот поток слов, что на нее сейчас вылился."
    
    show kat smile with dspr
    
    kat "Да, я на скрипке хорошо играть умею."
    mi "Пра-а-авда?"
    
    "Протяжно произнесла Мику."
    
    show kat grin with dspr
    
    kat "Правда-правда."
    mi "Так это же замечательно! Тогда тебе точно надо ко мне записаться! Я буду на пианино, а ты на скрипке, будет просто прекрасное сочетание!"
    
    show mi sad with dspr
    
    mi "А то звучания одного инструмента крайне недостаточно, для красивой мелодии."
    
    show kat smile2 with dspr
    
    kat "Знаешь[wp] Почему бы и нет? Попробуем сыграть вместе!"
    
    show mi happy with dspr
    
    mi "Чудесно, просто чудесно!"
    
    show mi normal with dspr
    
    "Я громко прокашлялся, и девочки перевели взгляд на меня. {w}Видимо, за своими разговорами они немного забыли про меня."
    
    me "Мику, подпишешь Кате обходной?"
    mi "Ну конечно! Давай его сюда!"
    
    show mi normal:
        ease_quart 2.5 xcenter -0.2    

    "Катя протянула Мику бегунок, и та, элегантно выхватив его из рук, в припрыжку побежала в подсобку."
    
    show kat normal with dspr
    
    me "Ты точно хочешь играть с девочкой-пулеметом?"
    
    "С легкой насмешкой в голосе спросил я."
    
    show kat smile with dspr
    
    kat "А что, она такая забавная когда тараторит, и к тому же у нее тут целый муз кружок, с кучей инструментов."
    kat "Правда, я и на половине играть не умею, но зато скрипкой владею в совершенстве!"
    me "В таком случае желаю тебе удачи и терпения."
    kat "Да ладно, могло быть и хуже."
    
    show mi normal pioneer:
        ease_quart 2.0 xcenter 0.28
    
    "Совсем скоро, музыкантка вернулась из подсобки."
    
    mi "Готово! Теперь ты полноправная участница нашего муз кружка! То есть моего, но теперь будет наш!"
    
    "Мику торжественно протянула Кате обходной."
    
    show kat happy with dspr
    
    kat "Спасибо!"
    me "Отлично, мы тогда пойдем, нам ещё несколько мест посетить успеть надо, иначе вожатая стукнет."
    
    show mi grin with dspr
    
    mi "Хорошо, не буду задерживать! А тебя, Катя, тогда жду тут после обеда, договорились?"
    
    "Катя одобрительно кивнула, и мы покинули кружок."
    
    window hide
    stop ambience fadeout 0.5
    stop music fadeout 2
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_musclub_verandah_day_wnfh with door_invert_blure_dissolve
    play sound sfx_close_door_1
    $ renpy.pause(1.0)
    window show
    
    "Мы, преисполняясь хорошим настроением, отправились в сторону медпункта."

    window hide
    scene bg ext_musclub_day with santa_barbara_out_blure_dissolve2
    $ renpy.pause(1.0)
    play music music_list["two_glasses_of_melancholy"] fadein 5
    scene bg ext_lenin_square_day_wnfh with slide_up_blure_dissolve2
    window show
    ## Славя докладывает где искать ОД
    "Проходя мимо по площади, нас позади окликнули."
    "Мы остановились, и к нам подбежала Славя."
    
    show sl normal pioneer at center with dissolve
    
    sl "Вот вы где, а я вас везде ищу."
    me "Что-то случилось?"
    sl "Ольга Дмитриевна просила вам передать, если успеете закончить до обеда, то она будет ждать вас у себя в домике."
    me "Хорошо, спасибо."
    sl "Всё, я побежала!"
    
    hide sl with dissolve
    
    "Славя развернулась и ушла в неизвестном направлении, а мы продолжили свой путь."
    
    window hide
    scene bg ext_aidpost_day with dissolve2
    window show

    "Скоро мы стояли перед зданием медпункта."
    "И прежде чем войти во внутрь, я постучался."
    
    th "Пожалуйста, пусть тебя не будет на месте, прошу, прошу!"
    
    $ wnfh_set_name("cs","Голос")
    
    cs "Войдите!"
    
    "Громко сказала медсестра изнутри."
    
    th "Ну не-е-ет."
    
    "С огромным нежеланием, я распахнул входную дверь и мы вошли в медпункт."
    
    window hide
    stop ambience fadeout 0.5
    stop music fadeout 2
    play sound sfx_open_door_1
    scene bg int_aidpost_day with door_blure_dissolve
    play ambience ambience_medstation_inside_day fadein 3
    show cs normal at right with dissolve
    show kat normal pioneer at left with dissolve
    $ wnfh_set_name("cs","Виола")
    window show
    
    ## В медпункте
    "В медпункте сидела Виола и заполняла какие-то бумаги."
    "Закончив подписывать, она повернулась к нам, и Катя подошла к ней."
    
    kat "Здравствуйте, я Катя, новенькая здесь!"
    cs "Что, поранились где-то? Или что-то болит?"
    me "Аэ[wp] нет."
    
    show cs smile at right with dspr
    play music music_list["eternal_longing"] fadein 5
    
    cs "Зачем же вы тогда пожаловали?"
    
    th "Обычного, с этого вопроса и начинается программа телепередач."
    
    me "Виолетта Церновна, не могли бы вы подписать Кате бегунок?"
    
    show cs normal at right with dspr
    
    "Она раздражённо вздохнула."
    
    cs "Просто Виола."
    cs "Давай, пионерка, сюда свой «бегунок»."
    
    show cs normal glasses at right with dspr
    
    "Катя протянула Виоле лист."
    "Быстро изучив его, медсестра поставила там размашистую такую подпись."
    
    cs "Всё, если точно больше ничего не надо, то топайте отсюда."
    cs "А то вы меня отвлекаете от важной работы."
    
    show kat smile with dspr
    show kat smile:
        ease_quart 3.0 xcenter 0.6

    "Забрав обходной лист, Катя в припрыжку пошла на выход."
    
    show kat smile:
        ease_quart 2.0 xcenter 1.2
    
    th "Вот так вот просто?"
    th "А где там фирменное «давай раздевайся пионер, слушать тебя будем»?"
    th "Хотя[wp] {w}Не-не, лучше не надо."
    # А жаль(
    
    window hide
    stop ambience fadeout 0.5
    stop music fadeout 0.5
    scene bg ext_aidpost_day with door_invert_blure_dissolve
    play sound sfx_close_door_1
    play ambience ambience_camp_center_day fadein 3
    show kat normal pioneer at center with dissolve
    window show
    
    me "Что ж, всё прошло куда лучше чем обычно."
    kat "А как обычно всё проходит?"
    me "Хо, лучше тебе этого не знать."
    
    show kat confused with dspr
    
    kat "Но[wp] Почему?"
    me "Думаю, сама когда-нибудь узнаешь."
    me "Так, осталось последнее место."
    
    "Быстрым и уверенным шагом мы отправились к библиотеке."
    
    window hide
    scene bg ext_library_day with slide_right_blure_dissolve2
    window show
    
    "Библиотека, ровно как и медпункт, одно из тех мест которое я просто не могу терпеть." 
    "А всё из-за ужасного зверя, обитающего там. {w}Нашей библиотекарши Жени."
    "Понадеюсь, что она быстро подпишет обходной, и я с Катей покинем это место живыми."
    
    th "Наверное стоит предупредить её, но что если с ней Женя себя не будет вести себя так[wp] Как обычно ведёт."
    th "Ладно, будет что будет."
    
    "С диким нежеланием, я вошел внутрь библиотеки, и следом за мной Катя."
    
    window hide
    #scene bg ext_library_day at wnfh_entrance(1.0)
    stop ambience fadeout 0.5
    #$ renpy.pause(1.0)
    play sound sfx_open_door_1
    scene bg int_library_day with bibl_entrance
    play ambience ambience_library_day fadein 3
    show mz normal pioneer glasses at left
    show kat normal pioneer at right 
    with dissolve
    window show
    
    ## В библиотеке
    "Женя сидела на своем месте и что самое удивительное — не спала."
    
    mz "Зачем пришли?"
    me "Да вот, новенькой обходный лист подписать надо."
    
    show mz bukal pioneer glasses at left with dspr
    
    mz "Хорошо, давайте сюда."
    
    "Катя подошла к столу Жени и протянула ей лист." 
    "Через секунду, Женя поставила подпись и вернула обходной обратно Кате."
    
    mz "Читательский билет заводить будем?"
    
    show kat thinking with dspr
    
    kat "А это надолго?" 
    mz "Если пишешь быстро, то нет."
    
    show kat normal with dspr
    
    kat "Тогда давай, наверное."
    
    "Женя достала из ящика некий лист с именами и подписями."
    
    mz "Слева имя, фамилия, справа в конце твоя подпись — всё."
    
    "Катя сделала всё как надо, и Женя убрала листок обратно."
    
    mz "Что-то ещё вам надо?"
    me "Нет, всё, мы уходим."
    
    show kat sad with dspr
    
    kat "Но[wp]"
    me "Уходи-и-им."
    
    show kat guilty with dspr
    
    kat "Ладно[wp]"
    
    window hide
    stop ambience fadeout 0.5
    scene bg ext_library_day with door_invert_blure_dissolve
    play sound sfx_close_door_1
    show kat normal pioneer at center with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_list["two_glasses_of_melancholy"] fadein 5
    window show

    me "Какая-то она слишком добрая была."
    #kat "Очевидно, что кто-то помог ей избавиться от недотраха." 
    kat "А что, обычно злюка?"
    me "Ну[wp] Не то чтобы, просто[wp]"
    me "Ай сложно объяснить."
    me "Скажем, у нас так исторически сложилось, что мы самую малость недолюбливаем друг друга."
    
    show kat surprise with dspr
    
    kat "И как же так вышло?"
    me "Долго рассказывать."
    
    show kat thinking with dspr
    
    kat "Понятно[wp]"
    
    th "Какие-то все слишком[wp] {w}Нормальные."
    th "Виола не пошлила, Женя не докапывалась."
    th "Прям полный разрыв шаблонов."
    
    "С заполненным обходным, мы отправились к вожатой."
    
    window hide
    hide kat with dissolve
    scene bg ext_house_of_mt_day with slide_left_blure_dissolve2
    $ renpy.pause(1.0)
    window show
    
    "Благо идти тут было недалеко, и мы уже скоро были у домика."
    "Мы поднялись по ступенькам к двери, и постучавшись вошли в дом."
    
    window hide
    play sound sfx_open_door_1
    scene bg ext_house_of_mt_day at wnfh_entrance
    stop ambience fadeout 0.5
    scene bg int_house_of_mt_day with door_blure_dissolve2
    play ambience ambience_int_cabin_day fadein 3
    window show
    
    ## Сдача бегунка вожатой
    
    "Ольга Дмитриевна была в домике и вновь подписывала какие-то документы за столом."
    
    show mt normal pioneer close at right with dissolve
    show kat normal pioneer close at left with dissolve
    
    "Мы подошли ближе к вожатой, и Катя торжественно протянула ей заполненный бегунок."
    
    show kat confused with dspr
    
    "И Ольга Дмитриевна просто положила его в стопку к другим документам, даже не посмотрев."
    
    mt "Молодцы ребята, обходной я потом посмотрю, когда с делами закончу. {w}Куда-нибудь успела записаться?"
    
    show kat smile with dspr
    
    kat "Да, в муз кружок записалась."
    
    show mt smile with dspr
    
    mt "Молодец, а то там Мику совсем скучает одна."
    me "Ладно, мы теперь свободны?"
    mt "Да, в целом вы свободны, только обед уже через десять минут."
    me "Тогда мы наверное на улице подождём обеда."
    
    "Вожатая угукнула и вернулась к своим бумагам, а мы покинули домик."
    
    window hide
    stop ambience fadeout 0.5
    scene bg ext_house_of_mt_day with door_invert_blure_dissolve
    play sound sfx_close_door_1
    show kat normal pioneer with dissolve
    play ambience ambience_camp_center_day fadein 3
    window show

    "Выйдя, мы сели на крылечке."
    
    me "Ну-с, как тебе лагерь?"
    
    show kat smile2 with dspr
    
    kat "Уютненько, люди хорошие."
    
    show kat obida with dspr
    
    kat "Кроме тех двух[wp]"
    kat "Ну, тех, кто из ведра окатили меня на входе."
    me "Алиса с Ульяной?"
    kat "Ага."
    me "Зря ты о них так, просто дурачатся."
    me "Так-то люди они хорошие."
    kat "Возможно, но это не отменяет, что они хулиганьё!"
    
    "Фыркнула она и сложила руки."
    
    me "Да ладно тебе, подружитесь ещё."
    
    "Между нами повисла тишина."
    
    stop music fadeout 5
    
    "Которую мне захотелось разбавить."
    
    me "Наверное немного поздновато задавать такой вопрос но[wp]"
    me "Почему ты приехала на неделю позже?"
    
    show kat thinking with dspr
    
    "Катя серьёзно задумалась над этим вопросом."
    "Как будто, этот вопрос был чем-то необычным для неё."
    
    kat "Я[wp] {w}Я не знаю?"
    me "В смысле[wp] Не знаешь?"
    
    play sound sfx_dinner_horn_processed
    
    "Катя уже собиралась что-то ответить, но горн на обед прервал её."
    
    me "Ладно, потом расскажешь."
    
    "Мы молча отправились в столовую."

    jump d8_obed_me_kat
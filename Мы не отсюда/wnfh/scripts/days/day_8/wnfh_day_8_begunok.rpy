label d8_begunok:

    window hide dissolve
    hide mid d8_breakfast_empty with dissolve
    $ renpy.pause(1.0)
    stop ambience fadeout 2.5
    $ wnfh_set_time()
    scene bg ext_dining_hall_near_day with slide_right_blure_dissolve2
    play ambience ambience_camp_center_evening fadein 3
    play music music_list["dance_of_fireflies"] fadein 5
    $ renpy.pause(1.0)
    window show

    if wnfh_Data.getChoice_result_number("d8_choice_n2") == 1:

        jump d8_begunok_w_mi

    elif wnfh_Data.getChoice_result_number("d8_choice_n3") == 1:

        jump d8_begunok_w_un

    else: #wnfh_Data.getChoice_result_number("d8_choice_n1") == 2:

        jump d8_begunok_canon

label d8_begunok_w_mi:

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
    
    th "Козалось бы, несколько минут, не так уж и много."
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
    
    kat "Ух ты, у вас ещё и плотники тут есть?"
    me "Да, напротив нашего клуба авиамоделирования, Стас и Сергей."
    me "Странные ребята, если честно[wp]"
    mi "По правде говоря, впервые слышу вообще о них."
    me "Ну, неудивительно, они же из другого отряда, и почти безвылазно сидят у себя. А вот чем они там занимаются, — неизвестно."

    "продолжение следует"

label d8_begunok_w_un:

    "placeholder"

label d8_begunok_canon:
    
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
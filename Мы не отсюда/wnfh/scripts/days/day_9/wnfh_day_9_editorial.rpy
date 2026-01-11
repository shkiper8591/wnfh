label d9_editorial:
    
    $ wnfh_Data.FlagSet("journalist") == True
    window hide dissolve
    stop ambience fadeout 2.5
    hide mi
    show mt normal pioneer panama at left
    show kat sad pioneer at right
    show bg ext_musclub_day
    with dissolve2
    play ambience ambience_camp_center_day fadein 2.5
    $ renpy.pause(0.5)
    show bg ext_lenin_square_day_wnfh with dissolve
    $ renpy.pause(0.5)
    show bg ext_library_day with dissolve
    window show dissolve

    mt "Вот и пришли. Дальше вы сами."

    show kat confused pioneer at right with dspr

    kat "Так мы бы и сами могли дойти."

    show mt angry pioneer panama at left with dspr

    mt "Могли. А могли и «потеряться» по пути."
    mt "Особенно это касается тебя, Семён."
    me "А я-то чё сразу?"

    show mt normal pioneer panama at left with dspr

    mt "Всё, вас там внутри уже ждут."

    "Демонстративно отсалютовав, я первым вошёл внутрь."

    stop ambience fadeout 2.5
    scene bg int_library_day
    show mz normal pioneer glasses at left
    show kat normal pioneer at right
    with door_blure_dissolve
    play sound sfx_open_door_1
    play ambience ambience_library_day fadein 2.5

    "Внутри была — как не удивительно — Женя, которая сидела за столом и, судя по всему, пересчитывала книги или что-то в этом роде."
    "Но как только мы вошли, она отвлеклась от этого дела."

    mz "О, а вот и обещанное пополнение."

    "Она встала из-за стола и подошла к Кате."

    mz "Кажется, мы с тобой ещё не знакомы."
    mz "Я Евгения, заведую этим тихим уголком знаний."

    th "Что? Мы же вчера здесь были, как она[wp] Что?"

    "Закончив представляться, Женя протянула Кате руку, которую она пожала."

    show kat smile pioneer at right with dspr

    kat "А мне кажется, мы очень даже знакомы."

    show mz bukal pioneer glasses at left with dspr

    "После такого ответа библиотекарша решила присмотреться повнимательнее."

    mz "Аня?"
    kat "Мимо. Я Катя."

    show mz confused pioneer glasses at left with dspr

    mz "Точно, Катя. Простите, у меня плохая память на лица."
    mz "Идём, покажу ваше рабочее место."

    "Мы проследовали за Женей в дальний угол библиотеки, где был вход в подсобное помещение."

    scene bg int_editorial_day_wnfh
    show un dr_normal_wk dr background
    show mz normal pioneer glasses at left
    show kat normal pioneer at right
    with dissolve

    "И зайдя внутрь, мы встретили Лену, которая сидела за холстом и что-то рисовала."

    th "Получается, она — первый и единственный доброволец."

    show un dr_smile dr background with dspr

    un "Приветики!"

    show kat smile pioneer at right with dspr

    kat "Здравствуй."

    if wnfh_Data.getChoice_points_sum("un") == 4:

        "Я улыбнулся и помахал Лене."

    else:

        "Я лениво помахал Лене."

    show un dr_normal_wk dr background with dspr
    show mz sceptic pioneer glasses at left 
    with dspr

    mz "Итак, товарищи, кто из вас двоих умеет грамотно писать?"
    me "У меня тройка по русскому."
    
    show mz bukal pioneer glasses at left with dspr

    mz "Так, понятно, а ты?"

    show kat thinking pioneer at right with dspr

    kat "Ну[wp] Я, конечно, не самая грамотная, но могу творчески мыслить."
    mz "Сойдёт. Значит, будешь писать статьи."

    show kat surprise pioneer at right with dspr

    kat "Ох, хорошо, но[wp]"
    mz "Никаких но, иди сюда."

    show mz bukal pioneer glasses far at right
    show kat surprise pioneer far at fright
    with dspr

    "Женя отвела Катю к столу, на котором стояла печатная машинка."

    mz "Вот твоё рабочее место, садись давай."

    show kat wr wr_normal background at center behind mz with dspr

    "Повинуясь, Катя села за стол и положила руки на клавиши."
    #КОСЯК визуала: спрайт Кати расчитан на наличие листа в машинке, потому тут у неё не хватает куска плеча.

    show mz normal pioneer glasses far at right with dspr

    mz "Так, аппаратура довольно простая, но не прощающая ошибок."
    mz "А посему нужно хорошо следить за тем, что печатаешь."

    show bg int_editorial_day_bumaga_wnfh with dspr
    play sound wnfh_sfx_list["typewriter_paper"]

    "Женя вставила лист бумаги в машинку и поставила его на исходное положение."

    mz "Каждый раз, когда заканчиваешь писать строку, лист нужно вручную отводить назад."
    mz "Попробуй пока что-нибудь написать, привыкни к аппарату."
    mz "Так, теперь ты."

    play sound sfx_open_table
    $ renpy.pause(1.0)
    show kat wr wr_normal_wk background at center with dspr
    play sound wnfh_sfx_list["typewriter_typing"] loop fadein 0.5
    show mz normal pioneer glasses at right with dspr

    "Открыв ящик стола, Женя взяла оттуда, судя по всему, фотоаппарат и подошла ко мне."

    mz "Ты у нас будешь заниматься фотографией."

    "Она протянула мне фотоаппарат."
    "Взяв его и разглядев вблизи, я очень сильно удивился, поняв, что это самый настоящий «Полароид»."

    th "Нихрена себе подарочек, блин. А откуда здесь вообще такой?"

    show mz angry pioneer glasses at right with dspr

    mz "Данный образец техники очень дорогой, так что отвечаешь за него своей жизнью."
    me "Да, понимаю, я такие уже держал пару раз."

    show mz normal pioneer glasses at right with dspr

    mz "Отлично, значит, мне меньше объяснять."
    me "Верно."

    show kat wr wr_normal background at center
    show un dr_normal background
    show mz normal pioneer glasses far at center with dspr
    with dspr
    play sound wnfh_sfx_list["mz_clap"]

    "Женя встала в центр помещения и негромко похлопала, привлекая внимание."

    mz "Так, товарищи, инструктаж я вам провела."
    mz "Настало время пробной работы."

    show mz confused pioneer glasses at center with dspr

    mz "Вам нужно будет сделать небольшую статью о[wp]"

    show mz excitement pioneer glasses at center with dspr

    mz "Успехах лагерной активности, во!"

    show mz fun pioneer glasses at center with dspr

    mz "Сходите в спортзал и клубы, поспрашиваете там, как дела, чего достигли. Только без особого фанатизма, ладно?"
    me_kat "Ладно." 
    mz "Всё, к обеду жду сданную работу."

    hide mz with dissolve
    show un dr_normal_wk dr background with dspr

    "Когда наша новая начальница ушла, девушки сразу засуетились."
    "Лена убрала холст и закрепила на мольберте большой лист бумаги."

    play sound sfx_open_table

    "В это время Катя, порывшись в ящике рабочего стола, достала оттуда блокнот и карандаш."

    show kat normal pioneer at right with dspr

    kat "Так, ну что, пойдём?"

    th "Быстро, однако, она перепрофилировалась из музыкантов в редакторы."

    me "Ага."
    kat "А ты, Лен?"

    show un dr_smile dr background with dspr

    un "Я бы с радостью, но нужно же подготовить саму газету."
    un "Поэтому без меня."
    kat "Ясненько."

    stop ambience fadeout 2.5
    scene bg ext_library_day
    show kat normal pioneer at center
    with dissolve
    play ambience ambience_camp_center_day fadein 2.5

    kat "Так, с чего бы нам начать[wp] {w}Есть мысли?"
    me "На удивление есть. Предлагаю начать со спортивной секции."
    kat "Хорошо, а почему оттуда?"
    me "Потому что она ближе, вот и всё."

    show kat interested pioneer at center with dspr

    kat "О как. Справедливо."
    me "Пойдём, я знаю короткий путь."

    "Обойдя библиотеку, мы пошли коротким путём через пролесок."

    window hide dissolve
    stop ambience fadeout 2.5
    scene black with dissolve2
    $ renpy.pause(0.5)
    play ambience wnfh_ambience_list["sporthall"] fadein 2.5
    scene bg int_sporthall_day_wnfh
    show kat normal pioneer at left
    with dissolve2
    window show dissolve

    "Войдя в спортивный корпус и пройдя по коридорам, мы вышли в основной зал."
    "Здесь была группа пионеров чуть младше меня, которые бегали по кругу."
    "За всем этим следила главная спортсменка лагеря. {w=0.5}Ульяна."

    show usw normalsmile sport2 far at right with dissolve

    th "Где она находит столько времени? И деда на складе подменяет, и в спортзале занятия проводит."
    th "И это только то, о чём я знаю — небось, у неё ещё какие-нибудь занятия тут есть."

    show usw normalsmile sport2 at right with dissolve

    "Мы подошли к ней поближе, и тогда она обратила на нас внимание."

    play sound wnfh_sfx_list["usw_whistle"]

    "Ульяна достала свисток и остановила тренировку, сказав, что пока можно отдохнуть."
    "Уставшие пионеры мигом заняли свободные лавочки."

    usw "Так-так, чем обязана?"
    kat "Хотим взять интервью об успехах спорткружка."
    usw "Интервью?"

    show usw grin sport2 at right with dspr

    usw "Так вы же вроде музыканты. Или вы собираетесь петь серенаду о спортзале?"

    show usw laugh2 sport2 at right with dspr

    usw "Или, быть может, вдарите бодрого року? Это было бы вообще отлично!"

    show kat pockerface pioneer at left with dspr

    "Мы с катей недоумевающе переглянулись."

    me "Вообще-то мы это делаем для клуба журналистики."

    show usw normalsmile sport2 at right with dspr

    usw "А-а-а, так вы журналисты!"

    show usw laugh sport2 at right with dspr

    usw "Извините, не признала."
    me "Блин, Ульян, хорош стебать уже, а?"

    show kat normal pioneer at left
    show usw normalsmile sport2 at right
    with dspr
    
    usw "Ладно, ладно[wp] Не знаю даже, что сказать. {w=1.0}Наверное, успехи у нас пока скромные."
    me "Так и не скажешь, вон как ребят мучишь."

    show usw upset sport2 at right with dspr

    "Она грустно охнула."

    usw "Да я просчиталась прилично, и мы слишком много пропустили."
    usw "Теперь вот ускоренно нагоняем."
    kat "К чему такая спешка?"

    show usw smile sport2 at right with dspr

    usw "А вот скоро сами всё узнаете!"
    me "А по дружбе расскажешь?"

    show usw tricky sport2 at right with dspr

    "Со свойственным ей хитрым взглядом Ульянка задумчиво почесала подбородок."
    "После чего наклонилась поближе к нам."

    show usw smile sport2 at right with dspr

    usw "По секрету, через два дня у нас будет большое соревнование по футболу."
    usw "Вот к нему мы и готовимся."

    show usw dontlike sport2 at right with dspr

    usw "Вообще ещё Алиса участвует, но ей хоть бы что. Как будто её вообще это не заботит."
    me "То есть?"
    usw "Ну вы видите, чтобы она тренировала свою группу? Я вот нет."

    show usw upset sport2 at right with dspr

    usw "А это делает исход матча предсказуемым и совсем не интересным."

    "Всё это время Катя делала пометки себе в блокнот."

    kat "Так, запишем следующим образом: у спорткружка имеются определённые успехи."

    show usw normal sport2 at right with dspr

    usw "Получается, что так."
    kat "Что же, думаю, это всё, что мы хотели узнать. Спасибо тебе!"

    show usw laugh2 sport2 at right with dspr

    usw "Вам тоже спасибо за визит!"

    "Помахав на прощание, мы покинули спортзал."

    window hide dissolve
    stop ambience fadeout 2.5
    scene bg ext_lenin_square_day_wnfh
    show kat smile pioneer at center
    with dissolve2
    play ambience ambience_camp_center_day fadein 2.5
    $ renpy.pause(0.5)
    window show dissolve

    kat "Так-с, теперь куда направимся?"
    me "В клубы, куда же ещё."

    show kat thinking pioneer at center with dspr

    kat "Не знаю, мало ли."

    window hide dissolve
    stop ambience fadeout 2.5
    scene bg int_clubs_male_day
    show sh normal pioneer at right
    show kat normal pioneer at left
    with dissolve2
    play ambience ambience_clubs_inside_day fadein 2.0
    $ renpy.pause(0.5)
    window show dissolve

    "Поход в клубы прошёл довольно[wp] Предсказуемо."
    "Мы встретились с Шуриком, поговорили о наших успехах."
    "Мы с ним долго рассказывали про нашу самую большую модель самолёта, которая по задумке должна быть на радиоуправлении."
    "Но пришлось с сожалением признать, что из-за нехватки деталей от этой идеи пришлось отказаться."
    "После этого мы быстренько зашли в соседний клуб, к плотникам. Кроме того, что одного из них зовут Стасом, а другого Сергеем, я ничего не знал ни про них, ни про сам клуб."
    "Стоит отметить, что у ребят дела идут очень даже неплохо. Вытачивают всякие прикольные модели из дерева и не жалуются."
    "Несколько штук даже были в цвете — девчонки из их отряда, хоть никто из них в кружке не состоит, время от времени занимались покраской."
    "Проведя в гостях у плотников немного времени и попрощавшись с ними, мы отправились к нашей подруге-музыкантше."

    window hide dissolve
    scene bg ext_musclub_day
    show kat normal pioneer at center 
    with dissolve2
    window show dissolve

    "Направляясь к музклубу, Катя на пол пути остановилась."

    kat "И вот мы снова здесь[wp]"
    me "Ага."

    show kat obida pioneer at center with dspr

    kat "Блин! Неправильно всё это!"
    kat "Почему нашего мнения никто даже не спросил?"
    kat "Как будто я хочу заниматься всем этим!"
    me "Мне казалось, ты выглядела весьма заинтересованной тогда, разве нет?"

    show kat upset pioneer at center with dspr

    "Она издала грустный вздох."

    kat "Ну[wp] Я скорее из вежливости вид сделала."
    kat "Не закатывать же истерику из-за этого."
    kat "Просто[wp]"

    show kat sad pioneer at center with dspr

    kat "Несправедливо всё это."

    "Голос Кати дрожал, словно она была готова расплакаться."

    me "Что ж, мы ничего не можем поделать с этим."
    me "Но нам же никто не запретил сюда ходить, верно?"
    kat "Да[wp]"
    me "Ну тогда больше стимул закончить со статьёй и прийти обратно."
    me "Так что давай, не унывай."

    show kat smile pioneer at center with dspr

    "Я слегка потрепал ей волосы, на что она тщетно попыталась воспротивиться."

    kat "Ну всё, идём скорее уже."

    hide kat with dissolve

    "Катя мигом убежала вперёд к музклубу."

    th "Ох, ну и качели эмоциональные у неё, конечно."

    window hide dissolve
    show bg ext_musclub_verandah_day_wnfh
    $ renpy.pause(0.5)
    stop ambience fadeout 2.5
    scene bg int_musclub_day
    show kat smile pioneer at left
    with dissolve2
    play sound sfx_open_door_clubs_2
    play ambience ambience_music_club_day fadein 2.5 
    $ renpy.pause(0.5)
    window show dissolve

    kat "Приветики, а вот и снова мы!"

    show kat surprise pioneer at left with dspr

    ## возможно, тут можно сделать арт........

    "Войдя внутрь, мы застали крайне грустную картину."

    show mi sad pioneer far at right
    with dissolve

    "Мику сидела в углу, уткнувшись лицом в колени и тихонько хныча."     

    th "Похоже, она приняла наш перевод слишком близко к сердцу. {w=1.0}Блин, даже не удобно как-то теперь, хотя казалось бы[wp]"

    show kat sad pioneer close at left
    show mi sad pioneer close at right
    with dspr

    "Мы подошли к ней, и Катя села рядом."

    kat "Эй, Микусь, ты в порядке?"

    "Она подняла заплаканный взгляд на Катю."
    
    mi "Нет. Не в порядке."
    
    "Какое-то время вглядываясь в глаза подруги, она перевела взгляд на меня."
    
    show mi cry pioneer close at right with dspr
    
    mi "Снова я одна в этих проклятых стенах!"
    mi "Единственных друзей увели в этот чёртов клуб, и[wp] И[wp]"
    
    "Не сумев сдержать эмоции, Мику разрыдалась и вновь уткнулась лицом в колени."
    "Катя крепко обняла её, а я в это время присел напротив девушек."
    
    kat "Слушай, это же не конец света. Мы ведь всё ещё можем к тебе ходить в свободное время. И будем ходить."
    kat "Мы же не можем тебя тут одну бросить, нам вообще-то тоже очень нравится музыка. И твоя компания тоже!"
    me "Вот именно."
    mi "А какой смысл? У нас времени будет совсем чуть-чуть — ни разыграться, ни поболтать."
    mi "А вдруг вам нужно будет большую статью сделать? Вы тогда вообще не придёте!"
    mi "Я ведь уже успела обрадоваться, что настал конец моему одиночеству, что у меня появились хорошие друзья с общими интересами."
    mi "А сегодня у меня их отняли[wp]"

    show kat guilty pioneer close at left with dspr
    
    "Мы с Катей переглянулись, не зная, как быть дальше."
    "Катя только утешительно поглаживала Мику по плечу."
    
    th "Нужно что-то делать[wp] Нужно что-то сказать[wp] Только вот что? Впрочем, пофигу! Будет что будет."

    me "Мику, ты чересчур преувеличиваешь."
    me "Мы и сами не в восторге от сложившейся ситуации, но куда нам деваться?"
    me "Послушай[wp]"
    
    "Пододвинувшись поближе к ней, я положил руку ей на колено."
    
    me "Это не трагедия, а просто неприятное стечение обстоятельств."
    me "И это не стоит того, чтобы лить слёзы, лучше уж приберечь их для важных моментов."
    
    th "Блин, сам от себя такого не ожидал. Но эффект, кажется, есть."

    show mi sad pioneer close at right with dspr

    "Я аккуратно поднял её голову и вытёр слёзы."

    me "Как только закончим, я обещаю, мы мигом к тебе примчимся."
    me "Нам осталось совсем немного. Пара часов, и мы будем свободны."

    if wnfh_Data.getChoice_points_sum("mi") == 3:

        show kat confused pioneer close at left with dspr

        "Ничего не говоря, Мику немного приподнялась, вырвавшись из объятий Кати."
        
        show mi happy pioneer close at right with dspr
        ## +1 к ЛП Мику 
        "После чего резко обняла меня."
        "Это было настолько неожиданно, что я едва не свалился на спину."

        show mi cry_smile pioneer close at right with dspr

        mi "Спасибо вам за тёплые слова."
        mi "Мне просто[wp] Впрочем, неважно."

    else:

        show mi cry_smile pioneer close at right
        show kat smile pioneer close at left
        with dspr

        mi "Спасибо вам, ребята."
        kat "Хе, мы же, в конце концов, товарищи!"
        me "Это верно подмеченно."

    show mi normal pioneer at right with dspr

    "Мику встала, а мы за ней."

    mi "Так-с, и что же вас привело сюда, если вы всё ещё заняты?"
    
    show kat thinking pioneer at left with dspr

    kat "Вообще нам надо написать об успехах музклуба, но[wp]"

    show mi sad pioneer at right with dspr

    mi "Но писать попросту не о чем."

    show kat upset pioneer at left with dspr

    kat "Получается, что так."

    show mi normal pioneer at right with dspr

    mi "Ну тогда чего вы тут стоите?"

    show mi grin pioneer at right with dspr

    mi "Идите и доделывайте свои дела, чтобы скорее исполнить ваше обещание!"

    show kat joy pioneer at left with dspr

    kat "Да, пожалуй, так и поступим!"

    show mi happy pioneer at right with dspr

    mi "Всё тогда, буду ждать вас!"

    "Быстрым шагом мы направились обратно в клуб журналистики."

    window hide dissolve
    stop ambience fadeout 2.5
    hide kat
    hide mi
    show bg ext_musclub_day
    with dissolve
    play ambience ambience_camp_center_day fadein 2.5
    $ renpy.pause(0.5)
    window show dissolve

    th "Да уж, Мику, похоже, переживает серьёзные проблемы на фоне одиночества, раз её так это волнует[wp] {w}Печально всё это."
    th "Да ещё эта их ссора с Алисой[wp] {w=1.0}Блин, хотел бы я как-нибудь помочь, только как?"
    th "Возможно, Лена может подсобить? Они же вместе живут, наверняка что-нибудь знает и подскажет."
    th "Впрочем, это проблемы будущего меня."

    show kat normal pioneer at center
    show bg ext_lenin_square_day_wnfh
    with dissolve

    "По пути в библиотеку у нас с Катей завязался диалог."

    kat "Слушай, а красиво у тебя получилось."
    me "В смысле?"
    kat "Ну, с Мику. Так успокоил её[wp]"

    show kat smile pioneer at center with dspr

    "Она слегка усмехнулась."

    kat "Полагаю, ты у нас в этом спец!"
    me "А, нет, вовсе нет. Просто от души говорил, вот и всё. Чистая импровизация."
    kat "Вот оно как[wp]"
    kat "Получается, у тебя действительно доброе сердце!"
    me "Наверное." 

    window hide dissolve
    scene bg ext_library_day with dissolve2
    $ renpy.pause(0.5)
    stop ambience fadeout 2.5
    show bg int_editorial_day_bumaga_wnfh
    play ambience ambience_library_day fadein 2.5 
    show un dr_normal_wk dr background
    with dissolve2
    $ renpy.pause(0.3)
    play sound wnfh_sfx_list["typewriter_typing"] loop fadein 0.5
    show kat wr wr_normal_wk background at center with dissolve
    window show dissolve

    "Прибыв в нашу редакцию, мы без лишних слов принялись за работу."
    "Мы работали в ускоренном темпе, и газета была готова как раз к обеду."

    scene bg int_library_day
    show kat guilty pioneer at left
    show un normal pioneer at fleft
    show mz angry pioneer glasses at right
    with dissolve
    stop sound fadeout 0.3

    "Сдав работу, мы получили разгромную критику."

    mz "Товарищи, это совсем никуда не годится!"
    mz "Написано ужасно. Много повторов, стиль не соблюдён, ошибки в простейших словах!"

    show un smile pioneer at fleft with dspr

    mz "Только художественное оформление меня более-менее порадовало."

    show mz bukal pioneer glasses at right
    show un shy pioneer at fleft
    with dspr

    mz "Однако! У нас всё же газета, а не холст! Поэтому вот эти вот завитушки и[wp] Не знаю, цветочки? В общем, это лишнее!"
    mz "Подводя итог, результатом я крайне недовольна, а у нас на завтра большие планы!"
    mz "Поэтому после обеда вы всем составом возвращаетесь и переделываете, ясно?"
    me "Ясно."

    show un normal pioneer at fleft with dspr

    mz "Кстати о фотографе. Чтобы ты, Семён, зря времени не терял, будешь помогать Кате писать."
    mz "И то, что у тебя там трояк по русскому, сейчас особой роли не играет. Всё же, это какая-никакая помощь."
    me "Принял."
    mz "Всё, а теперь быстро потопали в столовую!"

    window hide dissolve
    stop ambience fadeout 2.5
    show bg ext_library_day
    hide kat
    hide un
    hide mz
    with dissolve2
    play ambience ambience_camp_center_day fadein 2.5
    window show dissolve

    "Разгромная критика от Жени сильно подорвала наш боевой дух."
    "Но ещё обиднее было то, что к Мику мы придём куда позже, чем собирались."

    th "Блин, подумает ведь ещё, что её обманули и кинули."
    th "Надеюсь, что до такого не дойдёт. Мы хоть с Мику и мало общаемся, но всё же неприятно видеть девушку в слезах."

    window hide dissolve
    stop ambience fadeout 2.5
    show bg int_editorial_day_bumaga_wnfh
    show un dr_normal_wk dr background
    show kat wr wr_normal_wk background at center
    with dissolve2
    play sound wnfh_sfx_list["typewriter_typing"] loop fadein 0.5
    play ambience ambience_library_day fadein 2.5
    $ renpy.pause(0.5)
    window show dissolve

    "Вернувшись обратно в нашу подсобку, мы снова принялись за работу."
    "В этот раз с учётом всех полученных ранее замечаний."

    window hide dissolve
    #stop ambience fadeout 2.5
    $ wnfh_set_time("sunset")
    show bg int_editorial_sunset_wnfh with dissolve2
    $ renpy.pause(0.3, hard=True)
    #play ambience ambience_cabin_evening fadein 2.5
    window show dissolve
    #КОСЯК: вечернему фону также нужна вариация с бумагой.

    "Преследуя цель сделать свою работу как можно лучше, мы не заметили, как наступил вечер."
    "Это означало, что до ужина осталось всего ничего и нам следует поторопиться."
    "Разумеется, это сказалось на качестве последних строк, но в остальном работа должна была выйти хорошо."
    "По крайней мере, мы на это надеялись."

    scene bg int_library_sunset_wnfh
    show kat normal pioneer at left
    show un normal pioneer at fleft
    show mz bukal pioneer glasses at right 
    with dissolve2
    stop sound fadeout 1.0

    "В этот раз, сдав статью, мы получили более-менее неплохую оценку."

    mz "Что же, конечно, ваша работа звёзд с неба не хватает, но[wp]"
    mz "Очень даже неплохо. Есть что подтянуть, но это уже хотя бы можно людям показывать."
    mz "Думаю, ещё одна-две таких статьи и вы набьёте руку."

    "Окончив свою мысль, Женя перевела пристальный взгляд на меня."

    show mz sceptic pioneer glasses at right with dspr

    mz "Кстати говоря, не могу не отметить тот факт, что с твоей помощью, Семён, качество текста возросло."
    mz "Отчего у меня закрались лёгкие подозрения касательно твоего низкого балла по русскому языку."

    th "Вот же блин, опасный момент[wp] Она, похоже, не поняла, что это была шутка."

    me "Ну[wp] Вдвоём просто проще работать, вот и всё."
    me "Так-то в русском я вообще не бом-бом."

    "В ответ она только хмыкнула и сверкнула глазами."

    mz "А так, что ещё могу сказать[wp]"

    show mz fun pioneer glasses at right with dspr

    mz "Молодцы!"

    show kat laugh pioneer at left
    show un smile2 pioneer at fleft
    with dspr

    "Нас охватила такая радость, что мы аж хором воскликнули «Ура-а!»."

    show mz normal pioneer glasses at right with dspr

    mz "Ладно, порадовались маленькому успеху, а теперь пора на ужин идти."

    "Зарядившись хорошим настроением, мы покинули библиотеку."

    window hide dissolve
    jump d9_musclub_evening
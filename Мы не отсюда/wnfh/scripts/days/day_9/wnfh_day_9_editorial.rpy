label d9_editorial:
    
    window hide dissolve
    stop ambience fadeout 2.5
    hide mi
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

    kat "Так мы же и сами тогда могли дойти."

    show mt angry pioneer panama at left with dspr

    mt "Могли. А могли ровно также и «потеряться» по пути."
    mt "Особенно это касается тебя, Семён."
    me "А я-то чё сразу."

    show mt normal pioneer panama at left with dspr

    mt "Всё, вас там внутри уже ждут."

    "Демонстративно отсалютовав, я первым вошёл внутрь."

    stop ambience fadeout 2.5
    scene bg int_library_day
    show mz normal pioneer glasses at left
    show kat normal pioneer at right
    with dissolve
    play ambience ambience_library_day fadein 2.5

    "Внутри была, как не удивительно, Женя, которая сидела за столом и, судя по всеми, пересчитывала книги или что-то в этом роде."
    "Но как только мы вошли, она отвлеклась от этого дела."

    mz "О, а вот и обещанное пополнение."

    "Она встала из-за стола и подошла к Кате."

    mz "Кажется, мы с тобой не очень знакомы."
    mz "Я Евгения, заведую здесь тихим уголком знаний."

    th "Что? Мы же вчера здесь были, как она[wp] Что?"

    "Закончив представляться, Женя протянула Кате руку, которую она и пожала."

    show kat smile pioneer at right with dspr

    kat "А мне кажется, мы очень даже знакомы."

    "На данную фразу, Женя пристально вгляделась в Катю."

    mz "Аня? Инна? Мария?"
    kat "Мимо. Я Катя."

    show mz bukal pioneer glasses at left with dspr

    mz "Точно, Катя. Простите, у меня плохая память на новые лица."
    mz "Идём, покажу ваше рабочее место."

    "Мы проследовали за библиотекаршей в дальний угол библиотеки, где был вход в подсобное помещение."

    scene bg int_editorial_day_wnfh
    show un dr_normal_wk dr background
    show mz normal pioneer glasses at left
    show kat normal pioneer at right
    with dissolve

    "И зайдя внутрь, здесь уже была Лена, которая сидела за холстом и что-то рисовала."

    th "Получается, она первый и единственный доброволец."

    show un dr_smile dr background with dspr

    un "Приветики!"

    show kat smile pioneer at right with dspr

    kat "Здравствуй."

    if wnfh_Data.getChoice_points_sum("un") == 4:

        "Я с довольной улыбкой, радостно помахал Лене."

    else:

        "Я лениво помахал Лене."

    show un dr_normal_wk dr background with dspr
    show mz sceptic pioneer glasses at left 
    with dspr

    mz "И так, товарищи, кто из вас двоих умеет грамотно писать?"
    me "У меня тройка по русскому."
    
    show mz bukal pioneer glasses at left with dspr

    mz "Так, понятно, а ты?"

    show kat thinking pioneer at right with dspr

    kat "Ну[wp] Я конечно не самая грамотная, но могу творчески мыслить."
    mz "Сойдёт, значит будешь писать статьи."

    show kat surprise pioneer at right with dspr

    kat "Ох, хорошо, но[wp]"
    mz "Никаких но, иди сюда."

    "Женя отвела Катю ко столу, на котором стояла печатная машинка."

    mz "Вот твоё рабочее место, садись давай."

    show kat wr wr_normal background with dissolve

    "Повинуясь, Катя села за стол и положила руки на клавиши."

    mz "Так, аппаратура довольно простая, но не прощающая ошибок."
    mz "А посему, нужно хорошо следить за печатанием."

    show bg int_editorial_day_bumaga_wnfh with dspr

    "Женя вставила лист бумаги в машинку и поставила его на исходное положение."

    mz "Каждый раз, когда заканчиваешь писать строку, лист нужно вручную отводить назад."
    mz "Попробуй что-нибудь писать, привыкни к аппарату, а тем временем[wp]"

    show kat wr wr_normal_wk background with dspr

    "Открыв ящик в столе, Женя взяла оттуда, судя по всему, фотоаппарат и подошла ко мне."

    show mz normal pioneer glasses at left with dspr

    mz "Ты у нас будешь заниматься фотографией."

    "Она протянула мне фотоаппарат."
    "Взяв его и разглядев вблизи, я очень сильно удивился, поняв, что это самый настоящий «полароид»."

    th "Нихрена себе подарочек блин, а откуда такое вообще здесь?"

    show mz angry pioneer glasses at left with dspr

    mz "Данный образец техники очень дорогой, так что отвечаешь за него своей жизнью."
    me "Да, понимаю, я такие уже держал пару раз."

    show mz normal pioneer glasses at left with dspr

    mz "Отлично, значит мне меньше объяснять."
    me "Верно."

    show kat wr wr_normal background
    show un dr_normal background
    with dspr

    "Женя встала в центр помещения и негромко похлопала, привлекая внимание."

    mz "Так товарищи, инструктаж я вам провела."
    mz "А теперь настало время пробной работы."

    show mz confused pioneer glasses at left with dspr

    mz "Вам нужно будет сделать небольшую статью о[wp]"

    show mz excitement pioneer glasses at left with dspr

    mz "Успехах лагерной активности, во!"

    show mz fun pioneer glasses at left with dspr

    mz "Сходите в спортзал и клубы, поспрашиваете там, как дела, чего достигли. Только без особого фанатизма, ладно?"
    me_kat_d "Ладно." 
    mz "Всё, к обеду жду сданную работу."

    hide mz with dissolve

    "Когда начальник ушла, девушки сразу засуетились."
    "Лена убрала холст, и закрепила на мольберте большой лист бумаги."
    "В это время Катя, порывшись в ящике рабочего стола, достала оттуда блокнот и карандаш."

    show kat normal pioneer at right with dspr

    kat "Так, ну что, пойдём?"

    th "Быстро однако она перепрофилировалась из музыкантов в редактор стенгазеты."

    me "Ага."
    kat "А ты Лен?"
    un "Я бы с радостью, но нужно же подготовить саму газету."
    un "Поэтому без меня."
    kat "Ясненько."

    stop ambience fadeout 2.5
    scene bg ext_library_day
    show kat normal pioneer at center
    with dissolve
    play ambience ambience_camp_center_day fadein 2.5

    kat "Так, с чего бы нам начать[wp]"
    kat "Есть мысли?"
    me "На удивление, есть. Предлагаю начать с спортивной секции."
    kat "Хорошо, а почему оттуда?"
    me "Потому что она ближе, вот и всё."
    kat "О как, справедливо вполне."
    me "Пойдём за мной, я знаю короткий путь."

    "Обойдя библиотеку, мы пошли коротким путём через пролесок."

    window hide dissolve
    stop ambience fadeout 2.5
    scene black with dissolve2
    $ renpy.pause(0.5)
    $ renpy.notify("Нужно найти подходящий эмбиент для спортзала")
    play ambience ambience_soccer_play_background fadein 2.5
    scene bg int_sporthall_day_wnfh
    show kat normal pioneer at left
    with dissolve2
    window show dissolve

    "Войдя в спорт секцию, и пройдя по коридорам, мы вышли в основной зал."
    "Здесь была пара младших групп пионеров, которые бегали по кругу."
    "За всем этим следила главная любитель спорта в лагере. {w=0.5}Ульяна."

    show usw normalsmile sport2 far at right with dissolve

    th "Где же она находит столько времени? И деда на складе заменит, и в спортзале занятия проведёт."
    th "У неё ещё небось есть несколько хобби и занятий, о которых мне неизвестно."

    show usw normalsmile sport2 at right with dissolve

    "Мы подошли к ней ближе и тогда она нас заметила."
    "Ульяна достала свисток и остановила тренировки, сказав, что пока отдых."
    "Уставшие дети мигом заняли свободные лавочки."

    usw "Так-так, чем обязана?"
    kat "Хотим взять интервью об успехах спорткружка."

    show usw normal sport2 at right with dspr
    
    usw "Ох, ну[wp] Не знаю даже что сказать. {w=1.0}Наверное, успехи у нас пока скромные."
    me "Так и не скажешь, вон как ребят мучаешь."

    show usw upset sport2 at right with dspr

    "Она грустно охнула."

    show usw calml sport2 at right with dspr

    usw "Мы слишком много пропустили по моим личным упущениям."
    usw "Теперь вот ускоренно нагоняем."
    kat "К чему такая спешка?"

    show usw smile sport2 at right with dspr

    usw "А вот скоро всё сами узнаете!"
    me "А по дружбе расскажешь?"

    show usw tricky sport2 at right with dspr

    "Со свойственным хитрым взглядом, Ульянка задумчиво почесала подбородок."
    "После чего наклонилась поближе к нам."

    show usw smile sport2 at right with dspr

    usw "По секрету, через два дня у нас будет большое футбольное соревнование."
    usw "Вот к нему мы и готовимся."

    show usw dontlike sport2 at right with dspr

    usw "Ещё в этом деле должна участвовать Алиса, но её, как будто, это вообще не заботит."
    me "То есть?"
    usw "Ну вы видите чтобы она тренировала свою группу? Я вот нет."

    show usw upset sport2 at right with dspr

    usw "А это делает исход матча предсказуемым и совсем не интересным."

    "Всё это время, Катя делала пометки себе в блокнот."

    kat "Так, запишем следующим образом: у спорткружка имеются определённые успехи."

    show usw normal sport2 at right with dspr

    usw "Получается, что так."
    kat "Что же, думаю, это всё что мы хотели узнать. Спасибо тебе!"

    show usw laugh2 sport2 at right with dspr

    usw "Вам тоже спасибо за визит."

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

    scene black with dissolve2

    "Поход в клубы прошёл довольно[wp] Обычно."
    "Мы встретились с Шуриком, поговорили об наших успехах."
    "Он и я много рассказывали про нашу самую большую модель самолёта, которая по задумке должна быть на радиоуправлении."
    "Но, было выражено сожаление о том, что идею с управлением невозможно реализовать из-за недостатка деталей."
    "После этого, мы быстренько зашли в соседний клуб плотников. Про тамошних обитателей, я знал только их имена: Стас и Сергей. Так что надолго мы там не задержались."
    "Стоит отметить, что у ребят дела идут очень даже неплохо. Вытачивают всякие модели из дерева прикольные, и не жалуются."
    "Покинув их, мы отправились к нашей подруге музыкантке[wp]"

    window hide dissolve
    scene bg ext_musclub_day
    show kat normal pioneer at center 
    with dissolve2
    window show dissolve

    "Направляясь к музклубу, Катя на пол пути остановилась."

    kat "И вот мы снова здесь[wp]"
    me "Ага."

    show kat obida pioneer at center with dspr

    kat "Блин! Не правильно всё это!"
    kat "Почему нашего мнения даже никто не спросил?"
    kat "Как будто я хочу заниматься всем этим."
    me "Но ты же показала заинтересованность, разве нет?"

    show kat upset pioneer at center with dspr

    "Она издала грустный вздох."

    kat "Скорее из вежливости."
    kat "Не закатывать же истерику из-за этого."
    kat "Просто[wp]"

    show kat sad pioneer at center with dspr

    kat "Несправедливо всё это[wp]"

    "Голос Кати дрожал, словно она вот-вот готова была расплакаться."

    me "Что ж, мы ничего не можем поделать с этим."
    me "Но, нам же никто не запретил сюда ходить, верно?"
    kat "Да[wp]"
    me "Ну тогда больше стимул закончить со статьёй и прийти обратно."
    me "Так что давай, не унывай."

    show kat smile pioneer at center with dspr

    "Я слегка потрепал ей волосы, на что она попыталась тщетно остановить меня."

    kat "Ну всё, идём скорее уже."

    "Катя мигом убежала вперёд к музклубу."

    th "Ох, ну и качели эмоциональные у неё конечно."

    window hide dissolve
    show bg ext_musclub_verandah_day_wnfh
    $ renpy.pause(0.5)
    stop ambience fadeout 2.5
    scene bg int_musclub_day
    show kat smile pioneer at left
    with dissolve2
    play ambience ambience_music_club_day fadein 2.5 
    $ renpy.pause(0.5)
    window show dissolve

    kat "Приветики, а вот и снова мы!"

    show kat surprise pioneer at left with dspr

    ## возможно, тут можно сделать арт........

    "Войдя внутрь мы застали крайне грустную картину."
    "В углу сидела Мику, уткнувшись лицом в колени и тихонько хныча."     

    th "Похоже, наш перевод сильно на ней сказался. {w=1.0}Блин, даже не удобно как-то теперь, хотя казалось бы."

    show kat sad pioneer close at left
    show mi sad pioneer close at right
    with dissolve

    "Мы подошли к ней, и Катя села рядом."

    kat "Эй, Микусь, ты в порядке?"

    "Она подняла заплаканный взгляд на Катю. "
    "Продолжительное вглядываясь в неё, она уткнулась обратно лицом в колени."
    
    mi "Нет. Не в порядке."
    
    "Пробубнила она, после чего снова подняла взгляд, но в этот раз на меня."
    
    show mi cry pioneer close at right with dspr
    
    mi "Снова я одна в этих проклятых стенах!"
    mi "Единственных друзей увели в этот чёртов клуб, и[wp] И[wp]"
    
    "Не сумев сдержать эмоции, Мику разрыдалась и вновь уткнула лицо себе в колени."
    "Катя крепко обняла её, а я в это время присел напротив нашей музыкантки."
    
    kat "Слушай, это же не конец света, мы ведь всё ещё можем к тебе ходить в свободное время."
    kat "Да и не можем мы тебя бросить одну, нам вообще-то тоже очень нравится музыка и твоя компания!"
    me "Она абсолютно права."
    mi "А какой смысл? Времени недостаточно будет у нас, так что не разыграться, не поболтать."
    mi "Да и что если вам нужно будет большую статью сделать? Вы тогда вообще не придёте!"
    mi "Я ведь уже успела обрадоваться, что вот и настал конец моему одиночеству, что вот у меня хорошие друзья с общим интересом."
    mi "А сегодня у меня их отняли[wp]"
    
    "Мы с Катей переглянулись, не зная, как быть дальше."
    "Катя только утешительно поглаживала Мику по плечу."
    
    th "Нужно что-то делать[wp] Нужно что-то сказать[wp] Только вот что? В прочем, пофигу! Пусть будет что будет!"

    me "Мику, ты слишком преувеличиваешь."
    me "Мы и сами не в восторге от сложившейся ситуации, но куда нам деваться?"
    me "Послушай[wp]"
    
    "Пододвинувшись поближе к ней, я положил руку ей на колено."
    
    me "Это не трагедия, а просто неприятное стечение обстоятельств."
    me "И это не стоит того, чтобы лить слёзы, лучше уж приберечь их для важных моментов."
    
    th "Блин, и откуда во мне столько глубоких мыслей?"

    show mi sad pioneer close at right with dspr

    "Я аккуратно поднял её голову и утёр слёзы."
    
    $ wnfh_Data.FlagSet("d9_me_mi_promise") == True

    me "Как только закончим, я обещаю, мы мигом побежим к тебе."
    me "Нам осталось совсем немного, в течении, может, пары часов будем свободны."

    if wnfh_Data.getChoice_points_sum("mi") == 4:

        show kat confused pioneer close at left with dspr

        "Ничего не говоря, Мику немного приподнялась, вырвавшись из объятий Кати."
        
        show mi happy pioneer close at right with dspr
        ## +1 к ЛП Мику 
        "После чего, резко обняла меня."
        "Это было настолько неожиданно, что я не удержался и свалился на спину."

        show kat smile pioneer close at left with dspr

        mi "Спасибо вам за тёплые слова."
        mi "Мне просто[wp] В прочем, неважно."

    else:

        show mi cry_smile pioneer close at right
        show kat smile pioneer close at left
        with dspr

        mi "Спасибо вам ребята, за эту поддержку."
        kat "Хе, мы же в конце-концов товарищи!"
        me "Это верно подмеченно."

    show mi normal pioneer close at right with dspr

    "Мику встала, а мы за ней."

    mi "Так-с, и что же вас привело сюда, если вы всё ещё заняты?"
    
    show kat thinking pioneer close at left with dspr

    kat "Вообще мы хотели узнать об успехах музклуба, но[wp]"

    show mi sad pioneer close at right with dspr

    mi "Но вы уже и так всё узнали, не так ли?"

    show kat upset pioneer close at left with dspr

    kat "Получается что так."

    show mi normal pioneer close at right with dspr

    mi "Ну тогда чего вы тут стоите?"

    show mi grin pioneer close at right with dspr

    mi "Идите и доделывайте свои дела, чтобы скорее исполнить ваше обещание!"

    show kat joy pioneer close at left with dspr

    kat "Да, пожалуй так и поступим!"

    show mi happy pioneer close at right with dspr

    mi "Всё тогда, буду ждать вас!"

    "Быстрым шагом мы направились на выход, обратно в клуб журналистики."

    stop ambience fadeout 2.5
    scene black with dissolve2

    th "Да уж, Мику похоже переживает серьёзные проблемы на фоне одиночества, раз её так это волнует[wp]"
    th "Печально всё это, да и ещё ссора с Алисой[wp] {w=1.0}Блин, хотел бы я как-нибудь помочь ей только как?"
    th "Возможно, Лена может помочь с этим, они же вместе живут, наверняка что-нибудь знает и подскажет."
    th "В прочем, это проблемы будущего меня."

    "По пути в библиотеку, у нас с Катей завязался диалог."

    kat "Слушай, а красиво у тебя получилось."
    me "В смысле?"
    kat "Ну, с Мику, так успокоил её[wp]"
    kat "Полагаю, ты у нас в этом спец!"

    "Она слегка усмехнулась."

    me "А, нет, вовсе нет. Просто от души говорил, вот и всё."
    kat "То есть?"
    me "Это была чистая импровизация."
    kat "Вот оно что[wp]"
    kat "Получается, у тебя действительно доброе сердце!"
    me "Да наверное." 

    window hide dissolve
    play ambience ambience_camp_center_day fadein 2.5
    scene bg ext_library_day with dissolve2
    $ renpy.pause(0.5)
    stop ambience fadeout 2.5
    scene bg int_editorial_day_wnfh
    play ambience_library_day fadein 2.5 
    show un dr_normal background
    with dissolve2
    $ renpy.pause(0.3)
    show kat wr wr_normal background with dissolve
    window show dissolve

    "Прибыв в нашу редакцию, мы без лишних слов принялись за работу."
    "В ускоренном темпе, газета была готова как раз к обеду."

    scene bg int_library_day
    show kat guilty pioneer at left
    show un normal pioneer at fleft
    show mz angry pioneer glasses at right
    with dissolve

    "Сдав работу, мы получили разгромную критику."

    mz "Товарищи, это совсем никуда не годится!"
    mz "Написано ужасно. Много повторов, стиль не соблюден, иногда встречаются ошибки в простейших словах."

    show un smile pioneer fleft with dspr

    mz "Только художественное оформление меня более менее порадовало."

    show un shy pioneer fleft with dspr

    mz "Однако! У нас всё же газета, а не холст! Поэтому вот эти вот завитушки и[wp] Не знаю, цветочки? В общем это лишнее!"
    mz "Подводя итог, результатом я крайне недовольна, а у нас завтра большие планы!"
    mz "Поэтому сейчас после обеда вы всем составом возвращаетесь и переделываете, ясно?"
    me "Ясно."
    mz "Кстати о фотографе. Чтобы ты, Семён, зря времени не терял, будешь помогать Кате писать."
    mz "И пофигу, что у тебя там трояк по-русскому, это всё же какая никакая помощь."
    me "Принял."
    mz "Всё, а теперь быстро потопали в столовую!"

    window hide dissolve
    stop ambience fadeout 2.5
    scene black with dissolve2
    window show dissolve

    "Разгромная критика от Жени сильно подорвала наш боевой дух."
    "Но больше всего обиднее было то, что мы сильно припозднимся к Мику."

    th "Блин, бедная девочка небось опять рыдать будет, думая что её обманули."
    th "Надеюсь, что до такого не дойдёт. Мы хоть с Мику и мало общаемся, но всё же неприятно видеть девушку рыдающую от горя."

    window hide dissolve
    play ambience ambience_library_day fadein 2.5
    scene bg int_editorial_day_wnfh
    show un dr_normal background
    show kat wr wr_normal background
    with dissolve2
    $ renpy.pause(0.5)
    window show dissolve

    "Вернувшись обратно в нашу подсобку, мы снова принялись за работу."
    "В этот раз с учётом всех полученных ранее замечаний."

    stop ambience fadeout 2.5
    show bg int_editorial_sunset_wnfh with dissolve2
    play ambience ambience_cabin_evening fadein 2.5

    "Преследуя цель сделать свою работу как можно лучше, мы вовсе и не заметили, как уже наступил вечер."
    "Это означало, что скоро время ужина, отчего мы стали поторапливаться."
    "Разумеется, это сказалось на качестве последних строк, но, в остальном, работа должна была быть хорошей."
    "По крайней мере, мы на это надеялись."

    scene bg int_library_sunset_wnfh
    show kat normal pioneer at left
    show un normal pioneer at fleft
    show mz bukal pioneer glasses at right 
    with dissolve2

    "В этот раз, сдав статью, мы получили более мене неплохую оценку."

    mz "Что же, конечно ваша работа звёзд с неба не хватает, но[wp]"
    mz "Очень даже неплохо. Есть что подтянуть, но это уже можно людям показывать."
    mz "Думаю, ещё одна-две таких статьи, и вы уже набьёте руку."

    "Окончив свою мысль, Женя перевела пристальный взгляд на меня."

    mz "Кстати говоря, не могу не отметить тот факт, что с твоей помощью, Семён, качество текста возросло."
    mz "Отчего у меня закрались лёгкие подозрения, а точно ли у тебя тройка по русскому языку?"

    th "Вот же блин, опасный момент, она похоже не поняла, что это была шутка."

    me "Ну[wp] Вдвоём просто проще работать, вот и всё."
    me "В русском я вообще не бом-бом."

    "В ответ она только хмыкнула и сверкнула глазами."

    mz "А так, что ещё могу сказать[wp]"

    show mz fun pioneer glasses at right with dspr

    mz "Молодцы!"

    show kat smile pioneer at left
    show un smile2 pioneer at fleft
    with dspr

    "Нас охватила настоящая радость, что мы аж хором воскликнули «Ура-а!»."

    show mz normal pioneer glasses at right with dspr

    mz "Ладно, порадовались маленькому успеху, а теперь пора на ужин идти."

    "С хорошим настроением, мы покинули библиотеку."

    window hide dissolve
    jump d9_musclub_evening
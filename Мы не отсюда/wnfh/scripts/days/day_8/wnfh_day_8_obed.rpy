label d8_obed_me_alone_alt:
    $ wnfh_Data.FlagSet("d8_obed_me_alone", "alone_alt")
    window hide dissolve
    stop ambience fadeout 5.0
    scene bg ext_dining_hall_near_day
    with slide_right_blure_dissolve5
    play ambience ambience_camp_center_day fadein 5.0
    $ renpy.pause(1.0)
    window show dissolve

    "Вернувшись в лагерь, мы с Алисой разошлись по своим делам."
    "Она пошла к себе домой, вероятнее всего, делить добычу с Ульяной."
    "Я же, прикинув, что до обеда осталось всего ничего, пошёл к столовой."
    "Там, усевшись на лавочку, я стал ожидать начала великого жора."
    "Но до тех пор нужно было чем-то себя занять[wp]"
    
    th "Интересно, что же всё-таки они искали? Да ещё так близко к лагерю[wp]"
    th "С другой стороны, какая разница? Может, действительно, как говорила Алиса, нашли какой-нибудь условный уран и теперь хотят его подальше вывезти отсюда, чтобы детей не убило."
    th "Скорее всего, так и есть, ибо больше вариантов особо на ум и не приходит."
    th "Ладно, чёрт с ними. Главное, меня пусть не трогают."
    
    "Время шло предательски медленно."
    "Идти куда-то было лень, спать тоже не хотелось."
    
    th "Вот бы сейчас на меня свалилось какое-нибудь чудо[wp]"
    
    "Но, разумеется, никакого «чуда» на меня не свалилось."
    
    play sound sfx_dinner_horn_processed
    window hide dissolve
    stop ambience fadeout 2.0
    scene bg int_dining_hall_day with door_blure_dissolve2
    play ambience ambience_dining_hall_empty
    $ renpy.pause(1.0)
    stop ambience fadeout 2.0
    scene bg int_dining_hall_people_day with dissolve2
    play ambience ambience_dining_hall_full fadein 2.0
    $ renpy.pause(0.5)
    window show dissolve
    
    "Обед как обед: взял еду, нашёл место и сел. Вот и всё."
    "Даже из друзей ни с кем не пересёкся, но мне как-то всё равно было."

    th "Мечты сбываются, да? Сколько я уже хотел один поесть? Дня три?"
    th "То товарищи ко мне подсаживаются, то я к ним[wp]"

    "Обед я закончил в кратчайшие сроки."

    th "Но всего хорошего помаленьку."

    jump d8_posle_obeda

label d8_obed_me_alone:
    $ wnfh_Data.FlagSet("d8_obed_me_alone", "alone_canon")
    window hide dissolve
    scene bg ext_dining_hall_away_day with slide_up_blure_dissolve2
    $ renpy.pause(1.0)
    scene bg ext_dining_hall_near_day with dissolve
    $ renpy.pause(1.0)
    window show dissolve

    "Придя к столовой, я никого не увидел у входа."

    th "Однажды и я получу суперспособность оказываться у столовой сразу после призыва на поесть. Нужно только подождать[wp]"

    window hide dissolve
    stop ambience fadeout 2.0
    scene bg int_dining_hall_people_day with door_blure_dissolve2
    play ambience ambience_dining_hall_full fadein 2.0
    $ renpy.pause(0.5)
    window show dissolve
    
    "Обед прошёл вполне обыденно: взял еду, сел за стол и всё."
    "Даже ни с кем из товарищей по отряду не пересёкся, что удивительно. Впрочем, я и не пытался их искать."
    
    th "Да уж, невесело, однако[wp] Зато один поем, наконец."
    th "Может, даже вездесущая вожатая не будет меня тревожить."

    "И за время обеда меня действительно никто не потревожил. Такое не каждый день случается."
    "А это означает, что я спокойно, хоть и в быстром темпе, расправился со своим обедом и отправился к выходу."

    jump d8_posle_obeda

label d8_obed_me_dv:

    $ wnfh_Data.FlagSet("d8_obed_me_dv", True)
    window hide dissolve
    stop ambience fadeout 5.0
    scene bg ext_dining_hall_away_day 
    show dv normal pioneer2 at left
    with santa_barbara_in_blure_dissolve5
    play ambience ambience_camp_center_day fadein 5.0
    $ renpy.pause(0.5)
    window show dissolve

    "Вернулись в лагерь мы довольно быстро."
    "В конце концов, спускаться с горки, да ещё и с весомой долей адреналина в крови, гораздо проще."
    "И учитывая то, что примерно через десять минут должен был начаться обед, мы сразу пошли к столовой."

    show usw normal pioneer at right with dissolve
    play music music_list["went_fishing_caught_a_girl"] fadein 5.0

    "Однако, оказывается, здесь нас уже ждала Ульяна."
    
    show usw normal pioneer at right with dspr

    "Она оценила нас своим хитрым взглядом."
    "Было очевидно, что она уже явно что-то себе напридумывала, но виду старалась не подавать."

    usw "И где вы были?"

    show dv smile pioneer2 at left with dspr

    dv "По полю гуляли, клещей собирали."
    me "И яблоки."
    usw "Яблоки?"

    show usw dontlike pioneer at right with dspr

    "Ульяна довольно резко рассердилась."

    show dv guilty pioneer2 at left with dspr

    usw "Знала я, что не стоило тебе рассказывать!"

    "Её недовольный взгляд сверлил Алису."

    dv "Да ладно тебе, пару яблок всего взяла, кто узнает-то?"

    show usw grin pioneer at right with dspr

    usw "Никто, если я получу долю!"

    show dv smile pioneer2 at left with dspr

    dv "Так бы сразу."

    "Алиса было потянулась в свой «карман», но резко остановилась."

    show dv surprise pioneer2 at left with dspr

    dv "Ой, а яблок-то и нет[wp]"
    dv "Семён, а у тебя как?"

    show dv shy pioneer2 at left with dspr

    "Порывшись в карманах, я нашёл там одно единственное яблоко."

    th "Видать, все выпали, когда убегали."

    show usw upset pioneer at right with dspr

    usw "Не густо."
    me "Что ж, в таком случае[wp]"

    "Я подошёл к Ульяне и протянул ей красивое заливное яблоко."

    me "Оно твоё."

    $ wnfh_Data.AddLove_points({"usw":1})

    show usw laugh pioneer at right
    show dv normal pioneer2 at left
    with dspr

    usw "О, спасибочки! Будет чем подкрепиться после занятий спортом."
    me "С Алисой хотя бы поделись! Она, всё же, их добывала."

    show usw grin pioneer at right with dspr

    usw "Обязательно!"

    show usw normalsmile pioneer at right with dspr

    me "Ну что, когда там уже обед?"

    "Ульяна посмотрела на воображаемые часы."

    usw "Да вот с минуты на минуту начаться должен. Можем уже пойти занимать места."

    window hide dissolve
    stop ambience fadeout 3.5
    scene bg int_dining_hall_day
    show dv normal pioneer at left
    show usw normalsmile pioneer at right
    with dissolve2
    play ambience ambience_dining_hall_empty fadein 3.5
    $ renpy.pause(0.5)
    play sound sfx_dinner_horn_processed
    window show dissolve

    "Горн прозвучал, как только мы вошли в столовую."
    "Взяв по подносу, мы уселись у окошка."
    "Разумеется, меня посадили так, чтобы солнце слепило прямо в глаз, но спорить было бесполезно."

    stop ambience fadeout 1.0
    show bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 1.0

    "Спустя довольно короткий промежуток времени обеденный зал был уже битком заполнен пионерами."
    "И всё бы ничего, да вот только буквально напротив нас расположились никто иные, как Лена и Катя."

    th "Вот и думай: совпадение, судьба или они всё же специально?"

    "Я старался на них особо не зацикливаться, но всё же мимолётом успел заметить устремлённый на меня изучающий взгляд Лены."

    me "Вот так свезло[wp]"

    show usw normal pioneer at right
    show dv smile pioneer at left
    with dspr

    usw "Ты о чём?"

    "Алиса же тихонько хихикала."

    usw "А ты чего смеёшься?"

    "Ульяна непонимающе смотрела то на меня, то на Алису. Даже на себя посмотрела, видимо, чтобы удостовериться, не с неё ли смеются."

    show usw dontlike pioneer at right with dspr

    usw "Так, ну-ка выкладывайте!"
    me "Да ничего такого."

    show dv laugh pioneer at left with dspr

    dv "Просто Семён накосячил и теперь переживает, не сдала ли его одна девушка. Так, Семён?"
    me "Сдала, вероятнее всего."

    show usw grin pioneer at right with dspr

    usw "Та-а-ак, а с этого места поподробнее!"

    show dv normal pioneer at left with dspr

    "Алиса быстренько пересказала Ульяне весь сыр-бор. Не без преувеличений, разумеется, куда же без них."
    "Но, благо, сама по себе история была не настолько большая, чтобы её можно было извратить до неузнаваемости."

    show usw normal pioneer at right with dspr

    dv "[wp]Такие вот дела."
    usw "Вот оно что[wp]"

    show usw laugh pioneer at right with dspr

    usw "Ты точно чокнутый, Сёма!"

    show usw upset pioneer at right with dspr

    usw "Эх, такого друга потеряем сегодня. Жил без страха и умрёт без страха."
    me "Не надо меня хоронить раньше времени. Может, договорюсь ещё."

    show dv smile pioneer at left with dspr

    dv "О да, договариваться ты умеешь."

    show dv grin pioneer at left with dspr

    dv "Тебе напомнить, как ты «договорился» с Планшетиком, после чего она ваш клуб начала ещё сильнее прессовать?"
    dv "Тогда даже Ольге вмешаться пришлось, потому что Шура нажаловался."
    me "Ну бывают просчёты, но я учусь на своих ошибках."

    show dv laugh pioneer at left with dspr

    dv "Ну-ну!"

    "А тем временем еда медленно, но верно подошла к концу."
    "Даже чай был уже выпит, что я не сразу заметил."

    th "Да уж, иногда тяжело с таким аппетитом."

    me "Ох[wp] Что ж, приятно было побеседовать, но мне пора на заслуженный послеобеденный перерыв."
    dv "Пока-пока."

    if wnfh_Data.getChoice_result_number("d7_choice_n8") == 2:

        show usw dontlike pioneer at right with dspr

        usw "Эй, опять?! Я убирать за тобой не собираюсь!"
        me "За друзьями нужно ухаживать."

    "Я медленно пошёл в сторону выхода."

    jump d8_posle_obeda

label d8_obed_me_kat_un:
    $ wnfh_Data.FlagSet("d8_obed_me_kat_un", True)
    window hide dissolve
    show bg ext_dining_hall_away_day 
    show kat normal pioneer at left
    show un smile pioneer at right
    with slide_up_blure_dissolve2
    $ renpy.pause(1.0)
    show bg ext_dining_hall_near_day with dissolve
    $ renpy.pause(1.0)
    stop ambience fadeout 2.0
    scene bg int_dining_hall_people_day
    show kat normal pioneer at left
    show un smile pioneer at right
    with door_blure_dissolve2
    play ambience ambience_dining_hall_full fadein 2.0
    $ renpy.pause(0.5)
    window show dissolve

    th "Обед, обед, обед. Каждый день одна и та же рутина. Может, пора научиться жить чисто на солнечной энергии?"
    th "Ну а что? Буддистские монахи же так живут и не жалуются, значит, вкусно!"

    show un smile2 pioneer at right with dspr
    show kat smile pioneer at left with dspr

    un "Семён, не спи! Обед так пропустишь."
    me "А, да, точно[wp]"

    show un smile pioneer at right with dspr
    show kat normal pioneer at left with dspr

    "Забрав подносы с едой, мы сели за первый попавшийся свободный стол."
    $ renpy.notify("Тут должны быть подносы с хавчиком, но мне (Серёге) их лень ставить")

    "Будучи голодным как волк, я сразу же накинулся на свой обед."
    "Но, похоже, девушкам очень уж хотелось поболтать."

    kat "Слушай, Семён, а вот расскажи-ка мне[wp]"
    me "М?"

    show kat interested pioneer at left with dspr

    kat "Как же ты всё-таки ту карту потерял? И почему это так важно для вожатой?"

    "Я раздражённо фыркнул."

    me "Не терял я её, у меня карту Ульяна украла."
    me "Пол-лагеря за ней оббежал, пока не выяснилось, что она её уже где-то выкинула."
    me "И где эта самая карта, даже она не знает!"
    kat "Ха, занятно."

    show kat happy pioneer at left with dspr

    kat "Зато пока бегал, весь лагерь изучил."

    "Катя тихо похихикала."

    me "А что до вожатой[wp] Видимо, дело принципа, не знаю."
    
    "В наш диалог решила вклиниться Лена."

    un "Дело не только в принципе. Эти же карты другим сменам давать будут, а они им полезны, особенно младшим."    
    me "Ну, возможно."
    un "Не возможно, а так и есть."
    me "В любом случае."

    show kat smile pioneer at left with dspr

    "Я постарался полностью сконцентрироваться на обеде."
    "И, видимо, девочки решили последовать моему примеру, также уткнувшись в свои тарелки."

    # таймскип
    window hide dissolve
    $ renpy.pause(1.0)
    window show dissolve

    "Наконец, с обедом было закончено. Ну, мной — тарелки Лены и Кати всё ещё были полными."
    "Медленно и неуклюже я поднялся из-за стола."

    me "Ну-с, хорошо провели время, но мне пора на послеобеденный перерыв."
    me "Так что[wp] Увидимся, когда увидимся."

    kat_un "Пока!"

    "Девушки синхронно помахали мне, а я отправился на выход."

    jump d8_posle_obeda

label d8_obed_me_kat_mi:
    $ wnfh_Data.FlagSet("d8_obed_me_kat_mi", True)
    window hide dissolve
    scene bg ext_dining_hall_away_day
    show kat normal pioneer at left
    show mi normal pioneer at right
    with slide_up_blure_dissolve
    $ renpy.pause(1.0)
    show bg ext_dining_hall_near_day with dissolve
    $ renpy.pause(1.0)
    stop ambience fadeout 2.0
    scene bg int_dining_hall_people_day
    show mi normal pioneer at right
    show kat normal pioneer at left
    with door_blure_dissolve2
    play ambience ambience_dining_hall_full fadein 2.0
    $ renpy.pause(0.5)
    window show dissolve

    "Зайдя в столовую, я отработал стандартную, уже обкатанную схему."
    "Буфет, поднос, столик. Какая-то круговая порука[wp]"

    show chair_r at chair_move_out behind mi
    $ renpy.pause(0.3, hard=True)
    show mi normal pioneer at sit_down_right
    $ renpy.pause(1.0, hard=True)
    show chair_r at chair_move_in behind mi
    show right d8_breakfast_full tray spoon foods behind mid with dissolve

    "Катя и я завалились за столик."
    "Мику же аккуратно, даже с некоторой грацией, села за стол и стала потихонечку есть."
    show right d8_breakfast_full tray foods behind mid with dissolve
    "Что нельзя было сказать про меня, ведь за это время я уже умудрился изгваздаться."

    th "И как я только умудряюсь?"
    
    show kat grin pioneer with dspr
    
    kat "Семён, ты хрюша, в курсе?"
    
    "Катя с усмешкой указала взглядом на пятно на моей рубашке."
    "Я грустно посмотрел на него, а девочки тихонько засмеялись."
    
    show kat laugh 
    show mi laugh 
    with dspr 
    
    "Я попытался оттереть пятно рукой, но сделал только хуже, размазав его ещё сильнее. Девочки же от моих неудачных попыток засмеялись ещё громче."
    "Поняв, что в этой битве я проиграл, я грозно фыркнул и обиженно уткнулся в тарелку."
    
    show mid d8_breakfast_half tray foods with dissolve
    show kat smile 
    show mi normal 
    with dspr
    
    mi "Семён, ну не обижайся ты!"

    show left d8_breakfast_half tray foods with dissolve
    
    me "Да не обижаюсь я, просто[wp] Неприятно немного."
    
    show right d8_breakfast_half tray foods with dissolve
    show mi happy with dspr
    
    mi "Вот и славно, что не обижаешься."
    
    show mi normal
    show kat normal 
    with dspr
    
    "Мы все молча и спокойно продолжили есть."
    
    show left d8_breakfast_empty tray foods
    show right d8_breakfast_empty tray foods 
    with dissolve
    
    "Мику и Катя закончили, что странно, быстрее меня, при том что ел я довольно быстро."
    
    show kat normal pioneer at get_up
    show chair_l at chair_move_out
    $ renpy.pause(0.5, hard=True)
    show mi normal pioneer at get_up
    show chair_r at chair_move_out
    
    hide left
    hide right 
    with dissolve
    
    mi "Ладно, Семён, мы с Катей пойдём в музкружок. Ты к нам тоже заходи, может, даже вместе сыграем, я вот ещё ни разу не играла в трио!"
    kat "Ой, знаешь, Мику, мне только нужно будет заскочить к себе в домик. Буквально на десять минут, ладно?"
    mi "Конечно, я же не говорю, что нужно прям обязательно бежать в музкружок, позабыв обо всём остальном!"

    show kat smile with dspr

    kat "Спасибо тебе."
    mi "Ну так что, Семён, зайдёшь к нам?"
    me "Что ж, если дел других не будет, то, наверное, приду."
    mi "Отлично, тогда буду ждать вас обоих!"
    
    window hide dissolve
    show mi normal pioneer:
        ease_quart 4.0 xcenter 1.2
    show kat normal pioneer behind chair_r:
        ease_quart 5.0 xcenter 1.2
    
    $renpy.pause(2.0, hard=True)
    
    hide mi 
    hide kat 
    with dissolve
    window show dissolve
    
    "Девочки ушли, а я стал в ускоренном темпе доедать."
    
    show mid d8_breakfast_empty tray spoon foods with dissolve
    
    "И спустя минуту наконец-то прикончил свой обед."
    
    window hide dissolve
    scene bg int_dining_hall_people_day with dissolve2
    window show dissolve

    "Встав, я направился на выход из столовой."
    "И лишь ближе к выходу вспомнил про то пятно."
    "В грязной форме щеголять не очень хотелось, и я попросился на кухню отмыть рубашку в раковине."
    "Благо, сегодня настроение у наших поварих было хорошим, и они пустили меня."
    "Там я кое-как отмылся и наконец покинул столовую."
    
    jump d8_posle_obeda

label d8_obed_me_kat:
    $ wnfh_Data.FlagSet("d8_obed_me_kat", True)
    window hide
    scene bg ext_dining_hall_away_day with slide_up_blure_dissolve2
    $ renpy.pause(1.0)
    scene bg ext_dining_hall_near_day with dissolve
    $ renpy.pause(1.0)
    window show
    ## Обед
    "Пионеров на входе было немного, и мы с Катей быстренько прошмыгнули в столовую."
    
    window hide
    stop ambience fadeout 0.5
    scene bg int_dining_hall_day
    show kat normal pioneer at center
    with dnr_entrance
    play ambience ambience_dining_hall_empty fadein 3 
    window show

    "Внутри почти никого не было, лишь несколько человек сидели и обедали в гордом одиночестве."
    "Мы подошли к раздаче и, взяв подносы, пошли к моему любимому столику."
    
    window hide dissolve
    show chair_l behind kat 
    show chair_r behind mi
    show table
    show shakers
    with dissolve
    
    stop ambience fadeout 0.5
    show bg int_dining_hall_people_day with dissolve2
    play ambience ambience_dining_hall_full fadein 3
    
    show mid d8_breakfast_full tray spoon foods with dissolve
    show kat normal pioneer behind chair_r:
        xcenter -0.2
        ease_quart 4.0 xcenter 0.15
    
    $ renpy.pause(4.0, hard=True)
    show left d8_breakfast_full tray foods behind shakers with dissolve
    show chair_l at chair_move_out behind kat
    $ renpy.pause(0.7, hard=True)
    show kat normal pioneer at sit_down_left behind table
    $ renpy.pause(1.0, hard=True)
    show chair_l at chair_move_in behind kat
    $ renpy.pause(0.3, hard=True)
    window show dissolve
    
    "И как только мы заняли своё место, столовая тут же стала наполняться людьми."
    
    show mid d8_breakfast_full tray foods with dissolve
    
    me "Вовремя мы, однако."

    show kat confused pioneer at left with dspr 

    kat "М? Ты о чём?"
    me "Ты посмотри, сколько людей сразу завалилось. Мы бы не протолкнулись."

    show kat pockerface pioneer at left with dspr

    "Она вяло осмотрела вошедших, пожала плечами и вернулась к еде."

    me "Похоже, голод тебя волнует куда больше. Понимаю."

    "Усмехнувшись, я также принялся за обед."

    show kat sad pioneer at left with dspr

    kat "Да не только[wp]"
    me "А что ещё?"

    show kat smile pioneer at left with dspr

    kat "Да так, волнуюсь немного по поводу знакомств с новыми людьми."
    kat "Как будут относиться ко мне, примут ли в свой коллектив[wp]"

    "Я покачал головой."

    me "Не бери в голову."

    show kat thinking pioneer at left with dspr

    kat "Легко сказать[wp]"
    me "И легко сделать."
    me "Я понимаю, о чём ты, сам через это прошёл здесь. И хочу сказать, что всё довольно-таки просто."
    me "А стресс лучше не заедать, потолстеешь."

    show kat obida pioneer at left with dspr

    "Последние слова вырвались сами собой, и я даже как-то не подумал, что мог обидеть девчонку."
    "И, судя по её выражению лица, всё же я её задел."

    kat "Ничё я не потолстею!"
    me "Виноват, само как-то вырвалось."

    show kat upset pioneer at left with dspr

    "Она грустно вздохнула и стала водить ложкой по тарелке."

    window hide dissolve
    call screen wnfh_choice(
        ["kat", "Приободрить", "Может, старая добрая прогулка поможет?", "d8_obed_me_kat_1", {"kat":1}],
        ["neutral", "Промолчать", "Иногда лучше оставить человека в покое", "d8_obed_me_kat_2"],
        ["d8_choice_n9", "Семён думает, как бы приободрить Катю"]
        ) with sphere_blure_dissolve2
    
label d8_obed_me_kat_1:

    window show dissolve

    th "Наверное, стоит как-то поднять ей настроение. Но учитывая ограниченность моих ресурсов, остаётся только звать на прогулку."
    th "Хотя, возможно, она уже устала от прогулок, после бегунка-то."
    th "Впрочем, нефиг гадать — нужно спросить!"

    me "Слушай, может, прогуляемся после обеда? Думаю, прогулка хорошо поможет отвлечься."

    show kat thinking pioneer at left with dspr

    "После моего предложения Катя ненадолго задумалась." 

    kat "После обеда, пожалуй, нет[wp] Всё же я думала после еды немного отдохнуть, а потом к Мику в клуб сходить."

    show kat happy pioneer at left with dspr

    kat "Но вот, скажем, после ужина вполне можно пройтись!"
    me "Отлично, так даже лучше."

    show kat joy pioneer at left with dspr

    kat "Вот и славненько."

    show kat normal pioneer at left with dspr

    kat "А теперь нам бы с обедом закончить."
    me "Это верно подмечено!"

    "С удвоенной силой мы оба принялись за еду."

    # таймскип
    window hide dissolve
    $ renpy.pause(1.0)
    window show dissolve

    "И за какие-то жалкие пять минут еда была уничтожена."
    "Катя облокотилась на спинку стула."
    "Я же, кое-как, но всё же встал из-за стола."

    me "Что ж, ты как хочешь, а я, пожалуй, пойду домой[wp]"
    kat "Ага, до скорой встречи!"

    "Помахав на прощание, я отправился на выход из столовой."

    jump d8_posle_obeda

label d8_obed_me_kat_2:

    window show dissolve

    th "Стресс это, конечно, плохо, но это личное дело каждого."
    th "А я своими потугами могу только хуже сделать. Или она вообще начнёт считать, что я так к ней из жалости."
    th "Поэтому лучше оставить эдакий статус-кво."

    "Я полностью сосредоточился на еде."
    "Через какое-то время, явно без особого энтузиазма, за еду принялась и Катя."

    # таймскип
    window hide dissolve
    $ renpy.pause(1.0)
    window show dissolve

    "Спустя пару минут моя пайка была уничтожена, тогда как моя подруга всё ещё возилась со своей."
    "Медленно встав из-за стола, я потянулся, похрустев позвоночником."

    me "Ну что ж, пойду-ка я[wp]"
    kat "Угу[wp]"
    me "Покеда."
    kat "Пока[wp]"

    jump d8_posle_obeda
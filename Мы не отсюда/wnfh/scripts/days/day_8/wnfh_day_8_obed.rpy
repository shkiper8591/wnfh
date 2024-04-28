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
    "Она пошла к себе домой, вероятнее всего делится яблоками с Ульяной."
    "А я же, прикинув, что до обеда остаётся не так уж и много, пошел к столовой."
    "Там, усевшись на лавочку, я стал ожидать начала великого жора."
    "Но до тех пор, нужно было себя чем-то занять[wp]"
    
    th "Интересно, что же всё-таки искали те люди в хим защите? Да и ещё так рядом с лагерем[wp]"
    th "С другой стороны, какая разница? Может действительно, как говорила Алиса, нашли какой-нибудь условный уран, и теперь хотят его подальше вывезти отсюда, чтобы детей не убило."
    th "Скорее всего так и есть, ибо больше вариантов у меня особо и нет на уме[wp]"
    th "Ладно, чёрт с ними, главное пусть это не касается меня."
    
    "Время же предательски медленно шло."
    "Идти куда-то было лень, спать тоже не хотелось."
    
    th "Вот бы сейчас на меня свалилось какой-нибудь чудо."
    
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
    "Даже из друзей ни с кем не пересёкся, но мне как-то всё равно было на это."

    th "Мечты сбываются, да? Сколько я уже хотел один поесть? Дня три?"
    th "То подсаживаются постоянно товарищи моделисты, то подсаживаюсь я[wp]"

    "Мой обед же закончился в короткие сроки."

    th "Но всего хорошего по маленьку[wp]"

    jump d8_posle_obeda

label d8_obed_me_alone:
    $ wnfh_Data.FlagSet("d8_obed_me_alone", "alone_canon")
    window hide dissolve
    scene bg ext_dining_hall_away_day with slide_up_blure_dissolve2
    $ renpy.pause(1.0)
    scene bg ext_dining_hall_near_day with dissolve
    $ renpy.pause(1.0)
    window show dissolve

    "Придя к столовой, у входа никого уже не было."

    th "Однажды, и я получу суперспособность оказываться у столовой сразу после призыва на поесть. Нужно только подождать[wp]"

    window hide dissolve
    stop ambience fadeout 2.0
    scene bg int_dining_hall_people_day with door_blure_dissolve2
    play ambience ambience_dining_hall_full fadein 2.0
    $ renpy.pause(0.5)
    window show dissolve
    
    "Обед проходил без особого интереса: взял еду, сел за стол и всё."
    "Даже ни с кем из товарищей по отряду не пересёкся, что удивительно. В прочем, я и не пытался их искать."
    
    th "Да уж, не весело, однако[wp] Зато один поем наконец."
    th "Может ещё даже вездесущая вожатая не будет тревожить."

    "И за время обеда меня действительно никто не потревожил. Такое не каждый день случается."
    "А это означало, что я спокойно и в быстром темпе расправился со своим обедом и отправился к выходу."

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

    "Вернулись в лагерь мы довольно скоро."
    "В конце-концов, спускаться с горки, да и ещё полной адреналина крови, гораздо проще."
    "И учитывая, что, примерно, через десять минут должен был начаться обед, мы сразу пришли к столовой."

    show usw normal pioneer at right with dissolve
    play music music_list["went_fishing_caught_a_girl"] fadein 5.0

    "Однако, оказывается, нас здесь уже ждала Ульяна."
    
    show usw normal pioneer at right with dspr

    "Она оценила нас своим хитрым взглядом."
    "Было слишком очевидно, что она уже явно что-то надумала себе в уме, но виду не показывала."

    usw "Где вы были?"

    show dv laugh pioneer2 at left with dspr

    dv "По полю гуляли, клещей собирали."
    me "И яблоки тоже."

    show usw normal pioneer at right with dspr

    usw "Яблоки?"

    show usw dontlike pioneer at right with dspr

    "Резко Ульяна стала довольно сердитой."

    show dv guilty pioneer2 at left with dspr

    usw "Знала я, что не стоило доверять эту информацию тебе."

    "Её недовольный взгляд сверлил Алису."

    dv "Да ладно тебе, пару яблок всего взяла, кто узнает?"

    show usw grin pioneer at right with dspr

    usw "Никто, если я получу долю[wp]"

    show dv smile pioneer2 at left with dspr

    dv "Так бы сразу."

    "Алиса было потянулась в свой «карман» для яблок, но резко остановился."

    show dv surprise pioneer2 at left with dspr

    dv "Ой, а яблок-то и нет."

    show dv scared pioneer2 at left with dspr

    dv "Семён, а у тебя что?"

    show dv shy pioneer2 at left with dspr

    "Порывшись в своих карманах и нашёл там одно единственное яблоко."

    th "Видать все выпали когда убегали."

    show usw upset pioneer at right with dspr

    usw "Не густо у вас всё."
    me "Что ж, в таком случае[wp]"

    "Я подошёл к Ульяне и протянул ей красивое заливное яблоко."

    me "Оно твоё."

    $ wnfh_Data.AddLove_points({"usw":1})

    show usw laugh pioneer at right
    show dv normal pioneer2 at left
    with dspr

    usw "О, спасибочки! Будет чем подкрепиться после занятий спортом."
    me "С Алисой хотя бы поделись, она всё же их добывала."

    show usw grin pioneer at right with dspr

    usw "Обязательно!"

    show usw normalsmile pioneer at right with dspr

    me "Ну что, когда там уже обед?"

    "Ульяна посмотрела на воображаемые часы."

    usw "Да вот с минуты на минуту начаться должен, можем уже пойти занимать места."

    window hide dissolve
    stop ambience fadeout 3.5
    scene bg int_dining_hall_empty_day
    show dv normal pioneer at left
    show usw normalsmile pioneer at right
    with dissolve2
    play ambience ambience_dining_hall_empty fadein 3.5
    $ renpy.pause(0.5)
    play sound sfx_dinner_horn_processed
    window show dissolve

    "Горн прозвучал как только мы вошли в столовую."
    "Взяв по подносу, мы уселись у окошка."
    "Разумеется, меня посадили так, чтобы солнце слепило прямо в глаз, но спорить было бесполезно."

    stop ambience fadeout 1.0
    show bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 1.0

    "В течении короткого промежутка времени, обеденный зал уже был полон пионерами."
    "И как бы, всё бы ничего, но буквально напротив нас расположились никто иные как Лена и Катя."

    th "Вот и думай, совпадение, судьба или же специально?"

    "Я старался на них особо не зацикливаться, но всё же мимолётом успел заметить, как Лена изучала меня своим взглядом."

    me "Вот так свезло[wp]"

    show usw normal pioneer at right
    show dv smile pioneer at left
    with dspr

    usw "Ты о чём?"

    "Алиса же тихонько хихикала."

    usw "А ты чего смеёшься?"

    "Ульяна непонимающе смотрела то на меня, то на Алису. Даже на себя посмотрела, видимо, чтобы удостоверится не с неё ли смеются."

    show usw dontlike pioneer at right with dspr

    usw "А ну-ка выкладывайте давайте!"
    me "Да ничего такого."

    show dv laugh pioneer at left with dspr

    dv "Просто Семён накосячил, и теперь переживает, не сдала ли его одна девушка, не так ли?"
    me "Сдала вероятнее всего."

    show usw grin pioneer at right with dspr

    usw "Так, а с этого места поподробнее!"

    show dv normal pioneer at left with dspr

    "Алиса быстренько пересказала Ульяне весь сырбор. Конечно же с преувеличениями, куда же без них."
    "Но, благо сама по себе история была небольшая, чтобы извратить её до неузнаваемости."

    show usw normal pioneer at right with dspr

    dv "[wp]Такие вот дела."
    usw "Вот оно что[wp]"

    show usw laugh pioneer at right with dspr

    usw "Ты точно чокнутый, Сёма!"

    show usw upset pioneer at right with dspr

    usw "Эх, такого друга потеряем сегодня. Жил без страха и умрёт без страха."
    me "Не надо меня уже хоронить. Может договорюсь ещё."
    dv "О да, договариваться ты умеешь."

    "С ноткой сарказма проговорила она."

    show dv grin pioneer at left with dspr

    dv "Тебе напомнить, как ты договорился с Планшетиком, после чего она ваш клуб начала ещё сильнее прессовать?"
    dv "Тогда даже вроде Ольге вмешаться пришлось, потому-что Шура нажаловался."
    me "Ну бывают просчёты, но я учусь на своих ошибках."

    show dv laugh pioneer at left with dspr

    dv "Ну-ну!"

    "А тем временем, еда, медленно но верно, подошла к своему концу."
    "Даже чай был уже выпит, что я не сразу заметил."

    th "Да уж, иногда тяжело с таким аппетитом."

    me "Ох, что ж, приятно было побеседовать, но мне пора на заслуженный послеобеденный перерыв."
    dv "Пока-пока."

    if wnfh_Data.getChoice_result_number("d7_choice_n2") == 2:

        usw "Эй, опять?! Я убирать за тобой не собираюсь!"
        me "За друзьями нужно ухаживать."

        "Усмехнувшись сказал я."

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
    # мне кароче нахуй в падлу эмоции менять им, пусть кто-нибудь другой этим займётся, заранее спасибо.
    $ renpy.notify("На протяжении всей дальнейшей сцены должны меняться эмоции, но мне лень этим заниматься")

    th "Обед, обед, обед. Каждый день одна и та же рутина. Может пора научиться питаться солнцем?"
    th "Ну а что? Буддистские монахи же так живут и не жалуются, значит вкусно!"

    un "Семён, не спи! Обед так упустишь."
    me "А, да, точно[wp]"

    "Забрав подносы с едой, мы сели за первый попавшийся свободный стол."
    $ renpy.notify("Тут должны быть подносы с хавчиком, но мне (Серёге) их лень ставить")

    "Усевшись за стол, я, будучи очень голодным, сразу же уткнулся в свой обед."
    "Но, похоже, у моих подруг было дикое желание поболтать."

    kat "Слушай, Семён, а вот расскажи-ка мне[wp]"
    me "М?"
    kat "Как же ты всё-таки карту потерял, и почему это так важно для вожатой?"

    "Я раздражённо фыркнул."

    me "Не терял я её, у меня карту Ульяна украла."
    me "Пол лагеря за ней оббежал, пока не выяснилось, что она её уже где-то выкинула."
    me "И где эта самая карта даже она не знает."
    kat "Ха, занятно."
    kat "Зато, пока бегал весь лагерь изучил."

    "Катя тихо похихикала."

    me "А что до вожатой, видимо, дело принципа, не знаю."
    
    "В наш диалог решила вклиниться Лена."

    un "Дело не только в принципе. Эти же карты другим сменам давать будут, а они им полезны, особенно младшим."    
    me "Ну, возможно."
    un "Не возможно, а так и есть."
    me "В любом случае."

    "Я постарался полностью сконцентрироваться на обеде."
    "И, видимо, девочки решили последовать моему примеру, также углубившись в свои тарелки."

    # таймскип
    window hide dissolve
    $ renpy.pause(1.0)
    window show dissolve

    "Наконец, с обедом было закончено. И закончил я куда раньше, чем мои подруги."
    "Медленно и неуклюже я поднялся из-за стола."

    me "Ну-с, хорошо провели время, но мне пора на послеобеденный перерыв."
    me "Так что[wp] Увидимся когда увидимся."

    kat_un_d "Пока!"

    "Синхронно сказали они и помахали мне, а я отправился на выход."

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

    "Зайдя в столовую, всё было сделано по стандартной, уже отработанной схеме."
    "Буфет, поднос, столик. Какая-то, круговая порука[wp]"

    show chair_r at chair_move_out behind mi
    $ renpy.pause(0.3, hard=True)
    show mi normal pioneer at sit_down_right
    $ renpy.pause(1.0, hard=True)
    show chair_r at chair_move_in behind mi
    show right d8_breakfast_full tray spoon foods behind mid with dissolve

    "Катя и я завалились за столик."
    "Мику же аккуратно, даже с некоторой грацией села за стол, и стала потихонечку есть."
    show right d8_breakfast_full tray foods behind mid with dissolve
    "Что нельзя было сказать про меня, ведь за это время, я уже успел немного испачкать форму едой."

    th "И как только я умудряюсь?"
    
    show kat grin pioneer with dspr
    
    kat "Семён, ты хрюша, в курсе?"
    
    "Насмешливо сказала Катя, указывая взглядом на пятно на моей форме."
    "Я грустно посмотрел на пятно, а девочки тихонько засмеялись."
    
    show kat laugh 
    show mi laugh 
    with dspr 
    
    "Я попытался оттереть пятно рукой, но сделал только хуже, размазав его ещё сильнее, а от моих неудачных попыток девочки ещё сильнее засмеялись."
    "Поняв, что ничего не получится, я грозно фыркнул и обиженно уткнулся в тарелку."
    
    show mid d8_breakfast_half tray foods with dissolve
    show kat smile 
    show mi normal 
    with dspr
    
    mi "Семён, ну не обижайся ты!"

    show left d8_breakfast_half tray foods with dissolve
    
    me "Да не обижаюсь я, просто неприятно немного."
    
    show right d8_breakfast_half tray foods with dissolve
    show mi happy with dspr
    
    mi "Вот и славно, что не обижаешься."
    
    show mi normal
    show kat normal 
    with dspr
    
    "Мы все уткнулись обратно в свои тарелки."
    
    show left d8_breakfast_empty tray foods
    show right d8_breakfast_empty tray foods 
    with dissolve
    
    "Мику и Катя закончили на удивление быстрее меня, при том, что ел я довольно быстро."
    
    show kat normal pioneer at get_up
    show chair_l at chair_move_out
    $ renpy.pause(0.5, hard=True)
    show mi normal pioneer at get_up
    show chair_r at chair_move_out
    
    hide left
    hide right 
    with dissolve
    
    mi "Ладно, Семён, мы с Катей пошли в муз кружок. Ты к нам тоже заходи, может даже вместе сыграем, я вот ещё ни разу не играла в трио!"
    me "Что ж, постараюсь зайти к вам, если дел не будет других."
    
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
    
    "Девочки ушли, а я, стал в ускоренном темпе доедать."
    
    show mid d8_breakfast_empty tray spoon foods with dissolve
    
    "И спустя минуту наконец-то прикончил свой обед."
    
    window hide dissolve
    scene bg int_dining_hall_people_day with dissolve2
    window show dissolve

    "Встав я направился на выход из столовой."
    "И только лишь ближе к выходу, вспомнил про пятно на моей форме."
    "В грязной форме щеголять не очень хотелось и я попросился на кухню отмыть пятно в раковине."
    "Благо, сегодня поварихи не были злыми и пустили меня."
    "Там я кое-как отмыл пятно, и наконец покинул столовую."
    
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
    "Возле столовой было немного пионеров, и я с Катей быстренько прошмыгнули в столовую."
    
    window hide
    stop ambience fadeout 0.5
    scene bg int_dining_hall_day
    show kat normal pioneer at center
    with dnr_entrance
    play ambience ambience_dining_hall_empty fadein 3 
    window show

    "Внутри было почти пусто, лишь пару человек сидели и обедали в гордом одиночестве."
    "Мы подошли к раздаче, и взяв подносы пошли к моему любимому столику."
    
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
    
    "И как только мы заняли своё место, столовая тут же стала наполнятся людьми."
    
    show mid d8_breakfast_full tray foods with dissolve
    
    me "Вовремя мы однако."

    show kat confused pioneer at center with dspr 

    kat "М, ты о чём?"
    me "Ты посмотри сколько людей сюда завалилось, мы бы не протолкнулись."

    show kat pockerface pioneer at center with dspr

    "Она вяло осмотрела вошедших людей, пожала плечами и вернулась к еде."

    me "Похоже, голод тебя волнует куда больше, понимаю."

    "Усмехнувшись, я также принялся за обед."

    show kat sad pioneer at center with dspr

    kat "Голод и стресс."
    me "Стресс?"

    show kat smile pioneer at center with dspr

    kat "Да так, волнуюсь немного по поводу знакомств с новыми людьми."
    kat "Как они примут меня в свой коллектив, как будут относится ко мне."

    "Я покачал головой."

    me "Не бери в голову."

    show kat thinking pioneer at center with dspr

    kat "Легко сказать[wp]"
    me "И легко сделать."
    me "Я понимаю о чём ты, через такое же прошёл здесь. И хочу сказать, что это довольно всё-таки просто."

    show kat obida pioneer at center with dspr

    me "А стресс лучше незаедать, потолстеешь."

    "Последние слова сами собой вырвались, и я даже как не подумал, что мог бы обидеть девчонку."
    "И, судя по её выражению лица, всё же немного я её задел."

    kat "Ничё я не потолстею!"
    me "Виноват, само как-то вырвалось."

    show kat upset pioneer at center with dspr

    "Она по грустному вздохнула и стала водить ложкой в еде."

    window hide dissolve
    call screen wnfh_choice(
        ["kat", "Преободрить", "Может старая добрая прогулка поможет?", "d8_obed_me_kat_1", {"kat":1}],
        ["neutral", "Лучше не тревожить", "Иногда лучше оставить человека на едине", "d8_obed_me_kat_2", {None}],
        ["d8_choice_n9", "Семён думает как бы Преободрить Катю"]
        ) with sphere_blure_dissolve2

label d8_obed_me_kat_1:

    window show dissolve

    th "Наверное, стоит как-то поднять настроение ей. Но учитывая ограниченность моих ресурсов, тут только остаётся звать на прогулку."
    th "Хотя, возможно она устала от прогулок после бегунка-то."
    th "В прочем, нефиг гадать, а нужно спрашивать!"

    me "Слушай, может мы прогуляемся после обеда? Думаю, прогулка хорошо поможет отвлечься от стресса."

    show kat thinking pioneer at center with dspr

    "После моего предложения, Катя надолго задумалась." 

    kat "После обеда, пожалуй нет[wp] Всё же я думала после еды немного отдохнуть, а потом к Мику сходить в клуб."

    show kat happy pioneer at center with dspr

    kat "Но вот вечером, скажем, после ужина, вполне можно походить!"
    me "Отлично, так даже лучше."

    show kat joy pioneer at center with dspr

    kat "Вот и славненько."

    show kat normal pioneer at center with dspr

    kat "А теперь, нам бы с обедом закончить[wp]"
    me "Это верно подмечено!"

    "С удвоенной силой, мы оба принялись за еду."

    # таймскип
    window hide dissolve
    $ renpy.pause(1.0)
    window show dissolve

    "И всего-то за пять минут, еда была уничтожена."
    "Катя облокотилась на спинку стула."
    "Я же, кое-как, но всё же встал из-за стола."

    me "Что ж, ты как хочешь, а я пожалуй пойду домой[wp]"
    kat "Ага, пока, и до скорой встречи!"

    "Помахав на прощание, я отправился на выход из столовой."

    jump d8_posle_obeda

label d8_obed_me_kat_2:

    window show dissolve

    th "Стресс это конечно плохо, но это личное дело каждого."
    th "А я своими потугами могу только хуже сделать, или она вообще начнёт считать, что я так к ней из жалости."
    th "Поэтому, лучше оставить этакий статус к-во."

    "Я полностью погрузился в свою еду."
    "Через какое-то время, явно без особого энтузиазма, за еду принялась и Катя."

    # таймскип
    window hide dissolve
    $ renpy.pause(1.0)
    window show dissolve

    "Спустя пару минут, моя пайка была уничтожена. Когда как моя подруга всё ещё возилась со своей."
    "Медленно встав из-за стола, я потянулся, похрустев позвоночником."

    me "Ну что ж, пойду-ка я[wp]"
    kat "Угу[wp]"
    me "Покеда."
    kat "Пока[wp]"

    jump d8_posle_obeda
label d8_obed_me_alone_alt:

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

    $ wnfh_Data.AddLove_points({"usw"}:1)

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

    "To be continued!"

    jump d8_posle_obeda

label d8_obed_me_kat_un:

    window hide dissolve
    show bg ext_dining_hall_away_day 
    show kat normal pioneer at left
    show un smile pioneer at right
    with slide_up_blure_dissolve2
    $ renpy.pause(1.0)
    show bg ext_dining_hall_near_day
    with dissolve
    $ renpy.pause(1.0)
    window show dissolve

    "placeholder"

    jump d8_obed_me_kat_mi

label d8_obed_me_kat_mi:

    window hide
    scene bg ext_dining_hall_away_day with slide_up_blure_dissolve2
    $ renpy.pause(1.0)
    scene bg ext_dining_hall_near_day with dissolve
    $ renpy.pause(1.0)
    window show

    show chair_r at chair_move_out behind mi
    $ renpy.pause(0.3, hard=True)
    show mi normal pioneer at sit_down_right
    $ renpy.pause(1.0, hard=True)
    show chair_r at chair_move_in behind mi
    show right d8_breakfast_full tray spoon foods behind mid with dissolve
    
    "Мику аккуратно, даже с некоторой грацией села за стол, и стала аккуратно есть."
    show right d8_breakfast_full tray foods behind mid with dissolve
    "Что нельзя было сказать про меня, ведь за это время, я уже успел немного испачкать форму едой."
    
    show kat grin with dspr
    
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
    
    mi "Сенечка, ну не обижайся ты!"
    
    show mi shy with dspr
    show left d8_breakfast_half tray foods with dissolve
    
    mi "Ой, то есть Семён."
    
    "Я медленно поднял взгляд на Мику, и вопросительно посмотрел на нее и краем глаза заметил, как недалеко сидящая Лена, сверлит презрительным взглядом Мику."
    # un "Тоби пи@да!"
    "Тут же я перевёл взгляд уже на Лену, от чего та вся засмущалась и вернулась обратно к еде."
    
    th "Ну и ну, то Сёмочка, то теперь вот некий Сенечка. {w}Ещё бы Семечкой обозвали, во хохма-то будет!"
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
    
    mi "Ладно Семен, мы с Катей пошли в муз кружок. Ты к нам тоже заходи, может даже вместе сыграем, я вот ещё ни разу не играла в трио!"
    me "Обязательно зайду."
    
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
    
    stop ambience fadeout 3.5
    scene bg ext_dining_hall_near_day with dissolve2
    play ambience ambience_camp_center_day fadein 3.5

    "placeholder"

    jump d8_male_clubs_day

label d8_obed_me_kat:
    ### НАДО ПЕРЕДЕЛАТЬ!!!!!!! СЕРГЕЙ НЕ ЗАБУДЬ ДЫРЯВАЯ ТЫ ГАЛАВА!!!!!!!
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
    scene bg int_dining_hall_day with dnr_entrance
    play ambience ambience_dining_hall_empty fadein 3 
    window show

    "Внутри было почти пусто, лишь пару человек сидели и обедали в гордом одиночестве."
    "Мы подошли к раздаче, и взяв подносы пошли к моему любимому столику."
    
    window hide
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
    window show
    
    "И как только мы заняли своё место, столовая тут же стала наполнятся людьми."
    
    show mi normal pioneer behind chair_r:
        xcenter 1.4
        ease_quart 5.0 xcenter 0.8
    
    show mid d8_breakfast_full tray foods with dissolve
    
    "А ещё спустя минуту, к нам подошла Мику."
    
    mi "Можно к вам сесть, а то я вроде старалась раньше закончить, чтобы успеть место занять, а по итогу опять пришла одна из самых последних."
    
    show kat smile with dspr
    
    kat "Да конечно, садись."
    mi "Спасибо!"
    
    "placeholder"
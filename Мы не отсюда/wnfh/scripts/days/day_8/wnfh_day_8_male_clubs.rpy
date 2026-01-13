label d8_male_clubs:

    stop ambience fadeout 2.0
    scene bg ext_admin_day_wnfh with santa_barbara_in_blure_dissolve2
    play ambience ambience_camp_center_day fadein 2.0
    $ renpy.pause(0.3)
    window show dissolve

    "Мы вышли из здания администрации, Катя помахала мне на прощание и ушла в сторону музклуба."
    "Как только она скрылась из виду, я сел на лавочку."
    "Дел, естественно, у меня никаких не было. Но не сидеть же мне без дела, верно?"

    th "Не то чтобы я прям хотел чем-то заняться, но и просто так шататься до ужина туда-сюда как-то не хочется."

    "И тут меня осенило."

    th "Если я хочу чем-то заняться, то мне к пацанам. У них всегда найдётся работёнка."

    $ wnfh_set_slot_data(chapter = 1, game_date = "24-07-1989", scene = "Рабочий день с парнями")
    window hide dissolve
    scene bg ext_clubs_day with dissolve2
    $ renpy.pause(0.3)
    stop ambience fadeout 2.0
    scene bg int_clubs_male_day
    show sv angry pioneer glasses tablet at right
    show sh normal pioneer at cleft
    show el normal pioneer at fleft
    with slide_right_blure_dissolve2
    play sound sfx_open_door_clubs
    play ambience ambience_clubs_inside_day fadein 2.0
    play music music_list["eat_some_trouble"] fadein 5.0
    $ renpy.notify("Музыка на фоне очень условная. В идеале, тут должна стоять тема Светы, либо же что-то бодрое.")
    $ renpy.pause(0.3)
    window show dissolve

    "И, похоже, чуйка меня не подвела — в клубах снова была Света. Она что-то на повышенных тонах высказывала моим товарищам."

    sv "[wp]Значит, найдите Семёна как можно скорее! Нам нужно всё успеть к завтрашнему дню!"
    sh "А вот и он."

    "Шурик кивнул в мою сторону. Света медленно повернулась ко мне."

    sv "Вспомнишь лучик[wp]"

    show sv happy pioneer glasses tablet at right with dspr

    sv "Ну что ж, раз вы все собрались[wp]"

    show sv angry pioneer glasses tablet at right with dspr

    sv "То бегом в библиотеку! Давайте, ать-два, ать-два!"

    hide sv with dissolve

    "Строевым шагом Света покинула помещение клуба."
    "Я же посмотрел на своих товарищей."

    me "И в чём сыр-бор?"
    sh "Да вот, сказано нам идти убираться в библиотеке."
    el "В подсобке, если быть точнее."
    me "А они сами не могут?"

    show sh normal pioneer at center with dspr

    "Шурик прошёл в сторону выхода."

    sh "Не знаю, но со слов Светки, там нужна грубая мужская сила."
    el "А ещё она говорит, что там всё завалено."

    "Я глубоко вздохнул."

    me "Знаете, я шёл сюда за делом. Но не на такое дело я надеялся."

    hide el 
    hide sh
    with dspr

    "Парни слегка усмехнулись и покинули помещение. Разумеется, я последовал за ними."

    window hide dissolve
    stop music fadeout 5.0
    stop ambience fadeout 2.0
    scene bg ext_clubs_day
    show sv angry pioneer glasses tablet at right
    show sh normal pioneer at cleft
    show el normal pioneer at fleft
    with dissolve2
    play ambience ambience_camp_center_day fadein 2.0
    $ renpy.pause(0.3)
    window show dissolve

    sv "Как-то вы медленно."
    sv "Давайте, раз-два, раз-два."

    show sv angry pioneer glasses tablet:
        ease 1.0 xcenter 1.5

    "Света продолжила идти строевым шагом в сторону библиотеки."
    "При этом она запевала какую-то строевую песню, но я особо не вслушивался."
    "Мы же нехотя плелись за ней."

    me "А по какому поводу нас вообще запрягли убираться в библиотеке?"
    el "Женя предложила организовать клуб журналистики в подсобке."
    sh "Да, а вожатая обеими руками поддержала эту идею."
    sh "Честно, я не особо понимаю, кого она туда набирать собирается."
    sv "Так, что там за разговоры в строю?!"

    show bg ext_lenin_square_day_wnfh with dissolve

    "Выйдя на площадь, наш конвой оказался в центре всеобщего внимания."
    "Разные пионеры, включая пару знакомых, среди которых Славя и Ульяна, глазели на нас."
    "Девочки даже помахали нам. Я в ответ им тоже вяло помахал."

    th "Скорее бы всё это уже закончилось[wp]"

    show bg ext_library_day with dissolve

    "Наконец мы дошли до библиотеки."

    window hide dissolve
    stop ambience fadeout 2.0
    scene bg int_library_day
    show el normal pioneer at fleft
    show sh normal pioneer at left
    show sv angry pioneer glasses tablet at center
    show mz normal pioneer glasses at right
    with sphere_blure_dissolve2
    play ambience ambience_library_day fadein 2.0
    $ renpy.pause(0.2)
    window show dissolve

    "Евгения уже ожидала нас внутри."

    mz "Ого, как вас много."

    show sv happy pioneer glasses tablet at center with dspr

    sv "Личный состав клуба авиамоделирования доставлен в целости и сохранности!"

    show mz sceptic pioneer glasses at right with dspr

    mz "Э-э, спасибо[wp] Думаю, ты можешь идти."

    show sv angry_smile pioneer glasses tablet at center with dspr

    sv "Идти? Я пойду, когда увижу чистую подсобку."
    sv "А за этими товарищами нужен глаз да глаз!"

    show mz bukal pioneer glasses at right with dspr

    mz "Думаю, я и сама могу с этим справиться."
    sv "Ты так думаешь или так положено думать?"

    show mz angry pioneer glasses at right with dspr

    "Женя раздражённо фыркнула."

    mz "Так, ребят, идите в подсобку пока и потихоньку разгребайте там всё."
    mz "Мне тут надо {i}уладить один вопрос{/i}."

    "Без лишних вопросов мы все направились в указанном нам направлении."

    hide sv
    hide mz
    show el normal pioneer at left 
    show sh normal pioneer at right
    with dissolve

    "Пройдя в заднюю часть библиотеки, я остановился перед дверью в подсобку с целью оглядеть всё вокруг."

    sh "Почему встали?"
    me "Да вот думаю, куда будем весь мусор сгребать пока."
    el "Так можно же в окно выкидывать."

    "Предложение Серёги звучало очень даже разумно."

    sh "А если там что-то большое?"
    me "Сломаем. Это же мусор, всё равно."
    sh "Справедливо."
    el "Только чем ломать будем? Руками?"
    me "Получается так."
    sh "Ну, может, у Жени найдётся какой-нибудь инструмент."
    sh "Ладно, это всё потом, нам сейчас нужно оценить масштаб бедствия."
    me "Это точно."

    "Я потянул ручку двери, но открыть саму дверь у меня удалось с большим трудом."

    $ renpy.notify("Тут должен быть фон засранной подсобки, ну и в целом выглядеть он должен совсем иначе, не как этот вот")
    hide el
    hide sh
    with dspr
    show bg int_editorial_day_wnfh with dissolve

    "Положение вещей внутри было весьма плачевным."
    "Куча коробок с макулатурой, каких-то ящиков, мешков, набитых не пойми чем."
    "Какой-то реквизит, очевидно, для постановок."
    "На полу были разбросаны бумага и книги."
    "Посреди всего этого безобразия стояли огромный шкаф и стол."
    "Более того, было ясно, что реализовать план Серёги не выйдет из-за количества мусора. До окна банально было не добраться, а открыть его с внешней стороны, очевидно, не представлялось возможным. Только выбивать."
    "И довершало всё это великолепие огромное количество паутины и пыли. Хотя нет, пылищи!"
    "Настолько запущенного места я в жизни ещё не встречал."

    show el surprise pioneer at left 
    show sh upset pioneer at right
    with dissolve

    el "Ёма-а-а[wp]"
    sh "Не поспорить. Ну, не будем медлить."

    hide el
    hide sh
    with dspr

    "Шурик прошёл вперёд меня и взялся за мешки."
    "Судя по тому, как он напрягся, они совсем не лёгкие."
    "Я тоже решил не отставать и пошёл таскать ящики."
    "Серому же достались коробки."

    window hide dissolve
    scene black with dissolve
    $ renpy.pause(0.2, hard=True)
    scene bg int_editorial_day_wnfh
    show sh normal pioneer at right
    show el normal pioneer at left
    with dissolve
    window show dissolve

    "Спустя минут двадцать-тридцать мы вытащили большую часть хлама."
    "Поначалу мы аккуратно складывали его за пределами подсобки."
    "Но потом стали просто выкидывать за дверь."
    "Под грудами мусора же обнаружилось кресло. Только, несмотря на усталость, никто не рискнул садиться на старое пыльное сиденье."
    "А ещё тут лежало красивое советское знамя."

    th "Вот это, конечно, здешние пионеры дают[wp] Просто выбросили флаг своей страны."

    "В целом, тут было ещё много разного хлама. Я даже не знаю, как называются некоторые из этих вещей."

    me "Нам бы Женю позвать, чтобы лишнего не выбросить."
    sh "Ага. Серый, иди метнись за ней, а мы тут пока с Семёном шкаф переставим куда-нибудь."

    hide el with dspr

    "Серёга моментально удалился из подсобки."

    th "Ну почему он, а не я?"

    "Грустно вздохнув от этой мысли, я подошёл к шкафу."

    me "И куда будем его ставить?"
    sh "Тут вариантов, на самом деле, не то чтобы много."
    sh "Думаю, в тот угол поставим."
    me "Ну давай."

    play sound wnfh_sfx_list["furniture_move_loop"] loop fadein 2.0

    "Мы поудобнее схватились за боковые стороны шкафа и попытались его поднять."
    "Но сразу стало ясно, что мы неслабо так переоценили свои силы."
    "Поэтому мы стали двигать шкаф, так сказать, шагающим методом."
    "Это заняло немного больше времени, но зато мы не надорвали спины."
    "После чего мы ещё сразу передвинули стол, поставив его около стены."

    stop sound fadeout 2.0

    sh "Уже что-то да проявляется."
    me "Да, по крайней мере, теперь здесь можно спокойно ходить."
    me "И кстати[wp]"

    play sound sfx_open_window

    "Я подошёл к окну и открыл его настежь, запустив свежего воздуха в помещение."

    sh "Да, то что надо."

    show el normal pioneer at left
    show mz normal pioneer glasses at center
    with dissolve

    mz "Так-с, давайте-ка посмотрим, как вы здесь справляетесь."

    "Войдя внутрь, Евгения бегло осмотрела помещение."

    mz "Неплохо-неплохо, осталось только пылюку вытереть и расставить всё необходимое."

    show mz fun pioneer glasses at center with dspr

    mz "Но с последним я уже сама справлюсь."
    el "А может, я тебе помогу?"

    show mz sad pioneer glasses at center with dspr

    mz "А ты не устал?"

    show el grin pioneer at left with dspr

    el "Ни капли!"

    show mz shy pioneer glasses at center with dspr

    mz "Ну, я бы не отказалась от помощи[wp]"

    show el smile pioneer at left with dspr
    show sh smile pioneer at right with dspr

    "Мы с Шуриком переглянулись и слегка усмехнулись."

    me "Так, с этим всё понятно, а что делать с мусором, который мы вытащили?"

    show mz normal pioneer glasses at center with dspr
    show el normal pioneer at left with dspr
    show sh normal pioneer at right with dspr

    mz "А, оттащите его в кладовку."
    mz "Там как раз ещё должно оставаться свободное место."
    sh "Почему тогда сразу не складировали всё там?"

    show mz bukal pioneer glasses at center with dspr

    mz "Это не ко мне вопрос, а к прошлой смене."
    sh "Ясно[wp]"

    hide sh with dspr

    "Шурик пошёл на выход из подсобки."

    sh "Давай, Семён, мы перетащим всё, а Серёга пусть приберётся."
    me "Есть!"

    "Я уж было последовал за Шуриком, как Женя резко меня остановила и вручила ключ."

    mz "Потом верни, понял?"
    me "Понял."

    window hide dissolve
    stop ambience fadeout 2.0
    scene black with dissolve2
    $ renpy.pause(0.3)
    play ambience ambience_camp_center_day fadein 2.0
    scene bg ext_library_day
    show sh upset pioneer at center
    with door_blure_dissolve2
    window show dissolve

    "Спустя минут тридцать или сорок мы с Шуриком всё перетаскали."
    "И после проделанной работы мы уселись на рядом стоящую лавочку."

    sh "Ух, ну вот, сделали всё."
    me "Ага[wp] Блин, сейчас бы газировочки."
    sh "И не говори."
    sh "Трудно им автомат тут поставить, что ли?"

    "Шурик посмеялся, а я поддержал его."

    if wnfh_Data.getChoice_result_number("d8_choice_n1") == 2:

        show sh serious pioneer at center with dspr

        sh "Слушай, я тебе ещё не дорассказал по поводу старого лагеря."
        me "Я весь внимание."
        sh "В общем, поскольку то здание старое, под ним должен быть бункер."
        sh "Отголосок старого ГОСТа, который не так давно отменили. {w=0.5}Как по мне, зря."
        me "Офигеть. И ты думаешь, что вот так просто можно будет пройти в бункер?"

        show sh normal_smile pioneer at center with dspr

        sh "Нет, но мы что-нибудь придумаем!"

        show sh normal pioneer at center with dspr

        sh "Важно то, что он не функционирует и его вряд ли могли разграбить какие-нибудь мародёры."
        me "Ага, но всё оборудование из него могли вывезти сами военные."
        sh "Не проверишь — не узнаешь."

    else:

        show sh serious pioneer at center with dspr

        sh "Слушай, я же тебе не рассказывал, что мы планируем вылазку в старый лагерь?"
        me "Что? Зачем?"
        sh "За деталями для самолёта, очевидно же. У нас отсутствуют передатчики для радиоуправления."
        me "И ты думаешь, их можно найти в этой заброшке?"

        show sh normal_smile pioneer at center with dspr

        "Шурик поправил очки и усмехнулся."

        sh "Согласно одному старому ГОСТу, под подобными зданиями должен располагаться бункер."
        sh "И его вряд ли могли разграбить в такой-то глуши."
        me "Зато могли сами военные. Не оставлять же оборудование."

        show sh normal pioneer at center with dspr

        sh "Возможно, но проверить всё равно стоит."

    play sound sfx_dinner_horn_processed

    "Раздался горн, призывающий пионеров на ужин."

    sh "Ну что ж, пора немного подзаправиться."
    me "Да, только ключ Жеке верну."
    sh "Давай тогда, на ужине ещё, может, встретимся."

    hide sh with dissolve

    "Мы пожали друг другу руки, Шурик ушёл к столовой, а я — в библиотеку."

    stop ambience fadeout 1.0
    scene bg int_library_day with dissolve
    play ambience ambience_library_day fadein 1.0

    "Я быстренько забежал внутрь."
    "Жени и Серого я не обнаружил, но оно и не было чем-то удивительным."
    "Я просто оставил ключ от кладовки на столе библиотекарши и убежал в столовую."

    jump d8_evening
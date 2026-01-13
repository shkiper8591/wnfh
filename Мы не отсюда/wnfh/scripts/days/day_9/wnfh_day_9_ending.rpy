label d9_ending:
    
    $ wnfh_set_slot_data(chapter = 1, game_date = "25-07-1989", scene = "Завершение дня")
    window hide dissolve
    stop ambience fadeout 2.5
    scene bg ext_house_of_mt_sunset with dissolve2
    $ renpy.pause(0.3)
    scene bg int_house_of_mt_sunset
    show mt normal pioneer far at center
    with door_blure_dissolve
    play sound sfx_open_dooor_campus_2
    play ambience ambience_int_cabin_evening fadein 2.5 
    $ renpy.pause(0.3)
    play sound wnfh_sfx_list["writing_loop"] loop fadein 0.5
    window show dissolve

    "Медленно и без особого настроения я вернулся домой."
    "Внутри была вожатая, которая подписывала и сортировала какие-то бумаги."

    me "Вот и я."

    if wnfh_Data.FlagGet("mt_angry") == True:

        mt "Как тебе моя трудотерапия?"
        me "Больше косячить не буду."

        show mt laugh pioneer far at center with dspr

        mt "То-то же!"

        "Она громко посмеялась."

        show mt smile pioneer far at center with dspr

    else:

        mt "Что-то рано ты."
        me "Да, на улице, кажется, дождь намечается."
        me "Тучи сгущаются, громыхает вдали."
        me "Поэтому решил особо не задерживаться."

        show mt smile pioneer far at center with dspr

        mt "Ну и правильно."

    play sound sfx_bed_squeak2

    "Сняв обувь, я упал на кровать и уставился в потолок."

    me "Ольга Дмитриевна, нам нужно поговорить."
    mt "Что такое?"
    me "Лена, она[wp] Кажется, она такая же, как я."

    show mt normal pioneer far at center with dspr
    stop sound fadeout 0.5

    "Повисла тишина."

    show mt normal pioneer at center with dspr

    "Вожатая отложила письменные принадлежности и встала из-за стола, пересев поближе ко мне."

    mt "Выкладывай."
    me "Стоял на площади, думал о великом[wp]{nw=4.5}"
    mt "Семён, ближе к делу."
    me "Короче, Лена сказала, мол, нужно побеседовать, и повела меня к воротам."
    me "Ничего не говорила, оглядывалась постоянно."
    me "А потом спросила что-то типа «ты не отсюда, да?»."
    me "Перед этим она говорила, что не сумасшедшая."

    "Ольга пододвинулась чуть поближе."

    mt "Так, и?"
    me "Что «и»? Вам не кажется странным уводить человека подальше от других и задавать такие вопросы?"
    mt "Кажется, дальше-то что было?"
    me "Я сыграл дурачка и сделал вид, что не понял её."

    "Вожатая с облегчением выдохнула, вытирая пот со своего лба."

    mt "Молодец, что так поступил."
    me "Что? Почему?"
    mt "С вами, попадашками, всё очень сложно. Я не могу объяснить всех подробностей, но[wp]"
    mt "Скажем так, такие люди очень легко могут быть завербованы."
    me "Завербованы?"

    window hide dissolve
    stop ambience fadeout 2.5
    show bg int_house_of_mt_night2
    show mt normal pioneer at center
    $ wnfh_set_time("night")
    with flash
    play sound sfx_thunder_crack
    play ambience wnfh_ambience_list["rain_in_building"] fadein 2.5
    $ renpy.pause(0.3)
    window show dissolve

    "В этот момент, словно в кино, раздался раскат грома."
    "По крыше стал стучать ливень, а в дом задул прохладный ветер."

    mt "Да, в спецслужбы."
    me "То есть, они действуют по принципу «клин клином вышибает»?"
    mt "Наверное, я сама многого не знаю."
    me "И тем не менее, вы знаете, что их вербуют. Откуда?"

    show mt sad pioneer at center with dspr

    "Ольга отстранённо посмотрела в окно."
    "Раздался тяжёлый вздох."

    mt "Видела. Лично."
    mt "Вы ведь не первые у меня. И наверняка не последние."
    mt "А потом подобные граждане раскрывают наши подпольные сети."
    me "Но зачем прятаться? Мы что, унтерменши какие-то? Меня могут расстрелять? Что со мной будет, если меня поймают?"

    "Ольга Дмитриевна смотрела на меня. Пустой взгляд раздумий."
    "Было очевидно, что ей этот диалог не просто даётся."

    mt "Я[wp] Я не знаю."
    mt "Мне много раз доводилось видеть, как таких как ты забирают."

    show mt scared pioneer at center with dspr

    mt "И больше я их не видела."

    "По щекам Ольги потекли слёзы."

    show mt scared pioneer close at center with dspr

    "Я тут же поднялся, усевшись напротив неё."

    th "Никогда её такой не видел. Похоже, этот вопрос для неё куда более личный, чем я мог представить."

    me "Оль, ну всё, не надо плакать."
    me "Всё будет хорошо. {w=0.5}И со мной, и с остальными."

    "Я попытался приобнять её, но она отстранилась."

    mt "Хотелось бы верить."

    show mt sad pioneer at center with dspr

    mt "Ладно, пора спать. А тебе совет: постарайся поменьше пересекаться с Леной."
    mt "Или, по крайней мере, больше головой думать, а не как вы, мужики, обычно любите."
    me "Обещаю."

    show mt sad_smile_wnfh pioneer at center with dspr

    mt "Вот и молодец."

    "Она потрепыхала мне волосы, после чего удалилась к своей кровати."

    hide mt with dissolve

    th "Действительно, пора уже баиньки. Утро вечера мудренее."

    show blink with None

    "Я переоделся и улёгся, а сон сам собой утянул меня к себе."

    window hide dissolve
    stop ambience fadeout 2.5
    $ renpy.pause(2.5, hard=True)
    scene black

    jump d10_morning

label d9_ending_dv:

    $ wnfh_set_slot_data(chapter = 1, game_date = "25-07-1989", scene = "Завершение дня")
    window hide dissolve
    scene bg ext_house_of_mt_night with dissolve2
    $ renpy.pause(0.3)
    stop ambience fadeout 2.0
    play sound sfx_open_dooor_campus_2
    scene bg int_house_of_mt_night
    camera at SRD_screen_raindrops_effect("False")
    show mt sad nightdress at center
    with dissolve
    play ambience wnfh_ambience_list["rain_in_building"] fadein 2.5
    $ renpy.pause(0.3)
    window show dissolve

    "Внутри меня встретила обеспокоенная вожатая."

    mt "А, вот и ты. Честно говоря, я уже начала волноваться[wp]"

    show mt shocked nightdress at center with dspr

    "Ольга Дмитриевна внимательно осмотрела меня с ног до головы."

    mt "Мать моя женщина, Семён, ты где был-то?"
    me "На улице."
    mt "Ты специально по грязи бегал, что ли? Посмотри на свою обувь!"

    "Я перевёл взгляд вниз, а тамошний вид, мягко говоря, производил впечатление."
    "Вся моя обувь, носки и даже ноги были в грязи."

    show mt normal nightdress at center with dspr

    mt "Я тебя таким в постель не пущу."
    me "И что вы мне прикажете делать?"
    mt "Стой здесь, скоро приду."

    hide mt with dissolve
    play sound sfx_close_door_campus_1

    "Захватив таз, вожатая вышла из дома."

    th "Отчаянная женщина."

    "Чтобы зря время не терять, я быстро снял с себя всё грязное и сел на стул в ожидании помощи."

    show mt normal nightdress at center with dspr
    play sound sfx_open_dooor_campus_1

    "Спустя пару минут Ольга вернулась."
    "Подойдя ко мне, она поставила мне под ноги таз и дала из шкафа чистое полотенце."

    me "Спасибо."

    play sound wnfh_sfx_list["me_tazik"] loop fadein 0.5

    "Я тут же принялся отмывать с себя всю грязь."
    
    hide mt with dissolve

    "В это же время вожатая улеглась в постель."

    mt "Так где ты был?"
    me "Гулял с Алисой."
    mt "Надеюсь, без очередных выходок?"
    me "Не понимаю, о чём вы."
    mt "Давай не начинай тут, Семён. Всё я о вас знаю."
    me "Не пойман — не вор."

    "Фыркнув, Ольга отвернулась к стенке."

    mt "Давай быстрее заканчивай и выключай свет. Спать охота."
    me "Есть."

    stop sound fadeout 0.5
    $ renpy.pause(1.0)
    show bg int_house_of_mt_night2 with dspr
    play sound sfx_click_3
    $ renpy.pause(0.5)
    play sound sfx_bed_squeak2

    "Быстро закончив отмываться и вытираться, я, следуя приказу, выключил свет, после чего улёгся в постель."

    me "Спокойной ночи."
    mt "Спокойной."

    window hide dissolve
    $ renpy.pause(1.0)
    show blink with None
    stop ambience fadeout 2.5
    $ renpy.pause(2.5, hard=True)
    scene black
    jump wnfh_day_10

label d9_ending_kat:
#Если что, я этот кусок ещё не тестил, так что хз, есть тут трейсы или прочая дичь.

    $ wnfh_set_slot_data(chapter = 1, game_date = "25-07-1989", scene = "Завершение дня")
    scene bg ext_houses_night_wnfh at wnfh_running
    $ renpy.pause(1.0)
    window show dissolve

    "Выбежав из леса, мы продолжили наш марафон по лагерю."

    th "Давай, Семён, последний рывок — и мягенькая постель будет прямо перед тобой!"

    "Правда, в потёмках было затруднительно что-либо разглядеть, так что я то и дело о что-то спотыкался."

    scene black with dissolve
    play sound sfx_bush_body_fall

    "И в один такой момент, когда до наших домиков уже было рукой подать, я споткнулся и упал на землю."
    "Последнее, что я успел сделать, так это отпустить Катю, чтобы не утянуть её за собой."

    th "Вот холера, теперь я по уши в грязи[wp]"

    kat "Семён, ты как там?"

    "Падение было болезненным, но терпимым."

    scene bg ext_house_of_kat_light_night_wnfh
    show kat surprise pioneer at center
    with dissolve

    "Медленно я поднялся и оглянулся. Катя уже стояла в дверях своего домика."

    me "Жить буду, нужно только пару костей вправить."

    show kat scared pioneer at center with dspr
    play sound wnfh_sfx_list["cracking_knuckles"]

    "Демонстративно я похрустел в локтях и запястьях."
    "От такого зрелища Катю аж передёрнуло."

    show kat happy pioneer at center with dspr

    kat "Знаешь, а хорошо погуляли!"
    me "Да, неплохо. Иди домой, а то простынешь."

    show kat shy pioneer at center with dspr

    "Под тусклым светом уличной лампы было видно, как её щёки налились румянцем."

    kat "До завтра."

    hide kat with dissolve
    play sound sfx_close_door_campus_1

    "Катя аккуратно вошла домой."

    me "Ну а мне же сейчас будут готовить расстрельную бригаду."

    window hide dissolve
    scene bg ext_house_of_mt_night with dissolve
    $ renpy.pause(0.5)
    stop ambience fadeout 2.5
    scene bg int_house_of_mt_night with door_blure_dissolve
    play sound sfx_open_dooor_campus_2
    play ambience wnfh_ambience_list["rain_in_building"] fadein 2.5
    $ renpy.pause(0.5)
    window show dissolve

    "Я завалился в дом, и в тишине было слышно, как с меня стекают капли воды и грязи."

    show mt surprise pioneer far at center with dissolve

    "Обернувшаяся на звук вожатая обомлела от моего внешнего вида."
    "Казалось, она хочет что-то сказать, но замешательство не позволяет."

    mt "Это где ты так?"
    me "Да вот в метрах пяти от дома споткнулся, пока бежал сюда."

    show mt sad pioneer far at center with dspr

    mt "Ох, Семён-Семён, и что мне с тобой делать?"
    me "Понять и простить."
    mt "Да я не про это, как я тебя таким грязным в постель-то пущу?"
    me "Просто полотенце дайте, я ототрусь."

    show mt normal pioneer far at right with dspr
    play sound sfx_open_cupboard

    "Ничего не говоря, вожатая встала из-за стола и подошла к шкафу."
    "Оттуда она достала полотенце, таз и старую добрую советскую водогрейку."

    show mt normal pioneer at center with dspr

    "Весь этот набор она протянула мне."

    mt "На вот, и мигом в душ."
    me "Обратно под ливень?!"

    show mt angry pioneer at center with dspr

    mt "Иначе будешь спать на полу!"
    me "Понял."

    th "Что же за напасть-то такая!"

    window hide dissolve
    stop ambience fadeout 2.0
    play sound sfx_close_door_campus_1
    scene bg ext_house_of_mt_night with dissolve
    play ambience wnfh_ambience_list["rain_night"] fadein 2.5
    window show dissolve

    "Спорить с вожатой смысла не было."
    "Благо, на выходе она дала мне ещё пару полотенец, чтобы я укрылся ими от дождя."

    scene black with dissolve2

    "До душа я добрался без особых проблем."

    th "Вот хорошо, что не вчера изгваздался. Пришлось бы ещё сидеть ждать, пока вода нагреется."

    "Много времени мытьё не заняло, и я отправился домой."

    scene bg ext_house_of_mt_night with dissolve

    "Добрался я уже без происшествий и по возможности избегая грязи."
    "Правда, идти по улице в одних полотенцах было очень некомфортно."

    window hide dissolve
    stop ambience fadeout 2.5
    play sound sfx_open_dooor_campus_2
    scene bg int_house_of_mt_night
    show mt normal nightdress at center
    with dissolve2
    play ambience wnfh_ambience_list["rain_in_building"] fadein 2.5
    $ renpy.pause(0.5)
    window show dissolve

    me "А вот и снова я."

    show mt laugh nightdress at center with dspr

    mt "Ну вот, совсем другое дело!"

    show mt smile nightdress at center with dspr

    mt "Сменную одежду я тебе на кровать положила."
    me "Спасибо."

    "Надев всё необходимое, я улёгся в постель."

    show bg int_house_of_mt_night2 with dspr
    play sound sfx_click_3

    "Вожатая выключила свет и тоже улеглась спать." 

    mt "Спокойной ночи."
    me "И вам того же."

    window hide dissolve
    show blink with None
    stop ambience fadeout 2.5
    $ renpy.pause(2.5, hard=True)
    scene black

    jump d10_morning

label d9_ending_un:

    $ wnfh_set_slot_data(chapter = 1, game_date = "25-07-1989", scene = "Завершение дня")
    window hide dissolve
    stop ambience fadeout 2.5
    scene bg ext_house_of_mt_sunset with dissolve2
    $ renpy.pause(0.3)
    scene bg int_house_of_mt_sunset
    show mt normal pioneer at center
    with door_blure_dissolve
    play sound sfx_open_dooor_campus_1
    play ambience ambience_int_cabin_evening fadein 2.5
    $ renpy.pause(0.5)
    window show dissolve

    "Мне очень хотелось пройтись и поразмышлять в одиночку, однако громыхающая неподалёку гроза явно намекала, что задерживаться на улице не стоит."
    "А спорить со стихией у меня никакого желания не было."

    me "Я вернулся."

    show mt smile pioneer at center with dspr

    mt "Как-то ты рановато, обычно тебя только под самую ночь дожидаешься."
    me "На улице дождь собирается, поэтому не стал задерживаться."
    mt "И правильно."

    play sound sfx_bed_squeak1

    "Не теряя особо времени, я улёгся на кровать."

    if wnfh_Data.FlagGet("mt_angry") == True:

        mt "Вижу, моя трудотерапия пошла на пользу."
        me "Ещё как."

        show mt grin pioneer at center with dspr

        mt "Будешь ещё отлынивать?"
        me "Никак нет."
        mt "Умничка!"

        show mt smile pioneer at center with dspr

    "Я пытался собраться с мыслями. Проанализировать случившееся."

    th "Так, что мы имеем? Меня шантажируют. Шаг влево, шаг вправо — расстрел. {w}Не исключено, что буквально."
    th "Не знаю, кто за всем этим стоит, но ежу понятно, что Лена не по своему желанию мне угрожает."
    th "И вот ведь сволочуги какие, а! Нашли самую скромную девчушку и завербовали её! Просто слов нет."
    th "На Лену я обиду точно не держу, ей просто не посчастливилось стать их марионеткой. Но как там говорил Морфеус? «Пока они часть системы, они — наши враги»? {w=2.0}Да, кажется, как-то так."

    show mt normal pioneer at center with dspr

    mt "Ты какой-то задумчивый, Семён."
    mt "Уж не случилось чего?"
    me "Случилось, но я не хочу об этом говорить."
    mt "Чего так?"
    me "Личная тема."
    mt "Семён, если тебя что-то тревожит или кто-то обижает, то[wp]{nw=2.5}"
    me "Не-не-не, ничего подобного. Просто это моё личное."

    "Вожатая только хмыкнула, после чего продолжила заниматься своими делами."

    window hide dissolve
    scene black with dissolve2
    stop ambience fadeout 2.5
    $ renpy.pause(1.0)
    $ wnfh_set_time("night")
    scene bg int_house_of_mt_night2 with dissolve2
    play ambience wnfh_ambience_list["rain_in_building"] fadein 2.5
    $ renpy.pause(1.0)
    window show dissolve

    "За окном шла гроза. Мы с вожатой давно улеглись спать."
    "Вернее, она-то уснула, а меня никак не покидали смутные мысли."

    th "Мне нужно рассказать Ольге о случившемся."
    th "Сильный ливень вполне может заглушить разговоры, так что лучше момента не придумать."

    play sound sfx_bed_squeak2

    "Медленно поднявшись, я подошёл к кровати вожатой."

    me "Ольга Дмитриевна."

    "Нет ответа."

    th "Надеюсь, она спит не столь же крепко, как Добрыня."

    me "Ольга Дмитриевна."

    "Я немного потряс её за плечо."
    "Она поёрзала и что-то пробубнила себе под нос."

    me "Ольга Дмитриевна, это срочно!"

    show mt sad nightdress at center with dissolve

    "Наконец, издав звук явного негодования, вожатая очнулась."

    mt "Семён, а это «срочно» не может подождать до утра?"
    me "Лена-попаданец и она работает на какие-то спецслужбы."

    show mt shocked nightdress at center with dspr

    mt "Чего?!"

    "Вожатая резко поднялась и уставилась на меня."

    show mt angry nightdress at center with dspr

    mt "Рассказывай."

    "Сев напротив Ольги, я стал выкладывать всё произошедшее."

    window hide dspr
    show black with dissolve
    $ renpy.pause(0.5)
    hide black
    show mt sad nightdress at center
    with dissolve
    window show dspr

    mt "Ох и вляпались же мы[wp]"
    me "И что теперь делать?"

    show mt normal nightdress at center with dspr

    "Вожатая ушла в глубокие размышления."

    mt "Хороший вопрос[wp]"
    mt "Возможно, мне для этого придётся привлечь Славю."

    if wnfh_Data.FlagGet("mt_angry") == True:

        me "А как она может помочь?"
        mt "Неважно. Не сбивай мысль."

    else: 

        me "Погодите, Славю?"
        mt "Да-да, не сбивай мысль."

    "Пару минут поразмышляв в тишине, Ольга начала говорить."

    mt "Ты говоришь, она пока ни о ком больше не знает. Значит, у нас ещё есть время."
    mt "Мы со Славей успеем подготовить все необходимые бумаги и удостоверения."
    mt "Тебе же придётся поводить Лену за нос и попутно втереться в доверие."
    mt "Постарайся разузнать, что ей ещё известно. А ещё лучше — где она хранит, так сказать, разведданные."

    "Вожатая нервно выдохнула, а её саму немного трясло."

    show mt sad nightdress at center with dspr

    mt "Подай, пожалуйста, валерьянки."

    "Я взял склянку с таблетками и передал Ольге."
    "Та залпом съела сразу пять штук."

    me "Простите, что я такой дурак[wp]"
    mt "Да чего уж теперь извиняться? Что сделано, то сделано."
    me "То есть, никакой злобы вы на меня не держите, да?"
    mt "Ещё как держу, вот только толку-то от неё? Вот именно, никакого."
    mt "Ладно, давай возвращаться ко сну[wp] Как-нибудь."
    mt "Завтра уже будем действовать."
    me "Есть, товарищ генерал!"

    hide mt with dissolve

    "Я шутливо отдал честь, на что Ольга Дмитриевна только покачала головой и улеглась обратно."
    "За ней ушёл спать и я."

    window hide dissolve
    show blink with None
    stop ambience fadeout 2.5
    $ renpy.pause(2.5, hard=True)
    scene black
    jump d10_morning
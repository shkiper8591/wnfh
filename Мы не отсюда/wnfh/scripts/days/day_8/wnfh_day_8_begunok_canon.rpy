label d8_begunok_canon:

    window hide dissolve
    hide mid d8_breakfast_empty with dissolve
    $ renpy.pause(1.0)
    stop ambience fadeout 2.5
    
    scene bg ext_dining_hall_near_day
    show kat normal pioneer at center
    with slide_right_blure_dissolve2
    play ambience ambience_camp_center_evening fadein 3
    play music music_list["dance_of_fireflies"] fadein 5
    $ renpy.pause(1.0)
    window show dissolve
    $ wnfh_Data.FlagSet("d8_begunok", True)
    $ wnfh_set_time()
    ## Семён и Катя отправляются заполнять бегунок
    "Я вышел из столовой и позвал сидящую на лавочке Катю." 
    "Посмотрев на меня, она неспешно поднялась и подошла ко мне."
    
    show kat normal pioneer at center with dissolve
    
    kat "Ну что, куда пойдём в первую очередь?"
    me "Смотря что тебе интереснее."
    
    "Девушка стала внимательно изучать список позиций в обходном."
    
    show kat thinking with dspr
    
    kat "Я[wp] Не знаю, тут всё интересно, в целом."
    me "Ладно, допустим."
    me "Давай тогда разберёмся сначала с клубами и музкружком, чтобы потом не надо было туда-сюда ходить."
    me "А потом надо будет выполнить задание по поимке неуловимой вожатой."
    
    show kat grin with dspr
    
    "Катя усмехнулась."
    
    kat "И где же мы будем её искать, раз она неуловимая?"
    me "На месте разберёмся."
    
    show kat smile2 with dspr
    
    kat "Ладно, пойдём уже."
    
    "Скомандовала она, и мы быстрым шагом отправились в сторону клубов."
    
    window hide
    scene bg ext_clubs_day with dissolve2
    $ renpy.pause(1.0)
    window show
    
    "Вскоре мы подошли к клубам, открыли дверь и вошли."
    
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
    kat "Тут же никого нет[wp] {w}Кто подписывать-то будет?"
    
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
    
    "Закрыв клубы, мы направились в сторону музкружка."
    
    window hide
    scene bg ext_musclub_day with slide_left_blure_dissolve2
    show kat normal pioneer with dissolve
    window show
    ## В музкружке
    "Сократив путь через небольшой пролесок, мы дошли до цели. Оттуда доносилась исполняемая мелодия."
    
    # Какая-нибудь пианинко на фоне (может кавер хатсуне мику?)))))))
    kat "Красиво играет."
    me "Да, это наша девочка-оркестр. {w}Мику зовут."
    kat "Наверное, это о ней мне Лена рассказывала."
    kat "Это же она с длинными аквамариновыми волосами?"
    me "Да-да-да, всё верно."
    me "А Лена тебе рассказывала, как сильно она любит тараторить?"
    
    window hide
    hide kat with dissolve
    $ renpy.pause(1.0)
    scene bg ext_musclub_verandah_day_wnfh with santa_barbara_in_blure_dissolve2
    show kat normal pioneer at left with dissolve
    window show
    
    kat "Вроде как, но думаю, она сильно преувеличивает."
    th "Хо-хо, девочка, как же ты ошибаешься[wp] Как же ошибаешься[wp]"
    
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
    
    "Войдя внутрь, мы застали Мику играющей на пианино[wp] Или рояле? Неважно, в общем."
    "Главное, что это было нисколечко не удивительно."
    "Но продлилось это недолго, ведь она тут же обратила на нас внимание. А вот это уже было удивительно."
    
    show mi normal pioneer at left
    show kat thinking pioneer at center 
    with dissolve
    
    mi "Приветик! Какими судьбами пожаловали к нам? Ну, то есть, ко мне, я тут только одна, но надеюсь, скоро нас будет больше!"
    
    "Мику настолько быстро протараторила, что Катя аж в ступор впала."
    
    kat "И тебе привет."
    
    show mi grin with dspr
    
    mi "А ты у нас новенькая значит, да? {w}Тогда давай знакомиться, я Мику! Нет, честно-честно! Никто не верит, а меня правда так зовут. Просто у меня мама из Японии. Папа с ней познакомился, когда строил там[wp] Ну, то есть не строил – он у меня инженер[wp]"
    mi "Короче, атомную станцию! Или плотину[wp] Или мост[wp] Ну, неважно!"
    
    "Мику говорила с такой скоростью, что половину слов просто проглатывала."
    
    th "Девочка-пулемёт, вот твоё настоящее имя. Поэтому никто и не верит в твою историю."
    
    "Бедная Катя, похоже, всё сильнее и сильнее удивлялась тому, с какой скоростью Мику вываливала на неё свою биографию."
    
    kat "А я Катя."
    
    "Тихо проговорила девочка."
    
    mi "Приятно познакомиться! Не хочешь вступить ко мне в музыкальный кружок? А то мне здесь очень грустно одной. Ты, кстати, умеешь на чём-нибудь играть?"
    
    "Наша новенькая немного призадумалась, видимо, обрабатывая тот поток слов, что на неё сейчас вылился."
    
    show kat smile with dspr
    
    kat "Да, я на скрипке хорошо играть умею."
    mi "Пра-а-авда?"
    
    "Протяжно произнесла Мику."
    
    show kat grin with dspr
    
    kat "Правда-правда!"
    mi "Так это же замечательно! Тогда тебе точно надо ко мне записаться! Я буду на рояле, а ты на скрипке! Будет просто прекрасное сочетание!"
    
    show mi sad with dspr
    
    mi "А то звучания одного инструмента бывает недостаточно для красивой мелодии."
    
    show kat smile2 with dspr
    
    kat "Знаешь[wp] Почему бы и нет? Попробуем сыграть вместе!"
    
    show mi happy with dspr
    
    mi "Чудесно, просто чудесно!"
    
    show mi normal with dspr
    
    "Я громко прокашлялся, и девочки перевели взгляд на меня. {w}Видимо, за своими разговорами они немного забыли обо мне."
    
    me "Мику, подпишешь Кате обходной?"
    mi "Ну конечно! Давай его сюда!"
    
    show mi normal:
        ease_quart 2.5 xcenter -0.2    

    "Катя протянула Мику бегунок, и та, элегантно выхватив его из рук, вприпрыжку побежала в подсобку."
    
    show kat normal with dspr
    
    me "Ты точно хочешь играть с девочкой-пулемётом?"
    
    "С лёгкой насмешкой в голосе спросил я."
    
    show kat smile with dspr
    
    kat "А что? Она такая забавная, когда тараторит. И к тому же, у неё тут целый музкружок с кучей инструментов!"
    kat "Правда, я и на половине этого богатства играть не умею, но зато скрипкой владею в совершенстве!"
    me "В таком случае желаю тебе удачи и терпения."
    kat "Да ладно, могло быть и хуже."
    
    show mi normal pioneer:
        ease_quart 2.0 xcenter 0.28
    
    "Совсем скоро музыкантша вернулась из подсобки."
    
    mi "Готово! Теперь ты — полноправная участница нашего музкружка! То есть моего, но теперь он будет наш!"
    
    "Мику торжественно протянула Кате обходной."
    
    show kat happy with dspr
    
    kat "Спасибо!"
    me "Отлично, мы тогда пойдём, нам ещё несколько мест посетить надо, иначе вожатая стукнет."
    
    show mi grin with dspr
    
    mi "Хорошо, не буду задерживать! А тебя, Катя, тогда жду тут после обеда, договорились?"
    
    "Катя одобрительно кивнула, и мы покинули кружок."
    "Мы, преисполненные хорошим настроением, отправились в сторону медпункта."
    
    window hide
    stop ambience fadeout 0.5
    stop music fadeout 2
    play ambience ambience_camp_center_day fadein 3
    scene black with door_invert_blure_dissolve
    play sound sfx_close_door_1
    $ renpy.pause(1.0)
    window show
    
    "И вы, читатель, надеюсь, тоже преисполнены хорошим настроением."
    "Собственно, ради того, чтобы сохранить ваше хорошее настроение, я предлагаю вам сделку."
    "Вы не заставляете меня писать две тысячи строк о захватывающем дух заполнении бегунка, а я, в свою очередь, не заставляю вас это читать."
    "Ну ладно, не буду вас задерживать, продолжаем!"
    
    window hide dissolve
    play sound sfx_open_door_1
    scene bg ext_house_of_mt_day at wnfh_entrance
    stop ambience fadeout 0.5
    scene bg int_house_of_mt_day with door_blure_dissolve2
    play ambience ambience_int_cabin_day fadein 3
    window show dissolve
    
    ## Сдача бегунка вожатой
    
    "Разобравшись с бегунком, мы мигом прибежали к нашей вожатой."
    "Ольга Дмитриевна была в домике и вновь подписывала какие-то документы за столом."
    
    show mt normal pioneer close at right
    show kat normal pioneer close at left
    with dissolve
    
    "Мы подошли ближе к вожатой, Катя торжественно протянула ей заполненный бегунок[wp]"
    
    show kat confused with dspr
    
    "И Ольга Дмитриевна просто положила его в стопку к другим документам, даже не посмотрев."
    
    mt "Молодцы, ребята. Обходной я потом посмотрю, когда с делами закончу. {w}Куда-нибудь успела записаться?"
    
    show kat smile with dspr
    
    kat "Да, я в музкружок записалась."
    
    show mt smile with dspr
    
    mt "Молодец, а то Мику там совсем скучает одна."
    me "Ладно, мы теперь свободны?"
    mt "Да, в целом, вы свободны, только обед уже через десять минут."
    me "Тогда мы, наверное, на улице его подождём."
    
    "Вожатая угукнула и вернулась к своим бумагам, а мы покинули домик."
    
    window hide dissolve
    stop ambience fadeout 0.5
    scene bg ext_house_of_mt_day with door_invert_blure_dissolve
    play sound sfx_close_door_1
    show kat normal pioneer with dissolve
    play ambience ambience_camp_center_day fadein 3
    window show dissolve

    "Выйдя, мы сели на крылечке."
    
    me "Ну-с, как тебе лагерь?"
    
    show kat smile2 with dspr
    
    kat "Уютненько, люди хорошие."
    
    show kat obida with dspr
    
    kat "Кроме тех двух[wp]"
    kat "Ну, тех, которые из ведра меня на входе окатили."
    me "Алиса с Ульяной?"
    kat "Ага."
    me "Зря ты о них так, просто дурачатся."
    me "Так-то люди они хорошие."
    kat "Возможно, но того, что они — хулиганьё, это не отменяет!"
    
    "Фыркнула она и сложила руки."
    
    me "Да ладно тебе, подружитесь ещё."
    
    "Между нами повисла тишина."
    
    stop music fadeout 5
    
    "Которую мне захотелось разбавить."
    
    me "Наверное, немного поздновато задавать такой вопрос, но[wp]"
    me "Почему ты приехала на неделю позже?"
    
    show kat thinking with dspr
    
    "Катя серьёзно задумалась над моим вопросом."
    "Так, словно я спросил её о чём-то очень необычном."
    
    kat "Я[wp] {w}Я не знаю[wp]"
    me "В смысле[wp] Не знаешь?"
    
    play sound sfx_dinner_horn_processed
    
    "Катя уже собиралась что-то ответить, но горн на обед прервал её."
    
    me "Ладно, потом расскажешь."
    
    "Мы молча отправились в столовую."

    jump d8_obed_me_kat
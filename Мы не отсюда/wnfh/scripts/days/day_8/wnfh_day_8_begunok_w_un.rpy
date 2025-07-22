label d8_begunok_w_un:
    window hide dissolve
    hide mid d8_breakfast_empty with dissolve
    $ renpy.pause(1.0)
    stop ambience fadeout 2.5
    
    scene bg ext_dining_hall_near_day 
    show kat normal pioneer at left
    show un normal pioneer at right
    with slide_right_blure_dissolve2
    play ambience ambience_camp_center_evening fadein 3
    play music music_list["dance_of_fireflies"] fadein 5
    $ renpy.pause(1.0)
    window show dissolve
    $ wnfh_Data.FlagSet("d8_begunok", "lena")
    $ wnfh_set_time()

    me "Так, какие там места нам нужно посетить?"

    "Катя поднесла листок поближе к себе и стала читать вслух."

    kat "Музыкальный кружок, клубы, медпункт и библиотека."

    show un normal pioneer at right with dspr

    "Лена наклонилась над листком и сделала вид, что всё поняла, глядя на повёрнутый вверх ногами бегунок."
    
    un "Что ж, медпункт и библиотека тут поблизости, можем сразу туда сходить."

    "В голове я нарисовал себе карту лагеря."

    # возможно тут следует показать карту под какой-нибудь смешной звук
    # а потом сделать анимацию как Семён представляет себе путь по лагерю

    show black with dissolve
    $ renpy.notify("Тут должна быть карта с анимацией")
    th "Если так прикинуть, то эффективнее выйдет начать с дальнего края «Совёнка»."
    th "И потом, если идти зигзагами от музклуба[wp] Да[wp]"
    th "После чего посетим клубы, пройдём через площадь — вот мы уже в библиотеке, и медпункт совсем рядом[wp]"
    th "А оттуда прямо к домику вожатой! По-моему, всё идеально складывается."

    hide black
    show kat smile pioneer far at left
    show un smile pioneer far at right
    with sphere_blure_dissolve2

    "Пока я стоял и раздумывал над маршрутом, Лена и Катя, явно заболтавшись, успели уже отойти на небольшое расстояние от столовой."

    me "Так, подождите меня!"

    show kat smile pioneer at left
    show un smile2 pioneer at right
    with dissolve

    "Перемахнув через перила, я подбежал к девушкам, которые тихонько хихикали надо мной."

    me "Чего смеётесь? Хоть бы предупредили!"

    show un smile pioneer at right with dspr

    un "Меньше в облаках витать надо!"
    me "Куда вы идти решили-то?"

    show un grin pioneer at right
    show kat normal pioneer at left
    with dspr

    un "Грызть гранит науки!"

    "Шутливо ответила Лена."

    me "Ага, то есть в библиотеку."

    show kat thinking pioneer at left with dspr

    kat "Ты же, надеюсь, не против?"

    show un shy pioneer at right with dspr

    un "Да[wp]"
    me "Та как бы нет, просто я продумал более эффективный маршрут[wp]"

    "Я отмахнулся рукой."

    me "А пофиг, идёмте."

    show kat normal pioneer at left
    show un smile pioneer at right
    show bg ext_library_day
    with dissolve2

    "И вот я снова стоял перед логовом дракона."
    "С библиотекой меня связывал один неприятный инцидент, который мне не сильно хочется вспоминать."

    me "Так, с библиотекой давайте, зашли и вышли."

    show kat confused pioneer at left with dspr

    kat "А к чему такая спешка?"

    show un normal pioneer at right with dspr

    un "Да, Семён. Может, она хочет получше осмотреться?"

    "Глядя прямо на Лену, я глубоко вздохнул."

    show un laugh pioneer at right with dspr

    "И тут она, по всей видимости, вспомнила эту «занимательную» историю."

    un "Ах да, точно[wp]"

    "Через смех сказала она, вгоняя нашу новенькую в полный ступор."
    "Катя смотрела то на Лену, то на меня, и так по кругу."

    kat "Мне кто-нибудь расскажет, в чём дело?"
    me "Ну, сейчас она прекратит и пояснит тебе."

    show un smile3 pioneer at right with dspr

    "Через некоторое время Лена успокоилась."

    show kat interested pioneer at left with dspr

    un "Если вкратце, Семён по своей невнимательности обвалил все стеллажи в библиотеке и сбежал с места преступления."
    un "За это его и недолюбливает наша библиотекарша."

    show kat smile2 pioneer at left with dspr

    kat "Забавная история."
    me "Да-да, упасть со смеху можно, давайте зайдём уже."

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

    "Внутри, как обычно, сидела Женя, которая с усталым видом заполняла какой-то журнал."
    "Завидев нас, она медленно подняла взгляд и оглядела наш небольшой отряд."
    "Дольше всех, разумеется, она задержала свой взор на мне. Однако в нём не было какого-либо презрения. Что ж, и на том спасибо."

    mz "Да вас тут целая группа."

    "Она посмотрела на Лену."

    mz "Мне казалось, только Семёна запрягли на это дело."

    show un grin pioneer at fright with dspr

    un "А я по собственной инициативе."
    mz "Вот как[wp] Ну ладно."

    show un smile pioneer at fright with dspr

    mz "Что, обходной лист подписать, да?"

    "Катя быстро одобрительно закивала."
    "Цокнув языком, Женя протянула руку, как бы прося бегунок."
    "Благо, наша новенькая быстро сообразила, что делать."

    kat "Меня Катей звать, кстати."

    "Сказала она, вручая лист, который библиотекарша тут же принялась подписывать."

    show kat confused pioneer at cright with dspr

    mz "Я знаю."

    "Безэмоционально ответила Женя."
    "После чего остановилась на полпути и посмотрела на Катю."

    show mz fun pioneer glasses at left 
    show kat smile pioneer at cright with dspr
    with dspr

    "Секунду поглядев на неё, она усмехнулась и поправила себя."

    mz "В смысле, я Женя, заправляю этим замечательным местом."
    kat "Да я уж поняла."

    "Закончив подписывать, Женя вернула лист Кате."

    show mz normal pioneer glasses at left with dspr

    mz "Так, если хочешь брать здесь книжки, придётся завести читательский билет."
    kat "О как[wp] Ну хорошо, давай."
    mz "Да, только мне сейчас немного не до этого, так что зайди попозже."

    "Чуть ли не протараторила библиотекарша и жестом руки указала нам на выход."

    show un shy pioneer at fright with dspr

    un "А, кстати, Жень[wp] Прости, пожалуйста, я завтра тебе книжку занесу, ладно?"

    "Женя глубоко вздохнула."
    "И я прям прочувствовал, как в этом вздохе она подавляла желание применить на Лене все известные ей техники уничтожения человека взглядом."
    "Или же раздумывала над каким-то очередным хитрым выражением, которым можно опустить её лицом в грязь."
    "Но, на удивление, Женя ничего не сказала и просто кивнула."

    show un laugh pioneer at fright with dspr

    un "Спасибо! С меня шоколадка за срыв сроков."

    window hide dissolve
    stop ambience fadeout 3.5
    scene bg ext_library_day
    show kat normal pioneer at left
    show un smile pioneer at right
    with dissolve2 
    play ambience ambience_camp_center_day fadein 3.5
    window show dissolve

    "Выйдя из библиотеки, я с облегчением вздохнул."

    me "Фух[wp] Какая-то она добрая прям сегодня."
    kat "А бывает злая?"
    me "Ну, обычно она вся из себя бука."

    show un normal pioneer at right with dspr

    un "Семён, мне кажется, ты слегка обнаглел."
    me "Да в смысле?"
    un "Сам накосячил, а теперь считаешь, что она сама по себе злая."
    me "Так я ж не специально!"

    show un shy pioneer at right with dspr

    un "Хоть бы извинился, а то после твоего побега ей пришлось просить помощи у Сергея[wp]"

    "Разумеется, мне было стыдно за то, что я сбежал из библиотеки после собственного косяка[wp] Но моя гордость не позволяет принять этот факт."
    th "Но вот сейчас, когда я узнал, что ещё и Сергею пришлось убирать за мной, мне стало действительно неловко перед ним."
    th "Зато теперь я знаю, откуда растут ноги у его с Женей романа."

    show un normal pioneer at right 
    show kat scared pioneer at left
    with dspr

    un "Семён!"

    "Резко и громко вырвала меня из мыслей Лена, чем немного напугала нас с Катей."

    show kat normal pioneer at left with dspr

    me "А? Что?"
    un "Ты какой-то чересчур мечтательный сегодня. Может, лучше оставишь обходной нам двоим?"

    th "А что, звучит как мысль. Всё равно желания всем этим заниматься у меня нет."
    th "С другой стороны, вожатая будет очень сильно ругаться. Не исключаю, что матом."

    if wnfh_Data.FlagGet("d7_kat_oblivanie") == "me_oblil":

        th "Да и с Катей неудобно как-то выходит[wp] Я её облил, так ещё и бросаю вот. Нужно же хоть как-то отработать свой косяк."

    th "Ах, как же сложно иногда бывает!"

    call screen wnfh_choice(
        ["neutral", "Оставить", "Мне это всё не упёрлось", "d8_begunok_w_un_end1", {"kat": -1, "un": -1}],
        ["kat", "Остаться", "Вожатая будет очень сильно ругаться", "d8_begunok_w_un_cont", {"kat": 1, "un": 1}],
        ["d8_choice_n6", "Семён думает не оставить ли Катю Лене"]
        ) with sphere_blure_dissolve2

label d8_begunok_w_un_end1:

    "Эмоции всё же взяли надо мной вверх, и я принял предложение Лены."

    me "А знаешь? Да пожалуйста!"

    "Отмахнувшись рукой, я оставил девушек наедине, отправившись в клубы."

    jump d8_me_dv_avantyra

label d8_begunok_w_un_cont:

    "Голос разума в моей голове оказался сильнее эмоций, так что мне хватило ума не соглашаться на это предложение."

    me "Нет уж, я с вами до конца, а то вожатая меня убьёт."

    show un smile pioneer at right
    show kat smile pioneer at left
    with dspr

    un "Вот и славненько."
    kat "Ну что ж, споры между собой вы утрясли, предлагаю пойти дальше."
    me "Да уж[wp]"

    "Хорошо, что идти тут было недалеко — до медпункта мы дошли за считаные минуты."

    stop music fadeout 3.5
    stop ambience fadeout 3.5
    window hide dissolve
    scene black with dissolve2
    window show dissolve
    play music wnfh_music_list["sharkle_dream"] fadein 3.5

    "Знаете, что делает хорошую историю воистину хорошей? Уважение к читателю."
    "Мне нравится эта философия, поэтому я не буду вас мучать долгим и мучительным рассказом о бегунке. Всё равно ничего интересного более не происходило."
    "А посему я возьму на себя власть отправить нас в конец всего это мероприятия[wp]"

    stop music fadeout 3.5
    window hide dissolve
    scene bg ext_house_of_mt_day
    show kat normal pioneer at left
    show un smile pioneer at right
    with dissolve2
    play ambience ambience_camp_center_day fadein 3.5
    window show dissolve
    play music wnfh_music_list["the_bridge"] fadein 3.5

    "Наконец, собрав все подписи, мы стояли перед домиком вожатой."
    "Куда, собственно, мы незамедлительно вошли."

    stop ambience fadeout 3.5
    show bg int_house_of_mt_day
    show mt sad pioneer far at center
    with dissolve2
    play ambience ambience_int_cabin_day fadein 3.5

    "Внутри, как и следовало ожидать, за столом сидела вожатая и заполняла какие-то документы."

    kat "Вот и мы!"

    show mt surprise pioneer far at center with dspr 

    "Ольга Дмитриевна оторвала свой взгляд от бумаг и удивлённым взглядом уставилась на Лену."

    mt "Товарищ Тихонова, у меня тут другие пионеры, можешь подождать за дверью?"

    show un grin pioneer at right with dspr

    un "А я с ними заодно!"

    show mt angry pioneer far at center with dspr

    "После ответа Лены вожатая перевела взгляд уже на меня. И она явно была недовольна."

    mt "Так, задание я поручила тебе одному, а ты, значит, решил Елену запрячь!"
    me "Уверяю вас, никто никого не запрягал! Это её личная инициатива. Да, Лена?"

    show un smile pioneer at right with dspr

    "Она радостно закивала головой."

    show mt normal pioneer far at center with dspr

    mt "Ладно[wp] Давайте сюда обходной и можете идти."

    "Катя быстренько положила листок на стол к вожатой, а та убрала его в большую стопку документов."

    mt "Только далеко не уходите, скоро обед."

    show kat sad pioneer at left with dspr

    kat "О, это хорошо, а то я уже проголодаться успела."
    me "Ну, тогда идёмте ждать[wp]"

    window hide dissolve
    stop ambience fadeout 3.5
    scene bg ext_house_of_mt_day
    show kat normal pioneer at left
    show un smile pioneer at right
    with dissolve2
    play ambience ambience_camp_center_day fadein 3.5
    window show dissolve

    "Выйдя на улицу, я присел на ступеньки."

    show kat confused pioneer at left
    show un normal pioneer at right
    with dspr

    kat "И[wp] Почему ты сел?" 
    un "Вот да. Обед же скоро, сказали."
    me "Ну, а дальше-то что? Я устал и хочу посидеть."

    if wnfh_Data.getChoice_points_sum("un") <= 5:

        jump d8_begunok_w_un_1

    else:

        jump d8_begunok_w_un_2

label d8_begunok_w_un_2:

    show un smile pioneer at left with dspr

    un "А знаешь[wp]"

    $ renpy.notify("Мб тут надо фоновый спрайт Лены на шезлонге") 

    "Лена прошлась и улеглась в шезлонг."

    show un laugh pioneer at right
    show kat confused pioneer at left
    with dspr

    un "Что-то я тоже устала."

    "Наша новенькая же сначала окинула непонимающим взглядом меня, потом Лену, затем вновь меня."

    show un smile pioneer at right with dspr

    kat "Странные вы. Если мы отсюда с горном в столовую пойдём, в самую толкучку попадём."
    me "Та не, эти троглодиты быстро проталкиваются, так что как раз вовремя придём."

    "Уже разлёгшаяся как у себя дома Лена одобрительно закивала головой."

    show kat thinking pioneer at left with dspr

    kat "Ясно[wp]"

    show kat happy pioneer at left with dspr

    kat "Ну что ж, тогда и я с вами заодно посижу!"

    $ wnfh_Data.AddLove_points({"kat":1})
    #КОСЯК: я хз, что это за вручения ЛП Кати, но они не работают, только трейс выдают. Закомменчено во избежание трейсов в игре.

    "Отряхнув ступеньку, Катя аккуратно села рядом со мной."

    show kat thinking pioneer at left with dspr

    "Мы сидели в тишине несколько секунд, пока Катя не решила прервать её."

    kat "И[wp] Что мы будем делать?"
    me "Ну как что? Сидеть отдыхать и ждать обеда."
    
    show un smile2 pioneer at right
    show kat sad pioneer at left
    with dspr 

    $ renpy.notify("В будущем тут будет миниигра в «города»")

    un "Или давайте играть в города!"
    me "Обычно те, кто предлагают в это сыграть, очень хорошо знают географию[wp]"
    
    "Лена негромко засмеялась."
    
    un "Ну да, есть немного."
    me "Что ж, я согласен."
    
    show kat upset pioneer at left with dspr

    "Катя же грустно вздохнула."
    "И, судя по этом вздоху, она-то как раз географию знала так себе."
    
    kat "Ладно, давайте сыграем."
    un "Отлично. Тогда я начинаю, далее Семён, а затем ты, и так по кругу."
    me "Идёт."
    kat "Да."

    "После нашего согласия Лена сделала задумчивый взгляд."

    un "Что же, начнём с чего-нибудь простого. Энгельс!"
    me "Мы же в города играем, а не в политиков."

    "С лёгким смешком в голосе сказал я."

    me "Так, мне на С, ну[wp] Пусть будет Самара." 
    
    show un normal pioneer at right with dspr

    un "Что ещё за Самара?"

    "Данный вопрос серьёзно так поставил меня в ступор."

    me "В смысле?"
    un "В прямом."
    un "Может, ты имеешь в виду Куйбышев?"

    th "Зараза, только начали, а я уже прокололся на такой простой теме[wp] Надеюсь, не придётся выкручиваться[wp]"

    me "Я так понимаю, мой ответ не засчитан?"
    un "Правильно понимаешь."
    me "Ладно, тогда пусть будет[wp] Саратов."

    "Катя же была полностью погружена в себя и явно за игрой не следила."
    "Так что я легонько ткнул её в плечо."

    me "Тебе на В."
    kat "А? Что? Ой, точно. Так[wp] Ну, Владивосток."

    "В итоге мы провели следующие минут пять, играя в эти пресловутые города."
    "Зато мы очень хорошо скоротали время и не заметили, как прошли эти пять минут."

    kat "[wp]Москва!"
    me "Было уже."

    show kat surprise pioneer at left with dspr

    kat "Что? Когда?"
    me "Лена говорила полминуты назад[wp]"

    play sound sfx_dinner_horn_processed

    "Вдалеке раздался горн на обед."

    un "Потом как-нибудь продолжим."
    me "Да уж, увлекательная игра."

    show kat serious pioneer at left with dspr

    "Катя тут же встала и прошла пару шагов."

    kat "Давайте уже, скорее!"

    "С большим трудом Лена поднялась с шезлонга и потянулась."

    un "Какой он удобный-то!"

    "Мне же в плане поднятия своей тушки повезло несколько меньше[wp]"
    
    show kat scared pioneer at left
    show un shocked pioneer at right
    with dspr

    "А всё из-за того, что как только я начал вставать со ступеньки, мне по спине очень сильно вдарили дверью, отчего я свалился на землю."

    show mt surprise pioneer panama at center with dissolve

    mt "Ох ё[wp] Вы тут чего расселись-то? Могли бы у столовой подождать."
    me "В города играли[wp]"

    show kat smile pioneer at left
    show un smile pioneer at right
    show mt sad pioneer panama at center 
    with dspr

    mt "Прости, Семён[wp] Я тебя там не зашибла?"

    "Катя и Лена в этот момент помогли мне встать и отряхнули меня."

    me "Да не, ничего. Так, пустяки."

    show mt normal pioneer panama at center with dspr

    mt "Ладно, давайте, не задерживайтесь, если не хотите остаться голодными."

    "Вожатая подошла ко мне и аккуратно поправила мои взъерошенные волосы."

    show mt grin pioneer panama at center with dspr

    mt "Так-то лучше!"

    window hide dissolve

    stop music fadeout 5.0
    jump d8_obed_me_kat_un

label d8_begunok_w_un_1:

    "Лена посмотрела на меня каким-то осуждающим взглядом."

    hide un with dissolve2

    # Надо анимацию Лене
    $ renpy.notify("Тут надо анимацию того как уходит Лена вправо")

    "И, гордо хмыкнув, развернулась и пошла в сторону центра лагеря."

    me "Интересно, чего это она?"

    if wnfh_Data.getChoice_points_sum("kat") <= 1:

        "Катя посмотрела на меня, а потом на уходящую Лену."
        
        kat "Наверное, я тоже пойду."
        
        hide kat with dissolve
        $ renpy.notify("Надо Кате анимацию как она уходит вправо")
        
        "Сказала она и ушла вслед за Леной, оставив меня одного."
        
        th "Ну, зато посижу в тишине и спокойно дождусь обеда."

        stop music fadeout 5.0
        jump d8_obed_me_alone
    
    else:

        jump d8_begunok_w_un_flagcheck

label d8_begunok_w_un_flagcheck:

# тут будет фактчек если Семён облил

    if wnfh_Data.FlagGet("d7_kat_oblivanie") == "dv_oblila":
        
        jump d8_begunok_w_un_flagcheck_dv_oblila

    elif wnfh_Data.FlagGet("d7_kat_oblivanie") == "me_oblil":

        if wnfh_Data.getChoice_result_number("d7_choice_n9") == 1:
            jump d8_begunok_w_un_flagcheck_me_oblil
        else:
            jump d8_begunok_w_un_2

    else:

        jump d8_begunok_w_un_flagcheck_ne_oblil

label d8_begunok_w_un_flagcheck_dv_oblila:

    kat "Странная она какая-то[wp]"
    me "Странная, говоришь?"
    
    "Катя села рядом со мной на ступеньку, перед этим аккуратно стряхнув пыль с неё."
    
    kat "Ну да, настроение у неё прям переменчивое."
    kat "То перед библиотекой, то вот сейчас."
    me "Честно, не замечал никогда такого особо."
    me "Хотя я и не общаюсь с ней толком[wp]"
    
    # удивлённый ебальник кате
    
    "Моя собеседница сильно удивилась моим словам, что было видно по её лицу."
    
    kat "А так и не скажешь, что вы мало общаетесь."
    me "Недавно вот только начали дружить[wp]"
    kat "Вот оно что[wp]"
    
    "Разумеется, наше общение с Леной и дружбой-то тяжело было назвать. Скорее, мы были как коллеги, не более того."
    
    if wnfh_Data.FlagGet("d7_me_pogulyal_w_un") == True:
    
        "Тем не менее, вчерашняя прогулка мне понравилась, пусть она и была прервана Мику."
    
    kat "И что, ты совсем тут ни с кем не общаешься? Как-то грустно это."
    me "Ну, почему же. С Алисой вот дружу."
    
    "После упоминания Алисы Катя резко переменилась в лице."
    
    kat "Ах, та самая, которая меня облила[wp] Хороший друг, ничего не скажешь."
    me "Хе, ну она правда хороший друг. Только юмор у них с Ульяной своеобразный."
    kat "Я уж заметила[wp]"
    
    "Вдалеке раздался горн на обед, что ознаменовало конец наших посиделок."
    
    me "Ну что, время обеда."
    kat "Это точно."

    stop music fadeout 5.0
    jump d8_obed_me_kat

label d8_begunok_w_un_flagcheck_ne_oblil:

    $ wnfh_Data.AddLove_points({"kat":1})
    #КОСЯК: я хз, что это за вручения ЛП Кати, но они не работают, только трейс выдают. Закомменчено во избежание трейсов в игре.

    "Мы с Катей проводили уходящую вдаль Лену, после чего наша новенькая села рядом со мной, предварительно стряхнув всю пыль рукой."

    kat "Какая-то она[wp] Загадочная, что ли."

    show kat grin pioneer at left with dspr

    kat "Как ты с ней общаешься вообще?"

    "С лёгкой насмешкой в голосе спросила она у меня."

    me "Не знаю, я с ней и не общаюсь особо."

    show kat surprise pioneer at left with dspr

    kat "Это как так?"
    me "Ну, вот так."

    show kat thinking pioneer at left with dspr

    "Катя увела взгляд и что-то пробубнила себе под нос."

    kat "Хотя, наверное, оно и не удивительно, с её-то переменчивым настроением."

    "Тем не менее я услышал всё, что она сказала."

    me "Что-то ты не лучшего мнения о ней."
    me "Она, между прочим, вероятнее всего — единственная причина, по которой рыжие хвосты ничего с тобой не сделали."

    show kat interested pioneer at left with dspr

    kat "Рыжие хвосты?"
    me "Алиса и Ульяна."

    show kat laugh pioneer at left with dspr

    "Катя залилась хохотом."

    show kat grin pioneer at left with dspr

    kat "И что бы они мне сделали?"
    me "Не знаю. Например, бревно уронили?"

    show kat surprise pioneer at left with dspr

    kat "Серьёзно?"
    me "Нет, конечно. Но зная их, точно придумали бы что-нибудь[wp]"

    show kat normal pioneer at left with dspr

    kat "Ты их так хорошо знаешь?"
    me "Ха, спрашиваешь! Алиса — мой единственный друг здесь."

    show kat thinking pioneer at left with dspr

    kat "Как-то грустно это[wp]"

    "Моя собеседница опечаленно уставила свой взор на землю."

    me "Ну, а ты успела найти здесь друзей помимо Лены и Мику?"
    
    show kat upset pioneer at left with dspr

    kat "Нет, к сожалению."
    kat "Мне тяжело друзей заводить."

    if wnfh_Data.getChoice_points_sum("kat") == 3:

        kat "Разве что, с тобой вроде как сдружилась ещё."

    show kat normal pioneer at left with dspr

    "Так мы и провели несколько минут за обычными светскими беседами."

    play sound sfx_dinner_horn_processed

    "И только горн на обед ознаменовал их конец."

    me "Ну, нам пора в путь."

    "Мы медленно поднялись со ступенек и отправились в столовую."

    stop music fadeout 5.0
    jump d8_obed_me_kat

label d8_begunok_w_un_flagcheck_me_oblil:

    #$ wnfh_Data.AddLove_points({"kat":1})
    #КОСЯК: я хз, что это за вручения ЛП Кати, но они не работают, только трейс выдают. Закомменчено во избежание трейсов в игре.

    show kat normal pioneer at left with dspr
    $ renpy.notify("Возможно тут следует дать Кате анимацию передвижения, но щас кароче лень этим маяцаааа")
    "Катя проводила взглядом ушедшую Лену и села рядом со мной."
    
    kat "Соглашусь, пожалуй, с тобой. Устала я ходить[wp]"

    "Усевшись настолько удобно, насколько это позволяли ступеньки, она положила голову на руки и задумчиво уставилась куда-то вдаль."
    "Отследив траекторию её взгляда, я понял, что она наблюдает за уходящей Леной."

    kat "Странная она всё-таки, но забавная."
    me "Лена-то?"

    "В ответ Катя лишь грустно угукнла."

    me "Это да[wp] Правда, я её толком и не знаю, чтобы утверждать наверняка."

    show kat interested pioneer at left with dspr

    kat "Серьёзно?"
    me "Ну да, а что такого?"

    show kat smile pioneer at left with dspr

    kat "Хм, а выглядите как хорошие друзья."

    "Меня позабавил её ответ."

    me "Нет, действительно хороший друг у меня здесь один, и это Алиса."
    kat "Та самая, которая якобы подставила тебя?"
    me "В смысле «якобы»?"

    show kat smile2 pioneer at left with dspr

    "Резко и немного грубо выдал я. А Катя лишь смеялась, по всей видимости, над моей реакцией."

    kat "Я шучу. Всё же по тебе было видно, что ты не хотел принимать прямого участия."

    show kat grin pioneer at left with dspr

    kat "К тому же ты извинился, пусть и не совсем искренне[wp]"

    "Последние слова из её уст прозвучали как некий призыв к действию."
    "Прям таки читалось: «Давай, Семён, ещё раз извинись, только в этот раз будь честнее!»."

    window hide dissolve
    call screen wnfh_choice(
        ["kat", "Извиниться. Ещё раз", "Давай, Семён, у тебя всё получится!", "d8_begunok_w_un_appologize", {"kat": 1}],
        ["kat", "Промолчать", "Я не канадец, чтобы помногу извиняться", "d8_begunok_w_un_silience", {"kat": -1}],
        ["d8_choice_n7", "Семён думает извиниться ли перед Катей - рут Лены"]
        ) with sphere_blure_dissolve2
    #КОСЯК: этот выбор вызывает трейс, хз почему. Отсылают на строку 569.

label d8_begunok_w_un_appologize:

    window show dissolve

    me "Да, просто я перенервничал тогда[wp]"
    me "Прости, пожалуйста, мне правда не хотелось тебя обливать."
    me "Мне вообще не хотелось в этом участвовать, но сдуру согласился[wp]"
     
    show kat smile pioneer at left with dspr

    "Катя насмешливо хмыкнула."

    if wnfh_Data.getChoice_points_sum("kat") == 3:

        show kat happy pioneer at left with dspr

        kat "Хорошо, я прощу тебя."

    else:

        kat "Что ж, я подумаю над твоими словами."

    play sound sfx_dinner_horn_processed

    "Вдали раздался долгожданный горн на обед."

    me "Ну-с, пора идти[wp]"
    
    stop music fadeout 5.0
    jump d8_obed_me_kat

label d8_begunok_w_un_silience:

    window show dissolve
    
    "Я предпочёл промолчать в ответ на этот очевиднеший намёк и грустно уткнулся взглядом в землю, где стал разглядывать пробегающих муравьёв."
    "Пионерка не отрывала с меня взор ещё несколько секунд. Но, поняв, что ничего она от меня не услышит, Катя также уткнула взгляд в землю."

    kat "Ясно[wp]"

    play sound sfx_dinner_horn_processed

    "Так мы и сидели молча, дожидаясь горна на обед."

    me "Что ж, пора в путь."

    stop music fadeout 5.0
    jump d8_obed_me_kat
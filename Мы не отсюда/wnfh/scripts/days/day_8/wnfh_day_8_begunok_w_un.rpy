label d8_begunok_w_un:
    $ wnfh_Data.FlagSet("d8_begunok", True)
    $ wnfh_set_time()
    show kat normal pioneer at left
    show un smile pioneer at right
    with dissolve

    me "Так, какие там места нам нужно посетить?"

    "Катя поднесла листок поближе к себе и стала читать вслух."

    kat "Музыкальный кружок, клубы, медпункт и библиотека."

    show un normal pioneer at right with dspr

    "Лена наклонилась над листком и, сделала вид, что понимает всё вверх ногами."
    
    un "Что ж, медпунт и библиотека тут по близости, можем туда сходить сразу."

    "У меня в голове сразу возникла карта лагеря."

    # возможно тут следует показать карту под какой-нибудь смешной звук
    # а потом сделать анимацию как Семён представляет себе путь по лагерю

    show black with dissolve
    $ renpy.notify("Тут должна быть карта с анимацией ЧИТАЙ коммент day_8_begunok line 1133")
    th "Если так прикинуть, то эффективнее выйдет начать с дальнего края «Совёнка»."
    th "И потом если двигаться зигзагообразно от муз клуба[wp] Да[wp]"
    th "После чего посетим клубы, пройдёмся через площадь, вот мы уже в библиотеке и медпункте."
    th "А оттуда прямо к домику вожатой! По моему всё идеально складывается."

    hide black
    show kat smile pioneer far at left
    show un smile pioneer far at right
    with sphere_blure_dissolve2

    "Пока я стоял и раздумывал маршрут, Лена и Катя, явно заболтавшись, успели уже отойти на небольшое расстояние от столовой."

    me "Так, подождите меня!"

    show kat smile pioneer at left
    show un smile2 pioneer at right
    with dissolve

    "Перемахнув через перила, я подбежал к девушкам, которые тихонько хихикали надо мной."

    me "Чего смеётесь, хоть бы предупредили."

    show un smile pioneer at right with dspr

    un "Меньше в облаках летать надо!"
    me "Куда вы идти решили-то?"

    show un grin pioneer at right
    show kat normal pioneer at left
    with dspr

    un "Грызть гранит науки!"

    "Шутливо ответила мне она."

    me "Ага, то есть в библиотеку."

    show kat thinking pioneer at left with dspr

    kat "Мы же надеемся ты не против?"

    show un shy pioneer at right with dspr

    un "Да[wp]"
    me "Та как бы нет, просто у меня в голове есть более эффективный маршрут но[wp]"

    "Я отмахнулся рукой."

    me "Ай пофиг, идёмте."

    show kat normal pioneer at left
    show un smile pioneer at right
    show bg ext_library_day
    with dissolve2

    "И вот снова я стоял перед этим логовом дракона."
    "С библиотекой меня связывал один неприятный инцидент, о котором я не очень-то и хотел вспоминать."

    me "Так, с библиотекой давайте зашли и вышли."

    show kat confused pioneer at left with dspr

    kat "А к чему такая спешка в отношение библиотеки?"

    show un normal pioneer at right with dspr

    un "Да Семён, может она хочет получше осмотреться?"

    "Глядя прямо на Лену я глубоко вздохнул."

    show un laugh pioneer at right with dspr

    "И тут она, по всей видимости, вспомнила об этой «занимательной» истории."

    un "Ах да, точно[wp]"

    "Через смех сказала она, вгоняя нашу новенькую в полный ступор."
    "Катя смотрела то на Лену, то на Меня, и так по кругу."

    kat "Мне кто-нибудь расскажет в чём дело?"
    me "Ну сейчас она остановится и пояснит тебе."

    show un smile3 pioneer at right with dspr

    "Через некоторое время Лена успокоилась."

    show kat interested pioneer at left with dspr

    un "Коротко говоря, Семён по своей невнимательности обвалил все полки в библиотеке и сбежал с места преступления."
    un "За это его недолюбливает наша библиотекарша."

    show kat smile2 pioneer at left with dspr

    kat "Забавная история."
    me "Да-да, давайте уже заходить."

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

    "И внутри как обычно сидела Женя, которая с усталым видом заполняла какой-то журнал."
    "Завидев нас, она медленно подняла свой взгляд и оглядела."
    "Дольше всех, разумеется, она задержала свой взор на мне. Однако, в нём не было какого-то презрения, и на том спасибо."

    mz "Да вас тут целая группа."

    "Она посмотрела на Лену."

    mz "Мне казалось, что это только Семёна запрегли на это дело."

    show un grin pioneer at fright with dspr

    un "А я по собственной инициативе!"
    mz "Вот как[wp] Ну ладно."

    show un smile pioneer at fright with dspr

    mz "Что, обходной лист подписать, да?"

    "Катя быстро одобрительно закивала."
    "Цокнув языком, Женя протянула руку, как бы прося бегунок."
    "Благо, наша новенькая была соображающая и поняла что делать."

    kat "Меня Катей звать кстати говоря."

    "Сказала она вручая лист, который библиотекарша тут же принялась подписывать."

    show kat confused pioneer at cright with dspr

    mz "Я знаю[wp]"

    "Безэмоционально ответила Женя."
    "После чего остановилась на полпути росписи и посмотрела на Катю."

    show mz fun pioneer glasses at left 
    show kat smile pioneer at cright with dspr
    with dspr

    "Секунду поглядев на неё она усмехнулась и сказала."

    mz "В смысле, я Женя, заправляю этим замечательным местом."
    kat "Да я уж поняла."

    "Закончив подписывать, Женя вернула лист Кате."

    show mz normal pioneer glasses at left with dspr

    mz "Так, если хочешь книжки брать из библиотеки, то нужно будет заполнить читательский билет."
    kat "О как, ну хорошо, давай[wp]"
    mz "Да, только мне не до этого сейчас немного, так что давай попозже ты подходи."

    "Чуть ли не протараторила библиотекарша и жестом руки показала, чтобы мы покинули помещение."

    show un shy pioneer at fright with dspr

    un "А, кстати, Жень, прости пожалуйста, я завтра тебе книжку занесу, ладно?"

    "Женя глубоко вздохнула."
    "И я прям прочувствовал, как в этом вздохе она перебирала десятки способой уничтожения человека взглядом."
    "Или же раздумывала над каким-то очередным хитрым выражением, которым можно опустить лицом в грязь."
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

    "Выйдя из библиотеки я с облегчением вздохнул."

    me "Фух[wp] Какая-то она добрая прям."
    kat "А бывает злая?"
    me "Ну, она обычно вся из себя бука."

    show un normal pioneer at right with dspr

    un "Семён, мне кажется ты немного наглый."
    me "Да всмысле?"
    un "Сам накосячил, а теперь считаешь, что она злая."
    me "Так, а я специально разве?"

    show un shy pioneer at right with dspr

    un "Хоть бы извинился, а то после твоего побега ей пришлось просить помощи у Сергея."

    "Разумеется, мне было стыдно за то, что я тогда сбежал из библиотеки, когда сам и накосячил. Но моя гордость не позволяет принять этот факт."
    th "Но вот сейчас, когда я узнал, что Сергей убирал за мной, мне стало действительно неловко перед ним."
    th "Зато, мне теперь стало известно откуда растут ноги у его с Женей романа."

    show un normal pioneer at right 
    show kat scared pioneer at left
    with dspr

    un "Семён!"

    "Резко и громко выговорила Лена, чем немного напугала меня и Катю."

    show kat normal pioneer at left with dspr

    me "А, что?"
    un "Ты какой-то мечтательный сегодня. Может лучше Катю на меня оставишь?"

    th "А что, звучит как мысль, всё равно я не хочу этим всем заниматься."
    th "С другой стороны, вожатая будет очень сильно ругаться на меня и, возможно, даже матом."

    if wnfh_Data.FlagGet("d7_kat_oblil_me") == True:

        th "Да и неудобно как-то выходит, я её облил, так и ещё бросаю вот. Нужно хоть как-то же отработать свой косяк[wp]"

    th "Ах, как же сложно иногда бывает!"

    call screen wnfh_choice(
        ["neutral", "Оставить", "Мне это всё не упёрлось", "d8_begunok_w_un_end1", {"kat": -1, "un": -1}],
        ["kat", "Остаться", "Вожатая будет очень сильно ругаться", "d8_begunok_w_un_cont", {"kat": 1, "un": 1}],
        ["d8_choice_n6", "Семён думает не оставить ли Катю Лене"]
        ) with sphere_blure_dissolve2

label d8_begunok_w_un_end1:

    "Эмоции всё же взяли надо мной вверх, и я принял предложение Лены."

    me "А знаешь? Да, пожалуйста!"

    "Отмахнувшись рукой, я оставил девушек на едине, отправившись в клубы."

    jump d8_me_dv_avantyra

label d8_begunok_w_un_cont:

    "Голос разума в моей голове оказался сильнее эмоций, так что мне хватило ума не согласится на это."

    me "Нет уж, я с вами до конца, а то вожатая меня убьёт."

    show un smile pioneer at right
    show kat smile pioneer at left
    with dspr

    un "Вот и славненько."
    kat "Ну что ж, споры между собой вы утрясли, теперь идёмте уже."
    me "Да уж[wp]"

    "Хорошо, что идти тут было недалеко и мы сразу отправились в медпункт."

    stop music fadeout 3.5
    stop ambience fadeout 3.5
    window hide dissolve
    scene black with dissolve2
    window show dissolve
    play music wnfh_music_list["sharkle_dream"] fadein 3.5

    "Знаете, что делает хорошую историю во истину хорошей? Уважение к читателю."
    "Мне нравится эта философия, поэтому не буду вас мучать долгим и мучительным рассказом о бегунке. Всё равно, ничего интересного более не происходило."
    "А посему, я возьму на себя власть отправить нас в конец всего это мероприятия[wp]"

    stop music fadeout 3.5
    window hide dissolve
    scene bg ext_house_of_mt_day
    show kat normal pioneer at left
    show un smile pioneer at right
    with dissolve2
    play ambience ambience_camp_center_day fadein 3.5
    window show dissolve
    play music wnfh_music_list["the_bridge"] fadein 3.5

    "Наконец собрав все подписи, мы стояли перед домиком вожатой."
    "Куда, собственно, мы незамедлительно и вошли."

    stop ambience fadeout 3.5
    show bg int_house_of_mt_day
    show mt sad pioneer far at center
    with dissolve2
    play ambience ambience_int_cabin_day fadein 3.5

    "Внутри, как не неожиданно, за столом сидела вожатая и заполняла какие-то документы."

    kat "Вот и мы!"

    show mt surprise pioneer far at center with dspr 

    "Ольга Дмитриевна оторвала свой взгляд от бумаг и удивлённым взглядом уставилась на Лену."

    mt "Товарищ Тихонова, у меня тут другие пионеры, можешь подождать за дверью?"

    show un grin pioneer at right with dspr

    un "А я с ними заодно!"

    show mt angry pioneer far at center with dspr

    "После ответа Лены, вожатая перевела взгляд уже на меня. И она была явно недовольна."

    mt "Так, задание поручила тебе одному значит, а ты решил Елену запрячь!"
    me "Ха, уверяю вас, никто никого не запрягал! Это её личная инициатива, да, Лена?"

    show un smile pioneer at right with dspr

    "Она радостно закивала головой."

    show mt normal pioneer far at center with dspr

    mt "Ладно[wp] Давайте сюда обходной лист и можете идти[wp]"

    "Катя быстренько положила листок на стол к вожатой, а та убрала его в большую стопку документов."

    mt "Только далеко не уходите, уже скоро обед."

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
    un "Да! Обед же скоро, сказали."
    me "Ну, а дальше-то что? Я устал и хочу посидеть."

    if wnfh_Data.getChoice_points_sum("un") <= 5:

        jump d8_begunok_w_un_1

    else:

        jump d8_begunok_w_un_2

label d8_begunok_w_un_2:

    show un smile pioneer at left with dspr

    un "А знаешь."

    $ renpy.notify("Мб тут надо фоновый спрайт Лены на шезлонге") 

    "Лена прошлась и улеглась в шезлонг."

    show un laugh pioneer at right
    show kat confused pioneer at left
    with dspr

    un "Что-то я тоже устала."

    "Наша новенькая же, непонимающем взглядом сначала окинула меня, потом Лену и затем вновь меня."

    show un smile pioneer at right with dspr

    kat "Странный вы, мы если отсюда в столовую пойдём, в толкучку попадём."
    me "Та не, эти троглодиты быстро проталкиваются, так что как раз вовремя придём."

    "Уже разлегшаяся как у себя дома Лена, одобрительно закивала головой."

    show kat thinking pioneer at left with dspr

    kat "Ясно[wp]"

    show kat happy pioneer at left with dspr

    kat "Ну что ж, тогда и я с вами за одно посижу!"

    $ wnfh_Data.AddLove_points({"kat":1})

    "Отряхнув ступеньку, Катя аккуратно села рядом со мной."

    show kat thinking pioneer at left with dspr

    "Мы сидели в тишине несколько секунд, пока Катя не решила прервать её."

    kat "И[wp] Что мы будем делать?"
    me "Ну как что, сидеть, отдыхать и ждать обеда."
    
    show un smile2 pioneer at right
    show kat sad pioneer at left
    with dspr 

    $ renpy.notify("В будущем тут будет миниигра в «города»")

    un "Или давайте играть в города!"
    me "Обычно, те кто предлагают в это сыграть, очень хорошо знают географию[wp]"
    
    "Лена негромко засмеялась."
    
    un "Ну да, есть немного."
    me "Что ж, я согласен."
    
    show kat upset pioneer at left with dspr

    "Катя же грустно вздохнула."
    "И, судя по этом вздоху, она-то как раз географию не очень хорошо знала."
    
    kat "Ладно, давайте сыграем."
    un "Отлично. Тогда я начинаю, далее Семён, а затем ты, и так по кругу."
    me "Идёт."
    kat "Да."

    "После нашего согласия, Лена сделала задумчивый взгляд."

    un "Что же, начнём с чего-нибудь простого. Энгельс!"
    me "Мы же в города играем, а не политиков."

    "С легким смешком в голосе сказал я."

    me "Так, мне на С, ну[wp] Пусть будет Самара." 
    
    show un normal pioneer at right with dspr

    un "Что ещё за «Самара»?"

    "Данный вопрос серьёзно так поставил меня в ступор."

    me "В смысле?"
    un "В прямом."
    un "Может, ты имеешь ввиду Куйбышев?"

    th "Зараза, только начали, а я уже прокололся на такой простой теме[wp] Надеюсь не придётся выкручиватся[wp]"

    me "Я так понимаю, мой ответ не засчитан?"
    un "Абсолютно верно."
    me "Ладно, тогда пусть будет[wp] Саратов."

    "Катя же была полностью погружена в себя и, явно за игрой не следила."
    "Так что, я легонько ткнул её в плечо."

    me "Тебе на В."
    kat "А, что? Ой, точно. Так[wp] Ну, Владивосток."

    "Ну а далее, мы провели следующие минут пять играя в эти пресловутые города."
    "Зато, мы очень хорошо сократили время и не заметили, как прошли эти пять минут."

    kat "[wp]Москва!"
    me "Было уже."

    show kat surprise pioneer at left with dspr

    kat "Что, когда?"
    me "Лена говорила полминуты назад[wp]"

    play sound sfx_dinner_horn_processed

    "Вдалеке раздался горн на обед."

    un "И так, потом продолжим как-нибудь!"
    me "Да уж, увеселительная игра."

    show kat serious pioneer at left with dspr

    "Катя тут же встала и прошлась пару шагов."

    kat "Давайте уже, скорее."

    "С большим трудом, Лена поднялась с шезлонга и потянулась."

    un "Какой он удобный-то!"

    "Мне же повезло меньше вплане вставания[wp]"
    
    show kat scared pioneer at left
    show un shocked pioneer at right
    with dspr

    "А всё из-за того, что как только я начал вставать со ступеньки, мне по спине очень сильно ударила дверь, от чего я свалился на землю."

    show mt surprise pioneer panama at center with dissolve

    mt "Ох ё, вы тут чего расселись, могли у столовой подождать."
    me "В города играли[wp]"

    show kat smile pioneer at left
    show un smile pioneer at right
    show mt normal pioneer at center 
    with dspr

    "Девушки, кроме вожатой, помогли встать и отряхнули меня."

    mt "Ладно, давайте, не задерживайтесь если не хотите остаться голодными."

    window hide dissolve

    jump d8_obed_me_kat_un

label d8_begunok_w_un_1:

    "Лена посмотрела на меня каким-то около осудительным взглядом."

    hide un with dissolve2

    # Надо анимацию Лене
    $ renpy.notify("Тут надо анимацию того как уходит Лена вправо")

    "И, гордо хмыкнув, она развернулась и пошла в сторону центра лагеря."

    me "Интересно, чего это она[wp]"

    if wnfh_Data.getChoice_points_sum("kat") <= 1:

        "Катя посмотрела на меня, а потом на уходящую Лену."
        
        kat "Наверное, я тоже пойду."
        
        hide kat with dissolve
        $ renpy.notify("Надо Кате анимацию как она уходит вправо")
        
        "Сказала она и ушла вслед за Леной, оставив меня совсем одного."
        
        th "Ну, зато посижу в тишине и спокойно дождусь обеда[wp]"
        
        jump d8_obed_alone
    
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
    me "Странная говоришь?"
    
    "Катя села рядом со мной на ступеньку, перед этим аккуратно сбросив пыль с неё."
    
    kat "Ну да, настроение у неё прям переменчивое."
    kat "То перед библиотекой, то вот сейчас."
    me "Честно, не замечал никогда такого особо[wp]"
    me "Хотя, я и не общаюсь с ней толком."
    
    # удивлённый ебальник кате
    
    "Моя собеседница сильно удивилась моим словам, что было видно по её лицу."
    
    kat "А так и не скажешь, что вы мало общаетесь."
    me "Недавно вот только начали дружить[wp]"
    kat "Вот оно что[wp]"
    
    "Разумеется, наше общение с Леной и дружбой-то тяжело было назвать. Скорее, мы были как коллеги, не более того."
    
    if wnfh_Data.FlagGet("d7_me_pogulyal_w_un") == True:
    
        "Тем не менее, вчерашняя прогулка мне понравилась, пусть она и была прервана благодаря Мику."
    
    kat "И что, ты совсем тут ни с кем не общаешься? Как-то грустно это."
    me "Ну, почему ни с кем. С Алисой вот дружу хорошо."
    
    "После упоминания Алисы, Катя резко переменилась в лице."
    
    kat "Ах, та самая которая меня облила[wp] Хороший друг, ничего не скажешь."
    me "Хе, но она правда хороший друг. Только юмор у неё и Ульяны своеобразный."
    kat "Я уж заметила[wp]"
    
    "Вдалеке раздался горн на обед, что ознаменовало конец наших посиделок."
    
    me "Ну что, время обеда."
    kat "Это точно."

    jump d8_obed_me_kat

label d8_begunok_w_un_flagcheck_ne_oblil:

    $ wnfh_Data.AddLove_points({"kat":1})

    "Я и Катя проводили уходящую вдаль Лену, после чего, наша новенькая села рядом со мной, предварительно скинув всё пыль рукой."

    kat "Какая-то загадочная она[wp]"

    show kat grin pioneer at left with dspr

    kat "Как ты с ней общаешься вообще?"

    "С лёгкой насмешкой в голосе спросила она у меня."

    me "Не знаю, я с ней не общаюсь."

    show kat surprise pioneer at left with dspr

    kat "Это как так?"
    me "Ну, вот так."

    show kat thinking pioneer at left with dspr

    "Катя увела взгляд и что-то пробубнила себе под нос."

    kat "Хотя, наверное, оно и не удивительно какое у неё переменчивое настроение."

    "Тем не менее, я всё услышал, что она сказала."

    me "Что-то ты низкого мнения о ней."
    me "Она, между прочим, вероятнее всего единственная причина по которой, с тобой рыжие хвосты ничего не сделали."

    show kat interested pioneer at left with dspr

    kat "Рыжие хвосты?"
    me "Алиса и Ульяна."

    show kat laugh pioneer at left with dspr

    "Катя залилась хохотом."

    show kat grin pioneer at left with dspr

    kat "И что они сделали бы мне?"
    me "Не знаю, например, бревно уронили?"

    show kat surprise pioneer at left with dspr

    kat "Серьёзно?"
    me "Нет конечно, но зная их, точно придумали бы что-нибудь[wp]"

    show kat normal pioneer at left with dspr

    kat "Ты их так хорошо знаешь?"
    me "Ха, спрашиваешь, Алиса мой единственный друг здесь."

    show kat thinking pioneer at left with dspr

    kat "Как-то грустно это[wp]"

    "Моя собеседница грустно уставила свой взор в землю."

    me "Ну, а ты успела найти здесь друзей помимо Лены и Мику?"
    
    show kat upset pioneer at left with dspr

    kat "Нет, к сожалению."
    kat "Мне тяжело друзей заводить."

    if wnfh_Data.getChoice_points_sum("kat") == 3:

        kat "Разве что, с тобой вроде как сдружилась ещё."

    show kat normal pioneer at left with dspr

    "Так мы и провели несколько минут за обычными светскими беседами."

    play sound sfx_dinner_horn_processed

    "Единственное, что прервало нас это горн на обед."

    me "Ну, нам пора в путь."

    "Мы медленно поднялись со ступенек и отправились в столову."

    jump d8_obed_me_kat

label d8_begunok_w_un_flagcheck_me_oblil:

    $ wnfh_Data.AddLove_points({"kat":1})

    show kat normal pioneer at left with dspr
    $ renpy.notify("Возможно тут следует дать Кате анимацию передвижения, но щас кароче лень этим маяцаааа")
    "Катя проводила взглядом ушедшую Лену и, села рядом со мной."
    
    kat "Соглашусь пожалуй с тобой, устала я ходить[wp]"

    "Усевшись настолько удобно, насколько это позволяли ступеньки, она положила голову на руки и задумчиво уставилась куда-то вдаль."
    "Отследив траекторию её взгляда, я понял, что она наблюдает за уходящей Леной."

    kat "Странная она всё-таки, но забавная."
    me "Лена-то?"

    "В ответ, Катя лишь грустно угукнла."

    me "Это да[wp] Правда, я её толком и не знаю, чтобы наверняка так утверждать."

    show kat interested pioneer at left with dspr

    kat "Серьёзно?"
    me "Ну да, а что такого?"

    show kat smile pioneer at left with dspr

    kat "Хм, а выглядите как хорошие друзья."

    "Меня позабавил её ответ."

    me "Нет, действительно хороший друг у меня тут, так это Алиса."
    kat "Та самая, которая якобы подставила тебя?"
    me "Всмысле якобы?"

    show kat smile2 pioneer at left with dspr

    "Резко и, немного, грубо выдал я. А Катя лишь смеялась, по всей видимости, от моей реакции."

    kat "Я шучу. Всё же, по тебе было видно, что ты не хотел принимать прямого участия."

    show kat grin pioneer at left with dspr

    kat "К тому же, ты извинился, пусть и не совсем искренне~"

    "Последние слова из её уст прозвучали, как некий призыв к действию."
    "Прям таки читалось: «Давай, Семён, ещё раз извинись, только в этот раз более честно и искреннее»."

    window hide dissolve
    call screen wnfh_choice(
        ["Извиниться. Ещё раз", "Давай, Семён, у всё получится", "d8_begunok_w_un_appologize", {"kat":1}],
        ["Промолчать", "Я не канадец чтобы извинятся по многу", "d8_begunok_w_un_silience", {"kat": -1}],
        ["d8_choice_n7", "Семён думает извиниться ли перед Катей - рут Лены"]
        ) with sphere_blure_dissolve2

label d8_begunok_w_un_appologize:

    window show dissolve

    me "Да, перенервничал просто я тогда[wp]"
    me "Прости, пожалуйста, мне правда не хотелось тебя обливать."
    me "Мне вообще не хотелось в этом участвовать, но с дуру согласился[wp]"
     
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

    jump d8_obed_me_kat

label d8_begunok_w_un_silience:

    window show dissolve
    
    "Я предпочёл промолчать на этот очевиднеший намёк и грустно уткнулся взглядом в землю, где стал разглядывать пробегающих муравьёв."
    "Пионерка не отрывала с меня с меня свой взор ещё несколько секунд. Но, поняв, что ничего она от меня не услышит, Катя также уткнула взгляд в землю."

    kat "Ясно[wp]"

    play sound sfx_dinner_horn_processed

    "Так и сидели мы молча, дожидаясь горна на обед."

    me "Что ж, пора в путь."

    jump d8_obed_me_kat
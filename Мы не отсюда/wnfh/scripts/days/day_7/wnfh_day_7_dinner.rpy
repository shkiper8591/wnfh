label d7_zavtrak:

    window hide dissolve
    stop music fadeout 3.5
    stop ambience fadeout 2.0
    scene bg int_dining_hall_people_day with slide_right_blure_dissolve2
    play ambience ambience_dining_hall_full fadein 2.0
    window show dissolve
    ## Сцена в столовой
    if wnfh_Data.getChoice_result_number("d7_choice_n1") == 1:
        "Пришёл я в столовую, немного припозднившись, но всё равно оставалось ещё достаточно мест."
    else:
        "Пришёл я в столовую чуть ли не одним из первых."
    "Но не успел я взять свой завтрак, как все нормальные места уже были заняты."
    
    th "И как они только успевают-то?"  
    
    "Среди хотя бы немного знакомых мне людей свободное место было рядом с Алисой и Ульяной."
    "Ещё одно местечко оставалось рядом с Леной."

    window hide dissolve
    call screen wnfh_choice(
        ["un", "Сесть с Леной", "Тихо посидеть с тихоней", "d7_un_zavtrak", {"un":1}],
        ["dv", "Сесть с рыжими", "С ними должно быть весело", "d7_dv_usw_zavtrak", {"dv":1,"usw":1}],
        ["d7_choice_n2", "С кем сесть в столовой. Завтрак. Д7"]
        ) with sphere_blure_dissolve2

label d7_un_zavtrak:
    # мне короче лень ставить завтраки, у тебя, Стас, в этом опыта больше, ты и ставь. Got it?
    window show dissolve
    th "Думаю, лучше посидеть с главной стесняшей всея лагеря."
    th "А то Алиса с Ульяной – страшное комбо, они же достанут меня своими шутками."

    if wnfh_Data.getChoice_result_number("d7_choice_n1") == 1:

        th "Особенно пока я в таком побитом состоянии и весь обмазан йодом."
    
    show un normal pioneer at center with dissolve

    "Лена сидела и медленно поедала свой завтрак, не обращая на меня никакого внимания."

    me "Тут занято?"

    show un shy pioneer with dspr

    un "А, что? Н-Нет, не занято, м-можешь сесть, если хочешь."

    "Малость испуганно ответила она."

    th "Видимо, я её немного напугал своим неожиданным вопросом."

    me "Спасибки."
    if wnfh_Data.getChoice_result_number("d7_choice_n1") == 1:
        me "Доброе утро, кстати."
        
        show un smile pioneer with dspr

        un "И тебе[wp]"

        show un shocked pioneer with dspr

        "Лена стала разглядывать меня с явным удивлением."

        un "Где ты так?"
        me "Бегал."

        show un sad pioneer with dspr

        un "Бедный, что ж ты себя не бережёшь[wp]"
        un "То спину надрываешь, помогая перетаскивать тяжести, то вот[wp]"
        me "Да пустяки. {w}Но в следующий раз передай своим родителям, чтобы полегче чемоданы собирали."

        show un laugh pioneer with dspr

        un "Хорошо, обязательно передам."

        "Закончив с разговорами, я приступил к еде."

        show un shy pioneer with dspr

        "Но краем глаза заметил, что Лена снова вся засмущалась, будто хочет то ли что-то сказать, то ли спросить."

        un "И кстати[wp] Сёмо[wp] Семён[wp]"
        me "М?"
        un "Спасибо тебе за помощь."
        me "Так ты вроде ещё вчера спасибо сказала."

        show un smile3 pioneer with dspr

        un "Ну так ещё раз."
        un "Просто я бы без тебя никак не справилась."
        me "Хех, другого бы попросила[wp]"

        "Я продолжил уплетать свою овсянку."

        show un shy pioneer with dspr

        un "И ещё, Сём[wp]"
        me "В третий раз благодарить меня не надо, мне и первого раза хватило."
        un "Да не в этом дело[wp]"
        me "А в чём же?"

        "Лена замялась ещё сильнее."

        un "Ну[wp] Я-Я[wp] Ты[wp] Я[wp]"
        me "М?"
        un "В общем, я хотела сказать[wp]"

    else:
        
        "Я сел напротив неё."

        me "Ну ты даёшь, конечно! При всех Алисе нос отрывать."

        show un serious pioneer with dspr

        un "Может, о чём-то другом поговорим?"

        "Рассерженно ответила она."

        me "Извини, само как-то вырвалось."

        show un shy pioneer with dspr

        un "Ты тоже извини, я сегодня немного[wp] Сама не своя."
        me "Я заметил. А чего ты так?"

        show un sad pioneer with dspr

        un "Я-Я{w} Н-Не хочу говорить об этом[wp] По крайней мере не сейчас"
        
        show un smile pioneer with dspr

        me "Хорошо, как скажешь."

        "Проанализировав завтрак, представлявший овсянку с не пойми чем, я принялся за еду."

        show un shy pioneer with dspr

        un "Там, на площади, я не закончила из-за Алисы[wp]"
        me "Да, кстати, что ты хотела сказать?"
        un "Ох[wp]"

        "Лена сильно замялась, видимо, готовясь."

        un "В общем[wp] Ну[wp] Я[wp] Э[wp]"

        show un sad pioneer with dspr

        un "Я хотела сказать, что[wp]"

    show un normal pioneer with dspr
    
    mt "Семён!"

    "Неожиданно появившаяся вожатая прервала Лену на самом важном моменте."

    show mt normal pioneer behind chair_r:
        xcenter 1.2
        ease 2.0 xcenter 0.9
    play music music_list["two_glasses_of_melancholy"] fadein 1.5
    
    mt "Семён! Вот ты где! У меня для тебя важное партзадание!"

    th "Какое-то полнейшее невезение у Лены с этими словами, кто-то да обязательно перебьёт."

    "Говорила она, слегка запыхавшись."

    if wnfh_Data.getChoice_result_number("d7_choice_n1") == 1:
        show mt surprise pioneer behind chair_r

        mt "Ох, мне, конечно, Славя говорила, что ты упал, но что всё настолько серьёзно[wp]"
        me "Да ладно, всего лишь царапины, ничего серьёзного."
        mt "Точно?"
        me "У Виолы можете поинтересоваться. Ей виднее будет."

        show mt normal pioneer behind chair_r

        mt "Хорошо[wp] {w}Так, задание."

    me "Я вас внимательно слушаю."
    mt "К нам скоро приедет автобус, а я никак не успеваю его встретить."

    show mt sad pioneer at right with dspr

    mt "Поэтому прошу, пожалуйста, встреть наше пополнение и сопроводи ко мне."
    me "А как же Света?"
    mt "Занята."
    me "А Славя?"

    show mt angry pioneer at right with dspr

    mt "Семён, если я прошу тебя, значит больше мне некого! Хоть иногда соображай!"
    mt "Если хочешь, можешь взять кого-нибудь с собой за компанию, чтобы скучно не было."
    mt "Но задание есть задание, и оно должно быть выполнено, ясно?"
    me "Ясно."

    show mt angry pioneer:
        xcenter 0.8 ycenter 0.5

    mt "Всё тогда, быстрее доедай и шагай на остановку. У тебя в распоряжении пять-десять минут."

    show mt angry pioneer:
        ease_quart 1.5 xcenter 1.5

    "Вожатая умчалась куда-то так же быстро, как и пришла сюда."
    "Я же ускорил темп поедания завтрака."

    stop music fadeout 3.5
    show un smile pioneer with dspr

    un "Я бы могла сходить с тобой за компанию, если хочешь."

    window hide dissolve
    call screen wnfh_choice(
        ["un", "Нет, не стоит", "Одному проще и быстрее", "d7_un_no_2_lbl", {"un":-1}],
        ["un", "Да, давай", "В компании будет веселее", "d7_un_yes_2_lbl", {"un":1}],
        ["d7_choice_n3", "Пойти встречать с Леной"]
        ) with sphere_blure_dissolve2

label d7_un_no_2_lbl:
    window show dissolve

    me "Думаю, я сам справлюсь, а тебя напрягать особо не хочется."

    show un normal pioneer with dspr

    "Она грустно вздохнула."
    
    un "Ну ладно." 

    "Менее чем за минуту я управлися с овсянкой, а чай прикончил и вовсе за один глоток."

    me "Ну всё, я помчался."
    un "Удачи тебе."
    me "Ага, спасибо, тебе тоже."

    jump d7_me_meet_kat_alone

label d7_un_yes_2_lbl:
    window show dissolve

    me "Думаю, вместе будет веселее."
    un "Я вот тоже так считаю."

    "Радостным голосом сказала она."

    me "Только тебе следует поторопится."
    me "Я вот уже почти всё съел, а тебя ещё полтарелки."
    un "Да[wp] {w}Не хочу я овсянку эту. Сколько можно её уже подавать?"
    me "Зато наполнение другое, хе-хе."

    "Лена отодвинула тарелку с кашей в сторону и стала медленно потягивать чай."
    "Я же съел всё меньше чем за минуту, а подостывший чай и вовсе выпил за один глоток."

    show un shocked pioneer with dspr

    un "В-Вау."
    me "Что?"
    un "Ты хотя бы вкус успел почувствовать?"
    me "Не знаю. Да и неважно, давай скорее разберёмся с пополнением и всё."

    show un smile pioneer with dspr

    un "Согласна."

    jump d7_me_meet_kat_w_un

label d7_dv_usw_zavtrak:
    window show dissolve

    th "Конечно, сидеть с ними было сомнительным удовольствием, ибо они – те ещё любители колких шуток."
    th "Но куда уж деваться, Алиса – единственный человек из здесь находящихся, с которым есть о чём поговорить и которую я могу назвать другом."
    ## Стас, поправь Ульяну. Если ты это не сделаешь, то я сожру тебя с говном. 
    ## Диалог с рыжими
    show chair_l behind usw
    show chair_r behind dv
    show usw grin pioneer at wnfh_sit_left behind table
    show dv normal pioneer at wnfh_sit_right behind table
    show table
    show shakers
    show left d11_breakfast_full tray foods behind shakers
    show right d11_breakfast_full tray foods behind shakers
    with dissolve
    
    "Подойдя к ним, я сразу заметил, что Ульяна, уставившись на меня, давит ехидную лыбу."
    
    me "Можно к вам сесть?"
    dv "Да, можно."
    usw "Конечно!"
    
    show mid d11_breakfast_full tray spoon foods
    with dissolve
    #34 звук того, что он поставил поднос на стол
    "Хитрым голосом сказала Ульянка."
    
    th "Ох, не нравится мне всё это, по любому опять что-то с Алисой затеяли и хотят меня к себе завербовать."
    
    "Усевшись за стол, я бегло изучий свой завтрак."
    
    me "Что это такое?"
    usw "Овсянка, сэр!"
    me "Сколько можно подавать чёртову овсянку?"
    dv "Скажи спасибо, что наполнение другое."
    
    "Грустно угукнув и закончив анализ пищи, я принялся с большой скоростью уплетать свой завтрак."

    if wnfh_Data.getChoice_result_number("d7_choice_n1") == 1:
        usw "Семён, а ты в чём весь?"
        me "В йоде."
        show usw surp2 pioneer at wnfh_sit_left behind table with dspr
        usw "Подрался, что ли?"
        dv "Не думаю, что самый неконфликтный человек во всём лагере мог с кем-нибудь подраться."
        me "Упал."
        show usw upset pioneer at wnfh_sit_left behind table with dspr
        usw "Эх, скукота какая."
        dv "Как я и думала."
        dv "Кстати."
    
    show mid d11_breakfast_full tray foods with dspr
    show left d11_breakfast_half tray foods with dspr
    
    dv "Семён, а ты чем сегодня заниматься думаешь?"
    me "Продолжу с моделистами моделировать. {w}А что?"
    dv "Да вот[wp]"
    
    show usw laugh pioneer at wnfh_sit_left behind table with dspr
    
    usw "На свиданку тебя позвать хочет!"
    
    "Довольно громко выдала Ульяна, от чего некоторые пионеры поблизости странно покосились на нас."
    
    show dv angry pioneer at wnfh_sit_right behind table with dspr
    
    dv "Да я тебе щас!"
    
    "Алиса дала Ульяне лёгкий подзатыльник."
    
    show usw upset pioneer at wnfh_sit_left behind table with dspr
    
    usw "Ой, да ладно тебе, пошутить уже нельзя?"
    dv "Нет, такие шутки нельзя шутить!"
    
    show dv shy pioneer at wnfh_sit_right behind table with dspr
    
    dv "Я вовсе не собиралась его куда-то звать."
    dv "А просто поинтересовалась по-дружески[wp]"
    
    "Застенчивым голосом сказала Алиса."
    "Ульяна же быстро вернулась к своему нормальному состоянию."
    
    show usw normalsmile pioneer at wnfh_sit_left behind table with dspr
    
    usw "Ну-ну!"
    me "Мдэ[wp]"
    
    "Стоило мне вернуться к своему завтраку, как тут же к нам чуть ли не подбежала Ольга Дмитриевна."
    ## Просьба ОД
    show mt normal pioneer behind chair_r:
        xcenter 1.2
        ease 2.0 xcenter 0.9
    play music music_list["two_glasses_of_melancholy"] fadein 1.5
    
    mt "Семён! Вот ты где! У меня для тебя важное партзадание!"

    "Говорила она, малость, запыхавшись."

    if wnfh_Data.getChoice_result_number("d7_choice_n1") == 1:
        show mt surprise pioneer behind chair_r

        mt "Ох, мне, конечно, Славя говорила, что ты упал, но что всё настолько серьёзно[wp]"
        me "Да ладно, всего лишь царапины, ничего серьёзного."
        mt "Точно?"
        me "У Виолы можете поинтересоваться. Ей виднее будет."

        show mt normal pioneer behind chair_r

        mt "Хорошо[wp] {w}Так, задание."
    
    show right d11_breakfast_half tray foods with dspr
    
    me "Я вас слушаю."
    mt "Доедай давай быстрее и иди на остановку."
    me "А зачем?"
    
    "Вожатая посмотрела на двух рыжих пионерок, будто не желая говорить это перед ними."
    "Но, тяжело вздохнув, она продолжила."
    
    mt "К нам пополнение приезжает, надо его встретить и сопроводить ко мне."
    
    show dv smile pioneer at wnfh_sit_right behind table with dspr
    show usw smile pioneer at wnfh_sit_left behind table with dspr
    
    "После её слов Ульяна и Алиса быстренько перекинулись хитрыми взглядами."
    
    th "Не к добру это всё, явно что-то придумали."
    
    mt "Прости, что так резко, но я просто не успеваю, а Славя занята сейчас."
    me "А Планш[wp] То есть Света?"
    mt "Светлана сейчас занята куда более {i}важными{/i} делами."
    me "Ладно[wp]"
    
    "Вздохнув, я посмотрел на вожатую недовольным взглядом."
    
    th "Чёрт, ну почему опять я должен всё делать? Что, на весь лагерь никого больше не найдётся?"
    th "Да ещё прямо посреди завтрака человека напрягать, отправлять на какое-то задание[wp] {w}Достало! Не буду соглашаться!"
    
    show mt smile pioneer behind chair_r with dspr
    
    mt "Пожалуйста. А я тебе прощу твои ночные гуляния."
    
    show mid d11_breakfast_half tray foods with dspr
    
    th "А вот такое предложение звучало куда интереснее[wp] {w}Таки и надо было с этого начинать!"
    
    me "Ладно, сейчас доем и пойду встречать."
    mt "Спасибо тебе огромное!"
    
    show mt normal pioneer behind chair_r:
        xcenter 0.9
        ease 1.5 xcenter 1.2
    $ renpy.pause(2.0, hard=True)
    hide mt with dissolve
    
    "Когда вожатая удалилась куда-то вглубь столовой, Алиса немного приподнялась и наклонилась ко мне."

    dv "Слушай, Семён."
    me "М?"

    "Она легонько хихикнула."

    show dv laugh pioneer at wnfh_sit_right behind table with dspr

    dv "А может пополнение-то, таво, по-пионерски встретить, так сказать?"

    "Я не очень понял, что она имела ввиду."

    th "Мне вот известно, как костёр по-пионерски тушить, но чёт не особо представляю встречу человека таким образом[wp]"

    me "То есть?"
    
    show usw grin pioneer at wnfh_sit_left behind table with dspr

    usw "То есть облить из ведра."

    "Резко вставила свои пять копеек Ульяна."

    me "О как."
    me "А если там не один-два человека, а скажем[wp] Десять?"

    show dv normal pioneer at wnfh_sit_right behind table with dspr

    dv "Мысль верная, конечно[wp]"

    "Задумчиво проговорила Алиса."

    show dv smile pioneer at wnfh_sit_right behind table with dspr

    dv "Только вот тут на такое количество народу мест не найдётся."

    show dv grin pioneer2 at wnfh_sit_right behind table with dspr

    dv "Так что можешь не беспокоиться по этому поводу."
    usw "Ну что, ты в деле?"

    window hide dissolve

    call screen wnfh_choice(
        ["dv", "Чёрт возьми, да!", "Звучит очень весело, хе-хе", "d7_dv_yes_1", {"dv":1}],
        ["dv", "Думаю, нет", "Не хочу портить свою репутацию", "d7_dv_no_1", {"dv":-1}],
        ["d7_choice_n8", "Алиса предлагает облить пополнение в лагере."]
        ) with sphere_blure_dissolve2

label d7_dv_yes_1:

    "Взвесив все за и против, я решил, что это – отличная идея."

    me "Думаю, это будет весело."
    dv "А то!"
    usw "Хи-хи, ну что, быстренько доедаем и в путь за ведром!"

    "Мы одобрительно кивнули и принялись за еду. Закончив с ней, мы немедля покинули столовую."

    jump d7_me_meet_kat_w_dw_n_usw

label d7_dv_no_1:

    "Идея, мягко говоря, звучала ужасно, и я никак не мог подписаться на что-то подобное."

    show dv normal pioneer at wnfh_sit_right behind table with dspr

    me "Пожалуй, откажусь. Мне это не сильно интересно. К тому же вожатая потом даст мне просраться."
    dv "Что ж, ладно."

    "Алиса медленно вернулась на своё место."
    "А я же с удвоенной силой принялся за завтрак, и уже через минуту от него ничего не осталось."
    
    show mid d11_breakfast_empty tray spoon with dspr
    
    me "Так, всё, дамы, я опаздываю. Чао-какао."
    
    show usw dontlike pioneer at wnfh_sit_left behind tableм with dspr 
    
    "Я встал из-за стола."
    
    usw "Эй, а убирать за тобой кто будет?"
    # тут можно добавить выбор с тем что убирать поднос за собой или нет !7
    "Недовольным голосом сказала Ульянка."
    
    me "Извини, подруга, у меня важное задание, нет времени на такие мелочи."
    
    scene bg int_dining_hall_people_day with dissolve2
    
    "Сказал я и, помохав рукой на прощание, быстро удалился из столовой."

    stop music fadeout 5.0
    jump d7_me_meet_kat_alone
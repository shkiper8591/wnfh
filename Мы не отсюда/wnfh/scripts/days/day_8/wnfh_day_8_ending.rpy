label d8_ending:

    window hide dissolve
    stop ambience fadeout 2.0
    $ wnfh_set_time()
    scene bg ext_lenin_square_night_wnfh with dissolve2
    play ambience ambience_camp_center_night fadein 2.0
    $ renpy.pause(0.5)
    scene bg ext_houses_night_wnfh with dissolve2
    $ renpy.pause(0.5)
    scene bg ext_house_of_mt_night with dissolve2
    $ renpy.pause(0.5)
    stop ambience fadeout 2.0
    scene bg int_house_of_mt_night 
    show mt normal nightdress at center
    with dissolve2
    play ambience ambience_int_cabin_night fadein 2.0
    $ renpy.pause(0.3)
    window show dissolve

    "Тихонько я вошел в дом."
    "Вожатая там уже готовила свою постель ко сну и, видимо, не услышала как я зашёл."

    mt "Ох, хоть бы сегодня он пришёл вовремя."
    me "Это вы про меня?"

    show mt surprise nightdress at center with dspr

    "Ольга Дмитриевна от испуга резко повернулась и схватилась за сердце."

    mt "Господи, Семён, напугал."
    me "Извините."

    show mt smile nightdress at center with dspr

    mt "Так-так, неужели наша сова вовремя пришла на отбой?"
    me "Сам в шоке."

    show mt grin nightdress at center with dspr

    mt "Я надеюсь завтра не пойдёт снег."

    show mt normal nightdress at center with dspr

    "Я устало подошел к кровати и уселся на неё."
    "Быстро сняв в себя всю форму, я улёгся под одеяло."

    mt "Ну-с, спокойной ночи."

    $ wnfh_set_time("night")

    show bg int_house_of_mt_night2 with dspr
    hide mt with dissolve

    "Ольга Дмитриевна выключила свет и тоже легла в постель."

    me "И вам спокойной ночи[wp]"

    window hide dissolve
    stop ambience fadeout 2.0
    show blink
    with None
    $ renpy.pause(3.0)
    scene black
    stop ambience fadeout 2.0
    $ renpy.pause(1.5, hard=True)
    jump d9_morning

label d8_ending_dv:
    
    scene bg ext_house_of_mt_night with dissolve2

    "Я прошёл пару метров и остановился перед домиком вожатой."

    th "Свет горит[wp] Тут два варианта, либо за меня волнуются, либо Лена не врала."
    th "И я очень надеюсь, что это первый вариант."

    $ wnfh_set_time()
    window hide dissolve
    stop ambience fadeout 2.0
    scene bg int_house_of_mt_night
    show mt walk_1 wlk background
    with dissolve
    play ambience ambience_int_cabin_night fadein 2.0
    $ renpy.pause(0.3)
    window hide dissolve
    $ renpy.notify("Тут должна быть анимация того, как вожатая ходит туда сюда, но пока-что этого нет")
    
    "Тихо войдя внутрь, я застал вожатую ходящую от одного стенки дома до другой."
    "А на лице её читались глубокие раздумия и немного злости."

    me "Здравствуйте."

    hide mt with dspr
    $ renpy.pause(0.1)
    show mt angry nightdress at center with dissolve

    "Как только я дал о себе знать, вожатая подняла на меня свой недовольный взгляд."

    me "Простите, что как обычно поздно прихожу."
    me "Загулял просто."
    mt "Я вижу, что загулял."
    mt "Вернее услышала."

    "И тут мне стало понятно, что всё же второй вариант правильный."

    mt "Двенадцать часов ночи, а ты музыку на весь лагерь играешь!"
    mt "Так и ещё такую дурацкую!"

    "Я стыдливо опустил взгляд в пол."

    show mt normal nightdress at center with dspr

    mt "Семён, у меня просто нет слов."
    mt "В общем, это была последняя твоя ночная прогулка."
    mt "Я многое могла терпеть, многое могла простить."
    mt "Я простила твоё гуляние по крыше клубов."

    "Она вытянула руку и начала загибать пальцы."

    mt "Я простила ваш с Алисой саботаж, когда в душе шла только горячая вода."
    mt "Я даже простила, как ты разгромил Жене библиотеку, хотя она очень долго возмущалась мне по этому поводу."

    "Лукаво улыбнувшись я поднял взгляд обратно на вожатую."

    me "Ну слушайте, была же установка вести себя естественно, вот и выполняю приказ."
    mt "Да, но это не значит, что ты должен мешать остальным."
    mt "Короче! Это уже нельзя просто так оставлять."
    mt "А значит, завтра будет ждать тебя наказание."

    if wnfh_Data.FlagGet("mt_angry") == True:

        mt "При этом двойное уже."

    "Наконец, вожатая отошла в сторону, пропуская меня дальше в дом."
    "Разумеется, я незамедлительно воспользовался такой возможностью и, быстренько сняв форму, лег под одеяло."

    $ wnfh_set_time("night")
    show bg int_house_of_mt_night2 with dspr

    "Грустно вздохнув, вожатая выключила свет в доме."

    hide mt with dissolve

    "После чего она подошла к своей кровати и легла в постель."

    mt "Спокойной ночи."
    me "И вам спокойной."

    window hide dissolve
    show blink
    with None
    stop ambience fadeout 2.0
    $ renpy.pause(3.0)
    scene black
    $ renpy.pause(1.5, hard=True)
    jump d9_morning
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

    "Я тихонько вошёл в дом."
    "Вожатая уже готовила свою постель ко сну и, видимо, не услышала, как я зашёл."

    mt "Ох, хоть бы сегодня он пришёл вовремя."
    me "Это вы про меня?"

    show mt surprise nightdress at center with dspr

    "Ольга Дмитриевна от испуга резко повернулась и схватилась за сердце."

    mt "Господи, Семён! Напугал[wp]"
    me "Извините."

    show mt smile nightdress at center with dspr

    mt "Так-так, неужели наша сова вернулась к отбою?"
    me "Сам в шоке."

    show mt grin nightdress at center with dspr

    mt "Надеюсь, завтра не пойдёт снег!"

    show mt normal nightdress at center with dspr

    "Я устало подошёл к кровати и уселся на неё."
    "Быстро сняв с себя форму, я забрался под одеяло."

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

    "Я дошёл до домика вожатой и остановился на входе."

    th "Свет горит[wp] Тут два варианта: либо за меня волнуются, либо Лена не врала."
    th "И я очень надеюсь, что верным окажется первый."

    $ wnfh_set_time()
    window hide dissolve
    stop ambience fadeout 2.0
    scene bg int_house_of_mt_night
    show mt walk_1 wlk background
    with dissolve
    play ambience ambience_int_cabin_night fadein 2.0
    $ renpy.pause(0.3)
    window hide dissolve
    $ renpy.notify("Тут должна быть анимация того, как вожатая ходит туда-сюда, но пока что этого нет")
    
    "Тихо войдя внутрь, я застал вожатую, ходящую от одной стенки дома к другой."
    "На лице её читались глубокие раздумья. И немного злости."

    me "Здравствуйте."

    hide mt with dspr
    $ renpy.pause(0.1)
    show mt angry nightdress at center with dissolve

    "Как только я дал о себе знать, вожатая подняла на меня свой недовольный взгляд."

    me "Простите, что опять поздно пришёл."
    me "Загулял просто."
    mt "Я вижу, что загулял."
    mt "Вернее, услышала."

    "И тут мне стало понятно, что всё же правильным был второй вариант."

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
    mt "Я даже простила погром в библиотеке, хотя Женя очень долго возмущалась мне по этому поводу."

    "Лукаво улыбнувшись, я поднял взгляд обратно на вожатую."

    me "Ну слушайте, была же установка вести себя естественно, вот я и выполняю приказ."
    mt "Да, но это не значит, что ты должен мешать остальным."
    mt "Короче! Это уже нельзя просто так оставлять."
    mt "А значит, завтра тебя будет ждать наказание."

    if wnfh_Data.FlagGet("mt_angry") == True:

        mt "Причём двойное!"

    "Наконец вожатая отошла в сторону, пропуская меня в дом."
    "Разумеется, я незамедлительно воспользовался такой возможностью и, быстренько сняв форму, лёг под одеяло."

    $ wnfh_set_time("night")
    show bg int_house_of_mt_night2 with dspr

    "Ольге Дмитриевне оставалось лишь печально вздохнуть."

    hide mt with dissolve

    "Она выключила свет, подошла к своей кровати и легла."

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
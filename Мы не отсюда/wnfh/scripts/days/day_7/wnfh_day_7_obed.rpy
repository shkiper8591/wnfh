label d7_obed:

    window hide dissolve
    scene bg ext_dining_hall_away_day with slide_right_blure_dissolve2
    window show dissolve
    
    "Прибыв на место, я к своему удивлению приметил, что у столовой всё ещё толпилось приличное число пионеров."
    "От чего появилась хоть и небольшая, но надежда занять отличное место в глубине столовой и посидеть в гордом одиночестве."
    "А то в последнее время мне как-то особо не удаётся."
    
    window hide
    stop ambience fadeout 0.5
    scene bg int_dining_hall_day with sphere_blure_dissolve2
    play ambience ambience_dining_hall_empty fadein 3 
    window show

    "И действительно, внутри пока было не очень многолюдно." 
    "А посему я как можно быстрее взял поднос с едой и ушёл в самый дальний угол столовой."
    "Там я занял вполне уютное местечко у окна. Правда, вид из него был не самый интересный."
    
    window hide
    show chair_l behind table
    show chair_r behind table
    show table
    show shakers behind mid
    with dissolve
    
    stop ambience fadeout 0.5
    show bg int_dining_hall_people_day with dissolve2
    play ambience ambience_dining_hall_full fadein 3
    
    show mid d10_dinner_full tray spoon foods with dissolve
    window show

    "Как только я занял своё место, столовая чуть ли не в миг наполнилась пионерами."
    
    show un normal pioneer behind chair_r:
        xcenter 1.2
        ease_quart 4.0 xcenter 0.6
    show kat normal pioneer behind chair_r:
        xcenter 1.4 
        ease_quart 5.0 xcenter 0.8
    ## Семён, Лена и Катя в столовой

    if wnfh_Data.FlagGet("me_neznayu_imya_kat") == True:

        "И я было уже начал есть, как ко мне подошли Лена и наша новенькая."

    else:

        "И я было уже начал есть, как ко мне подошли Лена и[wp] {w}Катя?"
    
    th "Ну да, так просто одному пообедать никогда не выходит."
    
    show un shy pioneer behind chair_r with dspr
    
    un "Можно мы к тебе сядем?"
    
    window hide dissolve
    call screen wnfh_choice(
        ["un", "Можно", "Ладно, пусть садятся", "d7_obed_me_w_un_kat", {"kat":1, "un":1}],
        ["neutral", "Не можно", "Хочется поесть одному", "d7_obed_me_alone", {"kat":-1, "un":-1}],
        ["d7_choice_n6", "Разрешить сесть рядом Кате и Лене в столовой"]
        ) with dissolve2

label d7_obed_me_alone:

    window show dissolve

    th "Ох, не хочется мне сейчас сидеть с кем-то в компании."

    if wnfh_Data.getChoice_points_sum("un") <= 0: 

        me "Аэ[wp] Тут[wp] Э[wp] З-Занято, да. Я тут занял ребятам из клубов."

        show un normal pioneer behind chair_r with dspr

        un "Правда?"

        "Она посмотрела в сторону."
        "Я посмотрел туда же и увидел сидящих там Серёгу и Шурика."

        $ wnfh_set_name("kat", "Катя")

        un "Ну хорошо. {w}Пойдём, Кать, тут занято."

        show un normal pioneer behind chair_r, chair_l:
            ease_quart 4.0 xcenter -0.6
        show kat normal pioneer behind chair_r, chair_l:
            ease_quart 5.0 xcenter -0.6

        "Лена напоследок бросила на меня недовольный взгляд, после чего девушки ушли."

        th "Зараза[wp]"
        hide un
        hide kat
        "С малость подпорченным настроением я принялся уплетать обед."
        "И быстро расправившись с ним, я покинул пределы столовой."

        jump d7_posle_obeda

    elif wnfh_Data.getChoice_points_sum("un") == 1:

        me "Простите, тут сейчас занято[wp] Да[wp]"

        show un normal pioneer behind chair_r with dspr

        if wnfh_Data.FlagGet("me_neznayu_imya_kat") == True:

            "Лена посмотрела на меня, потом на новенькую, после чего пожала плечами."

        else:

            "Лена посмотрела на меня, потом на Катю, после чего пожала плечами."

        $ wnfh_set_name("kat", "Катя")

        un "Что ж, ну ладно. {w}Пойдём, Кать, здесь занято."

        hide un
        hide kat
        with dissolve

        "Катя грустно угукнула, и девушки удалились вглубь столовой."
        "Когда они ушли, я принялся уплетать свой обед."
        "И, закончив с ним, я быстренько отправился на выход из столовой."

        jump d7_posle_obeda

    else:

        me "Извините, дамы, но я занял тут своим товарищам."
        me "Просто они пока отлучились по делам."

        show un smile pioneer behind chair_r with dspr

        "Лена слегка улыбнулась."

        un "Ой, это ты нас извини."

        show un grin pioneer behind chair_r with dspr

        $ wnfh_set_name("kat", "Катя")

        un "Ну-с, тогда не будем мешать. Пойдём, Кать. {w=1.0}Кстати, приятного аппетита!"
        me "Спасибо большое."

        hide un
        hide kat
        with dissolve

        "Девушки удалились куда-то вглубь столовой, а я принялся за обед."
        "С которым довольно быстро расправился, после чего направился на выход из столовой."

        jump d7_posle_obeda

label d7_obed_me_w_un_kat:

    window show dissolve

    me "Да, конечно, садитесь."
    
    show un smile pioneer with dspr
    
    un "Спасибо!"
    
    window hide
    show un smile pioneer at go_to_chair_left behind table
    show kat normal pioneer at go_to_chair_right behind chair_r
    $ renpy.pause(1.0, hard=True)
    
    show chair_r at chair_move_out behind un
    $ renpy.pause(0.3, hard=True)
    show chair_l at chair_move_out behind kat
    $ renpy.pause(0.7, hard=True)
    
    show un smile pioneer at sit_down_left
    $ renpy.pause(0.3, hard=True)
    show kat normal pioneer at sit_down_right
    $ renpy.pause(1.0, hard=True)
    
    show chair_l at chair_move_in
    $ renpy.pause(0.3, hard=True)
    show chair_r at chair_move_in
    show left d10_dinner_full tray spoon foods behind mid 
    show right d10_dinner_full tray spoon foods behind mid 
    with dissolve
    window show
    
    "Девочки сели, а я полностью сосредоточился на обеде, коим был суп, а точнее — летние щи."
    
    show mid d10_dinner_full tray foods with dissolve
    
    th "Как же давно такие не ел[wp] Наверное, лет пять или шесть."
    
    show left d10_dinner_full tray foods with dissolve
    show right d10_dinner_full tray foods with dissolve
    
    th "На даче стоял жаркий летний день, и отец наготовил целую кастрюлю этих щей[wp]"
    th "Щей? Щий? Супа, в общем."
    
    if wnfh_Data.FlagGet("me_neznayu_imya_kat") == True:

        "За своими раздумьями я не обращал внимания на увлечённо о чём-то болтающих Лену и[wp]"

        th "Кстати, как нашу новенькую зовут-то?"

        me "Дамы, простите, что перебиваю вас, но[wp] Лена, можешь представить мне свою подругу?"
        me "А то я её имени не знаю до сих пор."
        un "Вот как? Ну что ж, знакомьтесь. Семён, это Катя. Катя, это Семён."

        $ wnfh_set_name("kat", "Катя")

        kat "Ага[wp]"

        "Катя отозвалась без особого энтузиазма."

        un "Вот и познакомились. А теперь, Семён, изволь мы продолжим наш диалог."

    else:

        "За своими раздумьями я не обращал внимания на увлечённо о чём-то болтающих Лену и Катю."
    
    show mid d10_dinner_half tray foods with dissolve
    
    "Не знаю почему, но мне стало крайне любопытно, о чём же они там разговаривают."
    
    me "О чём болтаете?"
    
    show un shy pioneer
    show kat shy pioneer 
    with dspr
    
    "После моего вопроса они залились румянцем, будто я спросил о чём-то неприличном."
    "И лишь спустя время Лена взяла на себя инициативу."
    
    show un grin pioneer with dspr
    show right d10_dinner_half tray foods with dissolve
    
    # тут бы тоже вставить проверку ЛП

    un "Боюсь, {i}Сёмочка{/i}, это не твоё дело."
    th "Сёмочка? {w}Меня так ещё никто не называл тут."
    un "Так, о разных девичьих темах, которые тебе, парню, не понять."
    me "А если пойму?"
    
    "Я ухмыльнулся, полагая, что переиграл её."
    
    show left d10_dinner_half tray foods with dissolve
    show un laugh pioneer with dspr 
    
    un "Тогда у меня для тебя плохие новости!"
    
    show kat happy pioneer with dspr
    
    "Лена засмеялась, а немного погодя захихикала и Катя."
    "Я же не сразу понял, за что именно меня подстебали, но зато быстро понял, что моё переигрывание было переиграно."
    "И лишь несколькими секундами позже я всё осознал." 
    
    me "Ааааа[wp] {w}Ладно уж, храните свои секреты."
    
    show un normal with dspr
    show kat normal with dspr
    
    "Лена одобрительно угукнула и продолжила диалог с Катей."
    "А я вернулся к своему обеду."
    "И мимоходом я всё же подслушал, о чём болтали девочки."
    "Но, как и предупреждала Лена, я ничего не понял, так что интерес пропал сам собой."
    
    th "А эта новенькая быстро нашла себе друга. Не то что я."
    th "Интересно, почему именно Лена? {w}Хотя учитывая то, как скромно она себя вела и какая стесняша у нас Тихонова, все вопросы отпадают сами собой."
    
    show mid d10_dinner_empty tray spoon foods with dissolve
    
    "За моими размышлениями суп кончился довольно быстро."
    "Чай тоже держался недолго и был выпит одним залпом."
    
    hide mid with dissolve
    
    me "Ладненько, пойду я."
    un "Пока!"
    kat "Угу."
    
    scene bg int_dining_hall_people_day with dissolve
    
    "Встав из-за стола, я быстренько отнёс поднос и покинул пределы столовой."

    jump d7_posle_obeda
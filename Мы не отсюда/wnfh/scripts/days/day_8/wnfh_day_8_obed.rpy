label d8_obed_me_alone_alt:

    window hide dissolve
    stop ambience fadeout 5.0
    scene bg ext_dining_hall_near_day 
    show dv normal pioneer at center
    with slide_right_blure_dissolve5
    play ambience ambience_camp_center_day fadein 5.0
    $ renpy.pause(1.0)
    window show dissolve

    "placeholder"

    jump d8_obed_me_kat_mi

label d8_obed_me_alone:

    window hide dissolve
    scene bg ext_dining_hall_away_day with slide_up_blure_dissolve2
    $ renpy.pause(1.0)
    scene bg ext_dining_hall_near_day with dissolve
    $ renpy.pause(1.0)
    window show dissolve

    "placeholder"

    jump d8_obed_me_kat_mi

label d8_obed_me_kat_un:

    window hide dissolve
    scene bg ext_dining_hall_away_day with slide_up_blure_dissolve2
    $ renpy.pause(1.0)
    scene bg ext_dining_hall_near_day with dissolve
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
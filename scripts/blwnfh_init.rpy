init 0:
    $ mods["blwnfh_main"]=u"Мы не отсюда"

    transform running:
        block:
            zoom 1.1 xcenter 0.5 ycenter 0.5
        block:
            ease 0.2 xoffset 0 yoffset 0
            ease 0.2 xoffset 25 yoffset 50
            ease 0.2 xoffset 0 yoffset 0
            ease 0.2 xoffset -25 yoffset 50
        repeat
        
    transform fatigue:
        block:
            zoom 1.4 xcenter 0.5 ycenter 0.3
        block:
            ease 1 xoffset 0 yoffset 0
            ease 1 xoffset 15 yoffset 40
            ease 1 xoffset 0 yoffset 0
            ease 1 xoffset -15 yoffset 40
        repeat

    transform hello_t:
        align (0.7, 0.5) alpha 0.0
        linear 0.5 alpha 1.0



label blwnfh_main:
    $ persistent.sprite_time = "day"
    $ day_time()
    scene bg ext_square_day with dissolve
    

    $ set_mode_nvl()

    nvlkat "Fuck you"
    "Asshole"
    nvlkat "Клуб любителей кожевного мастерства на один этаж ниже"

    $ set_mode_adv()
    
    
    show kat 1 pioneer with dspr
    "Пионер 1"
    show kat 2 pioneer with dspr
    "Пионер 2"
    show kat 3 pioneer with dspr
    "Пионер 3"
    show kat 1 kupalnik with dspr
    "Купальник 1"
    show kat 2 kupalnik with dspr
    "Купальник 2"
    show kat 3 kupalnik with dspr
    "Купальник 3"
    show kat 1 povsedn with dspr
    "Повседневка 1"
    show kat 2 povsedn with dspr
    "Повседневка 2"
    show kat 3 povsedn with dspr
    "Повседневка 3"
    show kat 1 povsedn rubashka with dspr
    "Повседневка с рубашкой 1"
    show kat 2 povsedn rubashka with dspr
    "Повседневка с рубашкой 2"
    show kat 3 povsedn rubashka with dspr
    "Повседневка с рубашкой 3"
    
    show sl upset pioneer at left with dspr
    
    show mt smile pioneer panama with dspr
    mt "Бегунок нужно заполнить, я его дам"
    mt "Карту лагеря нужно запомнить, её я не дам"
    hide mt with dspr
    
    "Мы запускаем лохотрон"

    jump blwnfh_day1
    
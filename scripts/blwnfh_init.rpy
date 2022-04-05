init python:
    far_size = (675, 1080)
    # Git test
    blwnfh_far_kat = "mods/blwnfh/images/sprites/far/kat/"
    
    kat = Character(u'Катя', color="#ff97bb", ctc="ctc_animation", ctc_position="fixed", what_color="#e2c778", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    ukat = Character(u'Девушка', color="#ff97bb", ctc="ctc_animation", ctc_position="fixed", what_color="#e2c778", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    renpy.image("kat normal2 pioneer far", ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite(far_size, (0, 0), blwnfh_far_kat + "kat_1_body.png", (0, 0), blwnfh_far_kat + "kat_1_pioneer.png", (0, 0), blwnfh_far_kat + "kat_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite(far_size, (0, 0), blwnfh_far_kat +  "kat_1_body.png", (0, 0), blwnfh_far_kat + "kat_1_pioneer.png", (0, 0), blwnfh_far_kat + "kat_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite(far_size, (0, 0), blwnfh_far_kat + "kat_1_body.png", (0, 0), blwnfh_far_kat + "kat_1_pioneer.png", (0, 0), blwnfh_far_kat + "kat_1_normal.png")))
 
init:
    $ mods["blwnfh_main"]=u"Мы не отсюда"
    
    # Персонажи #
        
    # Инициализация спрайтов #
    
    
    
    # Катя злая
    #image kat angry pioneer
    #image kat angry pioneer close
    #image kat angry pioneer far
    
    # Катя плачет
    #image kat cry pioneer
    #image kat cry pioneer close
    #image kat cry pioneer far
    
    # Катя ухмыляется                 
    #image kat grin pioneer
    #image kat grin pioneer close             
    #image kat grin pioneer far
    
    # Катя виноватая                                         
    #image kat guilty pioneer
    
    #image kat guilty pioneer close
    
    #image kat guilty pioneer far
    
    # Катя смеётся                                         
    #image kat laugh pioneer
    
    #image kat laugh pioneer close  
    
    #image kat laugh pioneer far
    
    # Катя обычная                                         
    #image kat normal pioneer
    #image kat normal pioneer close
    image kat normal pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), blwnfh_far_kat + "kat_1_body.png", (0, 0), blwnfh_far_kat + "kat_1_pioneer.png", (0, 0), blwnfh_far_kat + "kat_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), blwnfh_far_kat + "kat_1_body.png", (0, 0), blwnfh_far_kat + "kat_1_pioneer.png", (0, 0), blwnfh_far_kat + "kat_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((900, 1080), (0, 0), blwnfh_far_kat + "kat_1_body.png", (0, 0), blwnfh_far_kat + "kat_1_pioneer.png", (0, 0), blwnfh_far_kat + "kat_1_normal.png"))



    
    
    # Катя в ярости                                         
    #image kat rage pioneer
    #image kat rage pioneer close
    #image kat rage pioneer far
    
    # Катя грустная                                         
    #image kat sad pioneer
    #image kat sad pioneer close              
    #image kat sad pioneer far
    
    # Катя напуганная
    #image kat scared pioneer
    #image kat scared pioneer close           
    #image kat scared pioneer far 
    
    # Катя шокированная                                        
    #image kat shocked pioneer
    #image kat shocked pioneer close          
    image kat shocked pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_body.png", (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_pioneer.png", (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0)),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_body.png", (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_pioneer.png", (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((900, 1080), (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_body.png", (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_pioneer.png", (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_shocked.png"))

    
    # Катя застенчивая                                         
    #image kat shy pioneer
    #image kat shy pioneer close              
    #image kat shy pioneer far
    
    # Катя улыбается                                         
    #image kat smile pioneer
    #image kat smile pioneer close
    image kat smile pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_body.png", (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_pioneer.png", (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_body.png", (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_pioneer.png", (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((900, 1080), (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_body.png", (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_pioneer.png", (0, 0), "mods/blwnfh/images/sprites/far/kat/kat_1_smile.png"))
    
    # Катя удивлённая                                         
    #image kat surprise pioneer               
    #image kat surprise pioneer close         
    #image kat surprise pioneer far           
    
    # Переменные #

    # BG #
    
    $ blwnfh_bg = "mods/blwnfh/images/bg/"
    image bg int_dining_hall_people_sunset = blwnfh_bg + "int_dining_hall_people_sunset.jpg"
    image bg ext_camp_entrance_sunset = blwnfh_bg + "ext_camp_entrance_sunset.jpg"
    image bg ext_clubs_sunset = blwnfh_bg + "ext_clubs_sunset.jpg"
    image bg int_attic2_day = blwnfh_bg + "int_attic2_day.jpg"
    image bg ext_warehouse_day = blwnfh_bg + "ext_warehouse_day.jpg"
    image bg int_warehouse_day = blwnfh_bg + "int_warehouse_day.jpg"
    # Эффекты #
    
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
    
label blwnfh_main:
    "Проверка связи, главный лейбл"
    
    show kat normal pioneer far with dspr
    
    "Ща врубаем ночь"
    $ persistent.sprite_time = "night" # Освещение на спрайты #
    $ night_time()
    kat "Привет"
    
    "А теперь утро"
    $ persistent.sprite_time = "sunset" # Освещение на спрайты #
    $ sunset_time()
    "Утро"
    kat "Ахуеть, утро"
    
    show kat normal2 pioneer far with dspr
    
    "И хуякс, день!"
    $ persistent.sprite_time = "day" # Освещение на спрайты #
    $ day_time()
    "День"
    kat "Колдун ебучий"
    
    "Мы запускаем лохотрон"
    jump blwnfh_day1
    
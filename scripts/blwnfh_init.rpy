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
    
label blwnfh_main:
    "Проверка связи, главный лейбл"
    
    show kat normal pioneer far with dspr
    
    "Ща врубаем ночь"
    $ persistent.sprite_time = "night" # Освещение на спрайты #
    $ night_time()
    kat "Привет"
    
    show cg gulls with dspr
    
    "А теперь утро"
    $ persistent.sprite_time = "sunset" # Освещение на спрайты #
    $ sunset_time()
    "Утро"
    kat "Ахуеть, утро"
    
    "И хуякс, день!"
    $ persistent.sprite_time = "day" # Освещение на спрайты #
    $ day_time()
    "День"
    kat "Колдун ебучий"
    
    "Мы запускаем лохотрон"
    jump blwnfh_day1
    
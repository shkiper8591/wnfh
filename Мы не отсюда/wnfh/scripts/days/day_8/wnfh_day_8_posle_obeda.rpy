label d8_posle_obeda:

    window hide dissolve
    stop ambience fadeout 3.5
    scene bg ext_dining_hall_near_day with slide_right_blure_dissolve2
    play ambience ambience_camp_center_day fadein 3.5
    $ renpy.pause(0.5)
    window show dissolve
    
    "Аттэншн! Дальнейший клик приведёт к тому, что вы отправитесь НАХУЙ!"
    "Наебал. Но следующий точно отправит."
    "Точно[wp]"
    "Ща-ща-ща, погоди, загрузится."
    "Блять, ну хули ты кликаешь блять, сказано же нахуй, грузится!"
    "И вообще, обнови диск уже, вон как медленно всё работает."
    "Всё, загрузилось, так что следующий клик тебя отправит в главное меню игры."
label d10_un_lr_kat_and_sl:

    window hide dissolve
    stop ambience fadeout 2.0
    call screen wnfh_time_skip("Пятнадцать минут ходьбы спустя", ts_transition = santa_barbara_in_dissolve, ts_text_spd = 25, ts_timer = 5) with dissolve2
    scene bg ext_house_of_mt_day
    show un normal pioneer at left
    with dissolve2
    $ renpy.pause(0.5)
    scene bg int_house_of_mt_day
    show un normal pioneer at left
    show mt normal pioneer far at right 
    with dissolve2
    play ambience ambience_int_cabin_day fadein 2.0
    $ renpy.pause(0.5)
    window show dissolve

    "this is placeholder my fellow nigga"
d10_un_lr_doubts_about_kat:
    
    window hide dissolve
    stop ambience fadeout 2.0
    call screen wnfh_time_skip("Крутой переход", 100, santa_barbara_in_dissolve, 25, 3) with dissolve2
    scene bg int_house_of_mt_day
    show un normal pioneer at left
    show mt normal pioneer at right
    play ambience ambience_int_cabin_day fadein 2.0
    $ renpy.pause(0.3)
    window show dissolve

    "placeholder"
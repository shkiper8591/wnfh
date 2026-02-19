label d10_zavtrak_raspredelitelnya_shlyapa_hogwartsa:
    $ wnfh_set_time()

    if wnfh_Data.FlagGet("journalist") == True:

        "Плэйсхолдер"

        jump d10_zavtrak_w_kat

    else:

        jump d10_zavtrak_w_males

label d10_zavtrak_w_un:

    if wnfh_Data.FlagGet("me_stukach") == True:

        jump d10_zavtrak_w_un_stukach_route

    else:

        jump d10_zavtrak_w_un_love_route

label d10_zavtrak_w_un_love_route:

    "placeholder"

label d10_zavtrak_w_un_stukach_route:
    
    $ wnfh_set_time()
    scene bg int_dining_hall_people_day with dissolve2
    play ambience ambience_dining_hall_full fadein 2.0
    $ renpy.pause(1.0, hard=True)


    "placeholder"

label d10_zavtrak_w_dv:

    "placeholder"

label d10_zavtrak_w_males:

    "placeholder"

label d10_zavtrak_w_kat:

    "placeholder"

label d10_zavtrak_w_dv_n_mi:

    "placeholder"

label d10_zavtrak_w_mi:

    "placeholder"
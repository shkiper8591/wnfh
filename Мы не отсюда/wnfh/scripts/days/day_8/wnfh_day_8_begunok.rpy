label d8_begunok:

    window hide dissolve
    hide mid d8_breakfast_empty with dissolve
    $ renpy.pause(1.0)
    stop ambience fadeout 2.5
    
    scene bg ext_dining_hall_near_day with slide_right_blure_dissolve2
    play ambience ambience_camp_center_evening fadein 3
    play music music_list["dance_of_fireflies"] fadein 5
    $ renpy.pause(1.0)
    window show

    if wnfh_Data.getChoice_result_number("d8_choice_n2") == 1:

        jump d8_begunok_w_mi

    elif wnfh_Data.getChoice_result_number("d8_choice_n3") == 1:

        jump d8_begunok_w_un

    else:

        jump d8_begunok_canon
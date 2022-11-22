label blwnfh_test_anim:
    
    "да начнётся веселье!"
    
    play music blwnfh_music_list["santa_barbara"] noloop
    scene bg ext_bus with dissolve
    $ renpy.pause(2.0)
    scene bg ext_camp_entrance_day with santa_barbara_in_dissolve2
    $ renpy.pause(0.5)
    scene bg ext_square_day with santa_barbara_in_dissolve2
    $ renpy.pause(0.5)
    scene bg ext_houses_day with santa_barbara_in_dissolve2
    $ renpy.pause(0.5)
    scene bg ext_clubs_day with santa_barbara_in_dissolve2
    $ renpy.pause(0.5)
    scene bg ext_dining_hall_away_day with santa_barbara_in_dissolve2
    $ renpy.pause(0.5)
    scene bg ext_house_of_mt_day with santa_barbara_in_dissolve2
    $ renpy.pause(0.5)
    scene bg ext_library_day with santa_barbara_in_dissolve2
    $ renpy.pause(0.5)
    scene bg ext_boathouse_day with santa_barbara_in_dissolve2
    $ renpy.pause(0.5)
    scene bg ext_playground_day with santa_barbara_in_dissolve2
    $ renpy.pause(0.5)
    scene bg ext_stage_normal_day with santa_barbara_in_dissolve2
    $ renpy.pause(0.5)
    scene bg ext_beach_day with santa_barbara_in_dissolve2
    $ renpy.pause(0.5)
    scene bg ext_musclub_day with santa_barbara_in_dissolve2
    $ renpy.pause(0.5)
    "Конец!"
    
    
    
    
    #"hooynya nevedomoya"
    #
    #scene expression blwnfh_doubvis_vert("int_house_of_mt_sunset")
    #
    ##show wat:
    ##    subpixel True
    ##    block:
    ##        xalign 0.3 yalign 0.5
    ##    parallel:
    ##        ease 2.0 xalign 0.7
    ##        ease 2.0 xalign 0.3
    ##        repeat
    ##    parallel:
    ##        ease 2.0 yalign 0.3
    ##        ease 2.0 yalign 0.7
    ##        repeat
    ##    parallel:
    ##        linear 2.0 rotate 360.0
    ##        linear 2.0 rotate 0.0
    ##        repeat
    ##with dissolve
    ##
    ##show un smile pioneer behind wat with dspr 
    #
    #"stop"
    #
    #scene bg int_house_of_mt_sunset
    #
    #"nigga"
    
    jump blwnfh_test
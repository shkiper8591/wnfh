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
    
    jump blwnfh_test
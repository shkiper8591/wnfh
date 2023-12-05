label wnfh_test_anim:
    
    play music music_list["i_want_to_play"] fadein 2.5

    scene bg ext_beach_day with dissolve

    "Добро пожаловать в отладку анимаций! Здесь тестируются как анимации спрайтов, так и переходы между фонами."
    "Так, что мы хотели бы отладить?"

    menu:
        "Анимации спрайтов":
            jump spritesanim
        "Переходы фонов":
            jump bgtransits
        "Анимации для ЦГ":
            jump cganim

label cganim:

    
    "Пример ванильной цг"

    scene cg d9_dv_scene_1
    
    "Работает"
    "Пример модовой ЦГ"
    scene cg d8_dv_sem_scene
    "Работает?"
    "Ещё пример"
    scene expression wnfh_wakeup("cg d12_mt_volosbl")
    show unblink
    with None

    "У-ля-ля"
    "Ну всё, насмотрелся и хватит, съебал-ка в... Ну скажем..."
    "4-й день"
    jump wnfh_day_10

label spritesanim:

    "Берём Ульянку"

    show us smile pioneer with dissolve

    us "Шо ты собрался делать со мной?"
    me "Санту барбару."

    show us normal with dspr

    us "Что?"

    scene bg ext_square_day
    show us dontlike pioneer
    with santa_barbara_in_dissolve2

    me "Как тебе?"
    us "Мне не понравилось."

label bgtransits:

    "Транзит santa_barbara"
    "Да начнётся веселье!"
    
    play music wnfh_music_list["santa_barbara"] noloop
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
    
    jump wnfh_test
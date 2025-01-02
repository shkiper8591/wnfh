label d9_musclub:

    window hide dissolve
    stop music fadeout 5.0
    $ renpy.pause(1.0, hard=True)
    $ wnfh_set_time()
    stop ambience fadeout 5.0
    scene bg ext_dining_hall_away_day
    show mi normal pioneer at right
    show kat normal pioneer at left
    with santa_barbara_out_blure_dissolve5
    play ambience ambience_camp_center_day fadein 5.0
    $ renpy.pause(0.5)
    window show dissolve

    "Закончив с завтраком, мы спешно покинули столовую и, зашагав счастливой походкой, отправились в музклуб."
    "И я, словно в кино, шёл между Катей и Мику. Что со стороны, наверное, смотрелось"

    me "Хороший сегодня денёк."
    mi "Это точно! Солнышко не печёт, а приятно греет. Самое то, чтобы сидеть и играть музыку!"

    show kat sad pioneer at center with dspr

    kat "Честно, от легкого ветерка я бы сейчас не отказалась."
    mi "На этот счёт можно не беспокоиться, у меня есть вентилятор в клубе."

    show mi upset pioneer at center with dspr

    mi "Правда, он очень сильно гремит и вообще того глядишь развалится."

    show mi normal pioneer at center with dspr

    mi "Но всё же лучше чем ничего."

    show kat smile pioneer at center with dspr

    kat "Спасибо большое."

    show bg ext_lenin_square_day_wnfh with dissolve

    me "Так, "
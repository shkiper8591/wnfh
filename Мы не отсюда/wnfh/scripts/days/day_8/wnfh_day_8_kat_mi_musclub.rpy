label d8_kat_mi_musclub:
	
	stop music fadeout 5.0
	stop ambience fadeout 2.0
    scene bg ext_admin_day_wnfh with santa_barbara_in_blure_dissolve2
    play ambience ambience_camp_center_day fadein 2.0
    $ renpy.pause(0.5)
    scene bg ext_musclub_day with slide_left_blure_dissolve2
    $ renpy.pause(0.5)
    scene bg ext_musclub_verandah_day_wnfh
    show kat normal pioneer at center
    with sphere_blure_dissolve2
    play music music_list["memories_piano_outdoors"] fadein 5.0
    $ renpy.notify("МУЗЫКА МАКСИМАЛЬНО УСЛОВНАЯ, ТУТ НУЖНА БУДЕТ ДРУГАЯ, БОЛЕЕ ВЕСЁЛАЯ!")
    $ renpy.pause(0.5)
    window show dissolve

    "Подойдя к музклубу, мы услышали доносящуюся оттуда музыку."

    me "Похоже, Мику коротает время в ожидании тебя."
    kat "А она красиво играет."
    me "Ну, в конце-концов она полжизни посвятила музыке."

    show kat confused pioneer at center with dspr

    kat "Серьёзно?"
    me "По крайней мере она сама так говорит."

    show kat normal pioneer at center with dspr

    kat "Надо же[wp]"

    window hide dissolve
    stop music fadeout 5.0
    stop ambience fadeout 2.0
    scene bg int_musclub_day
    show kat smile pioneer close at left
    show mi normal pioneer at right
    with slide_right_blure_dissolve2
    play ambience ambience_music_club_day fadein 2.0
    play music music_list["so_good_to_be_careless"] fadein 5.0
    $ renpy.notify("Надо бы другую музыку для музклуба в общем и Мику в частности, а то со гуд ту би керлесс заебала. Желательно собственного производства.")
    $ renpy.pause(0.3)
    window show dissolve

    "Когда мы вошли внутрь, Мику прекратила игру на пианино и перевела свой взгляд на нас."

    mi "Ухты, даже вдвоём пришли, неожиданно-неожиданно, а я уже думала, что про меня позабыли."
    me "Дела у нас были."

    show mi grin pioneer at right with dspr

    mi "А я знаю, что у вас дела были."

    "Мы с Катей переглянулись."

    kat "Кто-то рассказал?"

    show mi smile pioneer at right with dspr

    "Мику захихикала и махнула в сторону окна."

    mi "У меня же большое окно, вас не трудно было заметить несущих какие-то коробки."

    show mi surprise pioneer at right with dspr

    mi "Кстати, что это были за коробки? А то я тут всю голову уже сломала размышляя над этим, прям покая мне не даёт."

    show kat smile pioneer close at left with dspr

    "Катя усмехнулась."

    kat "Боюсь тебя разачаровывать, но там были лагерные документы."

    show mi upset pioneer at right with dspr

    mi "Ну, в общем-то я так и примерно думала."

    show mi grin pioneer at right with dspr

    mi "Хотя в душе я надеялась, что вы несёте какие-нибудь вкусняшки для праздновства."
    mi "Правда, я прекрасно понимала, что вряд ли этот день празднуют у вас."

    "Я на секунду призадумался."
    "Мне не совсем было понятно, о каком празднике вообще может идти речь."

    show kat confused pioneer close at left with dspr

    kat "А что за праздник?"

    th "Похоже, я не один такой."

    show mi serious pioneer at right with dspr

    mi "Завтра день когда, благодаря усилиям Советского союза, закончилась оккупация американцев над Японией."
    mi "И в тот же день Япония стала членом советского блока. Для нас, японцев, это во истину великий день."
    
    show kat normal pioneer close at left with dspr

    kat "Хороший день."
    mi "Очень[wp]"

    "Я попытался переварить только что услышанную информацию, но она конфликтовала с историей которую знал я."
    "И, видимо, из-за этого конфликта, у меня знатно так разболелась голова."

    th "Вот же зараза, как невовремя-то!"

    "Боль была адская, но я постарался сдерживать себя, а также как можно скорее переключить свои мысли на что-нибудь другое."

    show kat confused pioneer close at left
    show mi upset pioneer at right
    with dspr

    kat "Семён, с тобой всё хорошо?"
    mi "Да, ты чего-то весь побледнел аж, жарко стало?"
    me "Со мной всё х-хорошо, просто мигрень настигла."

    show mi upset pioneer close at right with dspr

    "Мику подошла ко мне и потрогала мой лоб."

    show mi shocked pioneer close at right with dspr

    mi "Да ты огненный же, как тебе может быть «хорошо»?!"
    me "Странно, я ощущаю себя нормально."

    show kat upset pioneer close at left with dspr

    kat "Поиграли, блин, втроём."

    show mi serious pioneer at right with dspr

    mi "Так, ещё не всё потеряно! У меня тут полно чаёв разных лечащих, сейчас мы тебя быстро вылечим и сможем поиграть музыку."
    me "Мику, мне и вправду хорошо."

    show mi dontlike pioneer at right with dspr

    mi "И слышать ничего не хочу! Я вижу как тебе «хорошо», еле на ногах стоишь!"
    mi "Так, Катя, давай помогай."

    show kat sad pioneer at left with dspr

    kat "Может лучше медсестру позвать?"

    "А что было дальше, вы узнаете потом, потому-что на этом моменте мне стало лень писать. Либо сегодня (на момент отправки коммита) продолжу, либо потом"
    "После клика вы отправитесь в главное меню игры."
    "Я не шучу, это последнее предупреждение!"
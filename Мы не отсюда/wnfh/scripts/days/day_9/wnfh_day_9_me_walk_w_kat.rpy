label d9_walk_w_kat:

    window hide dissolve2
    play music wnfh_music_list["chilling_out"] fadein 6.5
    stop ambience fadeout 5.0
    scene bg ext_path2_sunset_wnfh
    show kat smile pioneer at center
    with sphere_blure_dissolve5
    play ambience ambience_forest_evening fadein 5.0
    $ renpy.pause(0.5)
    window show dissolve2

    "Немного пробежавшись, мы вышли в пролесок."
    "Он был мне более менее знаком, поскольку мы здесь часто бывали с Алисой."
    "Ну, как бывали, скорее использовали как этакую тропу отступления после очередной своей авантюры."
    "К сожалению, она перестала быть актуальной после последней авантюры с душевыми[wp]{nw=6.5}"

    kat "А куда ведёт эта тропа?"

    "Вопрос Кати выбил меня из моих размышлений."

    me "На другой конец лагеря."

    show kat interested pioneer at center with dspr

    kat "Это как?"
    me "Ну вот так. Просто большой крюк делаем и всё."
    me "Как раз, если идти в этом темпе, то за час мы пройдём её."
    me "Главное никуда не сворачивать."

    show kat normal pioneer at center with dspr

    kat "Похоже, ты здесь частенько гулял."

    show cg d9_me_kat_walking_wnfh with dissolve2

    me "аваывавы"

    hide cg 
    show kat sad pioneer at center
    show ext_path2_night
    with dissolve2
    $ wnfh_set_time("night")
    stop music fadeout 2.0
    stop ambience fadeout 2.0
    play ambience wnfh_ambience_list["thunder1"] fadein 2.0
    queue wnfh_ambience_list["rain_night"] fadein 1.0

    "Но, неожиданно, наш диалог прервал раскат грома."

    me "Гроза мать её."

    "В этот же миг, на лес спустилась тьма, в которой трудно было разглядеть хоть что-то."
    "Затем, почти сразу за громом, последовал сильный ветер."
    "Он сильно колыхал листву, и нам повезло оказаться в лесу, иначе мы бы в полной мере ощутили его на себе."
    "Уже чувствовались падающие капли дождя, прорывавшиеся сквозь кроны деревьев."

    me "Пора бежать домой!"

    show kat scared pioneer at center with dspr

    "Схватив Катю за руку, я повёл нас обратно."

    kat "П-Притормози, я не поспеваю за тобой."
    me "Лучше начать поспевать, иначе мы грозим тут промокнуть и простыть!"
    me "А я болеть ой как не хочу!"

    "Тем не менее, я слегка сбросил скорость."
    "Всё потому, что я прекрасно чувствовал как Катя, чуть ли не падает после каждого шага."
    "Но даже так, она всё равно еле поспевала за мной, хотя казалось бы, я далеко не спортсмен."
    "Видимо, адреналин это сильная штука."

    th "Погуляли, блин! Надеюсь, я не испачкаюсь уж через чур."


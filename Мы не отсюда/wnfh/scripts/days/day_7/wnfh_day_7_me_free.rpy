label d7_me_free:

    "Когда они ушли, я посмотрел на солнце, чтобы прикинуть время."

    th "Уже почти полдень, скоро обед. Пойду, значит, ждать обеда."

    "Медленным шагом я отправился на площадь."

    scene bg ext_lenin_square_day_wnfh with dissolve2

    "Придя к Ленину, я некоторое время рассматривал его."
    "И вдоволь наглядевшись на лидера социалистической революции, я уселся на ближайшую лавочку."

    th "Пожалуй, вздремну немного перед обедом."

    window hide dissolve
    show blink
    with None
    scene black
    $ renpy.pause(2.5)
    play sound sfx_dinner_horn_processed
    show unblink
    scene bg ext_lenin_square_day_wnfh
    with None
    window show dissolve

    "Неизвестное количество времени спустя меня разбудил горн к обеду."

    me "Ну, пора набивать желудок."

    "Встав с лавочки, я неспеша пошёл к столовой."

    jump d7_obed
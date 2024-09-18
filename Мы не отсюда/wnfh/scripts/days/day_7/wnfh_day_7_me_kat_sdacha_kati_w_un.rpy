label d7_me_kat_sdacha_kati_w_un:
        
    window hide dissolve
    scene bg ext_house_of_mt_day
    show mt dc_reading dc background
    show un normal pioneer at cleft
    show kat serious casual shirt at fleft
    with slide_left_blure_dissolve2
    window show dissolve
    "Вожатая действительно была у себя дома."
    "Вернее, у дома. Она лежала в шезлонге и читала книгу."
    "От чего мне в голову сразу закрались мысли о том, что где-то нас обманули и никаких серьёзных дел ни у кого не было."
    "Хотя кто знает, кто знает[wp]"

    me "Здраствуйте, Ольга Дмитриевна. Мы доставили ваше пополнение."
   
    $ wnfh_Data.get_achievement("post")
    $ renpy.pause(1.0, hard=True)
    show mt dc_smotrit dc background with dspr

    mt "Вы достаточно быстро."
    mt "Хотя, я так полагаю, это всё благодаря товарищу Тихоновой."

    show un shy pioneer at cleft with dspr

    un "Н-Нет, Семён тоже активное участие принимал."
    mt "Да? Ну хорошо, хорошо[wp]"

    hide mt with dspr
    $ renpy.pause(0.1)
    show mt smile pioneer at right with dspr

    "Вожатая закрыла книгу и встала с шезлонга."
    mt "Итак, где они?"

    show un surprise pioneer at cleft with dspr

    un "О-Они? Тут одна Катя[wp]"

    show mt surprise pioneer at right with dspr

    mt "Как одна?"

    show kat normal at cleft
    show un surprise pioneer at fleft 
    with dspr

    "Катя вышла вперёд."

    kat "Я одна приехала."

    show mt normal pioneer at right with dspr

    mt "Чудеса[wp] А мне говорили, что будут двое."

    show mt sad pioneer at right
    show un smile pioneer at fleft 
    with dspr

    mt "Ох, простите, ребята, что напрягла вас."
    mt "С одним пионером-то я бы могла управиться."

    show un smile2 pioneer at fleft with dspr

    me "Всё нормально, вы нас особо не напрягли."
    un "Правда-правда."
    mt "Ну хорошо, тогда можете идти, дальше я тут сама справлюсь."

    hide mt
    hide kat
    with dissolve
    show un smile pioneer at center with dspr

    "Мы отошли на небольшое расстояние от домика."        
    me "Ну-с[wp] Мне надо бежать в клубы."

    show un shy pioneer at center with dspr

    un "С-Семён."
    me "М?"

    show un smile pioneer at center with dspr

    un "Не хотел бы ты погулять после обеда?"
    me "Ох[wp]"

    window hide dissolve 
    call screen wnfh_choice(
        ["un", "Да, конечно", "Прогулка — полезное занятие", "d7_un_yes_1_lbl", {"un":1}],        
        ["un", "Пожалуй, нет", "Прогулка после обеда? Увольте!", "d7_un_no_1_lbl", {"un":-1}],
        ["neutral", "Я подумаю", "Я же не знаю, что будет после обеда", "d7_un_neutral_1_lbl"],
        ["d7_choice_n5", "Погулять ли с Леной"]
        ) with dissolve2
    #КОСЯК: если сказать Лене да и потом не дать ей подсесть за обедом, прогулка отменится даже при наличии ЛП и спокойствии Лены. Не уверен, правда, намеренно или нет, но всё же укажу.

label d7_un_yes_1_lbl:

    show un laugh pioneer at center with dspr

    un "Замечательно!"

    show un smile pioneer at center with dspr

    un "А то скучновато одной постоянно гулять по лагерю."
    me "А как же Мику? Почему её не позовёшь гулять? Соседки, как-никак."

    show un smile2 pioneer at center with dspr

    un "А ты поди вытащи её из кружка, я посмотрю на тебя."
    me "Понял."

    show un smile3 pioneer at center with dspr

    un "Ну что ж, после обеда встретимся на площади?"
    me "А сейчас ты куда?"

    show un grin pioneer at center with dspr

    un "По делам."
    me "Понятно. Ну, в таком случае до встречи."

    show un smile pioneer at center with dspr

    un "Да, пока."

    "Помахав на прощание Лене, я отправился в клубы."

    window hide dissolve
    jump d7_male_clubs

label d7_un_no_1_lbl:

    show un sad pioneer at center with dspr

    un "Оу[wp]"
    me "Прости, дела просто есть на сегодня."

    if wnfh_Data.getChoice_result_number("d7_choice_n1") == 1:
        me "Да и не очень хочется шастать по лагерю, будучи обмазанным йодом."
        un "Да[wp]"

    show un shy pioneer at center with dspr

    un "Ну ладно, тогда я пойду[wp]"
    me "Давай, пока."

    hide un with dissolve2

    "Лена удалилась в сторону домиков."
    "Немного постояв на месте, я отправился в клубы."

    window hide dissolve
    jump d7_male_clubs

label d7_un_neutral_1_lbl:

    show un normal pioneer at center with dspr

    me "До обеда ещё далеко, много чего может случиться. {w}Дел могут навалить, например."
    un "Ладно, тогда после обеда подойду к тебе."
    me "Хорошо, договорились."
    un "Угу[wp]"

    "Помахав Лене на прощание, я отправился в клубы."

    window hide dissolve
    jump d7_male_clubs
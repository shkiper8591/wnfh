label d8_evening_2:

    scene bg ext_lenin_square_sunset_wnfh with slide_up_blure_dissolve2
    play ambience ambience_camp_center_evening fadein 2.0
    play music music_list["dance_of_fireflies"] fadein 5.0

    if wnfh_Data.getChoice_result_number("d8_choice_n10") == 1:

        "Вернувшись на площадь, Катя помахала мне на прощание и ушла к домикам."

        if wnfh_Data.getChoice_result_number("d8_choice_n11") == 1:

            jump d8_evening_2_w_dv
    
        else:

            jump d8_ending

    else:

        "Вернувшись в лагерь, я вышел на площадь."
        "Дело медленно шло к ночи, поэтому пионеров тут особо не было."
        "Да и мне в целом тут делать было нечего, посему я направился к себе домой."

        jump d8_ending

label d8_evening_2_w_dv:

    "placeholder"


    












    #"d8_choice_n11" "Алиса зовёт Семёна на сцену" вариант 1 согласился, вариант 2 отказался (для себя, чтобы не забыть)
    
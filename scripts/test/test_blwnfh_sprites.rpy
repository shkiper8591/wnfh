label blwnfh_sprites_test:
    
    play music music_list["went_fishing_caught_a_girl"]
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_square_day with dissolve
    
    "Тест нового спрайта Кати"
    "Какую тушку нам нужно просмотреть?"
    
    menu:
        "Первую":
            jump kat_1
        "Вторую":
            jump kat_2
        "Третью":
            jump kat_3
        "Четвертую":
            jump kat_4

label kat_1:
    
    "Какую одёжку мы хотим отсмотреть?"
    
    menu:
        "Пионерскую":
            jump kat_1_pioneer
        "Купальник":
            jump kat_1_swim
        "Обычную одежду":
            jump kat_1_casual
        "Обычную одежду + рубашка":
            jump kat_1_shirt

label kat_1_pioneer:    
    "Первая тушка пионерская"                                                   
    
    "Normal"
    
    show kat normal pioneer with dissolve
    
    "Confused"
    
    show kat confused with dspr
    
    "Cry"
    
    show kat cry with dspr
    
    "interested"
    
    show kat interested with dspr
    
    "Sad"
    
    show kat sad with dspr
    
    "Serious"
    
    show kat serious with dspr
    
    "Smile"
    
    show kat smile with dspr

label kat_1_swim:
    
    "Первая тушка купальник"
    
    "Normal"
    
    show kat normal swim with dissolve
    
    "Confused"
    
    show kat confused with dspr
    
    "Cry"
    
    show kat cry with dspr
    
    "interested"
    
    show kat interested with dspr
    
    "Sad"
    
    show kat sad with dspr
    
    "Serious"
    
    show kat serious with dspr
    
    "Smile"
    
    show kat smile with dspr

label kat_1_casual:
    
    "Первая тушка обычная одежда"
    
    "Normal"
    
    show kat normal casual with dissolve
    
    "Confused"
    
    show kat confused with dspr
    
    "Cry"
    
    show kat cry with dspr
    
    "interested"
    
    show kat interested with dspr
    
    "Sad"
    
    show kat sad with dspr
    
    "Serious"
    
    show kat serious with dspr
    
    "Smile"
    
    show kat smile with dspr

label kat_1_casual:
    
    "Первая тушка обычная одежда + рубашка"
    
    "Normal"
    
    show kat normal casual shirt with dissolve
    
    "Confused"
    
    show kat confused with dspr
    
    "Cry"
    
    show kat cry with dspr
    
    "interested"
    
    show kat interested with dspr
    
    "Sad"
    
    show kat sad with dspr
    
    "Serious"
    
    show kat serious with dspr
    
    "Smile"
    
    show kat smile with dspr     
    
label kat_2:
    
    "Какую одёжку мы хотим отсмотреть?"
    
    menu:
        "Пионерскую":
            jump kat_2_pioneer
        "Купальник":
            jump kat_2_swim
        "Обычную одежду":
            jump kat_2_casual
        "Обычную одежду + рубашка":
            jump kat_2_shirt
            
label kat_2_pioneer:
            
    "Вторая тушка пионерская"
    
    "Guilty"
    
    show kat guilty pioneer with dissolve
    
    "Horny"
    
    show kat horny with dspr
    
    "Scared"
    
    show kat scared with dspr
    
    "Shy"
    
    show kat shy with dspr
    
    "Surprise"
    
    show kat surprise with dspr
    
label kat_2_swim:
            
    "Вторая тушка купальник"
    
    "Guilty"
    
    show kat guilty swim with dissolve
    
    "Horny"
    
    show kat horny with dspr
    
    "Scared"
    
    show kat scared with dspr
    
    "Shy"
    
    show kat shy with dspr
    
    "Surprise"
    
    show kat surprise with dspr    
    
label kat_2_casual:
            
    "Вторая тушка обычная одежда"
    
    "Guilty"
    
    show kat guilty casual with dissolve
    
    "Horny"
    
    show kat horny with dspr
    
    "Scared"
    
    show kat scared with dspr
    
    "Shy"
    
    show kat shy with dspr
    
    "Surprise"
    
    show kat surprise with dspr    
    
label kat_2_shirt:
            
    "Вторая тушка обычная одежда + рубашка"
    
    "Guilty"
    
    show kat guilty casual shirt with dissolve
    
    "Horny"
    
    show kat horny with dspr
    
    "Scared"
    
    show kat scared with dspr
    
    "Shy"
    
    show kat shy with dspr
    
    "Surprise"
    
    show kat surprise with dspr      
    
label kat_3:
    
    "Какую одёжку мы хотим отсмотреть?"
    
    menu:
        "Пионерскую":
            jump kat_3_pioneer
        "Купальник":
            jump kat_3_swim
        "Обычную одежду":
            jump kat_3_casual
        "Обычную одежду + рубашка":
            jump kat_3_shirt    
    
label kat_3_pioneer:

    "Третья тушка пионерская"
    
    "Angry"
    
    show kat angry pioneer with dissolve
    
    "Grin"
    
    show kat grin with dspr
    
    "Laugh"
    
    show kat laugh with dspr
    
    "Smile2"
    
    show kat smile2 with dspr

label kat_3_swim:

    "Третья тушка купальник"

    "Angry"
    
    show kat angry swim with dissolve
    
    "Grin"
    
    show kat grin with dspr
    
    "Laugh"
    
    show kat laugh with dspr
    
    "Smile2"
    
    show kat smile2 with dspr
    
label kat_3_casual:

    "Третья тушка обычная одежда"

    "Angry"
    
    show kat angry casual with dissolve
    
    "Grin"
    
    show kat grin with dspr
    
    "Laugh"
    
    show kat laugh with dspr
    
    "Smile2"
    
    show kat smile2 with dspr
    
label kat_3_shirt:   
    
    "Третья тушка обычная одежда + рубашка"

    "Angry"
    
    show kat angry casual shirt with dissolve
    
    "Grin"
    
    show kat grin with dspr
    
    "Laugh"
    
    show kat laugh with dspr
    
    "Smile2"
    
    show kat smile2 with dspr
    
label kat_4:

    "Какую одёжку мы хотим отсмотреть?"
    
    menu:
        "Пионерскую":
            jump kat_4_pioneer
        "Купальник":
            jump kat_4_swim
        "Обычную одежду":
            jump kat_4_casual
        "Обычную одежду + рубашка":
            jump kat_4_shirt

label kat_4_pioneer:

    "Четвертая тушка пионерская"
    
    "Happy"
    
    show kat happy pioneer with dissolve
    
    "Obida"
    
    show kat obida with dspr
    
    "Thinking"
    
    show kat thinking with dspr
    
    "Upset"
    
    show kat upset with dspr

label kat_4_swim:

    "Четвертая тушка купальник"
    
    "Happy"
    
    show kat happy swim with dissolve
    
    "Obida"
    
    show kat obida with dspr
    
    "Thinking"
    
    show kat thinking with dspr
    
    "Upset"
    
    show kat upset with dspr

label kat_4_casual:

    "Четвертая тушка обычная одежда"
    
    "Happy"
    
    show kat happy casual with dissolve
    
    "Obida"
    
    show kat obida with dspr
    
    "Thinking"
    
    show kat thinking with dspr
    
    "Upset"
    
    show kat upset with dspr

label kat_4_shirt:

    "Четвертая тушка обычная одежда + рубашка"
    
    "Happy"
    
    show kat happy casual with dissolve
    
    "Obida"
    
    show kat obida with dspr
    
    "Thinking"
    
    show kat thinking with dspr
    
    "Upset"
    
    show kat upset with dspr
    
    "Кликни, чтобы вернутся в тестовое меню"
    
    jump blwnfh_test
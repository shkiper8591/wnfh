label blwnfh_sprites_test:
    
    play music music_list["went_fishing_caught_a_girl"]
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_square_day with dissolve
    
    "Тест новых спрайтов"
    "Чей спрайт нам нужно отладить?"
    
    menu:
        "Кати":
            jump kat
        "Светы":
            jump sv

label kat:
    
    "Какую тушку нам нужно просмотреть?"
    
    menu:
        "С хвостиками":
            jump kat_normal
        "С распущенными волосами":
            jump kat_loose

label kat_normal:
    
    "Какую позу нам нужно просмотреть?"
    
    menu:
        "Первую":
            jump kat_1
        "Вторую":
            jump kat_2
        "Третью":
            jump kat_3
        "Четвертую":
            jump kat_4
    
    "Какую одёжку мы хотим отсмотреть?"

label kat_1:
    
    menu:
        "Пионерскую":
            jump kat_1_pioneer
        "Купальник":
            jump kat_1_swim
        "Обычную одежду":
            jump kat_1_casual
        "Обычную одежду + рубашка":
            jump kat_1_shirt
        "Купальник + рубашка":
            jump kat_1_swim_shirt
        "Пионерская + рубашка":
            jump kat_1_pioneer_shirt

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

label kat_1_swim_shirt:
    
    "Первая тушка купальник + рубашка"
    
    "Normal"
    
    show kat normal swim shirt with dissolve
    
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
    
label kat_1_pioneer_shirt:

    "Первая тушка пионерская + рубашка"
    
    "Normal"
    
    show kat normal swim shirt with dissolve
    
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
        "Купальник + рубашка":
            jump kat_2_swim_shirt
        "Пионерская + рубашка":
            jump kat_2_pioneer_shirt

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

label kat_2_swim_shirt:
    
    "Вторая тушка купальник + рубашка"
    
    "Guilty"
    
    show kat guilty swim shirt with dissolve
    
    "Horny"
    
    show kat horny with dspr
    
    "Scared"
    
    show kat scared with dspr
    
    "Shy"
    
    show kat shy with dspr
    
    "Surprise"
    
    show kat surprise with dspr  
    
label kat_2_pioneer_shirt:

    "Вторая тушка пионерская одежда + рубашка"
    
    "Guilty"
    
    show kat guilty pioneer shirt with dissolve
    
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
        "Купальник + рубашка":
            jump kat_3_swim_shirt
        "Пионерская + рубашка":
            jump kat_3_pioneer_shirt

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
    
label kat_3_swim_shirt:
    
    "Третья тушка купальник + рубашка"

    "Angry"
    
    show kat angry swim shirt with dissolve
    
    "Grin"
    
    show kat grin with dspr
    
    "Laugh"
    
    show kat laugh with dspr
    
    "Smile2"
    
    show kat smile2 with dspr
    
label kat_3_pioneer_shirt:

    "Третья тушка купальник + рубашка"

    "Angry"
    
    show kat angry pioneer shirt with dissolve
    
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
        "Купальник + рубашка":
            jump kat_4_swim_shirt
        "Пионерская + рубашка":
            jump kat_4_pioneer_shirt

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
    
label kat_4_swim_shirt:
    
    "Четвертая тушка купальник + рубашка"
    
    "Happy"
    
    show kat happy swim shirt with dissolve
    
    "Obida"
    
    show kat obida with dspr
    
    "Thinking"
    
    show kat thinking with dspr
    
    "Upset"
    
    show kat upset with dspr
    
label kat_4_pioneer_shirt:
    
    "Четвертая тушка пионерская + рубашка"
    
    "Happy"
    
    show kat happy pioneer shirt with dissolve
    
    "Obida"
    
    show kat obida with dspr
    
    "Thinking"
    
    show kat thinking with dspr
    
    "Upset"
    
    show kat upset with dspr
    
    "Кликни, чтобы вернутся в тестовое меню"
    
label kat_loose:
    
    "Какую позу нам нужно просмотреть?"
    
    menu:
        "Первую":
            jump kat_1_loose
        "Вторую":
            jump kat_2_loose
        "Третью":
            jump kat_3_loose
        "Четвертую":
            jump kat_4_loose
    
    "Какую одёжку мы хотим отсмотреть?"
    
    menu:
        "Пионерскую":
            jump kat_1_pioneer_loose
        "Купальник":
            jump kat_1_swim_loose
        "Обычную одежду":
            jump kat_1_casual_loose
        "Обычную одежду + рубашка":
            jump kat_1_shirt_loose
        "Купальник + рубашка":
            jump kat_1_swim_shirt_loose
        "Пионерская + рубашка":
            jump kat_1_pioneer_shirt_loose

label kat_1_pioneer_loose:    
    "Первая тушка пионерская"                                                   
    
    "Normal"
    
    show kat normal pioneer loose with dissolve
    
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

label kat_1_swim_loose:
    
    "Первая тушка купальник"
    
    "Normal"
    
    show kat normal swim loose with dissolve
    
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

label kat_1_casual_loose:
    
    "Первая тушка обычная одежда"
    
    "Normal"
    
    show kat normal casual loose with dissolve
    
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

label kat_1_casual_loose:
    
    "Первая тушка обычная одежда + рубашка"
    
    "Normal"
    
    show kat normal casual shirt loose with dissolve
    
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

label kat_1_swim_shirt_loose:
    
    "Первая тушка купальник + рубашка"
    
    "Normal"
    
    show kat normal swim shirt loose with dissolve
    
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
    
label kat_1_pioneer_shirt_loose:

    "Первая тушка пионерская + рубашка"
    
    "Normal"
    
    show kat normal swim shirt loose with dissolve
    
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
    
label kat_2_loose:
    
    "Какую одёжку мы хотим отсмотреть?"
    
    menu:
        "Пионерскую":
            jump kat_2_pioneer_loose
        "Купальник":
            jump kat_2_swim_loose
        "Обычную одежду":
            jump kat_2_casual_loose
        "Обычную одежду + рубашка":
            jump kat_2_shirt_loose
        "Купальник + рубашка":
            jump kat_2_swim_shirt_loose
        "Пионерская + рубашка":
            jump kat_2_pioneer_shirt_loose

label kat_2_pioneer_loose:
            
    "Вторая тушка пионерская"
    
    "Guilty"
    
    show kat guilty pioneer loose with dissolve
    
    "Horny"
    
    show kat horny with dspr
    
    "Scared"
    
    show kat scared with dspr
    
    "Shy"
    
    show kat shy with dspr
    
    "Surprise"
    
    show kat surprise with dspr
    
label kat_2_swim_loose:
    
    "Вторая тушка купальник"
    
    "Guilty"
    
    show kat guilty swim loose with dissolve
    
    "Horny"
    
    show kat horny with dspr
    
    "Scared"
    
    show kat scared with dspr
    
    "Shy"
    
    show kat shy with dspr
    
    "Surprise"
    
    show kat surprise with dspr    
    
label kat_2_casual_loose:
            
    "Вторая тушка обычная одежда"
    
    "Guilty"
    
    show kat guilty casual loose with dissolve
    
    "Horny"
    
    show kat horny with dspr
    
    "Scared"
    
    show kat scared with dspr
    
    "Shy"
    
    show kat shy with dspr
    
    "Surprise"
    
    show kat surprise with dspr    
    
label kat_2_shirt_loose:
            
    "Вторая тушка обычная одежда + рубашка"
    
    "Guilty"
    
    show kat guilty casual shirt loose with dissolve
    
    "Horny"
    
    show kat horny with dspr
    
    "Scared"
    
    show kat scared with dspr
    
    "Shy"
    
    show kat shy with dspr
    
    "Surprise"
    
    show kat surprise with dspr      

label kat_2_swim_shirt_loose:
    
    "Вторая тушка купальник + рубашка"
    
    "Guilty"
    
    show kat guilty swim shirt with dissolve
    
    "Horny"
    
    show kat horny with dspr
    
    "Scared"
    
    show kat scared with dspr
    
    "Shy"
    
    show kat shy with dspr
    
    "Surprise"
    
    show kat surprise with dspr  
    
label kat_2_pioneer_shirt_loose:

    "Вторая тушка пионерская одежда + рубашка"
    
    "Guilty"
    
    show kat guilty pioneer shirt loose with dissolve
    
    "Horny"
    
    show kat horny with dspr
    
    "Scared"
    
    show kat scared with dspr
    
    "Shy"
    
    show kat shy with dspr
    
    "Surprise"
    
    show kat surprise with dspr  
    
label kat_3_loose:
    
    "Какую одёжку мы хотим отсмотреть?"
    
    menu:
        "Пионерскую":
            jump kat_3_pioneer_loose
        "Купальник":
            jump kat_3_swim_loose
        "Обычную одежду":
            jump kat_3_casual_loose
        "Обычную одежду + рубашка":
            jump kat_3_shirt_loose    
        "Купальник + рубашка":
            jump kat_3_swim_shirt_loose
        "Пионерская + рубашка":
            jump kat_3_pioneer_shirt_loose

label kat_3_pioneer_loose:

    "Третья тушка пионерская"
    
    "Angry"
    
    show kat angry pioneer loose with dissolve
    
    "Grin"
    
    show kat grin with dspr
    
    "Laugh"
    
    show kat laugh with dspr
    
    "Smile2"
    
    show kat smile2 with dspr

label kat_3_swim_loose:

    "Третья тушка купальник"

    "Angry"
    
    show kat angry swim loose with dissolve
    
    "Grin"
    
    show kat grin with dspr
    
    "Laugh"
    
    show kat laugh with dspr
    
    "Smile2"
    
    show kat smile2 with dspr
    
label kat_3_casual_loose:

    "Третья тушка обычная одежда"

    "Angry"
    
    show kat angry casual loose with dissolve
    
    "Grin"
    
    show kat grin with dspr
    
    "Laugh"
    
    show kat laugh with dspr
    
    "Smile2"
    
    show kat smile2 with dspr
    
label kat_3_shirt_loose:   
    
    "Третья тушка обычная одежда + рубашка"

    "Angry"
    
    show kat angry casual shirt loose with dissolve
    
    "Grin"
    
    show kat grin with dspr
    
    "Laugh"
    
    show kat laugh with dspr
    
    "Smile2"
    
    show kat smile2 with dspr
    
label kat_3_swim_shirt_loose:
    
    "Третья тушка купальник + рубашка"

    "Angry"
    
    show kat angry swim shirt loose with dissolve
    
    "Grin"
    
    show kat grin with dspr
    
    "Laugh"
    
    show kat laugh with dspr
    
    "Smile2"
    
    show kat smile2 with dspr
    
label kat_3_pioneer_shirt_loose:

    "Третья тушка купальник + рубашка"

    "Angry"
    
    show kat angry pioneer shirt loose with dissolve
    
    "Grin"
    
    show kat grin with dspr
    
    "Laugh"
    
    show kat laugh with dspr
    
    "Smile2"
    
    show kat smile2 with dspr
    
label kat_4_loose:

    "Какую одёжку мы хотим отсмотреть?"
    
    menu:
        "Пионерскую":
            jump kat_4_pioneer_loose
        "Купальник":
            jump kat_4_swim_loose
        "Обычную одежду":
            jump kat_4_casual_loose
        "Обычную одежду + рубашка":
            jump kat_4_shirt_loose
        "Купальник + рубашка":
            jump kat_4_swim_shirt_loose
        "Пионерская + рубашка":
            jump kat_4_pioneer_shirt_loose

label kat_4_pioneer_loose:

    "Четвертая тушка пионерская"
    
    "Happy"
    
    show kat happy pioneer loose with dissolve
    
    "Obida"
    
    show kat obida with dspr
    
    "Thinking"
    
    show kat thinking with dspr
    
    "Upset"
    
    show kat upset with dspr

label kat_4_swim_loose:

    "Четвертая тушка купальник"
    
    "Happy"
    
    show kat happy swim loose with dissolve
    
    "Obida"
    
    show kat obida with dspr
    
    "Thinking"
    
    show kat thinking with dspr
    
    "Upset"
    
    show kat upset with dspr

label kat_4_casual_loose:

    "Четвертая тушка обычная одежда"
    
    "Happy"
    
    show kat happy casual loose with dissolve
    
    "Obida"
    
    show kat obida with dspr
    
    "Thinking"
    
    show kat thinking with dspr
    
    "Upset"
    
    show kat upset with dspr

label kat_4_shirt_loose:

    "Четвертая тушка обычная одежда + рубашка"
    
    "Happy"
    
    show kat happy casual shirt loose with dissolve
    
    "Obida"
    
    show kat obida with dspr
    
    "Thinking"
    
    show kat thinking with dspr
    
    "Upset"
    
    show kat upset with dspr
    
    "Кликни, чтобы вернутся в тестовое меню"
    
label kat_4_swim_shirt_loose:
    
    "Четвертая тушка купальник + рубашка"
    
    "Happy"
    
    show kat happy swim shirt loose with dissolve
    
    "Obida"
    
    show kat obida with dspr
    
    "Thinking"
    
    show kat thinking with dspr
    
    "Upset"
    
    show kat upset with dspr
    
label kat_4_pioneer_shirt_loose:
    
    "Четвертая тушка пионерская + рубашка"
    
    "Happy"
    
    show kat happy pioneer shirt loose with dissolve
    
    "Obida"
    
    show kat obida with dspr
    
    "Thinking"
    
    show kat thinking with dspr
    
    "Upset"
    
    show kat upset with dspr
    
label sv:
    
    "Света в очках без планшета."
    
    show sv angry pioneer glasses with dissolve
    
    "Света без очков с планшетом."
    
    show sv angry pioneer tablet with dspr
    
    "Света с очками и планшетом."
    
    show sv angry pioneer glasses tablet with dissolve
    
    "Кликни чтобы вернутся в меню отладки"
    
    jump blwnfh_test
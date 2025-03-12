label wnfh_sprites_test:
    
    play music music_list["went_fishing_caught_a_girl"]
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_square_day with dissolve
    
    "Тест новых спрайтов"
    "Чей спрайт нам нужно отладить?"
    
    menu:
        "дабл спрайты":
            jump double
        "Кати":
            jump kat
        "Светы":
            jump sv
        "Деда":
            jump sd
        "Ульяны":
            jump us
        "Лены":
            jump un
label double:

    "Испытание бобёр номер один."

    show dv normal pioneer at left
    show dv normal pioneer at right as dv2

    "испытание началось"

label us:
    "Какую тушку нам нужно просмотреть?"
    
    menu:
        "С пучком на голове":
            jump us_normal
        "С бантиком":
            jump us_bant

label us_normal:

    "Какую позу нам нужно просмотреть?"
    
    menu:
        "Первую":
            jump us_1
        "Вторую":
            jump us_2
        "Третью":
            jump us_3

label us_bant:
    "Какую позу нам нужно просмотреть?"
    
    menu:
        "Первую":
            jump us_1_bant
        "Вторую":
            jump us_2_bant
        "Третью":
             jump us_3_bant

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
    
    "Joy"
    
    show kat joy with dspr
    
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
    
    "Joy"
    
    show kat joy with dspr
    
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
    
    "Joy"
    
    show kat joy with dspr
    
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
    
    "Joy"
    
    show kat joy with dspr
    
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
    
    "Joy"
    
    show kat joy with dspr
    
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
    
    "Joy"
    
    show kat joy with dspr
    
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
    
    "Rage"
    
    show kat rage with dspr
    
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
    
    "Rage"
    
    show kat rage with dspr
    
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
    
    "Rage"
    
    show kat rage with dspr
    
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
    
    "Rage"
    
    show kat rage with dspr
    
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
    
    "Rage"
    
    show kat rage with dspr
    
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
    
    "Rage"
    
    show kat rage with dspr
    
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
    
    "Joy"
    
    show kat joy with dspr
    
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
    
    "Joy"
    
    show kat joy with dspr
    
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
    
    "Joy"
    
    show kat joy with dspr
    
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
    
    "Joy"
    
    show kat joy with dspr
    
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
    
    "Joy"
    
    show kat joy with dspr
    
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
    
    "Joy"
    
    show kat joy
    
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
    
    "Rage"
    
    show kat rage with dspr
    
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
    
    "Rage"
    
    show kat rage with dspr
    
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
    
    "Rage"
    
    show kat rage with dspr
    
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
    
    "Rage"
    
    show kat rage with dspr
    
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
    
    "Rage"
    
    show kat rage with dspr
    
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
    
    "Rage"
    
    show kat rage with dspr
    
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
    
    "Новая эмоция Светы"
    
    show sv worried pioneer with dissolve
    
    "Света в очках без планшета."
    
    show sv angry pioneer glasses with dissolve
    
    "Света без очков с планшетом."
    
    show sv angry pioneer tablet with dspr
    
    "Света с очками и планшетом."
    
    show sv angry pioneer glasses tablet with dissolve
    
    "Кликни чтобы вернутся в меню отладки"
    
    jump wnfh_test
    
label sd:

    "Мы хотим отсмотреть спрайты с сигаретой или без?"
    
    menu:
        "Без сигареты":
            jump sd_normal
        "С сигаретой":
            jump sd_cigarete
            
label sd_normal:
    
    "С очками или без?"
    
    menu:
        "С очками":
            jump sd_normal_glasses
        "Без":
            jump sd_normal_1

label sd_normal_1:
    
    "Нормальная/спокойная эмоция"
    
    show sd forma normal at center with dissolve
    
    "Злая эмоция"
    
    show sd forma angry with dspr
    
    "Ухмылка"
    
    show sd forma grin with dspr
    
    "Сурьёзная эмоция"
    
    show sd forma serious with dspr
    
    "Улыбка"
    
    show sd forma smile with dspr
    
    "Смех"
    
    show sd forma laugh with dspr
    
label sd_normal_glasses:    
    
    "Нормальная/спокойная эмоция"
    
    show sd forma normal glasses at center with dissolve
    
    "Злая эмоция"
    
    show sd forma angry with dspr
    
    "Ухмылка"
    
    show sd forma grin with dspr
    
    "Сурьёзная эмоция"
    
    show sd forma serious with dspr
    
    "Улыбка"
    
    show sd forma smile with dspr
    
    "Смех"
    
    show sd forma laugh with dspr
    
label sd_cigarete:

    "С очками или без?"
    
    menu:
        "С очками":
            jump sd_cigarete_glasses
        "Без":
            jump sd_cigarete_1
            
label sd_cigarete_1:
    
    "Нормальная/спокойная эмоция"
    
    show sd forma cigarete normal at center with dissolve
    
    "Злая эмоция"
    
    show sd forma cigarete angry with dspr
    
    "Ухмылка"
    
    show sd forma cigarete grin with dspr
    
    "Сурьёзная эмоция"
    
    show sd forma cigarete serious with dspr
    
    "Улыбка"
    
    show sd forma cigarete smile with dspr
    
    "Смех"
    
    show sd forma cigarete laugh with dspr
    
label sd_cigarete_glasses:

    "Нормальная/спокойная эмоция"
    
    show sd forma cigarete normal glasses at center with dissolve
    
    "Злая эмоция"
    
    show sd forma cigarete angry with dspr
    
    "Ухмылка"
    
    show sd forma cigarete grin with dspr
    
    "Сурьёзная эмоция"
    
    show sd forma cigarete serious with dspr
    
    "Улыбка"
    
    show sd forma cigarete smile with dspr
    
    "Смех"
    
    show sd forma cigarete laugh with dspr
    
label us_1:

    "Какую одёжку мы хотим отсмотреть?"
    
    menu:
        "Пионерскую":
            jump us_1_pioneer
        "Платье":
            jump us_1_dress
        "Купальник":
            jump us_1_swim
        "Спортивная":
            jump us_1_sport
        "Спортивная 2":
            jump us_1_sport2
        "Спортивная 2 с повязками":
            jump us_1_sport2_bandage

label us_1_pioneer:
    
    "Пионерская"
    
    "Нормальная"
    
    show us normal pioneer at center with dissolve
    
    "Нормальная с улыбкой"
    
    show us normalsmile with dspr
    
    "Ухмылка"
    
    show us grin with dspr
    
    "Смех"
    
    show us laugh with dspr
    
    "Смех2"
    
    show us laugh2 with dspr
    
    "Грусть"
    
    show us sad with dspr
    
    "Улыбка"
    
    show us smile with dspr
    
label us_1_dress:

    "Платье"
    
    "Нормальная"
    
    show us normal dress at center with dissolve
    
    "Нормальная с улыбкой"
    
    show us normalsmile with dspr
    
    "Ухмылка"
    
    show us grin with dspr
    
    "Смех"
    
    show us laugh with dspr
    
    "Смех2"
    
    show us laugh2 with dspr
    
    "Грусть"
    
    show us sad with dspr
    
    "Улыбка"
    
    show us smile with dspr
    
label us_1_swim:

    "Купальник"
    
    "Нормальная"
    
    show us normal swim at center with dissolve
    
    "Нормальная с улыбкой"
    
    show us normalsmile with dspr
    
    "Ухмылка"
    
    show us grin with dspr
    
    "Смех"
    
    show us laugh with dspr
    
    "Смех2"
    
    show us laugh2 with dspr
    
    "Грусть"
    
    show us sad with dspr
    
    "Улыбка"
    
    show us smile with dspr
    
label us_1_sport:

    "Спортивная"
    
    "Нормальная"
    
    show us normal sport at center with dissolve
    
    "Нормальная с улыбкой"
    
    show us normalsmile with dspr
    
    "Ухмылка"
    
    show us grin with dspr
    
    "Смех"
    
    show us laugh with dspr
    
    "Смех2"
    
    show us laugh2 with dspr
    
    "Грусть"
    
    show us sad with dspr
    
    "Улыбка"
    
    show us smile with dspr
       
label us_1_sport2:

    "Спортивная2"
    
    "Нормальная"
    
    show us normal sport2 at center with dissolve
    
    "Нормальная с улыбкой"
    
    show us normalsmile with dspr
    
    "Ухмылка"
    
    show us grin with dspr
    
    "Смех"
    
    show us laugh with dspr
    
    "Смех2"
    
    show us laugh2 with dspr
    
    "Грусть"
    
    show us sad with dspr
    
    "Улыбка"
    
    show us smile with dspr
    
label us_1_sport2_bandage:

    "Спортивная2 с повязками"
    
    "Нормальная"
    
    show us normal sport2 bandage at center with dissolve
    
    "Нормальная с улыбкой"
    
    show us normalsmile with dspr
    
    "Ухмылка"
    
    show us grin with dspr
    
    "Смех"
    
    show us laugh with dspr
    
    "Смех2"
    
    show us laugh2 with dspr
    
    "Грусть"
    
    show us sad with dspr
    
    "Улыбка"
    
    show us smile with dspr
    
label us_2:
    
    menu:
        "Пионерскую":
            jump us_2_pioneer
        "Платье":
            jump us_2_dress
        "Купальник":
            jump us_2_swim
        "Спортивная":
            jump us_2_sport
        "Спортивная 2":
            jump us_2_sport2
        "Спортивная 2 с повязками":
            jump us_2_sport2_bandage

label us_2_pioneer:

    "Пионерская"
    
    "Злая"
    
    show us angry pioneer at center with dissolve
    
    "Непонимание?"
    
    show us calml with dspr
    
    "Недовольство"
    
    show us dontlike with dspr
    
    "Страх"
    
    show us fear with dspr
    
    "Поникшая"
    
    show us upset with dspr

label us_2_dress:

    "Платье"
    
    "Злая"
    
    show us angry dress at center with dissolve
    
    "Непонимание?"
    
    show us calml with dspr
    
    "Недовольство"
    
    show us dontlike with dspr
    
    "Страх"
    
    show us fear with dspr
    
    "Поникшая"
    
    show us upset with dspr
    
label us_2_swim:

    "Купальник"
    
    "Злая"
    
    show us angry swim at center with dissolve
    
    "Непонимание?"
    
    show us calml with dspr
    
    "Недовольство"
    
    show us dontlike with dspr
    
    "Страх"
    
    show us fear with dspr
    
    "Поникшая"
    
    show us upset with dspr
    
label us_2_sport:

    "Спортивная"
    
    "Злая"
    
    show us angry sport at center with dissolve
    
    "Непонимание?"
    
    show us calml with dspr
    
    "Недовольство"
    
    show us dontlike with dspr
    
    "Страх"
    
    show us fear with dspr
    
    "Поникшая"
    
    show us upset with dspr
    
label us_2_sport2:

    "Спортивная2"
    
    "Злая"
    
    show us angry sport2 at center with dissolve
    
    "Непонимание?"
    
    show us calml with dspr
    
    "Недовольство"
    
    show us dontlike with dspr
    
    "Страх"
    
    show us fear with dspr
    
    "Поникшая"
    
    show us upset with dspr
    
label us_2_sport2_bandage:

    "Спортивная2 с повязками"
    
    "Злая"
    
    show us angry sport2 bandage at center with dissolve
    
    "Непонимание?"
    
    show us calml with dspr
    
    "Недовольство"
    
    show us dontlike with dspr
    
    "Страх"
    
    show us fear with dspr
    
    "Поникшая"
    
    show us upset with dspr
       
label us_3: 

    menu:
        "Пионерскую":
            jump us_3_pioneer
        "Платье":
            jump us_3_dress
        "Купальник":
            jump us_3_swim
        "Спортивная":
            jump us_3_sport
        "Спортивная 2":
            jump us_3_sport2
        "Спортивная 2 с повязками":
            jump us_3_sport2_bandage

label us_3_pioneer:

    "Пионерская"
    
    "Плачь"
    
    show us cry pioneer at center with dissolve
    
    "Плачь2"
    
    show us cry2 with dspr
    
    "Смущение"
    
    show us shy with dspr
    
    "Смущение2"
    
    show us shy2 with dspr
    
    "Удивление1"
    
    show us surp1 with dspr
    
    "Удивление2"
    
    show us surp2 with dspr
    
    "Удивление3"
    
    show us surp3 with dspr
    
label us_3_dress:    

    "Платье"
    
    "Плачь"
    
    show us cry dress at center with dissolve
    
    "Плачь2"
    
    show us cry2 with dspr
    
    "Смущение"
    
    show us shy with dspr
    
    "Смущение2"
    
    show us shy2 with dspr
    
    "Удивление1"
    
    show us surp1 with dspr
    
    "Удивление2"
    
    show us surp2 with dspr
    
    "Удивление3"
    
    show us surp3 with dspr
        
label us_3_swim:    

    "Купальник"
    
    "Плачь"
    
    show us cry swim at center with dissolve
    
    "Плачь2"
    
    show us cry2 with dspr
    
    "Смущение"
    
    show us shy with dspr
    
    "Смущение2"
    
    show us shy2 with dspr
    
    "Удивление1"
    
    show us surp1 with dspr
    
    "Удивление2"
    
    show us surp2 with dspr
    
    "Удивление3"
    
    show us surp3 with dspr
        
label us_3_sport:    

    "Спортивная"
    
    "Плачь"
    
    show us cry sport at center with dissolve
    
    "Плачь2"
    
    show us cry2 with dspr
    
    "Смущение"
    
    show us shy with dspr
    
    "Смущение2"
    
    show us shy2 with dspr
    
    "Удивление1"
    
    show us surp1 with dspr
    
    "Удивление2"
    
    show us surp2 with dspr
    
    "Удивление3"
    
    show us surp3 with dspr
        
label us_3_sport2:    

    "Спортивная2"
     
    "Плачь"
    
    show us cry sport2 at center with dissolve
    
    "Плачь2"
    
    show us cry2 with dspr
    
    "Смущение"
    
    show us shy with dspr
    
    "Смущение2"
    
    show us shy2 with dspr
    
    "Удивление1"
    
    show us surp1 with dspr
    
    "Удивление2"
    
    show us surp2 with dspr
    
    "Удивление3"
    
    show us surp3 with dspr
       
label us_3_sport2_bandage:

    "Спортивная2 с повязками"
    
    "Плачь"
    
    show us cry sport2 bandage at center with dissolve
    
    "Плачь2"
    
    show us cry2 with dspr
    
    "Смущение"
    
    show us shy with dspr
    
    "Смущение2"
    
    show us shy2 with dspr
    
    "Удивление1"
    
    show us surp1 with dspr
    
    "Удивление2"
    
    show us surp2 with dspr
    
    "Удивление3"
    
    show us surp3 with dspr

label us_1_bant:

    "Какую одёжку мы хотим отсмотреть?"
    
    menu:
        "Пионерскую":
            jump us_1_pioneer_bant
        "Платье":
            jump us_1_dress_bant
        "Купальник":
            jump us_1_swim_bant
        "Спортивная":
            jump us_1_sport_bant
        "Спортивная 2":
            jump us_1_sport2_bant
        "Спортивная 2 с повязками":
            jump us_1_sport2_bandage_bant

label us_1_pioneer_bant:
    
    "Пионерская"
    
    "Нормальная"
    
    show us normal pioneer bant at center with dissolve
    
    "Нормальная с улыбкой"
    
    show us normalsmile with dspr
    
    "Ухмылка"
    
    show us grin with dspr
    
    "Смех"
    
    show us laugh with dspr
    
    "Смех2"
    
    show us laugh2 with dspr
    
    "Грусть"
    
    show us sad with dspr
    
    "Улыбка"
    
    show us smile with dspr
    
label us_1_dress_bant:

    "Платье"
    
    "Нормальная"
    
    show us normal dress bant at center with dissolve
    
    "Нормальная с улыбкой"
    
    show us normalsmile with dspr
    
    "Ухмылка"
    
    show us grin with dspr
    
    "Смех"
    
    show us laugh with dspr
    
    "Смех2"
    
    show us laugh2 with dspr
    
    "Грусть"
    
    show us sad with dspr
    
    "Улыбка"
    
    show us smile with dspr
    
label us_1_swim_bant:

    "Купальник"
    
    "Нормальная"
    
    show us normal swim bant at center with dissolve
    
    "Нормальная с улыбкой"
    
    show us normalsmile with dspr
    
    "Ухмылка"
    
    show us grin with dspr
    
    "Смех"
    
    show us laugh with dspr
    
    "Смех2"
    
    show us laugh2 with dspr
    
    "Грусть"
    
    show us sad with dspr
    
    "Улыбка"
    
    show us smile with dspr
    
label us_1_sport_bant:

    "Спортивная"
    
    "Нормальная"
    
    show us normal sport bant at center with dissolve
    
    "Нормальная с улыбкой"
    
    show us normalsmile with dspr
    
    "Ухмылка"
    
    show us grin with dspr
    
    "Смех"
    
    show us laugh with dspr
    
    "Смех2"
    
    show us laugh2 with dspr
    
    "Грусть"
    
    show us sad with dspr
    
    "Улыбка"
    
    show us smile with dspr
       
label us_1_sport2_bant:

    "Спортивная2"
    
    "Нормальная"
    
    show us normal sport2 bant at center with dissolve
    
    "Нормальная с улыбкой"
    
    show us normalsmile with dspr
    
    "Ухмылка"
    
    show us grin with dspr
    
    "Смех"
    
    show us laugh with dspr
    
    "Смех2"
    
    show us laugh2 with dspr
    
    "Грусть"
    
    show us sad with dspr
    
    "Улыбка"
    
    show us smile with dspr
    
label us_1_sport2_bandage_bant:

    "Спортивная2 с повязками"
    
    "Нормальная"
    
    show us normal sport2 bandage bant at center with dissolve
    
    "Нормальная с улыбкой"
    
    show us normalsmile with dspr
    
    "Ухмылка"
    
    show us grin with dspr
    
    "Смех"
    
    show us laugh with dspr
    
    "Смех2"
    
    show us laugh2 with dspr
    
    "Грусть"
    
    show us sad with dspr
    
    "Улыбка"
    
    show us smile with dspr
    
label us_2_bant:
    
    menu:
        "Пионерскую":
            jump us_2_pioneer_bant
        "Платье":
            jump us_2_dress_bant
        "Купальник":
            jump us_2_swim_bant
        "Спортивная":
            jump us_2_sport_bant
        "Спортивная 2":
            jump us_2_sport2_bant
        "Спортивная 2 с повязками":
            jump us_2_sport2_bandage_bant

label us_2_pioneer_bant:

    "Пионерская"
    
    "Злая"
    
    show us angry pioneer bant at center with dissolve
    
    "Непонимание?"
    
    show us calml with dspr
    
    "Недовольство"
    
    show us dontlike with dspr
    
    "Страх"
    
    show us fear with dspr
    
    "Поникшая"
    
    show us upset with dspr

label us_2_dress_bant:

    "Платье"
    
    "Злая"
    
    show us angry dress bant at center with dissolve
    
    "Непонимание?"
    
    show us calml with dspr
    
    "Недовольство"
    
    show us dontlike with dspr
    
    "Страх"
    
    show us fear with dspr
    
    "Поникшая"
    
    show us upset with dspr
    
label us_2_swim_bant:

    "Купальник"
    
    "Злая"
    
    show us angry swim bant at center with dissolve
    
    "Непонимание?"
    
    show us calml with dspr
    
    "Недовольство"
    
    show us dontlike with dspr
    
    "Страх"
    
    show us fear with dspr
    
    "Поникшая"
    
    show us upset with dspr
    
label us_2_sport_bant:

    "Спортивная"
    
    "Злая"
    
    show us angry sport bant at center with dissolve
    
    "Непонимание?"
    
    show us calml with dspr
    
    "Недовольство"
    
    show us dontlike with dspr
    
    "Страх"
    
    show us fear with dspr
    
    "Поникшая"
    
    show us upset with dspr
    
label us_2_sport2_bant:

    "Спортивная2"
    
    "Злая"
    
    show us angry sport2 bant at center with dissolve
    
    "Непонимание?"
    
    show us calml with dspr
    
    "Недовольство"
    
    show us dontlike with dspr
    
    "Страх"
    
    show us fear with dspr
    
    "Поникшая"
    
    show us upset with dspr
    
label us_2_sport2_bandage:

    "Спортивная2 с повязками"
    
    "Злая"
    
    show us angry sport2 bant bandage at center with dissolve
    
    "Непонимание?"
    
    show us calml with dspr
    
    "Недовольство"
    
    show us dontlike with dspr
    
    "Страх"
    
    show us fear with dspr
    
    "Поникшая"
    
    show us upset with dspr
       
label us_3_bant: 

    menu:
        "Пионерскую":
            jump us_3_pioneer_bant
        "Платье":
            jump us_3_dress_bant
        "Купальник":
            jump us_3_swim_bant
        "Спортивная":
            jump us_3_sport_bant
        "Спортивная 2":
            jump us_3_sport2_bant
        "Спортивная 2 с повязками":
            jump us_3_sport2_bandage_bant

label us_3_pioneer_bant:

    "Пионерская"
    
    "Плачь"
    
    show us cry pioneer bant at center with dissolve
    
    "Плачь2"
    
    show us cry2 with dspr
    
    "Смущение"
    
    show us shy with dspr
    
    "Смущение2"
    
    show us shy2 with dspr
    
    "Удивление1"
    
    show us surp1 with dspr
    
    "Удивление2"
    
    show us surp2 with dspr
    
    "Удивление3"
    
    show us surp3 with dspr
    
label us_3_dress_bant:    

    "Платье"
    
    "Плачь"
    
    show us cry dress bant at center with dissolve
    
    "Плачь2"
    
    show us cry2 with dspr
    
    "Смущение"
    
    show us shy with dspr
    
    "Смущение2"
    
    show us shy2 with dspr
    
    "Удивление1"
    
    show us surp1 with dspr
    
    "Удивление2"
    
    show us surp2 with dspr
    
    "Удивление3"
    
    show us surp3 with dspr
        
label us_3_swim_bant:    

    "Купальник"
    
    "Плачь"
    
    show us cry swim bant at center with dissolve
    
    "Плачь2"
    
    show us cry2 with dspr
    
    "Смущение"
    
    show us shy with dspr
    
    "Смущение2"
    
    show us shy2 with dspr
    
    "Удивление1"
    
    show us surp1 with dspr
    
    "Удивление2"
    
    show us surp2 with dspr
    
    "Удивление3"
    
    show us surp3 with dspr
        
label us_3_sport_bant:    

    "Спортивная"
    
    "Плачь"
    
    show us cry sport bant at center with dissolve
    
    "Плачь2"
    
    show us cry2 with dspr
    
    "Смущение"
    
    show us shy with dspr
    
    "Смущение2"
    
    show us shy2 with dspr
    
    "Удивление1"
    
    show us surp1 with dspr
    
    "Удивление2"
    
    show us surp2 with dspr
    
    "Удивление3"
    
    show us surp3 with dspr
        
label us_3_sport2_bant:    

    "Спортивная2"
     
    "Плачь"
    
    show us cry sport2 bant at center with dissolve
    
    "Плачь2"
    
    show us cry2 with dspr
    
    "Смущение"
    
    show us shy with dspr
    
    "Смущение2"
    
    show us shy2 with dspr
    
    "Удивление1"
    
    show us surp1 with dspr
    
    "Удивление2"
    
    show us surp2 with dspr
    
    "Удивление3"
    
    show us surp3 with dspr
       
label us_3_sport2_bandage_bant:

    "Спортивная2 с повязками"
    
    "Плачь"
    
    show us cry sport2 bant bandage at center with dissolve
    
    "Плачь2"
    
    show us cry2 with dspr
    
    "Смущение"
    
    show us shy with dspr
    
    "Смущение2"
    
    show us shy2 with dspr
    
    "Удивление1"
    
    show us surp1 with dspr
    
    "Удивление2"
    
    show us surp2 with dspr
    
    "Удивление3"
    
    show us surp3 with dspr
    
label un:
    "Какую дистанцию мы хотим отсмотреть?"
    
    menu:
        "Normal":
            jump un_normal
        "Far":
            jump un_far
        "Close":
            jump un_close
    
    "Какую позу мы хотим отсмотреть?"

label un_normal:

    menu:
        "Первую":
            jump un_1_normal
        "Вторую":
            jump un_2_normal
        "Третью":
            jump un_3_normal

label un_1_normal:

    "Поза 1"
    
    "Нормальная эмоция"
    
    show un apron normal at center with dissolve
    
    "Злая"
    
    show un angry with dspr
    
    "Злая улыбка"
    
    show un evil_smile with dspr
    
    "Смущение"
    
    show un shy with dspr

    "Улыбка"
    
    show un smile with dspr
    
    "Улыбка_2"
    
    show un smile2 with dspr
    
label un_2_normal:

    "Поза 2"
    
    "Плачь"
    
    show un apron cry at center with dissolve
    
    "Плачь с улыбкой"
    
    show un cry_smile with dspr 
    
    "Грусть"

    show un sad with dspr
    
    "Испуг"
    
    show un scared with dspr
    
    "Шок"
    
    show un shocked with dspr
    
    "Удивление"
    
    show un surprise with dspr
    
    "Злая2"
    
    show un angry2 with dspr

label un_3_normal:

    "Поза 3"
    
    "Ухмылка"

    show un apron grin at center with dissolve
    
    "Смех"

    show un laugh with dspr
    
    "Ярость"
    
    show un rage with dspr
    
    "Серьёзная"
    
    show un serious with dspr
    
    "Улыбка_3"
    
    show un smile3 with dspr
    
label un_far:

    menu:
        "Первую":
            jump un_1_far
        "Вторую":
            jump un_2_far
        "Третью":
            jump un_3_far

label un_1_far:

    "Поза 1"
    
    "Нормальная эмоция"
    
    show un apron normal far at center with dissolve
    
    "Злая"
    
    show un angry with dspr
    
    "Злая улыбка"
    
    show un evil_smile with dspr
    
    "Смущение"
    
    show un shy with dspr

    "Улыбка"
    
    show un smile with dspr
    
    "Улыбка_2"
    
    show un smile2 with dspr
    
label un_2_far:

    "Поза 2"
    
    "Плачь"
    
    show un apron cry far at center with dissolve
    
    "Плачь с улыбкой"
    
    show un cry_smile with dspr 
    
    "Грусть"

    show un sad with dspr
    
    "Испуг"
    
    show un scared with dspr
    
    "Шок"
    
    show un shocked with dspr
    
    "Удивление"
    
    show un surprise with dspr
    
    "Злая2"
    
    show un angry2 with dspr

label un_3_far:

    "Поза 3"
    
    "Ухмылка"

    show un apron grin far at center with dissolve
    
    "Смех"

    show un laugh with dspr
    
    "Ярость"
    
    show un rage with dspr
    
    "Серьёзная"
    
    show un serious with dspr
    
    "Улыбка_3"
    
    show un smile3 with dspr
    
label un_close:

    menu:
        "Первую":
            jump un_1_close
        "Вторую":
            jump un_2_close
        "Третью":
            jump un_3_close

label un_1_close:

    "Поза 1"
    
    "Нормальная эмоция"
    
    show un apron normal close at center with dissolve
    
    "Злая"
    
    show un angry with dspr
    
    "Злая улыбка"
    
    show un evil_smile with dspr
    
    "Смущение"
    
    show un shy with dspr

    "Улыбка"
    
    show un smile with dspr
    
    "Улыбка_2"
    
    show un smile2 with dspr
    
label un_2_close:

    "Поза 2"
    
    "Плачь"
    
    show un apron cry close at center with dissolve
    
    "Плачь с улыбкой"
    
    show un cry_smile with dspr 
    
    "Грусть"

    show un sad with dspr
    
    "Испуг"
    
    show un scared with dspr
    
    "Шок"
    
    show un shocked with dspr
    
    "Удивление"
    
    show un surprise with dspr
    
    "Злая2"
    
    show un angry2 with dspr

label un_3_close:

    "Поза 3"
    
    "Ухмылка"

    show un apron grin close at center with dissolve
    
    "Смех"

    show un laugh with dspr
    
    "Ярость"
    
    show un rage with dspr
    
    "Серьёзная"
    
    show un serious with dspr
    
    "Улыбка_3"
    
    show un smile3 with dspr
    
    "Кликни чтобы выйти"
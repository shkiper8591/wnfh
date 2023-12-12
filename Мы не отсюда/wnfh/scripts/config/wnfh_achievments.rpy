init 0 python:

    # ДАЛЬШЕ БОГА НЕТ
    # ДАЛЬШЕ БОГА НЕТ
    # ДАЛЬШЕ БОГА НЕТ
    
    ## Регистрация ачивок ##
    
    wnfh_ach_list = [
        #Тэг ачивки   Иконка            Заголовк                 Подпись                             Трофей             Персонаж
        ["payday"    ,"icon_payday"    ,"Конфетный вор"         ,"Было весело"                      ,"trophy_silver"   ,"usw"],
        ["spirt"     ,"icon_spirt"     ,"Где мне найти спирт?"  ,"Живая вода"                       ,"trophy_silver"   ,"usw"],   
        ["bkrr"      ,"icon_bkrr"      ,"Да, именно"            ,"Это отсылка на БКРР"              ,"trophy_bronz"    ,"kat"],     
        ["alpha"     ,"icon_alpha-0.1" ,"Первопроходец"         ,"Version alpha-0.1"                ,"trophy_gold"     ,"kat"],
        ["post"      ,"icon_post"      ,"Груз доставлен"        ,"Почти без повреждений"            ,"trophy_bronz"    ,"kat"],     
        ["zgdun"     ,"icon_zgdun"     ,"Великий ждун"          ,"Дети уже школу закончили?"        ,"trophy_gold"     ,"kat"],    
        ["alarm"     ,"icon_alarm"     ,"Das Boot"              ,"Доплавался, блин"                 ,"trophy_silver"   ,"kat"],
        ["zaebist"   ,"icon_zaebist"   ,"Всё идёт по плану"     ,"При коммунизме всё будет заебись" ,"trophy_silver"   ,"kat"],
        ["handass"   ,"icon_handass"   ,"Рукожоп"               ,"Ну как так-то?"                   ,"trophy_bronz"    ,"kat"],
    ]

    if not persistent.wnfh_ach:
        persistent.wnfh_ach = dict()
    
    ## Создание ачивки ##
    
    for ach in wnfh_ach_list:
        renpy.image("wnfh_ach_" + ach[0], im.Composite(
        (590, 100),
        (0  , 0  ), im.MatrixColor(im.Scale(wnfh_gui["banners"]["ach_frame_1_2"], 590, 100), im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
        (0  , 0  ), im.MatrixColor(im.Scale(wnfh_gui["banners"]["ach_frame_1_1"], 590, 100), im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
        (94 , 12 ), im.Scale(wnfh_BANNERS + ach[1] + ".png"  , 75 , 75 ),
        (515, 15 ), im.Scale(wnfh_BANNERS + "leaf_" + persistent.timeofday + ".png"  , 45 , 68 ),
        (184, 50 ), im.Scale(wnfh_BANNERS + ach[4] + ".png"  , 38 , 38 ),
        ))

        if ach[0] not in persistent.wnfh_ach:
            persistent.wnfh_ach[ach[0]] = False
    
    ##Это для отображения на странице с ачивками
    import renpy.display.im as im

    for ach in wnfh_ach_list:
        renpy.image("wnfh_ach_menu_" + ach[0], im.Composite(
            (455, 99),
            (12, 12 ), im.Scale(wnfh_BANNERS + ach[1] + ".png"  , 75 , 75 ),
            (0, 0), im.Scale(wnfh_gui["banners"]["ach_menu_frame"], 455, 99),
        ))
    
    renpy.image("wnfh_ach_lock", im.Scale(wnfh_gui["banners"]["ach_menu_frame_lock"], 455, 99))

    ## Призыв ачивок ##
    
    def wnfh_get_achievement(ach):
        if not persistent.wnfh_ach[ach]:
            persistent.wnfh_ach[ach] = True
            renpy.play(wnfh_sfx_list["ps4_ach"], channel="sound")
            
            renpy.show("wnfh_ach_" + ach, [wnfh_get_achievement_atl], behind=["ach_title" + str(i), "ach_signature" + str(i)])
            for index,title in enumerate(wnfh_ach_list, start = 0):
                if ach in title:
                    num = index
            renpy.show("ach_title", [wnfh_get_ach_title_atl], tag="ach_title" + str(i), what=Text(wnfh_ach_list[num][2], style=style.wnfh_ach_title, size=30))
            renpy.show("ach_signature", [wnfh_get_ach_signature_atl], tag="ach_signature" + str(i), what=Text(wnfh_ach_list[num][3], style=style.wnfh_ach_signature, size=27))
            
            renpy.pause(7.5)
            renpy.hide("wnfh_ach_" + ach)
            renpy.hide("ach_title")
            renpy.hide("ach_signature")
    
    ## Подсчёт ачивок ##
    
    def wnfh_check_achievements():
        j = 0
        for i in persistent.wnfh_ach.values():
            if i:
                j += 1
        return j
    
    ## Обнуление ачивок ##
    
    def wnfh_reset_achievements():
        for ach in wnfh_ach_list:
            persistent.wnfh_ach[ach[0]] = False
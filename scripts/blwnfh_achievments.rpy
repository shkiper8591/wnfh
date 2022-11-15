init -1 python:
    
    ## Объявляем разные картинки ##
    
    
    
    ## Регистрация ачивок ##
    
    blwnfh_ach_list = (
        #Тэг ачивки   Иконка            Заголовк           Подпись                Листок         Трофей
        ("payday"    ,"icon_payday"    ,"title_payday"    ,"signature_payday"    ,"leaf_day"    ,"trophy_silver"),   
        ("bkrr"      ,"icon_bkrr"      ,"title_bkrr"      ,"signature_bkrr"      ,"leaf_sunset" ,"trophy_bronz"),     
        ("alpha-0.1" ,"icon_alpha-0.1" ,"title_alpha-0.1" ,"signature_alpha-0.1" ,"leaf_day"    ,"trophy_platina"),
        ("post"      ,"icon_post"      ,"title_post"      ,"signature_post"      ,"leaf_day"    ,"trophy_bronz"),     
        ("zgdun"     ,"icon_zgdun"     ,"title_zgdun"     ,"signature_zgdun"     ,"leaf_day"    ,"trophy_platina"),    
        ("alarm"     ,"icon_alarm"     ,"title_alarm"     ,"signature_alarm"     ,"leaf_day"    ,"trophy_silver"),
        ("zaebist"   ,"icon_zaebist"   ,"title_zaebist"   ,"signature_zaebist"   ,"leaf_day"    ,"trophy_silver"),
        ("handass"   ,"icon_handass"   ,"title_handass"   ,"signature_handass"   ,"leaf_day"    ,"trophy_bronz"),
    )
    
    
    
    if not persistent.blwnfh_ach:
        persistent.blwnfh_ach = dict()
    
    ## Создание ачивки ##
    
    for ach in blwnfh_ach_list:
        renpy.image("blwnfh_ach_" + ach[0], im.Composite(
        (600, 125),
        (0, 0), im.Scale(blwnfh_gui["banners"]["ach_frame"], 600, 125),
        (94, 26), im.Scale(blwnfh_BANNERS + ach[1] + ".png", 75, 75),
        (0, 0), im.Scale(blwnfh_BANNERS + ach[2] + ".png", 600, 125),
        (0, 0), im.Scale(blwnfh_BANNERS + ach[3] + ".png", 600, 125),
        (515, 30), im.Scale(blwnfh_BANNERS + ach[4] + ".png", 45, 68),
        (184, 65), im.Scale(blwnfh_BANNERS + ach[5] + ".png", 38, 38),
        ))
        
        if ach[0] not in persistent.blwnfh_ach:
            persistent.blwnfh_ach[ach[0]] = False
    
    ##Это для отображения на странице с ачивками
    #for ach in blwnfh_ach_list:
    #    renpy.image("blwnfh_ach_" + ach[1], im.Scale(blwnfh_ACHIEVEMENTS + ach[1] + ".png", 1177, 150))
    #    if ach[1] not in persistent.blwnfh_ach:
    #        persistent.blwnfh_ach[ach[1]] = False
    #
    #renpy.image("blwnfh_ach_lock", im.Scale(blwnfh_ACHIEVEMENTS + "lock.png", 1177, 150))
    
    
    ## Призыв ачивок ##
    
    def blwnfh_get_achievement(ach):
        if not persistent.blwnfh_ach[ach]:
            persistent.blwnfh_ach[ach] = True
            renpy.play(blwnfh_sfx_list["ps4_ach"], channel="sound")
            renpy.show("blwnfh_ach_" + ach, [blwnfh_get_achievement_atl])
            renpy.pause(7.5)
            renpy.hide("blwnfh_ach_" + ach)
            
    ## Подсчёт ачивок ##
    
    def blwnfh_check_achievements():
        j = 0
        for i in persistent.blwnfh_ach.values():
            if i:
                j += 1
        return j
    
    ## Обнуление ачивок ##
    
    def blwnfh_reset_achievements():
        for ach in blwnfh_ach_list:
            persistent.blwnfh_ach[ach[0]] = False
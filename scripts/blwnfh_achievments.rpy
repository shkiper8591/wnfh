init -1 python:
    
    ## Регистрация ачивок ##
    
    blwnfh_ach_list = (
        ("payday", "payday_icon"),
        ("bkrr", "bkrr_icon"),
        ("alpha-0.1", "alpha-0.1_icon"),
        ("post", "post_icon"),
        ("zgdun", "zgdun_icon"),
        ("alarm", "alarm_icon")
    )
    
    if not persistent.blwnfh_ach:
        persistent.blwnfh_ach = dict()
    
    #Это для появления в игре
    for ach in blwnfh_ach_list:
        renpy.image("blwnfh_ach_" + ach[0], im.Scale(blwnfh_ACHIEVEMENTS + ach[0] + ".png", 600, 125))
        if ach[0] not in persistent.blwnfh_ach:
            persistent.blwnfh_ach[ach[0]] = False
    
    #Это для отображения на странице с ачивками
    for ach in blwnfh_ach_list:
        renpy.image("blwnfh_ach_" + ach[1], im.Scale(blwnfh_ACHIEVEMENTS + ach[1] + ".png", 1177, 150))
        if ach[1] not in persistent.blwnfh_ach:
            persistent.blwnfh_ach[ach[1]] = False
    
    renpy.image("blwnfh_ach_lock", im.Scale(blwnfh_ACHIEVEMENTS + "lock.png", 1177, 150))
    
    
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
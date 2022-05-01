init 1:
    
    # Бежит бежит бежит
    
    transform blwnfh_running:
        truecenter
        zoom 1.25
        parallel:
            ease 0.25 zoom 1.30 rotate 0.75
            ease 0.20 zoom 1.25 rotate -0.75
            ease 0.25 zoom 1.30 rotate 0.75
            ease 0.20 zoom 1.35 rotate -0.75
            repeat
        parallel:
            ease 0.25 xpos 0.495
            ease 0.20 xpos 0.505
            repeat
        parallel:
            ease 0.25 ypos 0.495
            ease 0.30 ypos 0.505
            repeat
        
    transform fatigue:
        block:
            zoom 1.4 xcenter 0.5 ycenter 0.3
        block:
            ease 1 xoffset 0 yoffset 0
            ease 1 xoffset 15 yoffset 40
            ease 1 xoffset 0 yoffset 0
            ease 1 xoffset -15 yoffset 40
        repeat
    
    # Размещение спрайтов на экране (сидя)

    transform blwnfh_sit_left:
        xalign 0.28
        xanchor 0.5
        yanchor 0.0
        ypos 0.22

    transform blwnfh_sit_center:
        xalign 0.5
        yanchor 0.0
        ypos 0.22

    transform blwnfh_sit_right:
        xalign 0.72
        xanchor 0.5
        yanchor 0.0
        ypos 0.22
        
    # Для персонажей невысокого роста и для дистанции close

    transform blwnfh_sit_left_close:
        xalign 0.28
        xanchor 0.5
        yanchor 0.0
        ypos 0.15

    transform blwnfh_sit_center_close:
        xalign 0.5
        yanchor 0.0
        ypos 0.15

    transform blwnfh_sit_right_close:
        xalign 0.72
        xanchor 0.5
        yanchor 0.0
        ypos 0.15
        
    # Анимации "встань" и "сядь" для спрайтов

    transform sit_down:
        subpixel True
        parallel:
            ease 1.0 ypos 0.22
        parallel:
            ease 0.75 zoom 1.05
            ease 0.5 zoom 1.0

    transform sit_down1:
        subpixel True
        parallel:
            ease 1.0 ypos 0.15
        parallel:
            ease 0.75 zoom 1.05
            ease 0.5 zoom 1.0

    transform sit_down1_close:
        subpixel True
        parallel:
            ease 1.0 ypos 0.05
        parallel:
            ease 0.75 zoom 1.05
            ease 0.5 zoom 1.0

    transform get_up:
        subpixel True
        parallel:
            ease 1.0 ypos 0.0
        parallel:
            ease 0.75 zoom 1.05
            ease 0.5 zoom 1.0

    transform get_up_fast:
        subpixel True
        parallel:
            ease 0.3 ypos 0.0
        parallel:
            ease 0.2 zoom 1.05
            ease 0.07 zoom 1.0

    # Анимация стула, когда персонаж встаёт или садится

    transform chair_move_sd:
        yanchor 0.0
        ypos 0.1
        zoom 0.95
        ease 0.75 ypos 0.0 zoom 1.0

    transform chair_move_gu:
        yanchor 0.0
        ease 0.75 ypos 0.1 zoom 0.95
        
    # Эффект двоения в глазах

    transform blwnfh_doubvis(imgn, z=1.1, zt=1.0, t=1.0):
        contains:
            ImageReference(imgn)
            truecenter
            linear zt zoom z
        contains:
            ImageReference(imgn)
            truecenter
            zoom z
            alpha 0.0
            pause zt
            linear t xpos 0.48 alpha 0.3 zoom (z + 0.05)
        contains:
            ImageReference(imgn)
            truecenter
            zoom z
            alpha 0.0
            pause zt
            linear t xpos 0.51 alpha 0.2 zoom (z + 0.05)

    transform blwnfh_doubvis_vert(imgn, z=1.1, zt=1.0, t=1.0, first=39, second=11):
        contains:
            ImageReference(imgn)
            truecenter
            linear zt zoom z
        contains:
            ImageReference(imgn)
            truecenter
            zoom z
            alpha 0.0
            pause zt
            parallel:
                linear t alpha 0.3 zoom (z + 0.05)
            parallel:
                linear 5.0 rotate -first
                linear 10.0 rotate first
                linear 5.0 rotate 0
                repeat
        contains:
            ImageReference(imgn)
            truecenter
            zoom z
            alpha 0.0
            pause zt
            linear t alpha 0.2 zoom (z + 0.05)
            parallel:
                linear 1.0 rotate second
                linear 2.0 rotate -second
                linear 1.0 rotate 0
                repeat
            parallel:
                linear 1.5 zoom (z + 0.15)
                linear 2.5 zoom (z + 0.05)
    
    # Эффект для моментов пробуждения

    transform blwnfh_wakeup(imgn):
        contains:
            ImageReference(imgn)
        contains:
            im.MatrixColor(ImageReference(imgn), im.matrix.brightness(0.5))
            truecenter
            alpha 0.9
            zoom 1.05
            ease 5.0 alpha 0.0 zoom 1.0
        contains:
            im.MatrixColor(ImageReference(imgn), im.matrix.brightness(0.5))
            truecenter
            alpha 0.9
            zoom 1.075
            ease 5.0 alpha 0.0 zoom 1.0

    transform blwnfh_wakeup_dark(imgn):
        contains:
            ImageReference(imgn)
        contains:
            im.MatrixColor(ImageReference(imgn), im.matrix.brightness(0.1))
            truecenter
            alpha 0.9
            zoom 1.05
            ease 5.0 alpha 0.0 zoom 1.0
        contains:
            im.MatrixColor(ImageReference(imgn), im.matrix.brightness(0.1))
            truecenter
            alpha 0.9
            zoom 1.075
            ease 5.0 alpha 0.0 zoom 1.0
    
    # Анимации получения ачивментов и предметов

    transform blwnfh_get_achievement_atl:
        pos(-0.4, 0.15)
        anchor(0.0, 0.5)
        ease 1.0 pos(0.0, 0.15)
        pause 3.0
        ease 1.0 pos(-0.4, 0.15)
        
    transform blwnfh_get_item_atl:
        pos(-0.1, 0.75)
        anchor(0.0, 0.5)
        alpha 0.0
        ease 1.0 pos(0.0, 0.75) alpha 1.0
        pause 3.0
        ease 1.0 pos(-0.1, 0.75) alpha 0.0
    
init python:
    
    # Регистрация ачивок и предметов
    
    blwnfh_ach_list = (
        ("payday", u"Конфетный вор"),
    )
    
    if not persistent.blwnfh_ach:
        persistent.blwnfh_ach = dict()
    
    for ach in blwnfh_ach_list:
        renpy.image("blwnfh_ach_" + ach[0], im.Scale(blwnfh_IMAGES + "gui/achievements/" + ach[0] + ".png", 600, 125))
        if ach[0] not in persistent.blwnfh_ach:
            persistent.blwnfh_ach[ach[0]] = False
    
    renpy.image("blwnfh_ach_blank", im.Scale(blwnfh_IMAGES + "gui/achievements/blank.png", 600, 125))
    
    blwnfh_item_list = ("knife", "paint", "tape", "key", "food", "powder", "accumulator", "comb", "pills", "apple", "note", "shark_tooth", "matchbox", "love_letter", "tabs", "bandana", "gram", "birth_certificate", "roses", "healing_potion")
    
    for item in blwnfh_item_list:
        renpy.image("blwnfh_item_" + item, im.Scale(blwnfh_IMAGES + "gui/items/" + item + ".png", 450, 360))
    
    # Призыв ачивок и предметов
    
    def blwnfh_get_achievement(ach):
        if not persistent.blwnfh_ach[ach]:
            persistent.blwnfh_ach[ach] = True
            renpy.play(blwnfh_sfx_list["ps4_ach"], channel="sound")
            renpy.show("blwnfh_ach_" + ach, [blwnfh_get_achievement_atl])
            renpy.pause(7.5)
            renpy.hide("blwnfh_ach_" + ach)

    def blwnfh_get_item(item, sounded=True):
        if sounded:
            renpy.play(blwnfh_sfx_list["get_item"], channel="sound")
        renpy.show("blwnfh_item_%s" % item, [blwnfh_get_item_atl])
        renpy.pause(5.0)
        renpy.hide("blwnfh_item_%s" % item)
    
    # Просто полезная херня
    
    def blwnfh_check_achievements():
        j = 0
        for i in persistent.bkrr_ach.values():
            if i:
                j += 1
        return j
    
    def blwnfh_reset_achievements():
        for ach in blwnfh_ach_list:
            persistent.blwnfh_ach[ach[0]] = False
    

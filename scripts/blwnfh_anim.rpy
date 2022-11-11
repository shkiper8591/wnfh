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
        ypos 0.09

    transform blwnfh_sit_right:
        xalign 0.72
        xanchor 0.5
        yanchor 0.0
        ypos 0.09
        
    # Для персонажей невысокого роста и для дистанции close

    transform blwnfh_sit_left_close:
        xalign 0.28
        xanchor 0.5
        yanchor 0.0
        ypos 0.02

    transform blwnfh_sit_right_close:
        xalign 0.72
        xanchor 0.5
        yanchor 0.0
        ypos 0.02
        
    # Анимации "встань" и "сядь" для спрайтов

    transform sit_down:
        subpixel True
        parallel:
            ease 1.0 ypos 0.12
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


    transform chair_move_out: # Отодвигается
        yanchor 0.0
        ease 0.75 zoom 0.95
    
    transform chair_move_in: # Задвигается
        yanchor 0.0 
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
    
    transform blwnfh_get_table_atl:
        pos(-0.4, 0.15)
        anchor(0.0, 0.5)
        alpha 0.0
        ease 1.0 pos(0.0, 0.15) alpha 1.0
        pause 4.0
        ease 1.0 pos(-0.4, 0.15) alpha 0.0

    transform blwnfh_technical_chocolatki:
        xpos 0.25
        xzoom -1
        pause 0.333
        xzoom 1
        pause 0.333
        repeat

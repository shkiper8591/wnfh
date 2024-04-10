init -5:
    
    # Заход в здание
    transform wnfh_entrance(x = 0.5):
        pos(x, 0.5)
        anchor(x, 0.5)
        subpixel True
        #truecenter
        #zoom 1.0
        ease_quart 2.0 zoom 1.5
    
    # Бежит бежит бежит
    
    transform wnfh_running:
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

    transform wnfh_sit_left:
        xalign 0.28
        xanchor 0.5
        yanchor 0.0
        ypos 0.09

    transform wnfh_sit_right:
        xalign 0.72
        xanchor 0.5
        yanchor 0.0
        ypos 0.09
        
    # Для персонажей невысокого роста и для дистанции close

    transform wnfh_sit_left_close:
        xalign 0.28
        xanchor 0.5
        yanchor 0.0
        ypos 0.02

    transform wnfh_sit_right_close:
        xalign 0.72
        xanchor 0.5
        yanchor 0.0
        ypos 0.02
        
    # Анимации "встань" и "сядь" для спрайтов
    
    transform go_to_chair_left:
        subpixel True
        ease_quart 2.0 xpos 0.44
    
    transform go_to_chair_right:
        subpixel True
        ease 1.0 xpos 0.85
    
    transform sit_down_left:
        subpixel True
        ease_quart 2.0 xpos 0.28
        parallel:
            ease 1.0 ypos 0.12
        parallel:
            ease 0.75 zoom 1.05
            ease 0.5 zoom 1.0
    
    transform sit_down_right:
        subpixel True
        ease_quart 2.0 xpos 0.72
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

    transform wnfh_doubvis(imgn, z=1.1, zt=1.0, t=1.0):
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

    transform wnfh_doubvis_vert(imgn, z=1.1, zt=1.0, t=1.0, first=39, second=11):
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
                ease t alpha 0.3 zoom (z + 0.05)
            parallel:
                ease 7.0 rotate -first
                ease 7.0 rotate first
                repeat
        contains:
            ImageReference(imgn)
            truecenter
            zoom z
            alpha 0.0
            pause zt
            linear t alpha 0.2 zoom (z + 0.05)
            parallel:
                ease 3.0 rotate second
                ease 3.0 rotate -second
                repeat
            parallel:
                ease 1.5 zoom (z + 0.15)
                ease 2.5 zoom (z + 0.05)
    
    # Эффект для моментов пробуждения

    transform wnfh_wakeup(imgn):
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

    transform wnfh_wakeup_dark(imgn):
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

    transform wnfh_get_achievement_atl:
        subpixel True
        pos(-0.5, 0.15)
        anchor(0.0, 0.5)
        ease_quart 1.5 pos(-0.05, 0.15)
        pause 5.0
        ease_quart 1.5 pos(-0.5, 0.15)
    
    transform wnfh_get_ach_title_atl(x_pos=0.095, y_pos=0.131):
        pos(x_pos-0.4, y_pos)
        anchor(0.0, 0.5)
        ease 1.0 pos(x_pos, y_pos)
        pause 3.0
        ease 1.0 pos(x_pos-0.4, y_pos)
        
    transform wnfh_get_ach_signature_atl(x_pos=0.119, y_pos=0.17):
        pos(x_pos-0.4, y_pos)
        anchor(0.0, 0.5)
        ease 1.0 pos(x_pos, y_pos)
        pause 3.0
        ease 1.0 pos(x_pos-0.4, y_pos)
        
    transform wnfh_get_item_atl:
        pos(-0.1, 0.75)
        anchor(0.0, 0.5)
        alpha 0.0
        ease 1.0 pos(0.0, 0.75) alpha 1.0
        pause 3.0
        ease 1.0 pos(-0.1, 0.75) alpha 0.0
    
    transform wnfh_get_table_atl:
        pos(-0.4, 0.15)
        anchor(0.0, 0.5)
        alpha 0.0
        ease 1.0 pos(0.0, 0.15) alpha 1.0
        pause 4.0
        ease 1.0 pos(-0.4, 0.15) alpha 0.0

    transform wnfh_technical_chocolatki:
        xpos 0.25
        xzoom -1
        pause 0.333
        xzoom 1
        pause 0.333
        repeat

    # Огонь #

    transform wnfh_fire_light_atl(imgf):
        im.MatrixColor(imgf, im.matrix.brightness(0.17))
        choice 2:
            ease 0.4 alpha 0.5
        choice 2:
            ease 0.3 alpha 0.75
        choice 2:
            ease 0.3 alpha 0.6
        choice:
            ease 0.25 alpha 0.9
        choice:
            ease 0.2 alpha 1.0
        repeat
    
    # Анимации предметов #
    
    transform wnfh_get_item_atl(pos_x, pos_y):
        xalign (0.0)
        pos(pos_x, 0.18)
        anchor(0.0, 0.5)
        alpha 0.0
        pause 1.0
        ease 1.0 pos(pos_x, pos_y) alpha 1.0
        pause 3.0
        ease 1.0 pos(-0.4, pos_y) alpha 0.0

    transform wnfh_item_icon_atl(pos_x_start, pos_y_start, pos_x_mid, pos_y_mid, pos_x_end, pos_y_end):
        pos(pos_x_start, pos_y_start)
        anchor(0.0, 0.5)
        alpha 0.0
        pause 2.5
        ease 2.5 pos(pos_x_mid, pos_y_mid) alpha 1.0
        ease 1.0 pos(pos_x_end, pos_y_end) alpha 0.0
        
    # Анимации реакции персонажей #
        
    transform wnfh_get_relation_atl(pos_x, pos_y):
        xalign (0.0)
        pos(pos_x, 0.18)
        anchor(0.0, 0.5)
        alpha 0.0
        pause 1.0
        ease 1.0 pos(pos_x, pos_y) alpha 1.0
        pause 3.0
        ease 1.0 pos(-0.4, pos_y) alpha 0.0

    transform wnfh_relation_indicator_atl(pos_x_start, pos_y_start, pos_x_mid, pos_y_mid, pos_x_end, pos_y_end):
        pos(pos_x_start, pos_y_start)
        anchor(0.0, 0.5)
        alpha 0.0
        pause 2.5
        ease 2.5 pos(pos_x_mid, pos_y_mid) alpha 1.0
        ease 1.0 pos(pos_x_end, pos_y_end) alpha 0.0
    
    ## Анимации меню ##
    
    # Главное меню #
    
    transform wnfh_bg_spawn_atl():
        subpixel True
        truecenter
        on show:
            alpha 0.0
            ease 4.0 alpha 1.0

    transform wnfh_news_spawn_atl():
        zoom 0.0
        ease 0.5 zoom 1.2
        ease 0.2 zoom 1.0

    transform wnfh_mm_button_hover_atl(z = 1.0):
        pos(0.5, 0.5)
        anchor(0.5, 0.5)
        on hover:
            ease 0.15 zoom (z - 0.15)
            ease 0.15 zoom (z - 0.02)
        on idle:
            ease 0.15 zoom z
            
    transform wnfh_splash_anim(x, y, rot):
        block:
            rotate rot
            pos(x, y)
            anchor(0.5, 0.5)
        block:
            ease 0.25 zoom 1.30
            ease 0.20 zoom 1.25
        repeat
    
    ## Временное говно ##
    transform wnfh_menu_pos_atl(z, x, y, rot):
        zoom z
        pos(x, y)
        anchor(0.5, 0.5)
        rotate rot
        wnfh_menu_hover_atl(z, rot)
        
    transform wnfh_menu_hover_atl(z, rot):
        on hover:
            ease 0.1 zoom (z - 0.15) rotate 0.0
            ease 0.1 zoom (z - 0.02)
        on idle:
            ease 0.1 zoom z rotate rot
    
    # Меню ачивок #
    
    transform wnfh_ach_char_banners(z, x, y):
        zoom z
        pos(x, y)
        anchor(0.5, 0.55)
        wnfh_ach_char_banners_hover(z)
    transform wnfh_ach_char_banners_hover(z):
        on hover:
            ease 0.1 zoom (z - 0.08)
            ease 0.1 zoom (z - 0.02)
        on idle:
            ease 0.1 zoom z
            
    # Меню галереи #
    
    transform wnfh_gallery_item_atl:
        subpixel True
        truecenter
        on hover:
            ease 0.25 zoom 0.95
        on idle:
            ease 0.1 zoom 1.0
        
    transform wnfh_gallery_mode_atl:
        subpixel True
        truecenter
        on hover:
            ease 0.25 zoom 1.25
        on idle:
            ease 0.1 zoom 1.0
    
    transform atl_wnfh_widget_lp_down:
        subpixel True
        truecenter
        on show:
            ypos -0.2
            ease_quart 1.0 ypos 0.08
        on hide:
            ypos 0.08
            ease_quart 1.0 ypos -0.2

    transform atl_wnfh_game_menu_selector(pause):
        subpixel True
        choice:
            xpos 0.0 xanchor 0.5 yanchor 0.5 alpha 0.0
        choice:
            xpos 1.0 xanchor 0.5 yanchor 0.5 alpha 0.0
        pause (1 + pause)/6
        ease_quart 1 xpos 0.5 ypos 0.5 alpha 1.0

    transform wjuh_bg:
        subpixel True
        yzoom 0.0 xzoom 0.0
        block:
            ease_quart 0.5 xzoom 1.0
        block:
            ease_quart 0.5 yzoom 1.0

    transform wjuh_line:
        subpixel True
        xzoom 0.0
        ease_quart 0.5 xzoom 1.0

    transform wnfh_dissolve:
        alpha 0.0
        ease_quart 1.0 alpha 1.0

    transform wnfh_db_red_small:
        subpixel True
        ysize 150
        ease 0.5 ysize 100
    transform wnfh_db_red_large:
        subpixel True
        ysize 100
        ease 0.5 ysize 150

    transform wnfh_db_green_small:
        subpixel True
        xsize 802
        ease 0.5 xsize 902
    transform wnfh_db_green_large:
        subpixel True
        xsize 902
        ease 0.5 xsize 802

    transform wnfh_db_blue_small:
        subpixel True
        xsize 320
        ease 0.5 xsize 220
    transform wnfh_db_blue_large:
        subpixel True
        xsize 220
        ease 0.5 xsize 320

    transform wnfh_db_buttons_small:
        subpixel True
        ypos 0.5
        ease 0.5 ypos 0.65
    transform wnfh_db_buttons_large:
        subpixel True
        ypos 0.65
        ease 0.5 ypos 0.5

    transform wnfh_pass:
        subpixel True
        pass
init -3:
    transform govno_ebanoe:
        on hover:
            ImageReference(wnfh_gui["tint_elements"]["button_hover"])
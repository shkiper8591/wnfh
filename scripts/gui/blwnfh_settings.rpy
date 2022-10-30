init 2:
    
    screen blwnfh_settings_menu():
        modal True tag menu
        
        key "game_menu":
            action NullAction()
        
        key "screenshot":
            action NullAction()
        
        frame:
            background blwnfh_gui["img"]["fon"]
            area(0.0, 0.0, 1.0, 1.0)
            
            imagebutton:
                action ShowMenu("blwnfh_menu")
                idle blwnfh_gui["gallery"]["back"]
                hover blwnfh_gui["gallery"]["back"]
                hover_sound blwnfh_gui["sound"]["plimp"]
                at blwnfh_menu_pos_atl(0.82, 0.1, 0.082, 0.0)
                
        python:
            blwnfh_posx = .333
            blwnfh_posy = .52
        
            from random import randrange
            
            def menu_img_status(imgf, condition="hover"):
                if condition == "hover":
                    return im.MatrixColor(imgf, im.matrix.contrast(1.7))
                if condition == "insensitive":
                    return im.Alpha(imgf, 0.38)
                    
            menu_hovered_action_plimp = Play("sound", blwnfh_gui["sound"]["plimp"])
            menu_hovered_action_cat = Play("sound", blwnfh_GUI + "meow" + str(randrange(6)) + ".ogg")
        
        default play_text = False
        default settings_text = False
        default galary_text = False
        default achievements_text = False
        default scheme_text = False
        default dlc_text = False
        default info_text = False
        default exit_text = False
        
        if play_text:
            text "Играть"       style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0 
        elif settings_text:
            text "Настройки"    style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0 
        elif galary_text:
            text "Галерея"      style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0 
        elif achievements_text:
            text "Достижения"   style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0 
        elif scheme_text:
            text "Схема"        style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0
        elif dlc_text:
            text "Дополнения"   style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0
        elif info_text:
            text "Информация"   style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0
        elif exit_text:
            text "Выход"        style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0
        else:
            null height 20
            
        text blwnfh_get_usertime():
            align(0.9265625, 0.0844444)
            font blwnfh_FONTS + "msjhl.ttc"
            size 30

        text "Настройки":
            align(0.5, 0.06)
            style "blwnfh_title"
            size 80
            kerning 2
        
        if not persistent.sukablyat_blwnfh:
            textbutton "Виджет (ЛП): выкл." xpos 0.65 ypos 0.255:
                style "blwnfh_menu"
                hover_sound blwnfh_gui["sound"]["plimp"]
                hovered Show("settings_widget_sukablyat_on_blwnfh", transition=Dissolve(0.2))
                unhovered [Hide("settings_widget_sukablyat_on_blwnfh", transition=Dissolve(0.2))]
                action [SetField(persistent,'lp_widget_7dl', True), Hide("settings_widget_sukablyat_on_blwnfh", transition=Dissolve(0.2)), Show("settings_widget_sukablyat_off_blwnfh", transition=Dissolve(0.2))]
        else:
            textbutton "Виджет (ЛП): вкл." xpos 0.65 ypos 0.255:
                style "blwnfh_menu"
                hover_sound blwnfh_gui["sound"]["plimp"]
                hovered Show("settings_widget_sukablyat_off_blwnfh", transition=Dissolve(0.2))
                unhovered [Hide("settings_widget_sukablyat_off_blwnfh", transition=Dissolve(0.2))]
                action [SetField(persistent,'lp_widget_7dl', False), Hide("settings_widget_sukablyat_off_blwnfh", transition=Dissolve(0.2)), Show("settings_widget_sukablyat_on_blwnfh", transition=Dissolve(0.2))]

        
        frame:
            background "#0005"
            area(1201, 466, 655, 550)
            
            frame:
                background "#0000"
                left_margin 20
                right_margin 30
                
                
                vbox:
                    align(0.5, 0.0)
    
                    null height 20
    
                    text u"Подсказка":
                        align(0.5, 0.0)
                        style "blwnfh_menu"
                        size 42
                        kerning 2.2
    
                    null height 25
    
                    viewport:
                        id "menu_news"
                        draggable True
                        mousewheel True
                        scrollbars None

                        
            vbar:
                value YScrollValue("menu_news")
                bottom_bar Frame(blwnfh_gui["img"]["vbar_full"], 0, 0)
                top_bar Frame(blwnfh_gui["img"]["vbar_null"], 0, 0)
                thumb "null"
                at Transform(alpha=0.74, align=(0.98, 0.5), xzoom=1.5, yzoom=0.92)
            

    transform blwnfh_menu_pos_atl(z, x, y, rot):
        zoom z
        pos(x, y)
        anchor(0.5, 0.5)
        rotate rot
        blwnfh_menu_hover_atl(z, rot)
        
    transform blwnfh_menu_hover_atl(z, rot):
        on hover:
            ease 0.1 zoom (z - 0.15) rotate 0.0
            ease 0.1 zoom (z - 0.02)
        on idle:
            ease 0.1 zoom z rotate rot
        
    transform blwnfh_splash_anim(x, y, rot):
        block:
            rotate rot
            pos(x, y)
            anchor(0.5, 0.5)
        block:
            ease 0.25 zoom 1.30
            ease 0.20 zoom 1.25
        repeat
        
screen settings_widget_sukablyat_on_blwnfh():
    text "Включить виджет для" xpos 0.653 ypos 0.6:
        style "blwnfh_menu"
    text "отображения прогресса и" xpos 0.653 ypos 0.646:
        style "blwnfh_menu"
    text "информации по моду (в" xpos 0.653 ypos 0.692:
        style "blwnfh_menu"
    text "т.ч. очков отношений)." xpos 0.653 ypos 0.738:
        style "blwnfh_menu"
screen settings_widget_sukablyat_off_blwnfh():
    text "Выключить виджет для" xpos 0.653 ypos 0.6:
        style "blwnfh_menu"
    text "отображения прогресса и" xpos 0.653 ypos 0.646:
        style "blwnfh_menu"
    text "информации по моду (в" xpos 0.653 ypos 0.692:
        style "blwnfh_menu"
    text "т.ч. очков отношений)." xpos 0.653 ypos 0.738:
        style "blwnfh_menu"
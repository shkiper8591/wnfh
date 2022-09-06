init 2:
    
    screen blwnfh_menu():
        modal True tag menu
        
        key "game_menu":
            action NullAction()
        
        key "screenshot":
            action NullAction()
        
        frame:
            background blwnfh_gui["img"]["fon"]
            area(0.0, 0.0, 1.0, 1.0)
        
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
            text "Играть" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0 
        elif settings_text:
            text "Настройки" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0 
        elif galary_text:
            text "Галлерея" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0 
        elif achievements_text:
            text "Достижения" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0 
        elif scheme_text:
            text "Схема" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0
        elif dlc_text:
            text "Дополнения" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0
        elif info_text:
            text "Информация" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0
        elif exit_text:
            text "Выход" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0
        else:
            null height 20
            
        text blwnfh_get_usertime():
            align(0.9265625, 0.0844444)
            font blwnfh_FONTS + "msjhl.ttc"
            size 30

        text "Мы не отсюда":
            align(0.5, 0.04)
            style "blwnfh_menu"
            size 80
            kerning 1
        
        text blwnfh_splash():
            font blwnfh_FONTS + "vcr_osd.ttf"
            color "#FFFF00"
            size 20
            at blwnfh_splash_anim(0.65, 0.138, -3.0)
        
        imagebutton:
            action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_test")]
            idle blwnfh_gui["img"]["fish"]
            hover blwnfh_gui["img"]["fish"]
            hovered menu_hovered_action_cat                       
            at blwnfh_menu_pos_atl(1.0, 0.088020833, 0.0944444, 0.0) 
        
        imagebutton:
            action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_test")]
            idle blwnfh_gui["img"]["play"]
            hover blwnfh_gui["img"]["play"]
            hover_sound blwnfh_gui["sound"]["plimp"]
            hovered ToggleScreenVariable("play_text")
            unhovered ToggleScreenVariable("play_text")            
            at blwnfh_menu_pos_atl(1.0, 0.233854167, 0.377777778, 0.0)
            
        imagebutton:
            action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_test")]
            idle blwnfh_gui["img"]["settings"]
            hover blwnfh_gui["img"]["settings"]
            hover_sound blwnfh_gui["sound"]["plimp"]
            hovered ToggleScreenVariable("settings_text")
            unhovered ToggleScreenVariable("settings_text")
            at blwnfh_menu_pos_atl(1.0, 0.088020833, 0.284259259, 0.0)
        
        imagebutton:
            action [Hide("blwnfh_menu", transition=dissolve), ShowMenu("blwnfh_gallery_menu")]
            idle blwnfh_gui["img"]["gallery"]
            hover blwnfh_gui["img"]["gallery"]
            hover_sound blwnfh_gui["sound"]["plimp"]
            hovered ToggleScreenVariable("galary_text")
            unhovered ToggleScreenVariable("galary_text")
            at blwnfh_menu_pos_atl(1.0, 0.380208333, 0.284259259, 0.0)
        
        imagebutton:
            action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_test")]
            idle blwnfh_gui["img"]["achievements"]
            hover blwnfh_gui["img"]["achievements"]
            hover_sound blwnfh_gui["sound"]["plimp"]
            hovered ToggleScreenVariable("achievements_text")
            unhovered ToggleScreenVariable("achievements_text")
            at blwnfh_menu_pos_atl(1.0, 0.4875, 0.284259259, 0.0)
        
        imagebutton:
            action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_test")]
            idle blwnfh_gui["img"]["scheme"]
            hover blwnfh_gui["img"]["scheme"]
            hover_sound blwnfh_gui["sound"]["plimp"]
            hovered ToggleScreenVariable("scheme_text")
            unhovered ToggleScreenVariable("scheme_text")
            at blwnfh_menu_pos_atl(1.0, 0.594270833, 0.284259259, 0.0)
        
        imagebutton:
            action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_test")]
            idle blwnfh_gui["img"]["dlc"]
            hover blwnfh_gui["img"]["dlc"]
            hover_sound blwnfh_gui["sound"]["plimp"]
            hovered ToggleScreenVariable("dlc_text")
            unhovered ToggleScreenVariable("dlc_text")
            at blwnfh_menu_pos_atl(1.0, 0.701041667, 0.284259259, 0.0)
        
        imagebutton:
            action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_test")]
            idle blwnfh_gui["img"]["info"]
            hover blwnfh_gui["img"]["info"]
            hover_sound blwnfh_gui["sound"]["plimp"]
            hovered ToggleScreenVariable("info_text")
            unhovered ToggleScreenVariable("info_text")
            at blwnfh_menu_pos_atl(1.0, 0.808333333, 0.284259259, 0.0)
        
        imagebutton:
            action Return()
            idle blwnfh_gui["img"]["exit"]
            hover blwnfh_gui["img"]["exit"]
            hover_sound blwnfh_gui["sound"]["plimp"]
            hovered ToggleScreenVariable("exit_text")
            unhovered ToggleScreenVariable("exit_text")
            at blwnfh_menu_pos_atl(1.0, 0.915104167, 0.284259259, 0.0)
        
        frame:
            background "#0005"
            area(1416, 466, 440, 550)

            vbox:
                align(0.5, 0.0)

                null height 20

                text u"Новости":
                    align(0.5, 0.0)
                    style "blwnfh_menu"
                    size 42
                    kerning 2.2

                null height 25
                
                text u"alpha 0.1\n Добавлено 6 дней. Добавлено 6 дней. Добавлено 6 дней. Добавлено 6 дней.":
                    pos(0.05, 0.0)
                    style "blwnfh_menu"
                    size 25
                    kerning 1
                
                viewport:
                        id "menu_ach_viewport"
                        draggable True
                        mousewheel True
                        scrollbars None
                
                

            vbar:
                value YScrollValue("menu_ach_viewport")
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

label blwnfh_main:
    $ init_splash()
    call screen blwnfh_menu with dspr
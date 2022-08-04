init 2:
    screen blwnfh_menu():
        tag menu
        modal True
        
        key "game_menu":
            action NullAction()

        key "screenshot":
            action NullAction()

        python:
        
            from random import randrange
            
            def menu_img_status(imgf, condition="hover"):
                if condition == "hover":
                    return im.MatrixColor(imgf, im.matrix.contrast(1.7))
                if condition == "insensitive":
                    return im.Alpha(imgf, 0.38)

            menu_hovered_action_plimp = Play("sound", blwnfh_gui["sound"]["plimp"])
            menu_hovered_action_cat = Play("sound", blwnfh_GUI + "meow" + str(randrange(6)) + ".ogg")
            
        frame:
            
            background blwnfh_gui["img"]["fon"]
            area(0.0, 0.0, 1.0, 1.0)
            
            text blwnfh_get_usertime():
                align(0.9265625, 0.0844444)
                font blwnfh_FONTS + "msjhl.ttc"
                size 30

            text "Мы не отсюда":
                align(0.5, 0.04)
                font blwnfh_FONTS + "msjhl.ttc"
                #style "blwnfh_menu"
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
                hovered menu_hovered_action_plimp                        
                at blwnfh_menu_pos_atl(1.0, 0.233854167, 0.377777778, 0.0)
                
            imagebutton:
                action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_test")]
                idle blwnfh_gui["img"]["settings"]
                hover blwnfh_gui["img"]["settings"]
                hovered menu_hovered_action_plimp
                at blwnfh_menu_pos_atl(1.0, 0.088020833, 0.284259259, 0.0)
            
            imagebutton:
                action [Hide("blwnfh_menu", transition=dissolve), ShowMenu("blwnfh_gallery_menu")]
                idle blwnfh_gui["img"]["gallery"]
                hover blwnfh_gui["img"]["gallery"]
                hovered menu_hovered_action_plimp
                at blwnfh_menu_pos_atl(1.0, 0.380208333, 0.284259259, 0.0)
            
            imagebutton:
                action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_test")]
                idle blwnfh_gui["img"]["achievements"]
                hover blwnfh_gui["img"]["achievements"]
                hovered menu_hovered_action_plimp
                at blwnfh_menu_pos_atl(1.0, 0.4875, 0.284259259, 0.0)
            
            imagebutton:
                action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_test")]
                idle blwnfh_gui["img"]["scheme"]
                hover blwnfh_gui["img"]["scheme"]
                hovered menu_hovered_action_plimp
                at blwnfh_menu_pos_atl(1.0, 0.594270833, 0.284259259, 0.0)
            
            imagebutton:
                action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_test")]
                idle blwnfh_gui["img"]["music"]
                hover blwnfh_gui["img"]["music"]
                hovered menu_hovered_action_plimp
                at blwnfh_menu_pos_atl(1.0, 0.701041667, 0.284259259, 0.0)
            
            imagebutton:
                action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_test")]
                idle blwnfh_gui["img"]["info"]
                hover blwnfh_gui["img"]["info"]
                hovered menu_hovered_action_plimp
                at blwnfh_menu_pos_atl(1.0, 0.808333333, 0.284259259, 0.0)
            
            imagebutton:
                action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_test")]
                idle blwnfh_gui["img"]["exit"]
                hover blwnfh_gui["img"]["exit"]
                hovered menu_hovered_action_plimp
                at blwnfh_menu_pos_atl(1.0, 0.915104167, 0.284259259, 0.0)

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
    call screen blwnfh_menu with dspr
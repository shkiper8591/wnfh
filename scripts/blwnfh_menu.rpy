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
                action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_test")]
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
    #screen blwnfh_menu_achievements():
    #    tag menu
    #    modal True
    #
    #    key "game_menu":
    #        action NullAction()
    #
    #    key "screenshot":
    #        action NullAction()
    #
    #    $ columns = 2
    #    $ rows = len(blwnfh_ach_list)+1
    #    
    #    frame:
    #        background blwnfh_gui["img"]["fon"]
    #        area(0.0, 0.0, 1.0, 1.0)
    #    
    #    imagebutton:
    #        align(0.9, 0.9)
    #        idle blwnfh_MAIN_MENU + "back_idle.png"
    #        hover blwnfh_MAIN_MENU + "back_hover.png"
    #        action Return()
    #        
    #    frame:
    #        background "#0005"
    #        area(128, 38, 1160, 985)
    #
    #        vbox:
    #            align(0.5, 0.0)
    #
    #            null height 50
    #
    #            text u"Достижения {size=-4}{k=0.0}(%s / %s){/k}{/size}" % (blwnfh_check_achievements(), len(blwnfh_ach_list)):
    #                align(0.5, 0.0)
    #                #style "bkrr_service2"
    #                size 42
    #                kerning 2.2
    #
    #            null height 25
    #            
    #            viewport:
    #                    id "menu_ach_viewport"
    #                    draggable True
    #                    mousewheel True
    #                    scrollbars None
    #
    #                    grid columns rows:
    #                        spacing 15
    #
    #                        for ach in blwnfh_ach_list:
    #                            if persistent.blwnfh_ach[ach[0]]:
    #                                imagebutton:
    #                                    action NullAction()
    #                                    idle ("blwnfh_ach_" + ach[0])
    #                                    hover im.MatrixColor(ImageReference("blwnfh_ach_" + ach[0]), im.matrix.contrast(1.3))
    #                                    align(0.75, 0.5)
    #                                text ach[1]:
    #                                    #style "bkrr_service2"
    #                                    size 36
    #                                    kerning 1.25
    #                                    align(1.0, 0.5)
    #                            else:
    #                                add im.Alpha(ImageReference("blwnfh_ach_blank"), 0.42):
    #                                    align(0.75, 0.5)
    #                                text u"Достижение не открыто.":
    #                                    #style "bkrr_service2"
    #                                    size 36
    #                                    kerning 1.25
    #                                    align(1.0, 0.5)
    #
    #                        null
    #
    #                        null
    #
    #            vbar:
    #                value YScrollValue("menu_ach_viewport")
    #                bottom_bar Frame(blwnfh_gui["img"]["vbar_full"], 0, 0)
    #                top_bar Frame(blwnfh_gui["img"]["vbar_null"], 0, 0)
    #                thumb "null"
    #                at Transform(alpha=0.74, align=(0.02, 0.5), xzoom=1.5, yzoom=0.92)
    #
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
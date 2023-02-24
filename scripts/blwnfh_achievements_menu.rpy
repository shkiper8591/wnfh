init 2:
    
    screen blwnfh_achievements():

        tag menu
        modal True

        key "game_menu":
            action NullAction()

        key "screenshot":
            action NullAction()

        $ columns = 2
        $ rows = 1

        # Основные элементы
        
        
        
        python:
            def achievements_make_thumb(imgf):
                return im.Scale(imgf, 357, 200)
        frame:
            background blwnfh_gui["img"]["fon"]
            area (0.0, 0.0, 1.0, 1.0)
        #{size=-4}{k=0.0}(%s / %s){/k}{/size} % (blwnfh_check_achievements(), len(blwnfh_ach_list))
            text u"Достижения {size=-4}{k=0.0}(%s / %s){/k}{/size}" % (blwnfh_check_achievements(), len(blwnfh_ach_list)):
                align(0.5, 0.04)
                style "blwnfh_menu"
                size 80
                kerning 1
                # back

            imagebutton:
                action ShowMenu("blwnfh_menu")
                idle blwnfh_gui["achievements"]["back"]
                hover blwnfh_gui["achievements"]["back"]
                hover_sound blwnfh_gui["sound"]["plimp"]
                at blwnfh_menu_pos_atl(0.82, 0.1, 0.082, 0.0)

            # achievements

            frame:
                background "#0005"
                area(300, 166, 1351, 845)
            
                frame:
                    background "#0000"
                    left_margin 60
                    #right_margin 30
                    
                    hbox:
                        align(0.5, 0.0)
                
                        null height 50
                        
                
                        null height 25
                
                        viewport:
                            id "menu_ach_viewport"
                            draggable True
                            mousewheel "horizontal"
                            scrollbars None
                            
                            imagebutton:
                                action ShowMenu("blwnfh_menu")
                                idle blwnfh_gui["banners"]["ach_kat_idle"]
                                hover blwnfh_gui["banners"]["ach_kat_hover"]
                                hover_sound blwnfh_gui["sound"]["plimp"]
                                at blwnfh_menu_pos_atl(0.82, 0.1, 0.5, 0.0)
                            #imagebutton:
                            #    action ShowMenu("blwnfh_menu")
                            #    idle blwnfh_gui["banners"]["ach_un_idle"]
                            #    hover blwnfh_gui["banners"]["ach_un_hover"]
                            #    hover_sound blwnfh_gui["sound"]["plimp"]
                            #    at blwnfh_menu_pos_atl(0.82, 0.5, 0.082, 0.0)
                            #for ach in blwnfh_ach_list:
                            #    if persistent.blwnfh_ach[ach[0]]:
                            #        imagebutton:
                            #            action NullAction()
                            #            idle ("blwnfh_ach_" + ach[1])
                            #            hover im.MatrixColor(ImageReference("blwnfh_ach_" + ach[1]), im.matrix.contrast(1.3))
                            #            align(0.75, 0.5)
                            #        text " ":
                            #            style "blwnfh_news"
                            #    else:
                            #        add im.Alpha(ImageReference("blwnfh_ach_lock"), 0.42):
                            #            align(0.75, 0.5)
                            #        text " ":
                            #            style "blwnfh_news"

                
                            #null
                            #
                            #null
                
                bar:
                    value YScrollValue("menu_ach_viewport")
                    bottom_bar Frame(blwnfh_gui["img"]["vbar_full"], 0, 0)
                    top_bar Frame(blwnfh_gui["img"]["vbar_null"], 0, 0)
                    thumb "null"
                    at Transform(alpha=0.74, align=(0.98, 0.5), xzoom=1.5, yzoom=0.92)

init 2:
    
    screen blwnfh_achievements():

        tag menu
        modal True

        key "game_menu":
            action NullAction()

        key "screenshot":
            action NullAction()

        $ columns = 2
        $ rows = len(blwnfh_ach_list)+1

        # Основные элементы

        frame:
            background blwnfh_gui["img"]["fon"]
            area (0.0, 0.0, 1.0, 1.0)

            # back

            imagebutton:
                action Return()
                idle blwnfh_gui["gallery"]["back"]
                hover blwnfh_gui["gallery"]["back"]
                at blwnfh_menu_pos_atl(0.82, 0.86, 0.85, -6.7)

            # achievements

            frame:
                background "#0005"
                area(128, 38, 1160, 985)

                vbox:
                    align(0.5, 0.0)

                    null height 50

                    text u"Достижения {size=-4}{k=0.0}(%s / %s){/k}{/size}" % (blwnfh_check_achievements(), len(blwnfh_ach_list)):
                        align(0.5, 0.0)
                        style "blwnfh_menu"
                        size 42
                        kerning 2.2

                    null height 25

                    viewport:
                        id "menu_ach_viewport"
                        draggable True
                        mousewheel True
                        scrollbars None

                        grid columns rows:
                            spacing 15

                            for ach in blwnfh_ach_list:
                                if persistent.blwnfh_ach[ach[0]]:
                                    imagebutton:
                                        action NullAction()
                                        idle ("blwnfh_ach_" + ach[0])
                                        hover im.MatrixColor(ImageReference("blwnfh_ach_" + ach[0]), im.matrix.contrast(1.3))
                                        align(0.75, 0.5)
                                    text ach[1]:
                                        style "blwnfh_menu"
                                        size 36
                                        kerning 1.25
                                        align(1.0, 0.5)
                                else:
                                    add im.Alpha(ImageReference("blwnfh_ach_blank"), 0.42):
                                        align(0.75, 0.5)
                                    text u"Достижение не открыто.":
                                        style "blwnfh_menu"
                                        size 36
                                        kerning 1.25
                                        align(1.0, 0.5)

                            null

                            null

                vbar:
                    value YScrollValue("menu_ach_viewport")
                    bottom_bar Frame(blwnfh_gui["img"]["vbar_full"], 0, 0)
                    top_bar Frame(blwnfh_gui["img"]["vbar_null"], 0, 0)
                    thumb "null"
                    at Transform(alpha=0.74, align=(0.02, 0.5), xzoom=1.5, yzoom=0.92)

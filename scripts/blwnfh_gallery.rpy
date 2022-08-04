init python:
    blwnfh_gallery_grid = {
        "bg":(
            #["",False], 
            (["int_warehouse_day", False], ["int_warehouse_night", False], ["int_warehouse_night_lamp_off_light_on", False], ["int_warehouse_night_lamp_on_light_off", False], ["int_warehouse_night_lamp_on_light_on", False], ["int_warehouse_sunset", False],),
            (["ext_clubs_sunset",False], ["ext_music_club_sunset",False], ["ext_warehouse_day",False], ["int_dining_hall_people_sunset",False], ["int_library_sunset",False])
        ),
        "cg":(
            (["d2_dv_sem_scene", False], ["d5_me_mirror_tractor_blwnfh",False], ["disclaimer",False], ["Katya_Avtobus",False],),
        )
    }

init 2:
    screen blwnfh_gallery_menu():

        tag menu
        modal True

        key "game_menu":
            action NullAction()

        key "screenshot":
            action NullAction()

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

            hbox:
                align(0.5, 0.5)
                spacing 40

                for mode in ("bg", "cg"):
                    imagebutton:
                        action Show("blwnfh_gallery", transition=dissolve)
                        idle (blwnfh_gui["gallery"][mode])
                        hover im.MatrixColor(blwnfh_gui["gallery"][mode], im.matrix.contrast(1.1))
                        hovered [SetVariable("blwnfh_gallery_mode", mode), SetVariable("blwnfh_gallery_page", 0)] # пришлось вставить костыль, т. к. множество действий в action по какой-то причине отключает ATL
                        at blwnfh_gallery_mode_atl

    ## Экран меню галереи: ATL

    # Общее

    transform blwnfh_gallery_mode_atl:
        subpixel True
        truecenter
        on hover:
            ease 0.25 zoom 1.25
        on idle:
            ease 0.1 zoom 1.0

    ##    Экран галереи    ##

    $ blwnfh_gallery_mode = None

    $ blwnfh_gallery_page = 0

    screen blwnfh_gallery():

        tag menu
        modal True

        key "game_menu":
            action NullAction()

        key "screenshot":
            action NullAction()

        python:

            def gallery_make_thumb(imgf):
                return im.Scale(imgf, 384, 216)

            columns = 2
            rows = 3
            cells = rows * columns

        # Основные элементы

        frame:
            background blwnfh_gui["img"]["fon"]
            area(0.0, 0.0, 1.0, 1.0)

            # back

            imagebutton:
                action ShowMenu("blwnfh_gallery_menu")
                idle blwnfh_gui["gallery"]["back"]
                hover blwnfh_gui["gallery"]["back"]
                at blwnfh_menu_pos_atl(0.82, 0.86, 0.85, -6.7)

            # gallery

            frame:
                background "#0005"
                area(128, 38, 1080, 985)

                vbox:
                    align(0.5, 0.0)

                    null height 50

                    text u"Галерея":
                        align(0.5, 0.0)
                        #style "blwnfh_service2"
                        size 42
                        kerning 2.2

                    null height 25

                    hbox:

                        null width 84

                        grid columns rows:
                            spacing 37

                            for img in blwnfh_gallery_grid[blwnfh_gallery_mode][blwnfh_gallery_page]:
                                if (blwnfh_gallery_mode, img[0]) in persistent._seen_images.keys():
                                    $ th = gallery_make_thumb(ImageReference((blwnfh_gallery_mode, img[0]))) if not img[1] else gallery_make_thumb(img[1])
                                    imagebutton:
                                        action Show("blwnfh_gallery_item", transition=blwnfh_fade(0.5, color="black"), item=(blwnfh_gallery_mode, img[0]))
                                        idle im.Composite((383, 268), (13, 13), im.Sepia(th), (0, 0), im.Alpha(blwnfh_gui["gallery"]["idle_frame"], 0.4))
                                        hover im.Composite((383, 268), (13, 13), th, (0, 0), blwnfh_gui["gallery"]["hover_frame"])
                                        at blwnfh_gallery_item_atl
                                else:
                                    imagebutton:
                                        action NullAction()
                                        idle blwnfh_gui["gallery"]["lock"]
                                        hover blwnfh_gui["gallery"]["lock"]
                                        at blwnfh_gallery_item_atl

                            for i in range(cells - len(blwnfh_gallery_grid[blwnfh_gallery_mode][blwnfh_gallery_page])):
                                null

                        null width 27

                        # pages

                        viewport:
                            id "menu_gallery_viewport"
                            draggable True
                            mousewheel True
                            scrollbars None

                            vbox:
                                yalign 0.5
                                spacing -22

                                for page in range(len(blwnfh_gallery_grid[blwnfh_gallery_mode])):
                                    if blwnfh_gallery_page != page:
                                        imagebutton:
                                            action SetVariable("blwnfh_gallery_page", page)
                                            idle im.Alpha(im.FactorScale(blwnfh_gui["gallery"]["button_1"], 0.75), 0.7)
                                            hover im.FactorScale(blwnfh_gui["gallery"]["button_1"], 0.75)
                                            align(0.5, 0.5)
                                    else:
                                        add im.FactorScale(blwnfh_gui["gallery"]["button_2"], 0.6):
                                            align(0.5, 0.5)

    ## Экран галереи: ATL

    # Общее

    transform blwnfh_gallery_item_atl:
        subpixel True
        truecenter
        on hover:
            ease 0.25 zoom 0.95
        on idle:
            ease 0.1 zoom 1.0

    ##    Экран просмотра элементов галереи    ##

    screen blwnfh_gallery_item(item):

        tag menu
        modal True

        key "game_menu":
            action NullAction()

        key "screenshot":
            action NullAction()

        imagebutton:
            action Show("blwnfh_gallery", transition=Fade(0.25, 0.0, 0.25, color="#000"))
            idle ImageReference(item)
            hover ImageReference(item)
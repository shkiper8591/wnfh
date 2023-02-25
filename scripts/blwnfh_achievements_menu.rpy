init 2:
    
    screen blwnfh_achievements():

        tag menu
        modal True

        key "game_menu":
            action NullAction()

        key "screenshot":
            action NullAction()

        $ columns = len(characters_banners_idle)
        $ rows = 1

        # Основные элементы
        
        
        
        python:
            def achievements_make_thumb(imgf):
                return im.Scale(imgf, 357, 200)
            
            
            
            
        frame:
            background blwnfh_gui["img"]["fon"]
            area (0.0, 0.0, 1.0, 1.0)
            #text u"Достижения {size=-4}{k=0.0}(%s / %s){/k}{/size}" % (blwnfh_check_achievements(), len(blwnfh_ach_list)):
            text u"Достижения":
                align(0.5, 0.04)
                style "blwnfh_title"
                size 80
                kerning 1
                # back

            imagebutton:
                action ShowMenu("blwnfh_menu")
                idle blwnfh_gui["achievements"]["back"]
                hover blwnfh_gui["achievements"]["back"]
                hover_sound blwnfh_gui["sound"]["plimp"]
                at blwnfh_menu_pos_atl(0.5, 0.1, 0.082, 0.0)

            # achievements
            
            imagebutton:
                action [Hide("blwnfh_achievements", transition=dissolve), Jump("blwnfh_reset")]
                idle blwnfh_gui["banners"]["relation_up"]
                hover blwnfh_gui["banners"]["relation_down"]
            
            frame:
                background "#0005"
                area(-10, 200, 1920, 750)
            
                frame:
                    background "#0000"
                    left_margin 10
                    
                    viewport id "menu_ach_viewport":
                        
                        draggable True
                        mousewheel "horizontal"
                        scrollbars "horizontal"
                        grid columns rows:
                        
                            spacing 15
                            for index,person_baner in enumerate(characters_banners_idle):
                                for name in blwnfh_characters.keys():
                                    if name in person_baner:
                                        $ character = name
                                frame:
                                    background "#0000"
                                    area(0.0, 0.0, 300, 700)
                                    imagebutton:
                                        action ShowMenu("blwnfh_menu")
                                        idle blwnfh_gui["banners"][characters_banners_idle[index]]
                                        hover blwnfh_gui["banners"][characters_banners_hover[index]]
                                        hover_sound blwnfh_gui["sound"]["plimp"]
                                        at blwnfh_ach_char_banners(0.8, 0.5, 0.5)
                                    frame:
                                        background "#0000"
                                        area(0.0, 0.92, 288, 100)
                                        grid 3 1:
                                            xalign 0.5
                                            for i in ["trophy_bronz","trophy_silver","trophy_gold"]:
                                                frame:
                                                    background "#0000"
                                                    area(0.0, 0.0, 90, 50)
                                                    add blwnfh_gui["banners"][i]:
                                                        zoom 0.25
                                                    $ znak = 0
                                                    $ sum_znak_elem = 0
                                                    for element in blwnfh_ach_list:
                                                        if element[5] == i and element[6] == character:  
                                                            if persistent.blwnfh_ach[element[0]]:
                                                                $ znak += 1
                                                            $ sum_znak_elem += 1
                                                    text "{}/{}".format(str(znak),str(sum_znak_elem)):
                                                        align(1.0, 0.8)
                                                        style "blwnfh_title"
                                                        size 30
                                                        kerning 1
    
    #screen blwnfh_achievements_window():
    
    transform blwnfh_ach_char_banners(z, x, y):
        zoom z
        pos(x, y)
        anchor(0.5, 0.55)
        blwnfh_ach_char_banners_hover(z)
    transform blwnfh_ach_char_banners_hover(z):
        on hover:
            ease 0.1 zoom (z - 0.08)
            ease 0.1 zoom (z - 0.02)
        on idle:
            ease 0.1 zoom z

label blwnfh_reset:
    $ blwnfh_reset_achievements()
    jump blwnfh_main_menu
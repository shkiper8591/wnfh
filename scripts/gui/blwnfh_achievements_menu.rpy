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
        frame:
            background im.Blur(blwnfh_gui["main_menu"]["fon"], 1.5)
            area (0.0, 0.0, 1.0, 1.0)
            #text u"Достижения {size=-4}{k=0.0}(%s / %s){/k}{/size}" % (blwnfh_check_achievements(), len(blwnfh_ach_list)):
            text "Достижения":
                align(0.5, 0.055)
                style "blwnfh_title"
                size 80
                kerning 1
                # back

            imagebutton:
                action Return()
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
                                        action ShowMenu("blwnfh_achievements_window", character=character)
                                        idle blwnfh_gui["banners"][characters_banners_idle[index]]
                                        hover blwnfh_gui["banners"][characters_banners_hover[index]]
                                        hover_sound blwnfh_gui["sound"]["plimp"]
                                        at blwnfh_ach_char_banners(0.8, 0.5, 0.5)
                                    frame:
                                        background "#0000"
                                        area(0.0, 620, 288, 80)
                                        grid 2 1:
                                            xalign 0.5
                                            frame:
                                                background "#0000"
                                                area(0.0, 0.0, 120, 70)
                                                add blwnfh_gui["banners"]["trophy_white"]:
                                                    zoom 0.4
                                                    align(0.6, 0.5)
                                            frame:
                                                background "#0000"
                                                area(0.0, 0.0, 120, 70)
                                                $ znak = 0
                                                $ sum_znak_elem = 0
                                                for element in blwnfh_ach_list:
                                                    if element[6] == character:  
                                                        if persistent.blwnfh_ach[element[0]]:
                                                            $ znak += 1
                                                        $ sum_znak_elem += 1
                                                text "{}/{}".format(str(znak),str(sum_znak_elem)):
                                                    align(0.4, 0.5)
                                                    style "blwnfh_title"
                                                    size 60
                                                    kerning 1
    
    screen blwnfh_achievements_window(character):
        tag menu
        modal True

        key "game_menu":
            action NullAction()

        key "screenshot":
            action NullAction()

        $ columns = len(characters_banners_idle)
        $ rows = 1

        # Основные элементы   
        frame:
            background im.Blur(blwnfh_gui["main_menu"]["fon"], 1.5)
            area (0.0, 0.0, 1.0, 1.0)
            text str(blwnfh_characters[character][0]):
                align(0.5, 0.055)
                style "blwnfh_title"
                size 80
                kerning 1
            imagebutton:
                action ShowMenu("blwnfh_achievements")
                idle blwnfh_gui["achievements"]["back"]
                hover blwnfh_gui["achievements"]["back"]
                hover_sound blwnfh_gui["sound"]["plimp"]
                at blwnfh_menu_pos_atl(0.5, 0.1, 0.082, 0.0)
            grid 3 1:
                xalign 0.5
                for i in ["trophy_bronz","trophy_silver","trophy_gold"]:
                    frame:
                        background "#0005"
                        area(0.0, 145, 550, 70)
                        xmargin 30
                        grid 2 1:
                            xalign 0.5
                            frame:
                                background "#0000"
                                area(0.0, 0.0, 200, 60)
                                xmargin 5
                                if i == "trophy_bronz":
                                    text "Обычные":
                                        style "blwnfh_title"
                                        size 60
                                        kerning 1
                                elif i == "trophy_silver":
                                    text "Особые":
                                        style "blwnfh_title"
                                        size 60
                                        kerning 1
                                else:
                                    text "Концовки":
                                        style "blwnfh_title"
                                        size 60
                                        kerning 1
                                
                            frame:
                                background "#0000"
                                area(0.0, 0.0, 200, 60)
                                
                                add blwnfh_gui["banners"][i]:
                                    zoom 0.4
                                    xalign 1.0
                                $ znak = 0
                                $ sum_znak_elem = 0
                                for element in blwnfh_ach_list:
                                    if element[5] == i and element[6] == character:  
                                        if persistent.blwnfh_ach[element[0]]:
                                            $ znak += 1
                                        $ sum_znak_elem += 1
                                text "{}/{}".format(str(znak),str(sum_znak_elem)):
                                    align(0.5, 0.5)
                                    style "blwnfh_title"
                                    size 60
                                    kerning 1

            grid 3 1:
                xalign 0.5
                for trof in ["trophy_bronz","trophy_silver","trophy_gold"]:
                    frame:
                        background "#0005"
                        area(0.0, 0.3, 550, 730)
                        xmargin 30
                        viewport id "menu_ach_list":
                            draggable True
                            mousewheel True
                            scrollbars "vertical"
                            $ temp = 0
                            for element in blwnfh_ach_list:
                                if element[5] == trof and element[6] == character:
                                    $ temp += 1
                            grid 1 temp:
                                for element in blwnfh_ach_list:
                                    if element[5] == trof and element[6] == character:
                                        if persistent.blwnfh_ach[element[0]]:
                                            frame:
                                                default ach_hovered = False
                                                background "#0000"
                                                area(0.0, 0.0, 460, 111)
                                                imagebutton:
                                                    action NullAction()
                                                    idle "blwnfh_ach_menu_" + element[0]
                                                    hover "blwnfh_ach_menu_" + element[0]
                                                    hovered ToggleScreenVariable("ach_hovered")
                                                    unhovered ToggleScreenVariable("ach_hovered")
                                                    hover_sound blwnfh_gui["sound"]["plimp"]
                                                    #zoom 0.98
                                                frame:
                                                    background "#0000"
                                                    area(0.2, 0.0, 340, 99)
                                                    if ach_hovered:
                                                        text element[3]:
                                                            style "blwnfh_title"
                                                            size 35
                                                            kerning 1
                                                            min_width 330
                                                            text_align 1.0
                                                            layout "tex"
                                                    else:
                                                        text element[2]:
                                                            style "blwnfh_title"
                                                            size 35
                                                            kerning 1
                                                            min_width 330
                                                            text_align 1.0
                                                            layout "tex"
                                                
                                        else:
                                            frame:
                                                background "#0000"
                                                area(0.0, 0.0, 500, 100)
                                                add "blwnfh_ach_lock"

label blwnfh_reset:
    $ blwnfh_reset_achievements()
    jump blwnfh_main_menu
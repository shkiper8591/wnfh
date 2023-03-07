init 2:
    
    screen blwnfh_menu():
        modal True tag menu
        
        key "game_menu":
            action NullAction()
        
        key "screenshot":
            action NullAction()
        
        
        
        frame:
            background im.Blur(blwnfh_gui["img"]["fon"], 1.5)
            area(0.0, 0.0, 1.0, 1.0)
        frame:
            background blwnfh_gui["img"]["gradient2"] 
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
            
            blwnfh_menu_button = [
            
                 #Тег кнопки     #Текст кнопки
                ["play"         ,"Играть"        ,[Hide("blwnfh_menu", transition=dissolve), Start("blwnfh_day_1_dream")]  ],
                ["saves"        ,"Загрузить"     ,[Jump("technical_chocolatki")]                                           ],
                ["achievements" ,"Достижения"    ,[ShowMenu("blwnfh_achievements", _transition=dissolve)]                  ],
                ["gallery"      ,"Галерея"       ,[Jump("technical_chocolatki")]                                           ],
                ["sсheme"       ,"Схема"         ,[Jump("technical_chocolatki")]                                           ],
                ["dlc"          ,"Дополнения"    ,[Jump("technical_chocolatki")]                                           ],
                ["settings"     ,"Настройки"     ,[ShowMenu("blwnfh_settings_menu", _transition=dissolve)]                 ],
                ["exit"         ,"Выход"         ,[Return()]                                           ],
            ]

            menu_hovered_action_cat = Play("sound", blwnfh_SFX + "meow" + str(randrange(6)) + ".ogg")
        
        frame:
            background "#0000"
            area(0.0, 0.0, 1.0, 1.0)
            
            frame:
                background "#0000"
                area(0.5, 0.05, 500, 100)
                xanchor 0.5
                text "Мы не отсюда":
                    style "blwnfh_title"
                    min_width 500
                    text_align 0.5
            
            text blwnfh_splash():
                style "blwnfh_splashes"
                at blwnfh_splash_anim(0.65, 0.138, -3.0)
            
            
            frame:
                background "#0000"
                area(0.22, 0.6, 600, 800)
                xanchor 0.5 yanchor 0.5
                $ lines = 0
                for button in blwnfh_menu_button:
                    $ lines += 1
                grid 1 lines:
                    xalign 0.5
                    for button in blwnfh_menu_button:
                        frame:
                            background "#0000"
                            area(0.0, 0.0, 500, 86)
                            ymargin 3
                            textbutton button[1]:
                                action [button[2]]
                                background "#0000"
                                text_style "blwnfh_title"
                                text_size 60
                                text_min_width 474
                                text_text_align 0.0
                                hover_sound blwnfh_gui["sound"]["plimp"]
                                at blwnfh_mm_button_hover_atl()
                        
        #default play_text = False
        #default settings_text = False
        #default galary_text = False
        #default achievements_text = False
        #default scheme_text = False
        #default dlc_text = False
        #default info_text = False
        #default exit_text = False
        
        #if play_text:
        #    text "Играть" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0 
        #elif settings_text:
        #    text "Настройки" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0 
        #elif galary_text:
        #    text "Галерея" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0 
        #elif achievements_text:
        #    text "Достижения" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0 
        #elif scheme_text:
        #    text "Схема" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0
        #elif dlc_text:
        #    text "Дополнения" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0
        #elif info_text:
        #    text "Информация" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0
        #elif exit_text:
        #    text "Выход" style "blwnfh_menu" size 80 kerning 1 pos (blwnfh_posx, blwnfh_posy) text_align 0.0
        #else:
        #    null height 20
            
        #text blwnfh_get_usertime():
        #    align(0.9265625, 0.0844444)
        #    font blwnfh_FONTS + "msjhl.ttc"
        #    size 30
        #
        #text "Мы не отсюда":
        #    align(0.5, 0.06)
        #    style "blwnfh_title"
        #
        #text blwnfh_splash():
        #    font blwnfh_FONTS + "vcr_osd.ttf"
        #    color "#FFFF00"
        #    size 20
        #    at blwnfh_splash_anim(0.65, 0.138, -3.0)
        #
        #imagebutton:
        #    action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_test")]
        #    idle blwnfh_gui["img"]["fish"]
        #    hover blwnfh_gui["img"]["fish"]
        #    hovered menu_hovered_action_cat                       
        #    at blwnfh_menu_pos_atl(1.0, 0.088020833, 0.0944444, 0.0) 
        #
        #imagebutton:
        #    action [Hide("blwnfh_menu", transition=dissolve), Jump("blwnfh_day_1_dream")]
        #    idle blwnfh_gui["img"]["play"]
        #    hover blwnfh_gui["img"]["play"]
        #    hover_sound blwnfh_gui["sound"]["plimp"]
        #    hovered ToggleScreenVariable("play_text")
        #    unhovered ToggleScreenVariable("play_text")
        #    at blwnfh_menu_pos_atl(1.0, 0.233854167, 0.377777778, 0.0)
        #
        #imagebutton:
        #    action ShowMenu("blwnfh_settings_menu", _transition=dissolve)
        #    idle blwnfh_gui["img"]["settings"]
        #    hover blwnfh_gui["img"]["settings"]
        #    hover_sound blwnfh_gui["sound"]["plimp"]
        #    hovered ToggleScreenVariable("settings_text")
        #    unhovered ToggleScreenVariable("settings_text")
        #    at blwnfh_menu_pos_atl(1.0, 0.088020833, 0.284259259, 0.0)
        #
        #imagebutton:
        #    action ShowMenu("blwnfh_gallery_menu")
        #    idle blwnfh_gui["img"]["gallery"]
        #    hover blwnfh_gui["img"]["gallery"]
        #    hover_sound blwnfh_gui["sound"]["plimp"]
        #    hovered ToggleScreenVariable("galary_text")
        #    unhovered ToggleScreenVariable("galary_text")
        #    at blwnfh_menu_pos_atl(1.0, 0.380208333, 0.284259259, 0.0)
        #
        #imagebutton:
        #    action ShowMenu("blwnfh_achievements")
        #    idle blwnfh_gui["img"]["achievements"]
        #    hover blwnfh_gui["img"]["achievements"]
        #    hover_sound blwnfh_gui["sound"]["plimp"]
        #    hovered ToggleScreenVariable("achievements_text")
        #    unhovered ToggleScreenVariable("achievements_text")
        #    at blwnfh_menu_pos_atl(1.0, 0.4875, 0.284259259, 0.0)
        #
        #imagebutton:
        #    action Jump("technical_chocolatki")
        #    idle blwnfh_gui["img"]["scheme"]
        #    hover blwnfh_gui["img"]["scheme"]
        #    hover_sound blwnfh_gui["sound"]["plimp"]
        #    hovered ToggleScreenVariable("scheme_text")
        #    unhovered ToggleScreenVariable("scheme_text")
        #    at blwnfh_menu_pos_atl(1.0, 0.594270833, 0.284259259, 0.0)
        #
        #imagebutton:
        #    action Jump("technical_chocolatki")
        #    idle blwnfh_gui["img"]["dlc"]
        #    hover blwnfh_gui["img"]["dlc"]
        #    hover_sound blwnfh_gui["sound"]["plimp"]
        #    hovered ToggleScreenVariable("dlc_text")
        #    unhovered ToggleScreenVariable("dlc_text")
        #    at blwnfh_menu_pos_atl(1.0, 0.701041667, 0.284259259, 0.0)
        #
        #imagebutton:
        #    action Jump("technical_chocolatki")
        #    idle blwnfh_gui["img"]["info"]
        #    hover blwnfh_gui["img"]["info"]
        #    hover_sound blwnfh_gui["sound"]["plimp"]
        #    hovered ToggleScreenVariable("info_text")
        #    unhovered ToggleScreenVariable("info_text")
        #    at blwnfh_menu_pos_atl(1.0, 0.808333333, 0.284259259, 0.0)
        #
        #imagebutton:
        #    action Return()
        #    idle blwnfh_gui["img"]["exit"]
        #    hover blwnfh_gui["img"]["exit"]
        #    hover_sound blwnfh_gui["sound"]["plimp"]
        #    hovered ToggleScreenVariable("exit_text")
        #    unhovered ToggleScreenVariable("exit_text")
        #    at blwnfh_menu_pos_atl(1.0, 0.915104167, 0.284259259, 0.0)
        #
        #frame:
        #    background "#0005"
        #    area(1201, 466, 655, 550)
        #    
        #    frame:
        #        background "#0000"
        #        left_margin 20
        #        right_margin 30
        #        
        #        
        #        vbox:
        #            align(0.5, 0.0)
        #
        #            null height 20
        #
        #            text u"Новости":
        #                align(0.5, 0.0)
        #                style "blwnfh_menu"
        #
        #            null height 25
        #
        #            viewport:
        #                id "menu_news"
        #                draggable True
        #                mousewheel True
        #                scrollbars None
        #                
        #                text u"{b}alpha 0.1{/b}\n" + "Альфа! Что принесла нам Альфа? НИ#$@ она нам не принесла, только это окошко с новостями, где будут писаться свежие обновления мода. Это создано для тех, кто не следит за группой.":
        #                    style "blwnfh_news"
        #                
        #    vbar:
        #        value YScrollValue("menu_news")
        #        bottom_bar Frame(blwnfh_gui["img"]["vbar_full"], 0, 0)
        #        top_bar Frame(blwnfh_gui["img"]["vbar_null"], 0, 0)
        #        thumb "null"
        #        at Transform(alpha=0.74, align=(0.98, 0.5), xzoom=1.5, yzoom=0.92)
        #    

    
            
    transform blwnfh_mm_button_hover_atl(z = 1.0):
        pos(0.0, 0.5)
        anchor(0.0, 0.5)
        on hover:
            ease 0.15 zoom (z - 0.15)
            ease 0.15 zoom (z - 0.02)
        on idle:
            ease 0.15 zoom z
    



    
    transform blwnfh_splash_anim(x, y, rot):
        block:
            rotate rot
            pos(x, y)
            anchor(0.5, 0.5)
        block:
            ease 0.25 zoom 1.30
            ease 0.20 zoom 1.25
        repeat
    
    
    
    ## Временное говно ##
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


label blwnfh_main:
    scene bg disclaimer with dissolve
    $ renpy.pause(100)
    jump blwnfh_main_menu
label blwnfh_main_menu:
    scene bg fon with dissolve
    $ renpy.pause(2)
    $ init_splash()
    call screen blwnfh_menu with dissolve
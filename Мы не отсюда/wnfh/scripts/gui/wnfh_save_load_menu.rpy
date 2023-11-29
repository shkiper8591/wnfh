init 2:
    screen wnfh_load:
        python:
            style.wnfh_save_load_button = Style(style.button)
            style.wnfh_save_load_button.background = wnfh_gui["save_load"]["load_button_idle"]
            style.wnfh_save_load_button.hover_background = wnfh_gui["save_load"]["load_button_hover"]
            style.wnfh_save_load_button.selected_background = wnfh_gui["save_load"]["load_button_selected"]
            style.wnfh_save_load_button.selected_hover_background = wnfh_gui["save_load"]["load_button_selected"]
            style.wnfh_save_load_button.selected_idle_background = wnfh_gui["save_load"]["load_button_selected"]
            
        modal True tag menu
        window:
            frame: # ======================================================= # Нижняя панель
                background background_color
                area(0.5, 0.0, 1.0, 0.2)
                xanchor 0.5 yanchor 0.0
                imagebutton:
                    idle wnfh_gui["save_load"]["settings_idle"]
                    hover wnfh_gui["save_load"]["settings_hover"]
                    xalign 0.1 yalign 0.08
                    action ShowMenu('wnfh_preferences')

            #hbox xalign 0.9 yalign 0.08:
            #    add get_image("gui/settings/star.png") yalign 0.65
            #    text " " + translation_new["LOAD"] + " " style "settings_link" yalign 0.5 color "#ffffff"
            #    add get_image("gui/settings/star.png") yalign 0.65
            frame: # ======================================================= # Нижняя панель
                background background_color
                area(0.5, 1.0, 1.0, 0.2)
                xanchor 0.5 yanchor 1.0

                imagebutton:
                    idle wnfh_gui["save_load"]["back_idle"]
                    hover wnfh_gui["save_load"]["back_hover"]
                    xalign 0.015 yalign 0.92
                    action Return()
    
                imagebutton:
                    idle wnfh_gui["save_load"]["load_game_idle"]
                    hover wnfh_gui["save_load"]["load_game_hover"]
                    xalign 0.5 yalign 0.92
                    action (FunctionCallback(on_load_callback, selected_slot), FileLoad(selected_slot))
    
                imagebutton:
                    idle wnfh_gui["save_load"]["delete_idle"]
                    hover wnfh_gui["save_load"]["delete_hover"]
                    xalign 0.97 yalign 0.92
                    action FileDelete(selected_slot)
    
            vbox: # ======================================================= # Кнопки слева
                xalign 0.01 yalign 0.5
                grid 1 10:
                    for i in range(0, 10):
                        if i == 0:
                            frame:
                                background background_color
                                area(0.0, 0.0, 50, 85)
                                imagebutton:
                                    idle wnfh_gui["save_load"]["auto_idle"]
                                    hover wnfh_gui["save_load"]["auto_hover"]
                                    action (FilePage("auto"), SetVariable("selected_slot", False))

                        else:
                            frame:
                                background background_color
                                area(0.0, 0.0, 50, 85)
                                imagebutton:
                                    idle wnfh_gui["save_load"][str(i) + "_idle"]
                                    hover wnfh_gui["save_load"][str(i) + "_hover"]
                                    action (FilePage(i), SetVariable("selected_slot", False))

            grid 4 3: # ======================================================= # Сетка сейвов
                xpos 0.04 ypos 0.1
                xmaximum 0.97 ymaximum 0.8
                transpose False
                xfill True
                yfill True
                for i in range(1, 13):
                    fixed:
                        add FileScreenshot(i) xpos 10 ypos 10 zoom 1.27673
                        button:
                            action SetVariable("selected_slot", i)
                            xfill False
                            yfill False
                            style "wnfh_save_load_button"
                            has fixed
                            text ("%s." % i + FileTime(i, format='%d.%m.%y, %H:%M', empty=" " + translation_new["Empty_slot"]) + "\n" + FileSaveName(i))
                            style "file_picker_text"
                            xpos 15 ypos 15

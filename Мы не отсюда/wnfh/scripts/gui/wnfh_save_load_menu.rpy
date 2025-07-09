screen wnfh_load(main_menu = False):

    modal True

    $ debug_frame = {
        "black":  frame_black  if persistent.wnfh_debug_color else frame_transparent,
        "red":    frame_red    if persistent.wnfh_debug_color else frame_transparent,
        "green":  frame_green  if persistent.wnfh_debug_color else frame_transparent,
        "blue":   frame_blue   if persistent.wnfh_debug_color else frame_transparent,
        "purple": frame_purpl  if persistent.wnfh_debug_color else frame_transparent
    }

    default wnfh_button_states = [False for i in range(1)]

    python:
        save_load_elements = [
            ["chapter"  ,"Глава 1"          ],
            ["date"     ,"12 июля 1989г"    ],
            ["filetime" ,"04/05/2025 15:12" ]
        ]
        if main_menu:
            wnfh_preferences_button = [
                ["back", "Назад", [ShowMenu('main_menu'), Hide('load')]]
            ]
        else:
            wnfh_preferences_button = [
                ["back", "Назад", [ShowMenu('game_menu_selector'), Hide('load')]]
            ]

        mm_backgrounds = {
            "night":  wnfh_gui["main_menu"]["mm_bg_night"],
            "sunset": wnfh_gui["main_menu"]["mm_bg_sunset"],
            "day":    wnfh_gui["main_menu"]["mm_bg_day"],
        }

    if main_menu:
        default current_hour = wnfh_get_usertime("hour") # ======================= Главное меню подстраивается под время суток компьютера

        default time_period = (
            "night"  if (current_hour >= 22 or current_hour < 8) else
            "sunset" if (current_hour < 12)                      else
            "day"    if (current_hour < 19)                      else
            "sunset"
        )

        frame:
            background mm_backgrounds[time_period] # ================== Фон в главном меню
            area(0.0, 0.0, 1.0, 1.0)

    add wnfh_gui["tint_elements"]["vignette"]

    for index, button in enumerate(wnfh_preferences_button[0:1]): # ================================================ Кнопка Назад
        frame:
            area(0.1, 0.08, 150, 60)
            xanchor 0.5 yanchor 0.5
            background debug_frame["blue"] 
            vbox: # ================================================ Вбокс кнопок
                pos (0.5, 0.5)
                xanchor 0.5 yanchor 0.5
                spacing 0
                for element in ["back_button_line", "back_button_bg", "back_button_line"]:
                    frame:
                        if persistent.wnfh_debug_color:
                            background wnfh_frames_elements[element][5]
                        else:
                            background frame_transparent 
                        area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])

            frame: # ================================================ Тонировка при наведении
                if wnfh_button_states[index]:
                    add Frame(wnfh_frames_elements["back_button_gradient"][0], left=wnfh_frames_elements["back_button_gradient"][3], top=0):
                        xalign 0.5 yalign 0.5 alpha 0.6
                        matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["back_button_gradient"][4]])
                    add Frame(wnfh_frames_elements["back_button_gradient"][0], left=wnfh_frames_elements["back_button_gradient"][3], top=0):
                        xalign 0.5 yalign 0.5 alpha 0.1
                else:
                    null height 20
                area(0.5, 0.5, wnfh_frames_elements["back_button_bg"][1], wnfh_frames_elements["back_button_bg"][2]) padding(0, 0) xanchor 0.5 yanchor 0.5
                background debug_frame["purple"]

                textbutton button[1]: # ================================================ Текст кнопок
                    style "wnfh_buttons"
                    text_style "wnfh_text_" + renpy.store.wnfh_tymeofday
                    hovered ToggleDict(wnfh_button_states, index)
                    unhovered ToggleDict(wnfh_button_states, index)
                    action button[2]
                    at wnfh_mm_button_hover_atl()

    frame at atl_wnfh_widget_lp_down: # ============================ Заголовок
        area(0.5, 0.08, wnfh_frames_elements["settings_main_title_bg"][1] + 40, wnfh_frames_elements["settings_main_title_bg"][2] + 20)
        xanchor 0.5 yanchor 0.5
        background debug_frame["black"]
        vbox: # ================================================ Фон таблички из трёх кусков
            pos (0.5, 0.5)
            xanchor 0.5 yanchor 0.5
            spacing 0
            for element in ["settings_main_title_line", "settings_main_title_bg", "settings_main_title_line"]:
                frame:
                    if persistent.wnfh_debug_color:
                        background wnfh_frames_elements[element][5]
                    else:
                        background frame_transparent 
                    area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                    add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                        matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]]) 

        text "Загрузить":
            style "wnfh_title_1_" + renpy.store.wnfh_tymeofday

    frame at govno_ebanoe2:
        area(0.5, 0.97, 1.0, 0.8)
        xanchor 0.5 yanchor 1.0
        background debug_frame["red"]
        vbox: # ================================================ Фон таблички из трёх кусков
            pos (0.5, 0.5)
            xanchor 0.5 yanchor 0.5
            spacing 0
            for element in ["save_load_box_line", "save_load_box_bg", "save_load_box_line"]:
                frame at wnfh_frames_elements[element][6]:
                #frame:
                    if persistent.wnfh_debug_color:
                        background wnfh_frames_elements[element][5]
                    else:
                        background frame_transparent
                    area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                    add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                        matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
        frame at wjuh_bg:
            area(0.5, 0.5, 0.98, 1.0)
            xanchor 0.5 yanchor 0.5
            background debug_frame["black"]

            viewport id "load":
                draggable True
                mousewheel True
                scrollbars "vertical"
                vbox:
                    pos (0.5, 0.5)
                    xanchor 0.5 yanchor 0.5
                    spacing 5
                    for element in range(10):
                        frame:
                            area (0.5, 0.0, wnfh_frames_elements["save_load_element_bg"][1] + 40, wnfh_frames_elements["save_load_element_bg"][2] + 20)
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["purple"]
                            vbox: # ================================================ Фон таблички из трёх кусков
                                pos (0.5, 0.5)
                                xanchor 0.5 yanchor 0.5
                                spacing 0
                                for element in ["save_load_element_line", "save_load_element_bg", "save_load_element_line"]:
                                    frame at wnfh_frames_elements[element][6]:
                                    #frame:
                                        if persistent.wnfh_debug_color:
                                            background wnfh_frames_elements[element][5]
                                        else:
                                            background frame_transparent
                                        area (0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
                            
                            
                            vbox:
                                pos (0.03, 0.5)
                                xanchor 0.0 yanchor 0.5
                                spacing 1
                                for element in range(len(save_load_elements)):
                                    frame:
                                        area (0.5, 0.5, 300, wnfh_frames_elements["save_load_element_bg"][2]/3)
                                        xanchor 0.5 yanchor 0.5
                                        background debug_frame["blue"]
                                        text save_load_elements[element][1]:
                                            style "wnfh_text_" + renpy.store.wnfh_tymeofday
                            frame:
                                area (0.97, 0.5, 300, wnfh_frames_elements["save_load_element_bg"][2])
                                xanchor 1.0 yanchor 0.5
                                background debug_frame["red"]
                            vbox:
                                pos (0.5, 0.5)
                                xanchor 0.5 yanchor 0.5
                                spacing 2
                                frame:
                                    area (0.5, 0.5, 1000, wnfh_frames_elements["save_load_element_bg"][2] * 1/3)
                                    xanchor 0.5 yanchor 0.5
                                    background debug_frame["green"]
                                frame:
                                    area (0.5, 1.0, 1000, wnfh_frames_elements["save_load_element_bg"][2] * 2/3)
                                    xanchor 0.5 yanchor 1.0
                                    background debug_frame["purple"]
                



    #python:
    #    style.wnfh_save_load_button = Style(style.button)
    #    style.wnfh_save_load_button.background = wnfh_gui["save_load"]["load_button_idle"]
    #    style.wnfh_save_load_button.hover_background = wnfh_gui["save_load"]["load_button_hover"]
    #    style.wnfh_save_load_button.selected_background = wnfh_gui["save_load"]["load_button_selected"]
    #    style.wnfh_save_load_button.selected_hover_background = wnfh_gui["save_load"]["load_button_selected"]
    #    style.wnfh_save_load_button.selected_idle_background = wnfh_gui["save_load"]["load_button_selected"]
    #    
    #modal True tag menu
    #window:
    #    frame: # ======================================================= # Нижняя панель
    #        if persistent.wnfh_debug_color:
    #            background frame_black
    #        else:
    #            background frame_transparent
    #        area(0.5, 0.0, 1.0, 0.2)
    #        xanchor 0.5 yanchor 0.0
    #        imagebutton:
    #            idle wnfh_gui["save_load"]["settings_idle"]
    #            hover wnfh_gui["save_load"]["settings_hover"]
    #            xalign 0.1 yalign 0.08
    #            action ShowMenu('wnfh_preferences')
    #    #hbox xalign 0.9 yalign 0.08:
    #    #    add get_image("gui/settings/star.png") yalign 0.65
    #    #    text " " + translation_new["LOAD"] + " " style "settings_link" yalign 0.5 color "#ffffff"
    #    #    add get_image("gui/settings/star.png") yalign 0.65
    #    frame: # ======================================================= # Нижняя панель
    #        if persistent.wnfh_debug_color:
    #            background frame_black
    #        else:
    #            background frame_transparent
    #        area(0.5, 1.0, 1.0, 0.2)
    #        xanchor 0.5 yanchor 1.0
    #        imagebutton:
    #            idle wnfh_gui["save_load"]["back_idle"]
    #            hover wnfh_gui["save_load"]["back_hover"]
    #            xalign 0.015 yalign 0.92
    #            action Return()
#
    #        imagebutton:
    #            idle wnfh_gui["save_load"]["load_game_idle"]
    #            hover wnfh_gui["save_load"]["load_game_hover"]
    #            xalign 0.5 yalign 0.92
    #            action (FunctionCallback(on_load_callback, selected_slot), FileLoad(selected_slot))
#
    #        imagebutton:
    #            idle wnfh_gui["save_load"]["delete_idle"]
    #            hover wnfh_gui["save_load"]["delete_hover"]
    #            xalign 0.97 yalign 0.92
    #            action FileDelete(selected_slot)
#
    #    vbox: # ======================================================= # Кнопки слева
    #        xalign 0.01 yalign 0.5
    #        grid 1 10:
    #            for i in range(0, 10):
    #                if i == 0:
    #                    frame:
    #                        if persistent.wnfh_debug_color:
    #                            background frame_black
    #                        else:
    #                            background frame_transparent
    #                        area(0.0, 0.0, 50, 85)
    #                        imagebutton:
    #                            idle wnfh_gui["save_load"]["auto_idle"]
    #                            hover wnfh_gui["save_load"]["auto_hover"]
    #                            action (FilePage("auto"), SetVariable("selected_slot", False))
    #                else:
    #                    frame:
    #                        if persistent.wnfh_debug_color:
    #                            background frame_black
    #                        else:
    #                            background frame_transparent
    #                        area(0.0, 0.0, 50, 85)
    #                        imagebutton:
    #                            idle wnfh_gui["save_load"][str(i) + "_idle"]
    #                            hover wnfh_gui["save_load"][str(i) + "_hover"]
    #                            action (FilePage(i), SetVariable("selected_slot", False))
    #                            
    #    grid 4 3: # ======================================================= # Сетка сейвов
    #        xpos 0.04 ypos 0.1
    #        xmaximum 0.97 ymaximum 0.8
    #        transpose False
    #        xfill True
    #        yfill True
    #        for i in range(1, 13):
    #            fixed:
    #                add FileScreenshot(i) xpos 10 ypos 10 zoom 1.27673
    #                button:
    #                    action SetVariable("selected_slot", i)
    #                    xfill False
    #                    yfill False
    #                    style "wnfh_save_load_button"
    #                    has fixed
    #                    text ("%s." % i + FileTime(i, format='%d.%m.%y, %H:%M', empty=" " + translation_new["Empty_slot"]) + "\n" + FileSaveName(i))
    #                    style "file_picker_text"
    #                    xpos 15 ypos 15
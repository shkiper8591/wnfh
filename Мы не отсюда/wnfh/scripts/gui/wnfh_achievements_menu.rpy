screen wnfh_achievements():
    modal True #tag menu
    
    $ debug_frame = {
        "black":  frame_black  if persistent.wnfh_debug_color else frame_transparent,
        "red":    frame_red    if persistent.wnfh_debug_color else frame_transparent,
        "green":  frame_green  if persistent.wnfh_debug_color else frame_transparent,
        "blue":   frame_blue   if persistent.wnfh_debug_color else frame_transparent,
        "purple": frame_purpl  if persistent.wnfh_debug_color else frame_transparent
    }
    
    default wnfh_button_states = [False for i in range(30)]

    python:
        mm_backgrounds = {
            "night":  wnfh_gui["main_menu"]["mm_bg_night"],
            "sunset": wnfh_gui["main_menu"]["mm_bg_sunset"],
            "day":    wnfh_gui["main_menu"]["mm_bg_day"],
        }

        if main_menu:
            wnfh_achievements_button = [
                ["back", "Назад", [ShowMenu('main_menu'), Hide('wnfh_achievements')]]
            ]
        else:
            wnfh_achievements_button = [
                ["back", "Назад", [ShowMenu('game_menu_selector'), Hide('wnfh_achievements')]]
            ]

        wnfh_bars = {
            "vtumb": [im.MatrixColor(wnfh_frames_elements["achievements_vbar_tumb"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["achievements_vbar_tumb"][4], renpy.store.wnfh_tymeofday)))],
            
            "bar_full": [im.Composite(
                (25, 25),
                (0, 0), im.MatrixColor(wnfh_frames_elements["achievements_vbar_full"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["achievements_vbar_full"][4], renpy.store.wnfh_tymeofday))),
                (0, 0), im.MatrixColor(wnfh_frames_elements["achievements_vbar_null"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["achievements_vbar_null"][4], renpy.store.wnfh_tymeofday))),
                )],
            "bar_null": [im.Composite(
                (25, 25),
                (0, 0), im.MatrixColor(wnfh_frames_elements["achievements_vbar_bg"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["achievements_vbar_bg"][4], renpy.store.wnfh_tymeofday))),
                (0, 0), im.MatrixColor(wnfh_frames_elements["achievements_vbar_null"][0], im.matrix.tint(*converter_hex('wnfh_tint_color', wnfh_frames_elements["achievements_vbar_null"][4], renpy.store.wnfh_tymeofday))),
                )],
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

    for index, button in enumerate(wnfh_achievements_button[0:1]): # ================================================ Кнопка Назад
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

    frame at atl_wnfh_widget_lp_down:
        area(0.5, 0.08, wnfh_frames_elements["settings_main_title_bg"][1] + 40, wnfh_frames_elements["settings_main_title_bg"][2] + 20)
        xanchor 0.5 yanchor 0.5
        background debug_frame["black"]
        vbox: # ================================================ Фон таблички из трёх кусков
            pos (0.5, 0.5)
            xanchor 0.5 yanchor 0.5
            spacing 0
            for element in ["settings_main_title_line", "settings_main_title_bg", "settings_main_title_line"]:
                #frame at wnfh_frames_elements[element][6]:
                frame:
                    if persistent.wnfh_debug_color:
                        background wnfh_frames_elements[element][5]
                    else:
                        background frame_transparent
                    area(0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                    add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                        matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])

        text "Достижения":
            style "wnfh_title_1_" + renpy.store.wnfh_tymeofday
    
    frame at govno_ebanoe2:
        area(0.5, 0.97, 1.0, 0.8)
        xanchor 0.5 yanchor 1.0
        background debug_frame["black"]
        vbox: # ================================================ Фон таблички из трёх кусков
            pos (0.5, 0.5)
            xanchor 0.5 yanchor 0.5
            spacing 0
            for element in ["achievements_box_line", "achievements_box_bg", "achievements_box_line"]:
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
            frame:
                area(0.01, 0.0, 500, 0.98)
                xanchor 0.0 yanchor 0.0
                background debug_frame["red"]
                #text "Список персонажей":
                #    style "wnfh_text_" + renpy.store.wnfh_tymeofday
                viewport id "achievements_char_list":
                    draggable True
                    mousewheel True
                    scrollbars None
                    vbox:
                        pos (0.5, 0.5)
                        xanchor 0.5 yanchor 0.5
                        spacing 0
                        frame: # ================================================ РАЗДЕЛИТЕЛЬ
                            area (0.5, 0.0, wnfh_frames_elements["achievements_char_list_bg_2"][1] + 40, wnfh_frames_elements["achievements_char_list_bg_2"][2] + 20)
                            xanchor 0.5 yanchor 0.0
                            background debug_frame["blue"]
                            vbox: # ================================================ Фон таблички из трёх кусков
                                pos (0.5, 0.5)
                                xanchor 0.5 yanchor 0.5
                                spacing 0
                                for element in ["achievements_char_list_line", "achievements_char_list_bg_2", "achievements_char_list_line"]:
                                    frame at wnfh_frames_elements[element][6]:
                                    #frame:
                                        if persistent.wnfh_debug_color:
                                            background wnfh_frames_elements[element][5]
                                        else:
                                            background frame_transparent
                                        area (0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                                        add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
                            text "Главные персонажи":
                                style "wnfh_text_" + renpy.store.wnfh_tymeofday

                        $ character_order = ["kat", "un", "mi", "dv", "usw", "sl", "mt", "din", "sv", "mz"]
                        $ character_with_img = [character for character in character_order]
                        for element, character in enumerate(character_with_img, start = 21 - len(character_with_img)):
                            frame:
                                area (0.5, 0.0, wnfh_frames_elements["achievements_char_list_bg"][1] + 40, wnfh_frames_elements["achievements_char_list_bg"][2] + 20)
                                xanchor 0.5 yanchor 0.0
                                background debug_frame["blue"]
                                vbox: # ================================================ Фон таблички из трёх кусков
                                    pos (0.5, 0.5)
                                    xanchor 0.5 yanchor 0.5
                                    spacing 0
                                    for element in ["achievements_char_list_line", "achievements_char_list_bg", "achievements_char_list_line"]:
                                        frame at wnfh_frames_elements[element][6]:
                                        #frame:
                                            if persistent.wnfh_debug_color:
                                                background wnfh_frames_elements[element][5]
                                            else:
                                                background frame_transparent
                                            area (0.5, 0.0, wnfh_frames_elements[element][1], wnfh_frames_elements[element][2]) padding(0, 0) xanchor 0.5
                                            add Frame(wnfh_frames_elements[element][0], left=wnfh_frames_elements[element][3], top=0):
                                                matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[element][4]])
                                frame:
                                    area (0.0, 0.5, wnfh_frames_elements["achievements_char_list_bg"][2] * 2, wnfh_frames_elements["achievements_char_list_bg"][2])
                                    xanchor 0.0 yanchor 0.5
                                    background debug_frame["green"]
                                    if renpy.store.wnfh_tymeofday == "day":
                                        add wnfh_gui["avatars"][character]:
                                            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.8
                                            zoom 0.19
                                    else:
                                        add wnfh_gui["avatars"][character]:
                                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][3])
                                            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.8
                                            zoom 0.19
    
                                frame: # ================================================ Тонировка при наведении
                                    if wnfh_button_states[index]:
                                        add Frame(wnfh_frames_elements["achievements_char_list_gradient"][0], left=wnfh_frames_elements["achievements_char_list_gradient"][3], top=0):
                                            xalign 0.5 yalign 0.5 alpha 0.6
                                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["achievements_char_list_gradient"][4]])
                                        add Frame(wnfh_frames_elements["achievements_char_list_gradient"][0], left=wnfh_frames_elements["achievements_char_list_gradient"][3], top=0):
                                            xalign 0.5 yalign 0.5 alpha 0.1
                                    else:
                                        null height 20
                                    area(0.5, 0.5, wnfh_frames_elements["achievements_char_list_bg"][1], wnfh_frames_elements["achievements_char_list_bg"][2]) padding(0, 0) xanchor 0.5 yanchor 0.5
                                    background debug_frame["purple"]
                                    textbutton wnfh_characters[character][0]: # ================================================ Текст кнопок
                                        style "wnfh_buttons"
                                        text_style "wnfh_ach_title_1_" + renpy.store.wnfh_tymeofday
                                        text_text_align 1.0
                                        hovered ToggleDict(wnfh_button_states, character)
                                        unhovered ToggleDict(wnfh_button_states, character)
                                        #action button[2]
                                        at wnfh_mm_button_hover_atl()
                frame:
                    background debug_frame["green"]
                    area(1.0, 0.5, 50, 1.0)
                    xanchor 0.0 yanchor 0.5
                    vbar value YScrollValue("achievements_char_list"):
                        top_bar Frame(wnfh_bars["bar_null"][0], wnfh_frames_elements["achievements_vbar_null"][1], wnfh_frames_elements["achievements_vbar_null"][1])
                        bottom_bar Frame(wnfh_bars["bar_null"][0], wnfh_frames_elements["achievements_vbar_null"][1], wnfh_frames_elements["achievements_vbar_null"][1])
                        thumb wnfh_bars["vtumb"][0]
                        hover_thumb wnfh_bars["vtumb"][0]
                        xmaximum 33 ymaximum 1.0
                        pos (0.5, 0.5)
                        anchor (0.5, 0.5)

            #frame:
            #    area(0.45, 0.0, 400, 0.70)
            #    xanchor 0.5 yanchor 0.0
            #    background debug_frame["blue"]
            #    text "Спрайт":
            #        style "wnfh_text_" + renpy.store.wnfh_tymeofday
            #frame:
            #    area(0.45, 1.0, 600, 200)
            #    xanchor 0.5 yanchor 1.0
            #    background debug_frame["blue"]
            #    text "Ульяна. Человек, которая отчаянно старается сохранить юный задор, совмещая его со взрослыми ответственностями. Удается ей это с переменным успехом. Однако, она не подаёт виду, что новые ответственности нещадно давят на неё.":
            #        style "wnfh_ach_title_2_" + renpy.store.wnfh_tymeofday
            #frame:
            #    area(0.95, 0.0, 600, 600)
            #    xanchor 1.0 yanchor 0.0
            #    background debug_frame["green"]
            #    text "Галерея":
            #        style "wnfh_text_" + renpy.store.wnfh_tymeofday
            #frame:
            #    area(0.95, 1.0, 600, 200)
            #    xanchor 1.0 yanchor 1.0
            #    background debug_frame["purple"]
            #    text "Достижения":
            #        style "wnfh_text_" + renpy.store.wnfh_tymeofday


#label wnfh_reset:
#    $ wnfh_reset_achievements()
#    return
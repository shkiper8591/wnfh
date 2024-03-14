init 2:
    screen wnfh_get_achivement(ach):
        frame at wnfh_get_achievement_atl:
            area(0.0, 0.0, wnfh_frames_elements["ach_box_bg"][1] + 40, wnfh_frames_elements["ach_box_bg"][2] + 20)
            if persistent.wnfh_debug_color:
                background frame_black
            else:
                background frame_transparent
            vbox: # ================================================ Фон  из трёх кусков
                pos (0.5, 0.5)
                xanchor 0.5 yanchor 0.5
                spacing 0        
                for i in ["ach_box_line", "ach_box_bg", "ach_box_line"]:
                    # frame at wnfh_frames_elements[i][6]:
                    frame:
                        if persistent.wnfh_debug_color:
                            background wnfh_frames_elements[i][5]
                        else:
                            background frame_transparent
                        area(0.5, 0.0, wnfh_frames_elements[i][1], wnfh_frames_elements[i][2]) padding(0, 0) xanchor 0.5
                        add Frame(wnfh_frames_elements[i][0], left=wnfh_frames_elements[i][3], top=0):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][wnfh_frames_elements[i][4]])
            frame:
                area(1.0, 0.5, 660, 120)
                xanchor 1.0 yanchor 0.5
                if persistent.wnfh_debug_color:
                    background frame_black
                else:
                    background frame_transparent
                frame: # ==================== Аватарка
                    area(0.12, 0.5, 90, 90)
                    xanchor 0.5 yanchor 0.5
                    if persistent.wnfh_debug_color:
                        background frame_blue
                    else:
                        background frame_transparent
                    add wnfh_ach_list[ach][0]:
                        size(90, 90)
                        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
                    
                frame: # ==================== Кiт
                    area(0.88, 0.5, 70, 70)
                    xanchor 0.5 yanchor 0.5
                    if persistent.wnfh_debug_color:
                        background frame_blue
                    else:
                        background frame_transparent
                    if persistent.timeofday == "day":
                        add (wnfh_gui["banners"]["kit"]):
                            size(70, 70)
                            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
                    else:
                        add (wnfh_gui["banners"]["kit"]):
                            matrixcolor TintMatrix(wnfh_choice_tint_color[persistent.timeofday][3])
                            size(70, 70)
                            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
    
    
    
                frame: # ==================== Трофей
                    area(0.2, 0.91, 40, 40)
                    xanchor 0.0 yanchor 1.0
                    if persistent.wnfh_debug_color:
                        background frame_blue
                    else:
                        background frame_transparent
                    add wnfh_ach_list[ach][3]:
                        size(40, 40)
                        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
                
                frame: # ==================== Заголовок
                    area(0.2, 0.09, 0.6, 50)
                    xanchor 0.0 yanchor 0.0
                    if persistent.wnfh_debug_color:
                        background frame_green
                    else:
                        background frame_transparent
                    text wnfh_ach_list[ach][1]:
                        xalign 0.5 yanchor 0.5 ypos 0.5
                        line_leading 5 line_spacing -10
                        min_width 390
                        text_align 0.0
                        size 20
                        style "wnfh_choice_" + persistent.timeofday

                frame: # ==================== Подпись
                    area(0.27, 0.91, 0.53, 40)
                    xanchor 0.0 yanchor 1.0
                    if persistent.wnfh_debug_color:
                        background frame_green
                    else:
                        background frame_transparent
                    text wnfh_ach_list[ach][2]:
                        xalign 0.5 yanchor 0.5 ypos 0.5
                        line_leading 5 line_spacing -10
                        min_width 340
                        text_align 0.0
                        size 15
                        style "wnfh_choice_" + persistent.timeofday
        timer 10.0 action Hide("wnfh_get_achivement", transition=dissolve)
                



#init 0 python:
#
#    # ДАЛЬШЕ БОГА НЕТ
#    # ДАЛЬШЕ БОГА НЕТ
#    # ДАЛЬШЕ БОГА НЕТ
#    
#    ## Регистрация ачивок ##
#    
#    
#
#    if not persistent.wnfh_ach:
#        persistent.wnfh_ach = dict()
#    
#    ## Создание ачивки ##
#    
#    for ach in wnfh_ach_list:
#        renpy.image("wnfh_ach_" + ach[0], im.Composite(
#        (590, 100),
#        (0  , 0  ), im.MatrixColor(im.Scale(wnfh_gui["banners"]["ach_frame_1_2"], 590, 100), im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 2, persistent.timeofday))),
#        (0  , 0  ), im.MatrixColor(im.Scale(wnfh_gui["banners"]["ach_frame_1_1"], 590, 100), im.matrix.tint(*converter_hex('wnfh_choice_tint_color', 1, persistent.timeofday))),
#        (94 , 12 ), im.Scale(wnfh_BANNERS + ach[1] + ".png"  , 75 , 75 ),
#        (515, 15 ), im.Scale(wnfh_BANNERS + "leaf_" + persistent.timeofday + ".png"  , 45 , 68 ),
#        (184, 50 ), im.Scale(wnfh_BANNERS + ach[4] + ".png"  , 38 , 38 ),
#        ))
#
#        if ach[0] not in persistent.wnfh_ach:
#            persistent.wnfh_ach[ach[0]] = False
#    
#    ##Это для отображения на странице с ачивками
#    import renpy.display.im as im
#
#    for ach in wnfh_ach_list:
#        renpy.image("wnfh_ach_menu_" + ach[0], im.Composite(
#            (455, 99),
#            (12, 12 ), im.Scale(wnfh_BANNERS + ach[1] + ".png"  , 75 , 75 ),
#            (0, 0), im.Scale(wnfh_gui["banners"]["ach_menu_frame"], 455, 99),
#        ))
#    
#    renpy.image("wnfh_ach_lock", im.Scale(wnfh_gui["banners"]["ach_menu_frame_lock"], 455, 99))
#
#    ## Призыв ачивок ##
#    
#    def wnfh_get_achievement(ach):
#        if not persistent.wnfh_ach[ach]:
#            persistent.wnfh_ach[ach] = True
#            renpy.play(wnfh_sfx_list["ps4_ach"], channel="sound")
#            
#            renpy.show("wnfh_ach_" + ach, [wnfh_get_achievement_atl], behind=["ach_title" + str(i), "ach_signature" + str(i)])
#            for index,title in enumerate(wnfh_ach_list, start = 0):
#                if ach in title:
#                    num = index
#            renpy.show("ach_title", [wnfh_get_ach_title_atl], tag="ach_title" + str(i), what=Text(wnfh_ach_list[num][2], style=style.wnfh_ach_title, size=30))
#            renpy.show("ach_signature", [wnfh_get_ach_signature_atl], tag="ach_signature" + str(i), what=Text(wnfh_ach_list[num][3], style=style.wnfh_ach_signature, size=27))
#            
#            renpy.pause(7.5)
#            renpy.hide("wnfh_ach_" + ach)
#            renpy.hide("ach_title")
#            renpy.hide("ach_signature")
#    
#    ## Подсчёт ачивок ##
#    
#    def wnfh_check_achievements():
#        j = 0
#        for i in persistent.wnfh_ach.values():
#            if i:
#                j += 1
#        return j
#    
#    ## Обнуление ачивок ##
#    
#    def wnfh_reset_achievements():
#        for ach in wnfh_ach_list:
#            persistent.wnfh_ach[ach[0]] = False#
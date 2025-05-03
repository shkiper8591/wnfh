init 2:
    screen wnfh_get_achievement(ach):
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
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements[i][4]])
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
                    if renpy.store.wnfh_tymeofday == "day":
                        add (wnfh_gui["banners"]["kit"]):
                            size(70, 70)
                            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
                    else:
                        add (wnfh_gui["banners"]["kit"]):
                            matrixcolor TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][3])
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
                        style "wnfh_ach_title_1_" + renpy.store.wnfh_tymeofday

                frame: # ==================== Подпись
                    area(0.27, 0.91, 0.53, 40)
                    xanchor 0.0 yanchor 1.0
                    if persistent.wnfh_debug_color:
                        background frame_green
                    else:
                        background frame_transparent
                    text wnfh_ach_list[ach][2]:
                        style "wnfh_ach_title_2_" + renpy.store.wnfh_tymeofday

        timer 10.0 action Hide("wnfh_get_achivement", transition=dissolve)
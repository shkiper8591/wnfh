screen wnfh_relation(character = "<ПЕРСОНАЖ>", char_name = None, rel_text = "запомнит это", relation = None):
    python:
        pos_y = 0.5
        
        pos_y_step = 1.0
        
        pos_y_start = pos_y
        pos_y_mid = pos_y
        pos_y_end = pos_y

        # нормальный выбор имени
        name = wnfh_characters[character][0] if char_name is None else char_name
        
        # итоговая строка (БЕЗ color-тегов)
        full_text = name + rel_text
        
        text_len = len(full_text)

        # плавный размер
        base_size = 30
        min_size = 18

        if text_len <= 20:
            font_size = base_size
        else:
            # уменьшаем примерно на 1px за каждые 2 символа сверх 20
            font_size = max(min_size, base_size - (text_len - 20) // 2)


    frame at wnfh_get_achievement_atl:
        pos(0.5, 0.5)
        anchor(0.5, 0.5)
        xysize(wnfh_frames_elements["relation_box_bg"][1], wnfh_frames_elements["relation_box_bg"][2])

        background Frame(
            Transform(
                wnfh_frames_elements["relation_box_bg"][0],
                matrixcolor = TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["relation_box_bg"][4]])
                ),
            left = wnfh_frames_elements["relation_box_bg"][3],
            top = 0
        )

        foreground Frame(
            Transform(
                wnfh_frames_elements["relation_box_double_line"][0],
                matrixcolor = TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][wnfh_frames_elements["relation_box_double_line"][4]])
                ),
            left = wnfh_frames_elements["relation_box_double_line"][3],
            top = 6
        )

        text ("{color=%s}%s{/color}" + " " + rel_text) % (wnfh_characters[character][1], name):
            style "wnfh_text_" + renpy.store.wnfh_tymeofday
            text_align 0.0
            xmaximum 450
            size font_size


        if relation == "up":
            $ pos_y_start = pos_y + pos_y_step
            $ pos_y_end = pos_y - pos_y_step
            add wnfh_gui["banners"]["relation_up"]:
                at wnfh_relation_indicator(pos_y_start, pos_y_mid, pos_y_end)

        elif relation == "down":
            $ pos_y_start = pos_y - pos_y_step
            $ pos_y_end = pos_y + pos_y_step
            add wnfh_gui["banners"]["relation_down"]:
                at wnfh_relation_indicator(pos_y_start, pos_y_mid, pos_y_end)
    
        elif relation == "None":
            timer 1.0

        timer 10.0 action [Hide("wnfh_relation", transition=dissolve)]
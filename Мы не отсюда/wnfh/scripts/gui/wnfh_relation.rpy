screen wnfh_relation(character = "<ПЕРСОНАЖ>"):
    frame at wnfh_get_achievement_atl:
        pos(0.5, 0.5)
        xysize(wnfh_frames_elements["relation_box_bg"][1], wnfh_frames_elements["relation_box_bg"][2])

        text "{color=%s}%s{/color} запомнит это" % (wnfh_characters[character][1], wnfh_characters[character][0]):
            style "wnfh_text_" + renpy.store.wnfh_tymeofday

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
        timer 10.0 action [Hide("wnfh_relation", transition=dissolve)]
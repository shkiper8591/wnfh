init -1 python:
    
    ## Объявляем картинки для баннеров отношений ##
    
    renpy.image("rel_frame", im.MatrixColor(
        im.Scale(wnfh_gui["banners"]["relation_frame"], 600, 100),
        im.matrix.brightness(2)))  
    renpy.image("rel_up", im.Scale(wnfh_gui["banners"]["relation_up"], 41, 59))
    renpy.image("rel_down", im.Scale(wnfh_gui["banners"]["relation_down"], 41, 59))  
    renpy.image("rel_neutral", im.MatrixColor(
        im.Scale(wnfh_gui["banners"]["relation_neutral"], 41, 70),
        im.matrix.brightness(1)))
    
    ## А тут уже хуярим сами баннеры ##
    
    def wnfh_get_relation(character, text, relation):
        renpy.show("rel_frame", [wnfh_get_table_atl])
        
        renpy.show("char_text", [wnfh_get_relation_atl(0.03, 0.14)], tag="char_text" + str(i), what=Text(wnfh_characters[character][0], style=style.wnfh_thought, color=wnfh_characters[character][1], size=30))
        
        if character == "void":
            text_pos_y = 0.15
        else:
            text_pos_y = 0.17
        renpy.show("message_text", [wnfh_get_relation_atl(0.06, text_pos_y)], tag="message_text" + str(i), what=Text(text, style=style.wnfh_thought, size=30))

        # Страшная математика
        pos_x = 0.26
        pos_y = 0.15
        
        pos_y_step = 0.06
        pos_x_step = 0.06
        
        pos_y_start = pos_y
        pos_y_mid = pos_y
        pos_y_end = pos_y
        
        pos_x_start = pos_x
        pos_x_mid = pos_x
        pos_x_end = pos_x

        if relation == "up":
            pos_y_start = pos_y + pos_y_step
            pos_y_end = pos_y - pos_y_step
            renpy.show("rel_up", [wnfh_relation_indicator_atl(pos_x_start, pos_y_start, pos_x_mid, pos_y_mid, pos_x_end, pos_y_end)])
        elif relation == "down":
            pos_y_start = pos_y - pos_y_step
            pos_y_end = pos_y + pos_y_step
            renpy.show("rel_down", [wnfh_relation_indicator_atl(pos_x_start, pos_y_start, pos_x_mid, pos_y_mid, pos_x_end, pos_y_end)])
        elif relation == "neutral":
            pos_x_start = pos_x - pos_x_step
            pos_x_mid = pos_x
            pos_x_end = pos_x + pos_x_step
            renpy.show("rel_neutral", [wnfh_relation_indicator_atl(pos_x_start, pos_y_start, pos_x_mid, pos_y_mid, pos_x_end, pos_y_end)])
        elif relation == "None":
            renpy.pause(1.0)
        renpy.pause(1.5, hard=True)
        renpy.hide("rel_frame")
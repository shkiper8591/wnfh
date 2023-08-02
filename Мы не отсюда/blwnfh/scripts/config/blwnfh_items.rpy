init -1 python:

    wnfh_item_list = (
        "radio"
        "taburetka"
        )
    
    for item in wnfh_item_list:
        renpy.image("wnfh_item_" + item, im.Scale(wnfh_ACHIEVEMENTS + item + ".png", 288, 288))
    
    
    ## Призыв предметов ##
    
    def wnfh_get_item(item, sounded=True):
        if sounded:
            renpy.play(wnfh_sfx_list["pickup_sound"], channel="sound")
        
        for it in wnfh_item_list:
            renpy.image("wnfh_it_" + it[0], im.Scale(wnfh_ACHIEVEMENTS + it[0] + ".png", 600, 125))
        
        renpy.show("item_text", [wnfh_get_item_atl(0.06, text_pos_y)], tag="item_text" + str(i), what=Text(text, style=style.wnfh_thought, size=30))

        
        renpy.show("point", [wnfh_get_table_atl])
        
        renpy.show("item_text", [wnfh_get_item_atl(0.06, text_pos_y)], tag="item_text" + str(i), what=Text(text, style=style.wnfh_thought, size=30))

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
        renpy.hide("point")
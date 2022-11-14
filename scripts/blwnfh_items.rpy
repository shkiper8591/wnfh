init -1 python:

    blwnfh_item_list = (
        "radio"
        "taburetka"
        )
    
    for item in blwnfh_item_list:
        renpy.image("blwnfh_item_" + item, im.Scale(blwnfh_ACHIEVEMENTS + item + ".png", 288, 288))
    
    
    ## Призыв предметов ##
    
    def blwnfh_get_item(item, sounded=True):
        if sounded:
            renpy.play(blwnfh_sfx_list["pickup_sound"], channel="sound")
        
        for it in blwnfh_item_list:
            renpy.image("blwnfh_it_" + it[0], im.Scale(blwnfh_ACHIEVEMENTS + it[0] + ".png", 600, 125))
        
        renpy.show("item_text", [blwnfh_get_item_atl(0.06, text_pos_y)], tag="item_text" + str(i), what=Text(text, style=style.blwnfh_thought, size=30))

        
        renpy.show("point", [blwnfh_get_table_atl])
        
        renpy.show("item_text", [blwnfh_get_item_atl(0.06, text_pos_y)], tag="item_text" + str(i), what=Text(text, style=style.blwnfh_thought, size=30))

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
            renpy.show("rel_up", [blwnfh_relation_indicator_atl(pos_x_start, pos_y_start, pos_x_mid, pos_y_mid, pos_x_end, pos_y_end)])
        elif relation == "down":
            pos_y_start = pos_y - pos_y_step
            pos_y_end = pos_y + pos_y_step
            renpy.show("rel_down", [blwnfh_relation_indicator_atl(pos_x_start, pos_y_start, pos_x_mid, pos_y_mid, pos_x_end, pos_y_end)])
        elif relation == "neutral":
            pos_x_start = pos_x - pos_x_step
            pos_x_mid = pos_x
            pos_x_end = pos_x + pos_x_step
            renpy.show("rel_neutral", [blwnfh_relation_indicator_atl(pos_x_start, pos_y_start, pos_x_mid, pos_y_mid, pos_x_end, pos_y_end)])
        elif relation == "None":
            renpy.pause(1.0)
        renpy.pause(1.5, hard=True)
        renpy.hide("point")

init -2:
    transform blwnfh_get_item_atl(pos_x, pos_y):
        xalign (0.0)
        pos(pos_x, 0.18)
        anchor(0.0, 0.5)
        alpha 0.0
        pause 1.0
        ease 1.0 pos(pos_x, pos_y) alpha 1.0
        pause 3.0
        ease 1.0 pos(-0.4, pos_y) alpha 0.0

    transform blwnfh_item_icon_atl(pos_x_start, pos_y_start, pos_x_mid, pos_y_mid, pos_x_end, pos_y_end):
        pos(pos_x_start, pos_y_start)
        anchor(0.0, 0.5)
        alpha 0.0
        pause 2.5
        ease 2.5 pos(pos_x_mid, pos_y_mid) alpha 1.0
        ease 1.0 pos(pos_x_end, pos_y_end) alpha 0.0
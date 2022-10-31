init -1 python:

    blwnfh_item_list = (
        "knife",
        "paint",
        "tape",
        "key",
        "food",
        "powder",
        "accumulator",
        "comb",
        "pills",
        "apple",
        "note",
        "shark_tooth",
        "matchbox",
        "love_letter",
        "tabs",
        "bandana",
        "gram",
        "birth_certificate",
        "roses",
        "healing_potion",
        )
    
    for item in blwnfh_item_list:
        renpy.image("blwnfh_item_" + item, im.Scale(blwnfh_IMAGES + "gui/items/" + item + ".png", 450, 360))
    
    
    ## Призыв предметов ##
    
    def blwnfh_get_item(item, sounded=True):
        if sounded:
            renpy.play(blwnfh_sfx_list["get_item"], channel="sound")
        renpy.show("blwnfh_item_%s" % item, [blwnfh_get_item_atl])
        renpy.pause(5.0)
        renpy.hide("blwnfh_item_%s" % item)
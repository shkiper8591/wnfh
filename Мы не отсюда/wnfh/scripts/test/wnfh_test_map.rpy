label wnfh_map_test:
    $ wnfh_init_map_zones()
    "хуй"
    $ wnfh_set_zone("house_1", "house1_label")
    $ wnfh_set_zone("house_5", "house5_label")
    #$ wnfh_set_chibi("house_5", "chibi_hero.png", center=(0.52, 0.47))
    $ choice = wnfh_show_map()

    return
label house1_label:
    "Дом 1"
    return
label house5_label:
    "Дом 5"
    return
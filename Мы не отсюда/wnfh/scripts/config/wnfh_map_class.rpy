init -2 python:
    class wnfh_MapZone:
        def __init__(self, name, mask_path):
            self.name = name
            self.label = None
            self.available = False
            self.visits = 0
            self.mask = mask_path   # например: "map_mask_house_5.png"
            self.chibi = None
            self.center = (0.5, 0.5)

    wnfh_zones = {}
    wnfh_global_map_result = None

    def add_to_db(zone):
        data_set = wnfh_find_Operand()

    def _wnfh_click_zone(name):
        global wnfh_global_map_result
        zone = wnfh_zones[name]
        zone.visits += 1
        wnfh_global_map_result = name

    def wnfh_init_map_zones():
        wnfh_zones.clear()
        for i in range(1, 62):
            key = "house_%d" % i
            wnfh_zones[key] = wnfh_MapZone(key, wnfh_MASKS + "map_mask_house_%d.png" % i)

    def wnfh_set_zone(name, label):
        z = wnfh_zones[name]
        z.available = True
        z.label = label

    def wnfh_reset_zone(name):
        z = wnfh_zones[name]
        z.available = False
        z.label = None

    def wnfh_set_chibi(name, icon, center=None):
        z = wnfh_zones[name]
        z.chibi = icon
        if center:
            z.center = center

    def wnfh_reset_chibi(name):
        wnfh_zones[name].chibi = None

    def wnfh_show_map():
        renpy.call_screen("wnfh_map_screen")
        return wnfh_global_map_result

    wnfh_init_map_zones()
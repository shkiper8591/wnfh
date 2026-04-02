screen wnfh_map_screen():
    tag map
    modal True

    add wnfh_gui["map"]["map"]
    
    for name, zone in wnfh_zones.items():
        
        if zone.available and zone.label:
            imagebutton:
                idle  AlphaMask(wnfh_gui["map"]["map_available"], zone.mask)
                hover AlphaMask(wnfh_gui["map"]["map_selected"], zone.mask)
                # Динамическая строка с [zone.mask] создаёт Displayable из "map_mask_house_N.png" :contentReference[oaicite:0]{index=0}
                focus_mask zone.mask
                xpos 0 ypos 0
                action [
                    Function(_wnfh_click_zone, name),
                    Hide("wnfh_map_screen"),
                    Jump(zone.label),
                ]

    # 3) Чиби‑иконки над регионами
    for name, zone in wnfh_zones.items():
        if zone.chibi:
            add zone.chibi:
                xalign zone.center[0]
                yalign zone.center[1]
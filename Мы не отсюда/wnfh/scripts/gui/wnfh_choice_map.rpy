screen wnfh_map_screen(click_callback=None):
    python:
        map_action = click_callback or _on_map_click

    add wnfh_gui["map"]["map"]
    imagebutton:
        xysize (1920, 1080)
        xpos 0 ypos 0
        idle  AlphaMask(wnfh_gui["map"]["map_available"], wnfh_gui["map"]["map_mask"])
        hover AlphaMask(wnfh_gui["map"]["map_selected"],  wnfh_gui["map"]["map_mask"])
        focus_mask wnfh_gui["map"]["map_mask"]
        action Function(map_action)
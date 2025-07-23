init python:
    import renpy.exports as renpy
    from renpy.display.im import AlphaMask

    def _on_map_click():
        x, y = renpy.get_mouse_pos()
        mask_img = wnfh_gui["map"]["map_mask"]
        mask_surf = renpy.loader.load(mask_img).get_surface()
        try:
            pixel = mask_surf.get_at((x, y))
        except Exception:
            return
        if pixel.a > 0:
            renpy.jump("map_clicked")
        return
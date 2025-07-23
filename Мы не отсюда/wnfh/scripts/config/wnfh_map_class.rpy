init python:
    import json, renpy
    from renpy.display.im import AlphaMask

    # Загружаем JSON‑индекс fullsize RGBA масок
    try:
        idx_fn = renpy.loader.transfn("masks/map_mask_index.json")
        with open(idx_fn, encoding="utf-8") as f:
            mask_index = json.load(f)
    except Exception:
        mask_index = {}

    def _on_house_click(house_id):
        # Переход при клике на дом
        renpy.jump("you_clicked_" + house_id)
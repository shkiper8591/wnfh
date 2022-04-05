init -4 python:
    blwnfh_IMAGES = "mods/blwnfh/images/"
    blwnfh_SPRITES_CLOSE = blwnfh_IMAGES + "sprites/close/"
    blwnfh_SPRITES_NORMAL = blwnfh_IMAGES + "sprites/normal/"
    blwnfh_SPRITES_FAR = blwnfh_IMAGES + "sprites/far/"

init -2 python:
    blwnfh_far_size = (675, 1080)

    blwnfh_add_character("kat", {
        "name": "Катя",
        "color": "#ff97bb",
        "variants": [
            ("normal pioneer far", blwnfh_SPRITES_FAR, blwnfh_far_size, ["kat_1_body.png", "kat_1_pioneer.png", "kat_1_normal.png"])
        ]
    })
    blwnfh_clone_character_as_unknown("kat", "Девушка")

    
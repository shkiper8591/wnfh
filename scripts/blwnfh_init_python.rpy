## Инициалзация BG и CG ##
init -3 python:
    blwnfh_characters = {}

    def blwnfh_add_character(key, params):
        global blwnfh_characters
        blwnfh_characters[key] = params

    def blwnfh_clone_character_as_unknown(key, name):
        global blwnfh_characters
        blwnfh_characters["u" + key] = {
            "name": name,
            "color": blwnfh_characters[key]["color"]
        }

    def blwnfh_parse_folder(key):
        r = {}
        for path in renpy.list_files():
            if path.startswith(blwnfh_IMAGES + key + "/"):
                r[path.split("/")[-1].split(".")[0]] = path
        return r

    def blwnfh_make_images(key, r):
        for name, path in r.items():
            renpy.image(key + " " + name, path)

    blwnfh_backgrounds = blwnfh_parse_folder("bg")
    blwnfh_graphics = blwnfh_parse_folder("cg")

    blwnfh_make_images("bg", blwnfh_backgrounds)
    blwnfh_make_images("cg", blwnfh_graphics)

## Эта страшная хуйня, это оптимизация инициализации спрайтов. ##
## Не пытайтесь понять как оно работает, я сам в ахуе от написанного. ##
## Просто знайте, что в файле config эта штука позволяет без лишней анальной болит прописать спрайты. ##
init -1 python:
    blwnfh_DEFAULT_CHARACTER_ARGS = { "ctc": "ctc_animation", "ctc_position": "fixed", "what_color": "#e2c778", "drop_shadow": [(2, 2)], "drop_shadow_color": "#000", "what_drop_shadow": [(2, 2)], "what_drop_shadow_color": "#000" }

    for keyword, params in blwnfh_characters.items():
        globals()[keyword] = Character(params["name"], color=params["color"], **blwnfh_DEFAULT_CHARACTER_ARGS)
        if "variants" in params:
            for variant in params["variants"]:
                variant_name, path, size, sprites = variant
                composite_args = []
                for sprite in sprites:
                    composite_args.extend([(0, 0), path + "/" + keyword + "/" + sprite])
                composite = im.Composite(size, *composite_args)
                renpy.image(keyword + " " + variant_name, ConditionSwitch(
                    "persistent.sprite_time=='sunset'", im.MatrixColor(composite, im.matrix.tint(0.94, 0.82, 1.0)),
                    "persistent.sprite_time=='night'", im.MatrixColor(composite, im.matrix.tint(0.63, 0.78, 0.82)),
                    True, composite
                ))
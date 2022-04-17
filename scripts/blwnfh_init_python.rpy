## Инициалзация BG и CG ##
init -3 python:
    blwnfh_characters = {}

    def blwnfh_add_character(key, name, unknown_name, color):
        # Обычный
        blwnfh_add_character_by_params(key, {
            "name": name,
            "color": color,
            "kind": None
        })

        # Незнакомый
        blwnfh_add_character_by_params("u" + key, {
            "name": unknown_name,
            "color": color,
            "kind": None
        })

        # Обычный NVL
        blwnfh_add_character_by_params("nvl" + key, {
            "name": name + ": ",
            "color": color,
            "kind": nvl
        })

        # Незнакомый NVL
        blwnfh_add_character_by_params("nvl" + "u" + key, {
            "name": unknown_name + ": ",
            "color": color,
            "kind": nvl
        })

    def blwnfh_add_character_by_params(key, params):
        global blwnfh_characters
        blwnfh_characters[key] = params


    def blwnfh_parse_folder(key):
        r = {}
        for path in renpy.list_files():
            if path.startswith(blwnfh_IMAGES + key + "/"):
                r[path.split("/")[-1].split(".")[0]] = path
        return r


    def blwnfh_make_images(key, r):
        for name, path in r.items():
            renpy.image(key + " " + name, path)


    def blwnfh_add_variant(keyword, variant):
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


    def blwnfh_add_variants(keyword, variants):
        for variant in variants:
            blwnfh_add_variant(keyword, variant)


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
        globals()[keyword] = Character(params["name"], kind=params["kind"], color=params["color"], **blwnfh_DEFAULT_CHARACTER_ARGS)
        if "variants" in params:
            for variant in params["variants"]:
                blwnfh_add_variant(keyword, variant);

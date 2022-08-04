## Инициалзация BG и CG ##
init -3 python:

    def blwnfh_parse_folder(key):
        r = []
        for path in renpy.list_files():
            if path.startswith(blwnfh_IMAGES + key + "/"):
                r.append((path.split("/")[-1].split(".")[0], path))
        return r

    def blwnfh_make_images(key, r):
        for i in r:
            name, path = i
            renpy.image(key + " " + name, path)


    def blwnfh_add_variant(variant):
        keyword, files, size = variant
        composite_args = []
        for file in files:
            composite_args.extend([(0, 0), file])
        composite = im.Composite(size, *composite_args)
        renpy.image(keyword, ConditionSwitch(
            "persistent.sprite_time=='sunset'", im.MatrixColor(composite, im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(composite, im.matrix.tint(0.63, 0.78, 0.82)),
            True, composite
        ))


    # Внимание ночные ужасы

    from collections import defaultdict

    blwnfh_far_size = (675, 1080)
    blwnfh_normal_size = (900, 1080)
    blwnfh_close_size = (1125, 1080)

    blwnfh_sprites_variants = []

    def blwnfh_order_dict(dictionary):
        result = {}
        for k, v in sorted(dictionary.items()):
            if isinstance(v, dict):
                result[k] = blwnfh_order_dict(v)
            else:
                result[k] = v
        return result


    def blwnfh_nested_dict():
        return defaultdict(blwnfh_nested_dict)


    def blwnfh_default_to_regular(d):
        if isinstance(d, defaultdict):
            d = {k: blwnfh_default_to_regular(v) for k, v in d.items()}
        return d


    def blwnfh_get_path_dict(paths):
        new_path_dict = blwnfh_nested_dict()
        for path in paths:
            parts = path.split('/')
            if parts:
                marcher = new_path_dict
                for key in parts[:-1]:
                    marcher = marcher[key]
                marcher[parts[-1]] = path
        return blwnfh_default_to_regular(new_path_dict)


    def blwnfh_get_name(file):
        return file.split('_')[2].split('.')[0]


    def blwnfh_make_variant(root, id, name, distance, body, clothes, accessory, emotion):
        global blwnfh_sprites_variants, blwnfh_far_size, blwnfh_normal_size, blwnfh_close_size
        files = [body[1], clothes[1]]
        if accessory is not None:
            files.append(accessory[1])
        files.append(emotion[1])

        name = [name, blwnfh_get_name(emotion[0])]
        if accessory is not None:
            name.append(blwnfh_get_name(accessory[0]))
        name.append(blwnfh_get_name(clothes[0]))

        if distance != 'normal':
            name.append(distance)

        size = (0, 0)

        if distance == 'close':
            size = blwnfh_close_size

        if distance == 'far':
            size = blwnfh_far_size

        if distance == 'normal':
            size = blwnfh_normal_size

        variant_name = ' '.join(name)

        blwnfh_sprites_variants.append((variant_name, files, size))


    def blwnfh_parse_emotions(root, id, name, distance, body, clothes, accessory):
        emotions = root['emotions']
        for emotion in emotions.items():
            e_filename, e_path = emotion
            _, e_id, _ = e_filename.split('_')
            if e_id == id:
                blwnfh_make_variant(root, id, name, distance, body, clothes, accessory, emotion)


    def blwnfh_parse_clothes_type(root, id, name, distance, body, clothes_type):
        t_name, t_data = clothes_type  # casual
        t_root = root['clothes'][t_name]
        for c in t_data.items():
            c_name, c_data = c  # 1 2 3 accessory
            if type(c_data) is str:
                _, c_id, _ = c_data.split('_')
                if id == c_id:  # kat_1_body.png == kat_1_casual
                    if 'accessory' in t_root:
                        for accessory in t_root['accessory'].items():
                            _, a_id, _ = accessory[0].split('_')
                            if id == a_id:
                                blwnfh_parse_emotions(root, id, name, distance, body, c, accessory)
                    blwnfh_parse_emotions(root, id, name, distance, body, c, None)


    def blwnfh_parse_clothes(root, id, name, distance, body):
        clothes = root['clothes']
        for clothes_type in clothes.items():
            blwnfh_parse_clothes_type(root, id, name, distance, body, clothes_type)


    def blwnfh_parse_body(root, name, distance, body):
        filename, path = body
        _, id, _ = filename.split('_')
        blwnfh_parse_clothes(root, id, name, distance, body)


    def blwnfh_parse_distance(name, data):
        distance, root = data

        bodies = []
        for path in root.items():
            key, value = path
            if type(value) is str:
                bodies.append(path)

        for body in bodies:
            blwnfh_parse_body(root, name, distance, body)


    def blwnfh_parse_character(data):
        name, distances = data

        for distance in distances.items():
            blwnfh_parse_distance(name, distance)


    def blwnfh_parse_characters(root):
        for node in root.items():
            blwnfh_parse_character(node)

    
    blwnfh_raw_paths = []

    for i in blwnfh_parse_folder('sprites'):
        blwnfh_raw_paths.append(i[1])

    blwnfh_sprites_root = blwnfh_get_path_dict(blwnfh_raw_paths)['mods']['blwnfh']['images']['sprites']
    blwnfh_sprites_root = blwnfh_order_dict(blwnfh_sprites_root)

    blwnfh_parse_characters(blwnfh_sprites_root)

    for variant in blwnfh_sprites_variants:
        blwnfh_add_variant(variant)

    blwnfh_backgrounds = blwnfh_parse_folder("bg")
    blwnfh_graphics = blwnfh_parse_folder("cg")

    blwnfh_make_images("bg", blwnfh_backgrounds)
    blwnfh_make_images("cg", blwnfh_graphics)
    
init python:
    #Функция для отображения времени в меню
    from random import choice

    def blwnfh_get_usertime():
        from time import strftime, localtime
        time = strftime("%H:%M:%S", localtime())
        hour, min, sec = time.split(":")
        hour = int(hour)
        return str(hour) + ":" + str(min)

init 1:

    # Шрифты
    $ style.blwnfh_service = Style(style.default)
    $ style.blwnfh_service.font = blwnfh_FONTS + "msjhl.ttc"
    $ style.blwnfh_service.color = "#FFF"
    $ style.blwnfh_service.drop_shadow = (2, 2)
    $ style.blwnfh_service.drop_shadow_color = "#222"
    $ style.blwnfh_service.text_align = 0.5
    $ style.blwnfh_service.yalign = 0.5
    $ style.blwnfh_service.kerning = 17.0
    $ renpy.image("blwnfh_menu", ParameterizedText(style="blwnfh_menu", size=64))


    $ style.blwnfh_thought = Style(style.default)
    $ style.blwnfh_thought.drop_shadow = (2, 2)
    $ style.blwnfh_thought.drop_shadow_color = "#000"
    $ style.blwnfh_thought.text_align = 0.5
    $ renpy.image("blwnfh_thought", ParameterizedText(style="blwnfh_thought", size=40))
    
    # Всплывающие мысли спизженныe из БКРР, да кого я обманываю, тут половина кода спизжено из кефира и 7дл и ещё десятка других модов
    
    python:

        def blwnfh_thoughts_show(*args):
            colors = {
                "day":"#E2C778",
                "sunset":"#DCD168",
                "night":"#3CCFA2",
                "prologue":"#98D8DA"
            }
            pt = 0.1
            t = 4.0
            sy = ey = 1.0 / len(args)
            for i, text in enumerate(args):
                if not i % 2:
                    sx = -0.1
                    ex = random.uniform(0.3, 0.4)
                    rot = -27.5
                else:
                    sx = 1.1
                    ex = random.uniform(0.7, 0.6)
                    rot = 27.5
                sy += 0.1
                ey += 0.1
                renpy.show("thought_text", [blwnfh_thoughts_atl(t, pt, sx, sy, ex, ey, rot)], tag="thought_text" + str(i), what=Text(text, style=style.blwnfh_thought, color=colors[persistent.timeofday], size=40))
                pt += 0.22
            renpy.pause()
            for i in range(len(args)):
                renpy.hide("thought_text" + str(i))
                renpy.with_statement(Dissolve(0.15))

    transform blwnfh_thoughts_atl(t, pt, sx, sy, ex, ey, rot):
        pos(sx, sy)
        anchor(0.5, 0.5)
        rotate rot
        alpha 0.0
        pause pt
        ease t pos(ex, ey) rotate renpy.random.randint(-4, 4) alpha 1.0
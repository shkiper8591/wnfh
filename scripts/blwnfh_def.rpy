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
    def blwnfh_form_files_list(path):
        return {i[len(path):i.rfind(".")]:i for i in renpy.list_files() if i.startswith(path)}
    
    blwnfh_gui = dict()
    
    blwnfh_gui["img"] = {img:(blwnfh_MAIN_MENU + img + ".png") for img in ["fon", "bg", "vbar_full", "vbar_null"]}
    
    blwnfh_characters = {
        # персонажи оригинала
        "narrator":[None, None],     #Рассказчик
        "th":[None, None],           #Мысля Семёна
        "me":[u"Семён", "#E1DD7D"],
        "mi":[u"Мику", "#00DEFF"],
        "us":[u"Ульяна", "#FF3200"],
        "dv":[u"Алиса", "#FFAA00"],
        "mt":[u"Ольга Дмитриевна", "#00EA32"],
        "mz":[u"Женя", "#4A86FF"],
        "sh":[u"Шурик", "#FFF226"],
        "sl":[u"Славя", "#FFD200"],
        "el":[u"Электроник", "#FFFF00"],
        "un":[u"Лена", "#B956FF"],
        "cs":[u"Виола", "#A5A5FF"],
        "pi":[u"Пионер", "#E60000"],
        "uv":[u"Юля", "#4EFF00"],
        "voice":[u"... ", "#E1DD7D"],
        # новые персонажи
        "kat":[u"Катя", "#FF97BB"],
        "ukat":[u"Девушка", "#FF97BB"],
        "gp":[u"Галина Петровна", "#CECECE"],
        "zg":[u"Зинаида Геннадьевна", "#D199FF"],
        "sd":[u"Сергей Дмитриевич", "#878787"],

    }

    #renpy.image("bkrr_radio_icon", im.FactorScale(BKRR_IMAGES + "ui/dialogue_box/radio_icon.png", 0.051))
    #renpy.image("bkrr_speaker_icon", im.FactorScale(BKRR_IMAGES + "ui/dialogue_box/speaker_icon.png", 0.051))

    def blwnfh_chars_define(kind=adv):
        gl = globals()
        if kind == nvl:
            who_suffix = ":"
            ctc = "ctc_animation_nvl"
        else:
            who_suffix = ""
            ctc = "ctc_animation"
        what_color = "#FFDD7D"
        drop_shadow = (2, 2)
        for i, j in blwnfh_characters.items():
            if i == "narrator":
                gl[i] = Character(None, kind=kind, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
            elif i == "th":
                gl[i] = Character(None, kind=kind, what_color=what_color, what_drop_shadow=drop_shadow, what_prefix="~ ", what_suffix=" ~", ctc=ctc, ctc_position="fixed")
            else:
                gl[i] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
                gl[i+"_r"] = Character(j[0], kind=kind, who_color=what_color, who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
                gl[i+"_v"] = Character(u"Голос", kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
                #gl[i+"_radio"] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_prefix=" {image=blwnfh_radio_icon} ", what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
                #gl[i+"_speaker"] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_prefix=" {image=blwnfh_speaker_icon} ", what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")

    # Создание / объявление парных персонажей

    def blwnfh_double_char_define(first, second, time_of_day):
        colors = {
            "day":"#80A055",
            "sunset":"#CDAF69",
            "night":"#36B198"
        }
        gl = globals()
        what_color = "#FFDD7D"
        drop_shadow = (2, 2)
        character = "{color=%s}%s{/color} {color=%s}|{/color} {color=%s}%s{/color}" % (blwnfh_characters[first][1], blwnfh_characters[first][0], colors[time_of_day], blwnfh_characters[second][1], blwnfh_characters[second][0])
        gl[first + "_" + second + "_" + time_of_day[0]] = Character(character, kind=adv, what_color=what_color, what_drop_shadow=drop_shadow, ctc="ctc_animation", ctc_position="fixed")

    for i in [("kat", "mi", "day"), ("kat", "un", "day")]:
        blwnfh_double_char_define(i[0], i[1], i[2])\
    
    def blwnfh_set_mode(mode=adv):
        nvl_clear()
        blwnfh_chars_define(kind=mode)

    def blwnfh_set_name(name, value):
        blwnfh_characters[name][0] = value
        blwnfh_chars_define()

    def blwnfh_set_char_color(name, value):
        blwnfh_characters[name][1] = value
        blwnfh_chars_define()    
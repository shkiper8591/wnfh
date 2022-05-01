## Инициалзация BG и CG ##
init -3 python:

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
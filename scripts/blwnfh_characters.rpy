init -265 python:
    # Нормальные троеточия
    wp = "{w=-.25}.{w=-.25}.{w=-.25}."

init -1 python:
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
        "el":[u"Сергей", "#FFFF00"],
        "un":[u"Лена", "#B956FF"],
        "cs":[u"Виола", "#A5A5FF"],
        "pi":[u"Пионер", "#E60000"],
        "uv":[u"Юля", "#4EFF00"],
        "voice":[u"... ", "#E1DD7D"],
        # новые персонажи
        "kat":[u"Катя", "#FF97BB"],
        "gp":[u"Галина Петровна", "#CECECE"],
        "zg":[u"Зинаида Геннадьевна", "#D199FF"],
        "sd":[u"Сергей Дмитриевич", "#878787"],
        "void":[u" ", "#000000"]
    }
    
    #renpy.image("blwnfh_radio_icon", im.FactorScale(BKRR_IMAGES + "ui/dialogue_box/radio_icon.png", 0.051))
    #renpy.image("blwnfh_speaker_icon", im.FactorScale(BKRR_IMAGES + "ui/dialogue_box/speaker_icon.png", 0.051))

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

    ## Спизженные из БКРР парные персонажи и модернизированные для работы с NVL
    def blwnfh_double_char_define(first, second, time_of_day, kind=adv):
        colors = {
            "day":"#80A055",
            "sunset":"#CDAF69",
            "night":"#36B198"
        }
        gl = globals()
        if kind == nvl:
            who_suffix = ":"
            ctc = "ctc_animation_nvl"
        else:
            who_suffix = ""
            ctc = "ctc_animation"
        what_color = "#FFDD7D"
        drop_shadow = (2, 2)
        character = "{color=%s}%s{/color} {color=%s}|{/color} {color=%s}%s{/color}" % (blwnfh_characters[first][1], blwnfh_characters[first][0], colors[time_of_day], blwnfh_characters[second][1], blwnfh_characters[second][0])
        gl[first + "_" + second + "_" + time_of_day[0]] = Character(character, kind=kind, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")

    for i in [("kat", "mi", "day", adv), ("kat", "un", "day", adv), ("me", "dv", "night", nvl), ("me", "el", "sunset", adv), ("me", "kat", "day", adv)]:
        blwnfh_double_char_define(i[0], i[1], i[2], i[3])
    
    ## Функции для переобувания в воздухе ##
    # Переименование персонажа
    def blwnfh_set_name(name, value):
        blwnfh_characters[name][0] = value
        blwnfh_chars_define()
    
    # Смена цвета персонажа
    def blwnfh_set_char_color(name, value):
        blwnfh_characters[name][1] = value
        blwnfh_chars_define()
init -265 python:
    # Нормальные троеточия
    wp = "{w=-.25}.{w=-.25}.{w=-.25}."

init -4:

    image wnfh_ctc_animation = Animation("images/misc/ctc01.png", 0.15, "images/misc/ctc02.png", 0.15, "images/misc/ctc03.png", 0.15, "images/misc/ctc04.png", 0.15, "images/misc/ctc05.png", 0.15, "images/misc/ctc06.png", 0.15, "images/misc/ctc07.png", 0.15, "images/misc/ctc08.png", 0.15, xpos=0.895, ypos=0.98, xanchor=1.0, yanchor=1.0)

    image wnfh_ctc_animation_nvl = Animation("images/misc/ctc01.png", 0.15, "images/misc/ctc02.png", 0.15, "images/misc/ctc03.png", 0.15, "images/misc/ctc04.png", 0.15, "images/misc/ctc05.png", 0.15, "images/misc/ctc06.png", 0.15, "images/misc/ctc07.png", 0.15, "images/misc/ctc08.png", 0.15, xpos=0.9, ypos=0.94, xanchor=1.0, yanchor=1.0)
 

init -3 python:
    wnfh_characters = {
        # персонажи оригинала
        "narrator":[None, None,None],     #Рассказчик
        "th":[None, None,None],           #Мысля Семёна
        "me":[u"Семён", "#E1DD7D"],
        "mi":[u"Мику", "#00DEFF"],
        "usw":[u"Ульяна", "#FF3200"],
        "dv":[u"Алиса", "#FFAA00"],
        "mt":[u"Ольга Дмитриевна", "#00EA32"],
        "mz":[u"Женя", "#4A86FF"],
        "sh":[u"Шурик", "#FFF226"],
        "sl":[u"Славя", "#FFD200"],
        "el":[u"Сергей", "#FFFF00"],
        "un":[u"Лена", "#B956FF"],
        "cs":[u"Виолетта Церновна", "#A5A5FF"],
        "pi":[u"Пионер", "#E60000"],
        "uv":[u"Юля", "#4EFF00"],
        "voice":[u"... ", "#E1DD7D"],
        # новые персонажи
        "kat":[u"Катя", "#FF97BB"],
        "gp":[u"Тётя Галя", "#CECECE"],
        "zg":[u"Тётя Зина", "#D199FF"],
        "sd":[u"Сергей Дмитриевич", "#878787"],
        "void":[u" ", "#000000"],
        "sv":[u"Света", "#F3DA0B"],
        "din":[u"Дина", "#080ACE"],
        # для DLC про деда
        #"cm":[u"Командир", "#", False],
        #"olg":[u"Олег", "#", False],
        #"part":[u"Партизан", "#", False],
        #"kr":[u"Крестьянин", "#", False],
        #"sht":[u"Штайнер", "#", False],
        "neutral":[u"Костыль ебаный", "#BCBCBC"],
    }
    
    #renpy.image("wnfh_radio_icon", im.FactorScale(BKRR_IMAGES + "ui/dialogue_box/radio_icon.png", 0.051))
    #renpy.image("wnfh_speaker_icon", im.FactorScale(BKRR_IMAGES + "ui/dialogue_box/speaker_icon.png", 0.051))

    def wnfh_chars_define(kind=adv):
        gl = globals()
        if kind == nvl:
            who_suffix = ":"
            ctc = "wnfh_ctc_animation_nvl"
        else:
            who_suffix = ""
            ctc = "wnfh_ctc_animation"
        what_color = "#FFDD7D"
        drop_shadow = (2, 2)
        for i, j in wnfh_characters.items():
            if i == "narrator":
                gl[i] = Character(None, kind=kind, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
            elif i == "th":
                gl[i] = Character(None, kind=kind, what_color=what_color, what_drop_shadow=drop_shadow, what_prefix="~ ", what_suffix=" ~", ctc=ctc, ctc_position="fixed")
            else:
                gl[i] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
                gl[i+"_r"] = Character(j[0], kind=kind, who_color=what_color, who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
                gl[i+"_v"] = Character(u"Голос", kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
                #gl[i+"_radio"] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_prefix=" {image=wnfh_radio_icon} ", what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
                #gl[i+"_speaker"] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_prefix=" {image=wnfh_speaker_icon} ", what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")

    ## Спизженные из БКРР парные персонажи и модернизированные для работы с NVL
    def wnfh_double_char_define(first, second, time_of_day, kind=adv):
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
        character = "{color=%s}%s{/color} {color=%s}|{/color} {color=%s}%s{/color}" % (wnfh_characters[first][1], wnfh_characters[first][0], colors[time_of_day], wnfh_characters[second][1], wnfh_characters[second][0])
        gl[first + "_" + second + "_" + time_of_day[0]] = Character(character, kind=kind, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")

    for i in [("kat", "mi", "day", adv), ("kat", "un", "day", adv), ("me", "dv", "night", nvl), ("me", "el", "sunset", adv), ("me", "kat", "day", adv), ("me", "el", "night", adv)]:
        wnfh_double_char_define(i[0], i[1], i[2], i[3])
    
    ## Функции для переобувания в воздухе ##
    # Переименование персонажа
    def wnfh_set_name(name, value):
        wnfh_characters[name][0] = value
        wnfh_chars_define()
    
    # Смена цвета персонажа
    def wnfh_set_char_color(name, value):
        wnfh_characters[name][1] = value
        wnfh_chars_define()

init 0:
    $ mods["blwnfh_main"]=u"Мы не отсюда"

##init с объявлением переменных
init -4 python:

    ## Тут лежат пути к файлам
    blwnfh_ROOT = "mods/blwnfh/"
    
    blwnfh_FONTS = blwnfh_ROOT + "fonts/"
    
    blwnfh_SOUND = blwnfh_ROOT + "sound/"
    blwnfh_SFX = blwnfh_SOUND + "sfx/"
    blwnfh_AMBIENTS = blwnfh_SOUND + "ambients/"
    blwnfh_MUSIC = blwnfh_SOUND + "music/"
    blwnfh_GUI = blwnfh_SOUND + "gui/"
    
    blwnfh_IMAGES = blwnfh_ROOT + "images/"
    blwnfh_CG = blwnfh_IMAGES + "cg/"
    blwnfh_BG = blwnfh_IMAGES + "bg/"
    blwnfh_SPRITES_CLOSE = blwnfh_IMAGES + "sprites/close/"
    blwnfh_SPRITES_NORMAL = blwnfh_IMAGES + "sprites/normal/"
    blwnfh_SPRITES_FAR = blwnfh_IMAGES + "sprites/far/"
    blwnfh_MAIN_MENU = blwnfh_IMAGES + "gui/main_menu/"
    blwnfh_GALLERY = blwnfh_IMAGES + "gui/gallery/"
    blwnfh_TRANSITIONS = blwnfh_IMAGES + "transitions/"
    blwnfh_CHOICE = blwnfh_IMAGES + "gui/choice/"
  
init 1:
    python:

        def blwnfh_timeskip_transition(t=1.0):
            return ImageDissolve(blwnfh_TRANSITIONS + "timeskip.png", t, ramplen=0, reverse=False, alpha=True)
        
        def blwnfh_fade(time=1.0, color="white"):
            ft = time * 0.5
            fc = {
                "black":"#000",
                "white":"#FFF",
                "red":"#F00"
            }
            return Fade(ft, 0.0, ft, color = fc[color])
        
        def blwnfh_hurt_transition(t=0.5):
            return blwnfh_fade(time=t, color="red")
    
init 2:
    ## Звуковые эффекты ##
    $ blwnfh_sfx_list = blwnfh_form_files_list(blwnfh_SFX)

    
    # SFX Лист
    $ blwnfh_sfx_list["ps4_ach"] = blwnfh_SFX + "ps4_ach.ogg"
    
    
    # Рандомизация одинаковых звуков
    $ blwnfh_meow_list = [blwnfh_sfx_list[i] for i in blwnfh_sfx_list.keys() if i.startswith("meow")]

init -1 python:
##    Звуковые функции    ##
    from random import choice
    
    def blwnfh_mute(fade=2.5):
        for channel in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "music"):
            renpy.music.stop(channel=channel, fadeout=fade)

    def blwnfh_set_volume(channel, value, fade=0.0): # для удобства
        renpy.music.set_volume(volume=value, delay=fade, channel=channel)

    def blwnfh_play_random(list, channel="sound"):
        renpy.play(random.choice(list), channel=channel)

    # Создание листов
    def blwnfh_form_files_list(path):
        return {i[len(path):i.rfind(".")]:i for i in renpy.list_files() if i.startswith(path)}
    
    blwnfh_gui = dict()
    
    # Объявление списка GUI
    blwnfh_gui["img"] = {img:(blwnfh_MAIN_MENU + img + ".png") for img in [
        "fish",
        "exit",
        "info",
        "music",
        "joke",
        "scheme",
        "achievements", 
        "gallery",
        "settings",
        "test_fon",
        "fon",
        "bg",
        "vbar_full",
        "vbar_null",
        "play"
        ]}
    
    blwnfh_gui["gallery"] = {img:(blwnfh_GALLERY + img + ".png") for img in [
        "left",
        "right",
        "lock",
        "idle_frame",
        "hover_frame",
        "back",
        "button_1_idle",
        "button_1_hover",
        "button_2",
        "cg",
        "bg"
        ]}
    
    blwnfh_gui["sound"] = {
        "plimp": blwnfh_GUI + "plimp.ogg",
        # тут перечисляем все звуки для меню
    }

    # Ссылки на страницы мода

    blwnfh_gui["hyperlinks"] = {
        "vk":"https://vk.com/blwnfh",
        #"steam":""
        #"discord":""
    }
    
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
        "gp":[u"Галина Петровна", "#CECECE"],
        "zg":[u"Зинаида Геннадьевна", "#D199FF"],
        "sd":[u"Сергей Дмитриевич", "#878787"],

    }
    
    blwnfh_gui["transit"] = {img:(blwnfh_TRANSITIONS + img + ".png") for img in [
        "slide_left",
        "slide_right",
        "slide_up",
        "slide_down",
        "sphere",
        "sphere_invert",
        "clock_l",
        "clock_r",
        "slide_diagonal",
        "exp1",
        "exp2",
        "exp3",
        "ecstrusion"
        ]}
    
    blwnfh_gui["choice"] = {img:(blwnfh_CHOICE + img + ".png") for img in [
        "2_flang_bad",
        "2_flang_dv",
        "2_flang_kat",
        "2_flang_mi",
        "2_flang_mt",
        "2_flang_neutral",
        "2_flang_sl",
        "2_flang_un",
        "2_flang_us",
        "3_flang_bad",
        "3_flang_dv",
        "3_flang_kat",
        "3_flang_mi",
        "3_flang_mt",
        "3_flang_neutral",
        "3_flang_sl",
        "3_flang_un",
        "3_flang_us",
        "3_mid_bad",
        "3_mid_dv",
        "3_mid_kat",
        "3_mid_mi",
        "3_mid_mt",
        "3_mid_neutral",
        "3_mid_sl",
        "3_mid_un",
        "3_mid_us",
        "line_2",
        "line_3",
        "vignette",
        "vignette_night",
        "line_2_day",
        "line_2_sunset",
        "line_2_night",
        "line_2_prologue",
        "line_3_day",
        "line_3_sunset",
        "line_3_night",
        "line_3_prologue",
        ]}
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

    # Регистрация ачивок и предметов
    
    blwnfh_ach_list = (
        ("payday", u"Конфетный вор"),
    )
    
    if not persistent.blwnfh_ach:
        persistent.blwnfh_ach = dict()
    
    for ach in blwnfh_ach_list:
        renpy.image("blwnfh_ach_" + ach[0], im.Scale(blwnfh_IMAGES + "gui/achievements/" + ach[0] + ".png", 600, 125))
        if ach[0] not in persistent.blwnfh_ach:
            persistent.blwnfh_ach[ach[0]] = False
    
    renpy.image("blwnfh_ach_blank", im.Scale(blwnfh_IMAGES + "gui/achievements/blank.png", 600, 125))
    
    blwnfh_item_list = ("knife", "paint", "tape", "key", "food", "powder", "accumulator", "comb", "pills", "apple", "note", "shark_tooth", "matchbox", "love_letter", "tabs", "bandana", "gram", "birth_certificate", "roses", "healing_potion")
    
    for item in blwnfh_item_list:
        renpy.image("blwnfh_item_" + item, im.Scale(blwnfh_IMAGES + "gui/items/" + item + ".png", 450, 360))
    
    # Призыв ачивок и предметов
    
    def blwnfh_get_achievement(ach):
        if not persistent.blwnfh_ach[ach]:
            persistent.blwnfh_ach[ach] = True
            renpy.play(blwnfh_sfx_list["ps4_ach"], channel="sound")
            renpy.show("blwnfh_ach_" + ach, [blwnfh_get_achievement_atl])
            renpy.pause(7.5)
            renpy.hide("blwnfh_ach_" + ach)

    def blwnfh_get_item(item, sounded=True):
        if sounded:
            renpy.play(blwnfh_sfx_list["get_item"], channel="sound")
        renpy.show("blwnfh_item_%s" % item, [blwnfh_get_item_atl])
        renpy.pause(5.0)
        renpy.hide("blwnfh_item_%s" % item)
    
    # Просто полезная херня
    
    def blwnfh_check_achievements():
        j = 0
        for i in persistent.blwnfh_ach.values():
            if i:
                j += 1
        return j
    
    def blwnfh_reset_achievements():
        for ach in blwnfh_ach_list:
            persistent.blwnfh_ach[ach[0]] = False
























    ##    Настройки и ресурсы экранов мода    ##

    # Звуковые элементы меню

    

    # Графические элементы галереи

    #for img in ("bg", "button_1", "button_2", "cg", "noise_1", "noise_2", "noise_3", "noise_4", "not_opened_%s_1", "not_opened_%s_2", "not_opened_%s_3", "thumbnail_idle", "thumbnail_hover"):
    #    blwnfh_gui["img"][img] = BKRR_IMAGES + "ui/gallery/" + img + ".png"
    #
    ## Список ресурсов галереи
    #
    #blwnfh_gallery_grid = {
    #    "bg":(
    #        (["ext_music_club_verandah_day_v1", False], ["ext_music_club_verandah_day_v7", False], ["ext_music_club_verandah_night_v2", False], ["int_music_club_mattresses_day", False], ["int_music_club_mattresses_sunset", False], ["int_music_club_mattresses_night", False]),
    #        (["int_cinema_people", False], ["int_shed_blwnfh_v1", False], ["int_old_building_room_day_rainy_blwnfh", BKRR_IMAGES + "bg/int_old_building_room_day_rainy.jpg"], ["int_old_building_room_night_blwnfh_v1", blwnfh_fast_composite(BKRR_IMAGES + "bg/int_old_building_room_night_rainy.jpg", BKRR_IMAGES + "misc/int_old_building_room_mugs_fire.png", BKRR_IMAGES + "misc/int_old_building_room_fire1.png", BKRR_IMAGES + "misc/int_old_building_room_steam1.png")], ["int_old_building_room_day_blwnfh_v2", False], ["ext_path3_day_blwnfh", False]),
    #        (["semen_room_clean_blwnfh", False], ["ext_beach_water_day", BKRR_IMAGES + "bg/ext_beach_water_day.jpg"], ["int_infirmary_night_guitar", False], ["int_infirmary_sunset_guitar", False], ["int_infirmary_day_guitar", False], ["ext_pier_day", False]),
    #        (["ext_pier_sunset", False], ["int_clubs_male_day_wrecked", False], ["int_clubs_male_sunset_wrecked", False], ["ext_stage_big_day_str_blwnfh", False], ["ext_stage_big_day_const_blwnfh", False], ["ext_stage_big_day_evening_empty", False]),
    #        (["ext_backstage_big_day_night", False], ["ext_backstage_big_day_night_noplank", False], ["int_bus_people_day_blwnfh", False], ["ext_street_night", False], ["int_entrance_blwnfh", blwnfh_fast_composite(BKRR_IMAGES + "bg/int_entrance_outside.jpg", BKRR_IMAGES + "bg/int_entrance.png")], ["int_entrance_blwnfh_with_cat", blwnfh_fast_composite(BKRR_IMAGES + "bg/int_entrance_outside.jpg", BKRR_IMAGES + "bg/int_entrance.png", BKRR_IMAGES + "bg/int_entrance_cat.png")]),
    #        (["int_school_night", blwnfh_fast_composite(BKRR_IMAGES + "bg/int_school_ext.jpg", BKRR_IMAGES + "bg/int_school_night.png")], ["int_classroom_night", blwnfh_fast_composite(BKRR_IMAGES + "bg/int_classroom_ext.jpg", BKRR_IMAGES + "bg/int_classroom_night.png")])
    #    ),
    #    "cg":(
    #        (["d5_cat_in_ventilation", False], ["d5_ghost", False], ["d6_sl_ass", False], ["d6_on_floor", False], ["d6_dv_guitar", False], ["d6_sem_guitar", False]),
    #        (["d7_mi_embrace", False], ["d7_mi_dance", False], ["d7_mi_walking", False], ["d8_deer", im.Crop(BKRR_IMAGES + "cg/d8_deer.jpg", 0, 180, 1920, 1080)], ["d8_chibi", False], ["d8_fstar_main", False]),
    #        (["d9_walking", blwnfh_fast_composite(BKRR_ES_IMAGES + "bg/ext_houses_day.jpg", BKRR_IMAGES + "cg/d9_walking.png")], ["d9_wounded_dv", False], ["d9_squirrel_1", False], ["d9_squirrel_2", False], ["d9_kiss", False], ["d10_ghost", False]),
    #        (["d11_shirt_1", im.Crop(BKRR_IMAGES + "cg/d11_shirt.jpg", 0, 180, 1920, 1080)], ["d11_forest", im.Crop(BKRR_IMAGES + "cg/d11_forest.jpg", 0, 0, 1920, 1080)], ["d11_forest_view_with_shadow", False], ["d11_forest_view_with_pi", False], ["d11_mi_sleep_1", BKRR_IMAGES + "cg/d11_mi_sleep_1.png"], ["d11_mi_sleep_2", BKRR_IMAGES + "cg/d11_mi_sleep_2.png"]),
    #        (["d11_mi_sleep_3", im.Composite((config.screen_width, config.screen_height), (0, 0), BKRR_IMAGES + "cg/d11_mi_sleep_1.png", (1250, 375), im.Crop(BKRR_IMAGES + "cg/d11_mi_sleep_2.png", 1250, 375, 100, 100))], ["d11_night_guest", False], ["d12_mi_hair_sl", False], ["d12_mi_hair_sem", False], ["d12_mi_hair_sem_bite", False], ["d12_mi_bath_1", False]),
    #        (["d12_mi_bath_2", False], ["d12_noon_rest_1", False], ["d12_noon_rest_2", False], ["d12_us_kiss_2", False], ["d12_us_kiss_3", False], ["d13_beach", False]),
    #        (["d14_un_sleep", False], ["d14_us_fall", False], ["d14_un_cry", False], ["d14_dv_spy", False], ["d14_dv_window_1", False], ["d14_mi_confession_1", False]),
    #        (["d14_mi_confession_3", False], ["d14_rocket_2", BKRR_IMAGES + "cg/d14_rocket_2.png"], ["d15_mi_sleep", False], ["d16_catmiku", im.Crop(BKRR_IMAGES + "cg/d16_catmiku.jpg", 0, 0, 1920, 1080)], ["d16_cryptography", False], ["d16_gulls", False]),
    #        (["d16_picnic", BKRR_IMAGES + "cg/d16_picnic3.jpg"], ["d17_alisa_klaus", BKRR_IMAGES + "cg/d17_alisa_klaus.jpg"], ["d17_klaus_guitar", im.Scale(BKRR_IMAGES + "cg/d17_klaus_guitar.jpg", config.screen_width, config.screen_height)], ["d17_mt_mine", False], ["d17_sex", False], ["d18_bed_middle", im.Scale(BKRR_IMAGES + "cg/d18_bed.jpg", config.screen_width, config.screen_height)]),
    #        (["d18_bed_sleep", blwnfh_fast_composite(im.Scale(BKRR_IMAGES + "cg/d18_bed.jpg", config.screen_width, config.screen_height), im.Scale(BKRR_IMAGES + "cg/d18_bed_mi_sleep.png", config.screen_width, config.screen_height))], ["d18_bed_open", blwnfh_fast_composite(im.Scale(BKRR_IMAGES + "cg/d18_bed.jpg", config.screen_width, config.screen_height), im.Scale(BKRR_IMAGES + "cg/d18_bed_mi_open.png", config.screen_width, config.screen_height))], ["d18_alisarape", False], ["d18_alisarape2", blwnfh_fast_composite(BKRR_IMAGES + "cg/d18_alisarape.jpg", BKRR_IMAGES + "cg/d18_alisarape_2.png")], ["d18_young_od", False], ["d18_ulyana_molotok", False]),
    #        (["d18_sunset_original_mi", False], ["d19_truk_and_zmey", False], ["d19_truk_and_zmey_close", False], ["d19_bus_escape", False], ["d19_miku_bus_1", False], ["d19_miku_bus_2", False]),
    #        (["d19_miku_bus_3", False], ["d19_concert_alisa", im.Scale(BKRR_IMAGES + "cg/d19_concert_alisa.jpg", config.screen_width, config.screen_height)], ["d19_concert_ulyana", False], ["d19_concert_miku_semen", False], ["d19_slavya_captured", False], ["d19_pirates_on_stage", BKRR_IMAGES + "cg/d19_pirates_on_stage.jpg"]),
    #        (["d19_alisa_miku_song", blwnfh_fast_composite(BKRR_IMAGES + "cg/d19_alisa_miku_song/bg.png", BKRR_IMAGES + "cg/d19_alisa_miku_song/singers.png", BKRR_IMAGES + "cg/d19_alisa_miku_song/mic.png")], ["d19_chibi_alisa", BKRR_IMAGES + "cg/d19_chibi_alisa.jpg"], ["d19_final_campfire", False], ["blwnfh_epilogue_1", False], ["blwnfh_epilogue_2", False], ["blwnfh_epilogue_3", False]),
    #        (["blwnfh_epilogue_4", False], ["blwnfh_epilogue_7", False], ["ep_mi", blwnfh_fast_composite(BKRR_IMAGES + "cg/ep_mi_background.jpg", BKRR_IMAGES + "cg/ep_mi.png")], ["catday_warp_cat", False]),
    #    )
    #}
    #
    #for grid in blwnfh_gallery_grid.values():
    #    for page in grid:
    #        for img in page:
    #            img.append(str(random.randrange(1, 5, 1)))
    #            img.append(str(random.randrange(1, 4, 1)))
    #
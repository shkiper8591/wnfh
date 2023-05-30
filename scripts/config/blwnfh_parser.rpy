init -3 python:
    
    """
    Парсер БГ и СГ для ленивых
    А то заебали уже со своим говнокодом
    Насмотрелись блять гайдов Хандера и Деда
    Чей код не открою, везде ёбаные стены с объявлением каждого фона отдельно
    Хоть самому блять берись и делай гайды
    """
    
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

    blwnfh_backgrounds = blwnfh_parse_folder("bg")
    blwnfh_graphics = blwnfh_parse_folder("cg")

    blwnfh_make_images("bg", blwnfh_backgrounds)
    blwnfh_make_images("cg", blwnfh_graphics)
    
init -3 python:
    def blwnfh_fast_composite(*args):
        arg_list = list()
        for arg in args:
            arg_list.append((0, 0))
            arg_list.append(arg)
        return im.Composite((config.screen_width, config.screen_height), *arg_list)

    def blwnfh_fast_livecomposite(*args):
        arg_list = list()
        for arg in args:
            arg_list.append((0, 0))
            arg_list.append(arg)
        return LiveComposite((config.screen_width, config.screen_height), *arg_list)

init -2:
    image bg int_editorial_day_bumaga = blwnfh_fast_composite(im.Scale(blwnfh_IMAGES + "bg/int_editorial_day.jpg", config.screen_width, config.screen_height), im.Scale(blwnfh_OTHER + "int_editorial_day_bumaga.png", config.screen_width, config.screen_height))
    image cg d3_me_kat_blindage = blwnfh_fast_livecomposite(blwnfh_IMAGES + "cg/d3_me_kat_blindage.png", blwnfh_fire_light_atl(blwnfh_OTHER + "d3_me_kat_blindage_light.png"))
    image cg d3_me_kat_blindage2 = blwnfh_fast_livecomposite(blwnfh_IMAGES + "cg/d3_me_kat_blindage2.png", blwnfh_fire_light_atl(blwnfh_OTHER + "d3_me_kat_blindage_light.png"))
    #image cg d6_mt_volosbl = blwnfh_fast_livecomposite(blwnfh_IMAGES + "cg/d6_mt_volosbl.png", blwnfh_wakeup_dark(blwnfh_IMAGES + "cg/d6_mt_volosbl.png"))
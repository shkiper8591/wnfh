init -3 python:
    
    """
    Парсер БГ и СГ для ленивых
    А то заебали уже со своим говнокодом
    Насмотрелись блять гайдов Хандера и Деда
    Чей код не открою, везде ёбаные стены с объявлением каждого фона отдельно
    Хоть самому блять берись и делай гайды
    """
    
    def wnfh_parse_folder(key):
        r = []
        for path in renpy.list_files():
            if path.startswith(wnfh_IMAGES + key + "/"):
                r.append((path.split("/")[-1].split(".")[0], path))
        return r

    def wnfh_make_images(key, r):
        for i in r:
            name, path = i
            renpy.image(key + " " + name, path)

    wnfh_backgrounds = wnfh_parse_folder("bg")
    wnfh_graphics = wnfh_parse_folder("cg")

    wnfh_make_images("bg", wnfh_backgrounds)
    wnfh_make_images("cg", wnfh_graphics)
    
init -3 python:
    def wnfh_fast_composite(*args):
        arg_list = list()
        for arg in args:
            arg_list.append((0, 0))
            arg_list.append(arg)
        return im.Composite((config.screen_width, config.screen_height), *arg_list)

    def wnfh_fast_livecomposite(*args):
        arg_list = list()
        for arg in args:
            arg_list.append((0, 0))
            arg_list.append(arg)
        return LiveComposite((config.screen_width, config.screen_height), *arg_list)

init -2:
    image bg int_dining_hall_day_vedro_wnfh = wnfh_fast_composite(im.Scale(wnfh_ES_IMAGES + "bg/int_dining_hall_day.jpg", config.screen_width, config.screen_height), im.Scale(wnfh_OTHER + "vedro.png", config.screen_width, config.screen_height))
    image bg int_editorial_day_bumaga_wnfh = wnfh_fast_composite(im.Scale(wnfh_IMAGES + "bg/int_editorial_day_wnfh.jpg", config.screen_width, config.screen_height), im.Scale(wnfh_OTHER + "bumaga.png", config.screen_width, config.screen_height))
    image cg d9_me_kat_blindage_wnfh = wnfh_fast_livecomposite(wnfh_IMAGES + "cg/d9_me_kat_blindage_wnfh.png", wnfh_fire_light_atl(wnfh_OTHER + "d9_me_kat_blindage_light.png"))
    image cg d9_me_kat_blindage2_wnfh = wnfh_fast_livecomposite(wnfh_IMAGES + "cg/d9_me_kat_blindage2_wnfh.png", wnfh_fire_light_atl(wnfh_OTHER + "d9_me_kat_blindage_light.png"))
    #image cg d12_mt_volosbl = wnfh_fast_livecomposite(wnfh_IMAGES + "cg/d12_mt_volosbl.png", wnfh_wakeup_dark(wnfh_IMAGES + "cg/d12_mt_volosbl.png"))
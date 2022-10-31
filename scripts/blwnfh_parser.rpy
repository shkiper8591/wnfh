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
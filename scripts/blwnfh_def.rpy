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

    blwnfh_backgrounds = blwnfh_parse_folder("bg")
    blwnfh_graphics = blwnfh_parse_folder("cg")

    blwnfh_make_images("bg", blwnfh_backgrounds)
    blwnfh_make_images("cg", blwnfh_graphics)


init -265 python:
    
    wp = "{w=-.25}.{w=-.25}.{w=-.25}."
    
    # Всякий разный цветокор
    def Sepia(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.15) * im.matrix.tint(1.0, .94, .76))
    def OldPhoto(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.6) * im.matrix.brightness(0.03))
    def Grayed(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.01))

    # Цветокор под разное время суток
    def Notch(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.2) * im.matrix.saturation(0.6))
    def Dawn(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.1) * im.matrix.tint(0.94, 0.82, 1.0))
    def Noon(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(0.2) * im.matrix.tint(1.0, 0.94, 0.82))
    def HomeCity(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.1) * im.matrix.tint(0.82, 0.84, 1.0))
    def Rained(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.4) * im.matrix.tint(0.68, 0.90, 0.8) * im.matrix.saturation(0.6))
        
    def filmetile(bitmap, opacity=0.1):
        return im.Tile(im.Alpha(bitmap,opacity))
        
init python:
    #Функция для отображения времени в меню
    from random import choice

    def blwnfh_get_usertime():
        from time import strftime, localtime
        time = strftime("%H:%M:%S", localtime())
        hour, min, sec = time.split(":")
        hour = int(hour)
        return str(hour) + ":" + str(min)

    
init:   #Транзиты на любой вкус и цвет, точно не спизженные у 7дл, правда-правда         
                                                                #1 параметр: степень замедления транзита
                                                                #2 параметр: степень размытия
    #Слайд слева
    $ slide_left_dissolve = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_left"]), 1.0, 1)
    $ slide_left_dissolve2 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_left"]), 2.0, 1)
    $ slide_left_dissolve5 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_left"]), 5.0, 1)
    $ slide_left_dissolve10 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_left"]), 10.0, 1)
    #Слайд слева размытый
    $ slide_left_blure_dissolve = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_left"]), 1.0, 100)
    $ slide_left_blure_dissolve2 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_left"]), 2.0, 100)
    $ slide_left_blure_dissolve5 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_left"]), 5.0, 100)
    $ slide_left_blure_dissolve10 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_left"]), 10.0, 100)
    
    #Слайд справа
    $ slide_right_dissolve = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_right"]), 1.0, 1)
    $ slide_right_dissolve2 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_right"]), 2.0, 1)
    $ slide_right_dissolve5 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_right"]), 5.0, 1)
    $ slide_right_dissolve10 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_right"]), 10.0, 1)
    #Слайд справа размытый
    $ slide_right_blure_dissolve = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_right"]), 1.0, 100)
    $ slide_right_blure_dissolve2 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_right"]), 2.0, 100)
    $ slide_right_blure_dissolve5 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_right"]), 5.0, 100)
    $ slide_right_blure_dissolve10 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_right"]), 10.0, 100)
    
    #Слайд сверху
    $ slide_up_dissolve = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_up"]), 1.0, 1)
    $ slide_up_dissolve2 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_up"]), 2.0, 1)
    $ slide_up_dissolve5 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_up"]), 5.0, 1)
    $ slide_up_dissolve10 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_up"]), 10.0, 1)
    #Слайд сверху размытый
    $ slide_up_blure_dissolve = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_up"]), 1.0, 100)
    $ slide_up_blure_dissolve2 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_up"]), 2.0, 100)
    $ slide_up_blure_dissolve5 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_up"]), 5.0, 100)
    $ slide_up_blure_dissolve10 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_up"]), 10.0, 100)
    
    #Слайд снизу
    $ slide_down_dissolve = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_down"]), 1.0, 1)
    $ slide_down_dissolve2 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_down"]), 2.0, 1)
    $ slide_down_dissolve5 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_down"]), 5.0, 1)
    $ slide_down_dissolve10 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_down"]), 10.0, 1)
    #Слайд снизу размытый
    $ slide_down_blure_dissolve = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_down"]), 1.0, 100)
    $ slide_down_blure_dissolve2 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_down"]), 2.0, 100)
    $ slide_down_blure_dissolve5 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_down"]), 5.0, 100)
    $ slide_down_blure_dissolve10 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_down"]), 10.0, 100)
    
    #Сфера из центра
    $ sphere_dissolve = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere"]), 1.0, 1)
    $ sphere_dissolve2 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere"]), 2.0, 1)
    $ sphere_dissolve5 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere"]), 5.0, 1)
    $ sphere_dissolve10 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere"]), 10.0, 1)
    #Сфера из центра размытая
    $ sphere_blure_dissolve = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere"]), 1.0, 100)
    $ sphere_blure_dissolve2 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere"]), 2.0, 100)
    $ sphere_blure_dissolve5 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere"]), 5.0, 100)
    $ sphere_blure_dissolve10 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere"]), 10.0, 100)
    
    #Сфера в центр
    $ sphere_invert_dissolve = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere_invert"]), 1.0, 1)
    $ sphere_invert_dissolve2 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere_invert"]), 2.0, 1)
    $ sphere_invert_dissolve5 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere_invert"]), 5.0, 1)
    $ sphere_invert_dissolve10 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere_invert"]), 10.0, 1)
    #Сфера в центр размытая
    $ sphere_invert_blure_dissolve = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere_invert"]), 1.0, 100)
    $ sphere_invert_blure_dissolve2 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere_invert"]), 2.0, 100)
    $ sphere_invert_blure_dissolve5 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere_invert"]), 5.0, 100)
    $ sphere_invert_blure_dissolve10 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["sphere_invert"]), 10.0, 100)
    
    #Диагональный слайд размытый
    $ slide_diagonal_blure_dissolve = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_diagonal"]), 1.0, 100)
    $ slide_diagonal_blure_dissolve2 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_diagonal"]), 2.0, 100)
    $ slide_diagonal_blure_dissolve5 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_diagonal"]), 5.0, 100)
    $ slide_diagonal_blure_dissolve10 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["slide_diagonal"]), 10.0, 100)
    
    
    $ experemental1 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["exp1"]), 5, 1)
    $ experemental2 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["exp2"]), 5, 1)
    $ experemental3 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["exp3"]), 5, 10)
    $ experemental4 = ImageDissolve(im.Tile(blwnfh_gui["transit"]["ecstrusion"]), 5, 1)
    
    image anim_grain: #АААЙ БЛЯ ЧЁ ТАК ГРОМКО ШУМИТ?!
        filmetile(blwnfh_TRANSITIONS + "alt_noise1.png")
        pause 0.1
        filmetile(blwnfh_TRANSITIONS + "alt_noise2.png")
        pause 0.1
        filmetile(blwnfh_TRANSITIONS + "alt_noise3.png")
        pause 0.1
        repeat


init 1:
    # Шрифты
    $ style.blwnfh_title = Style(style.default)
    #$ style.blwnfh_title.font = blwnfh_FONTS + "Dymaxion scriptS.ttf"
    $ style.blwnfh_title.font = blwnfh_FONTS + "Sirius Cursiv.ttf"
    $ style.blwnfh_title.color = "#FFF"
    $ style.blwnfh_title.drop_shadow = (2, 2)
    $ style.blwnfh_title.drop_shadow_color = "#222"
    $ style.blwnfh_title.text_align = 0.5
    $ style.blwnfh_title.yalign = 0.5
    $ style.blwnfh_title.size = 80
    $ style.blwnfh_title.kerning = 2.0
    $ renpy.image("blwnfh_title", ParameterizedText(style="blwnfh_title", size=64))

    $ style.blwnfh_menu = Style(style.default)
    $ style.blwnfh_menu.font = blwnfh_FONTS + "msjhl.ttc"
    $ style.blwnfh_menu.color = "#FFF"
    $ style.blwnfh_menu.drop_shadow = (2, 2)
    $ style.blwnfh_menu.drop_shadow_color = "#222"
    $ style.blwnfh_menu.text_align = 0.5
    $ style.blwnfh_menu.yalign = 0.5
    $ style.blwnfh_menu.size = 42
    $ style.blwnfh_menu.kerning = 1.0
    $ renpy.image("blwnfh_menu", ParameterizedText(style="blwnfh_menu", size=64))
    
    $ style.blwnfh_settings = Style(style.default)
    $ style.blwnfh_settings.font = blwnfh_FONTS + "msjhl.ttc"
    $ style.blwnfh_settings.color = "#FFF"
    $ style.blwnfh_settings.text_align = 0.0
    $ style.blwnfh_settings.drop_shadow = (2, 2)
    $ style.blwnfh_settings.drop_shadow_color = "#222"
    $ style.blwnfh_settings.text_align = 0.5
    $ style.blwnfh_settings.yalign = 0.5
    $ style.blwnfh_settings.size = 35
    $ style.blwnfh_settings.kerning = 1.0
    $ renpy.image("blwnfh_settings", ParameterizedText(style="blwnfh_settings", size=64))

    $ style.blwnfh_settings_textbutton = Style(style.default)
    $ style.blwnfh_settings_textbutton.font = blwnfh_FONTS + "msjhl.ttc"
    $ style.blwnfh_settings_textbutton.size = 35
    $ style.blwnfh_settings_textbutton.kerning = 1.0
    $ style.blwnfh_settings_textbutton.color = "#FFF"
    $ style.blwnfh_settings_textbutton.text_align = 0.0
    $ style.blwnfh_settings_textbutton.drop_shadow = (2, 2)
    $ style.blwnfh_settings_textbutton.drop_shadow_color = "#222"
    $ style.blwnfh_settings_textbutton.hover_color = "#E6E6E6"
    $ style.blwnfh_settings_textbutton.selected_color = "#FFF"
    $ style.blwnfh_settings_textbutton.selected_idle_color = "#FFF"
    $ style.blwnfh_settings_textbutton.selected_hover_color = "#E6E6E6"
    $ style.blwnfh_settings_textbutton.insensitive_color = "#FFF"
      
    $ style.blwnfh_news = Style(style.default)
    $ style.blwnfh_news.font = blwnfh_FONTS + "msjhl.ttc"
    $ style.blwnfh_news.color = "#FFF"
    $ style.blwnfh_news.drop_shadow = (2, 2)
    $ style.blwnfh_news.drop_shadow_color = "#222"
    $ style.blwnfh_news.text_align = 0.0
    $ style.blwnfh_settings.size = 25
    $ style.blwnfh_news.kerning = 1.0
    $ renpy.image("blwnfh_news", ParameterizedText(style="blwnfh_news", size=64))
    
    $ style.blwnfh_choice_day = Style(style.default)
    $ style.blwnfh_choice_day.font = blwnfh_FONTS + "KarloCham-Line.otf"
    $ style.blwnfh_choice_day.color = "#E2C778"
    $ style.blwnfh_choice_day.drop_shadow = (3, 3)
    $ style.blwnfh_choice_day.drop_shadow_color = "#000"
    $ style.blwnfh_choice_day.text_align = 0.5
    $ style.blwnfh_choice_day.yalign = 0.5
    $ style.blwnfh_choice_day.size = 64
    $ style.blwnfh_choice_day.kerning = 1.0
    $ renpy.image("blwnfh_choice_day", ParameterizedText(style="blwnfh_choice_day", size=40))
    
    $ style.blwnfh_choice_sunset = Style(style.default)
    $ style.blwnfh_choice_sunset.font = blwnfh_FONTS + "KarloCham-Line.otf"
    $ style.blwnfh_choice_sunset.color = "#DCD168"
    $ style.blwnfh_choice_sunset.drop_shadow = (3, 3)
    $ style.blwnfh_choice_sunset.drop_shadow_color = "#000"
    $ style.blwnfh_choice_sunset.text_align = 0.5
    $ style.blwnfh_choice_sunset.yalign = 0.5
    $ style.blwnfh_choice_sunset.size = 64
    $ style.blwnfh_choice_sunset.kerning = 1.0
    $ renpy.image("blwnfh_choice_sunset", ParameterizedText(style="blwnfh_choice_sunset", size=40))
    
    $ style.blwnfh_choice_night = Style(style.default)
    $ style.blwnfh_choice_night.font = blwnfh_FONTS + "KarloCham-Line.otf"
    $ style.blwnfh_choice_night.color = "#3CCFA2"
    $ style.blwnfh_choice_night.drop_shadow = (3, 3)
    $ style.blwnfh_choice_night.drop_shadow_color = "#000"
    $ style.blwnfh_choice_night.text_align = 0.5
    $ style.blwnfh_choice_night.yalign = 0.5
    $ style.blwnfh_choice_night.size = 64
    $ style.blwnfh_choice_night.kerning = 1.0
    $ renpy.image("blwnfh_choice_night", ParameterizedText(style="blwnfh_choice_night", size=40))
    
    $ style.blwnfh_choice_prologue = Style(style.default)
    $ style.blwnfh_choice_prologue.font = blwnfh_FONTS + "KarloCham-Line.otf"
    $ style.blwnfh_choice_prologue.color = "#98D8DA"
    $ style.blwnfh_choice_prologue.drop_shadow = (3, 3)
    $ style.blwnfh_choice_prologue.drop_shadow_color = "#000"
    $ style.blwnfh_choice_prologue.text_align = 0.5
    $ style.blwnfh_choice_prologue.yalign = 0.5
    $ style.blwnfh_choice_prologue.size = 64
    $ style.blwnfh_choice_prologue.kerning = 1.0
    $ renpy.image("blwnfh_choice_prologue", ParameterizedText(style="blwnfh_choice_prologue", size=40))
    
    
    $ style.blwnfh_choice_text_day = Style(style.default)
    $ style.blwnfh_choice_text_day.font = blwnfh_FONTS + "KarloCham-Line.otf"
    $ style.blwnfh_choice_text_day.color = "#E2C778"
    $ style.blwnfh_choice_text_day.drop_shadow = (3, 3)
    $ style.blwnfh_choice_text_day.drop_shadow_color = "#000"
    $ style.blwnfh_choice_text_day.text_align = 0.5
    $ style.blwnfh_choice_text_day.yalign = 0.5
    $ style.blwnfh_choice_text_day.size = 40
    $ style.blwnfh_choice_text_day.kerning = 1.0
    $ renpy.image("blwnfh_choice_text_day", ParameterizedText(style="blwnfh_choice_text_day", size=40))
    
    $ style.blwnfh_choice_text_sunset = Style(style.default)
    $ style.blwnfh_choice_text_sunset.font = blwnfh_FONTS + "KarloCham-Line.otf"
    $ style.blwnfh_choice_text_sunset.color = "#DCD168"
    $ style.blwnfh_choice_text_sunset.drop_shadow = (3, 3)
    $ style.blwnfh_choice_text_sunset.drop_shadow_color = "#000"
    $ style.blwnfh_choice_text_sunset.text_align = 0.5
    $ style.blwnfh_choice_text_sunset.yalign = 0.5
    $ style.blwnfh_choice_text_sunset.size = 40
    $ style.blwnfh_choice_text_sunset.kerning = 1.0
    $ renpy.image("blwnfh_choice_text_sunset", ParameterizedText(style="blwnfh_choice_text_sunset", size=40))
    
    $ style.blwnfh_choice_text_night = Style(style.default)
    $ style.blwnfh_choice_text_night.font = blwnfh_FONTS + "KarloCham-Line.otf"
    $ style.blwnfh_choice_text_night.color = "#3CCFA2"
    $ style.blwnfh_choice_text_night.drop_shadow = (3, 3)
    $ style.blwnfh_choice_text_night.drop_shadow_color = "#000"
    $ style.blwnfh_choice_text_night.text_align = 0.5
    $ style.blwnfh_choice_text_night.yalign = 0.5
    $ style.blwnfh_choice_text_night.size = 40
    $ style.blwnfh_choice_text_night.kerning = 1.0
    $ renpy.image("blwnfh_choice_text_night", ParameterizedText(style="blwnfh_choice_text_night", size=40))
    
    $ style.blwnfh_choice_text_prologue = Style(style.default)
    $ style.blwnfh_choice_text_prologue.font = blwnfh_FONTS + "KarloCham-Line.otf"
    $ style.blwnfh_choice_text_prologue.color = "#98D8DA"
    $ style.blwnfh_choice_text_prologue.drop_shadow = (3, 3)
    $ style.blwnfh_choice_text_prologue.drop_shadow_color = "#000"
    $ style.blwnfh_choice_text_prologue.text_align = 0.5
    $ style.blwnfh_choice_text_prologue.yalign = 0.5
    $ style.blwnfh_choice_text_prologue.size = 40
    $ style.blwnfh_choice_text_prologue.kerning = 1.0
    $ renpy.image("blwnfh_choice_text_prologue", ParameterizedText(style="blwnfh_choice_text_prologue", size=40))

    $ style.blwnfh_thought = Style(style.default)
    $ style.blwnfh_thought.drop_shadow = (2, 2)
    $ style.blwnfh_thought.drop_shadow_color = "#000"
    $ style.blwnfh_thought.text_align = 0.5
    $ renpy.image("blwnfh_thought", ParameterizedText(style="blwnfh_thought", size=40))
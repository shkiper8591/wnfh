init -2:
    # Шрифты
    $ style.blwnfh_title = Style(style.default)
    $ style.blwnfh_title.font = blwnfh_FONTS + "Sirius Cursiv.ttf"
    $ style.blwnfh_title.color = "#FFF"
    $ style.blwnfh_title.drop_shadow = (2, 2)
    $ style.blwnfh_title.drop_shadow_color = "#222"
    $ style.blwnfh_title.text_align = 0.5
    $ style.blwnfh_title.yalign = 0.5
    $ style.blwnfh_title.size = 80
    $ style.blwnfh_title.kerning = 2.0
    $ renpy.image("blwnfh_title", ParameterizedText(style="blwnfh_title", size=64))

    $ style.blwnfh_ach_title = Style(style.default)
    $ style.blwnfh_ach_title.font = blwnfh_FONTS + "msjhl.ttc"
    $ style.blwnfh_ach_title.color = "#000"
    $ style.blwnfh_ach_title.text_align = 0.5
    $ style.blwnfh_ach_title.yalign = 0.5
    $ style.blwnfh_ach_title.size = 42
    $ style.blwnfh_ach_title.kerning = 1.0
    $ renpy.image("blwnfh_ach_title", ParameterizedText(style="blwnfh_ach_title", size=64))
    
    $ style.blwnfh_ach_signature = Style(style.default)
    $ style.blwnfh_ach_signature.font = blwnfh_FONTS + "msjhl.ttc"
    $ style.blwnfh_ach_signature.color = "#000"
    $ style.blwnfh_ach_signature.text_align = 0.5
    $ style.blwnfh_ach_signature.yalign = 0.5
    $ style.blwnfh_ach_signature.size = 38
    $ style.blwnfh_ach_signature.kerning = 1.0
    $ renpy.image("blwnfh_ach_signature", ParameterizedText(style="blwnfh_ach_signature", size=64))
    
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

    $ style.blwnfh_splashes = Style(style.default)
    $ style.blwnfh_splashes.font = blwnfh_FONTS + "vcr_osd.ttf"
    $ style.blwnfh_splashes.color = "#FFFF00"
    $ style.blwnfh_splashes.drop_shadow = (2, 2)
    $ style.blwnfh_splashes.drop_shadow_color = "#222"
    $ style.blwnfh_splashes.text_align = 0.5
    $ style.blwnfh_splashes.size = 20
    $ renpy.image("blwnfh_splashes", ParameterizedText(style="blwnfh_splashes", size=64))

    
    $ style.blwnfh_settings = Style(style.default)
    $ style.blwnfh_settings.font = blwnfh_FONTS + "AlumniSansPinstripe-Regular.ttf"
    $ style.blwnfh_settings.color = "#FFF"
    $ style.blwnfh_settings.text_align = 0.0
    $ style.blwnfh_settings.drop_shadow = (2, 2)
    $ style.blwnfh_settings.drop_shadow_color = "#222"
    $ style.blwnfh_settings.text_align = 0.5
    $ style.blwnfh_settings.yalign = 0.5
    $ style.blwnfh_settings.size = 30
    $ style.blwnfh_settings.kerning = 1.0
    $ renpy.image("blwnfh_settings", ParameterizedText(style="blwnfh_settings", size=30))

    $ style.blwnfh_settings_underwrites = Style(style.default)
    $ style.blwnfh_settings_underwrites.font = blwnfh_FONTS + "IntroDemo-BlackCAPS.otf"
    $ style.blwnfh_settings_underwrites.color = "#FFF"
    $ style.blwnfh_settings_underwrites.text_align = 0.0
    $ style.blwnfh_settings_underwrites.drop_shadow = (2, 2)
    $ style.blwnfh_settings_underwrites.drop_shadow_color = "#222"
    $ style.blwnfh_settings_underwrites.text_align = 0.5
    $ style.blwnfh_settings_underwrites.yalign = 0.5
    $ style.blwnfh_settings_underwrites.size = 30
    $ style.blwnfh_settings_underwrites.kerning = 1.0
    $ renpy.image("blwnfh_settings_underwrites", ParameterizedText(style="blwnfh_settings_underwrites", size=30))



    
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
    
    
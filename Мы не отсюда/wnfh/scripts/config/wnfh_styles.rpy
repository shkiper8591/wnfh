init -2:
    # Шрифты
    $ style.wnfh_title = Style(style.default)
    $ style.wnfh_title.font = wnfh_FONTS + "Sirius Cursiv.ttf"
    $ style.wnfh_title.color = "#FFF"
    $ style.wnfh_title.drop_shadow = (2, 2)
    $ style.wnfh_title.drop_shadow_color = "#222"
    $ style.wnfh_title.text_align = 0.5
    $ style.wnfh_title.yalign = 0.5
    $ style.wnfh_title.size = 80
    $ style.wnfh_title.kerning = 2.0
    $ renpy.image("wnfh_title", ParameterizedText(style="wnfh_title", size=64))

    $ style.wnfh_ach_title = Style(style.default)
    $ style.wnfh_ach_title.font = wnfh_FONTS + "msjhl.ttc"
    $ style.wnfh_ach_title.color = "#000"
    $ style.wnfh_ach_title.text_align = 0.5
    $ style.wnfh_ach_title.yalign = 0.5
    $ style.wnfh_ach_title.size = 42
    $ style.wnfh_ach_title.kerning = 1.0
    $ renpy.image("wnfh_ach_title", ParameterizedText(style="wnfh_ach_title", size=64))
    
    $ style.wnfh_ach_signature = Style(style.default)
    $ style.wnfh_ach_signature.font = wnfh_FONTS + "msjhl.ttc"
    $ style.wnfh_ach_signature.color = "#000"
    $ style.wnfh_ach_signature.text_align = 0.5
    $ style.wnfh_ach_signature.yalign = 0.5
    $ style.wnfh_ach_signature.size = 38
    $ style.wnfh_ach_signature.kerning = 1.0
    $ renpy.image("wnfh_ach_signature", ParameterizedText(style="wnfh_ach_signature", size=64))
    
    $ style.wnfh_menu = Style(style.default)
    $ style.wnfh_menu.font = wnfh_FONTS + "msjhl.ttc"
    $ style.wnfh_menu.color = "#FFF"
    $ style.wnfh_menu.drop_shadow = (2, 2)
    $ style.wnfh_menu.drop_shadow_color = "#222"
    $ style.wnfh_menu.text_align = 0.5
    $ style.wnfh_menu.yalign = 0.5
    $ style.wnfh_menu.size = 42
    $ style.wnfh_menu.kerning = 1.0
    $ renpy.image("wnfh_menu", ParameterizedText(style="wnfh_menu", size=64))

    $ style.wnfh_splashes = Style(style.default)
    $ style.wnfh_splashes.font = wnfh_FONTS + "vcr_osd.ttf"
    $ style.wnfh_splashes.color = "#FFFF00"
    $ style.wnfh_splashes.drop_shadow = (2, 2)
    $ style.wnfh_splashes.drop_shadow_color = "#222"
    $ style.wnfh_splashes.text_align = 0.5
    $ style.wnfh_splashes.size = 20
    $ renpy.image("wnfh_splashes", ParameterizedText(style="wnfh_splashes", size=64))

    
    $ style.wnfh_settings = Style(style.default)
    $ style.wnfh_settings.font = wnfh_FONTS + "AlumniSansPinstripe-Regular.ttf"
    $ style.wnfh_settings.color = "#FFF"
    $ style.wnfh_settings.text_align = 0.0
    $ style.wnfh_settings.drop_shadow = (2, 2)
    $ style.wnfh_settings.drop_shadow_color = "#222"
    $ style.wnfh_settings.text_align = 0.5
    $ style.wnfh_settings.yalign = 0.5
    $ style.wnfh_settings.size = 30
    $ style.wnfh_settings.kerning = 1.0
    $ renpy.image("wnfh_settings", ParameterizedText(style="wnfh_settings", size=30))

    $ style.wnfh_settings_underwrites = Style(style.default)
    $ style.wnfh_settings_underwrites.font = wnfh_FONTS + "IntroDemo-BlackCAPS.otf"
    $ style.wnfh_settings_underwrites.color = "#FFF"
    $ style.wnfh_settings_underwrites.text_align = 0.0
    $ style.wnfh_settings_underwrites.drop_shadow = (2, 2)
    $ style.wnfh_settings_underwrites.drop_shadow_color = "#222"
    $ style.wnfh_settings_underwrites.text_align = 0.5
    $ style.wnfh_settings_underwrites.yalign = 0.5
    $ style.wnfh_settings_underwrites.size = 30
    $ style.wnfh_settings_underwrites.kerning = 1.0
    $ renpy.image("wnfh_settings_underwrites", ParameterizedText(style="wnfh_settings_underwrites", size=30))



    
    $ style.wnfh_choice_day = Style(style.default)
    $ style.wnfh_choice_day.font = wnfh_FONTS + "IntroDemo-BlackCAPS.otf"
    $ style.wnfh_choice_day.color = "#E2C778"
    $ style.wnfh_choice_day.drop_shadow = (3, 3)
    $ style.wnfh_choice_day.drop_shadow_color = "#000"
    $ style.wnfh_choice_day.text_align = 0.5
    $ style.wnfh_choice_day.yalign = 0.5
    $ style.wnfh_choice_day.size = 30
    $ style.wnfh_choice_day.kerning = 1.0
    $ renpy.image("wnfh_choice_day", ParameterizedText(style="wnfh_choice_day", size=40))
    
    $ style.wnfh_choice_sunset = Style(style.default)
    $ style.wnfh_choice_sunset.font = wnfh_FONTS + "IntroDemo-BlackCAPS.otf"
    $ style.wnfh_choice_sunset.color = "#DCD168"
    $ style.wnfh_choice_sunset.drop_shadow = (3, 3)
    $ style.wnfh_choice_sunset.drop_shadow_color = "#000"
    $ style.wnfh_choice_sunset.text_align = 0.5
    $ style.wnfh_choice_sunset.yalign = 0.5
    $ style.wnfh_choice_sunset.size = 30
    $ style.wnfh_choice_sunset.kerning = 1.0
    $ renpy.image("wnfh_choice_sunset", ParameterizedText(style="wnfh_choice_sunset", size=40))
    
    $ style.wnfh_choice_night = Style(style.default)
    $ style.wnfh_choice_night.font = wnfh_FONTS + "IntroDemo-BlackCAPS.otf"
    $ style.wnfh_choice_night.color = "#3CCFA2"
    $ style.wnfh_choice_night.drop_shadow = (3, 3)
    $ style.wnfh_choice_night.drop_shadow_color = "#000"
    $ style.wnfh_choice_night.text_align = 0.5
    $ style.wnfh_choice_night.yalign = 0.5
    $ style.wnfh_choice_night.size = 30
    $ style.wnfh_choice_night.kerning = 1.0
    $ renpy.image("wnfh_choice_night", ParameterizedText(style="wnfh_choice_night", size=40))
    
    $ style.wnfh_choice_prologue = Style(style.default)
    $ style.wnfh_choice_prologue.font = wnfh_FONTS + "IntroDemo-BlackCAPS.otf"
    $ style.wnfh_choice_prologue.color = "#98D8DA"
    $ style.wnfh_choice_prologue.drop_shadow = (3, 3)
    $ style.wnfh_choice_prologue.drop_shadow_color = "#000"
    $ style.wnfh_choice_prologue.text_align = 0.5
    $ style.wnfh_choice_prologue.yalign = 0.5
    $ style.wnfh_choice_prologue.size = 30
    $ style.wnfh_choice_prologue.kerning = 1.0
    $ renpy.image("wnfh_choice_prologue", ParameterizedText(style="wnfh_choice_prologue", size=40))
    
    
    $ style.wnfh_choice_text_day = Style(style.default)
    $ style.wnfh_choice_text_day.font = wnfh_FONTS + "IntroDemo-BlackCAPS.otf"
    $ style.wnfh_choice_text_day.color = "#E2C778"
    $ style.wnfh_choice_text_day.drop_shadow = (3, 3)
    $ style.wnfh_choice_text_day.drop_shadow_color = "#000"
    $ style.wnfh_choice_text_day.text_align = 0.5
    $ style.wnfh_choice_text_day.yalign = 0.5
    $ style.wnfh_choice_text_day.size = 40
    $ style.wnfh_choice_text_day.kerning = 1.0
    $ renpy.image("wnfh_choice_text_day", ParameterizedText(style="wnfh_choice_text_day", size=40))
    
    $ style.wnfh_choice_text_sunset = Style(style.default)
    $ style.wnfh_choice_text_sunset.font = wnfh_FONTS + "IntroDemo-BlackCAPS.otf"
    $ style.wnfh_choice_text_sunset.color = "#DCD168"
    $ style.wnfh_choice_text_sunset.drop_shadow = (3, 3)
    $ style.wnfh_choice_text_sunset.drop_shadow_color = "#000"
    $ style.wnfh_choice_text_sunset.text_align = 0.5
    $ style.wnfh_choice_text_sunset.yalign = 0.5
    $ style.wnfh_choice_text_sunset.size = 40
    $ style.wnfh_choice_text_sunset.kerning = 1.0
    $ renpy.image("wnfh_choice_text_sunset", ParameterizedText(style="wnfh_choice_text_sunset", size=40))
    
    $ style.wnfh_choice_text_night = Style(style.default)
    $ style.wnfh_choice_text_night.font = wnfh_FONTS + "IntroDemo-BlackCAPS.otf"
    $ style.wnfh_choice_text_night.color = "#3CCFA2"
    $ style.wnfh_choice_text_night.drop_shadow = (3, 3)
    $ style.wnfh_choice_text_night.drop_shadow_color = "#000"
    $ style.wnfh_choice_text_night.text_align = 0.5
    $ style.wnfh_choice_text_night.yalign = 0.5
    $ style.wnfh_choice_text_night.size = 40
    $ style.wnfh_choice_text_night.kerning = 1.0
    $ renpy.image("wnfh_choice_text_night", ParameterizedText(style="wnfh_choice_text_night", size=40))
    
    $ style.wnfh_choice_text_prologue = Style(style.default)
    $ style.wnfh_choice_text_prologue.font = wnfh_FONTS + "IntroDemo-BlackCAPS.otf"
    $ style.wnfh_choice_text_prologue.color = "#98D8DA"
    $ style.wnfh_choice_text_prologue.drop_shadow = (3, 3)
    $ style.wnfh_choice_text_prologue.drop_shadow_color = "#000"
    $ style.wnfh_choice_text_prologue.text_align = 0.5
    $ style.wnfh_choice_text_prologue.yalign = 0.5
    $ style.wnfh_choice_text_prologue.size = 40
    $ style.wnfh_choice_text_prologue.kerning = 1.0
    $ renpy.image("wnfh_choice_text_prologue", ParameterizedText(style="wnfh_choice_text_prologue", size=40))

    $ style.wnfh_thought = Style(style.default)
    $ style.wnfh_thought.drop_shadow = (2, 2)
    $ style.wnfh_thought.drop_shadow_color = "#000"
    $ style.wnfh_thought.text_align = 0.5
    $ renpy.image("wnfh_thought", ParameterizedText(style="wnfh_thought", size=40))
    
    
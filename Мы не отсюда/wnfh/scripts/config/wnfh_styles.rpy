init -2:
    style wnfh_text:
        font wnfh_FONTS + "IntroDemo-BlackCAPS.otf"
        color "#FFFFFF"
        outlines [(0, "#000", 3, 3)]
        yoffset 1
        text_align 0.5
        align (0.5, 0.5)
        size 30
        kerning 1.0
        layout "tex"

    style wnfh_title_1 is wnfh_text:
        yoffset 7
        size 100

    style wnfh_title_2 is wnfh_text:
        yoffset 4
        size 50

    style wnfh_ach_title_1 is wnfh_text:
        text_align 0.0
        min_width 390
        yoffset 4
        size 20

    style wnfh_ach_title_2 is wnfh_text:
        text_align 0.0
        min_width 340
        yoffset 4
        size 15

    style wnfh_lp_counter:
        color "#FFFFFF"
        outlines [(0, "#000", 3, 3)]
        yoffset 1
        text_align 0.5
        align (0.5, 0.5)
        size 70
        kerning 1.0
        layout "tex"
    
    style wnfh_measure_unit is wnfh_text:
        size 15
        align (0.0, 0.5)

    style wnfh_text_day is wnfh_text:
        color wnfh_tint_color["day"][0]
    style wnfh_text_sunset is wnfh_text:
        color wnfh_tint_color["sunset"][0]
    style wnfh_text_night is wnfh_text:
        color wnfh_tint_color["night"][0]
    style wnfh_text_rain is wnfh_text:
        color wnfh_tint_color["rain"][0]
    style wnfh_text_prologue is wnfh_text:
        color wnfh_tint_color["prologue"][0]
    
    style wnfh_title_1_day is wnfh_title_1:
        color wnfh_tint_color["day"][0]
    style wnfh_title_1_sunset is wnfh_title_1:
        color wnfh_tint_color["sunset"][0]
    style wnfh_title_1_night is wnfh_title_1:
        color wnfh_tint_color["night"][0]
    style wnfh_title_1_rain is wnfh_title_1:
        color wnfh_tint_color["rain"][0]
    style wnfh_title_1_prologue is wnfh_title_1:
        color wnfh_tint_color["prologue"][0]

    style wnfh_title_2_day is wnfh_title_2:
        color wnfh_tint_color["day"][0]
    style wnfh_title_2_sunset is wnfh_title_2:
        color wnfh_tint_color["sunset"][0]
    style wnfh_title_2_night is wnfh_title_2:
        color wnfh_tint_color["night"][0]
    style wnfh_title_2_rain is wnfh_title_2:
        color wnfh_tint_color["rain"][0]
    style wnfh_title_2_prologue is wnfh_title_2:
        color wnfh_tint_color["prologue"][0]

    style wnfh_ach_title_1_day is wnfh_ach_title_1:
        color wnfh_tint_color["day"][0]
    style wnfh_ach_title_1_sunset is wnfh_ach_title_1:
        color wnfh_tint_color["sunset"][0]
    style wnfh_ach_title_1_night is wnfh_ach_title_1:
        color wnfh_tint_color["night"][0]
    style wnfh_ach_title_1_rain is wnfh_ach_title_1:
        color wnfh_tint_color["rain"][0]
    style wnfh_ach_title_1_prologue is wnfh_ach_title_1:
        color wnfh_tint_color["prologue"][0]

    style wnfh_ach_title_2_day is wnfh_ach_title_2:
        color wnfh_tint_color["day"][0]
    style wnfh_ach_title_2_sunset is wnfh_ach_title_2:
        color wnfh_tint_color["sunset"][0]
    style wnfh_ach_title_2_night is wnfh_ach_title_2:
        color wnfh_tint_color["night"][0]
    style wnfh_ach_title_2_rain is wnfh_ach_title_2:
        color wnfh_tint_color["rain"][0]
    style wnfh_ach_title_2_prologue is wnfh_ach_title_2:
        color wnfh_tint_color["prologue"][0]

    style wnfh_measure_unit_day is wnfh_measure_unit:
        color wnfh_tint_color["day"][0]
    style wnfh_measure_unit_sunset is wnfh_measure_unit:
        color wnfh_tint_color["sunset"][0]
    style wnfh_measure_unit_night is wnfh_measure_unit:
        color wnfh_tint_color["night"][0]
    style wnfh_measure_unit_rain is wnfh_measure_unit:
        color wnfh_tint_color["rain"][0]
    style wnfh_measure_unit_prologue is wnfh_measure_unit:
        color wnfh_tint_color["prologue"][0]
    

    style wnfh_buttons is wnfh_text:
        background None
        hover_sound wnfh_gui["sound"]["plimp"]

    style wnfh_splashs is wnfh_text:
        size 20











    style wnfh_choice_day is wnfh_text:
        color wnfh_choice_tint_color["day"][0]
    style wnfh_choice_sunset is wnfh_text:
        color wnfh_choice_tint_color["sunset"][0]
    style wnfh_choice_night is wnfh_text:
        color wnfh_choice_tint_color["night"][0]
    style wnfh_choice_prologue is wnfh_text:
        color wnfh_choice_tint_color["prologue"][0]


    $ style.wnfh_thought = Style(style.default)
    $ style.wnfh_thought.drop_shadow = (2, 2)
    $ style.wnfh_thought.drop_shadow_color = "#000"
    $ style.wnfh_thought.text_align = 0.5
    $ renpy.image("wnfh_thought", ParameterizedText(style="wnfh_thought", size=40))
    
    
    
label ESPE_menu:
    $ renpy.block_rollback()
    scene black
    call screen ESPE_main_menu_screen() with Fade(0.5, 0.0, 0.5)

screen ESPE_main_menu_screen():
    fixed:
        add Solid("#292929", xsize=250, ysize=1.0) at fast_align(0.5, 0.5)
        add Solid("#292929"):
            at transform:
                fast_align(0.5, 0.5)
                blur_light(0.2, 10, 15)
     
    use ESPE_main_menu_buttons()

screen ESPE_main_menu_buttons():
    vbox:
        xalign 0.5
        yalign 0.5
        first_spacing 100
        spacing 20

        text "Редактор частиц для бесконечного лета\n─── ⋆⋅☆⋅⋆ ───" xmaximum 480 style "espe_text_heading_36"

        textbutton "Перейти в редактор" xmaximum 250 style "espe_button" text_style "espe_button_text_24" text_size 22:
            action [Show("ESPE_smooth_transition", label="ESPE_editor_label", transition=Fade(0.5, 0.0, 0.5))]
        textbutton "Документация" xmaximum 240 style "espe_button" text_style "espe_button_text_24"

        textbutton "Выход в меню игры" xmaximum 240 style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_smooth_exit", transition=Pixellate(0.5, 4))]
        textbutton "Выход из игры" xmaximum 240 style "espe_button" text_style "espe_button_text_24":
            action [Show("ESPE_smooth_exit", is_quit=True, transition=Fade(0.5, 0.0, 0.5))]

screen ESPE_smooth_transition(label):
    add "black"

    timer 0.5 action [Hide("ESPE_smooth_transition"), Jump(label)]

screen ESPE_smooth_exit(is_quit=False):
    add "black"

    if not is_quit:
        timer 1.0 action [Function(ESPE_set_es_settings), MainMenu(False, False)]
    else:
        timer 1.0 action [Quit(False)]
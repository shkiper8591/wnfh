##Экраны буквально на +-20 строк.##

##Показывает спрайт и его размер.##
screen ESPE_particle_displayable_subscreen(displayable):
    tag espe_editor_subscreen

    add Solid("#000", xsize=240, ysize=240) at fast_pos_05anchor_alpha(0.8, 0.5, 0.8)

    add displayable at fast_pos_05anchor(0.8, 0.5)

    vbox:
        xanchor 0.5
        xpos 0.8
        ypos 0.615
        text espe_properties_divider_huge style "espe_text_24"
        text "Ш:{}, В:{}".format(*espe_get_displayable_size(displayable)) style "espe_text_24"

##*Экраны для показа частиц.*##
screen ESPE_editor_simple_particles_show():
    layer "master"
    zorder 10
    
    add ESPE_simple_particles_manager

screen ESPE_editor_complex_particles_show():
    layer "master"
    zorder 10

    add ESPE_complex_particles_manager
##*.........................*##

##Всплывающее уведомление о выбранной системе частиц.##
screen ESPE_psystem_type_notify(simple):
    tag espe_psystem_type_screen

    $ text_notify = "Простые частицы!"
    if not simple:
        $ text_notify = "Сложные частицы!"

    add Solid("#000", xsize=0.3, ysize=0.1) at fast_align_alpha(0.5, 0.5, 0.5)

    text text_notify xmaximum 0.3 style "espe_text_heading_36" at fast_align(0.5, 0.5)

    timer 1.5 action Hide("ESPE_psystem_type_notify", transition=Dissolve(0.5))

##Экран подсказок.##
screen ESPE_editor_hint(hint):
    zorder 100

    frame: 
        at fast_pos_05anchor(0.36, 0.5)

        xpadding 5
        ypadding 5
        xmaximum 384
        background "#00000066"

        text hint style "espe_text_24" text_align 0.0

##Экран подсказок для экранов генерации кода.##
screen ESPE_editor_hint_code_generate(hint, image_hint=None):
    zorder 100

    vbox:
        at fast_pos_05anchor(0.15, 0.5)

        frame: 
            xpadding 5
            ypadding 5
            xmaximum 384
            background "#00000066"

            text hint style "espe_text_24" text_align 0.0

        if image_hint is not None:
            add image_hint
        
label ESPE_load_scene_from_file:
    if espe_load_scene_from_file(espe_special_label_data):
        show screen ESPE_saved_loaded_notify(is_save=False)
    else:
        call screen ESPE_load_scene_fail()

    call screen ESPE_scene_editor_main()

label ESPE_load_psystem_from_file:
    if espe_load_psystem_from_file(espe_special_label_data):
        show screen ESPE_saved_loaded_notify(is_save=False)
    else:
        call screen ESPE_load_psystem_fail()

    call screen ESPE_editor_main_menu()

label smooth_exit_to_main_menu:
    if espe_editor_data.psystem_screen is not None:
        $ renpy.hide_screen(espe_editor_data.psystem_screen)

    $ espe_particles_show = True

    $ renpy.hide_screen("espe_editor_main")

    scene black
    with dissolve
    jump ESPE_menu
init:
    $ mods["ESPE_init_label"]=u"Редактор частиц!"
    #$ config.developer = True

init 100:
    $ ESPE_set_espe_settings()

    $ espe_editor_data = ESPEEditorData()
    $ espe_scene_editor_data = ESPESceneEditorData()

    $ espe_ov = ESPEOptimizedValues()

    $ ESPE_complex_particles_manager = SpriteManager(espe_psystem_complex_update)
    $ ESPE_complex_particles = espe_init_editor_psystem_complex()

    $ ESPE_simple_particles_manager = SpriteManager(espe_psystem_simple_update)
    $ ESPE_simple_particles = espe_init_editor_psystem_simple()

    $ is_chosen_psystem = False

    $ espe_particles_show = True
    $ espe_position_picker_enable = False
    $ espe_fps_counter_enable = False

label ESPE_init_label:
    # $ ESPE_set_espe_settings()

    # $ espe_list_files(directory=espe_scenes_dir, extension=".scene", dict_to_save=espe_scene_saves_dict)
    # $ espe_list_files(directory=espe_psystems_dir, extension=".psystem", dict_to_save=espe_psystem_saves_dict)

    # $ espe_editor_data = ESPEEditorData()
    # $ espe_scene_editor_data = ESPESceneEditorData()

    # $ espe_ov = ESPEOptimizedValues()
    
    # $ ESPE_complex_particles_manager = SpriteManager(espe_psystem_complex_update)
    # $ ESPE_complex_particles = espe_init_editor_psystem_complex()

    # #$ ESPE_complex_particles_manager = SpriteManager(espe_psystem_simple_update)
    # $ ESPE_simple_particles = None

    jump ESPE_menu
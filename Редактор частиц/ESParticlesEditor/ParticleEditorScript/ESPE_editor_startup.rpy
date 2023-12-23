label ESPE_editor_label:
    $ espe_list_scenes_files()
    $ espe_list_psystem_files()

    $ espe_special_label_data = None #Костыль :(.

    $ renpy.block_rollback()

    $ is_chosen_psystem = True if espe_editor_data.psystem_object is not None else False

    scene black

    show screen ESPE_scene(espe_scene_editor_data)
    show screen ESPE_editor_extra(True)

    if is_chosen_psystem:
        $ espe_editor_psystem_deep_reset()
        show screen ESPE_editor_main_menu()
    else:
        show screen ESPE_editor_menu_startup()
    with Dissolve(0.5)

    call screen ESPE_screen_holder()

    "Если ты прочитал это сообщение, значит, редактор накрылся :( Перезайдите в игру. Возможно, вы можете что-то ещё понажимать, но это маловероятно. Одна кнопка и вы окажетесь в главном менб БЛ :(."
init python:
    import os

    def espe_get_workshop_mod_directory():
        directory = os.path.dirname(os.path.abspath(__file__))
        for _ in range(3):
            directory = os.path.dirname(directory)
        directory = os.path.join(directory, "workshop\\content\\331470\\{}\\ESParticlesEditor".format(ESPE_MOD_ID))

        return directory

    espe_max_filesize = 10240 #Байт.
    #espe_main_dir = os.path.dirname(os.path.abspath(__file__))
    #espe_main_dir = os.path.join(os.path.dirname(espe_main_dir), "game\ESParticlesEditor") #ДЛЯ ГОТОВОЙ ВЕРСИИ.#
    #espe_main_dir = "C:\Games\Everlasting Summer SDK\game\mods\ESParticlesEditor" #os.path.join(os.path.dirname(espe_main_dir), "C:\Games\Everlasting Summer SDK\game\mods\ESParticlesEditor") #Каталог ESPrticleEditor.
    #espe_scenes_dir = os.path.join(espe_main_dir, "Scenes")
    #espe_psystems_dir = os.path.join(espe_main_dir, "ParticleSystems")
    
    #ДЛЯ WORKSHOP ВЕРСИИ.#
    ESPE_MOD_ID = 3115516302
    espe_main_dir = espe_get_workshop_mod_directory()
    espe_scenes_dir = espe_main_dir+"\\Scenes"
    espe_psystems_dir = espe_main_dir+"\\ParticleSystems"
    
    espe_scene_saves_dict = { }
    espe_psystem_saves_dict = { }

    def espe_open_mod_directory():
        os.startfile(espe_main_dir)

    def espe_list_scenes_files():
        store.espe_scene_saves_dict.clear()

        for system_filename in os.listdir(store.espe_scenes_dir):
            if system_filename.endswith(".scene"):
                file_path = os.path.join(store.espe_scenes_dir, system_filename)
                if os.path.getsize(file_path) <= espe_max_filesize:
                    with open(file_path, "r") as file:
                        filename = ESPEFileParser.get_filename(file)
                        if filename is not None:
                            store.espe_scene_saves_dict[filename] = file_path

    def espe_list_psystem_files():
        store.espe_psystem_saves_dict.clear()

        for system_filename in os.listdir(store.espe_psystems_dir):
            if system_filename.endswith(".psystem"):
                file_path = os.path.join(store.espe_psystems_dir, system_filename)
                if os.path.getsize(file_path) <= espe_max_filesize:
                    with open(file_path, "r") as file:
                        filename = ESPEFileParser.get_filename(file)
                        if filename is not None:
                            store.espe_psystem_saves_dict[filename] = file_path

    def espe_check_file_on_exist(filename, saves_dict):
        if saves_dict.get(filename, None) is None:
            return False
        return True

    def espe_save_scene(filename):
        system_filename = espe_get_system_filename(filename, ".scene")

        file_path = os.path.join(store.espe_scenes_dir, system_filename)

        with open(file_path, "w") as file:
            ESPEFileWriter.save_scene_data(file, filename, espe_scene_editor_data)
        
        store.espe_scene_saves_dict[filename] = file_path
    
    def espe_save_psystem(filename):
        system_filename = espe_get_system_filename(filename, ".psystem")

        file_path = os.path.join(store.espe_psystems_dir, system_filename)

        with open(file_path, "w") as file:
            ESPEFileWriter.save_psystem_data(file, filename, espe_editor_data)
        
        store.espe_psystem_saves_dict[filename] = file_path

    def espe_get_data_from_scene_file(filepath):
        file_data = None

        with open(filepath, "r") as file:
            file_data = ESPEFileParser.get_scene_data_from_file(file)

        if file_data is None:
            return None
        
        return file_data

    def espe_load_scene_from_file(filepath):
        file_data = None

        with open(filepath, "r") as file:
            file_data = ESPEFileParser.get_scene_data_from_file(file)

        if file_data is None:
            return False

        espe_scene_editor_data.set_data(file_data)
        return True

    def espe_load_scene_from_data(data):
        espe_scene_editor_data.set_data(data)

    def espe_get_data_from_psystem_file(filepath):
        file_data = None

        with open(filepath, "r") as file:
            file_data = ESPEFileParser.get_particle_system_data_from_file(file)

        if file_data is None:
            return None
        
        return file_data

    def espe_load_psystem_from_file(filepath):
        file_data = None

        with open(filepath, "r") as file:
            file_data = ESPEFileParser.get_particle_system_data_from_file(file)

        if file_data is None:
            return False

        espe_editor_data.set_data(file_data)
        return True

    def espe_load_psystem_from_data(data):
        espe_editor_data.set_data(data)

    def espe_get_system_filename(filename, extension):
        system_filename = ""
        for symb in filename:
            if not symb in store.espe_eng_alphabet + store.espe_digits_table:
                system_filename += store.espe_rus_alphabet.get(symb, '')
            else:
                system_filename += symb

        system_filename += extension
        
        return system_filename

screen ESPE_saved_loaded_notify(is_save):
    tag espe_scene_save_load_notify

    $ text_notify = "Сохранено!"
    if not is_save:
        $ text_notify = "Загружено!"

    add Solid("#000", xsize=0.3, ysize=0.1) at fast_align_alpha(0.5, 0.5, 0.5)

    text text_notify xmaximum 0.3 style "espe_text_heading_36" at fast_align(0.5, 0.5)

    timer 1.5 action Hide("ESPE_saved_loaded_notify", transition=Dissolve(0.5))
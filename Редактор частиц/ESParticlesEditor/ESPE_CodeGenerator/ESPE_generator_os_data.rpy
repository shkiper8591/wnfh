init 200 python:
    import os

    espe_compiled_psystems_dir = os.path.join(espe_main_dir, "CompiledPsystems")

    def espe_is_psystem_not_exist(filename):
        folder_name = "ESPE_" + espe_get_system_filename(filename, "_folder")
        psystem_path = os.path.join(espe_compiled_psystems_dir, folder_name)
        
        if not os.path.isdir(psystem_path):
            return True

        return False

    def espe_generate_psystem(filename):
        folder_name = "ESPE_" + espe_get_system_filename(filename, "_folder")
        psystem_path = os.path.join(espe_compiled_psystems_dir, folder_name)
        filename_ext = "ESPE_" + espe_get_system_filename(filename, ".txt")
        filepath = os.path.join(psystem_path, filename_ext)

        if not os.path.isdir(psystem_path):
            os.mkdir(psystem_path)
            ESPECodeGenerator.init_func_dict()
            ESPECodeGenerator.reset_generator()
            ESPECodeGenerator.analize_psystem()
            ESPECodeGenerator.PSYSTEM_CODE_NAME = filename

            with open(filepath, "w") as file:
                ESPECodeGenerator.generate_psystem(file)
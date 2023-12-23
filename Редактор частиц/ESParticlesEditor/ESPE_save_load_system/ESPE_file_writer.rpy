init 5 python:
    class ESPEFileWriter(renpy.object.Object):
        #Сцена.#
        background_properties = [
            "background_displayable",
            "xoffset",
            "yoffset",
            "alpha",
            "zoom",
            "rotate_angle"
        ]

        audio_properties = [
            "music_name",
            "music_src",
            "ambience_name",
            "ambience_src"
        ]

        sprite_general = [
            "sprites_amount"
        ]

        sprite_properties = [
            "sprite_special_name",
            "sprite_displayable",
            "tint_name",
            "tint_index",
            "xoffset",
            "yoffset",
            "alpha",
            "zoom",
            "rotate_angle",
            "zorder",
        ]
        #######

        #Система частиц.#
        editor_properties = [
            "psystem_type",
            "psystem_screen"
        ]

        name_properties = [
            "psystem_name"
        ]

        sprites_psystem_properties = [
            "p_displayable_list",
            "p_displayable_names"
        ]

        amount_properties = [
            "p_amount"
        ]

        lifetime_properties = [
            "p_lifetime",
            "p_lifetime_random_enable",
            "p_lifetime_random",
            "p_lifetime_spread",
            "p_lifetime_random_spread_enable",
            "p_lifetime_spread_random"
        ]

        explosiveness_properties = [
            "p_is_explosiveness",
            "p_explosiveness_factor",
            "p_explosiveness_amount"
        ]

        emitter_type_properties = [
            "p_spawn_area_type",
            "p_emitter_pos",
            "p_rectangle_emitter_pos",
            "p_rectangle_spawn_area",
            "p_radial_emitter_pos",
            "p_emitter_radius",
            "p_out_of_bounds_spawn_dict"
        ]

        movement_properties = [
            "p_move_type",
            "p_speed_simple_move_changer_type",
            "p_speed_accelerate_move_changer_type",
            "p_acc_accelerate_move_changer_type",
            "p_max_x_speed",
            "p_min_x_speed",
            "p_max_y_speed",
            "p_min_y_speed",
            "p_max_x_accelerate",
            "p_min_x_accelerate",
            "p_max_y_accelerate",
            "p_min_y_accelerate"
        ]

        extra_movement_properties = [
            "p_move_extra_type",
            "p_speed_extra_changer_type",
            "p_radius_oscillatory_changer_type",
            "p_random_start_phase",
            "p_max_speed_oscillatory",
            "p_min_speed_oscillatory",
            "p_extra_phase",
            "p_max_x_oscillatory",
            "p_min_x_oscillatory",
            "p_max_y_oscillatory",
            "p_min_y_oscillatory"
        ]

        alpha_properties = [
            "p_alpha_type",
            "p_alpha_changer_static_type",
            "p_alpha_changer_fade_in_out_type",
            "p_alpha_changer_oscillatory_type",
            "p_alpha_changer_oscillatory_speed_type",
            "p_alpha_changer_oscillatory_phase_type",
            "p_intermediate_max_alpha",
            "p_intermediate_min_alpha",
            "p_alpha_appear_time_percentage",
            "p_alpha_disappear_time_percentage",
            "p_alpha_max_speed",
            "p_alpha_min_speed",
            "p_alpha_phase"
        ]

        scale_properties = [
            "p_zoom_type",
            "p_zoom_changer_static_type",
            "p_zoom_changer_fade_in_out_type",
            "p_zoom_changer_oscillatory_type",
            "p_zoom_changer_oscillatory_speed_type",
            "p_zoom_changer_oscillatory_phase_type",
            "p_intermediate_max_zoom",
            "p_intermediate_min_zoom",
            "p_zoom_appear_time_percentage",
            "p_zoom_disappear_time_percentage",
            "p_zoom_max_speed",
            "p_zoom_min_speed",
            "p_zoom_phase"
        ]

        rotate_properties = [
            "p_rotate_type",
            "p_rotate_changer_static_type",
            "p_dynamic_rotate_changer_angle_type",
            "p_dynamic_rotate_changer_speed_type",
            "p_max_angle",
            "p_min_angle",
            "p_dynamic_rotate_max_start_angle",
            "p_dynamic_rotate_min_start_angle",
            "p_dynamic_rotate_max_speed",
            "p_dynamic_rotate_min_speed",
            "p_rotate_by_speed_type",
            "p_rotate_by_speed_start_angle",
            "p_rotate_by_speed_max_speed"
        ]

        optimization_properties = [
            "p_inner_frame_check",
            "p_fixed_dtime",
            "p_update_time",
            "p_is_screen_bounded"
        ]
        #################

        @staticmethod
        def save_scene_data(file, filename, scene_editor_data_object):
            scene_data = scene_editor_data_object.get_data()
          
            #Имя.#
            file.write(ESPEFileParser.FILENAME_LABEL + '\n')
            file.write("filename={}\n".format(filename))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ######

            #Данные фона.#
            file.write(ESPEFileParser.BACKGROUND_LABEL + '\n')
            for prop_name, prop_value in zip(ESPEFileWriter.background_properties, scene_data[0]):
                file.write("{}={}\n".format(prop_name, prop_value))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ##############

            #Данные звуковой сцены.#
            file.write(ESPEFileParser.AUDIO_LABEL + '\n')
            for prop_name, prop_value in zip(ESPEFileWriter.audio_properties, scene_data[1]):
                file.write("{}={}\n".format(prop_name, prop_value))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ########################

            #Данные спрайтов.#
            file.write(ESPEFileParser.SPRITES_LABEL + '\n')
            file.write("{}={}\n".format(ESPEFileWriter.sprite_general[0], scene_data[2][0]))

            if scene_data[3]:
                for sprite_data in scene_data[3]:
                    file.write('\n')
                    file.write(ESPEFileParser.SPRITE_LABEL + '\n')
                    for prop_name, prop_value in zip(ESPEFileWriter.sprite_properties, sprite_data):
                        file.write("{}={}\n".format(prop_name, prop_value))
                    file.write(ESPEFileParser.SPRITE_END_LABEL + '\n')
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            ##################

            #Конец файла.#
            file.write(ESPEFileParser.END_FILE_LABEL)
            ##############

            return True
        
        @staticmethod
        def save_psystem_data(file, filename, particle_editor_data_object):
            psystem_data = particle_editor_data_object.get_data()

            #Имя.#
            file.write(ESPEFileParser.FILENAME_LABEL + '\n')
            file.write("filename={}\n".format(filename))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ######

            #Данные редактора.#
            file.write(ESPEFileParser.EDITOR_LABEL + '\n')
            for prop_name, prop_value in zip(ESPEFileWriter.editor_properties, psystem_data[0]):
                file.write("{}={}\n".format(prop_name, prop_value))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ##############

            #Имя.#
            file.write(ESPEFileParser.NAME_LABEL + '\n')
            for prop_name, prop_value in zip(ESPEFileWriter.name_properties, psystem_data[1]):
                file.write("{}={}\n".format(prop_name, prop_value))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ##############

            #Данные спрайтов.#
            file.write(ESPEFileParser.SPRITES_LABEL + '\n')
            for prop_name, prop_value in zip(ESPEFileWriter.sprites_psystem_properties, psystem_data[2]):
                ##Пиздец ебаный.##
                file.write("{}={}\n".format(prop_name, str(prop_value).replace('[', '(').replace(']', ')').decode('unicode-escape').replace('u(', '(').replace('(u', '(').replace('u\'', '').replace('\'', '')))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ##############

            #Количество.#
            file.write(ESPEFileParser.AMOUNT_LABEL + '\n')
            for prop_name, prop_value in zip(ESPEFileWriter.amount_properties, psystem_data[3]):
                file.write("{}={}\n".format(prop_name, prop_value))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ##############

            #Время жизни.#
            file.write(ESPEFileParser.LIFETIME_LABEL + '\n')
            for prop_name, prop_value in zip(ESPEFileWriter.lifetime_properties, psystem_data[4]):
                file.write("{}={}\n".format(prop_name, prop_value))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ##############

            #Взрывчатость.#
            file.write(ESPEFileParser.EXPLOSIVENESS_LABEL + '\n')
            for prop_name, prop_value in zip(ESPEFileWriter.explosiveness_properties, psystem_data[5]):
                file.write("{}={}\n".format(prop_name, prop_value))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ##############

            #Тип испускания.#
            file.write(ESPEFileParser.EMITTER_TYPE_LABEL + '\n')
            for prop_name, prop_value in zip(ESPEFileWriter.emitter_type_properties, psystem_data[6]):
                if prop_name == "p_out_of_bounds_spawn_dict":
                    correct_str = str(["({}: {})".format(key, value) for key, value in prop_value.items()])[1:-1].replace('\'', '').replace('u(', '(')
                    file.write("{}={}\n".format(prop_name, correct_str))
                else:
                    file.write("{}={}\n".format(prop_name, prop_value))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ##############

            #Движение.#
            file.write(ESPEFileParser.MOVEMENT_LABEL + '\n')
            for prop_name, prop_value in zip(ESPEFileWriter.movement_properties, psystem_data[7]):
                file.write("{}={}\n".format(prop_name, prop_value))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ##############

            #Дополнительное движение.#
            file.write(ESPEFileParser.EXTRA_MOVEMENT_LABEL + '\n')
            for prop_name, prop_value in zip(ESPEFileWriter.extra_movement_properties, psystem_data[8]):
                file.write("{}={}\n".format(prop_name, prop_value))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ##############

            #Непрозрачность.#
            file.write(ESPEFileParser.ALPHA_LABEL + '\n')
            for prop_name, prop_value in zip(ESPEFileWriter.alpha_properties, psystem_data[9]):
                file.write("{}={}\n".format(prop_name, prop_value))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ##############

            #Масшиаб.#
            file.write(ESPEFileParser.SCALE_LABEL + '\n')
            for prop_name, prop_value in zip(ESPEFileWriter.scale_properties, psystem_data[10]):
                file.write("{}={}\n".format(prop_name, prop_value))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ##############

            #Вращение.#
            file.write(ESPEFileParser.ROTATE_LABEL + '\n')
            for prop_name, prop_value in zip(ESPEFileWriter.rotate_properties, psystem_data[11]):
                file.write("{}={}\n".format(prop_name, prop_value))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            file.write('\n')
            ##############

            #Оптимизация.#
            file.write(ESPEFileParser.OPTIMIZATION_LABEL + '\n')
            for prop_name, prop_value in zip(ESPEFileWriter.optimization_properties, psystem_data[12]):
                file.write("{}={}\n".format(prop_name, prop_value))
            file.write(ESPEFileParser.END_CATEGORY_LABEL + '\n')
            ##############

            #Конец файла.#
            file.write(ESPEFileParser.END_FILE_LABEL)
            ##############

            return True
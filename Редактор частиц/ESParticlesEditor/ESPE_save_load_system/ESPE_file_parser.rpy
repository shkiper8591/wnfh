init 5 python:
    import builtins

    class ESPEFileParser(renpy.object.Object):
        #Общее.#
        FILENAME_LABEL = "<FILENAME>"
        SPRITES_LABEL = "<SPRITES>"
        END_CATEGORY_LABEL = "<END>"
        END_FILE_LABEL = "<END_FILE>"
        ########

        #Сцена.#
        BACKGROUND_LABEL = "<BACKGROUND>"
        AUDIO_LABEL = "<AUDIO>"
        SPRITE_LABEL = "<SPRITE>"
        SPRITE_END_LABEL = "<SPRITE_END>"

        #Система частиц.#
        EDITOR_LABEL = "<EDITOR>"
        NAME_LABEL = "<NAME>"
        AMOUNT_LABEL = "<AMOUNT>"
        LIFETIME_LABEL = "<LIFETIME>"
        EXPLOSIVENESS_LABEL = "<EXPLOSIVENESS>"
        EMITTER_TYPE_LABEL = "<EMITTER_TYPE>"
        MOVEMENT_LABEL = "<MOVEMENT>"
        EXTRA_MOVEMENT_LABEL = "<EXTRA_MOVEMENT>"
        ALPHA_LABEL = "<ALPHA>"
        SCALE_LABEL = "<SCALE>"
        ROTATE_LABEL = "<ROTATE>"
        OPTIMIZATION_LABEL = "<OPTIMIZATION>"
        #######

        background_properties = [
            ["background_displayable", str, None],
            ["xoffset", int, (-config.screen_width, config.screen_width)],
            ["yoffset", int, (-config.screen_height, config.screen_height)],
            ["alpha", float, (0.0, 1.0)],
            ["zoom", float, (0.0, 10.0)],
            ["rotate_angle", int, (0, 360)]
        ]

        audio_properties = [
            ["music_name", str, None],
            ["music_src", str, None],
            ["ambience_name", str, None],
            ["ambience_src", str, None]
        ]

        sprite_general = [
            ["sprites_amount", int, None]
        ]

        sprite_properties = [
            ["sprite_special_name", str, None],
            ["sprite_displayable", str, None],
            ["tint_name", str, None],
            ["tint_index", int, (0, len(espe_sprite_tint_list) - 1)],
            ["xoffset", int, (-config.screen_width, config.screen_width)],
            ["yoffset", int, (-config.screen_height, config.screen_height)],
            ["alpha", float, (0.0, 1.0)],
            ["zoom", float, (0.0, 10.0)],
            ["rotate_angle", int, (0, 360)],
            ["zorder", int, (-100, 100)]
        ]
        #######

        #Система частиц.#
        #Сами виноваты будете, если эти параметры в файле тронете :).#
        editor_properties = [
            ["psystem_type", str, None],
            ["psystem_screen", str, None]
            ]
        
        name_properties = [
            ["psystem_name", str, None]
        ]

        #Здесь тоже осторожно, вместе с програмным названием вам надо менять и обычные названия, прописанные как в коде. Т.к. на основе двух этих списков строится словарь.#
        sprites_psystem_properties = [
            ["p_displayable_list", str, None],
            ["p_displayable_names", str, None]
        ]

        amount_properties = [
            ["p_amount", int, (0, 500)]
        ]

        lifetime_properties = [
            ["p_lifetime", float, (0.0, 100.0)],
            ["p_lifetime_random_enable", bool, None],
            ["p_lifetime_random", float, (0.0, 1.0)],
            ["p_lifetime_spread", float, (0.0, 100.0)],
            ["p_lifetime_random_spread_enable", bool, None],
            ["p_lifetime_spread_random", float, (0.0, 1.0)]
        ]

        explosiveness_properties = [
            ["p_is_explosiveness", bool, None],
            ["p_explosiveness_factor", float, (0.0, 1.0)],
            ["p_explosiveness_amount", int, None]
        ]

        emitter_type_properties = [
            ["p_spawn_area_type", int, (0, 4)],
            ["p_emitter_pos", int, (0, config.screen_width)],
            ["p_rectangle_emitter_pos", int, (0, config.screen_width)],
            ["p_rectangle_spawn_area", int, (0, config.screen_width)],
            ["p_radial_emitter_pos", int, (0, config.screen_width)],
            ["p_emitter_radius", int, (0, config.screen_height)],
            ["p_out_of_bounds_spawn_dict", bool, None]
        ]

        movement_properties = [
            ["p_move_type", int, (0, 2)],
            ["p_speed_simple_move_changer_type", bool, None],
            ["p_speed_accelerate_move_changer_type", bool, None],
            ["p_acc_accelerate_move_changer_type", bool, None],
            ["p_max_x_speed", float, (-1000.0, 1000.0)],
            ["p_min_x_speed", float, (-1000.0, 1000.0)],
            ["p_max_y_speed", float, (-1000.0, 1000.0)],
            ["p_min_y_speed", float, (-1000.0, 1000.0)],
            ["p_max_x_accelerate", float, (-100.0, 100.0)],
            ["p_min_x_accelerate", float, (-100.0, 100.0)],
            ["p_max_y_accelerate", float, (-100.0, 100.0)],
            ["p_min_y_accelerate", float, (-100.0, 100.0)]
        ]

        extra_movement_properties = [
            ["p_move_extra_type", int, (0, 1)],
            ["p_speed_extra_changer_type", bool, None],
            ["p_radius_oscillatory_changer_type", bool, None],
            ["p_random_start_phase", bool, None],
            ["p_max_speed_oscillatory", float, (-1000.0, 1000.0)],
            ["p_min_speed_oscillatory", float, (-1000.0, 1000.0)],
            ["p_extra_phase", float, (0.0, 360.0)],
            ["p_max_x_oscillatory", float, (0.0, 1080.0)],
            ["p_min_x_oscillatory", float, (0.0, 1080.0)],
            ["p_max_y_oscillatory", float, (0.0, 1080.0)],
            ["p_min_y_oscillatory", float, (0.0, 1080.0)]
        ]

        alpha_properties = [
            ["p_alpha_type", int, (0, 2)],
            ["p_alpha_changer_static_type", bool, None],
            ["p_alpha_changer_fade_in_out_type", bool, None],
            ["p_alpha_changer_oscillatory_type", bool, None],
            ["p_alpha_changer_oscillatory_speed_type", bool, None],
            ["p_alpha_changer_oscillatory_phase_type", bool, None],
            ["p_intermediate_max_alpha", float, (0.0, 1.0)],
            ["p_intermediate_min_alpha", float, (0.0, 1.0)],
            ["p_alpha_appear_time_percentage", float, (0.0, 1.0)],
            ["p_alpha_disappear_time_percentage", float, (0.0, 1.0)],
            ["p_alpha_max_speed", float, (-1000.0, 1000.0)],
            ["p_alpha_min_speed", float, (-1000.0, 1000.0)],
            ["p_alpha_phase", float, (0.0, 1080.0)]
        ]

        scale_properties = [
            ["p_zoom_type", int, (0, 2)],
            ["p_zoom_changer_static_type", bool, None],
            ["p_zoom_changer_fade_in_out_type", bool, None],
            ["p_zoom_changer_oscillatory_type", bool, None],
            ["p_zoom_changer_oscillatory_speed_type", bool, None],
            ["p_zoom_changer_oscillatory_phase_type", bool, None],
            ["p_intermediate_max_zoom", float, (0.0, 2.5)],
            ["p_intermediate_min_zoom", float, (0.0, 2.5)],
            ["p_zoom_appear_time_percentage", float, (0.0, 1.0)],
            ["p_zoom_disappear_time_percentage", float, (0.0, 1.0)],
            ["p_zoom_max_speed", float, (-1000.0, 1000.0)],
            ["p_zoom_min_speed", float, (-1000.0, 1000.0)],
            ["p_zoom_phase", float, (0.0, 1080.0)]
        ]

        rotate_properties = [
            ["p_rotate_type", int, (0, 2)],
            ["p_rotate_changer_static_type", bool, None],
            ["p_dynamic_rotate_changer_angle_type", bool, None],
            ["p_dynamic_rotate_changer_speed_type", bool, None],
            ["p_max_angle", float, (0.0, 360.0)],
            ["p_min_angle", float, (0.0, 360.0)],
            ["p_dynamic_rotate_max_start_angle", float, (0.0, 360.0)],
            ["p_dynamic_rotate_min_start_angle", float, (0.0, 360.0)],
            ["p_dynamic_rotate_max_speed", float, (-1000.0, 1000.0)],
            ["p_dynamic_rotate_min_speed", float, (-1000.0, 1000.0)],
            ["p_rotate_by_speed_type", int, (0, 1)],
            ["p_rotate_by_speed_start_angle", float, (0.0, 360.0)],
            ["p_rotate_by_speed_max_speed", float, (-1000.0, 1000.0)]
        ]

        optimization_properties = [
            ["p_inner_frame_check", bool, None],
            ["p_fixed_dtime", float, (0.0, 1.0)],
            ["p_update_time", float, (0.0, 1.0)],
            ["p_is_screen_bounded", bool, None]
        ]
        #######

        cycle_scene_editor_attempts = 130
        cycle_particle_editor_attemps = 130

        @staticmethod
        def get_scene_data_from_file(file):
            filename = ESPEFileParser.get_filename(file)
            background_data = ESPEFileParser.get_background_data(file, False)
            audio_data = ESPEFileParser.get_audio_data(file, False)
            general_sprites_data = ESPEFileParser.get_sprites_data(file, False)
            general_sprites_data_list = [ ]
            sprites_data = [ ]

            if None in [filename, background_data, audio_data, general_sprites_data]:
                return None

            if len(general_sprites_data) > 1:
                general_sprites_data_list = [ ] #Если вдруг появятся другие свойства. Но да, это мега-костыль.
                sprites_data = general_sprites_data[1:]
            general_sprites_data_list.append(general_sprites_data[0])

            return (filename, background_data, audio_data, general_sprites_data_list, sprites_data)

        @staticmethod
        def get_particle_system_data_from_file(file):
            filename = ESPEFileParser.get_filename(file)
            editor_data = ESPEFileParser.get_editor_data(file, False)
            name_data = ESPEFileParser.get_name_data(file, False)
            sprites_data = ESPEFileParser.get_sprites_psystem_data(file, False)
            amount_data = ESPEFileParser.get_amount_data(file, False)
            lifetime_data = ESPEFileParser.get_lifetime_data(file, False)
            explosiveness_data = ESPEFileParser.get_explosiveness_data(file, False)
            emitter_type_data = ESPEFileParser.get_emitter_type_data(file, False)
            movement_data = ESPEFileParser.get_movement_data(file, False)
            extra_movement_data = ESPEFileParser.get_extra_movement_data(file, False)
            alpha_data = ESPEFileParser.get_alpha_data(file, False)
            scale_data = ESPEFileParser.get_scale_data(file, False)
            rotate_data = ESPEFileParser.get_rotate_data(file, False)
            optimization_data = ESPEFileParser.get_optimization_data(file, False)

            if None in [filename, editor_data, name_data, sprites_data, amount_data, lifetime_data, explosiveness_data, emitter_type_data, movement_data, extra_movement_data, alpha_data, scale_data, rotate_data, optimization_data]:
                #raise ValueError(str([filename, editor_data, name_data, sprites_data, amount_data, lifetime_data, explosiveness_data, emitter_type_data, movement_data, extra_movement_data, alpha_data, scale_data, rotate_data, optimization_data]).replace(',', '\n')) 
                return None
            return (filename, editor_data, name_data, sprites_data, amount_data, lifetime_data, explosiveness_data, emitter_type_data, movement_data, extra_movement_data, alpha_data, scale_data, rotate_data, optimization_data)

        @staticmethod
        def get_filename(file):
            file.seek(0)
            line = file.readline().strip()
        
            if line != ESPEFileParser.FILENAME_LABEL:
                #return "Ошибка чтения."
                return None
            
            line = file.readline().strip()
            line_data = line.split('=')

            if len(line_data) != 2:
                return None
            
            if line_data[0] != "filename":
                return None
            
            filename = line_data[1]

            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                return None

            return filename

        @staticmethod
        def get_data_from_category(file, property_list):
            property_values = [ ]

            for prop_name, prop_type, prop_range in property_list:
                line = file.readline().strip()
                line_data = line.split('=')
                string_value = line_data[1]
                value = None

                opening_brackets = string_value.count('(')
                closing_brackets = string_value.count(')')
                tuple_of_values = False
                dictionary_of_values = False


                if line_data[0] != prop_name:
                    return None

                if opening_brackets != closing_brackets:
                    return None
                if ',' in string_value:
                    tuple_of_values = True
                if ':' in string_value:
                    dictionary_of_values = True
            
                
                if not ESPEFileParser.check_value_type(string_value, prop_type, tuple_of_values, dictionary_of_values):
                    raise ValueError()
                    return None

                if not tuple_of_values:
                    if '(' in string_value or ')' in string_value:
                        value = string_value[1:-1].split(',')
                    elif prop_type == bool:
                        value = string_value == "True"
                    else:                            
                        value = prop_type(string_value)
                elif dictionary_of_values:
                    pairs = string_value[1:-1].split("), (")
                    dict_strings = dict(pair.split(": ") for pair in pairs)
                    value = {key: (value == "True") for key, value in dict_strings.items()}
                else:
                    if prop_type == str:
                        value = string_value[1:-1].split(',')
                    else:
                        value = list(builtins.map(prop_type, string_value[1:-1].split(',')))
                
                if prop_range:
                    if tuple_of_values:
                        for elem in value:
                            if not(prop_range[0] <= elem <= prop_range[1]):
                                raise ValueError()
                                return None
                    else:
                        if not(prop_range[0] <= value <= prop_range[1]):
                            raise ValueError()
                            return None
                
                property_values.append(value)

            return property_values

        ##ДЛЯ СЦЕНЫ.##
        #######################################################################

        @staticmethod
        def get_background_data(file, from_start=True):
            property_values = [ ]

            if from_start:
                file.seek(0)

            line = file.readline().strip()
            loop_breakdown = 0

            while line != ESPEFileParser.BACKGROUND_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_scene_editor_attempts:
                    return None

            property_values = ESPEFileParser.get_data_from_category(file, ESPEFileParser.background_properties)

            if property_values is None or not property_values:
                return None
            
            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                return None
            
            return property_values
        
        @staticmethod
        def get_audio_data(file, from_start=True):
            if from_start:
                file.seek(0)

            line = file.readline().strip()
            loop_breakdown = 0

            while line != ESPEFileParser.AUDIO_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_scene_editor_attempts:
                    return None
            
            property_values = ESPEFileParser.get_data_from_category(file, ESPEFileParser.audio_properties)

            if property_values is None or not property_values:
                return None
            
            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                return None
            
            return property_values
        
        @staticmethod
        def get_sprites_data(file, from_start=True):
            sprite_properties = [ ]

            if from_start:
                file.seek(0)

            line = file.readline()
            line = line.strip()
            loop_breakdown = 0

            while line != ESPEFileParser.SPRITES_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_scene_editor_attempts:
                    return None

            sprite_properties = ESPEFileParser.get_sprites_category_data(file, ESPEFileParser.sprite_properties)

            if sprite_properties is None or not sprite_properties:
                return None

            return sprite_properties
        
        @staticmethod
        def get_sprites_category_data(file, property_list):
            property_values = [ ]

            line = file.readline().strip()
            line_data = line.split('=')
            string_value = line_data[1]
            value = None

            if not ESPEFileParser.check_value_type(string_value=string_value, value_type=int, is_tuple=False, is_dict=False):
                return None

            if line_data[0] != ESPEFileParser.sprite_general[0][0]:
                return None

            value = int(string_value)
            property_values.append(value)

            if value < 0:
                #Недопустимое число спрайтов.
                return None

            if value == 0:
                #Спрайтов нет. Возвращаем только кол-во спрайтов. Т.е. 0.
                return property_values

            line = file.readline().strip()

            while line != ESPEFileParser.END_CATEGORY_LABEL:
                line = file.readline().strip()

                #Здесь всё строго. Каждый спрайт идёт через одну пустую строку. Никак иначе.
                if line != ESPEFileParser.SPRITE_LABEL:
                    return None

                sprite_properties = [ ]

                for prop_name, prop_type, prop_range in property_list:
                    line = file.readline().strip()
                    line_data = line.split('=')
                    string_value = line_data[1]
                    value = None

                    opening_brackets = string_value.count('(')
                    closing_brackets = string_value.count(')')
                    tuple_of_values = False


                    if line_data[0] != prop_name:
                        return None

                    if prop_type != str:
                        if opening_brackets != closing_brackets:
                            return None
                        if ',' in string_value:
                            tuple_of_values = True

                    if not ESPEFileParser.check_value_type(string_value, prop_type, tuple_of_values, False):
                        return None

                    if not tuple_of_values:
                        value = prop_type(string_value)
                    else:
                        list(builtins.map(prop_type, value[1:-1].split(',')))
                    
                    if prop_range:
                        if not(prop_range[0] <= value <= prop_range[1]):
                            return None
                    
                    sprite_properties.append(value)

                line = file.readline().strip()

                if line != ESPEFileParser.SPRITE_END_LABEL:
                    #Файл повреждён или недопустимая иерархия.
                    raise ValueError("Метка1")
                    return None
                
                if sprite_properties:
                    property_values.append(sprite_properties)
                
                #Пропускаем пустую строку.
                line = file.readline().strip()
            
            #Завершаем блок спрайтов.
            if line !=ESPEFileParser.END_CATEGORY_LABEL:
                return None

            line = file.readline().strip()
            
            #Завершаем блок всего файла.
            if line != ESPEFileParser.END_FILE_LABEL:
                return None

            return property_values

        #######################################################################

        ##ДЛЯ СИСТЕМЫ ЧАСТИЦ.##
        #######################################################################

        @staticmethod
        def get_editor_data(file, from_start=True):
            property_values = [ ]

            if from_start:
                file.seek(0)

            line = file.readline().strip()
            loop_breakdown = 0

            while line != ESPEFileParser.EDITOR_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_particle_editor_attemps:
                    return None

            property_values = ESPEFileParser.get_data_from_category(file, ESPEFileParser.editor_properties)

            if property_values is None or not property_values:
                return None
            
            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                return None
            
            return property_values
        
        @staticmethod
        def get_name_data(file, from_start=True):
            property_values = [ ]

            if from_start:
                file.seek(0)

            line = file.readline().strip()
            loop_breakdown = 0

            while line != ESPEFileParser.NAME_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_particle_editor_attemps:
                    return None

            property_values = ESPEFileParser.get_data_from_category(file, ESPEFileParser.name_properties)

            if property_values is None or not property_values:
                return None
            
            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                return None
            
            return property_values

        @staticmethod
        def get_sprites_psystem_data(file, from_start=True):
            property_values = [ ]

            if from_start:
                file.seek(0)

            line = file.readline().strip()
            loop_breakdown = 0

            while line != ESPEFileParser.SPRITES_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_particle_editor_attemps:
                    return None

            property_values = ESPEFileParser.get_data_from_category(file, ESPEFileParser.sprites_psystem_properties)

            if property_values is None or not property_values:
                return None
            
            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                return None
            
            return property_values
        
        @staticmethod
        def get_amount_data(file, from_start=True):
            property_values = [ ]

            if from_start:
                file.seek(0)

            line = file.readline().strip()
            loop_breakdown = 0

            while line != ESPEFileParser.AMOUNT_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_particle_editor_attemps:
                    return None

            property_values = ESPEFileParser.get_data_from_category(file, ESPEFileParser.amount_properties)

            if property_values is None or not property_values:
                return None
            
            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                return None
            
            return property_values

        @staticmethod
        def get_lifetime_data(file, from_start=True):
            property_values = [ ]

            if from_start:
                file.seek(0)

            line = file.readline().strip()
            loop_breakdown = 0

            while line != ESPEFileParser.LIFETIME_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_particle_editor_attemps:
                    return None

            property_values = ESPEFileParser.get_data_from_category(file, ESPEFileParser.lifetime_properties)

            if property_values is None or not property_values:
                return None
            
            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                return None
            
            return property_values
        
        @staticmethod
        def get_explosiveness_data(file, from_start=True):
            property_values = [ ]

            if from_start:
                file.seek(0)

            line = file.readline().strip()
            loop_breakdown = 0

            while line != ESPEFileParser.EXPLOSIVENESS_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_particle_editor_attemps:
                    raise ValueError()
                    return None

            property_values = ESPEFileParser.get_data_from_category(file, ESPEFileParser.explosiveness_properties)

            if property_values is None or not property_values:
                raise ValueError()
                return None
            
            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                raise ValueError()
                return None
            
            return property_values
        
        @staticmethod
        def get_emitter_type_data(file, from_start=True):
            property_values = [ ]

            if from_start:
                file.seek(0)

            line = file.readline().strip()
            loop_breakdown = 0

            while line != ESPEFileParser.EMITTER_TYPE_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_particle_editor_attemps:
                    raise ValueError()
                    return None

            property_values = ESPEFileParser.get_data_from_category(file, ESPEFileParser.emitter_type_properties)

            if property_values is None or not property_values:
                raise ValueError()
                return None
            
            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                raise ValueError()
                return None
            
            return property_values
        
        @staticmethod
        def get_movement_data(file, from_start=True):
            property_values = [ ]

            if from_start:
                file.seek(0)

            line = file.readline().strip()
            loop_breakdown = 0

            while line != ESPEFileParser.MOVEMENT_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_particle_editor_attemps:
                    return None

            property_values = ESPEFileParser.get_data_from_category(file, ESPEFileParser.movement_properties)

            if property_values is None or not property_values:
                return None
            
            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                return None
            
            return property_values
        
        @staticmethod
        def get_extra_movement_data(file, from_start=True):
            property_values = [ ]

            if from_start:
                file.seek(0)

            line = file.readline().strip()
            loop_breakdown = 0

            while line != ESPEFileParser.EXTRA_MOVEMENT_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_particle_editor_attemps:
                    raise ValueError()
                    return None

            property_values = ESPEFileParser.get_data_from_category(file, ESPEFileParser.extra_movement_properties)

            if property_values is None or not property_values:
                raise ValueError()
                return None
            
            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                raise ValueError()
                return None
            
            return property_values
        
        @staticmethod
        def get_alpha_data(file, from_start=True):
            property_values = [ ]

            if from_start:
                file.seek(0)

            line = file.readline().strip()
            loop_breakdown = 0

            while line != ESPEFileParser.ALPHA_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_particle_editor_attemps:
                    raise ValueError()
                    return None

            property_values = ESPEFileParser.get_data_from_category(file, ESPEFileParser.alpha_properties)

            if property_values is None or not property_values:
                raise ValueError()
                return None
            
            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                raise ValueError()
                return None
            
            return property_values
        
        @staticmethod
        def get_scale_data(file, from_start=True):
            property_values = [ ]

            if from_start:
                file.seek(0)

            line = file.readline().strip()
            loop_breakdown = 0

            while line != ESPEFileParser.SCALE_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_particle_editor_attemps:
                    raise ValueError()
                    return None

            property_values = ESPEFileParser.get_data_from_category(file, ESPEFileParser.scale_properties)

            if property_values is None or not property_values:
                raise ValueError()
                return None
            
            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                raise ValueError()
                return None
            
            return property_values

        @staticmethod
        def get_rotate_data(file, from_start=True):
            property_values = [ ]

            if from_start:
                file.seek(0)

            line = file.readline().strip()
            loop_breakdown = 0

            while line != ESPEFileParser.ROTATE_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_particle_editor_attemps:
                    raise ValueError()
                    return None

            property_values = ESPEFileParser.get_data_from_category(file, ESPEFileParser.rotate_properties)

            if property_values is None or not property_values:
                raise ValueError()
                return None
            
            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                raise ValueError()
                return None
            
            return property_values
        
        @staticmethod
        def get_optimization_data(file, from_start=True):
            property_values = [ ]

            if from_start:
                file.seek(0)

            line = file.readline().strip()
            loop_breakdown = 0

            while line != ESPEFileParser.OPTIMIZATION_LABEL:
                loop_breakdown += 1
                line = file.readline().strip()

                if loop_breakdown > ESPEFileParser.cycle_particle_editor_attemps:
                    raise ValueError()
                    return None

            property_values = ESPEFileParser.get_data_from_category(file, ESPEFileParser.optimization_properties)

            if property_values is None or not property_values:
                raise ValueError()
                return None
            
            line = file.readline().strip()
            
            if line != ESPEFileParser.END_CATEGORY_LABEL:
                raise ValueError()
                return None

            line = file.readline().strip()

            #Завершаем блок всего файла.
            if line != ESPEFileParser.END_FILE_LABEL:
                raise ValueError()
                return None
            
            return property_values
        #######################################################################

        @staticmethod
        def check_value_type(string_value, value_type, is_tuple, is_dict):
            if string_value is None:
                return False

            if not callable(value_type):
                return False

            try:
                if not is_tuple:
                    value_type(string_value)
                elif is_dict:
                    pairs = string_value[1:-1].split("), (")
                    dict_strings = dict(pair.split(": ") for pair in pairs)
                    dict_typed = {key: (value_type(value)) for key, value in dict_strings.items()}
                else:
                    list(builtins.map(value_type, string_value[1:-1].split(',')))

                return True
            except (ValueError, TypeError):
                return False
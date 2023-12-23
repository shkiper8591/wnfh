init 200 python:
    import builtins

    class ESPECodeGenerator(object):
        TABULATE = "    "

        ##Я знаю, что так принято константы называть. Но сейчас... вы бы знали как мне похуй.##
        PSYSTEM_CODE_NAME = "Psystem"

        SINGLE_FILE = True
        GENERATE_FAST_MATH = True
        GENERATE_PARTICLE_RESET_FUNC = False
        UNIVERSAL_SYSTEM = False
        
        PSYSTEM_TOKEN_FUNCS = {
            "HEADING": None,

            "PARTICLE_OBJECT_CLASS_HEADING": None,
            "PARTICLE_OBJECT_INIT": None,
            "PARTICLE_METHODS": None,

            "PSYSTEM_CLASS_HEADING": None,
            "PSYSTEM_CLASS_INIT": None, #Для удобства пользвотеля в этот класс будет передаваться **kwargs.
            "PSYSTEM_ATTR_DICT": None, #Он будет вызываться где-то в самом конце или начале.
            "PSYSTEM_CLASS_METHODS": None,

            "SPRITE_MANAGER_UPDATE_FUNC": None,
            "SPRITE_MANAGER_CLASS": None,
            "PSYSTEM_INIT": None,
            "PSYSTEM_RESET": None,

            "FAST_MATH_GENERATOR": None
        }


        PSYSTEM_TOKENS = {
            "SIMPLE_PSYSTEM": False,
            "COMPLEX_PSYSTEM": False,

            "MULTIPLE_SPRITES": False,

            "RANDOM_LIFETIME": False,
            "RANDOM_APPEAR_DELAY": False,
            "EXPLOSIVENESS": False,

            "DOT_EMITTER": False,
            "RECTANGLE_EMITTER": False,
            "RADIAL_EMITTER": False,
            "SCREEN_EMITTER": False,
            "SIDES_EMITTER": False,

            "STATIC_MOVE": False,
            "SIMPLE_MOVE": False,
            "ACCELERATE_MOVE": False,
            
            "NO_EXTRA_MOVEMENT": False,
            "OSCILLATORY_EXTRA_MOVEMENT": False,

            "STATIC_ALPHA":False,
            "FADE_IN_OUT_ALPHA": False,
            "OSCILLATORY_ALPHA": False,

            "STATIC_ZOOM": False,
            "FADE_IN_OUT_ZOOM": False,
            "OSCILLATORY_ZOOM": False,

            "STATIC_ROTATE": False,
            "DYNAMIC_ROTATE": False,
            "ROTATE_BY_SPEED": False,
            "ROTATE_BY_SPEED_X": False,
            "ROTATE_BY_SPEED_Y": False,

            "INNER_FRAME_CHECK": False,
            "IS_SCREEN_BOUNDED": False
        }

        CHANGER_FUNCS_TOKENS = {
            "SIMPLE_MOVE_RANDOM_SPEED": False,

            "ACCELERATE_MOVE_RANDOM_SPEED": False,
            "ACCELERATE_MOVE_RANDOM_ACCELERATE": False,

            "OSCILLATORY_EXTRA_MOVEMENT_RANDOM_SPEED": False,
            "OSCILLATORY_EXTRA_MOVEMENT_RANDOM_AMPLITUDE": False,
            "OSCILLATORY_EXTRA_MOVEMENT_RANDOM_PHASE": False,

            "STATIC_ALPHA_RANDOM_TRANSPARENCY": False,
            "FADE_IN_OUT_ALPHA_RANDOM_TRANSPARENCY": False,
            
            "OSCILLATORY_ALPHA_RANDOM_TRANSPARENCY": False,
            "OSCILLATORY_ALPHA_RANDOM_SPEED": False,
            "OSCILLATORY_ALPHA_RANDOM_PHASE": False,

            "STATIC_ZOOM_RANDOM_SCALE": False,
            "FADE_IN_OUT_ZOOM_RANDOM_SCALE": False,

            "OSCILLATORY_ZOOM_RANDOM_SCALE": False,
            "OSCILLATORY_ZOOM_RANDOM_SPEED": False,
            "OSCILLATORY_ZOOM_RANDOM_PHASE": False,

            "STATIC_ROTATE_RANDOM_ANGLE": False,
            "DYNAMIC_ROTATE_RANDOM_START_ANGLE": False,
            "DYNAMIC_ROTATE_RANDOM_SPEED": False
        }

        @staticmethod
        def generate_psystem(file):
            ESPECodeGenerator.PSYSTEM_TOKEN_FUNCS["HEADING"](file)
            ESPECodeGenerator.write_heading_name(file, "Класс частицы")
            ESPECodeGenerator.write_divider(file)
            file.write('\n')
            ESPECodeGenerator.PSYSTEM_TOKEN_FUNCS["PARTICLE_OBJECT_CLASS_HEADING"](file)
            ESPECodeGenerator.PSYSTEM_TOKEN_FUNCS["PARTICLE_OBJECT_INIT"](file)
            file.write('\n')
            ESPECodeGenerator.PSYSTEM_TOKEN_FUNCS["PARTICLE_METHODS"](file)
            file.write('\n')
            ESPECodeGenerator.write_heading_name(file, "Класс системы частиц")
            ESPECodeGenerator.write_divider(file)
            file.write('\n')
            ESPECodeGenerator.PSYSTEM_TOKEN_FUNCS["PSYSTEM_CLASS_HEADING"](file)
            ESPECodeGenerator.PSYSTEM_TOKEN_FUNCS["PSYSTEM_CLASS_INIT"](file)
            file.write('\n')
            ESPECodeGenerator.PSYSTEM_TOKEN_FUNCS["PSYSTEM_CLASS_METHODS"](file)
            file.write('\n')

            if ESPECodeGenerator.SINGLE_FILE:
                if ESPECodeGenerator.GENERATE_FAST_MATH:
                    ESPECodeGenerator.write_heading_name(file, "Класс с заранее вычисленными тригонометрическими функциями")
                    ESPECodeGenerator.write_divider(file)
                    file.write('\n')
                    ESPECodeGenerator.PSYSTEM_TOKEN_FUNCS["FAST_MATH_GENERATOR"](file)
                    file.write('\n')

                ESPECodeGenerator.write_heading_name(file, "Функция обновления")
                file.write('\n')
                ESPECodeGenerator.write_divider(file)
                ESPECodeGenerator.PSYSTEM_TOKEN_FUNCS["SPRITE_MANAGER_UPDATE_FUNC"](file)
                file.write('\n')

                if ESPECodeGenerator.GENERATE_PARTICLE_RESET_FUNC:
                    ESPECodeGenerator.write_heading_name(file, "Функция сброса")
                    ESPECodeGenerator.write_divider(file)
                    file.write('\n')
                    ESPECodeGenerator.PSYSTEM_TOKEN_FUNCS["PSYSTEM_RESET"](file)
                    file.write('\n')
                    ESPECodeGenerator.write_tabulate(file, "#*Сброс системы частиц происходит следующим образом: вызовите данную функцию, передав в неё класс системы частиц. <Класс системы будет иметь обозначение <class> в названии>.*#\n")
                    ESPECodeGenerator.write_tabulate(file, "#*Пример: <")
                    ESPECodeGenerator.write_tabulate(file, "$ espe_psystem_reset_func(psystem_class=espe_{}_psystem_class)".format(ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()))
                    ESPECodeGenerator.write_tabulate(file, ">*#\n")
                    file.write('\n')

                ESPECodeGenerator.write_heading_name(file, "Свойства системы")
                ESPECodeGenerator.write_divider(file)
                file.write('\n')
                ESPECodeGenerator.PSYSTEM_TOKEN_FUNCS["PSYSTEM_ATTR_DICT"](file)
                file.write('\n')

                ESPECodeGenerator.write_heading_name(file, "Система")
                ESPECodeGenerator.write_divider(file)
                file.write('\n')

                file.write("init 100:\n")
                if ESPECodeGenerator.GENERATE_FAST_MATH:
                    ESPECodeGenerator.write_tabulate(file, "$ espe_omath = ESPEOptimizedValues()\n")
                ESPECodeGenerator.write_tabulate(file, "#*Переменная для использования. >>*#\n")
                ESPECodeGenerator.PSYSTEM_TOKEN_FUNCS["SPRITE_MANAGER_CLASS"](file)
                file.write('\n')
                ESPECodeGenerator.PSYSTEM_TOKEN_FUNCS["PSYSTEM_INIT"](file)
                file.write('\n')
                ESPECodeGenerator.write_tabulate(file, "#*<Вызов осуществляется через метод show() класса системы частиц с заданием перехода, если необходим.<<*#\n")
                ESPECodeGenerator.write_tabulate(file, "#*<Класс системы будет иметь обозначение <class> в названии>.*#\n")
                ESPECodeGenerator.write_tabulate(file, "#*Пример: <")
                ESPECodeGenerator.write_tabulate(file, "$ espe_{}_psystem_class.show(transition=dissolve, reset=True)".format(ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()))
                ESPECodeGenerator.write_tabulate(file, ">*#\n")
                ESPECodeGenerator.write_tabulate(file, "#*<")
                ESPECodeGenerator.write_tabulate(file, "$ espe_{}_psystem_class.show(transition=None, reset=True) <Без перехода>".format(ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()))
                ESPECodeGenerator.write_tabulate(file, ">*#\n")
                ESPECodeGenerator.write_tabulate(file, "#*<")
                ESPECodeGenerator.write_tabulate(file, "$ espe_{}_psystem_class.hide()".format(ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()))
                ESPECodeGenerator.write_tabulate(file, ">*#\n")
                ESPECodeGenerator.write_tabulate(file, "#*<Параметр reset принимает либо True, либо False. Если True, то система сбрасывается <как будто в первый раз запустили>>.*#\n")
                ESPECodeGenerator.write_tabulate(file, "#*<Если же reset=False, то частицы при повторном включении окажутся на том же месте, когда были на момент скрытия системы.*#\n")
                file.write('\n')
        
        @staticmethod
        def file_heading(file):
            file.write("init python:\n")
            ESPECodeGenerator.write_tabulate(file, "import random\n")
            ESPECodeGenerator.write_tabulate(file, "import builtins\n")
            ESPECodeGenerator.write_tabulate(file, "import math\n")
            file.write('\n')

        @staticmethod
        def file_particle_class_heading(file):
            ESPECodeGenerator.write_tabulate(file, "class ESPE{}Particle(renpy.object.Object):\n".format(ESPECodeGenerator.PSYSTEM_CODE_NAME))

        ##INIT class Particle ГЕНЕРАТОР.##
        #############################################################################################################

        @staticmethod
        def file_particle_class_init(file):
            ESPECodeGenerator.file_particle_class_init_hard(file)

        @staticmethod
        def file_particle_class_init_hard(file):
            ESPECodeGenerator.write_tabulate(file, "def __init__(self, displayable, manager, psystem, **kwargs):\n", multiplier=2)
            
            ESPECodeGenerator.write_tabulate(file, "self.displayable = displayable\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.manager = manager\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.psystem = psystem\n", multiplier=3)

            file.write('\n')
            ESPECodeGenerator.file_particle_class_init_displ_section(file)
            file.write('\n')
            ESPECodeGenerator.fire_particle_class_position_section(file)
            file.write('\n')
            ESPECodeGenerator.file_particle_class_init_movement_section(file)
            file.write('\n')
            ESPECodeGenerator.file_particle_class_init_extra_movement_section(file)

            if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                ESPECodeGenerator.file_particle_class_init_alpha_section(file)
                file.write('\n')
                ESPECodeGenerator.file_particle_class_init_zoom_section(file)
                file.write('\n')
                ESPECodeGenerator.file_particle_class_init_rotate_section(file)
            
            file.write('\n')
            ESPECodeGenerator.fire_particle_class_init_lifetime_section(file)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "self.active = False\n", multiplier=3)
            file.write('\n')

            if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                if ESPECodeGenerator.PSYSTEM_TOKENS["MULTIPLE_SPRITES"]:
                    ESPECodeGenerator.write_tabulate(file, "self.ready_to_set_child_t_obj = False\n", multiplier=3)
                    file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "if kwargs:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "for key, value in kwargs.items():\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "setattr(self, key, value)\n", multiplier=5)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "self.hide_child()\n", multiplier=3)

        @staticmethod
        def file_particle_class_init_displ_section(file):
            if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                ESPECodeGenerator.write_tabulate(file, "self.transform_object = Transform(child=displayable, function=self.transform_update_func)\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.transform_object.arguments = None\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.sprite = manager.create(self.transform_object)\n", multiplier=3)
            else:
               ESPECodeGenerator.write_tabulate(file, "self.sprite = manager.create(displayable)\n", multiplier=3)
        
        @staticmethod
        def fire_particle_class_position_section(file):
            ESPECodeGenerator.write_tabulate(file, "self.x = 0\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.y = 0\n", multiplier=3)

        @staticmethod
        def file_particle_class_init_movement_section(file):
            if ESPECodeGenerator.PSYSTEM_TOKENS["SIMPLE_MOVE"]:
                ESPECodeGenerator.write_tabulate(file, "self.x_speed = 0\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.y_speed = 0\n", multiplier=3)
            if ESPECodeGenerator.PSYSTEM_TOKENS["ACCELERATE_MOVE"]:
                ESPECodeGenerator.write_tabulate(file, "self.x_speed = 0\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.y_speed = 0\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.x_acceleration = 0\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.y_acceleration = 0\n", multiplier=3)

        @staticmethod
        def file_particle_class_init_extra_movement_section(file):
            if ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_EXTRA_MOVEMENT"]:
                ESPECodeGenerator.write_tabulate(file, "self.x_extra = 0\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.y_extra = 0\n", multiplier=3)
                file.write('\n')
                ESPECodeGenerator.write_tabulate(file, "self.extra_move_phase = 0\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.radius_x_extra = 0\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.radius_y_extra = 0\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.speed_extra = 0\n", multiplier=3)
                file.write('\n')
                ESPECodeGenerator.write_tabulate(file, "self.last_x_offset = 0\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.last_y_offset = 0\n", multiplier=3)
                file.write('\n')

        @staticmethod
        def file_particle_class_init_alpha_section(file):
            ESPECodeGenerator.write_tabulate(file, "self.alpha = 1.0\n", multiplier=3)

            if ESPECodeGenerator.PSYSTEM_TOKENS["FADE_IN_OUT_ALPHA"]:
                ESPECodeGenerator.write_tabulate(file, "self.intermediate_alpha = 1.0\n", multiplier=3)
                file.write('\n')
                ESPECodeGenerator.write_tabulate(file, "self.alpha_appear_time_end = 0.0\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.alpha_disappear_time_start = 0.0\n", multiplier=3)
            if ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_ALPHA"]:
                file.write('\n')
                ESPECodeGenerator.write_tabulate(file, "self.alpha_speed = 0.0\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.alpha_phase = 0.0\n", multiplier=3)

        @staticmethod
        def file_particle_class_init_zoom_section(file):
            ESPECodeGenerator.write_tabulate(file, "self.zoom = 1.0\n", multiplier=3)

            if ESPECodeGenerator.PSYSTEM_TOKENS["FADE_IN_OUT_ZOOM"]:
                ESPECodeGenerator.write_tabulate(file, "self.intermediate_zoom = 1.0\n", multiplier=3)
                file.write('\n')
                ESPECodeGenerator.write_tabulate(file, "self.zoom_appear_time_end = 0.0\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.zoom_disappear_time_start = 0.0\n", multiplier=3)
            if ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_ZOOM"]:
                file.write('\n')
                ESPECodeGenerator.write_tabulate(file, "self.zoom_speed = 0.0\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.zoom_phase = 0.0\n", multiplier=3)
        
        @staticmethod
        def file_particle_class_init_rotate_section(file):
            ESPECodeGenerator.write_tabulate(file, "self.angle = 0.0\n", multiplier=3)
            if ESPECodeGenerator.PSYSTEM_TOKENS["DYNAMIC_ROTATE"]: 
               file.write('\n')
               ESPECodeGenerator.write_tabulate(file, "self.rotate_speed = 0.0\n", multiplier=3)

        @staticmethod
        def fire_particle_class_init_lifetime_section(file):
            ESPECodeGenerator.write_tabulate(file, "self.lifetime = 0.0\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.cur_lifetime = 0.0\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "self.appear_delay = 0.0\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.cur_appear_delay = 0.0\n", multiplier=3)

        #############################################################################################################

        ##METHODS class Particle ГЕНЕРАТОР.##
        #############################################################################################################

        @staticmethod
        def file_particle_class_methods(file):
            if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                ESPECodeGenerator.file_particle_class_methods_transform_func_method(file)
                file.write('\n')
                ESPECodeGenerator.file_particle_class_methods_update_child_method(file)
                file.write('\n')

            ESPECodeGenerator.file_particle_class_methods_hide_child_method(file)
            file.write('\n')
            ESPECodeGenerator.file_particle_class_methods_set_child_method(file)
            file.write('\n')
            ESPECodeGenerator.file_particle_class_methods_destroy_method(file)
            file.write('\n')
            ESPECodeGenerator.file_particle_class_methods_position_methods(file)

        @staticmethod
        def file_particle_class_methods_transform_func_method(file):
            ESPECodeGenerator.write_tabulate(file, "def transform_update_func(self, t, st, at):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "t.alpha = self.alpha\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "t.zoom = self.zoom\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "t.rotate = self.angle\n", multiplier=3)
            file.write('\n')
            if ESPECodeGenerator.PSYSTEM_TOKENS["MULTIPLE_SPRITES"]:
                ESPECodeGenerator.write_tabulate(file, "if self.ready_to_set_child_t_obj:\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.ready_to_set_child_t_obj = False\n", multiplier=4)
                ESPECodeGenerator.write_tabulate(file, "t.child = renpy.store.ImageReference(tuple(self.displayable.split()))\n", multiplier=4)
                file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "return self.psystem.update_time\n", multiplier=3)

        @staticmethod
        def file_particle_class_methods_update_child_method(file):
            ESPECodeGenerator.write_tabulate(file, "def update_child(self):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "self.set_child(self.transform_object)\n", multiplier=3)

        @staticmethod
        def file_particle_class_methods_hide_child_method(file):
            ESPECodeGenerator.write_tabulate(file, "def hide_child(self):\n", multiplier=2)
            if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                ESPECodeGenerator.write_tabulate(file, "self.alpha = 0.0\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.sprite.set_child(self.transform_object)\n", multiplier=3)
            else:
                ESPECodeGenerator.write_tabulate(file, "self.y = config.screen_height + 10\n", multiplier=3)

        @staticmethod
        def file_particle_class_methods_set_child_method(file):
            ESPECodeGenerator.write_tabulate(file, "def set_child(self, displ):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "self.sprite.set_child(displ)\n", multiplier=3)

        @staticmethod
        def file_particle_class_methods_destroy_method(file):
            ESPECodeGenerator.write_tabulate(file, "def destroy(self):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "self.sprite.destroy()\n", multiplier=3)

        @staticmethod
        def file_particle_class_methods_position_methods(file):
            ESPECodeGenerator.write_tabulate(file, "@property\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "def x(self):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "return self.sprite.x\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "@x.setter\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "def x(self, value):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "self.sprite.x = value\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "@property\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "def y(self):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "return self.sprite.y\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "@y.setter\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "def y(self, value):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "self.sprite.y = value\n", multiplier=3)

        #############################################################################################################

        @staticmethod
        def file_psystem_class_heading(file):
            ESPECodeGenerator.write_tabulate(file, "class ESPE{}PSystem(renpy.object.Object):\n".format(ESPECodeGenerator.PSYSTEM_CODE_NAME))

        ##INIT class Psystem ГЕНЕРАТОР.##
        #############################################################################################################

        @staticmethod
        def file_psystem_class_init(file):
            ESPECodeGenerator.file_psystem_class_init_hard(file)

        @staticmethod
        def file_psystem_class_init_hard(file):
            ESPECodeGenerator.write_tabulate(file, "def __init__(self, manager, **kwargs):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "self.particle_object = ESPE{}Particle\n".format(ESPECodeGenerator.PSYSTEM_CODE_NAME), multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.manager = manager\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.omath = espe_omath\n", multiplier=3)
            file.write('\n')

            if ESPECodeGenerator.PSYSTEM_TOKENS["DOT_EMITTER"]:
                ESPECodeGenerator.write_tabulate(file, "self.positioning_func = self.dot_emitter\n", multiplier=3)
            if ESPECodeGenerator.PSYSTEM_TOKENS["RECTANGLE_EMITTER"]:
                ESPECodeGenerator.write_tabulate(file, "self.positioning_func = self.rectangle_emitter\n", multiplier=3)
            if ESPECodeGenerator.PSYSTEM_TOKENS["RADIAL_EMITTER"]:
                ESPECodeGenerator.write_tabulate(file, "self.positioning_func = self.radial_emitter\n", multiplier=3)
            if ESPECodeGenerator.PSYSTEM_TOKENS["SCREEN_EMITTER"]:
                ESPECodeGenerator.write_tabulate(file, "self.positioning_func = self.screen_emitter\n", multiplier=3)
            if ESPECodeGenerator.PSYSTEM_TOKENS["SIDES_EMITTER"]:
                ESPECodeGenerator.write_tabulate(file, "self.positioning_func = self.sides_emitter\n", multiplier=3)
            file.write('\n')

            if ESPECodeGenerator.PSYSTEM_TOKENS["SIMPLE_MOVE"]:
                ESPECodeGenerator.write_tabulate(file, "self.move_func = self.simple_move\n", multiplier=3)
                if not ESPECodeGenerator.CHANGER_FUNCS_TOKENS["SIMPLE_MOVE_RANDOM_SPEED"]:
                    ESPECodeGenerator.write_tabulate(file, "self.move_func_changer = self.speed_changer_constant\n", multiplier=3)
                else:
                    ESPECodeGenerator.write_tabulate(file, "self.move_func_changer = self.speed_changer\n", multiplier=3)
                file.write('\n')
            if ESPECodeGenerator.PSYSTEM_TOKENS["ACCELERATE_MOVE"]:
                ESPECodeGenerator.write_tabulate(file, "self.move_func = self.accelerate_move\n", multiplier=3)
                if not builtins.all([ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_SPEED"],
                            ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_ACCELERATE"]]):
                    ESPECodeGenerator.write_tabulate(file, "self.move_func_changer = self.move_prop_static_changer\n", multiplier=3)
                if builtins.all([ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_SPEED"],
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_ACCELERATE"]]):
                    ESPECodeGenerator.write_tabulate(file, "self.move_func_changer = self.speed_acc_changer\n", multiplier=3) 
                elif ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_SPEED"]:
                    ESPECodeGenerator.write_tabulate(file, "self.move_func_changer = self.static_accelerate_changer\n", multiplier=3)
                elif ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_ACCELERATE"]:
                    ESPECodeGenerator.write_tabulate(file, "self.move_func_changer = self.accelerate_changer\n", multiplier=3)
                file.write('\n')
            
            if ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_EXTRA_MOVEMENT"]:
                ESPECodeGenerator.write_tabulate(file, "self.extra_move_func = self.extra_move_oscillatory\n", multiplier=3)
                ESPECodeGenerator.file_psystem_init_extra_movement_oscillatory_changer_func(file)
                file.write('\n')
            
            if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                if ESPECodeGenerator.PSYSTEM_TOKENS["FADE_IN_OUT_ALPHA"]:
                    ESPECodeGenerator.write_tabulate(file, "self.alpha_func = self.alpha_fade_in_out_func\n", multiplier=3)
                    file.write('\n')
                if ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_ALPHA"]:
                    ESPECodeGenerator.write_tabulate(file, "self.alpha_func = self.alpha_oscillatory_func\n", multiplier=3)
                    file.write('\n')
                
                ESPECodeGenerator.file_psystem_init_alpha_changer_func(file)
                file.write('\n')

                if ESPECodeGenerator.PSYSTEM_TOKENS["FADE_IN_OUT_ZOOM"]:
                    ESPECodeGenerator.write_tabulate(file, "self.zoom_func = self.zoom_fade_in_out_func\n", multiplier=3)
                    file.write('\n')
                if ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_ZOOM"]:
                    ESPECodeGenerator.write_tabulate(file, "self.zoom_func = self.zoom_oscillatory_func\n", multiplier=3)
                    ESPECodeGenerator.file_psystem_init_oscillatory_zoom_changer_func(file)
                    file.write('\n')
                
                ESPECodeGenerator.file_psystem_init_zoom_changer_func(file)
                file.write('\n')
                
                if ESPECodeGenerator.PSYSTEM_TOKENS["DYNAMIC_ROTATE"]:
                    ESPECodeGenerator.write_tabulate(file, "self.rotate_func = self.dynamic_rotate_func\n", multiplier=3)
                    ESPECodeGenerator.file_psystem_init_rotate_changer_func(file)
                    file.write('\n')
                if ESPECodeGenerator.PSYSTEM_TOKENS["ROTATE_BY_SPEED"]:
                    ESPECodeGenerator.write_tabulate(file, "self.rotate_func = self.rotate_by_speed_func\n", multiplier=3)
                    file.write('\n')
            
            if ESPECodeGenerator.PSYSTEM_TOKENS["INNER_FRAME_CHECK"]:
                ESPECodeGenerator.write_tabulate(file, "self.old_st = 0.0\n", multiplier=3)
            else:
                ESPECodeGenerator.write_tabulate(file, "self.frame_dtime = 0.016\n", multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "for key, value in kwargs.items():\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "setattr(self, key, value)\n", multiplier=4)
            file.write('\n')

            if ESPECodeGenerator.PSYSTEM_TOKENS["EXPLOSIVENESS"]:
                ESPECodeGenerator.write_tabulate(file, "self.explosiveness_amount = self.amount * self.explosiveness_factor\n", multiplier=3)
                file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "self.active_particles = [ ]\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.inactive_particles = [ ]\n", multiplier=3)
            file.write('\n')

            ESPECodeGenerator.file_psystem_class_init_particle_list(file)

        @staticmethod
        def file_psystem_class_init_particle_list(file):
            ESPECodeGenerator.write_tabulate(file, "for prt_index in range(self.amount):\n", multiplier=3)
            if ESPECodeGenerator.PSYSTEM_TOKENS["MULTIPLE_SPRITES"]:
                ESPECodeGenerator.write_tabulate(file, "displ = renpy.random.choice(self.displayable_list)\n", multiplier=4)
            else:
                ESPECodeGenerator.write_tabulate(file, "displ = self.displayable_list\n", multiplier=4)
            if not ESPECodeGenerator.PSYSTEM_TOKENS["RANDOM_APPEAR_DELAY"]:
                ESPECodeGenerator.write_tabulate(file, "appear_delay = espe_{}_properties[\"lifetime_spread\"] * prt_index\n".format(ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()), multiplier=4)
            else:
                ESPECodeGenerator.write_tabulate(file, "appear_delay = renpy.random.uniform(espe_{}_properties[\"lifetime_spread\"] * espe_{}_properties[\"lifetime_spread_random\"], espe_{}_properties[\"lifetime_spread\"] * prt_index\)n".format(ESPECodeGenerator.PSYSTEM_CODE_NAME.lower(), ESPECodeGenerator.PSYSTEM_CODE_NAME.lower(), ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()), multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle = self.particle_object(displayable=displ, manager=self.manager, psystem=self, appear_delay=appear_delay)\n".format(ESPECodeGenerator.PSYSTEM_CODE_NAME), multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "self.inactive_particles.append(particle)\n", multiplier=4)

            # ESPECodeGenerator.write_tabulate(file, "\n", multiplier=10)
            #     if any([ESPECodeGenerator.PSYSTEM_TOKENS["SIMPLE_MOVE"], ESPECodeGenerator.PSYSTEM_TOKENS["ACCELERATE_MOVE"]]):
            #         ESPECodeGenerator.write_tabulate(file, "x_speed = self.\n", multiplier=3)
            #         ESPECodeGenerator.write_tabulate(file, "y_speed = 0\n", multiplier=3)
            #     if ESPECodeGenerator.PSYSTEM_TOKENS["ACCELERATE_MOVE"]:
            #         ESPECodeGenerator.write_tabulate(file, "x_acceleration = 0\n", multiplier=3)
            #         ESPECodeGenerator.write_tabulate(file, "y_acceleration = 0\n", multiplier=3)

        @staticmethod
        def file_psystem_init_extra_movement_oscillatory_changer_func(file):
            amount_of_changers_extra_move = 0

            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_SPEED"]:
                amount_of_changers_extra_move += 1
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_AMPLITUDE"]:
                amount_of_changers_extra_move += 1
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_PHASE"]:
                amount_of_changers_extra_move += 1
            if amount_of_changers_extra_move > 1:
                ESPECodeGenerator.write_tabulate(file, "self.move_extra_prop_changer_func = self.extra_move_prop_changer_oscillatory_zip\n", multiplier=3)
                return   

            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_SPEED"]:
                ESPECodeGenerator.write_tabulate(file, "self.move_extra_prop_changer_func = self.extra_move_speed_changer\n", multiplier=3)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_AMPLITUDE"]:
                ESPECodeGenerator.write_tabulate(file, "self.move_extra_prop_changer_func = self.extra_move_radius_changer\n", multiplier=3)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_PHASE"]:
                ESPECodeGenerator.write_tabulate(file, "self.move_extra_prop_changer_func = self.extra_move_phase_changer\n", multiplier=3)

        @staticmethod
        def file_psystem_init_alpha_changer_func(file):
            amount_of_changers_oscillatory_alpha = 0

            if ESPECodeGenerator.PSYSTEM_TOKENS["FADE_IN_OUT_ALPHA"]:
                if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["FADE_IN_OUT_ALPHA_RANDOM_TRANSPARENCY"]:
                    ESPECodeGenerator.write_tabulate(file, "self.alpha_changer_func = self.alpha_fade_in_out_changer\n", multiplier=3)
                else:
                    ESPECodeGenerator.write_tabulate(file, "self.alpha_changer_func = self.alpha_fade_in_out_constant_changer\n", multiplier=3)
                return

            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_TRANSPARENCY"]:
                amount_of_changers_oscillatory_alpha += 1
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_SPEED"]:
                amount_of_changers_oscillatory_alpha += 1
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_PHASE"]:
                amount_of_changers_oscillatory_alpha += 1
            if amount_of_changers_oscillatory_alpha > 1:
                ESPECodeGenerator.write_tabulate(file, "self.alpha_changer_func = self.alpha_oscillatory_changer_zip\n", multiplier=3)
                return

            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["FADE_IN_OUT_ALPHA_RANDOM_TRANSPARENCY"]:
                ESPECodeGenerator.write_tabulate(file, "self.alpha_changer_func = self.alpha_fade_in_out_changer\n", multiplier=3)

            if any([ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_TRANSPARENCY"], ESPECodeGenerator.CHANGER_FUNCS_TOKENS["STATIC_ALPHA_RANDOM_TRANSPARENCY"]]):
                ESPECodeGenerator.write_tabulate(file, "self.alpha_changer_func = self.alpha_static_changer\n", multiplier=3)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_SPEED"]:
                ESPECodeGenerator.write_tabulate(file, "self.alpha_changer_func = self.alpha_oscillatory_speed_changer\n", multiplier=3)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_PHASE"]:
                ESPECodeGenerator.write_tabulate(file, "self.alpha_changer_func = self.alpha_oscillatory_phase_changer\n", multiplier=3)

        @staticmethod
        def file_psystem_init_zoom_changer_func(file):
            amount_of_changers_oscillatory_zoom = 0

            if ESPECodeGenerator.PSYSTEM_TOKENS["FADE_IN_OUT_ZOOM"]:
                if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["FADE_IN_OUT_ZOOM_RANDOM_SCALE"]:
                    ESPECodeGenerator.write_tabulate(file, "self.zoom_changer_func = self.zoom_fade_in_out_changer\n", multiplier=3)
                else:
                    ESPECodeGenerator.write_tabulate(file, "self.zoom_changer_func = self.zoom_fade_in_out_constant_changer\n", multiplier=3)
                return

            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_SCALE"]:
                amount_of_changers_oscillatory_zoom += 1
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_SPEED"]:
                amount_of_changers_oscillatory_zoom += 1
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_PHASE"]:
                amount_of_changers_oscillatory_zoom += 1
            if amount_of_changers_oscillatory_zoom > 1:
                ESPECodeGenerator.write_tabulate(file, "self.zoom_changer_func = self.zoom_oscillatory_changer_zip\n", multiplier=3)
                return

            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["FADE_IN_OUT_ZOOM_RANDOM_SCALE"]:
                ESPECodeGenerator.write_tabulate(file, "self.zoom_changer_func = self.zoom_fade_in_out_changer\n", multiplier=3)

            if any([ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_SCALE"], ESPECodeGenerator.CHANGER_FUNCS_TOKENS["STATIC_ZOOM_RANDOM_SCALE"]]):
                ESPECodeGenerator.write_tabulate(file, "self.zoom_changer_func = self.zoom_static_changer\n", multiplier=3)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_SPEED"]:
                ESPECodeGenerator.write_tabulate(file, "self.zoom_changer_func = self.zoom_oscillatory_speed_changer\n", multiplier=3)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_PHASE"]:
                ESPECodeGenerator.write_tabulate(file, "self.zoom_changer_func = self.zoom_oscillatory_phase_changer\n", multiplier=3)

        @staticmethod
        def file_psystem_init_rotate_changer_func(file):
            amount_of_changers_dynamic_rotate = 0

            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["DYNAMIC_ROTATE_RANDOM_START_ANGLE"]:
                amount_of_changers_dynamic_rotate += 1
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["DYNAMIC_ROTATE_RANDOM_SPEED"]:
                amount_of_changers_dynamic_rotate += 1
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["DYNAMIC_ROTATE_RANDOM_SPEED"]:
                amount_of_changers_dynamic_rotate += 1
            if amount_of_changers_dynamic_rotate > 1:
                ESPECodeGenerator.write_tabulate(file, "self.rotate_changer_func = self.dynamic_rotate_changer_zip\n", multiplier=3)
                return

            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["STATIC_ROTATE_RANDOM_ANGLE"]:
                    ESPECodeGenerator.write_tabulate(file, "self.rotate_changer_func = self.rotate_static_changer\n", multiplier=3)

            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["DYNAMIC_ROTATE_RANDOM_START_ANGLE"]:
                ESPECodeGenerator.write_tabulate(file, "self.rotate_changer_func = self.dynamic_rotate_start_angle_changer\n", multiplier=3)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["DYNAMIC_ROTATE_RANDOM_SPEED"]:
                ESPECodeGenerator.write_tabulate(file, "self.rotate_changer_func = self.dynamic_rotate_speed_changer\n", multiplier=3)
            
        #############################################################################################################

        ##METHODS class Psystem ГЕНЕРАТОР.##
        #############################################################################################################

        @staticmethod
        def file_psystem_class_methods(file):
            ESPECodeGenerator.file_psystem_class_particles_process_method(file)
            file.write('\n')
            ESPECodeGenerator.file_psystem_class_dead_or_alive_method(file)
            file.write('\n')
            ESPECodeGenerator.file_psystem_class_reset_or_wait_method(file)
            file.write('\n')
            ESPECodeGenerator.file_psystem_class_reset_particle_method(file)
            file.write('\n')
            if ESPECodeGenerator.PSYSTEM_TOKENS["MULTIPLE_SPRITES"]:
                ESPECodeGenerator.file_psystem_class_choice_sprite_method(file)
                file.write('\n')
            
            if ESPECodeGenerator.PSYSTEM_TOKENS["RANDOM_LIFETIME"]:
                ESPECodeGenerator.file_psystem_class_lifetime_behavior_method(file)
                file.write('\n')
            
            if ESPECodeGenerator.PSYSTEM_TOKENS["EXPLOSIVENESS"]:
                ESPECodeGenerator.file_psystem_class_explosiveness_method(file)
                file.write('\n')

            if ESPECodeGenerator.PSYSTEM_TOKENS["INNER_FRAME_CHECK"]:
                ESPECodeGenerator.file_psystem_class_get_delta_frame_time_method(file)
                file.write('\n')
            
            if ESPECodeGenerator.PSYSTEM_TOKENS["DOT_EMITTER"]:
                ESPECodeGenerator.file_psystem_class_dot_emitter_method(file)
                file.write('\n')
            if ESPECodeGenerator.PSYSTEM_TOKENS["RECTANGLE_EMITTER"]:
                ESPECodeGenerator.file_psystem_class_rectangle_emitter_method(file)
                file.write('\n')
            if ESPECodeGenerator.PSYSTEM_TOKENS["RADIAL_EMITTER"]:
                ESPECodeGenerator.file_psystem_class_radial_emitter_method(file)
                file.write('\n')
            if ESPECodeGenerator.PSYSTEM_TOKENS["SCREEN_EMITTER"]:
                ESPECodeGenerator.file_psystem_class_screen_emitter_method(file)
                file.write('\n')
            if ESPECodeGenerator.PSYSTEM_TOKENS["SIDES_EMITTER"]:
                ESPECodeGenerator.file_psystem_class_sides_emitter_method(file)
                file.write('\n')
            
            if ESPECodeGenerator.PSYSTEM_TOKENS["SIMPLE_MOVE"]:
                ESPECodeGenerator.file_psystem_class_simple_move_method(file)
                file.write('\n')
                if not ESPECodeGenerator.CHANGER_FUNCS_TOKENS["SIMPLE_MOVE_RANDOM_SPEED"]:
                    ESPECodeGenerator.file_psystem_class_speed_changer_constant_method(file)
                file.write('\n')
            if ESPECodeGenerator.PSYSTEM_TOKENS["ACCELERATE_MOVE"]:
                ESPECodeGenerator.file_psystem_class_accelerate_move_method(file)
                file.write('\n')
                if not builtins.all([ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_SPEED"],
                            ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_ACCELERATE"]]):
                    ESPECodeGenerator.file_psystem_class_speed_accelerate_changer_constant_method(file)
                file.write('\n')
            
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["SIMPLE_MOVE_RANDOM_SPEED"]:
                ESPECodeGenerator.file_psystem_class_speed_changer_method(file)
                file.write('\n')
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_SPEED"] and ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_ACCELERATE"]:
                ESPECodeGenerator.file_psystem_class_speed_acc_changer_method(file)
                file.write('\n')
            elif ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_SPEED"]:
                ESPECodeGenerator.file_psystem_class_static_acc_speed_changer_method(file)
                file.write('\n')
            elif ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_ACCELERATE"]:
                ESPECodeGenerator.file_psystem_class_accelerate_changer_method(file)
                file.write('\n')
            
            if ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_EXTRA_MOVEMENT"]:
                ESPECodeGenerator.file_psystem_class_extra_move_oscillatory_method(file)
                file.write('\n')

                amount_of_changers_extra_move = 0
                if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_SPEED"]:
                    amount_of_changers_extra_move += 1
                    ESPECodeGenerator.file_psystem_class_extra_move_speed_changer_method(file)
                    file.write('\n')
                if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_AMPLITUDE"]:
                    amount_of_changers_extra_move += 1
                    ESPECodeGenerator.file_psystem_class_extra_move_radius_changer_method(file)
                    file.write('\n')
                if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_PHASE"]:
                    amount_of_changers_extra_move += 1
                    ESPECodeGenerator.file_psystem_class_extra_move_phase_changer_method(file)
                    file.write('\n')

                if amount_of_changers_extra_move > 1:
                    ESPECodeGenerator.file_psystem_class_extra_move_prop_changer_oscillatory_zip_method(file)
                    file.write('\n')
            
            if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                if ESPECodeGenerator.PSYSTEM_TOKENS["FADE_IN_OUT_ALPHA"]:
                    ESPECodeGenerator.file_psystem_class_alpha_fade_in_out_func_method(file)
                    file.write('\n')
                if ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_ALPHA"]:
                    ESPECodeGenerator.file_psystem_class_alpha_oscillatory_func_method(file)
                    file.write('\n')

                    amount_of_changers_oscillatory_alpha = 0
                    if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_TRANSPARENCY"]:
                        amount_of_changers_oscillatory_alpha += 1
                        ESPECodeGenerator.file_psystem_class_alpha_static_changer_method(file)
                        file.write('\n')
                    if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_SPEED"]:
                        amount_of_changers_oscillatory_alpha += 1
                        ESPECodeGenerator.file_psystem_class_alpha_oscillatory_speed_changer_method(file)
                        file.write('\n')
                    if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_PHASE"]:
                        amount_of_changers_oscillatory_alpha += 1
                        ESPECodeGenerator.file_psystem_class_alpha_oscillatory_phase_changer_method(file)
                        file.write('\n')
                    
                    if amount_of_changers_oscillatory_alpha > 1:
                        ESPECodeGenerator.file_psystem_class_alpha_oscillatory_changer_zip_method(file)
                        file.write('\n')
                
                if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["STATIC_ALPHA_RANDOM_TRANSPARENCY"]:
                    ESPECodeGenerator.file_psystem_class_alpha_static_changer_method(file)
                    file.write('\n')
                if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["FADE_IN_OUT_ALPHA_RANDOM_TRANSPARENCY"]:
                    ESPECodeGenerator.file_psystem_class_alpha_fade_in_out_changer_method(file)
                    file.write('\n')
                else:
                    ESPECodeGenerator.file_psystem_class_alpha_fade_in_out_changer_constant_method(file)
                    file.write('\n')
                
                if ESPECodeGenerator.PSYSTEM_TOKENS["FADE_IN_OUT_ZOOM"]:
                    ESPECodeGenerator.file_psystem_class_zoom_fade_in_out_func_method(file)
                    file.write('\n')
                if ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_ZOOM"]:
                    ESPECodeGenerator.file_psystem_class_zoom_oscillatory_func_method(file)
                    file.write('\n')

                    amount_of_changers_oscillatory_zoom = 0
                    if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_SCALE"]:
                        amount_of_changers_oscillatory_zoom += 1
                        ESPECodeGenerator.file_psystem_class_zoom_static_changer_method(file)
                        file.write('\n')
                    if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_SPEED"]:
                        amount_of_changers_oscillatory_zoom += 1
                        ESPECodeGenerator.file_psystem_class_zoom_oscillatory_speed_changer_method(file)
                        file.write('\n')
                    if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_PHASE"]:
                        amount_of_changers_oscillatory_zoom += 1
                        ESPECodeGenerator.file_psystem_class_zoom_oscillatory_phase_changer_method(file)
                        file.write('\n')
                    
                    if amount_of_changers_oscillatory_zoom > 1:
                        ESPECodeGenerator.file_psystem_class_zoom_oscillatory_changer_zip_method(file)
                        file.write('\n')
                
                if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["STATIC_ZOOM_RANDOM_SCALE"]:
                    ESPECodeGenerator.file_psystem_class_zoom_static_changer_method(file)
                    file.write('\n')
                if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["FADE_IN_OUT_ZOOM_RANDOM_SCALE"]:
                    ESPECodeGenerator.file_psystem_class_zoom_fade_in_out_changer_method(file)
                    file.write('\n')
                else:
                    ESPECodeGenerator.file_psystem_class_zoom_fade_in_out_changer_constant_method(file)
                    file.write('\n')
                    
                if ESPECodeGenerator.PSYSTEM_TOKENS["DYNAMIC_ROTATE"]:
                    ESPECodeGenerator.file_psystem_class_dynamic_rotate_func_method(file)
                    file.write('\n')

                    amount_of_changers_dynamic_rotate = 0
                    if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["DYNAMIC_ROTATE_RANDOM_START_ANGLE"]:
                        amount_of_changers_dynamic_rotate += 1
                        ESPECodeGenerator.file_psystem_class_dynamic_rotate_start_angle_changer_method(file)
                        file.write('\n')
                    if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["DYNAMIC_ROTATE_RANDOM_SPEED"]:
                        amount_of_changers_dynamic_rotate += 1
                        ESPECodeGenerator.file_psystem_class_dynamic_rotate_speed_changer_method(file)
                        file.write('\n')

                    if amount_of_changers_dynamic_rotate > 1:
                        ESPECodeGenerator.file_psystem_class_dynamic_rotate_changer_zip_method(file)
                        file.write('\n')

                if ESPECodeGenerator.PSYSTEM_TOKENS["ROTATE_BY_SPEED"]:
                    ESPECodeGenerator.file_psystem_class_rotate_by_speed_method(file)
                    file.write('\n')
                    ESPECodeGenerator.file_psystem_class_rotate_by_speed_changer_method(file)
                    file.write('\n')

                if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["STATIC_ROTATE_RANDOM_ANGLE"]:
                    ESPECodeGenerator.file_psystem_class_rotate_static_changer_method(file)
            
            ESPECodeGenerator.file_psystem_class_from_active_to_inactive_method(file)
            file.write('\n')
            ESPECodeGenerator.file_psystem_class_from_inactive_to_active_method(file)
            file.write('\n')
            ESPECodeGenerator.file_psystem_class_psystem_reset(file)
            file.write('\n')
            ESPECodeGenerator.file_psystem_class_show_psystem(file)
            file.write('\n')
            ESPECodeGenerator.file_psystem_class_hide_psystem(file)

        @staticmethod
        def file_psystem_class_particles_process_method(file):
            ESPECodeGenerator.write_tabulate(file, "def particles_process(self, st):\n", multiplier=2)

            if ESPECodeGenerator.PSYSTEM_TOKENS["INNER_FRAME_CHECK"]:
                ESPECodeGenerator.write_tabulate(file, "self.frame_dtime = self.get_delta_frame_time(st)\n", multiplier=3)
            else:
                ESPECodeGenerator.write_tabulate(file, "self.frame_dtime = self.fixed_dtime\n", multiplier=3)

            if any([ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_EXTRA_MOVEMENT"], ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_ALPHA"], ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_ZOOM"], ESPECodeGenerator.PSYSTEM_TOKENS["INNER_FRAME_CHECK"]]):
                ESPECodeGenerator.write_tabulate(file, "self.st = st\n", multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "for particle in reversed(self.active_particles):\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "if self.dead_or_alive(particle):\n", multiplier=4)

            if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                if not ESPECodeGenerator.PSYSTEM_TOKENS["STATIC_ALPHA"]:
                    ESPECodeGenerator.write_tabulate(file, "self.alpha_func(particle)\n", multiplier=5)
                if not ESPECodeGenerator.PSYSTEM_TOKENS["STATIC_ZOOM"]:
                    ESPECodeGenerator.write_tabulate(file, "self.zoom_func(particle)\n", multiplier=5)
                if not ESPECodeGenerator.PSYSTEM_TOKENS["STATIC_ROTATE"]:
                    ESPECodeGenerator.write_tabulate(file, "self.rotate_func(particle)\n", multiplier=5)

            if not ESPECodeGenerator.PSYSTEM_TOKENS["STATIC_MOVE"]:
                ESPECodeGenerator.write_tabulate(file, "self.move_func(particle)\n", multiplier=5)
            if not ESPECodeGenerator.PSYSTEM_TOKENS["NO_EXTRA_MOVEMENT"]:
                ESPECodeGenerator.write_tabulate(file, "self.extra_move_func(particle)\n", multiplier=5)

            if not builtins.all([ESPECodeGenerator.PSYSTEM_TOKENS["STATIC_ALPHA"],
                    ESPECodeGenerator.PSYSTEM_TOKENS["STATIC_ZOOM"], 
                    ESPECodeGenerator.PSYSTEM_TOKENS["STATIC_ROTATE"], 
                    ESPECodeGenerator.PSYSTEM_TOKENS["STATIC_MOVE"], 
                    ESPECodeGenerator.PSYSTEM_TOKENS["NO_EXTRA_MOVEMENT"]]):
                ESPECodeGenerator.write_tabulate(file, "pass\n", multiplier=5)

            ESPECodeGenerator.write_tabulate(file, "else:\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "self.from_active_to_inactive(particle)\n", multiplier=5)
            file.write('\n')

            if ESPECodeGenerator.PSYSTEM_TOKENS["EXPLOSIVENESS"]:
                ESPECodeGenerator.write_tabulate(file, "if self.explosiveness_func():\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "for particle in reversed(self.inactive_particles):\n", multiplier=4)
                ESPECodeGenerator.write_tabulate(file, "self.reset_or_wait(particle)\n", multiplier=5)
                ESPECodeGenerator.write_tabulate(file, "if particle.active:\n", multiplier=5)
                ESPECodeGenerator.write_tabulate(file, "self.from_inactive_to_active(particle)\n", multiplier=6)

                ESPECodeGenerator.write_tabulate(file, "else:\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "for particle in reversed(self.inactive_particles):\n", multiplier=4)
                ESPECodeGenerator.write_tabulate(file, "self.reset_or_wait(particle)\n", multiplier=5)
                ESPECodeGenerator.write_tabulate(file, "if particle.active:\n", multiplier=5)
                ESPECodeGenerator.write_tabulate(file, "self.from_inactive_to_active(particle)\n", multiplier=6)
            else:
                ESPECodeGenerator.write_tabulate(file, "for particle in reversed(self.inactive_particles):\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "self.reset_or_wait(particle)\n", multiplier=4)
                ESPECodeGenerator.write_tabulate(file, "if particle.active:\n", multiplier=4)
                ESPECodeGenerator.write_tabulate(file, "self.from_inactive_to_active(particle)\n", multiplier=5)

        @staticmethod
        def file_psystem_class_dead_or_alive_method(file):
            ESPECodeGenerator.write_tabulate(file, "def dead_or_alive(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.cur_lifetime += self.frame_dtime\n", multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "if particle.cur_lifetime > particle.lifetime:\n", multiplier=3)
            if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                ESPECodeGenerator.write_tabulate(file, "particle.hide_child()\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle.active = False\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "return False\n", multiplier=4)
            file.write('\n')

            if ESPECodeGenerator.PSYSTEM_TOKENS["IS_SCREEN_BOUNDED"]:
                ESPECodeGenerator.write_tabulate(file, "if -110 > particle.x < 1990 or -110 > particle.y < 1180:\n", multiplier=3)
                if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                    ESPECodeGenerator.write_tabulate(file, "particle.hide_child()\n", multiplier=4)
                ESPECodeGenerator.write_tabulate(file, "particle.active = False\n", multiplier=4)
                ESPECodeGenerator.write_tabulate(file, "return False\n", multiplier=4)
                file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "return True\n", multiplier=3)
        
        @staticmethod
        def file_psystem_class_reset_or_wait_method(file):
            ESPECodeGenerator.write_tabulate(file, "def reset_or_wait(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.cur_appear_delay += self.frame_dtime\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "if particle.cur_appear_delay >= particle.appear_delay:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.reset_particle(particle)\n", multiplier=4)

        @staticmethod
        def file_psystem_class_reset_particle_method(file):
            ESPECodeGenerator.write_tabulate(file, "def reset_particle(self, particle):\n", multiplier=2)
            if ESPECodeGenerator.PSYSTEM_TOKENS["RANDOM_LIFETIME"]:
                ESPECodeGenerator.write_tabulate(file, "self.lifetime_behavior(particle)\n", multiplier=3)
            else:
                ESPECodeGenerator.write_tabulate(file, "particle.lifetime = self.lifetime\n", multiplier=3)

            if ESPECodeGenerator.PSYSTEM_TOKENS["MULTIPLE_SPRITES"]:
                ESPECodeGenerator.write_tabulate(file, "self.choice_sprite(particle)\n", multiplier=3)
            
            if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                if any([ESPECodeGenerator.PSYSTEM_TOKENS["FADE_IN_OUT_ALPHA"],
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["STATIC_ALPHA_RANDOM_TRANSPARENCY"],
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["FADE_IN_OUT_ALPHA_RANDOM_TRANSPARENCY"],
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_TRANSPARENCY"],
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_TRANSPARENCY"],
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_SPEED"],
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_PHASE"]]):
                    ESPECodeGenerator.write_tabulate(file, "self.alpha_changer_func(particle)\n", multiplier=3)
                else:
                    if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["FADE_IN_OUT_ALPHA_RANDOM_TRANSPARENCY"]:
                        ESPECodeGenerator.write_tabulate(file, "particle.alpha = 0.0\n", multiplier=3)
                    else:
                        ESPECodeGenerator.write_tabulate(file, "particle.alpha = self.intermediate_max_alpha\n", multiplier=3)

                if any([ESPECodeGenerator.PSYSTEM_TOKENS["FADE_IN_OUT_ZOOM"],
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["STATIC_ZOOM_RANDOM_SCALE"],
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["FADE_IN_OUT_ZOOM_RANDOM_SCALE"],
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_SCALE"],
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_SCALE"],
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_SPEED"],
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_PHASE"]]):
                    ESPECodeGenerator.write_tabulate(file, "self.zoom_changer_func(particle)\n", multiplier=3)
                else:
                    ESPECodeGenerator.write_tabulate(file, "particle.zoom = self.intermediate_max_zoom\n", multiplier=3)
                
                if any([ESPECodeGenerator.CHANGER_FUNCS_TOKENS["STATIC_ROTATE_RANDOM_ANGLE"],
                        ESPECodeGenerator.PSYSTEM_TOKENS["DYNAMIC_ROTATE"],
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["DYNAMIC_ROTATE_RANDOM_START_ANGLE"],
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["DYNAMIC_ROTATE_RANDOM_SPEED"],
                        ESPECodeGenerator.PSYSTEM_TOKENS["ROTATE_BY_SPEED"]]):
                    ESPECodeGenerator.write_tabulate(file, "self.rotate_changer_func(particle)\n", multiplier=3)
                else:
                    ESPECodeGenerator.write_tabulate(file, "particle.angle = self.max_angle\n", multiplier=3)
            
            if any([ESPECodeGenerator.PSYSTEM_TOKENS["SIMPLE_MOVE"],
                    ESPECodeGenerator.PSYSTEM_TOKENS["ACCELERATE_MOVE"]]):
                ESPECodeGenerator.write_tabulate(file, "self.move_func_changer(particle)\n", multiplier=3)
                file.write('\n')

            if not ESPECodeGenerator.PSYSTEM_TOKENS["NO_EXTRA_MOVEMENT"]:
                ESPECodeGenerator.write_tabulate(file, "self.move_extra_prop_changer_func(particle)\n", multiplier=3)
                file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "particle.x, particle.y = self.positioning_func()\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "particle.cur_lifetime = 0.0\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.active = True\n", multiplier=3)
            file.write('\n')

            if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                ESPECodeGenerator.write_tabulate(file, "particle.update_child()\n", multiplier=3)
                       
        @staticmethod
        def file_psystem_class_choice_sprite_method(file):
            ESPECodeGenerator.write_tabulate(file, "def choice_sprite(self, particle):\n", multiplier=2)
            if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                ESPECodeGenerator.write_tabulate(file, "particle.displayable = renpy.random.choice(self.displayable_list)\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "particle.ready_to_set_child_t_obj = True\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "particle.transform_object.child = renpy.store.ImageReference(tuple(particle.displayable.split()))\n", multiplier=3)
            else:
                ESPECodeGenerator.write_tabulate(file, "particle.set_child(particle.displayable)\n", multiplier=3)

        @staticmethod
        def file_psystem_class_lifetime_behavior_method(file):
            ESPECodeGenerator.write_tabulate(file, "def lifetime_behavior(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "lifetime_difference = self.lifetime * self.lifetime_random\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.lifetime = random.uniform(self.lifetime - lifetime_difference, self.lifetime)\n", multiplier=3)

        @staticmethod
        def file_psystem_class_explosiveness_method(file):
            ESPECodeGenerator.write_tabulate(file, "def explosiveness_func(self):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "if len(self.inactive_particles) < self.explosiveness_amount:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "return False\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "return True\n", multiplier=3)

        @staticmethod
        def file_psystem_class_get_delta_frame_time_method(file):
            ESPECodeGenerator.write_tabulate(file, "def get_delta_frame_time(self, st):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "dtime = st - self.old_st\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.old_st = st\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "return dtime\n", multiplier=3)

        @staticmethod
        def file_psystem_class_dot_emitter_method(file):
            ESPECodeGenerator.write_tabulate(file, "def dot_emitter(self):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "return self.dot_emitter_pos\n", multiplier=3)

        @staticmethod
        def file_psystem_class_rectangle_emitter_method(file):
            ESPECodeGenerator.write_tabulate(file, "def rectangle_emitter(self):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "x_border = self.rectangle_spawn_area[0] >> 1\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "y_border = self.rectangle_spawn_area[1] >> 1\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "x = self.rectangle_emitter_pos[0] + renpy.random.randint(-x_border, x_border + 1)\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "y = self.rectangle_emitter_pos[1] + renpy.random.randint(-y_border, y_border + 1)\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "return x, y\n", multiplier=3)

        @staticmethod
        def file_psystem_class_radial_emitter_method(file):
            ESPECodeGenerator.write_tabulate(file, "def radial_emitter(self):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "radius = float(renpy.random.randint(0, self.emitter_radius))\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "angle = renpy.random.randint(0, self.omath.trigonometric_len - 1)\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "x = self.radial_emitter_pos[0] + int(radius * self.omath.ocos_angle_d(angle))\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "y = self.radial_emitter_pos[1] + int(radius * self.omath.osin_angle_d(angle))\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "return x, y\n", multiplier=3)

        @staticmethod
        def file_psystem_class_screen_emitter_method(file):
            ESPECodeGenerator.write_tabulate(file, "def screen_emitter(self):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "x = renpy.random.randint(0, config.screen_width)\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "y = renpy.random.randint(0, config.screen_height)\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "return x, y\n", multiplier=3)

        @staticmethod
        def file_psystem_class_sides_emitter_method(file):
            ESPECodeGenerator.write_tabulate(file, "def sides_emitter(self):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "side = renpy.random.choice(self.out_of_bounds_spawn_dict.keys())\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "if side == \"Left\":\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "return (-120, renpy.random.randint(0, config.screen_height))\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "if side == \"Right\":\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "return (config.screen_width + 120, renpy.random.randint(0, config.screen_height))\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "if side == \"Top\":\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "return (renpy.random.randint(0, config.screen_width), -120)\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "if side == \"Bottom\":\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "return (renpy.random.randint(0, config.screen_width), config.screen_height + 120)\n", multiplier=4)

        @staticmethod
        def file_psystem_class_simple_move_method(file):
            ESPECodeGenerator.write_tabulate(file, "def simple_move(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "dx = particle.x_speed * self.frame_dtime\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "dy = particle.y_speed * self.frame_dtime\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "particle.x += dx\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.y += dy\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "return True\n", multiplier=3)

        @staticmethod
        def file_psystem_class_accelerate_move_method(file): 
            ESPECodeGenerator.write_tabulate(file, "def accelerate_move(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.x_speed += particle.x_acceleration\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.y_speed += particle.y_acceleration\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "dx = particle.x_speed * self.frame_dtime\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "dy = particle.y_speed * self.frame_dtime\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "particle.x += dx\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.y += dy\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "return True\n", multiplier=3)

        @staticmethod
        def file_psystem_class_speed_changer_constant_method(file):
            ESPECodeGenerator.write_tabulate(file, "def speed_changer_constant(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.x_speed = self.max_x_speed\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.y_speed = self.max_y_speed\n", multiplier=3)

        @staticmethod
        def file_psystem_class_speed_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def speed_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.x_speed = renpy.random.uniform(self.min_x_speed, self.max_x_speed)\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.y_speed = renpy.random.uniform(self.min_y_speed, self.max_y_speed)\n", multiplier=3)

        @staticmethod
        def file_psystem_class_speed_accelerate_changer_constant_method(file):
            ESPECodeGenerator.write_tabulate(file, "def move_prop_static_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.x_speed = self.max_x_speed\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.y_speed = self.max_y_speed\n", multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "particle.x_acceleration = self.max_x_accelerate\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.y_acceleration = self.max_y_accelerate\n", multiplier=3)

        @staticmethod
        def file_psystem_class_speed_acc_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def speed_acc_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.x_speed = renpy.random.uniform(self.min_x_speed, self.max_x_speed)\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.y_speed = renpy.random.uniform(self.min_y_speed, self.max_y_speed)\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "particle.x_acceleration = renpy.random.uniform(self.min_x_accelerate, self.max_x_accelerate)\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.y_acceleration = renpy.random.uniform(self.min_y_accelerate, self.max_y_accelerate)\n", multiplier=3)

        @staticmethod
        def file_psystem_class_static_acc_speed_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def static_accelerate_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.x_speed = renpy.random.uniform(self.min_x_speed, self.max_x_speed)\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.y_speed = renpy.random.uniform(self.min_y_speed, self.max_y_speed)\n", multiplier=3)
            #if universal:

        @staticmethod
        def file_psystem_class_accelerate_changer_method(file):
            #if universal:
            ESPECodeGenerator.write_tabulate(file, "def accelerate_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.x_acceleration = renpy.random.uniform(self.min_x_accelerate, self.max_x_accelerate)\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.y_acceleration = renpy.random.uniform(self.min_y_accelerate, self.max_y_accelerate)\n", multiplier=3)

        @staticmethod
        def file_psystem_class_extra_move_oscillatory_method(file):
            ESPECodeGenerator.write_tabulate(file, "def extra_move_oscillatory(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "angle = int(particle.extra_move_phase + self.st * particle.speed_extra) % 360\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "dx = particle.radius_x_extra * self.omath.ocos_angle_d(angle)\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "dy = particle.radius_y_extra * self.omath.osin_angle_d(angle)\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "particle.x += dx - particle.last_x_offset\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.y += dy - particle.last_y_offset\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "particle.last_x_offset = dx\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.last_y_offset = dy\n", multiplier=3)

        @staticmethod
        def file_psystem_class_extra_move_speed_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def extra_move_speed_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.speed_extra = renpy.random.uniform(self.min_speed_oscillatory, self.max_speed_oscillatory)\n", multiplier=3)

        @staticmethod
        def file_psystem_class_extra_move_radius_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def extra_move_radius_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.radius_x_extra = renpy.random.uniform(self.min_x_oscillatory, self.max_x_oscillatory)\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.radius_y_extra = renpy.random.uniform(self.min_y_oscillatory, self.max_y_oscillatory)\n", multiplier=3)

        @staticmethod
        def file_psystem_class_extra_move_phase_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def extra_move_phase_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.extra_move_phase = renpy.random.uniform(0.0, 360.0)\n", multiplier=3)
        
        @staticmethod
        def file_psystem_class_extra_move_prop_changer_oscillatory_zip_method(file):
            ESPECodeGenerator.write_tabulate(file, "def extra_move_prop_changer_oscillatory_zip(self, particle):\n", multiplier=2)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_SPEED"]:
                ESPECodeGenerator.write_tabulate(file, "self.extra_move_speed_changer(particle)\n", multiplier=3)
            else:
                ESPECodeGenerator.write_tabulate(file, "particle.speed_extra = self.max_speed_oscillatory\n", multiplier=3)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_AMPLITUDE"]:
                ESPECodeGenerator.write_tabulate(file, "self.extra_move_radius_changer(particle)\n", multiplier=3)
            else:
                ESPECodeGenerator.write_tabulate(file, "particle.radius_x_extra = self.max_x_oscillatory\n", multiplier=3)
                ESPECodeGenerator.write_tabulate(file, "particle.radius_y_extra = self.max_y_oscillatory\n", multiplier=3)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_PHASE"]:
                ESPECodeGenerator.write_tabulate(file, "self.extra_move_phase_changer(particle)\n", multiplier=3)
            else:
                ESPECodeGenerator.write_tabulate(file, "particle.extra_move_phase = self.extra_move_phase\n", multiplier=3)

        @staticmethod
        def file_psystem_class_alpha_fade_in_out_func_method(file):
            ESPECodeGenerator.write_tabulate(file, "def alpha_fade_in_out_func(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "if particle.cur_lifetime < particle.alpha_appear_time_end:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "if particle.alpha_appear_time_end == 0.0:\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "return None\n", multiplier=5)
            ESPECodeGenerator.write_tabulate(file, "appear_normalized = particle.cur_lifetime / particle.alpha_appear_time_end\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha = particle.intermediate_alpha * appear_normalized * appear_normalized\n", multiplier=4)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "return None\n", multiplier=4)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "if particle.cur_lifetime < particle.alpha_disappear_time_start:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "return None\n", multiplier=4)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "if particle.cur_lifetime <= particle.lifetime:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "disappear_normalized = 1.0 - (particle.cur_lifetime - particle.alpha_disappear_time_start) / (particle.lifetime - particle.alpha_disappear_time_start)\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha = particle.intermediate_alpha - particle.intermediate_alpha * (-(disappear_normalized * disappear_normalized) + 1.0)\n", multiplier=4)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "return None\n", multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "particle.alpha = 0.0\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "return None\n", multiplier=3)

        @staticmethod
        def file_psystem_class_alpha_oscillatory_func_method(file):
            ESPECodeGenerator.write_tabulate(file, "def alpha_oscillatory_func(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "angle = int(particle.alpha_phase + self.st * particle.alpha_speed) % 360\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha = particle.intermediate_alpha * self.omath.osin_angle_d(angle)\n", multiplier=3)
        
        @staticmethod
        def file_psystem_class_alpha_static_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def alpha_static_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha = renpy.random.uniform(self.intermediate_min_alpha, self.intermediate_max_alpha)\n", multiplier=3)
        
        @staticmethod
        def file_psystem_class_alpha_fade_in_out_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def alpha_fade_in_out_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha = 0.0\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.intermediate_alpha = renpy.random.uniform(self.intermediate_min_alpha, self.intermediate_max_alpha)\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "if self.alpha_appear_time_percentage == 0.0:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha_appear_time_end = 0.01\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha_appear_time_end = particle.lifetime * self.alpha_appear_time_percentage\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "if self.alpha_disappear_time_percentage == 0.0:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha_disappear_time_start = 0.01\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha_disappear_time_start = particle.lifetime - particle.lifetime * self.alpha_disappear_time_percentage\n", multiplier=3)

        @staticmethod
        def file_psystem_class_alpha_fade_in_out_changer_constant_method(file):
            ESPECodeGenerator.write_tabulate(file, "def alpha_fade_in_out_constant_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha = 0.0\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "if self.alpha_appear_time_percentage == 0.0:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha_appear_time_end = 0.01\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha_appear_time_end = particle.lifetime * self.alpha_appear_time_percentage\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "if self.alpha_disappear_time_percentage == 0.0:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha_disappear_time_start = 0.01\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha_disappear_time_start = particle.lifetime - particle.lifetime * self.alpha_disappear_time_percentage\n", multiplier=3)

        @staticmethod
        def file_psystem_class_alpha_oscillatory_speed_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def alpha_oscillatory_speed_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha_speed = renpy.random.uniform(self.alpha_min_speed, self.alpha_max_speed)\n", multiplier=3)

        @staticmethod
        def file_psystem_class_alpha_oscillatory_phase_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def alpha_oscillatory_phase_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.alpha_phase = renpy.random.uniform(0.0, 360.0)\n", multiplier=3)
        
        @staticmethod
        def file_psystem_class_alpha_oscillatory_changer_zip_method(file):
            ESPECodeGenerator.write_tabulate(file, "def alpha_oscillatory_changer_zip(self, particle):\n", multiplier=2)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_TRANSPARENCY"]:
                ESPECodeGenerator.write_tabulate(file, "self.alpha_static_changer(particle)\n", multiplier=3)
            else:
                ESPECodeGenerator.write_tabulate(file, "particle.alpha = self.intermediate_max_alpha\n", multiplier=3)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_SPEED"]:
                ESPECodeGenerator.write_tabulate(file, "self.alpha_oscillatory_speed_changer(particle)\n", multiplier=3)
            else:
                ESPECodeGenerator.write_tabulate(file, "particle.alpha_speed = self.alpha_max_speed\n", multiplier=3)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_PHASE"]:
                ESPECodeGenerator.write_tabulate(file, "self.alpha_oscillatory_phase_changer(particle)\n", multiplier=3) 
            else:
                ESPECodeGenerator.write_tabulate(file, "particle.alpha_phase = self.alpha_phase\n", multiplier=3)           

        @staticmethod
        def file_psystem_class_zoom_fade_in_out_func_method(file):
            ESPECodeGenerator.write_tabulate(file, "def zoom_fade_in_out_func(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "if particle.cur_lifetime < particle.zoom_appear_time_end:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "appear_normalized = particle.cur_lifetime / particle.zoom_appear_time_end\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom = particle.intermediate_zoom * appear_normalized * appear_normalized\n", multiplier=4)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "return None\n", multiplier=4)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "if particle.cur_lifetime < particle.zoom_disappear_time_start:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "return None\n", multiplier=4)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "if particle.cur_lifetime <= particle.lifetime:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "disappear_normalized = 1.0 - (particle.cur_lifetime - particle.zoom_disappear_time_start) / (particle.lifetime - particle.zoom_disappear_time_start)\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom = particle.intermediate_zoom - particle.intermediate_zoom * (-(disappear_normalized * disappear_normalized) + 1.0)\n", multiplier=4)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "return None\n", multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "particle.zoom = 0.0\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "return None\n", multiplier=3)

        @staticmethod
        def file_psystem_class_zoom_oscillatory_func_method(file):
            ESPECodeGenerator.write_tabulate(file, "def zoom_oscillatory_func(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "angle = int(particle.zoom_phase + self.st * particle.zoom_speed) % 360\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom = particle.intermediate_zoom * self.omath.osin_angle_d(angle)\n", multiplier=3)
        
        @staticmethod
        def file_psystem_class_zoom_static_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def zoom_static_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom = renpy.random.uniform(self.intermediate_min_zoom, self.intermediate_max_zoom)\n", multiplier=3)
        
        @staticmethod
        def file_psystem_class_zoom_fade_in_out_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def zoom_fade_in_out_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom = 0.0\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.intermediate_zoom = renpy.random.uniform(self.intermediate_min_zoom, self.intermediate_max_zoom)\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "if self.zoom_appear_time_percentage == 0.0:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom_appear_time_end = 0.01\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom_appear_time_end = particle.lifetime * self.zoom_appear_time_percentage\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "if self.zoom_disappear_time_percentage == 0.0:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom_disappear_time_start = 0.01\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom_disappear_time_start = particle.lifetime - particle.lifetime * self.zoom_disappear_time_percentage\n", multiplier=3)

        @staticmethod
        def file_psystem_class_zoom_fade_in_out_changer_constant_method(file):
            ESPECodeGenerator.write_tabulate(file, "def zoom_fade_in_out_constant_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom = 0.0\n", multiplier=3)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "if self.zoom_appear_time_percentage == 0.0:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom_appear_time_end = 0.01\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom_appear_time_end = particle.lifetime * self.zoom_appear_time_percentage\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "if self.zoom_disappear_time_percentage == 0.0:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom_disappear_time_start = 0.01\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom_disappear_time_start = particle.lifetime - particle.lifetime * self.zoom_disappear_time_percentage\n", multiplier=3)

        @staticmethod
        def file_psystem_class_zoom_oscillatory_speed_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def zoom_oscillatory_speed_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom_speed = renpy.random.uniform(self.zoom_min_speed, self.zoom_max_speed)\n", multiplier=3)

        @staticmethod
        def file_psystem_class_zoom_oscillatory_phase_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def zoom_oscillatory_phase_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.zoom_phase = renpy.random.uniform(0.0, 360.0)\n", multiplier=3)
        
        @staticmethod
        def file_psystem_class_zoom_oscillatory_changer_zip_method(file):
            ESPECodeGenerator.write_tabulate(file, "def zoom_oscillatory_changer_zip(self, particle):\n", multiplier=2)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_SCALE"]:
                ESPECodeGenerator.write_tabulate(file, "self.zoom_static_changer(particle)\n", multiplier=3)
            else:
                ESPECodeGenerator.write_tabulate(file, "particle.zoom = self.intermediate_max_zoom\n", multiplier=3)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_SPEED"]:
                ESPECodeGenerator.write_tabulate(file, "self.zoom_oscillatory_speed_changer(particle)\n", multiplier=3)
            else:
                ESPECodeGenerator.write_tabulate(file, "particle.zoom_speed = self.zoom_max_speed\n", multiplier=3)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_PHASE"]:
                ESPECodeGenerator.write_tabulate(file, "self.zoom_oscillatory_phase_changer(particle)\n", multiplier=3) 
            else:
                ESPECodeGenerator.write_tabulate(file, "particle.zoom_phase = self.zoom_phase\n", multiplier=3)

        @staticmethod
        def file_psystem_class_dynamic_rotate_func_method(file):
            ESPECodeGenerator.write_tabulate(file, "def dynamic_rotate_func(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.angle += particle.rotate_speed * self.frame_dtime\n", multiplier=3)

        @staticmethod
        def file_psystem_class_dynamic_rotate_start_angle_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def dynamic_rotate_start_angle_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.angle = renpy.random.uniform(self.dynamic_rotate_min_start_angle, self.dynamic_rotate_max_start_angle)\n", multiplier=3)

        @staticmethod
        def file_psystem_class_dynamic_rotate_speed_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def dynamic_rotate_speed_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.rotate_speed = renpy.random.uniform(self.dynamic_rotate_min_speed, self.dynamic_rotate_max_speed)\n", multiplier=3)
        
        @staticmethod
        def file_psystem_class_dynamic_rotate_changer_zip_method(file):
            ESPECodeGenerator.write_tabulate(file, "def dynamic_rotate_changer_zip(self, particle):\n", multiplier=2)

            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["DYNAMIC_ROTATE_RANDOM_START_ANGLE"]:
                ESPECodeGenerator.write_tabulate(file, "self.dynamic_rotate_start_angle_changer(particle)\n", multiplier=3)
            else:
                ESPECodeGenerator.write_tabulate(file, "particle.angle = self.dynamic_rotate_max_start_angle\n", multiplier=3)
            if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["DYNAMIC_ROTATE_RANDOM_SPEED"]:
                ESPECodeGenerator.write_tabulate(file, "self.dynamic_rotate_speed_changer(particle)\n", multiplier=3)
            else:
                ESPECodeGenerator.write_tabulate(file, "particle.rotate_speed = self.rotate_max_speed\n", multiplier=3)
        
        @staticmethod
        def file_psystem_class_rotate_by_speed_method(file):
            ESPECodeGenerator.write_tabulate(file, "def dynamic_rotate_func(self, particle):\n", multiplier=2)
            if ESPECodeGenerator.PSYSTEM_TOKENS["ROTATE_BY_SPEED_X"]:
                ESPECodeGenerator.write_tabulate(file, "particle.angle = self.rotate_by_speed_start_angle + math.degrees(math.atan2(particle.x_speed, self.rotate_by_speed_max_speed)) * math.copysign(1, particle.y_speed)\n", multiplier=3)
            elif ESPECodeGenerator.PSYSTEM_TOKENS["ROTATE_BY_SPEED_Y"]:
                ESPECodeGenerator.write_tabulate(file, "particle.angle = self.rotate_by_speed_start_angle + math.degrees(math.atan2(particle.y_speed, self.rotate_by_speed_max_speed)) * math.copysign(1, particle.x_speed)\n", multiplier=3)

        @staticmethod
        def file_psystem_class_rotate_by_speed_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "rotate_by_speed_changer(self, particle):\n", multiplier=2)
            if ESPECodeGenerator.PSYSTEM_TOKENS["ROTATE_BY_SPEED_X"]:
                ESPECodeGenerator.write_tabulate(file, "particle.angle = self.rotate_by_speed_start_angle + math.degrees(math.atan2(particle.x_speed, self.rotate_by_speed_max_speed)) * math.copysign(1, particle.y_speed)\n", multiplier=3)
            elif ESPECodeGenerator.PSYSTEM_TOKENS["ROTATE_BY_SPEED_Y"]:
                ESPECodeGenerator.write_tabulate(file, "particle.angle = self.rotate_by_speed_start_angle + math.degrees(math.atan2(particle.y_speed, self.rotate_by_speed_max_speed)) * math.copysign(1, particle.x_speed)\n", multiplier=3)

        @staticmethod
        def file_psystem_class_rotate_static_changer_method(file):
            ESPECodeGenerator.write_tabulate(file, "def rotate_static_changer(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle.angle = renpy.random.uniform(self.min_angle, self.max_angle)\n", multiplier=3)
        
        @staticmethod
        def file_psystem_class_from_active_to_inactive_method(file):
            ESPECodeGenerator.write_tabulate(file, "def from_active_to_inactive(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "self.active_particles.remove(particle)\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.inactive_particles.append(particle)\n", multiplier=3)
        
        @staticmethod
        def file_psystem_class_from_inactive_to_active_method(file):
            ESPECodeGenerator.write_tabulate(file, "def from_inactive_to_active(self, particle):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "self.inactive_particles.remove(particle)\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.active_particles.append(particle)\n", multiplier=3)

        @staticmethod
        def file_psystem_class_psystem_reset(file):
            ESPECodeGenerator.write_tabulate(file, "def psystem_reset(self):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "for particle in reversed(self.active_particles):\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.from_active_to_inactive(particle)\n", multiplier=4)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "for index, particle in enumerate(self.inactive_particles):\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "if getattr(self, \"lifetime_spread_random\", None) is None:\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "appear_delay = self.lifetime_spread\n", multiplier=5)
            ESPECodeGenerator.write_tabulate(file, "else:\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "appear_delay = renpy.random.uniform(self.lifetime_spread * self.lifetime_spread_random, self.lifetime_spread)\n", multiplier=5)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "particle.appear_delay = appear_delay * index\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle.cur_appear_delay = 0.0\n", multiplier=4)
            if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                ESPECodeGenerator.write_tabulate(file, "particle.alpha = 0.0\n", multiplier=4)
            else:
                ESPECodeGenerator.write_tabulate(file, "particle.y = config.screen_height + 10\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle.active = False\n", multiplier=4)

        @staticmethod
        def file_psystem_class_show_psystem(file):
            ESPECodeGenerator.write_tabulate(file, "def show(self, transition=None, reset=True):\n", multiplier=2)
            if ESPECodeGenerator.PSYSTEM_TOKENS["INNER_FRAME_CHECK"]:
                ESPECodeGenerator.write_tabulate(file, "self.old_st = 0.0\n", multiplier=3)
                file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "if reset:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.psystem_reset()\n", multiplier=4)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "self.manager.redraw(0.0)\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "renpy.show(name=\"{}_psystem\", what=self.manager)\n".format(ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()), multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "if transition is not None:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "renpy.with_statement(transition)\n".format(ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()), multiplier=4)

        @staticmethod
        def file_psystem_class_hide_psystem(file):
            ESPECodeGenerator.write_tabulate(file, "def hide(self, transition=None):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "renpy.hide(name=\"{}_psystem\")\n".format(ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()), multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "if transition is not None:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "renpy.with_statement(transition)\n".format(ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()), multiplier=4)

        #############################################################################################################

        ##СВОЙСТВА СИСТЕМЫ.##
        #############################################################################################################

        @staticmethod
        def file_psystem_attr_dict(file):
            ESPECodeGenerator.write_tabulate(file, "espe_{}_properties = {{\n".format(ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()))
            ESPECodeGenerator.write_tabulate(file, "\"displayable_list\": , #<Спрайты для системы частиц <Имя спрайта в кавычках или список спрайтов в кавычках каждый через запятую.>>;\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "\"amount\": {}, #<Количество частиц в системе <Целое число>>;\n".format(espe_editor_data.p_amount), multiplier=2)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "\"lifetime\": {:0.3f}, #<Время жизни частиц <Секунды>>;\n".format(espe_editor_data.p_lifetime), multiplier=2)
            if ESPECodeGenerator.PSYSTEM_TOKENS["RANDOM_LIFETIME"]:
                ESPECodeGenerator.write_tabulate(file, "\"lifetime_random\": {:0.3f}, #<Разброс времени жизни <Коэффициент от 0.0 до 1.0>>;\n".format(espe_editor_data.p_lifetime_random), multiplier=2)

            ESPECodeGenerator.write_tabulate(file, "\"lifetime_spread\": {:0.3f}, #<Задержка появления <Секунды>>;\n".format(espe_editor_data.p_lifetime_spread), multiplier=2)
            if ESPECodeGenerator.PSYSTEM_TOKENS["RANDOM_APPEAR_DELAY"]:
                ESPECodeGenerator.write_tabulate(file, "\"lifetime_spread_random\": {:0.3f}, #<Разброс времени появления <Коэффициент от 0.0 до 1.0>>;\n".format(espe_editor_data.p_lifetime_spread_random), multiplier=2)
            file.write('\n')

            if ESPECodeGenerator.PSYSTEM_TOKENS["EXPLOSIVENESS"]:
                ESPECodeGenerator.write_tabulate(file, "\"explosiveness_factor\": {:0.3f}, #<Сила взрывчатости <Коэффициент от 0.0 до 1.0>>;\n".format(espe_editor_data.p_explosiveness_factor), multiplier=2)
                file.write('\n')

            if ESPECodeGenerator.PSYSTEM_TOKENS["DOT_EMITTER"]:
                ESPECodeGenerator.write_tabulate(file, "\"dot_emitter_pos\": [{}, {}], #<Позиция точечного испускателя <Два целых числа в квадратных скобках через запятую>>;\n".format(*espe_editor_data.p_emitter_pos), multiplier=2)
            if ESPECodeGenerator.PSYSTEM_TOKENS["RECTANGLE_EMITTER"]:
                ESPECodeGenerator.write_tabulate(file, "\"rectangle_emitter_pos\": [{}, {}], #<Позиция прямоугольного испускателя <Два целых числа в квадратных скобках через запятую>>;\n".format(*espe_editor_data.p_rectangle_emitter_pos), multiplier=2)
                ESPECodeGenerator.write_tabulate(file, "\"rectangle_spawn_area\": [{}, {}], #<Размер зоны испускания испускателя <Два целых числа в квадратных скобках через запятую>>;\n".format(*espe_editor_data.p_rectangle_spawn_area), multiplier=2)
            if ESPECodeGenerator.PSYSTEM_TOKENS["RADIAL_EMITTER"]:
                ESPECodeGenerator.write_tabulate(file, "\"radial_emitter_pos\": [{}, {}], #<Позиция радиального испускателя <Два целых числа в квадратных скобках через запятую>>;\n".format(*espe_editor_data.p_radial_emitter_pos), multiplier=2)
                ESPECodeGenerator.write_tabulate(file, "\"emitter_radius\": {}, #<Размер зоны радиального испускателя <Целое число>>;\n".format(espe_editor_data.p_emitter_radius), multiplier=2)
            if ESPECodeGenerator.PSYSTEM_TOKENS["SIDES_EMITTER"]:
                ESPECodeGenerator.write_tabulate(file, "\"out_of_bounds_spawn_dict\": {}, #<Границы испукания <True – включёна, False – отключена>>;\n".format(str(espe_editor_data.p_out_of_bounds_spawn_dict).replace('u\'', '\"').replace('\':', '\":')), multiplier=2)
            if not ESPECodeGenerator.PSYSTEM_TOKENS["SCREEN_EMITTER"]:
                file.write('\n')

            if not ESPECodeGenerator.PSYSTEM_TOKENS["STATIC_MOVE"]:
                ESPECodeGenerator.write_tabulate(file, "\"max_x_speed\": {:0.3f}, #<Горизонтальная скорость частиц <Число с плавающей точкой>>;\n".format(espe_editor_data.p_max_x_speed - 1000.0), multiplier=2)
                ESPECodeGenerator.write_tabulate(file, "\"max_y_speed\": {:0.3f}, #<Вертикальная скорость частиц <Число с плавающей точкой>>;\n".format(espe_editor_data.p_max_y_speed - 1000.0), multiplier=2)
                if any([ESPECodeGenerator.CHANGER_FUNCS_TOKENS["SIMPLE_MOVE_RANDOM_SPEED"], ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_SPEED"]]):
                    ESPECodeGenerator.write_tabulate(file, "\"min_x_speed\": {:0.3f}, #<Горизонтальная скорость частиц (граница 2) <Число с плавающей точкой>>;\n".format(espe_editor_data.p_min_x_speed - 1000.0), multiplier=2)
                    ESPECodeGenerator.write_tabulate(file, "\"min_y_speed\": {:0.3f}, #<Вертикальная скорость частиц (граница 2) <Число с плавающей точкой>>;\n".format(espe_editor_data.p_min_y_speed - 1000.0), multiplier=2)
                    file.write('\n')
                else:
                    file.write('\n')
            
            if ESPECodeGenerator.PSYSTEM_TOKENS["ACCELERATE_MOVE"]:
                ESPECodeGenerator.write_tabulate(file, "\"max_x_accelerate\": {:0.3f}, #<Горизонтальное ускорение частиц <Число с плавающей точкой>>;\n".format(espe_editor_data.p_max_x_accelerate - 100.0), multiplier=2)
                ESPECodeGenerator.write_tabulate(file, "\"max_y_accelerate\": {:0.3f}, #<Вертикальное ускорение частиц <Число с плавающей точкой>>;\n".format(espe_editor_data.p_max_y_accelerate - 100.0), multiplier=2)
                if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_ACCELERATE"]:
                    ESPECodeGenerator.write_tabulate(file, "\"min_x_accelerate\": {:0.3f}, #<Горизонтальное ускорение частиц (граница 2) <Число с плавающей точкой>>;\n".format(espe_editor_data.p_min_x_accelerate - 100.0), multiplier=2)
                    ESPECodeGenerator.write_tabulate(file, "\"min_y_accelerate\": {:0.3f}, #<Вертикальное ускорение частиц (граница 2) <Число с плавающей точкой>>;\n".format(espe_editor_data.p_min_y_accelerate - 100.0), multiplier=2)
                    file.write('\n')
                else:
                    file.write('\n')
            
            if ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_EXTRA_MOVEMENT"]:
                ESPECodeGenerator.write_tabulate(file, "\"max_speed_oscillatory\": {:0.3f}, #<Скорость колебания частиц <Число с плавающей точкой>>;\n".format(espe_editor_data.p_max_speed_oscillatory - 1000.0), multiplier=2)
                if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_SPEED"]:
                    ESPECodeGenerator.write_tabulate(file, "\"min_speed_oscillatory\": {:0.3f}, #<Скорость колебания частиц (граница 2) <Число с плавающей точкой>>;\n".format(espe_editor_data.p_min_speed_oscillatory - 1000.0), multiplier=2)
                ESPECodeGenerator.write_tabulate(file, "\"max_x_oscillatory\": {:0.3f}, #<Горизонтальная амплитуда колебания <Число с плавающей точкой>>;\n".format(espe_editor_data.p_max_x_oscillatory), multiplier=2)
                ESPECodeGenerator.write_tabulate(file, "\"max_y_oscillatory\": {:0.3f}, #<Вертикальная амплитуда колебания <Число с плавающей точкой>>;\n".format(espe_editor_data.p_max_y_oscillatory), multiplier=2)
                if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_AMPLITUDE"]:
                    ESPECodeGenerator.write_tabulate(file, "\"min_x_oscillatory\": {:0.3f}, #<Горизонтальная амплитуда колебания (граница 2) <Число с плавающей точкой>>;\n".format(espe_editor_data.p_min_x_oscillatory), multiplier=2)
                    ESPECodeGenerator.write_tabulate(file, "\"min_y_oscillatory\": {:0.3f}, #<Вертикальная амплитуда колебания (граница 2) <Число с плавающей точкой>>;\n".format(espe_editor_data.p_min_y_oscillatory), multiplier=2)
                if not ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_PHASE"]:
                    ESPECodeGenerator.write_tabulate(file, "\"extra_phase\": {:0.3f}, #<Начальная фаза колебания <Число с плавающей точкой от 0.0 до 360.0>>;\n".format(espe_editor_data.p_extra_phase), multiplier=2)
                file.write('\n')

            if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                ESPECodeGenerator.write_tabulate(file, "\"intermediate_max_alpha\": {:0.3f}, #<Непрозрачность частиц <Число с плавающей точкой от 0.0 до 1.0>>;\n".format(espe_editor_data.p_intermediate_max_alpha), multiplier=2)
                if any([ESPECodeGenerator.CHANGER_FUNCS_TOKENS["STATIC_ALPHA_RANDOM_TRANSPARENCY"], ESPECodeGenerator.CHANGER_FUNCS_TOKENS["FADE_IN_OUT_ALPHA_RANDOM_TRANSPARENCY"], ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_TRANSPARENCY"]]):
                    ESPECodeGenerator.write_tabulate(file, "\"intermediate_min_alpha\": {:0.3f}, #<Непрозрачность частиц (граница 2) <Число с плавающей точкой от 0.0 до 1.0>>;\n".format(espe_editor_data.p_intermediate_min_alpha), multiplier=2)
                if ESPECodeGenerator.PSYSTEM_TOKENS["FADE_IN_OUT_ALPHA"]:
                    ESPECodeGenerator.write_tabulate(file, "\"alpha_appear_time_percentage\": {:0.3f}, #<Время появления <Число с плавающей точкой от 0.0 до 1.0>>;\n".format(espe_editor_data.p_alpha_appear_time_percentage), multiplier=2)
                    ESPECodeGenerator.write_tabulate(file, "\"alpha_disappear_time_percentage\": {:0.3f}, #<Время затухания <Число с плавающей точкой от 0.0 до 1.0>>;\n".format(espe_editor_data.p_alpha_disappear_time_percentage), multiplier=2)
                if ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_ALPHA"]:
                    ESPECodeGenerator.write_tabulate(file, "\"alpha_max_speed\": {:0.3f}, #<Скорость колебания непрозрачности частиц <Число с плавающей точкой>>;\n".format(espe_editor_data.p_alpha_max_speed), multiplier=2)
                    if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_SPEED"]:
                        ESPECodeGenerator.write_tabulate(file, "\"alpha_min_speed\": {:0.3f}, #<Скорость колебания непрозрачности частиц (граница 2) <Число с плавающей точкой>>;\n".format(espe_editor_data.p_alpha_min_speed), multiplier=2)
                    if not ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_PHASE"]:
                        ESPECodeGenerator.write_tabulate(file, "\"alpha_phase\": {:0.3f}, #<Начальная фаза колебания непрозрачности <Число с плавающей точкой от 0.0 до 360.0>>;\n".format(espe_editor_data.p_alpha_phase), multiplier=2)
                file.write('\n')

                ESPECodeGenerator.write_tabulate(file, "\"intermediate_max_zoom\": {:0.3f}, #<Масштаб частиц <Число с плавающей точкой>>;\n".format(espe_editor_data.p_intermediate_max_zoom), multiplier=2)
                if any([ESPECodeGenerator.CHANGER_FUNCS_TOKENS["STATIC_ZOOM_RANDOM_SCALE"], ESPECodeGenerator.CHANGER_FUNCS_TOKENS["FADE_IN_OUT_ZOOM_RANDOM_SCALE"], ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_SCALE"]]):
                    ESPECodeGenerator.write_tabulate(file, "\"intermediate_min_zoom\": {:0.3f}, #<Масштаб частиц (граница 2) <Число с плавающей точкой>>;\n".format(espe_editor_data.p_intermediate_min_zoom), multiplier=2)
                if ESPECodeGenerator.PSYSTEM_TOKENS["FADE_IN_OUT_ZOOM"]:
                    ESPECodeGenerator.write_tabulate(file, "\"zoom_appear_time_percentage\": {:0.3f}, #<Время появления <Число с плавающей точкой>>;\n".format(espe_editor_data.p_zoom_appear_time_percentage), multiplier=2)
                    ESPECodeGenerator.write_tabulate(file, "\"zoom_disappear_time_percentage\": {:0.3f}, #<Время затухания <Число с плавающей точкой>>;\n".format(espe_editor_data.p_zoom_disappear_time_percentage), multiplier=2)
                if ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_ZOOM"]:
                    ESPECodeGenerator.write_tabulate(file, "\"zoom_max_speed\": {:0.3f}, #<Скорость колебания Масштаба частиц <Число с плавающей точкой>>;\n".format(espe_editor_data.p_zoom_max_speed), multiplier=2)
                    if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_SPEED"]:
                        ESPECodeGenerator.write_tabulate(file, "\"zoom_min_speed\": {:0.3f}, #<Скорость колебания Масштаба частиц (граница 2) <Число с плавающей точкой>>;\n".format(espe_editor_data.p_zoom_min_speed), multiplier=2)
                    if not ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_PHASE"]:
                        ESPECodeGenerator.write_tabulate(file, "\"zoom_phase\": {:0.3f}, #<Начальная фаза колебания Масштаба <Число с плавающей точкой от 0.0 до 360.0>>;\n".format(espe_editor_data.p_zoom_phase), multiplier=2)
                file.write('\n')

                if not ESPECodeGenerator.PSYSTEM_TOKENS["ROTATE_BY_SPEED"]:
                    if ESPECodeGenerator.PSYSTEM_TOKENS["STATIC_ROTATE"]:
                        ESPECodeGenerator.write_tabulate(file, "\"max_angle\": {:0.3f}, #<Угол вращения <Число с плавающей точкой от 0.0 до 360.0>>;\n".format(espe_editor_data.p_max_angle), multiplier=2)
                    if ESPECodeGenerator.PSYSTEM_TOKENS["DYNAMIC_ROTATE"]:
                        ESPECodeGenerator.write_tabulate(file, "\"dynamic_rotate_max_start_angle\": {:0.3f}, #<Начальный угол вращения <Число с плавающей точкой от 0.0 до 360.0>>;\n".format(espe_editor_data.p_dynamic_rotate_max_start_angle), multiplier=2)
                        if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["DYNAMIC_ROTATE_RANDOM_START_ANGLE"]:
                            ESPECodeGenerator.write_tabulate(file, "\"dynamic_rotate_min_start_angle\": {:0.3f}, #<Начальный угол вращения (граница 2) <Число с плавающей точкой от 0.0 до 360.0>>;\n".format(espe_editor_data.p_dynamic_rotate_min_start_angle), multiplier=2)
                        
                        ESPECodeGenerator.write_tabulate(file, "\"dynamic_rotate_max_speed\": {:0.3f}, #<Скорость вращения <Число с плавающей точкой>>;\n".format(espe_editor_data.p_dynamic_rotate_max_speed - 1000.0), multiplier=2)
                        if ESPECodeGenerator.CHANGER_FUNCS_TOKENS["DYNAMIC_ROTATE_RANDOM_SPEED"]:
                            ESPECodeGenerator.write_tabulate(file, "\"dynamic_rotate_min_speed\": {:0.3f}, #<Скорость вращения (граница 2) <Число с плавающей точкой>>;\n".format(espe_editor_data.p_dynamic_rotate_min_speed - 1000.0), multiplier=2)
                else:
                    ESPECodeGenerator.write_tabulate(file, "\"rotate_by_speed_start_angle\": {:0.3f}, #<Базовый угол вращения <Число с плавающей точкой от 0.0 до 360.0>>;\n".format(espe_editor_data.p_rotate_by_speed_start_angle), multiplier=2)
                    ESPECodeGenerator.write_tabulate(file, "\"rotate_by_speed_max_speed\": {:0.3f}, #<Максимальная скорость вращения <Число с плавающей точкой от 0.0 до 360.0>>;\n".format(espe_editor_data.p_rotate_by_speed_max_speed - 1000.0), multiplier=2)
                file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "\"update_time\": {:0.3f}, #<Задержка перед вызовом функции обновления отрисовки <Секунды>>.\n".format(espe_editor_data.p_update_time), multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "}\n")

        #############################################################################################################

        ##FAST MATH.##
        #############################################################################################################

        @staticmethod
        def file_fast_math(file):
            ESPECodeGenerator.write_tabulate(file, "class ESPEOptimizedValues(object):\n")
            ESPECodeGenerator.write_tabulate(file, "def __init__(self, step=0.0625):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "self.trigonometric_step = step\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.sin_values = [math.sin(math.radians(x)) for x in range(-180, 180)]\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "self.cos_values = [math.cos(math.radians(x)) for x in range(-180, 180)]\n", multiplier=3)

            ESPECodeGenerator.write_tabulate(file, "self.trigonometric_len = len(self.sin_values)\n", multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "def osin_t(self, abs_time):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "return self.sin_values[int(round(self.trigonometric_len * abs_time))]\n", multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "def ocos_t(self, abs_time):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "return self.cos_values[int(round(self.trigonometric_len * abs_time))]\n", multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "def osin_random(self):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "return renpy.random.choice(self.sin_values)\n", multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "def ocos_random(self):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "return renpy.random.choice(self.cos_values)\n", multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "def osin_angle_d(self, degree):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "return self.sin_values[degree]\n", multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "def ocos_angle_d(self, degree):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "return self.cos_values[degree]\n", multiplier=3)

        #############################################################################################################

        ##ФУНКЦИЯ СБРОСА.##
        #############################################################################################################

        @staticmethod
        def file_psystem_reset(file):
            ESPECodeGenerator.write_tabulate(file, "def espe_psystem_reset_func(psystem_class):\n")
            ESPECodeGenerator.write_tabulate(file, "active_particles_len = len(psystem_class.active_particles)\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "inactive_particles_len = len(psystem_class.inactive_particles)\n", multiplier=2)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "for _ in range(active_particles_len):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle = psystem_class.active_particles.pop(0)\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.destroy()\n", multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "for _ in range(inactive_particles_len):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "particle = psystem_class.inactive_particles.pop(0)\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "particle.destroy()\n", multiplier=3)
            file.write('\n')

            ESPECodeGenerator.write_tabulate(file, "for prt_index in range(psystem_class.amount):\n", multiplier=2)
            ESPECodeGenerator.write_tabulate(file, "if isinstance(psystem_class.displayable_list, list):\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "displ = renpy.random.choice(psystem_class.displayable_list)\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "else:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "displ = psystem_class.displayable_list\n", multiplier=4)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "if getattr(psystem_class, \"lifetime_spread_random\", None) is None:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "appear_delay = psystem_class.lifetime_spread * prt_index\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "else:\n", multiplier=3)
            ESPECodeGenerator.write_tabulate(file, "appear_delay = renpy.random.uniform(psystem_class.lifetime_spread * psystem_class.lifetime_spread_random, psystem_class.lifetime_spread * prt_index)\n", multiplier=4)
            ESPECodeGenerator.write_tabulate(file, "particle = psystem_class.particle_object(displayable=displ, manager=psystem_class.manager, psystem=psystem_class, appear_delay=appear_delay)\n", multiplier=3)
            file.write('\n')
            
            ESPECodeGenerator.write_tabulate(file, "psystem_class.inactive_particles.append(particle)\n", multiplier=3)
        
        ##ФУНКЦИЯ ОБНОВЛЕНИЯ.##
        #############################################################################################################

        @staticmethod
        def file_sprite_manager_update_func(file):
            ESPECodeGenerator.write_tabulate(file, "def espe_{}_update_func(st):\n".format(ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()))
            ESPECodeGenerator.write_tabulate(file, "espe_{}_psystem_class.particles_process(st)\n".format(ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()), multiplier=2)
            file.write('\n')
            ESPECodeGenerator.write_tabulate(file, "return espe_{}_psystem_class.update_time\n".format(ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()), multiplier=2)
        
        #############################################################################################################

        #############################################################################################################

        ##СПРАЙТ МЕНЕДЖЕР.##
        #############################################################################################################

        @staticmethod
        def file_sprite_manager_class(file):
            psystem_lower = ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()
            ESPECodeGenerator.write_tabulate(file, "$ espe_{}_psystem = SpriteManager(update=espe_{}_update_func)\n".format(psystem_lower, psystem_lower))

        #############################################################################################################

        ##ИНИЦИАЛИЗАЦИЯ КЛАССА.##
        #############################################################################################################

        @staticmethod
        def file_psystem_init(file):
            psystem = ESPECodeGenerator.PSYSTEM_CODE_NAME
            psystem_lower = ESPECodeGenerator.PSYSTEM_CODE_NAME.lower()
            ESPECodeGenerator.write_tabulate(file, "$ espe_{}_psystem_class = ESPE{}PSystem(manager=espe_{}_psystem, **espe_{}_properties)\n".format(psystem_lower, psystem, psystem_lower, psystem_lower))

        #############################################################################################################

        @staticmethod
        def file_class(file):  
            ESPECodeGenerator.write_tabulate(file, "class ESPE{}Particle(renpy.object.Object):\n".format(ESPECodeGenerator.PSYSTEM_CODE_NAME))
            ESPECodeGenerator.write_tabulate(file, "def __init__(self, displayable, speed, speed_extra, accelerate)\n", multiplier=2)

        @staticmethod
        def write_tabulate(file, string, multiplier=1):
            file.write(ESPECodeGenerator.TABULATE * multiplier + string)
        
        @staticmethod
        def write_heading_name(file, name, tab_multiplier=1):
            file.write(ESPECodeGenerator.TABULATE * tab_multiplier + "##{}.##\n".format(name.upper()))

        @staticmethod
        def write_divider(file, tab_multiplier=1):
            file.write(ESPECodeGenerator.TABULATE * tab_multiplier + "#############################################################################################################\n")

        @staticmethod
        def analize_psystem():
            if espe_editor_data.psystem_type == "Простая":
                ESPECodeGenerator.PSYSTEM_TOKENS["SIMPLE_PSYSTEM"] = True
            if espe_editor_data.psystem_type == "Сложная":
                ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"] = True

            if len(espe_editor_data.p_displayable_list) > 1:
                ESPECodeGenerator.PSYSTEM_TOKENS["MULTIPLE_SPRITES"] = True

            if espe_editor_data.p_lifetime_random_enable:
                ESPECodeGenerator.PSYSTEM_TOKENS["RANDOM_LIFETIME"] = True
            if espe_editor_data.p_lifetime_random_spread_enable:
                ESPECodeGenerator.PSYSTEM_TOKENS["RANDOM_APPEAR_DELAY"] = True
            if espe_editor_data.p_is_explosiveness:
                ESPECodeGenerator.PSYSTEM_TOKENS["EXPLOSIVENESS"] = True

            if espe_editor_data.p_spawn_area_type == 0:
                ESPECodeGenerator.PSYSTEM_TOKENS["DOT_EMITTER"] = True
            if espe_editor_data.p_spawn_area_type == 1:
                ESPECodeGenerator.PSYSTEM_TOKENS["RECTANGLE_EMITTER"] = True
            if espe_editor_data.p_spawn_area_type == 2:
                ESPECodeGenerator.PSYSTEM_TOKENS["RADIAL_EMITTER"] = True
            if espe_editor_data.p_spawn_area_type == 3:
                ESPECodeGenerator.PSYSTEM_TOKENS["SCREEN_EMITTER"] = True
            if espe_editor_data.p_spawn_area_type == 4:
                ESPECodeGenerator.PSYSTEM_TOKENS["SIDES_EMITTER"] = True

            if espe_editor_data.p_move_type == 0:
                ESPECodeGenerator.PSYSTEM_TOKENS["STATIC_MOVE"] = True
            if espe_editor_data.p_move_type == 1:
                ESPECodeGenerator.PSYSTEM_TOKENS["SIMPLE_MOVE"] = True
                if espe_editor_data.p_speed_simple_move_changer_type:
                    ESPECodeGenerator.CHANGER_FUNCS_TOKENS["SIMPLE_MOVE_RANDOM_SPEED"] = True
            if espe_editor_data.p_move_type == 2:
                ESPECodeGenerator.PSYSTEM_TOKENS["ACCELERATE_MOVE"] = True
                if espe_editor_data.p_speed_accelerate_move_changer_type:
                    ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_SPEED"] = True
                if espe_editor_data.p_acc_accelerate_move_changer_type:
                    ESPECodeGenerator.CHANGER_FUNCS_TOKENS["ACCELERATE_MOVE_RANDOM_ACCELERATE"] = True

            if espe_editor_data.p_move_extra_type == 0:
                ESPECodeGenerator.PSYSTEM_TOKENS["NO_EXTRA_MOVEMENT"] = True
            if espe_editor_data.p_move_extra_type == 1:
                ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_EXTRA_MOVEMENT"] = True
                if espe_editor_data.p_speed_extra_changer_type:
                    ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_SPEED"] = True
                if espe_editor_data.p_radius_oscillatory_changer_type:
                    ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_AMPLITUDE"] = True
                if espe_editor_data.p_random_start_phase:
                    ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_EXTRA_MOVEMENT_RANDOM_PHASE"] = True
            

            if ESPECodeGenerator.PSYSTEM_TOKENS["COMPLEX_PSYSTEM"]:
                if espe_editor_data.p_alpha_type == 0:
                    ESPECodeGenerator.PSYSTEM_TOKENS["STATIC_ALPHA"] = True
                    if espe_editor_data.p_alpha_changer_static_type:
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["STATIC_ALPHA_RANDOM_TRANSPARENCY"] = True
                if espe_editor_data.p_alpha_type == 1:
                    ESPECodeGenerator.PSYSTEM_TOKENS["FADE_IN_OUT_ALPHA"] = True
                    if espe_editor_data.p_alpha_changer_fade_in_out_type:
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["FADE_IN_OUT_ALPHA_RANDOM_TRANSPARENCY"] = True
                if espe_editor_data.p_alpha_type == 2:
                    ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_ALPHA"] = True
                    if espe_editor_data.p_alpha_changer_oscillatory_type:
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_TRANSPARENCY"] = True
                    if espe_editor_data.p_alpha_changer_oscillatory_speed_type:
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_SPEED"] = True
                    if espe_editor_data.p_alpha_changer_oscillatory_phase_type:
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ALPHA_RANDOM_PHASE"] = True

                if espe_editor_data.p_zoom_type == 0:
                    ESPECodeGenerator.PSYSTEM_TOKENS["STATIC_ZOOM"] = True
                    if espe_editor_data.p_zoom_changer_static_type:
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["STATIC_ZOOM_RANDOM_SCALE"] = True
                if espe_editor_data.p_zoom_type == 1:
                    ESPECodeGenerator.PSYSTEM_TOKENS["FADE_IN_OUT_ZOOM"] = True
                    if espe_editor_data.p_zoom_changer_fade_in_out_type:
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["FADE_IN_OUT_ZOOM_RANDOM_SCALE"] = True
                if espe_editor_data.p_zoom_type == 2:
                    ESPECodeGenerator.PSYSTEM_TOKENS["OSCILLATORY_ZOOM"] = True
                    if espe_editor_data.p_zoom_changer_oscillatory_type:
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_SCALE"] = True
                    if espe_editor_data.p_zoom_changer_oscillatory_speed_type:
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_SPEED"] = True
                    if espe_editor_data.p_zoom_changer_oscillatory_phase_type:
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["OSCILLATORY_ZOOM_RANDOM_PHASE"] = True
                
                if espe_editor_data.p_rotate_type == 0:
                    ESPECodeGenerator.PSYSTEM_TOKENS["STATIC_ROTATE"] = True
                    if espe_editor_data.p_rotate_changer_static_type:
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["STATIC_ROTATE_RANDOM_ANGLE"] = True
                if espe_editor_data.p_rotate_type == 1:
                    ESPECodeGenerator.PSYSTEM_TOKENS["DYNAMIC_ROTATE"] = True
                    if espe_editor_data.p_dynamic_rotate_changer_angle_type:
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["DYNAMIC_ROTATE_RANDOM_START_ANGLE"] = True
                    if espe_editor_data.p_dynamic_rotate_changer_speed_type:
                        ESPECodeGenerator.CHANGER_FUNCS_TOKENS["DYNAMIC_ROTATE_RANDOM_SPEED"] = True
                if espe_editor_data.p_rotate_type == 2:
                    ESPECodeGenerator.PSYSTEM_TOKENS["ROTATE_BY_SPEED"] = True
                    if espe_editor_data.p_rotate_by_speed_type == 0:
                        ESPECodeGenerator.PSYSTEM_TOKENS["ROTATE_BY_SPEED_X"] = True
                    if espe_editor_data.p_rotate_by_speed_type == 1:
                        ESPECodeGenerator.PSYSTEM_TOKENS["ROTATE_BY_SPEED_Y"] = True
            
            if espe_editor_data.p_inner_frame_check:
                ESPECodeGenerator.PSYSTEM_TOKENS["INNER_FRAME_CHECK"] = True
            if espe_editor_data.p_is_screen_bounded:
                ESPECodeGenerator.PSYSTEM_TOKENS["IS_SCREEN_BOUNDED"] = True

        @staticmethod
        def reset_generator():
            for key in ESPECodeGenerator.PSYSTEM_TOKENS.keys():
                ESPECodeGenerator.PSYSTEM_TOKENS[key] = False
            for key in ESPECodeGenerator.CHANGER_FUNCS_TOKENS.keys():
                ESPECodeGenerator.CHANGER_FUNCS_TOKENS[key] = False
        
        @staticmethod
        def init_func_dict():
            ESPECodeGenerator.PSYSTEM_TOKEN_FUNCS = {
                "HEADING": ESPECodeGenerator.file_heading,

                "PARTICLE_OBJECT_CLASS_HEADING": ESPECodeGenerator.file_particle_class_heading,
                "PARTICLE_OBJECT_INIT": ESPECodeGenerator.file_particle_class_init,
                "PARTICLE_METHODS": ESPECodeGenerator.file_particle_class_methods,

                "PSYSTEM_CLASS_HEADING": ESPECodeGenerator.file_psystem_class_heading,
                "PSYSTEM_CLASS_INIT": ESPECodeGenerator.file_psystem_class_init, #Для удобства пользвотеля в этот класс будет передаваться **kwargs.
                "PSYSTEM_ATTR_DICT": ESPECodeGenerator.file_psystem_attr_dict, #Он будет вызываться где-то в самом конце или начале.
                "PSYSTEM_CLASS_METHODS": ESPECodeGenerator.file_psystem_class_methods,

                "SPRITE_MANAGER_UPDATE_FUNC": ESPECodeGenerator.file_sprite_manager_update_func,
                "SPRITE_MANAGER_CLASS": ESPECodeGenerator.file_sprite_manager_class,
                "PSYSTEM_INIT": ESPECodeGenerator.file_psystem_init,
                "PSYSTEM_RESET": ESPECodeGenerator.file_psystem_reset,

                "FAST_MATH_GENERATOR": ESPECodeGenerator.file_fast_math #Если было включено, то сгенерирует класс вычисленных заранее занчений тригонометрических функций.

                #"CODE_GENERATION_HARD": ESPECodeGenerator.file_code_generation_hard, #В эту функцию мы попадём в функции сборки класса системы. Это значит, что код будет сгенерирован так, что будет менее универсальным, но более производительным.
                #"CODE_GENERATION_HARD_PARTICLE_OBJECT_ATTR": ESPECodeGenerator.file_particle_class_hard_attr, #В эту функцию мы попадём в функции сборки класса класса одной частицы. Тоже самое, что для системы,  но для класса одной частицы.
                #"CODE_GENERATION_UNIVERSAL_PARTICLE_OBJECT_ATTR": ESPECodeGenerator.file_particle_class_universal_attr, #В эту функцию мы попадём в функции сборки класса класса одной частицы, если такая опция была выбрана. Это значит, что будут собраны все свойства частицы, даже которые не будут использоваться системой, сделанным в редакторе пользователя.
                #"CODE_GENERATION_UNIVERSAL_PSYSTEM": ESPECodeGenerator.file_code_generation_universal, #В эту функцию мы попадём в функции сборки класса системы, если такая опция была выбрана. Это значит, что будут собраны все методы, даже которые не будут использоваться системой, сделанным в редакторе пользователя.
                #"CODE_GENERATION_FULL_PSYSTEM": ESPECodeGenerator.file_code_generation_full, #Если пользователь выбрал полную систему, то будет сгенерирована абсолютно все доступные методы из редактора.
                #"CODE_GENERATION_UPDATE_FUNCS": ESPECodeGenerator.file_update_methods, #Если пользователь выбрал генерацию универсальной системы, то будут сгенерированы функции обновления свойств системы.
            }
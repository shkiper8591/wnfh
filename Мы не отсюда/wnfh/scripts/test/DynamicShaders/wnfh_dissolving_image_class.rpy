init 15 python:
    import builtins
    from renpy.uguu import GL_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT, GL_REPEAT

    WNFH_DS_GL_TEXTURE_WRAP_MODES = (GL_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT, GL_REPEAT)

    class DynamicDissolvingImage(renpy.Displayable):
        """
        `child`
            Отображаемый объект на которой будет накладываться шейдер.

        `noise_texture`
            Отображаемый объект, необходимый для создания динамического эффекта рассеивания.
            Вы можете использовать любую текстуру, но для идеального эффекта рекомендуется <бесшовная> и <чёрно-белая> текстура шума.

        `dissolve_power`
            float | int <Значение> Сила рассеивания. Чем выше, тем эффективнее светлые места в текстуре шума используются.
            Для данного параметра существует метод случайной генерации значеня: <random_dissolve_power(low_v=0.25, high_v=15.0)>.

        `smooth_power`
            float | int <Значение> Параметр, отвечающий за сглаживание рассеивания.
            Чем больше значение, тем менее резкие переходы между прозрачной и непрозрачной частью главного изображения.
            Для данного параметра существует метод случайной генерации значеня: <random_outlines_power(low_v=0.0, high_v=5.0)>.

        `outlines_power`
            float | int <Значение> Параметр, отвечающий за белую обводку между прозрачной и непрозрачной частью главного изображения.
            Рекомендуемый диапазон значений: от <0.0 до 5.0>.
            Для данного параметра существует метод случайной генерации значеня: <random_smooth_power(low_v=0.05, high_v=1.0)>.

        `internal_transparency_power`
            float | int <Значение> Параметр, отвечающий за прозрачность главного изображения, исключая края между прозрачной и непрозрачной частью.
            Эффект хорошо заметен при значении параметра <outlines_power> от 1.0 и выше.
            Для данного параметра существует метод случайной генерации значеня: <random_internal_transparency_power(low_v=0.0, high_v=1.0)>.

        `scroll_1, scroll_2, scroll_3`
            Кортеж из двух float | int значений <(Значение, Значение)> Параметры отвечающие за динамику текстуры шума для достижения динамического эффекта рассеивания.
            Вы можете не изменять данные параметры в ручную.
            Для данных параметров существует метод случайной генерации значений: <random_scrolls(low_v=-0.1, high_v=0.01)>.
        
        `texture_wrap`
            Кортеж из двух GL_CLAMP_TO_EDGE | GL_MIRRORED_REPEAT | GL_REPEAT значений <(Значение, Значение)> Данный параметр отвечает за режим отрисовки текстур для шейдеров.
            По-умолчанию значение: <(GL_REPEAT, GL_REPEAT)>. Не рекомендуется изменять.
        
        `force_update`
            boolean <Истина/Ложь> Если включено, то изображение будет постоянно перерисовываться с интервалом <force_update_delay>.
            Крайне не рекомендуется отключать данный параметр.
            Если отключён, то скорость обработки шейдера динамического рассеивания будет равен 5 кадров в секунду.

        `force_update_delay`
            Интервал между перерисовкой изображения.
            По-умолчанию значение: <0.016> (60 кадров в секунду).
            Если значение 0.0, то перерисовка будет производиться настолько быстро, насколько позволяет ваш компьютер.
        """

        def __init__(self, child, noise_texture, dissolve_power=10.0, smooth_power=0.25, outlines_power=0.0, internal_transparency_power=0.0, scroll_1=(0.1, -0.12), scroll_2=(-0.07, -0.08), scroll_3=(0.0, -0.05), texture_wrap=(GL_REPEAT, GL_REPEAT), force_update=True, force_update_delay=0.016, **kwargs):
            super(DynamicDissolvingImage, self).__init__(**kwargs)

            self._child = renpy.displayable(child)
            self._noise_texture = renpy.displayable(noise_texture)

            self._dissolve_power = float(dissolve_power)
            self._smooth_power = 1.0 - float(smooth_power)
            self._outlines_power = float(outlines_power)
            self._internal_transparency_power = float(internal_transparency_power)
            self._scroll_1 = tuple(float(elem) for elem in scroll_1)
            self._scroll_2 = tuple(float(elem) for elem in scroll_2)
            self._scroll_3 = tuple(float(elem) for elem in scroll_3)

            self._always_update = True
            self._force_update_delay = force_update_delay

            self._texture_wrap = tuple(elem for elem in texture_wrap)

        #<База>#
        def render(self, width, height, st, at):
            child_render = renpy.render(self._child, width, height, st, at)
            noise_render = renpy.render(self._noise_texture, width, height, st, at)

            main_render = renpy.Render(*child_render.get_size())

            main_render.mesh = True

            main_render.add_shader("wnfh.DynamicShader")

            main_render.add_uniform("u_dissolvePower", self._dissolve_power)
            main_render.add_uniform("u_smoothPower", self._smooth_power)
            main_render.add_uniform("u_outlinesPower", self._outlines_power)
            main_render.add_uniform("u_internalTransparencyPower", self._internal_transparency_power)
            main_render.add_uniform("u_scroll1", self._scroll_1)
            main_render.add_uniform("u_scroll2", self._scroll_2)
            main_render.add_uniform("u_scroll3", self._scroll_3)

            main_render.add_property("gl_texture_wrap", self._texture_wrap)

            main_render.blit(child_render, (0, 0), focus=True, main=True)
            main_render.blit(noise_render, (0, 0), focus=False, main=False)

            if self._always_update:
                renpy.redraw(self, self._force_update_delay)

            return main_render

        def event(self, ev, x, y, st):
            return self._child.event(ev, x, y, st)

        def visit(self):
            return [ self._child, self._noise_texture ]
        ########

        #<Рандомизаторы>#
        def random_scrolls(self, low_v=-0.1, high_v=0.01):
            for i in range(0, 2):
                setattr(self, "_scroll_{}".format(i + 1), (renpy.random.uniform(low_v, high_v), renpy.random.uniform(low_v, high_v)))

        def random_dissolve_power(self, low_v=0.25, high_v=15.0):
            self._dissolve_power = renpy.random.uniform(low_v, high_v)

        def random_smooth_power(self, low_v=0.05, high_v=1.0):
            self._smooth_power = 1.0 - renpy.random.uniform(low_v, high_v)

        def random_outlines_power(self, low_v=0.0, high_v=5.0):
            self._dissolve_power = renpy.random.uniform(low_v, high_v)

        def random_internal_transparency_power(self, low_v=0.0, high_v=1.0):
            self._smooth_power = renpy.random.uniform(low_v, high_v)
        #################

        #<Геттеры>#
        @property
        def child(self):
            return self._child

        @property
        def noise_texture(self):
            return self._noise_texture

        @property
        def dissolve_power(self):
            return self._dissolve_power

        @property
        def smooth_power(self):
            return 1.0 - self._smooth_power

        @property
        def outlines_power(self):
            return self._outlines_power

        @property
        def internal_transparency_power(self):
            return self._internal_transparency_power

        @property
        def scroll_1(self):
            return self._scroll_1
        @property
        def scroll_2(self):
            return self._scroll_2
        @property
        def scroll_3(self):
            return self._scroll_3

        @property
        def always_update(self):
            return self._always_update

        @property
        def force_update_delay(self):
            return self._force_update_delay

        @property
        def texture_wrap(self):
            return self._texture_wrap
        ###########

        #<Сеттеры>#
        @child.setter
        def child(self, value):
            self._child = renpy.displayable(value)

        @noise_texture.setter
        def noise_texture(self, value):
            self._noise_texture = renpy.displayable(value)

        @dissolve_power.setter
        def dissolve_power(self, value):
            if not isinstance(value, (int, float)):
                raise TypeError("<dissolve_power> attribute must be int or float. Got value <{}> and its type <{}>".format(value, type(value)))

            self._dissolve_power = float(value)

        @smooth_power.setter
        def smooth_power(self, value):
            if not isinstance(value, (int, float)):
                raise TypeError("<smooth_power> attribute must be int or float. Got value <{}> and its type <{}>".format(value, type(value)))

            self._smooth_power = 1.0 - float(value)

        @outlines_power.setter
        def outlines_power(self, value):
            if not isinstance(value, (int, float)):
                raise TypeError("<outlines_power> attribute must be int or float. Got value <{}> and its type <{}>".format(value, type(value)))

            self._outlines_power = float(value)

        @internal_transparency_power.setter
        def internal_transparency_power(self, value):
            if not isinstance(value, (int, float)):
                raise TypeError("<internal_transparency_power> attribute must be int or float. Got value <{}> and its type <{}>".format(value, type(value)))

            self._internal_transparency_power = float(value)

        @scroll_1.setter
        def scroll_1(self, value):
            if not isinstance(value, tuple) or len(value) != 2 or not builtins.all([isinstance(bool_value, (int, float)) for bool_value in value]):
                raise TypeError("<scroll_1> attribute must be tupple of two ints or floats. Got value <{}> and its type <{}>".format(value, type(value)))

            self._scroll_1 = tuple(float(elem) for elem in value)

        @scroll_2.setter
        def scroll_2(self, value):
            if not isinstance(value, tuple) or len(value) != 2 or not builtins.all([isinstance(bool_value, (int, float)) for bool_value in value]):
                raise TypeError("<scroll_2> attribute must be tupple of two ints or floats. Got value <{}> and its type <{}>".format(value, type(value)))

            self._scroll_2 = tuple(float(elem) for elem in value)

        @scroll_3.setter
        def scroll_3(self, value):
            if not isinstance(value, (tuple, list)) or len(value) != 2 or not builtins.all([isinstance(bool_value, (int, float)) for bool_value in value]):
                raise TypeError("<scroll_3> attribute must be tupple or list of two ints or floats. Got value <{}> and its type <{}>".format(value, type(value)))

            self._scroll_3 = tuple(float(elem) for elem in value)

        @always_update.setter
        def always_update(self, value):
            if not isinstance(value, bool):
                raise TypeError("<always_update> attribute must be a boolean. Got value <{}> and its type <{}>".format(value, type(value)))
            
            self._always_update = value

            if value:
                renpy.redraw(self, 0.0)

        @force_update_delay.setter
        def force_update_delay(self, value):
            if not isinstance(value, float) or value < 0.0:
                raise TypeError("<force_update_delay> attribute must be a float greater or equal 0.0. Got value <{}> and its type <{}>".format(value, type(value)))
            
            self._force_update_delay = value

        @texture_wrap.setter
        def texture_wrap(self, value):
            global DDS_GL_TEXTURE_WRAP_MODES

            if not isinstance(value, (tuple, list)) or len(value) != 2 or not builtins.all([mode in DDS_GL_TEXTURE_WRAP_MODES for mode in value]):
                raise TypeError("<texture_wrap> attribute must be tuple or list of two elements from these values: GL_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT, GL_REPEAT.")
            
            self._texture_wrap = tuple(elem for elem in value)
        ###########
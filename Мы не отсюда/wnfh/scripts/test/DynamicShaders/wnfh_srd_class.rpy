##<ДАННЫЙ ШЕЙДЕР БЫЛ СДЕЛАН НЕ МНОЙ. ОН БЫЛ ВЗЯТ ОТСЮДА: https://www.shadertoy.com/view/slfSzS>##
##<Я ЛИШЬ ПЕРЕНЕС ШЕЙДЕР НА RenPy.>##

init 15 python:
    import builtins
    from renpy.uguu import GL_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT, GL_REPEAT

    DDS_GL_TEXTURE_WRAP_MODES = (GL_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT, GL_REPEAT)

    class ScreenRainDropsImage(renpy.Displayable):
        """
        `child`
            Отображаемый объект на которой будет накладываться шейдер экранных капель.

        `general_size`
            float | int <Значение> Размер экранных капель в целом.
            Рекомендуемые значения: <от 0.1 до 1.0>
            Для данного параметра существует метод случайной генерации значеня: <random_general_size(low_v=0.0, high_v=1.0)>.

        `puddles_size`
            float | int <Значение> Размер экранных капель, игнорируя размер водяного хвоста.
            Рекомендуемые значения: <от 2.0 до 6.0>
            Для данного параметра существует метод случайной генерации значеня: <random_puddles_size(low_v=2.0, high_v=6.0)>.

        `trail_color_shift`
            float | int <Значение> Сила контрастности водяных хвостов.
            Рекомендуемые значения: <от 0.0 до 0.8>
            Для данного параметра существует метод случайной генерации значеня: <random_trail_color_shift(low_v=0.0, high_v=0.8)>.

        `drop_speed`
            float | int <Значение> Скорость стекания капель.
            Рекомендуемые значения: <от 0.2 до 0.4>
            Для данного параметра существует метод случайной генерации значеня: <random_drop_speed(low_v=0.2, high_v=0.4)>.

        `rain_distance`
            float | int <Значение> Условное расстояние. Можно считать как второй размер для экранных капель.
            Рекомендуемые значения: <от 0.4 до 1.0>
            Для данного параметра существует метод случайной генерации значеня: <random_rain_distance(low_v=0.4, high_v=1.0)>.

        `blur_size`
            float | int <Значение> Сила Гауссова размытия всего изображения. Эффект <запотевания> или <нечёткости от воды>.
            Там где капли и водяные хвосты не стекают, будет данный эффект.
            Рекомендуемые значения: <от 0.0 до 0.8>
            Для данного параметра существует метод случайной генерации значеня: <random_blur_size(low_v=0.0, high_v=0.8)>.

        `force_update`
            boolean <Истина/Ложь> Если включено, то изображение будет постоянно перерисовываться с интервалом <force_update_delay>.
            Если включён, то изображение будет постоянно обновлять свои свойства, если таковые изменяет пользователь.
            Не рекомендуется отключать данный параметр.

        `texture_wrap`
            Кортеж из двух GL_CLAMP_TO_EDGE | GL_MIRRORED_REPEAT | GL_REPEAT значений <(Значение, Значение)> Данный параметр отвечает за режим отрисовки текстур для шейдеров.
            По-умолчанию значение: <(GL_REPEAT, GL_REPEAT)>.
            Не рекомендуется изменять.

        `force_update_delay`
            Интервал между перерисовкой изображения.
            По-умолчанию значение: <0.0> (максимально быстро).
            Если значение 0.0, то перерисовка будет производиться настолько быстро, насколько позволяет ваш компьютер.
        """

        def __init__(self, child, general_size=0.2, puddles_size=3.0, trail_color_shift=0.3, drop_speed=0.2, rain_distance=1.0, blur_size=0.0, texture_wrap=(GL_REPEAT, GL_REPEAT), force_update=True, force_update_delay=0.016, **kwargs):
            super(ScreenRainDropsImage, self).__init__(**kwargs)

            self._child = renpy.displayable(child)

            self._general_size = float(general_size)
            self._puddles_size = float(puddles_size)
            self._trail_color_shift = float(trail_color_shift)
            self._drop_speed = float(drop_speed)
            self._rain_distance = float(rain_distance)
            self._blur_size = float(blur_size)

            self._always_update = force_update
            self._force_update_delay = force_update_delay

            self._texture_wrap = tuple(elem for elem in texture_wrap)

        #<База>#
        def render(self, width, height, st, at):
            child_render = renpy.render(self._child, width, height, st, at)

            main_render = renpy.Render(*child_render.get_size())

            main_render.mesh = True

            main_render.add_shader("SRD.ScreenRainDrops")

            main_render.add_uniform("u_general_size", self._general_size)
            main_render.add_uniform("u_puddles_size", self._puddles_size)
            main_render.add_uniform("u_trail_color_shift", self._trail_color_shift)
            main_render.add_uniform("u_drop_speed", self._drop_speed)
            main_render.add_uniform("u_rain_distance", self._rain_distance)
            main_render.add_uniform("u_blur_size", self._blur_size)

            main_render.add_property("gl_texture_wrap", self._texture_wrap)

            main_render.blit(child_render, (0, 0), focus=True, main=True)

            if self._always_update:
                renpy.redraw(self, self._force_update_delay)

            return main_render

        def event(self, ev, x, y, st):
            return self._child.event(ev, x, y, st)

        def visit(self):
            return [ self._child ]
        ########

        #<Рандомизаторы>#
        def random_general_size(self, low_v=0.0, high_v=1.0):
            self._general_size = renpy.random.uniform(low_v, high_v)

        def random_puddles_size(self, low_v=2.0, high_v=6.0):
            self._puddles_size = renpy.random.uniform(low_v, high_v)

        def random_trail_color_shift(self, low_v=0.0, high_v=0.8):
            self._trail_color_shift = renpy.random.uniform(low_v, high_v)

        def random_drop_speed(self, low_v=0.2, high_v=0.4):
            self._drop_speed = renpy.random.uniform(low_v, high_v)

        def random_rain_distance(self, low_v=0.4, high_v=1.0):
            self._rain_distance = renpy.random.uniform(low_v, high_v)

        def random_blur_size(self, low_v=0.0, high_v=0.8):
            self._blur_size = renpy.random.uniform(low_v, high_v)
        #################

        #<Геттеры>#
        @property
        def child(self):
            return self._child

        @property
        def general_size(self):
            return self._general_size

        @property
        def puddles_size(self):
            return self._puddles_size

        @property
        def trail_color_shift(self):
            return self._trail_color_shift

        @property
        def drop_speed(self):
            return self._drop_speed

        @property
        def rain_distance(self):
            return self._rain_distance

        @property
        def blur_size(self):
            return self._blur_size

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

        @general_size.setter
        def general_size(self, value):
            if not isinstance(value, (int, float)):
                raise TypeError("<general_size> attribute must be int or float. Got value <{}> and its type <{}>".format(value, type(value)))

            self._sepia_value = float(value)

        @puddles_size.setter
        def puddles_size(self, value):
            if not isinstance(value, (int, float)):
                raise TypeError("<puddles_size> attribute must be int or float. Got value <{}> and its type <{}>".format(value, type(value)))

            self._sepia_value = float(value)

        @trail_color_shift.setter
        def trail_color_shift(self, value):
            if not isinstance(value, (int, float)):
                raise TypeError("<trail_color_shift> attribute must be int or float. Got value <{}> and its type <{}>".format(value, type(value)))

            self._noise_value = float(value)

        @drop_speed.setter
        def drop_speed(self, value):
            if not isinstance(value, (int, float)):
                raise TypeError("<drop_speed> attribute must be int or float. Got value <{}> and its type <{}>".format(value, type(value)))

            self._scratch_value = float(value)

        @rain_distance.setter
        def rain_distance(self, value):
            if not isinstance(value, (int, float)):
                raise TypeError("<rain_distance> attribute must be int or float. Got value <{}> and its type <{}>".format(value, type(value)))

            self._vignetting = float(value)

        @blur_size.setter
        def blur_size(self, value):
            if not isinstance(value, (int, float)):
                raise TypeError("<blur_size> attribute must be int or float. Got value <{}> and its type <{}>".format(value, type(value)))

            self._vignetting = float(value)

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
init python:
    import math

    class ESPEOptimizedValues(object):
        ##Сумма затраченной памяти двух тригонометрических списков 672 байта. Это много? Я не знаю :(.##
        def __init__(self, step=0.0625):
            self.trigonometric_step = step
            self.sin_values = [math.sin(math.radians(x)) for x in range(-180, 180)]
            self.cos_values = [math.cos(math.radians(x)) for x in range(-180, 180)]
            self.trigonometric_len = len(self.sin_values)

        def osin_t(self, abs_time):
            return self.sin_values[int(round(self.trigonometric_len * abs_time))]
        
        def ocos_t(self, abs_time):
            return self.cos_values[int(round(self.trigonometric_len * abs_time))]

        def osin_random(self):
            return renpy.random.choice(self.sin_values)
        
        def ocos_random(self):
            return renpy.random.choice(self.cos_values)
        
        def osin_angle_d(self, degree):
            return self.sin_values[degree]
        
        def ocos_angle_d(self, degree):
            return self.cos_values[degree]
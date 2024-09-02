init 15 python:
    from renpy.uguu import GL_REPEAT

init 15:
    transform SRD_screen_raindrops_effect(update_delay=0.016, general_size=0.2, puddles_size=3.0, trail_color_shift=0.3, drop_speed=0.2, rain_distance=1.0, blur_size=0.0):
        mesh True
        shader "SRD.ScreenRainDrops"

        u_general_size general_size
        u_puddles_size puddles_size
        u_trail_color_shift trail_color_shift
        u_drop_speed drop_speed
        u_rain_distance rain_distance
        u_blur_size blur_size
        gl_texture_wrap (GL_REPEAT, GL_REPEAT)

        pause update_delay
        repeat

"""
    `update_delay`
        Интервал между перерисовкой изображения.
        По-умолчанию значение: <0.0> (максимально быстро).
        Если значение 0.0, то перерисовка будет производиться настолько быстро, насколько позволяет ваш компьютер.

    `general_size`
        float | int <Значение> Размер экранных капель в целом.
        Рекомендуемые значения: <от 0.1 до 1.0>

    `puddles_size`
        float | int <Значение> Размер экранных капель, игнорируя размер водяного хвоста.
        Рекомендуемые значения: <от 2.0 до 6.0>

    `trail_color_shift`
        float | int <Значение> Сила контрастности водяных хвостов.
        Рекомендуемые значения: <от 0.0 до 0.8>

    `drop_speed`
        float | int <Значение> Скорость стекания капель.
        Рекомендуемые значения: <от 0.2 до 0.4>

    `rain_distance`
        float | int <Значение> Условное расстояние. Можно считать как второй размер для экранных капель.
        Рекомендуемые значения: <от 0.4 до 1.0>

    `blur_size`
        float | int <Значение> Сила Гауссова размытия всего изображения. Эффект <запотевания> или <нечёткости от воды>.
        Там где капли и водяные хвосты не стекают, будет данный эффект.
        Рекомендуемые значения: <от 0.0 до 0.8>
"""
init 50:
    # $ WNFH_DS_example_mod_path = "mods/DynamicDissolveShader/DDS_Example_noises/"

    # image DDS_perlin = DDS_example_mod_path + "classic_perlin_512.png"
    # image DDS_techno_noise = DDS_example_mod_path + "techno_noise_512.png"
    # image DDS_turbulence_noise = DDS_example_mod_path + "turbulence_noise_512.png"
    # wnfh_DS

    image wnfh_DS_perling = wnfh_DS + "classic_perlin_512.png"
    image wnfh_DS_techno_noise = wnfh_DS + "techno_noise_512.png"
    image wnfh_DS_turbulence_noice = wnfh_DS + "turbulence_noise_512.png"


    #<Классическое объявление.>#
    image wnfh_DS_bg_ext_lenin_square_night_wnfh = DynamicDissolvingImage(child="bg ext_lenin_square_day_wnfh", noise_texture="wnfh_DS_perlin", outlines_power=10.0)
    ###########################

    #<Объявление как обычная переменная, хранящая ссылку на экземпляр класса.>#
    #<Позволяет изменять поля и использовать доступные методы.>#
    #$ DDS_slavya_default.random_scrolls()#
    #show expression DDS_slavya_default#
    #$ DDS_slavya_default.dissolve_power = 9.5#
    #$ Параметры, изменённые после <show expression> всё равно изменят поведение изображения.#
    $ wnfh_DS_slavya_default = DynamicDissolvingImage(child="sl smile pioneer far", noise_texture="wnfh_DS_turbulence_noise")

    $ wnfh_DS_slavya_max_oulines = DynamicDissolvingImage(child="sl smile pioneer far", noise_texture="wnfh_DS_turbulence_noise", outlines_power=5.0)

    $ wnfh_DS_slavya_smoke = DynamicDissolvingImage(child="sl smile pioneer far", noise_texture="wnfh_DS_turbulence_noise", dissolve_power=8.0, smooth_power=0.95, outlines_power=0.25)

    $ wnfh_DS_slavya_internal_zero = DynamicDissolvingImage(child="sl smile pioneer far", noise_texture="wnfh_DS_turbulence_noise", internal_transparency_power=1.0, outlines_power=5.0)
    ###########################################################################
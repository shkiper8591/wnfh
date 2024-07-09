label wnfh_test_shaders:

    $ wnfh_set_time("night")
    scene bg ext_lenin_square_night_wnfh

    show expression wnfh_DS_slavya_default at left
    show expression wnfh_DS_slavya_max_oulines:
        xpos 0.21
    show expression wnfh_DS_slavya_internal_zero:
        xpos 0.45
    show expression wnfh_DS_slavya_smoke:
        xpos 0.69
    with dissolve

    "Test chamber. Showing sprites. Default | Max outlines | Internal alpha zero | Smoke-like effect."

    hide wnfh_DDS_slavya_default
    hide wnfh_DS_slavya_max_oulines
    hide wnfh_DS_slavya_internal_zero
    hide wnfh_DS_slavya_smoke
    show wnfh_DS_bg_ext_lenin_square_night_wnfh
    with dissolve

    "Showing bg. With outlines. Classic perlin texture 512x512."
    "end"

    jump wnfh_test
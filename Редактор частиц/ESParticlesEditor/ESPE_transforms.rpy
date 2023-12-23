init:
    transform blur_light(img_alpha=0.2, blur_min, blur_max):
        alpha img_alpha
        blur blur_min
        parallel:
            ease 5.0 blur blur_max
            ease 5.0 blur blur_min
            repeat
    
    transform fast_align(x, y):
        align (x, y)

    transform fast_align_alpha(x, y, a):
        align (x, y)
        alpha a
    
    transform fast_pos_alpha(x, y, a):
        pos (x, y)
        alpha a

    transform fast_pos_05anchor(x, y):
        anchor (0.5, 0.5)
        pos (x, y)
    
    transform fast_pos_05anchor_alpha(x, y, a):
        anchor (0.5, 0.5)
        pos (x, y)
        alpha a

    transform fast_pos_05anchor_tint(x, y, color):
        anchor (0.5, 0.5)
        pos (x, y)
        matrixcolor TintMatrix(color)

    transform fast_pos_05anchor_alpha_tint(x, y, a, color):
        anchor (0.5, 0.5)
        pos (x, y)
        alpha a
        matrixcolor TintMatrix(color)
    
    transform fast_pos_05anchor_alpha_zoom_tint(x, y, a, z, color):
        anchor (0.5, 0.5)
        pos (x, y)
        alpha a
        zoom z
        matrixcolor TintMatrix(color)
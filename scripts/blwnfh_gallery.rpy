init python:
    blwnfh_mod_gallery = Gallery()
    page = 0
    blwnfh_gallery_mode = "cg"

    blwnfh_mod_gallery.locked_button = blwnfh_GALLERY + "lock.png"
    blwnfh_mod_gallery.navigation = False
    
    
    
    
    blwnfh_gallery_cg = [ # Заполняем ЦГ словарь
        "d2_dv_sem_scene",
        "d5_me_mirror_tractor_blwnfh",
        "disclaimer",
        "Katya_Avtobus",
    ]
    
    
    blwnfh_gallery_bg = [ # Заполняем БГ словарь
        "ext_clubs_sunset",
        "ext_music_club_sunset",
        "ext_warehouse_day",
        "int_dining_hall_people_sunset",
    ]

    # Создаём кнопки и их изображения, внезависимости от размера исходной картинки, будет масштабирование до 1920x1080
    for cg in blwnfh_gallery_cg:
        blwnfh_mod_gallery.button(cg)
        blwnfh_mod_gallery.image(im.Crop(blwnfh_CG + cg + ".png" , (0, 0, 1920, 1080)))
        blwnfh_mod_gallery.unlock(cg)
    
    for bg in blwnfh_gallery_bg:
        blwnfh_mod_gallery.button(bg)
        blwnfh_mod_gallery.image(im.Crop(blwnfh_BG + bg + ".jpg" , (0, 0, 1920, 1080)))
        blwnfh_mod_gallery.unlock(bg)
    # При нажатии на кнопку с изображением, будет происходить fade переход.
    blwnfh_mod_gallery.transition = fade
init 5 python:
    wnfh_chars_define()
    
    def say_anim():     
        amd = int(persistent.font_size <= "large") if wnfh_test_1 else 2
        return amd
    def say_size():
        return int(persistent.font_size <= "large")
    def MatrixConverter(dictionary_obj):
        main_dick = {}
        for button in dictionary_obj:
            temp_array = []
            for obj in dictionary_obj[button]:
                compozite = []
                compozite.append(obj[0])
                for obj_index in range(len(obj[1])):
                    compozite.append(obj[1][obj_index][0])
                    compozite.append(Transform(wnfh_gui["tint_elements"][obj[1][obj_index][1]], matrixcolor = TintMatrix(wnfh_tint_color[renpy.store.wnfh_tymeofday][obj[1][obj_index][2]])))
                compozite_obj = wnfh_Composite(*compozite)
                try:
                    if obj[-1] is True:
                        flip_args = True
                    else:
                        flip_args = None
                except Exception as E:
                    flip_args = None
                if flip_args != None:
                    temp_array.append(Transform(compozite_obj, xzoom = -1.0))
                else:
                    temp_array.append(compozite_obj)
            main_dick[button] = temp_array
        return main_dick
init -4 python:
    # Всякий разный цветокор
    def Sepia(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.15) * im.matrix.tint(1.0, .94, .76))
    def OldPhoto(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.6) * im.matrix.brightness(0.03))
    def Grayed(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.01))

    # Цветокор под разное время суток
    def Notch(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.2) * im.matrix.saturation(0.6))
    def Dawn(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.1) * im.matrix.tint(0.94, 0.82, 1.0))
    def Noon(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(0.2) * im.matrix.tint(1.0, 0.94, 0.82))
    def HomeCity(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.1) * im.matrix.tint(0.82, 0.84, 1.0))
    def Rained(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.4) * im.matrix.tint(0.68, 0.90, 0.8) * im.matrix.saturation(0.6))
    
    # Я забыл что это за залупа
    def filmetile(bitmap, opacity=0.1):
        return im.Tile(im.Alpha(bitmap,opacity))

        
init -1 python:
    def converter_hex(list_name, name, list_key_name=persistent.timeofday):
        hex_var = globals()[list_name][list_key_name][name]
        start_index = 1
        value_list = []
        for i in range(3):
            temp_convert = hex_var[start_index:start_index + 2]
            convert = int(temp_convert, 16) / 255.0
            value_list.append(convert)
            start_index+=2
        #try:
        #    pm=[1,2]
        #    pm[3]
        #except Exception as e:
        #    raise Exception(str(value_list),)         
        return value_list
    #def converter1(a,b):
    #    return [0.5961, 0.8471, 0.8549]
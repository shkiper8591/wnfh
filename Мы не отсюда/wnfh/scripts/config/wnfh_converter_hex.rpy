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
        return value_list
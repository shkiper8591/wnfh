screen ESPE_editor_input(obj, field, field_type, clamp_range=None, max_length=24, psystem_object=None, psystem_field=None, additional_value=None, multiplie_value=None, exclude=None, force_update_attr_func=None):
    modal True
    tag espe_input
    zorder 25

    default field_value = str(espe_multiplie_value(espe_additional_substract(getattr(obj, field), additional_value), multiplie_value))
  
    on 'hide' action [If(espe_input_safe_check(field_value, field_type, obj, field),
                        true=[SetField(obj, field, espe_divide_value(espe_additional(espe_clamp(espe_field_type_safe(field_value, field_type), clamp_range), additional_value), multiplie_value)),
                        If(psystem_field is not None and psystem_object is not None,
                            true=[SetField(psystem_object, psystem_field, espe_clamp(espe_field_type_safe(field_value, field_type), clamp_range))])]),
                    If(force_update_attr_func is not None, true=Function(force_update_attr_func))]

    add Solid("#000") alpha 0.2
    add Solid("#000", xsize=0.3, ysize=0.2) at fast_align_alpha(0.5, 0.5, 0.5)
    vbox:
        xalign 0.5
        yalign 0.5
        first_spacing 50
        spacing 20

        text "Введите значение аттрибута" xmaximum 0.3 style "espe_text_heading_36"

        input:
            value AdvancedScreenVariableInputValue(variable="field_value", var_type=str, exclude=exclude, returnable=False)
            length max_length
            xmaximum 0.3
            size 24
            at fast_align(0.5, 0.5)

        textbutton "Завершить редактирование" xmaximum 0.3 style "espe_button" text_style "espe_button_text_24" at fast_align(0.5, 0.5):
            action Hide("ESPE_editor_input")

##Для списков/кортежей.##
screen ESPE_editor_input_collections(obj, field, field_type, index, clamp_range=None, max_length=24, exclude=None, force_update_attr_func=None):
    modal True
    tag espe_input
    zorder 25

    default field_value_collection = str(getattr(obj, field))
    default field_value = str(getattr(obj, field)[index])
  
    on 'hide' action [If(espe_input_safe_check(field_value, field_type, obj, field),
                        true=[SetFieldCollection(obj, field, espe_clamp(espe_field_type_safe(field_value, field_type), clamp_range), index)]),

                    If(force_update_attr_func is not None, true=Function(force_update_attr_func))]

    add Solid("#000") alpha 0.2
    add Solid("#000", xsize=0.3, ysize=0.2) at fast_align_alpha(0.5, 0.5, 0.5)
    vbox:
        xalign 0.5
        yalign 0.5
        first_spacing 50
        spacing 20

        text "Введите значение аттрибута" xmaximum 0.3 style "espe_text_heading_36"

        input:
            value AdvancedScreenVariableInputValue(variable="field_value", var_type=str, exclude=exclude, returnable=False)
            length max_length
            xmaximum 0.3
            size 24
            at fast_align(0.5, 0.5)

        textbutton "Завершить редактирование" xmaximum 0.3 style "espe_button" text_style "espe_button_text_24" at fast_align(0.5, 0.5):
            action Hide("ESPE_editor_input_collections")
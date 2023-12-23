init -1000 python:
    def renpy_get_field(obj, name, kind):

        if not name:
            return obj

        rv = obj

        for i in name.split("."):
            rv = getattr(rv, i, object())
            if rv is object():
                raise NameError("The {} {} does not exist.".format(kind, name))

        return rv

    def renpy_set_field(obj, name, value, kind):
        fields, _, attr = name.rpartition(".")

        try:
            obj = renpy_get_field(obj, fields, kind)
            setattr(obj, attr, value)
        except:
            raise NameError("The {} {} does not exist.".format(kind, name))

    ##Позволяет изменять элемент поля объекта (если он является коллекцией).##
    @renpy.pure
    class SetFieldCollection(Action, FieldEquality):
        identity_fields = [ "object" ]
        equality_fields = [ "field", "value" ]

        kind = "field"

        def __init__(self, object, field, value, index, kind="field"):
            self.object = object
            self.field = field
            self.value = value
            self.index = index
            self.kind = kind

        def __call__(self):
            field_collection = getattr(self.object, self.field)

            if not isinstance(field_collection, (list, set, dict)):
                raise TypeError("The {} {} not a collection.".format(kind, name))
            
            field_collection[self.index] = self.value

            renpy_set_field(self.object, self.field, field_collection, self.kind)
            renpy.restart_interaction()

        def get_selected(self):
            return renpy_get_field(self.object, self.field, self.kind) == self.value
    
    ##Позволяет переключать элемент поля объекта (если он является коллекцией).##
    @renpy.pure
    class ToggleFieldCollection(Action, FieldEquality):

        identity_fields = [ "object"]
        equality_fields = [ "field", "true_value", "false_value"  ]

        kind = "field"

        def __init__(self, object, field, index_key, true_value=None, false_value=None, kind="field"):
            self.object = object
            self.field = field
            self.index = index_key
            self.true_value = true_value
            self.false_value = false_value
            self.kind = kind

        def __call__(self):
            field_collection = getattr(self.object, self.field)

            if not isinstance(field_collection, (list, set, dict)):
                raise TypeError("The {} {} not a collection.".format(kind, name))

            if self.true_value is not None:
                field_collection[self.index] = (field_collection[self.index] == self.true_value)

            field_collection[self.index] = not field_collection[self.index]

            if self.true_value is not None:
                if field_collection[self.index]:
                    field_collection[self.index] = self.true_value
                else:
                    field_collection[self.index] = self.false_value

            renpy_set_field(self.object, self.field, field_collection, self.kind)
            renpy.restart_interaction()

        def get_selected(self):
            rv = renpy_get_field(self.object, self.field, self.kind)

            if self.true_value is not None:
                rv = (rv == self.true_value)

            return rv
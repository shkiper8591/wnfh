init -1000 python:
    @renpy.pure
    class FieldValueCollection(BarValue, FieldEquality):
        offset = 0
        action = None
        force_step = False

        identity_fields = [ 'object', ]
        equality_fields = [ 'range', 'max_is_zero', 'style', 'offset', 'step', 'action', 'force_step', 'field' ]

        def __init__(self, object, field, index, range, max_is_zero=False, style="bar", offset=0, step=None, action=None, force_step=False):
            self.object = object
            self.field = field
            self.index = index
            self.range = range
            self.max_is_zero = max_is_zero
            self.style = style
            self.offset = offset
            self.force_step = force_step

            if step is None:
                if isinstance(range, float):
                    step = range / 10.0
                else:
                    step = max(range / 10, 1)

            self.step = step
            self.action = action

        def changed(self, value):

            if self.max_is_zero:
                if value == self.range:
                    value = 0
                else:
                    value = value + 1

            value += self.offset

            self.setattr_collection(self.object, self.field, value)
            renpy.restart_interaction()

            renpy.run(self.action)

        def get_adjustment(self):

            field_collection = getattr(self.object, self.field)

            field_collection[self.index] -= self.offset

            if self.max_is_zero:
                if field_collection[self.index] == 0:
                    field_collection[self.index] = self.range
                else:
                    field_collection[self.index] -= 1

            return ui.adjustment(
                range=self.range,
                value=field_collection[self.index],
                changed=self.changed,
                step=self.step,
                force_step=self.force_step,
            )

        def setattr_collection(self, object, field, value):
            field_collection = getattr(object, field)
            field_collection[self.index] = value

            setattr(object, field, field_collection)


        def get_style(self):
            return self.style, "v" + self.style
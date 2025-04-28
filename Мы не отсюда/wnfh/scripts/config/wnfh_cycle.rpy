init -10 python:
    #<НАШЕ> MystiSs

    # Моё. 140 лilograms of sex
    class wnfh_CycleField(Action):
        def __init__(self, object, field, values):
            self.object = object
            self.field = field

            self.values = values

            self.current_index = 0

            try:
                self.current_index = self.values.index(getattr(self.object, self.field))
            except ValueError:
                self.current_index = 0
            

        def __call__(self):
            self.current_index += 1
            self.current_index %= len(self.values)
            setattr(self.object, self.field, self.values[self.current_index])
            renpy.restart_interaction()
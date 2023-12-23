init -10 python:
    '''
    Улучшенный класс FieldInputValue, который позволяет менять численные значения полей классов. Я рот ебал обычного FieldInputValue.
    Добавлена возможность блокировать вхождения заданных символов.
    '''

    @renpy.pure
    class AdvancedFieldInputValue(InputValue, FieldEquality):
        identity_fields = [ "object" ]
        equality_fields = [ "field", "returnable" ]

        def __init__(self, object, field, field_type=str, exclude=None, default=True, returnable=False):
            self.object = object
            self.field = field

            self.default = default
            self.returnable = returnable
            self.field_type = field_type

            self.exclude = None
            if exclude is not None:
                self.exclude = exclude

        def get_text(self):
            return str(getattr(self.object, self.field))

        def set_text(self, s):
            utf_s = s.encode('utf-8')

            if self.exclude is not None:
                utf_s = self.exclude_chars(utf_s)

            if utf_s:
                setattr(self.object, self.field, self.field_type(utf_s))
            else:
                setattr(self.object, self.field, utf_s)

            renpy.restart_interaction()
        
        def exclude_chars(self, s):
            mod_s = s

            for symb in self.exclude:
                mod_s = mod_s.replace(symb, '')

            return mod_s
    

    ########################################################################################################


    '''
    Улучшенный класс ScreenVariableInputValue, который позволяет менять численные значения переменных экранов.
    Добавлена возможность блокировать вхождения заданных символов.
    '''

    class AdvancedScreenVariableInputValue(InputValue, FieldEquality):
        identity_fields = [ 'screen' ]
        equality_fields = [ "variable", "returnable" ]

        def __init__(self, variable, var_type=str, exclude=None, default=True, returnable=False):
            self.variable = variable

            self.default = default
            self.returnable = returnable
            self.var_type = var_type

            self.exclude = None
            if exclude is not None:
                self.exclude = exclude

            self.screen = renpy.current_screen()

        def get_text(self):
            cs = self.screen
            return str(cs.scope[self.variable])

        def set_text(self, s):
            utf_s = s.encode('utf-8')

            if self.exclude is not None:
                utf_s = self.exclude_chars(utf_s)

            cs = self.screen
            cs.scope[self.variable] = self.var_type(utf_s)
            renpy.restart_interaction()
        
        def exclude_chars(self, s):
            mod_s = s

            for symb in self.exclude:
                mod_s = mod_s.replace(symb, '')

            return mod_s
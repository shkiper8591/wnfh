init -5 python:
    from builtins import len as _len


    class wnfh_Composite(renpy.Displayable):
        def __init__(self, size, *args, **kwargs):
            super(wnfh_Composite, self).__init__(**kwargs)

            self.size = size
            self.args = args

            if len(args) % 2 != 0:
                renpy.error("Данных должно быть четное количество")

        def render(self, width, height, st, at):
            main_render = renpy.Render(*self.size)

            for i in range(1, _len(self.args), 2):
                child_render = renpy.render(self.args[i], width, height, st, at)
                child_pos = self.args[i-1]
                main_render.blit(child_render, child_pos)

            return main_render
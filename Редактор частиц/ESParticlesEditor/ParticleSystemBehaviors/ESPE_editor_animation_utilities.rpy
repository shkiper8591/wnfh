init -10 python:
    class ESPEAnimationEasings(renpy.object.Object):
        @staticmethod
        def linear(time):
            return time

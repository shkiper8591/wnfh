init python:
    def getMusicName():
        music_name = renpy.music.get_playing("music")
        if music_name is not None:
            return music_name.split("/")[-1].split(".")[0]
        else:
            return "Бога нет"
init python:

    ## Всякие прикольные звуковые функции ##

    from random import choice
    
    renpy.music.register_channel("ambience_2", "sfx", True)

    # Замутить каналы
    def wnfh_mute(fade=2.5):
        for channel in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "ambience_2", "music"):
            renpy.music.stop(channel=channel, fadeout=fade)
    
    # Менять громкость канала
    def wnfh_set_volume(channel, value, fade=0.0): # для удобства
        renpy.music.set_volume(volume=value, delay=fade, channel=channel)

    def wnfh_set_volume_all_channel(value=1.0):
        for channel in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "ambience_2", "music"):
            wnfh_set_volume(channel, value, 0.0)
    
    # Проигрывать рандомную музыку (нахуя?)
    def wnfh_play_random(list, channel="sound"):
        renpy.play(random.choice(list), channel=channel)



    # Второй канал для эмбиента
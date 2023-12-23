init python:
    class ESPESceneEditorData(renpy.object.Object):
        def __init__(self):
            self.is_scene_editor = False

            self.last_scene_editor_screen = "ESPE_scene_editor_main"
            self.last_p_editor_screen = "ESPE_editor_menu_startup"

            self.background = ESPEBackgroundUnit()
            self.sprite_list = [ ]

            self.current_music = None
            self.current_music_name = "Не играет"
            self.current_ambience = None
            self.current_ambience_name = "Не играет"

        def add_sprite(self):
            special_name = "Спрайт " + str(len(self.sprite_list) + 1)
            new_sprite = ESPESpriteUnit(special_name)

            self.sprite_list.append(new_sprite)

        def load_sprite(self, spec_name, sprite_displayable, tint_name, tint_index, xoffset, yoffset, alpha, zoom, rotate_angle, zorder):
            special_name = spec_name
            new_sprite = ESPESpriteUnit(special_name)

            new_sprite.displayable = sprite_displayable

            new_sprite.special_name = special_name

            new_sprite.tint = TintMatrix(espe_sprite_tint_list[tint_index][1])
            new_sprite.tint_index = tint_index

            new_sprite.xoffset = xoffset + config.screen_width
            new_sprite.yoffset = yoffset + config.screen_height

            new_sprite.alpha = alpha
            new_sprite.zoom = zoom

            new_sprite.rotate = rotate_angle

            new_sprite.zorder = zorder

            self.sprite_list.append(new_sprite)
        
        def remove_sprite(self, spr_obj):
            self.sprite_list.remove(spr_obj)
            del spr_obj

        def clear_sprites(self):
            while self.sprite_list:
                spr_obj = self.sprite_list.pop(0)
                del spr_obj
        
        def sort_by_zorder(self):
            self.sprite_list.sort(key=lambda spr: spr.zorder)

        def play_channel(self, src, channel_name, audio_name):
            renpy.music.stop(channel=channel_name, fadeout=1.0)
            renpy.music.queue(filenames=src, channel=channel_name, fadein=1.0)
            
            if channel_name == "music":
                self.current_music = src
                self.current_music_name = audio_name
            else:
                self.current_ambience = src
                self.current_ambience_name = audio_name

        def stop_channel(self, channel_name):
            renpy.music.stop(channel=channel_name, fadeout=1.0)

            if channel_name == "music":
                self.current_music = None
                self.current_music_name = "Не играет"
            else:
                self.current_ambience = None
                self.current_ambience_name = "Не играет"

        def is_music_ambience_active(self):
            if self.current_music is not None or self.current_ambience is not None:
                return True
            return False

        def turn_off_music_ambience(self):
            renpy.music.stop(channel="music", fadeout=1.0)
            renpy.music.stop(channel="ambience", fadeout=1.0)

            self.current_music = None
            self.current_ambience = None
            self.current_music_name = "Не играет"
            self.current_ambience_name = "Не играет"

        def get_sound_name(self, channel_name):
            if channel_name == "music":
                return self.current_music_name

            return self.current_ambience_name
        
        def get_sprite_list_length(self):
            length = len(self.sprite_list)

            if length < 1:
                return "Спрайтов на сцене нет"

            return length

        def set_data(self, scene_data):
            bg = self.background

            filename = scene_data[0]
            background_data = scene_data[1]
            audio_data = scene_data[2]
            general_sprites_data = scene_data[3]
            sprites_data = scene_data[4]

            bg.displayable = background_data[0]
            bg.xoffset = background_data[1] + config.screen_width
            bg.yoffset = background_data[2] + config.screen_height
            bg.alpha = background_data[3]
            bg.zoom = background_data[4]
            bg.rotate = background_data[5]

            if audio_data[1] != "None":
                self.play_channel(audio_data[1], "music", audio_data[0])
            else:
                self.stop_channel("music")
            
            if audio_data[3] != "None":
                self.play_channel(audio_data[3], "ambience", audio_data[2])
            else:
                self.stop_channel("ambience")

            self.clear_sprites()

            if sprites_data:
                for spr in sprites_data:
                    self.load_sprite(*spr)

        def get_data(self):
            bg = self.background
            music_name = self.current_music_name if self.current_music is not None else "Ничего не играет"
            ambience_name = self.current_ambience_name if self.current_ambience is not None else "Ничего не играет"
            general_sprites_data = [ ]
            sprites_data = [ ]

            background_data = [
                bg.displayable,
                bg.xoffset - config.screen_width,
                bg.yoffset - config.screen_height,
                bg.alpha,
                bg.zoom,
                bg.rotate
            ]

            audio_data = [
                music_name,
                self.current_music,
                ambience_name,
                self.current_ambience
            ]

            general_sprites_data.append(len(self.sprite_list))

            if general_sprites_data[0] > 0:
                for spr in self.sprite_list:
                    spr_data = [
                        spr.special_name,
                        spr.displayable,
                        espe_sprite_tint_list[spr.tint_index][0],
                        spr.tint_index,
                        spr.xoffset - config.screen_width,
                        spr.yoffset - config.screen_height,
                        spr.alpha,
                        spr.zoom,
                        spr.rotate,
                        spr.zorder
                    ]
                    sprites_data.append(spr_data)

            return (background_data, audio_data, general_sprites_data, sprites_data)
    
    class ESPEBackgroundUnit(renpy.object.Object):
        def __init__(self):
            self.displayable = "bg ext_square_sunset"

            self.xoffset = config.screen_width
            self.yoffset = config.screen_height

            self.alpha = 1.0
            self.zoom = 1.0

            self.rotate = 0

        def set_image(self, disp):
            self.displayable = disp
        
        def reset_transform(self):
            self.xoffset = config.screen_width
            self.yoffset = config.screen_height

            self.alpha = 1.0
            self.zoom = 1.0

            self.rotate = 0

    class ESPESpriteUnit(renpy.object.Object):
        def __init__(self, special_name="Спрайт 1"):
            self.displayable = "espe_temporary_image"

            self.special_name = special_name

            self.tint = TintMatrix(espe_sprite_tint_list[0][1])
            self.tint_index = 0

            self.xoffset = config.screen_width
            self.yoffset = config.screen_height

            self.zoom = 1.0
            self.alpha = 1.0

            self.rotate = 0

            self.zorder = 0
        
        def set_image(self, disp):
            self.displayable = disp
        
        def set_zorder(self, zorder):
            self.zorder = zorder

        def set_tint_cycle(self):
            self.tint_index = (self.tint_index + 1) % len(espe_sprite_tint_list)
            self.tint = TintMatrix(espe_sprite_tint_list[self.tint_index][1])
        
        def hovered(self):
            self.zoom += 0.05
        
        def unhovered(self):
            self.zoom -= 0.05

        def reset_transform(self):
            self.tint_index = 0
            self.tint = TintMatrix(espe_sprite_tint_list[0][1])

            self.xoffset = config.screen_width
            self.yoffset = config.screen_height

            self.zoom = 1.0
            self.alpha = 1.0

            self.rotate = 0

        def get_tint_name(self):
            return espe_sprite_tint_list[self.tint_index][0]
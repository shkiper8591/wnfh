init python:
    import pygame

    class ESPEPositionPicker(renpy.object.Object):
        """
        ESPEPositionPicker - Класс для определния позиции курсора мыши. Удобно, если необходимо определить нужную позицю.
        """

        def __init__(self, manager):
            self.manager = manager
            self.none_displayable = Text("None", alpha=0.0)
            self.none_displayable = Transform(self.none_displayable, alpha=0.0)

            self.displ = self.manager.create(self.none_displayable)

        def display_pos(self, mouse_pos):
            """
            Принимает на вход позицию мыши - mouse_pos.
            Выполняет некоторые вычисления. Выводит относительную и абсолютную координаты.
            """            

            width = float(config.screen_width)
            height = float(config.screen_height)
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            abs_width = mouse_x / width
            abs_height = mouse_y / height
            
            magic_num_x, magic_num_y = self.out_of_bounds_check(mouse_pos)

            relative = "({}, {})".format(mouse_pos[0], mouse_pos[1])
            absolute = "({:0.3}, {:0.3})".format(abs_width, abs_height)

            text_cords = Text(relative + '\n' + absolute, style="espe_text_24_extra")

            self.displ.set_child(text_cords)
            self.displ.x, self.displ.y = mouse_pos
            self.displ.x += magic_num_x
            self.displ.y -= magic_num_y
            self.manager.redraw()

        def out_of_bounds_check(self, mouse_pos):
            """
            Проверяет и на основе результата проверки перемещает информацию так, чтобы она не находилась за пределами экрана.
            """

            width = config.screen_width
            height = config.screen_height
            magic_num_x = -230 if mouse_pos[0] > width - 230 else 40

            magic_num_y = -25 if mouse_pos[1] < 21 else 25
            magic_num_y = 80 if mouse_pos[1] > height - 38 else magic_num_y

            return magic_num_x, magic_num_y

        def hide_pos(self):
            """
            Скрывает информацию о позиции.
            """

            self.displ.set_child(self.none_displayable)
            self.manager.redraw()
        
        def turn_on_picker(self):
            """
            Включает утилиту.
            """

            self.displ = self.manager.create(self.none_displayable)
            self.manager.redraw()

        def exit_picker(self):
            """
            Отключает утилиту.
            """
            
            self.displ.destroy()
            self.manager.redraw()

    def espe_pos_picker_event(ev, x, y, st):
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                store.espe_position_picker_displ.display_pos([x, y])
            if ev.button == 3:
                store.espe_position_picker_displ.hide_pos()


    espe_position_picker_manager = SpriteManager(None, espe_pos_picker_event)
    espe_position_picker_displ = ESPEPositionPicker(espe_position_picker_manager)

screen ESPE_position_picker():
    tag espe_position_picker
    zorder 1000

    add espe_position_picker_manager
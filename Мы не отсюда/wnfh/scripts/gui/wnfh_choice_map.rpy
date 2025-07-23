screen wnfh_map_screen(active_houses=None, click_callback=None):
    # Экран карты: каждый дом — отдельная кнопка
    # active_houses: список активных ID домов (по умолчанию все из JSON)
    # click_callback: функция(house_id) на клик
    default active_houses = active_houses if active_houses is not None else list(mask_index.keys())
    default click_cb       = click_callback or _on_house_click

    # Рисуем фоновую карту
    add wnfh_gui["map"]["map"]

    # Создаём кнопку для каждого дома
    for house_id, mask_path in mask_index.items():
        $ is_active = (house_id in active_houses)
        # Подготовим idle/hover изображения и действие
        $ idle_img  = AlphaMask(wnfh_gui["map"]["map_available"], mask_path) if is_active else Null()
        $ hover_img = AlphaMask(wnfh_gui["map"]["map_selected"],  mask_path) if is_active else Null()
        $ act       = Function(click_cb, house_id) if is_active else Null()

        imagebutton:
            # Полноэкранная кнопка с индивидуальной маской
            xysize config.screen_width, config.screen_height
            xpos 0 ypos 0

            idle  idle_img
            hover hover_img
            focus_mask mask_path
            action act
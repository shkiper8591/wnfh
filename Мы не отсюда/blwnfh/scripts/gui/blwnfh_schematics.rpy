init 2:
    
    screen blwnfh_schematic():
        modal True tag menu
        
        key "game_menu":
            action NullAction()
        
        key "screenshot":
            action NullAction()

        python:
            blwnfh_schematic_button = [
                ["return"      ,blwnfh_gui["settings"]["return"]               ,[Return()]                                           ],

            ]
            
            

        frame:
            background "#FFF"
            area(0.0, 0.0, 1.0, 1.0)
            at blwnfh_bg_spawn_atl
            frame: # ======================================================= # Выход
                background background_color
                area(0.0, 0.0, 200, 100)
                xanchor 0.0 yanchor 0.0
                frame:
                    xmargin 5
                    background button_blue
                    area(0.0, 0.5, 1.0, 1.0)
                    xanchor 0.0 yanchor 0.5
                    imagebutton:
                        action blwnfh_schematic_button[0][2]
                        idle blwnfh_schematic_button[0][1]
                        hover blwnfh_schematic_button[0][1]
                        hover_sound blwnfh_gui["sound"]["plimp"]
                        at blwnfh_mm_button_hover_atl()
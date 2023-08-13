init 2:
    
    screen wnfh_schematic():
        modal True tag menu
        
        key "game_menu":
            action NullAction()
        
        key "screenshot":
            action NullAction()

        python:
            wnfh_schematic_button = [
                ["return"      ,wnfh_gui["settings"]["return"]               ,[Return()]                                           ],

            ]
            
            

        frame:
            background "#FFF"
            area(0.0, 0.0, 1.0, 1.0)
            #at wnfh_bg_spawn_atl
            for index,data in enumerate(list(wnfh_Data.load_json())):
            #   while(true):
            #       for key_map in wnfh_Data.get(data)["Цепь выборов"]
            #for index, data in enumerate(len(wnfh_Data.load_json()),start=1)
                frame:
                    background "#AAA"
                    area(310*index+1,400 , 300,150 )
                    grid 1 3:
                        text str(data)
                        text wnfh_Data.getChoice_text(data)
                        text wnfh_Data.getChoice_result_text(data)                   
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
                        action wnfh_schematic_button[0][2]
                        idle wnfh_schematic_button[0][1]
                        hover wnfh_schematic_button[0][1]
                        hover_sound wnfh_gui["sound"]["plimp"]
                        at wnfh_mm_button_hover_atl()
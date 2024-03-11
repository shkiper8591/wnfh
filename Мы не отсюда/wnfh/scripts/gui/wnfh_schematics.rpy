init 2:
    
    screen wnfh_schematic():
        modal True tag menu
        
        key "game_menu":
            action NullAction()

        python:
            wnfh_schematic_button = [
                ["return"      ,wnfh_gui["settings"]["return"]               ,[Return()]                                           ],

            ]
            
            
        frame:
            if persistent.wnfh_debug_color:
                background frame_black
            else:
                background frame_transparent
            area(0.0, 0.0, 1.0, 1.0)
            #at wnfh_bg_spawn_atl
            viewport:
                mousewheel "horizontal"
                for index,data in enumerate(list(wnfh_Data.load_json())):
                    if str(data).find("key") > 0:
                #   while(true):
                #       for key_map in wnfh_Data.get(data)["Цепь выборов"]
                #for index, data in enumerate(len(wnfh_Data.load_json()),start=1)
                        frame:
                            background "#AAA"
                            area(310*index+1,400, 300, 600)
                            grid 1 1:
                                text str(wnfh_Data.get(data))
                    else:
                        frame:
                            background "#AAA"
                            area(310*index+1, 400, 300, 600)
                            grid 1 4:
                                text str(data)
                                text str(wnfh_Data.getChoice_points_sum('dv'))
                                text str(wnfh_Data.getChoice_text(data))
                                text str(wnfh_Data.getChoice_result_text(data))


            frame: # ======================================================= # Выход
                if persistent.wnfh_debug_color:
                    background frame_black
                else:
                    background frame_transparent
                area(0.0, 0.0, 200, 100)
                xanchor 0.0 yanchor 0.0
                imagebutton:
                    action wnfh_schematic_button[0][2]
                    idle wnfh_schematic_button[0][1]
                    hover wnfh_schematic_button[0][1]
                    hover_sound wnfh_gui["sound"]["plimp"]
                    at wnfh_mm_button_hover_atl()
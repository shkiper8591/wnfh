init 2:
    $ global background_color
    $ global button_red
    $ global button_green
    $ global button_blue
    $ global debag_switch
    $ global button_purpl
    $ persistent.mat_filter
    $ persistent.hentai_mod

    $ debag_switch = 0
    if debag_switch:
        $ background_color = "#0005"
        $ button_red =       "#F005"
        $ button_green =     "#0F05"
        $ button_blue =      "#00F5"
        $ button_purpl =     "#F0F5" 
    else:
        $ background_color = "#0000"
        $ button_red =       "#0000"
        $ button_green =     "#0000"
        $ button_blue =      "#0000"
        $ button_purpl =     "#0000"

    screen blwnfh_preferences():
        modal True tag menu
        $ bar_full = Frame(blwnfh_gui["settings"]["bar_full"], 73, 73)
        $ bar_null = Frame(blwnfh_gui["settings"]["bar_null"], 73, 73)
        $ htumb    = blwnfh_gui["settings"]["htumb"]
        key "game_menu":
            action NullAction()
        
        key "screenshot":
            action NullAction()
                
        python:
            def menu_img_status(imgf, condition="hover"):
                if condition == "hover":
                    return im.MatrixColor(imgf, im.matrix.contrast(1.7))
                if condition == "insensitive":
                    return im.Alpha(imgf, 0.38)
                    
            blwnfh_preferences_button = [
                
                 #Тег кнопки    #Изображение кнопки                               #Действие кнопки
                ["return"      ,blwnfh_gui["settings"]["return"]               ,[Return()]                                           ],
                
            ]
            blwnfh_underwrites = {"skip":[_preferences.skip_unseen,"Прочитанное","Всё"],"font":[persistent.font_size=="large","Обычный","Жирный"]}
            blwnfh_preferences_switch = [
                 #Тег переключалки   #Текст кнопки        #Вкл.                                                                                                             #Выкл.
                ["fullscreen"       ,"Полный экран"               ,[Preference("display", "fullscreen"),              Play("sound", blwnfh_sfx_list["plimp2"])]           ,  Preference("display", "window")                                                              , _preferences.fullscreen         ],
                ["autoforward"      ,"Автопереход"                ,[Preference("auto-forward after click", "enable"), Play("sound", blwnfh_sfx_list["plimp2"])]           ,  [Preference("auto-forward time", 0), Preference("auto-forward after click", "disable")]      , _preferences.afm_time != 0     ],
                ["skip"             ,"Пропускать"                 ,[Preference("skip", "all"),                        Play("sound", blwnfh_sfx_list["plimp2"])]           ,  Preference("skip", "seen")                                                                   , _preferences.skip_unseen        ],
                ["lovepoints"       ,"Заглушка"                   ,[NullAction(),                                     Play("sound", blwnfh_sfx_list["plimp2"])]           ,  NullAction()                                                                                 , NullAction()        ],
                ["font"             ,"Шрифт"                      ,[SetField(persistent, "font_size", "large"),       Play("sound", blwnfh_sfx_list["plimp2"])]           ,  SetField(persistent, "font_size", "small")                                                   , persistent.font_size == "large" ],
                ["lkjmsdl"          ,"Заглушка"                   ,[NullAction(),                                     Play("sound", blwnfh_sfx_list["plimp2"])]           ,  NullAction()                                                                                 , NullAction() ],                  
                ["hentai"                                         ,[SetField(persistent, "hentai_mod", True),         Play("sound", blwnfh_sfx_list["nya"])]              ,  SetField(persistent, "hentai_mod", False)                                                    , persistent.hentai_mod           ], 
                ["mat_filter"       ,"Мат-фильтр"                 ,SetField(persistent, "mat_filter", 1),             SetField(persistent, "mat_filter", 2)               ,  SetField(persistent, "mat_filter", 0)                                                        , ["Без цензуры","Как-то так: #@!&%","Литератураня замена"]]
            ]

            blwnfh_preferences_bar = [
                
                 #Тег бара           #Название бара                       #Действие
                ["music"            ,"Музыка"              ,Preference("music volume")                                       ],
                ["sound"            ,"Звуки"               ,Preference("sound volume")                                       ],
                ["ambience"         ,"Эмбиент"             ,Preference("voice volume")                                       ],
                ["text_speed"       ,"Скорость текста"     ,Preference("text speed")                                         ],
                ["autoforward_time" ,"Время автопереходов" ,Preference("auto-forward time")                                  ],
            ]
            key_values=["triple_off","triple_on1","triple_on2"]
        
          
        
        
        frame:
            background im.MatrixColor(im.Blur(blwnfh_gui["main_menu"]["mm_bg"], 3.0), im.matrix.tint(0.7, 0.7, 0.7))
            area(0.0, 0.0, 1.0, 1.0)
        frame:
            background blwnfh_gui["settings"]["base"]
            area(0.5, 0.0, 1461, 1080)
            xanchor 0.5
            
            frame:
                background background_color
                area(0.5, 0.0, 1.0, 0.15)
                xanchor 0.5
            
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
                            action blwnfh_preferences_button[0][2]
                            idle blwnfh_preferences_button[0][1]
                            hover blwnfh_preferences_button[0][1]
                            hover_sound blwnfh_gui["sound"]["plimp"]
                            at blwnfh_mm_button_hover_atl()
                                
                add blwnfh_gui["settings"]["pref_title"]:
                    pos(0.5, 0.0)
                    xanchor 0.5
            
            frame:
                background background_color
                area(0.5, 0.16, 1.0, 0.84)
                xanchor 0.5
                grid 1 3:
                    for bar in blwnfh_preferences_bar[0:3]:
                        frame:
                            background background_color
                            area(0.0, 0.0, 1.0, 120)
                            frame:
                                background button_red
                                area(0.0, 0.5, 0.2, 1.0)
                                yanchor 0.5
                                text bar[1]:
                                    pos(0.5, 0.5)
                                    style "blwnfh_settings"
                                    xanchor 0.5
                                    size 70
                                    kerning 1
                                    min_width 200
                                    layout "tex"
                                    #action Play("sound", blwnfh_gui["sound"]["plimp"]) 
                            frame:
                                background button_green
                                area(0.95, 0.5, 0.75, 0.8)
                                xanchor 1.0 yanchor 0.5
                                bar value bar[2]:
                                    left_bar bar_full
                                    right_bar bar_null
                                    thumb htumb
                                    hover_thumb htumb
                                    xmaximum 1.0 ymaximum 73 yanchor 0.5 ypos 0.5
                                
                add blwnfh_gui["settings"]["line"]:
                    pos(0.5, 0.41)
                    xanchor 0.5
                grid 1 2:
                    pos(0.5, 0.42)
                    xanchor 0.5
                    for bar in blwnfh_preferences_bar[3:5]:
                        frame:
                            background background_color
                            area(0.0, 0.0, 1.0, 120)
                            frame:
                                background button_red
                                area(0.0, 0.5, 0.2, 1.0)
                                yanchor 0.5
                                text bar[1]:
                                    pos(0.5, 0.5)
                                    style "blwnfh_settings"
                                    xanchor 0.5
                                    size 50
                                    kerning 1
                                    min_width 200
                                    layout "tex"
                            frame:
                                background button_green
                                area(0.95, 0.5, 0.75, 0.8)
                                xanchor 1.0 yanchor 0.5
                                bar value bar[2]:
                                    left_bar bar_full
                                    right_bar bar_null
                                    thumb htumb
                                    hover_thumb htumb
                                    xmaximum 1.0 ymaximum 73 yanchor 0.5 ypos 0.5
                add blwnfh_gui["settings"]["line"]:
                    pos(0.5, 0.695)
                    xanchor 0.5

                
                frame: 
                    background background_color
                    area(0.5, 1.0, 1.0, 0.3)
                    xanchor 0.5 yanchor 1.0
                    frame: # ======================================================= Матфильтр
                        background background_color
                        area(0.5, 1.0, 420, 120)
                        xanchor 0.5 yanchor 1.0
                        vbox:
                            pos(0.5, 1.0)
                            xanchor 0.5 yanchor 1.0
                            text blwnfh_preferences_switch[7][1]:
                                style "blwnfh_settings"
                                pos(0.5, 1.0)
                                xanchor 0.5 yanchor 0.5
                                text_align 0.5
                                size 50
                                kerning 1
                                min_width 200
                                layout "tex"
                            imagebutton:
                                pos(0.5, 0.9)
                                xanchor 0.5 yanchor 0.5
                                idle blwnfh_gui["settings"][key_values[persistent.mat_filter]]
                                hover blwnfh_gui["settings"][key_values[persistent.mat_filter]]
                                action blwnfh_preferences_switch[7][2+persistent.mat_filter]
                            text blwnfh_preferences_switch[7][5][persistent.mat_filter]:
                                style "blwnfh_settings_underwrites"
                                pos(0.5, 1.0)
                                xanchor 0.5 yanchor 0.5
                                text_align 0.5
                                size 30
                                kerning 1
                                min_width 200
                                layout "tex"


                    frame: # ======================================================= Хентай
                        background background_color
                        area(0.5, 0.05, 300, 100)
                        xanchor 0.5 yanchor 0.0
                        vbox:
                            pos(0.5, 0.5)
                            xanchor 0.5 yanchor 0.5
                            add blwnfh_gui["settings"]["hentai"]
                            if blwnfh_preferences_switch[6][3]: #Выкл
                                imagebutton:
                                    pos(0.5, 0.2)
                                    xanchor 0.5 yanchor 0.5
                                    idle im.Scale(blwnfh_gui["settings"]["hentai_on"], 112, 64)
                                    hover im.Scale(blwnfh_gui["settings"]["hentai_on"], 112, 64)
                                    action blwnfh_preferences_switch[6][2]
                            if not blwnfh_preferences_switch[6][3]: #Вкл
                                imagebutton:
                                    pos(0.5, 0.2)
                                    xanchor 0.5 yanchor 0.5
                                    idle im.Scale(blwnfh_gui["settings"]["hentai_off"], 112, 64)
                                    hover im.Scale(blwnfh_gui["settings"]["hentai_off"], 112, 64)
                                    action blwnfh_preferences_switch[6][1]

                    grid 2 3: # ==================================================== Кнопки
                        pos (0.5, 0.5)
                        xanchor 0.5 yanchor 0.5
                        xspacing 430
                        for i in range(6):
                            frame:
                                background background_color
                                area(0.0, 0.0, 500, 80)
                                xanchor 0.0 yanchor 0.0
                                #for switch in blwnfh_preferences_switch[0:1]:
                                frame:
                                    background button_blue
                                    area(1.0, 0.5, 100, 1.0)
                                    xanchor 1.0 yanchor 0.5
                                    if blwnfh_preferences_switch[i][4]: #Выкл
                                        imagebutton:
                                            pos(0.5, 0.5)
                                            xanchor 0.5 yanchor 0.5
                                            idle blwnfh_gui["settings"]["on"]
                                            hover blwnfh_gui["settings"]["on"]
                                            action blwnfh_preferences_switch[i][3]
                                    if not blwnfh_preferences_switch[i][4]: #Вкл
                                        imagebutton:
                                            pos(0.5, 0.5)
                                            xanchor 0.5 yanchor 0.5
                                            idle blwnfh_gui["settings"]["off"]
                                            hover blwnfh_gui["settings"]["off"]
                                            action blwnfh_preferences_switch[i][2]
                                frame:
                                    background button_red
                                    area(0.0, 0.5, 380, 1.0)
                                    xanchor 0.0 yanchor 0.5
                                    vbox:
                                        pos(0.5, 0.5)
                                        xanchor 0.5 yanchor 0.5
                                        spacing 0
                                        frame:
                                            background button_blue
                                            area(0.0, 0.0, 350, 30)
                                            xanchor 0.0 yanchor 0.0
                                        
                                            text blwnfh_preferences_switch[i][1]:
                                                style "blwnfh_settings"
                                                pos(0.5, 0.5)
                                                xanchor 0.5
                                                text_align 0.5
                                                size 50
                                                kerning 1
                                                min_width 200
                                                layout "tex"
                                        if blwnfh_preferences_switch[i][0] in blwnfh_underwrites.keys():
                                            frame:
                                                background button_green
                                                area(0.0, 0.0, 350, 30)
                                                xanchor 0.0 yanchor 0.0
                                                text blwnfh_underwrites[blwnfh_preferences_switch[i][0]][int(blwnfh_underwrites[blwnfh_preferences_switch[i][0]][0])+1]:
                                                    style "blwnfh_settings_underwrites"
                                                    pos(0.5, 1.0)
                                                    xanchor 0.5 yanchor 0.5
                                                    text_align 0.5
                                                    size 30
                                                    kerning 1
                                                    min_width 200
                                                    layout "tex"
                  

                        

            

















screen settings_widget_sukablyat_on_blwnfh():
    text "Маты будут выглядеть так: блять" xpos 0.653 ypos 0.6:
        style "blwnfh_settings"
screen settings_widget_sukablyat_off_blwnfh():
    text "Выключить матфильтр" xpos 0.653 ypos 0.6:
        style "blwnfh_settings"   
screen settings_widget_sukablyat_type_censor_blwnfh():
    text "Маты будут выглядеть так: @%#$!" xpos 0.653 ypos 0.6:
        style "blwnfh_settings"
screen settings_widget_sukablyat_type_change_blwnfh():
    text "Маты будут выглядеть так: блин" xpos 0.653 ypos 0.6:
        style "blwnfh_settings"

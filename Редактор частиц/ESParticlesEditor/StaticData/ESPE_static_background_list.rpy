init:
    image espe_chromakey = Solid("#00FF00", xsize=1920, ysize=1080)
    image espe_red = Solid("#f00000", xsize=1920, ysize=1080)

    $ ESPE_static_bg_list = [
        ["Свой мир", [
                ["Комната Семёна", "bg semen_room"],
                ["Комната Семёна. Окно", "bg semen_room_window"],
                ["Автобусная остановка", "bg bus_stop"],
                ["Интро. Лиаз", "bg int_liaz"],
                ["В Лиазе", "bg intro_xx"]
            ]
        ],
        ["Дорога от лагеря", [
                ["День", "bg ext_road_day"],
                ["Закат", "bg ext_road_sunset"],
                ["Ночь", "bg ext_road_night2"],
                ["Город. Ночь", "bg ext_road_night"]
            ]
        ],
        ["Автобус/остановка", [
                ["В автобусе. День", "bg int_bus"],
                ["В автобусе. Люди. День", "bg int_bus_people_day"],
                ["В автобусе. Ночь", "bg int_bus_night"],
                ["В автобусе. Люди. Ночь", "bg int_bus_people_night"],
                ["В автобусе. Силуэты", "bg int_bus_black"],
                ["Остановка. Автобус. День", "bg ext_bus"],
                ["Остановка. День", "bg ext_no_bus"],
                ["Остановка. Закат", "bg ext_no_bus_sunset"],
                ["Остановка. Автобус. Ночь", "bg ext_bus_night"],
                ["Остановка. День", "bg ext_no_bus_night"]
            ]
        ],
        ["Лагерные ворота", [
                ["День", "bg ext_camp_entrance_day"],
                ["Ночь", "bg ext_camp_entrance_night"]
            ]
        ],
        ["Кружок кибернетики", [
                ["День", "bg ext_clubs_day"],
                ["Ночь", "bg ext_clubs_night"],
                ["Внутри. День", "bg int_clubs_male_day"],
                ["Внутри. Ночь", "bg int_clubs_male_night"],
                ["Подсобка", "bg int_clubs_male2_night"],
                ["Подсобка. Без света", "bg int_clubs_male2_night_nolight"]
            ]

        ],
        ["Площадь", [
                ["День", "bg ext_square_day"],
                ["День с городом", "bg ext_square_day_city"],
                ["Закат", "bg ext_square_sunset"],
                ["Ночь", "bg ext_square_night"],
                ["Вечеринка. Ночь", "bg ext_square_night_party"],
                ["После вечеринки. Ночь", "bg ext_square_night_party2"]
            ]
        ],
        ["Домики", [
                ["День", "bg ext_houses_day"],
                ["Закат", "bg ext_houses_sunset"]
            ]
        ],
        ["Столовая", [
                ["День", "bg ext_dining_hall_away_day"],
                ["Закат", "bg ext_dining_hall_away_sunset"],
                ["Ночь", "bg ext_dining_hall_away_night"],
                ["Близко. День", "bg ext_dining_hall_near_day"],
                ["Близко. Закат", "bg ext_dining_hall_near_sunset"],
                ["Близко. Ночь", "bg ext_dining_hall_near_night"],
                ["Внутри. День", "bg int_dining_hall_day"],
                ["Внутри. Люди. День.", "bg int_dining_hall_people_day"],
                ["Внутри. Закат", "bg int_dining_hall_sunset"],
                ["Внутри. Ночь", "bg int_dining_hall_night"]
            ]
        ],
        ["Медпункт", [
                ["День", "bg ext_aidpost_day"],
                ["Ночь", "bg ext_aidpost_night"],
                ["Внутри. День", "bg int_aidpost_day"],
                ["Внутри. Яблоко. День", "bg int_aidpost_day_apple"],
                ["Внутри. Ночь", "bg int_aidpost_night"]
            ]
        ],
        ["Сцена", [
                ["Ночь", "bg ext_stage_normal_day"],
                ["День", "bg ext_stage_normal_night"],
                ["Вся сцена. Ночь", "bg ext_stage_big_night"]
            ]
        ],
        ["Спорт. площадь", [
                ["День", "bg ext_playground_day"],
                ["Ночь", "bg ext_playground_night"],
            ]
        ],
        ["Пляж", [
                ["День", "bg ext_beach_day"],
                ["Закат", "bg ext_beach_sunset"],
                ["Ночь", "bg ext_beach_night"]
            ]
        ],
        ["Лодочная станция", [
                ["День", "bg ext_boathouse_day"],
                ["Ночь", "bg ext_boathouse_night"]
            ]
        ],
        ["Библиотека", [
                ["День", "bg ext_library_day"],
                ["Ночь", "bg ext_library_night"],
                ["Внутри. День", "bg int_library_day"],
                ["Внутри. Ночь", "bg int_library_night2"],
                ["Внутри. Без света. Ночь", "bg int_library_night"]
            ]
        ],
        ["Муз. клуб", [
                ["День", "bg ext_musclub_day"],
                ["Внутри. День", "bg int_musclub_day"]
            ]
        ],
        ["Умывальники", [   
                ["Далеко. День", "bg ext_washstand_day"],
                ["Близко. Ночь", "bg ext_washstand2_day"]
            ]
        ],
        ["Баня", [
                ["Ночь", "bg ext_bathhouse_night"]
            ]
        ],
        ["Домик Ольги", [
                ["День", "bg ext_house_of_mt_day"],
                ["Закат", "bg ext_house_of_mt_sunset"],
                ["Ночь", "bg ext_house_of_mt_night"],
                ["Ночь. Без света", "bg ext_house_of_mt_night_without_light"],
                ["Внутри. День", "bg int_house_of_mt_day"],
                ["Внутри. Закат", "bg int_house_of_mt_sunset"],
                ["Внутри. Ночь", "bg int_house_of_mt_night"],
                ["Внутри. Без света. Ночь", "bg int_house_of_mt_night2"],
                ["Внутри. Без фон. Ночь", "bg int_house_of_mt_noitem_night"]
            ]
        ],
        ["Домик Алисы/Ульяны", [
                ["День", "bg ext_house_of_dv_day"],
                ["Ночь", "bg ext_house_of_dv_night"],
                ["Внутри. День", "bg int_house_of_dv_day"],
                ["Внутри. Ночь", "bg int_house_of_dv_night"]
            ]
        ],
        ["Домик Лены/Мику", [
                ["День", "bg ext_house_of_un_day"],
                ["Внутри. День", "bg int_house_of_un_day"],
                ["Внутри Ночь", "bg int_house_of_un_night"]
            ]
        ],
        ["Домик Слави/Жени", [
                ["День", "bg ext_house_of_sl_day"],
                ["Внутри. День", "bg int_house_of_sl_day"]
            ]
        ],
        ["Остров", [
                ["День", "bg ext_island_day"],
                ["Ночь", "bg ext_island_night"]
            ]
        ],
        ["Лес/Поляна", [
                ["День", "bg ext_path2_day"],
                ["Тропинка. День", "bg ext_path_day"],
                ["Тропинка. Закат", "bg ext_path_sunset"],
                ["Ночь", "bg ext_path2_night"],
                ["Тропинка. Ночь", "bg ext_path_night"],
                ["Поляна. День", "bg ext_polyana_day"],
                ["Поляна. Закат", "bg ext_polyana_sunset"],
                ["Поляна. Ночь", "bg ext_polyana_night"]
            ]
        ],
        ["Старый корпус", [
                ["Ночь", "bg ext_old_building_night"],
                ["Лунный свет. Ночь", "bg ext_old_building_night_moonlight"],
                ["Внутри. Ночь", "bg int_old_building_night"]
            ]
        ],
        ["Катакомбы/бункер/шахты", [
                ["Туннель", "bg int_catacombs_entrance"],
                ["Туннель. Красное свечение", "bg int_catacombs_entrance_red"],
                ["Туннель. Дыра в шахту", "bg int_catacombs_hole"],
                ["Дверь бункера", "bg int_catacombs_door"],
                ["Бункер", "bg int_catacombs_living"],
                ["Бункер. Слом. дверь", "bg int_catacombs_living_nodoor"],
                ["Шахта", "bg int_mine"],
                ["Шахта. Поворот", "bg int_mine_halt"],
                ["Шахта. Развилка", "bg int_mine_crossroad"],
                ["Шахта. Дверь в котельную", "bg int_mine_door"],
                ["Шахта. Котельная", "bg int_mine_room"],
                ["Шахта. К. свет. Котельная", "bg int_mine_room_red"],
                ["Выход. Свет. Ночь", "bg int_mine_exit_night_light"],
                ["Выход. Без света. Ночь", "bg int_mine_exit_night_nolight"],
                ["Выход. Факел", "bg int_mine_exit_night_torch"],
            ]
        ],
        ["Цвета", [
                ["Зелёный фон", "espe_chromakey"],
                ["Красный фон", "espe_red"],
                ["Чёрный фон", "black"],
                ["Белый фон", "white"]
            ]
        ]
    ]
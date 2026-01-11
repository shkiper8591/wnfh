init python:

    wnfh_slot_data = {
        "chapter": 999,
        "game_date": "00-00-0000", ## DD-MM-YYYY
        "scene": "Омниссия не благословил этот процесс. Свяжитесь с ближайшим магосом для проведения обряда устранения сбоев."
        }

    def wnfh_get_string_lp():
        result_text = "|".join(str(wnfh_Data.getChoice_points_sum(character)) for character in wnfh_character_order)
        return result_text

    def wnfh_to_roman(num):
        mapping = {
            0: "Пролог",
            1: "Глава I",
            2: "Глава II",
            3: "Глава III",
            4: "Глава IV",
            5: "Глава V",
            999: "ОШИБКА",
        }
        return mapping.get(num, "")

    def wnfh_month_to_genitive(month):
        months = {
            0: "мяу",
            1: "января",
            2: "февраля",
            3: "марта",
            4: "апреля",
            5: "мая",
            6: "июня",
            7: "июля",
            8: "августа",
            9: "сентября",
            10: "октября",
            11: "ноября",
            12: "декабря"
        }
        return months.get(int(month), "")

    def wnfh_set_slot_data(chapter, game_date, scene):
        wnfh_slot_data["chapter"] = chapter
        wnfh_slot_data["game_date"] = game_date
        wnfh_slot_data["scene"] = scene
    

    def wnfh_get_string_slot_data():
        result_text = "{}|{}|{}".format(wnfh_slot_data["chapter"], wnfh_slot_data["game_date"], wnfh_slot_data["scene"])
        return result_text

    def wnfh_create_slot_extra_data():
        return "{}##{}".format(wnfh_get_string_lp(), wnfh_get_string_slot_data())

    def wnfh_get_slot_extra_data(save_name):
        data_dict = {}
        slot_info = renpy.loadsave.slot_json(save_name)
        if slot_info is None:
            return data_dict
        extra_info = slot_info["_save_name"]

        # Разбор двух частей: LP и slot data
        lp_info, slot_data_info = extra_info.split("##")
        lp_info_array = lp_info.split("|")

        data_dict["lp_info"] = {}

        for index, char in enumerate(wnfh_character_order):
            data_dict["lp_info"][char] = lp_info_array[index]

        # Разбор chapter | date | scene
        chapter, game_date, scene = slot_data_info.split("|")

        # Преобразование
        chapter_roman = wnfh_to_roman(int(chapter))

        day, month, year = game_date.split("-")
        month_name = wnfh_month_to_genitive(month)

        # Формирование читабельных строк
        readable_chapter = "{}".format(chapter_roman)
        readable_date = "{} {} {}".format(day, month_name, year)
        readable_scene = "{}".format(scene)

        data_dict["chapter"] = readable_chapter
        data_dict["game_date"] = readable_date
        data_dict["scene"] = readable_scene

        return data_dict

    def wnfh__slotname(name, page=None, slot=False):

        if slot:
            return name

        if page is None:
            page = persistent._file_page

        try:
            page = int(page)
            page = page + persistent._file_folder * config.file_pages_per_folder
        except ValueError:
            pass

        if config.linear_saves_page_size is not None:
            try:
                page = int(page)
                name = int(name)
                return str((page - 1) * config.linear_saves_page_size + name)
            except ValueError:
                pass

        page = str(page)
        name = str(name)

        return page + "-" + name

    class wnfh_FileSave(Action, DictEquality):

        alt = "Save slot [text]"
        slot = None
        action = None

        def __init__(self, name, extra_info = None, confirm=True, newest=True, page=None, cycle=False, slot=False, action=None):

            self.name = name
            self.confirm = confirm
            self.page = page
            self.cycle = cycle
            self.slot = slot
            self.action = action
            self.extra_info = extra_info if extra_info is not None else save_name

            try:
                self.alt = __("Save slot %s: [text]") % (name,)
            except Exception:
                self.alt = "Save slot %s: [text]" % (name,)

        def __call__(self):

            if not self.get_sensitive():
                return

            fn = "{}-{}".format(self.page, self.name)

            if renpy.scan_saved_game(fn):
                if self.confirm:
                    layout.yesno_screen(layout.OVERWRITE_SAVE, wnfh_FileSave(self.name, self.extra_info, False, False, self.page, cycle=self.cycle, slot=self.slot, action=self.action))
                    return

            renpy.save(fn, extra_info=self.extra_info)

            renpy.restart_interaction()

            return renpy.run(self.action)

        def get_sensitive(self):
            if _in_replay:
                return False
            elif main_menu:
                return False
            elif (self.page or persistent._file_page) == "auto":
                return False
            else:
                return True

        def get_selected(self):
            if not self.confirm:
                return False

            return renpy.newest_slot(r'\d+') == wnfh__slotname(self.name, self.page, self.slot)
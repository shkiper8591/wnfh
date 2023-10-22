init -1002:
    if "wnfh_database" not in globals():
        default wnfh_database = {}
    if "wnfh_database_test" not in globals():
        default wnfh_database_test = {}
init -1001 python :
    import os
    import json
    #class StorageManager:
    #    def __init__(self,head=None):
    #        self.SaveObject = head
    #        self.next
    #    def container(self,head):
    #        lastEntry = self.head
    #        while(lastEntry):
    #            if head == lastEntry.head:
    #                return True
    #            else:
    #                lastEntry = lastEntry.
    #
    #
    #class SavelinkedList:
    #    def __init__(self):
    #        self.head=None
    #class Storage(object,index,memoryValue):
    #    def __init__(index,):
    #        self.head=None
    #    def __NAME_:
    #    def __EXIT__:
    #    def __ENTER__:

    class wnfh_BD(object):
        def __init__(self,location):
            self.location=os.path.expanduser(location)
            self.path_enviroment = location.split(".")[1].split("/")[-1]
            self.BD_INIT_MODULE = {}
            self.load(self.location)
            self.Encryption = True
        def load(self, location):
            #if os.path.exists(location):
            if self.path_enviroment in locals() or self.path_enviroment in globals():
                self.open_f()
            return True
        def load_json(self):
            return json.load(open(self.location,"r"))
        def open_f(self):
            self.BD_INIT_MODULE =  globals()[self.path_enviroment]
            self.dumpdb()
            #self.BD_INIT_MODULE = json.load(open(self.location,"r"))
        def dumpSave(self):
            globals()[self.path_enviroment] = self.BD_INIT_MODULE
        def dumpdb(self):
            try:
                json.dump(self.BD_INIT_MODULE, open(self.location, "w+"),ensure_ascii=False,indent=4)
                return True
            except:
                return False

        """
        установка нового флага
        функция принимает название флага и значение
        #wnfh_Data.FlagSet("d2_zavtrak_s_lenoy",True) 
        """
        def FlagSet(self,key,value = True):
            self.BD_INIT_MODULE[str(key)] = {'type':'flag','value':value}
            self.dumpdb()
            self.dumpSave()
            return True
        """
        Получение значения флага
        функция принимает название флага и возвращает значение
        #wnfh_Data.FlagGet("d2_zavtrak_s_lenoy")
        """
        def FlagGet(self,key):
            self.open_f()
            try:
                return self.BD_INIT_MODULE[key]['value']
            except KeyError:
                return None
        def write(self , key , value):
            self.BD_INIT_MODULE[str(key)] = value
            self.dumpdb()
            self.dumpSave()
            return True
        def get(self , key):
            try:
                return self.BD_INIT_MODULE[key]
            except KeyError:
                #print("Не было найдено значений" + str(key))
                return False
        """
        Описание:
        wnfh_Data.getChoice_result_number("1d_3")
        Возвращает номер выбранного ответа в выборе под состемным названием 1d_3 прим получаемого значения -2
        """
        def getChoice_result_number(self , key):
            try:
                return self.BD_INIT_MODULE[key]["Выбранно"]
            except KeyError:
                #print("Не было найдено значений" + str(key))
                return False
        """
        Описание:
        wnfh_Data.getChoice_result_text("1d_3")
        Возвращает текст выбранного ответа в выборе под состемным названием 1d_3 прим получаемого значения "Сбежать"
        """
        def getChoice_result_text(self , key):
            try:
                return self.BD_INIT_MODULE[key]["Текст выбора"]
            except KeyError:
                #print("Не было найдено значений" + str(key))
                return False
        """
        Описание:
        wnfh_Data.getChoice_text("1d_3")
        Возвращает заголовок выбора в выборе под состемным названием 1d_3 прим. Что же нам делать?
        """
        def getChoice_text(self , key):
            try:
                return self.BD_INIT_MODULE[key]["Название выбора"]
            except KeyError:
                #print("Не было найдено значений" + str(key))
                return False
        """
        Описание:
        wnfh_Data.getChoice_result_number("1d_3")
        Возвращает номер выбранного ответа в выборе под состемным названием 1d_3 прим получаемого значения -2
        """
        def getChoice_result_points(self , key):
            try:
                return self.BD_INIT_MODULE[key]["Влияние на персонажей"]
            except KeyError:
                #print("Не было найдено значений" + str(key))
                return False
        """
        Описание:
        wnfh_Data.getChoice_result_points():
        -----------------------------------
        1) wnfh_Data.getChoice_result_points(("1d_3"))
        Возвращает лавпойнты характерные выбору прим:
        {
        "uv":3
        "ls":-2
        }
        2)wnfh_Data.getChoice_result_points(("1d_3","uv"))
        возвращает число лавпойнтов персонажа uv характерные выбору прим. 3
        """
        def getChoice_result_points(self, key, person):
            try:
                return self.BD_INIT_MODULE[key]["Влияние на персонажей"][person]
            except KeyError:
                #print("Не было найдено значений" + str(key))
                return False
        def getChoice_points_sum(self, person):
            sum = 0
            self.open_f()
            for data in list(self.BD_INIT_MODULE ):
                try:
                    sum += int(self.BD_INIT_MODULE[data]["Влияние на персонажей"][person])
                except KeyError:
                    pass
                except TypeError:
                    pass
                except Exception:
                    raise 'Ошибка подсчёта лавпойнтов'
            return sum
        def delete(self , key):
            if not key in self.db:
                return False
            del self.db[key]
            self.dumpdb()
            self.dumpSave()
            return True
        def resetDB(self):
            self.BD_INIT_MODULE = {}
            self.write()
            return True

init -998 python:
    style.button_text_7dl = Style(style.default)
    style.button_text_7dl.color = "#c8ffff"
    style.button_text_7dl.insensitive_color = "#c8c8c8"
    style.button_text_7dl.selected_color = "#ffffc8"
    style.button_text_7dl.text_align = 0.5
    style.button_text_7dl.xalign = 0.5
    style.button_text_7dl.yalign = 0.5
    style.button_text_7dl.ypos = 9
    style.button_text_7dl.xpadding = 6
    style.button_text_7dl.size = 13

    def wnfh_add_flag(data, env):
        for i in data:
            if env == "prod":
                wnfh_Data.FlagSet(i, data[i])
            elif env == "test":
                wnfh_Data_test.FlagSet(i, data[i])


    def wnfh_find_Operand(data, env):
        if len(data[0]) == 6:
            data_set = data[0][4]
            wnfh_add_flag(data[0][5], env)
        elif len(data[0]) == 4:
            data_set = "Нет влияния"
        elif len(data[0]) == 5:
            for i in data[0][4]:
                if i in wnfh_characters.keys():
                    data_set = data[0][4]
                else:
                    wnfh_add_flag(data[0][4], env)
                    data_set = "Нет влияния"
            pass
        else:
            raise "Ебалан выбор оформлен неверно"
            sys.exit(1)
        return data_set

init 0 python:
    def widget_lp_wnfh():
        ui.button(clicked=None, style="wnfh_menu", xpos=0.79, xanchor=1.0, xminimum=120)
        ui.text("%s: %d" % ("Лена", wnfh_Data_test.getChoice_points_sum("usw")), style="button_text_7dl", color="#ff55ff")
        ui.button(clicked=None, style="wnfh_menu", xpos=0.93, xanchor=1.0, xminimum=120)
        ui.text("%s: %d" % ("Катя", wnfh_Data_test.getChoice_points_sum("kat")), style="button_text_7dl", color="#00ea32")


    config.overlay_functions.append(widget_lp_wnfh)
init -10 python :
    import os
    import json
    class BD(object):
        def __init__(self,location):
            self.location=os.path.expanduser(location)
            self.path_enviroment = location.split(".")[1].split("/")[-1]
            self.load(self.location)
            self.Encryption = True
        def load(self, location):
            #if os.path.exists(location):
            if self.path_enviroment in locals() or self.path_enviroment in globals():
                self.open_f()
            else:
                self.BD_INIT_MODULE = {}
                locals()[self.path_enviroment] = {}
            return True
        def load_json(self):
            return json.load(open(self.location,"r"))
        def open_f(self):
            self.BD_INIT_MODULE =  locals()[self.path_enviroment]
            #self.BD_INIT_MODULE = json.load(open(self.location,"r"))
        def dumpSave(self):
            try:
                locals()[self.path_enviroment] = self.BD_INIT_MODULE
            except:
                pass
        def dumpdb(self):
            try:
                json.dump(self.BD_INIT_MODULE, open(self.location, "w+"),ensure_ascii=False,indent=4)
                return True
            except:
                return False
        def write(self , key , value):
            try:
                self.BD_INIT_MODULE[str(key)] = value
                self.dumpdb()
                self.dumpSave()
                return True
            except Exception as e:
                #print("Ошибка записи в бд: " + str(e))
                return False   
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
                for data in list(self.BD_INIT_MODULE ):
                    try:
                        sum += int(self.BD_INIT_MODULE[data]["Влияние на персонажей"][person])
                    except KeyError:
                        pass
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

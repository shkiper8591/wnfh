init -10 python :
    import os
    import json
    class BD(object):
        def __init__(self,location):
            self.location=os.path.expanduser(location)
            self.load(self.location)
        def load(self, location):
            if os.path.exists(location):
                self.open_f()
            else:
                self.BD_INIT_MODULE = {}
            return True
        def open_f(self):
            self.BD_INIT_MODULE = json.load(open(self.location,"r"))

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
        def getChoice_result_number(self , key):
            try:
                return self.BD_INIT_MODULE[key]["Выбранно"]
            except KeyError:
                #print("Не было найдено значений" + str(key))
                return False
        def getChoice_result_text(self , key):
            try:
                return self.BD_INIT_MODULE[key]["Текст выбора"]
            except KeyError:
                #print("Не было найдено значений" + str(key))
                return False
        def getChoice_text(self , key):
            try:
                return self.BD_INIT_MODULE[key]["Название выбора"]
            except KeyError:
                #print("Не было найдено значений" + str(key))
                return False
        def getChoice_result_points(self , key):
            try:
                return self.BD_INIT_MODULE[key]["Влияние на персонажей"]
            except KeyError:
                #print("Не было найдено значений" + str(key))
                return False
        def getChoice_result_points(self , key, person):
            try:
                return self.BD_INIT_MODULE[key]["Влияние на персонажей"][person]
            except KeyError:
                #print("Не было найдено значений" + str(key))
                return False
        def delete(self , key):
            if not key in self.db:
                return False
            del self.db[key]
            self.dumpdb()
            return True
        def resetDB(self):
            self.BD_INIT_MODULE = {}
            self.write()
            return True

"""
2023 git@Deopster
"""
init -3:
    label null_ellement:
        $ wnfh_Data = wnfh_BD("./game/saves/wnfh_database.json")
        $ wnfh_Data_test = wnfh_BD("./game/saves/wnfh_database_test.json")
init -1002:
    
    #"""
    #Инициализация переменных renpy default если их ещё не существует в глобальной области видимости
    #Необходимо для работы rollback (перемотки диалогов назад), ибо именно переменные типа default
    #renpy трекирует при перемотке. Таким образом информация по выборам кешируется в данной переменной
    #в формате словаря и загружается в классе wnfh_BD при необходимости обновить данные
    #"""
    if "wnfh_database" not in globals():
        default wnfh_database = {}
    if "wnfh_database_test" not in globals():
        default wnfh_database_test = {}
    python:
        class StorageManager:
            def init(self,head=None):
                self.SaveObject = head
                self.next
            def container(self,head):
                lastEntry = self.head
                while(lastEntry):
                    if head == lastEntry.head:
                        return True
                    else:
                        lastEntry = lastEntry.next
        
        
        class SavelinkedList:
            def init(self):
                self.head=None
        class Storage:
            def init(self,object, index = None, memoryValue = None):
                self.head=None
init -1001 python :
    import os
    import json
    #"""
    #концептуально:
    #default {enviroment(test/prod)} <-> wnfh_BD (BD_INIT_MODULE) - метод класса (запись / чтение ) -> json <-> renpy новелла
    #"""
    class wnfh_BD(object):
        """
        Создание объектов класса происходит позже инициализации класса в файле main_menu.rpy
        !!!! ТАМ ЖЕ УКАЗАН ПУТЬ JSON И НАЗВАНИЕ ФАЙЛА wnfh_Data.dumpSave() (обновлено, 4 строка этого файла)       
        !!!! ВАЖНО - НАЗВАНИЕ ФАЙЛА JSON ДОЛЖНО СОВПАДАТЬ С НАИМЕНОВАНИЕМ default ПЕРЕМЕННОЙ пример строка 32
        объект используется в качестве 'указателя' области работы и хранения данных а также их разграничения между тестовой областью и продуктовой (игровой)
        """
        def __init__(self,location):
            self.location=os.path.expanduser(location) #местоположение json а также окружение prod / test
            self.path_enviroment = location.split(".")[1].split("/")[-1] #Получение название json из переменной окружения прим "./game/saves/wnfh_database.json" -> "wnfh_database"
            self.achivments_path = "./game/saves/"+self.path_enviroment+"_achivments.json"
            self.BD_INIT_MODULE = {} #инициализация словаря хранения - основная переменная для чтения
            self.Encryption = True  # кодировка json ( не используется)
            self.DumpJSON = True #Формировать ли json в папке сейвов игры /game/saves/wnfh_database.json
            self.ShowDebug = True
            self.load(self.location)
            json.dump(self.BD_INIT_MODULE, open(self.location, "w+"),ensure_ascii=False,indent=4)  
            self.achievements_init()
        #def __missing__(self,key):
        #    self.display("не найдено значение "+str(key))
        def ShowErrors(self,text):
            text = text.replace("{","").replace("}","")
            ui.textbutton("{color=#E1DD7D}{b}"+text+"{/b}{/color}",background="#00000080",xmaximum=700)
        def display(self,data):
            if self.ShowDebug == True:
                self.ShowErrors(str(data))
            return 0
        def load(self, location):
            #if os.path.exists(location):
            if  self.path_enviroment in globals():
                self.open_f()
            #else:
            #    raise Exception("Объявите верное название default переменных согласно вашему пути в файле data_base")
        def load_json(self,type):
            #"""
            #возвращает выгруженный json в качестве объекта словаря
            #Возможно будет использоваться для генерации схемы
            #Type dic:
            # "cho" - Выборы
            # "ach" - Ачивки
            #"""
            try:
                if type == "cho":
                    return json.load(open(self.location,"r"))
                elif type == "ach":
                    return json.load(open(self.achivments_path,"r"))
            except Exception:
                return {}
        def open_f(self):
            #"""
            #Обновление данных из кэша
            #"""
            try:
                self.BD_INIT_MODULE =  globals()[self.path_enviroment]
            except Exception as e:
                raise Exception("Произошла ошибка при попытке загрузки данных выбора из базы \
                                - ошибка python {0} , причиной этому может быть то что переменная хранения ещё не была инициализированна: \
                                Существует ли переменная? - {1}, если переменная существует проблема скорее всего кроется в неверной формате заполнения json {3}".format(e,self.path_enviroment in globals(),str(self.BD_INIT_MODULE)))
            
            #if renpy.in_rollback():
            #    self.BD_INIT_MODULE = json.load(open(self.location,"r"))
            #    self.dumpdb() #запись в json
        def dumpSave(self):
            globals()[self.path_enviroment] = self.BD_INIT_MODULE
            #self.display("DATA CHANGED")
            #self.display(self.BD_INIT_MODULE)
            #self.dumpdb()
        """
        Запись json
        """
        def get_achievement(self,name):
            data = self.load_json("ach")
            if data[name]["Получено"] is False:
                renpy.show_screen("wnfh_get_achievement",name)
                self.set_achievement(name,data)
            else:
                self.display(str(data[name]["Получено"]))

        def achievements_clear(self):
            self.achievements_init(True)

        def set_achievement(self,name,data):
            data[name]["Получено"] = True
            self.dump_achievements(data)

        def achievements_init(self,clear = False):
            out_data = self.load_json("ach")
            in_data={}
            dic_names = ["Иконка ","Заголовок","Подпись","Трофей","Персонаж"]
            def Generate_or_update_New_Dic_from_incode_list(change_flag = True):
                for key_name in wnfh_ach_list.keys():
                    temp_dic={}
                    for index,value in enumerate(wnfh_ach_list[key_name]):
                        temp_dic[dic_names[index]] = value
                        temp_dic["Получено"] = False
                        if not change_flag and key_name in out_data.keys():
                            try:
                                temp_dic["Получено"] = out_data[str(key_name)]["Получено"]
                            except Exception:
                                temp_dic["Получено"] = False
                    in_data[key_name] =temp_dic
            if len(out_data) == 0 or clear is True:
                Generate_or_update_New_Dic_from_incode_list()
            else:
                Generate_or_update_New_Dic_from_incode_list(False)
            self.dump_achievements(in_data)

        def dump_achievements(self,data):
            try:
                json.dump(data, open(self.achivments_path, "w+"),ensure_ascii=False,indent=4)
            except TypeError:
                raise Exception(str(data.keys()))
        def dumpdb(self):
            if self.DumpJSON is True:
                try:
                    json.dump(self.BD_INIT_MODULE, open(self.location, "w+"),ensure_ascii=False,indent=4)
                    return True
                except:
                    return False
        """
        Описание:
        1) wnfh_Data.FlagSet("d8_zavtrak_s_lenoy") 
        2) wnfh_Data.FlagSet("d8_zavtrak_s_lenoy",True) 
        3) wnfh_Data.FlagSet("d8_zavtrak_s_lenoy",True, "some initiator")
        установка нового флага
        -----------------------------------
        -> Функция принимает:
            1) Название флага 
            2) Значение флага (опционально можно не указывать тогда по умолчанию TRUE)
            3) Инициатор - кто и как инициализировал флаг, если флаг установлен при выборе инициатором будет название выбора (По умолчанию None)
        -----------------------------------
        <- Возвращает: None
        """
        def FlagSet(self,key,value = True, initiator=None):
            data = {'type':'flag','value':value,'initiator':initiator}
            self.BD_INIT_MODULE[str(key)] = data
            self.display(data)
            self.dumpSave()
            self.dumpdb()
            return True
        """
        Описание:
        1) wnfh_Data.FlagDataGet("d8_zavtrak_s_lenoy")
        Получение значения и иницатора флага
        -----------------------------------
        -> функция принимает:
            1) название флага
        -----------------------------------
        <- возвращает:
            1) Значение флага
            2) Инициатор создания флага
        Пример: (True,"1d_2")
        """
        def FlagDataGet(self,key=None):
            self.open_f()
            try:
                data = self.BD_INIT_MODULE[key]['value'],self.BD_INIT_MODULE[key]['initiator']
                self.display(data)
                return data
            except KeyError:
                raise Exception("При попытке получить значение флага {0} получено исключение \
                                #- вероятно неверно прописано название флага либо его ещё не существует. Проверьте json {1}".format(key, str(self.BD_INIT_MODULE)))

        """
        Описание:
        1) wnfh_Data.FlagGet("d8_zavtrak_s_lenoy")
        функция принимает название флага и возвращает его значение
        -----------------------------------
        -> функция принимает:
            1) название флага
        -----------------------------------
        <- возвращает:
            1) Значение флага
        Пример: True
        """
        def FlagGet(self,key=None):
            self.open_f()
            try:
                data = self.BD_INIT_MODULE[key]['value']
                self.display(data)
                return data
            except KeyError:
                self.ShowErrors("При попытке получить значение флага {0} получено исключение \
                - вероятно неверно прописано название флага либо его ещё не существует. Проверьте json {1}".format(key, "\n, ".join(self.BD_INIT_MODULE.keys())))
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
        1) wnfh_Data.getChoice_result_number("1d_3")
        Возвращает номер выбранного ответа в выборе 
        -----------------------------------
        -> функция принимает:
            1) Название выбора
        -----------------------------------
        <- возвращает:
            1) Номер выбранного ответа
        Пример: 2
        """
        def getChoice_result_number(self , key=None):
            if key is None:
                self.ShowErrors("Не указан ключ - название выбора, для корректной работы метода, получения выбора")
            try:
                data = self.BD_INIT_MODULE[key]["Выбранно"]
                self.display(data)
                return data
            except KeyError:
                self.ShowErrors(u"При попытке получить номер выбранного ответа получено исключение \nМетод: getChoice_result_number(self , key=None))\n Вероятно неверно прописано название выбора либо его ещё не существует. Список имеющихся выборов:\n "+"\n, ".join(self.BD_INIT_MODULE.keys())+"\nПередан выбор:\n"+key)

            #print("Не было найдено значений" + str(key))
            except Exception as e:
                raise Exception("Непредвиденная ошибка при попытке получить номер выбранного ответа")
        """
        Описание:
        1) wnfh_Data.getChoice_result_text("1d_3")
        Возвращает текст выбранного ответа в выборе 
        -----------------------------------
        -> функция принимает:
            1) Название выбора
        -----------------------------------
        <- возвращает:
            1) Текст выбранного ответа
        Пример: "Сбежать"       
        """
        def getChoice_result_text(self , key):
            try:
                data = self.BD_INIT_MODULE[key]["Текст выбора"]
                self.display(data)
                return data
            except KeyError:
                self.ShowErrors("При попытке получить текст выбранного ответа получено исключение \nМетод: getChoice_result_text(self , key))\n Вероятно неверно прописано название выбора либо его ещё не существует. Список имеющихся выборов:\n "+"\n, ".join(self.BD_INIT_MODULE.keys())+"\nПередан выбор:\n"+key)
            except Exception as e:
                raise Exception("Непредвиденная ошибка при попытке получить текст выбранного ответа")
        """
        Описание:
        1) wnfh_Data.getChoice_text("1d_3")
        Возвращает заголовок выбора в выборе 
        -----------------------------------
        -> функция принимает:
            1) Название выбора
        -----------------------------------
        <- возвращает:
            1) Текст выбранного ответа
        Пример: "Сбежать"   
        """
        def getChoice_text(self , key):
            try:
                data = self.BD_INIT_MODULE[key]["Название выбора"]
                self.display(data)
                return data
            except KeyError:
                self.ShowErrors("При попытке получить заголовок выбранного ответа получено исключение \nМетод: getChoice_text(self , key))\n Вероятно неверно прописано название выбора либо его ещё не существует. Список имеющихся выборов:\n "+"\n, ".join(self.BD_INIT_MODULE.keys())+"\nПередан выбор:\n"+key)
            except Exception as e:
                raise Exception("Непредвиденная ошибка при попытке получить заголовок выбранного ответа")
        """
        Описание:
        1) wnfh_Data.getChoice_result_number("1d_3")
        Возвращает полученное колличество лавпойнтов персонажей в данном выборе
        -----------------------------------
        -> функция принимает:
            1) Название выбора
        -----------------------------------
        <- возвращает:
            1) Словарь персонжей выбора и их лавпойнты
            2) Влияние отсутствует
        Пример: 
            1)        
                {
                "uv":3
                "ls":-2
                }
            2) "Отсутствует влияние"
        """
        def getChoice_result_points(self , key):
            try:
                return self.BD_INIT_MODULE[key]["Влияние на персонажей"]
            except KeyError:
                self.ShowErrors("При попытке получить колличество лавпойнтов в вилке {0} получено исключение (метод getChoice_result_points(self , key))\
                                - вероятно неверно прописано название выбора либо его ещё не существует. Проверьте json {1}".format(key,"\n, ".join(self.BD_INIT_MODULE.keys())))
            except Exception as e:
                raise Exception("Непредвиденная ошибка при попытке получить заголовок выбранного ответа")
        """
        Описание:
        1) wnfh_Data.getChoice_result_points(("1d_3","uv"))
        Возвращает полученное колличество лавпойнтов харакетрные определённому персонажу в данном выборе
        -----------------------------------
        -> функция принимает:
            1) Название выбора
            1.1) Наименование персонажа
        -----------------------------------
        <- возвращает:
            1) Колличество лавпонтов персонажа в данном выборе
            2) Персонаж не найден (в данном выборе нет лавпойнтов этого персонажа)
        Пример: 
            1) 3       
            2) "Не найдено"
        """
        def getChoice_result_points(self, key, person):
            if person or key is None:
                raise Exception("укажите ключ и персонажа")
            try:
                return self.BD_INIT_MODULE[key]["Влияние на персонажей"][person]
            except KeyError:
                self.ShowErrors("При попытке получить колличество лавпойнтов в вилке {0} получено исключение (метод getChoice_result_points(self , key))\
                                - вероятно неверно прописано название выбора либо персонажа. Проверьте json {1}".format(key,"\n, ".join(self.BD_INIT_MODULE.keys())))
                #return "Не надено"
            except Exception as e:
                raise Exception("Непредвиденная ошибка при попытке получить лавпойнты персонажа {0} в выборе {1}").format(person,key)
        """
        Описание:
        1) getChoice_points_sum("uv"):
        -----------------------------------
        -> функция принимает:
            1) Наименование персонажа
        -----------------------------------
        <- возвращает:
            1) Колличество лавпонтов персонажа по всем выборам
        Пример: 
            1) 3       
        """
        def rolback_fix(self,name):
            temp_data = self.load_json("cho")
            try:
                overwrite = temp_data[name]
                self.display(str(overwrite["rollback"]))
                overwrite["rollback"] = not overwrite["rollback"]
                self.BD_INIT_MODULE[name] = overwrite
                self.dumpSave()
                self.dumpdb()
                #self.display(name)
            except Exception:
                self.display("Ещё не создано условие")
            #temp_data = globals()[self.path_enviroment]
            #if len(temp_data) > len(self.BD_INIT_MODULE):
            #    self.BD_INIT_MODULE = temp_data
            #    self.dumpSave()
        def rollback_block(self,key):
            try:
                return self.BD_INIT_MODULE[key]["rollback"]
            except Exception:
                return False
        def getChoice_points_sum(self, person):
            sum = 0
            self.open_f()
            for data in list(self.BD_INIT_MODULE):
                try:
                    if self.rollback_block(data) == False:
                        sum += int(self.BD_INIT_MODULE[data]["Влияние на персонажей"][person])
                    else:
                        self.display(str(self.rollback_block(data)))
                except KeyError:
                    #self.ShowErrors("Лавпонты персонажа "+ person +"отсутствуют")
                    pass
                except TypeError:
                    #self.ShowErrors("Передан неверный тип данных "+ str(person))
                    pass
                except Exception:
                    raise Exception('Ошибка подсчёта лавпойнтов персонажа {0} - метод (getChoice_points_sum(self, person))').format(person)
            return sum
        """
        Удаление значения из словаря, не знаю зачем но может понадобится вручную удалять выбор
        """
        def AddLove_points(self,lovepoints):
            self.BD_INIT_MODULE[BD_INIT_MODULE.keys[-1]+random.randint(100000)] = {'type':'PointsSet', "Влияние на персонажей":lovepoints}
            self.dumpSave()

        def delete(self , key):
            if not key in self.BD_INIT_MODULE:
                return False
            del self.BD_INIT_MODULE[key]
            self.dumpSave()
            return True
        """
        полное обнуление данных
        Не советую вызывать, если не хотите начинать с 0
        (обнуляет данные на этом сохранении, при загрузки точки сохранения до обнуления всё будет ок)
        """
        def resetDB(self):
            globals()[self.path_enviroment] = {}
            self.open_f()



init -998 python:
    store.mousex = 0
    store.mousey = 0
    def wnfh_add_flag(data, env,initiator):
        for i in data:
            if env == "prod":
                wnfh_Data.FlagSet(i, data[i],initiator)
            elif env == "test":
                wnfh_Data_test.FlagSet(i, data[i],initiator)


    def wnfh_find_Operand(data, env,initiator):
        if len(data[0]) == 6:
            data_set = data[0][4]
            wnfh_add_flag(data[0][5], env,initiator)
        elif len(data[0]) == 4:
            data_set = "Нет влияния"
        elif len(data[0]) == 5:
            for i in data[0][4]:
                if i in wnfh_characters.keys():
                    data_set = data[0][4]
                else:
                    wnfh_add_flag(data[0][4], env,initiator)
                    data_set = "Нет влияния"
            pass
        else:
            raise "Ебалан выбор оформлен неверно"
            sys.exit(1)
        return data_set
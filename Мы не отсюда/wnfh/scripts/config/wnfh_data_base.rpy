"""
2023 git@Deopster
"""
init -1002:
    python:
        """
        Инициализация переменных renpy default если их ещё не существует в глобальной области видимости
        Необходимо для работы rollback (перемотки диалогов назад), ибо именно переменные типа default
        renpy трекирует при перемотке. Таким образом информация по выборам кешируется в данной переменной
        в формате словаря и загружается в классе wnfh_BD при необходимости обновить данные
        """
    if "wnfh_database" not in globals():
        default wnfh_database = {}
    if "wnfh_database_test" not in globals():
        default wnfh_database_test = {}
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
        !!!! ТАМ ЖЕ УКАЗАН ПУТЬ JSON И НАЗВАНИЕ ФАЙЛА
        !!!! ВАЖНО - НАЗВАНИЕ ФАЙЛА JSON ДОЛЖНО СОВПАДАТЬ С НАИМЕНОВАНИЕМ default ПЕРЕМЕННОЙ пример строка 32
        объект используется в качестве 'указателя' области работы и хранения данных а также их разграничения между тестовой областью и продуктовой (игровой)
        """
        def __init__(self,location):
            self.location=os.path.expanduser(location) #местоположение json а также окружение prod / test
            self.path_enviroment = location.split(".")[1].split("/")[-1] #Получение название json из переменной окружения прим "./game/saves/wnfh_database.json" -> "wnfh_database"
            self.BD_INIT_MODULE = {} #инициализация словаря хранения - основная переменная для чтения
            self.Encryption = True  # кодировка json ( не используется)
            self.DumpJSON = True #Формировать ли json в папке сейвов игры /game/saves/wnfh_database.json
            self.load(self.location)
        def load(self, location):
            #if os.path.exists(location):
            if  self.path_enviroment in globals():
                self.open_f()
                #raise Exception("Объявите верное название default переменных согласно вашему пути в файле data_base")
        def load_json(self):
            #"""
            #depricated function
            #возвращает выгруженный json в качестве объекта словаря
            #Возможно будет использоваться для генерации схемы
            #"""
            return json.load(open(self.location,"r"))
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
            self.dumpdb() #запись в json
            #self.BD_INIT_MODULE = json.load(open(self.location,"r"))
        def dumpSave(self):
            globals()[self.path_enviroment] = self.BD_INIT_MODULE
            self.dumpdb()
        """
        Запись json
        """
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
            self.BD_INIT_MODULE[str(key)] = {'type':'flag','value':value,'initiator':initiator}
            self.dumpSave()
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
                return self.BD_INIT_MODULE[key]['value'],self.BD_INIT_MODULE[key]['initiator']
            except KeyError:
                raise Exception("При попытке получить значение флага {0} получено исключение \
                                - вероятно неверно прописано название флага либо его ещё не существует. Проверьте json {1}".format(key, str(self.BD_INIT_MODULE)))

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
                return self.BD_INIT_MODULE[key]['value']
            except KeyError:
                raise Exception("При попытке получить значение флага {0} получено исключение \
                - вероятно неверно прописано название флага либо его ещё не существует. Проверьте json {1}".format(key, str(self.BD_INIT_MODULE)))
        def write(self , key , value):
            self.BD_INIT_MODULE[str(key)] = value
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
                raise "Не указан ключ - название выбора, для корректной работы метода, в"
            try:
                return self.BD_INIT_MODULE[key]["Выбранно"]
            except KeyError:
                raise Exception("При попытке получить номер выбранного ответа в вилке {0} получено исключение (метод getChoice_result_number(self , key=None))\
                                - вероятно неверно прописано название выбора либо его ещё не существует. Список имеющихся выборов{1}".format(key,str(self.BD_INIT_MODULE.keys())))
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
                return self.BD_INIT_MODULE[key]["Текст выбора"]
            except KeyError:
                raise Exception("При попытке получить текст выбранного ответа в вилке {0} получено исключение (метод getChoice_result_text(self , key)) \
                                - вероятно неверно прописано название выбора либо его ещё не существует. Проверьте json {1}".format(key,str(self.BD_INIT_MODULE)))
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
                return self.BD_INIT_MODULE[key]["Название выбора"]

            except KeyError:
                raise Exception("При попытке получить заголовок выбранного ответа в вилке {0} получено исключение (метод getChoice_text(self , key))\
                                - вероятно неверно прописано название выбора либо его ещё не существует. Проверьте json {1}".format(key,str(self.BD_INIT_MODULE)))
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
                raise Exception("При попытке получить колличество лавпойнтов в вилке {0} получено исключение (метод getChoice_result_points(self , key))\
                                - вероятно неверно прописано название выбора либо его ещё не существует. Проверьте json {1}".format(key,str(self.BD_INIT_MODULE)))
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
                return "Не надено"
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
                    raise Exception('Ошибка подсчёта лавпойнтов персонажа {0} - метод (getChoice_points_sum(self, person))').format(person)
            return sum
        """
        Удаление значения из словаря, не знаю зачем но может понадобится вручную удалять выбор
        """
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



    """
    Менеджер очередей ну а точнее просто связанный список =) (не дописан / не используется)
    """
    # class StorageManager:
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
    # class SavelinkedList:
    #    def __init__(self):
    #        self.head=None
    # class Storage(object,index,memoryValue):
    #    def __init__(index,):
    #        self.head=None
    #    def __NAME_:
    #    def __EXIT__:
    #    def __ENTER__:
init -1000:
    label null_ellement:
        $ wnfh_Data = wnfh_BD("./game/saves/wnfh_database.json")
        $ wnfh_Data_test = wnfh_BD("./game/saves/wnfh_database_test.json")
    
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

init -1 python:
    def widget_lp_wnfh():
        ui.button(clicked=None, style="wnfh_menu", xpos=0.65, ypos=0.05, xanchor=1.0, xminimum=120)
        ui.text("%s: %d" % ("Катя", wnfh_Data.getChoice_points_sum("kat")), style="wnfh_lp_counter", color=wnfh_characters["kat"][1])
        ui.button(clicked=None, style="wnfh_menu", xpos=0.7, ypos=0.05, xanchor=1.0, xminimum=120)
        ui.text("%s: %d" % ("Лена", wnfh_Data.getChoice_points_sum("un")), style="wnfh_lp_counter", color=wnfh_characters["un"][1])
        ui.button(clicked=None, style="wnfh_menu", xpos=0.75, ypos=0.05, xanchor=1.0, xminimum=120)
        ui.text("%s: %d" % ("Мику", wnfh_Data.getChoice_points_sum("mi")), style="wnfh_lp_counter", color=wnfh_characters["mi"][1])
        ui.button(clicked=None, style="wnfh_menu", xpos=0.8, ypos=0.05, xanchor=1.0, xminimum=120)
        ui.text("%s: %d" % ("Алиса", wnfh_Data.getChoice_points_sum("dv")), style="wnfh_lp_counter", color=wnfh_characters["dv"][1])
        ui.button(clicked=None, style="wnfh_menu", xpos=0.85, ypos=0.05, xanchor=1.0, xminimum=120)
        ui.text("%s: %d" % ("Ульяна", wnfh_Data.getChoice_points_sum("usw")), style="wnfh_lp_counter", color=wnfh_characters["usw"][1])
        ui.button(clicked=None, style="wnfh_menu", xpos=0.9, ypos=0.05, xanchor=1.0, xminimum=120)
        ui.text("%s: %d" % ("Славя", wnfh_Data.getChoice_points_sum("sl")), style="wnfh_lp_counter", color=wnfh_characters["sl"][1])
        ui.button(clicked=None, style="wnfh_menu", xpos=0.95, ypos=0.05, xanchor=1.0, xminimum=120)
        ui.text("%s: %d" % ("Света", wnfh_Data.getChoice_points_sum("sv")), style="wnfh_lp_counter", color=wnfh_characters["sv"][1])
        ui.button(clicked=None, style="wnfh_menu", xpos=1.0, ypos=0.05, xanchor=1.0, xminimum=120)
        ui.text("%s: %d" % ("Женя", wnfh_Data.getChoice_points_sum("mz")), style="wnfh_lp_counter", color=wnfh_characters["mz"][1])
    def cords():     
        ui.button(clicked=None, style="wnfh_menu", xpos=0.93, ypos=0.10, xanchor=1.0, xminimum=120)
        ui.text("%s: %d" % ("Мыш X",store.mousex), style="wnfh_lp_counter", color=wnfh_characters["mz"][1])
        
        ui.button(clicked=None, style="wnfh_menu", xpos=1.0, ypos=0.10, xanchor=1.0, xminimum=120)
        ui.text("%s: %d" % ("Мыш Y",store.mousey), style="wnfh_lp_counter", color=wnfh_characters["mz"][1])
        
    config.overlay_functions.append(widget_lp_wnfh)
    config.overlay_functions.append(cords)

init 0 python:

    class getMousePosition(renpy.Displayable):

        def __init__(self):
            renpy.Displayable.__init__(self)

        def event(self, ev, x, y, st):
            import pygame
            import os
            if ev.type == pygame.MOUSEMOTION: 
                store.mousex = x
                store.mousey = y
                #wnfh_Data.write("xCord",store.mousex)
                #wnfh_Data.write("yCord",store.mousey)
                #renpy.redraw(renpy.current_screen(),0)
                #renpy.full_redraw()
                renpy.restart_interaction()
            #if ev.type == pygame.QUIT:
            #path = "B:/SteamLibrary/steamapps/workshop/content/331470/Мы не отсюда/wnfh/scripts"
            ##print(os.listdir(path))
            ##print(pathlib.Path(__file__))
            #wnfh_Data.write("path",os.path.realpath(__file__))
            #for i in os.listdir(path)[0:-1]:
            #    for n in os.listdir(path+"/"+i):
            #        if n.endswith(".rpyc"):
            #            pass
            #            #os.remove(path + "/" + i + "/" +n)
        def render(self, width, height, st, at):
            return renpy.Render(400, 400)

    store.mousePosition= getMousePosition()

    def checkEvent():
        ui.add(mousePosition)
    config.overlay_functions.append(checkEvent) 
    
    
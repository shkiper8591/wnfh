import os
import time
if __name__ == "__main__":
    print("Запуск")
    time.sleep(2)
    try:
        path = str(os.path.realpath(__file__)).rsplit("\\", 2)[0] + "\Мы не отсюда\wnfh\scripts"
        for i in os.listdir(path)[0:-1]:
            for n in os.listdir(path+"/"+i):
                if n.endswith(".rpyc"):
                    os.remove(path + "/" + i + "/" +n)
    except Exception as e:
        print("Ошибка "+str(e))
    print("Готово")
    time.sleep(1000)

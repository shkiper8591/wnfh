import os
import time

if __name__ == "__main__":
    print("Запуск")
    time.sleep(2)

    try:
        path = str(os.path.realpath(__file__)).rsplit("\\", 2)[0] + "\Мы не отсюда\wnfh\scripts"

        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".rpyc"):
                    os.remove(os.path.join(root, file))

    except Exception as e:
        print("Ошибка " + str(e))

    print("Готово")
    time.sleep(1000)
init python:
    #Функция для отображения времени в меню
    from random import choice

    def wnfh_get_usertime():
        from time import strftime, localtime
        time = strftime("%H:%M:%S", localtime())
        hour, min, sec = time.split(":")
        hour = int(hour)
        return str(hour) + ":" + str(min)
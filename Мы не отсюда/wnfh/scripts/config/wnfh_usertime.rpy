init python:
    #Функция для отображения времени в меню
    from random import choice

    def wnfh_get_usertime():
        from time import strftime, localtime
        time = strftime("%H:%M:%S", localtime())
        hour, mins, sec = time.split(":")
        hour = int(hour)
        if int(sec) % 2 == 0:
            return str(hour) + ":" + str(mins)
        else:
            return str(hour) + " " + str(mins)
    def update_usertime():
        global wnft_user_time
        wnft_user_time = wnfh_get_usertime()
init python:
    
    ## Генератор названий для сохранений ##
    
    # Название мода для сохранений
    wnfh_title = [u"Мы не отсюда"]
    
    def wnfh_set_savename(day):
        chapters_list = {0: [0], 1:[1, 2], 2:[3, 4, 5, 6], 3:[7, 8, 9, 10], 4:[11, 12, 13, 14], 5:["Тест"]}
        
        for n,i in enumerate(chapters_list.values()):
            if day in i:
                chapter = n+1
        global save_name
        
        if chapter == 0:
            roman_chapter = "Пролог"
        elif chapter == 1:
            roman_chapter = "I"
        elif chapter == 2:
            roman_chapter = "II"
        elif chapter == 3:
            roman_chapter = "III"
        elif chapter == 4:
            roman_chapter = "IV"
        else:
            roman_chapter = "Тестовая"
        title = wnfh_title[0] + "\n"
        if day in range(0, 16):
            save_name = title + "Глава " + str(roman_chapter) + ". " + u"День № " + str(day)
        else:
            save_name = title + day
init python:
    
    ## Генератор названий для сохранений ##
    
    # Название мода для сохранений
    blwnfh_title = [u"Мы не отсюда"]
    
    def blwnfh_set_savename(day):
        chapters_list = {1:[1, 2], 2:[3, 4, 5, 6], 3:[7, 8, 9, 10], 4:[11, 12, 13, 14]}
        
        for n,i in enumerate(chapters_list.values()):
            if day in i:
                chapter = n+1
        global save_name
        
        if chapter == 1:
            roman_chapter = "I"
        elif chapter == 2:
            roman_chapter = "II"
        elif chapter == 3:
            roman_chapter = "III"
        else:
            roman_chapter = "IV"
            
        title = blwnfh_title[0] + "\n"
        if day in range(0, 16):
            save_name = title + "Глава " + str(roman_chapter) + ". " + u"День № " + str(day)
        else:
            save_name = title + day
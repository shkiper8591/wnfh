label blwnfh_nvltest: 
   
show anim prolog_1 with Dissolve(5.0)
    $ renpy.pause(1.5, hard=True)
    $ blwnfh_set_name("kat", "???")
    $ blwnfh_set_mode(nvl)
    play music blwnfh_music_list["sharkle_dream"] fadein 5
    nvl show
    
    th "Какой чудный сон[wp] {w}Птички поют, цветочки благоухают[wp] {w}Где-то я это уже видел[wp] Вернее слышал.\nВот только где? Может в фильме? Или сериале? Быть может книге какой-то? {w}А когда я вообще в последний раз держал в руках книгу?\nКак много вопросов и ни на один из них у меня нет ответа[wp] Но ведь так хочется!{w}\nВ прочем насколько это мне нужно? Просто знакомая фраза. Может я её вообще сам придумал? Во смех-то, и ещё считаю, что она из какого-то произведения!"
    
    kat "Семён.\n"
    
    "Донеслось откуда-то из тьмы.\n"
    
    kat "Семё-о-о-он, ты тут?"
    me "Да?\n"
    
    "Раздался лёгкий смешок.\n"
    
    kat "Тогда[wp] {w}Ты пойдешь со мной?"
    
    nvl hide
    stop music fadeout 5
    scene black with dissolve2
    $ renpy.pause(2.0, hard=True)
    "Возвращаемся в меню отладки?"
    
    menu: 
    
        "Да":
            jump blwnfh_test_main_menu 
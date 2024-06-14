label d8_kat_mi_musclub:
	
    stop music fadeout 5.0
    stop ambience fadeout 2.0
    scene bg ext_admin_day_wnfh with santa_barbara_in_blure_dissolve2
    play ambience ambience_camp_center_day fadein 2.0
    $ renpy.pause(0.5)
    scene bg ext_musclub_day with slide_left_blure_dissolve2
    $ renpy.pause(0.5)
    scene bg ext_musclub_verandah_day_wnfh
    show kat normal pioneer at center
    with sphere_blure_dissolve2
    play music music_list["memories_piano_outdoors"] fadein 5.0
    $ renpy.notify("МУЗЫКА МАКСИМАЛЬНО УСЛОВНАЯ, ТУТ НУЖНА БУДЕТ ДРУГАЯ, БОЛЕЕ ВЕСЁЛАЯ!")
    $ renpy.pause(0.5)
    window show dissolve

    "Подойдя к музклубу, мы услышали доносящуюся оттуда музыку."

    me "Похоже, Мику коротает время в ожидании тебя."
    kat "А она красиво играет."
    me "Ну, в конце-концов она полжизни посвятила музыке."

    show kat confused pioneer at center with dspr

    kat "Серьёзно?"
    me "По крайней мере она сама так говорит."

    show kat normal pioneer at center with dspr

    kat "Надо же[wp]"

    window hide dissolve
    stop music fadeout 5.0
    stop ambience fadeout 2.0
    scene bg int_musclub_day
    show kat smile pioneer close at left
    show mi normal pioneer at right
    with slide_right_blure_dissolve2
    play ambience ambience_music_club_day fadein 2.0
    play music music_list["so_good_to_be_careless"] fadein 5.0
    $ renpy.notify("Надо бы другую музыку для музклуба в общем и Мику в частности, а то со гуд ту би керлесс заебала. Желательно собственного производства.")
    $ renpy.pause(0.3)
    window show dissolve

    "Когда мы вошли внутрь, Мику прекратила игру на пианино и перевела свой взгляд на нас."

    mi "Ухты, даже вдвоём пришли, неожиданно-неожиданно, а я уже думала, что про меня позабыли."
    me "Дела у нас были."

    show mi grin pioneer at right with dspr

    mi "А я знаю, что у вас дела были."

    "Мы с Катей переглянулись."

    kat "Кто-то рассказал?"

    show mi smile pioneer at right with dspr

    "Мику захихикала и махнула в сторону окна."

    mi "У меня же большое окно, вас не трудно было заметить несущих какие-то коробки."

    show mi surprise pioneer at right with dspr

    mi "Кстати, что это были за коробки? А то я тут всю голову уже сломала размышляя над этим, прям покая мне не даёт."

    show kat smile pioneer close at left with dspr

    "Катя усмехнулась."

    kat "Боюсь тебя разачаровывать, но там были лагерные документы."

    show mi upset pioneer at right with dspr

    mi "Ну, в общем-то я так и примерно думала."

    show mi grin pioneer at right with dspr

    mi "Хотя в душе я надеялась, что вы несёте какие-нибудь вкусняшки для праздновства."
    mi "Правда, я прекрасно понимала, что вряд ли этот день празднуют у вас."

    "Я на секунду призадумался."
    "Мне не совсем было понятно, о каком празднике вообще может идти речь."

    show kat confused pioneer close at left with dspr

    kat "А что за праздник?"

    th "Похоже, я не один такой."

    show mi serious pioneer at right with dspr

    mi "Завтра ровно двадцать лет, как закончилась оккупация американцев над Японией."
    mi "И в тот же день Япония стала членом советского блока. {w=0.5}Для нас, японцев, это во истину великий день."
    
    show kat normal pioneer close at left with dspr

    kat "Хороший день."
    mi "Очень[wp]"

    "Я попытался переварить только что услышанную информацию."

    th "Япония член соц блока? Да и разве оккупация не закончилась в пятидесятые?"

    "В моей голове возник конфликт историй."
    "И, видимо, из-за этого конфликта, у меня знатно так разболелась голова."

    th "Вот же зараза, как невовремя-то!"

    "Боль была адская, но я постарался сдерживать себя, а также как можно скорее переключить свои мысли на что-нибудь другое."
    "Вот только, меня полностью поглотила эта мысль. Боль стала усиливаться и в один момент я не выдержал и упал на пол."

    $ renpy.notify("Мб сделать тут какую-нибудь анимацию падения, хз")
    play sound sfx_body_bump
    window hide
    show blink
    with None
    stop music fadeout 5.0
    scene black
    $ renpy.pause(0.3, hard=True)
    window show

    "Спустя какое-то время я очнулся."
    "Помещение наполнял шум, похоже, греющегося чайника, а вокруг меня постоянно ходили люди."
    "Ещё, по ощущениям, я лежал на какой-то мягкой подстилке и подушке."

    th "Надо же, они смогли поднять мою тяжелую тушу и перенести[wp]"

    "Вскоре, ходьба утихла, а моего лба коснулась девичья рука."

    mi "Огненный[wp]"
    kat "Эй, Семён, ты это, давай не болей!"
    mi "Что же это его так скосило? Да и ещё так резко[wp]"

    "Хоть и со слов Мику у меня лоб был горячий, я ощущал себя совершенно нормально."

    scene bg int_musclub_day
    show mi shy pioneer close at right
    show kat smile pioneer close at left
    show unblink
    with None

    me "Доброе утро, я полагаю."
    
    "Я попытался встать, но меня остановили Мику и Катя."

    show kat normal pioneer close at left
    show mi upset pioneer close at right
    with dspr

    kat "Тебе сейчас нужен покой."
    mi "Да, упасть так просто, ничего хорошего не значит."

    show mi serious pioneer close at right with dspr

    mi "Быть может ты на солнце перегрелся, весь день же ходишь туда обратно по делам."
    me "Может быть[wp] Но я не чувствую себя больным."

    show kat normal pioneer at left
    show mi serious pioneer at right
    with dspr

    "Немного приложив усилий, я всё же смог побороть девушек и встать."
    "Девушки же остались сидеть на подстилке, а вернее, пледе на котором я и лежал."
    "В это время раздался щелчок."

    show mi smile pioneer at right with dspr

    mi "О, кажется чайник вскипел!"

    show mi normal pioneer far at right with dspr

    "Мику отбежала в дальний угол помещения."

    me "У тебя тут даже чайник есть?"

    show kat happy pioneer at left with dspr

    kat "Представляешь? У неё тут все удобства."
    kat "Чайник, кулер с водой, чашки, собственно, чаи самых разных сортов и всякие иностранные сладости."
    me "Интересно, что за сладости такие."

    show mi normal pioneer at right with dspr

    "Вскоре, Мику возвратилась вместе с двумя чашками из которых исходил приятный аромат."
    "Она раздала чашки мне и Кате, а также дала по паре конфет."
    "После чего, она села рядом с нами."

    show kat confused pioneer at left with dspr

    kat "А ты чего без чая?"
    mi "Я недавно только пила чай, поэтому пока-что не хочу ещё."

    show kat normal pioneer at left with dspr

    kat "Жаль[wp]"

    "Тем временем я разглядывал, что же за конфету мне всунула Мику."
    "Вот только, иероглифы на ней отказывались мне что-то объяснять."

    me "А-э, Мику, можешь сказать, что это за конфета такая?"

    show mi smile pioneer at right with dspr

    mi "О, это одни из моих любимых."
    me "Хорошо[wp] А на вкус как они?"

    show mi grin pioneer at right with dspr

    mi "А ты открой и попробуй! Можешь не переживать, они вкусные и сладкие."

    "Я скептически посмотрел на Мику."

    th "Ну, травить меня точно не будут, так что[wp] Ай, чем чёрт не шутит!"

    "Открыв фантик, внутри оказалась обычная с виду шоколадная конфета."
    "Я её тут же целиком закинул в рот."
    "И Мику действительно не обманула. Вкус конфеты не поддавался описанию, но если коротко говоря: она была чертовски вкусной."

    mi "Ну, как оно?"
    me "Хорошие у вас сладости делают в Японии."

    show mi happy pioneer at right with dspr

    mi "Вот, а ты боялся."

    show mi normal pioneer at right
    show kat smile pioneer at left
    with dspr
    $ renpy.notify("Тут надобно вставить таймскип")
    window hide dissolve
    $ renpy.pause(0.3)
    window show dissolve

    "Так мы «чаёвничали» на протяжении минут десяти или пятнадцати."
    "Мику подливала нам чай и угощала сладостями, а также рассказывала всякие интересности."
    "Ну, интересно это было Кате. Меня же как-то особо не интересовали устройство гитарных струн, или какой там состав в японском шампуне."
    "А посему, я просто сидел и пил чай, раздумывая о всяком."
    "И под всяком, я подразумеваю о смысле моего пребывания здесь."

    th "Уже который раз я задумываюсь, что если, я просто уйду[wp] Будут ли меня искать?"
    th "Или может просто ликвидируют как только я перейду за условную черту?"

    if wnfh_Data.getChoice_result_number("d8_choice_n6") == 1:

        th "Тем более, после того, как мы с Алисой видели тех ребят в РХБЗ[wp]"
        
        if wnfh_Data.getChoice_result_number("d8_choice_n8") == 1:

            th "И тем более, после того, как стало ясно, что это военные ребята[wp]"

    th "Да и даже если ничего со мной не будет, куда я пойду-то?"
    th "Получается только и остаётся мне надеятся на чудо[wp]"

    kat "[wp]Семён, вот скажи, что сложнее: кроссворды или путаницы для детей?"

    "Несколько секунд с серьёзным лицом я думал над этим вопросом, пока не задумался над его абсурдностью."

    me "Чё?"

    show kat laugh pioneer at left
    show mi laugh pioneer at right
    with dspr

    "На этом, повествование, пока-что, обрывается."
    "Дальнейший клик отправит вас в главное меню игры."
    "Я вас предупредил."
label d7_me_meet_kat_w_dw_n_usw:

    window hide dissolve
    $ wnfh_set_time()
    stop ambience fadeout 3.0
    scene bg ext_dining_hall_near_day
    show dv normal pioneer at right
    show usw normalsmile pioneer at left 
    $ wnfh_Data.FlagSet("d7_kat_oblivanie", "me_oblil")
    with dissolve2
    play ambience ambience_camp_center_day fadein 3.0
    #play music music_list["timid_girl"] fadein 3.5
    $ renpy.pause(1)
    show bg ext_dining_hall_away_day with dissolve2 
    $ renpy.pause(1)
    show bg ext_lenin_square_day_wnfh with dissolve2
    window show dissolve

    "Выйдя на площадь, Ульяна остановилась."

    usw "Так, в общем, вы идите, я вас догоню. Если что, задержите новобранцев."
    me "А ты куда собралась?"

    show usw grin pioneer at left with dspr

    usw "У тебя память как у золотой рыбки? За ведром же!"
    me "Вообще про плохую память рыбок — это миф[wp]"

    show usw dontlike pioneer at left
    show dv laugh pioneer at right
    with dspr

    "Ульяна от моего потока мысли моментально начала злиться."
    "Алиса же положила руку мне на плечо."

    dv "Давай, эрудированный ты наш, пойдём, нам ещё засаду готовить!"
    usw "Да, там и блеснёшь умом!"

    show dv smile pioneer at right with dspr

    "Ульянка посмеялась на пару с Алисой, и мы пошли к остановке."

    window hide dissolve
    scene bg ext_clubs_day
    show dv normal pioneer at center
    with slide_up_blure_dissolve2
    stop music fadeout 5.0
    $ renpy.pause(0.2)
    window show dissolve

    "Выйдя к воротам, мы поняли, что те ещё закрыты. Но за ними уже слышалось гудение двигателя автобуса."

    th "Приехали уже[wp] Значит, времени на подготовку засады немного[wp] {w=1}Надеюсь, Ульяна быстро придёт."
    
    me "Так, где мне лучше всего встать?"
    
    "Алиса бегло оглядела вход в лагерь."
    
    dv "Там, под деревом. Лезь туда."
    
    "Она указала на место, о котором говорила."
    "Местечко действительно было неплохим[wp] {w}Для игры в прятки или типа того."
    "Кусты там очень уж разрослись. В случае чего быстро сбежать из засады не получится."
    
    me "Ты шутишь?"
    dv "Я абсолютно серьёзно."
    me "Я туда не полезу!"
    
    # H606 изменить ручку Алисы, сделать больше под ее кожу.
    
    "Цыкнув и закатив глаза, Алиса выставила перед собой кулак."

    window hide dissolve
    show bg ext_clubs_day behind dv:
        subpixel True
        ease 1.5 zoom 1.2
    $ renpy.pause(1.5)
    show bg ext_clubs_day:
        subpixel True
        zoom 1.2
        blur 30
    show dv normal pioneer:
        subpixel True
        blur 30
    with dissolve
    show black_curtain_knb_down:
        subpixel True
        ypos 1.0
        ease 1.5 ypos 0.85
    show black_curtain_knb_down as black_curtain_knb_up:
        subpixel True
        ypos -1.0
        ease 1.5 ypos -0.85
    $ renpy.pause(1.5)
    show hand_dv_stone:
        subpixel True
        align (0.5,0.5)
        pos (0, 1)
        zoom 0.55
        rotate 45
        ease 0.7 rotate 0 pos (0.2,0.7)
    $ renpy.pause(0.5)
    window show dissolve

    dv "Давай на цу-е-фа."

    th "Никогда не любил такой способ определения, кто будет водить в салках, или искать в прятках."
    th "Но деваться мне некуда, я не хочу лезть в эти кусты."

    me "Ладно, давай, до скольки играем?"
    dv "Ты с дубу рухнул? У нас времени мало, так что один раз."

    "Грустно вздохнув, мы занесли свои кулаки и под отсчёт «цу-е-фа», остановились."

    window hide dissolve
    show hand_me_stone:
        subpixel True
        align (0.5,0.5)
        pos (1, 1)
        zoom 0.65
        rotate -45
        ease 0.7 rotate 0 pos (0.75,0.7)
    play sound wnfh_sfx_list["wave_of_the_hand_knb_game"]
    $ renpy.pause(0.25)
    show knb_game_text_1 with dspr
    show hand_dv_stone:
        subpixel True
        align (0.5, 0.5)
        pos (0.2, 0.7)
        zoom 0.55
        rotate 0
        ease 0.15 rotate -20 pos (0.15, 0.5)
        ease 0.15 rotate 5 pos (0.18, 0.71)
        ease 0.15 rotate -20 pos (0.15, 0.5)
        ease 0.15 rotate 5 pos (0.18, 0.71)
        ease 0.15 rotate -20 pos (0.15, 0.5)
        ease 0.15 rotate 5 pos (0.18, 0.71)
    show hand_me_stone:
        subpixel True
        align (0.5,0.5)
        pos (0.75, 0.7)
        zoom 0.65
        rotate 0
        ease 0.15 rotate 20 pos (0.8, 0.5)
        ease 0.15 rotate -5 pos (0.73, 0.71)
        ease 0.15 rotate 20 pos (0.8, 0.5)
        ease 0.15 rotate -5 pos (0.72, 0.71)
        ease 0.15 rotate 20 pos (0.8, 0.5)
        ease 0.15 rotate -5 pos (0.73, 0.71)
    $ renpy.pause(0.25)
    show knb_game_text_2 with dspr
    $ renpy.pause(0.2)
    hide hand_dv_stone
    show hand_dv_paper:
        subpixel True
        align (0.5, 0.5)
        pos (0.18, 0.71)
        zoom 0.55
        rotate 5
        ease 0.3 rotate 0 pos (0.2, 0.7)
    show  hand_me_stone:
        subpixel True
        align (0.5, 0.5)
        pos (0.73, 0.71)
        zoom 0.65
        rotate -5
        ease 0.3 rotate 0 pos (0.75, 0.7)
    show knb_game_text_3 with dspr
    $ renpy.pause(0.25)
    hide knb_game_text_1
    hide knb_game_text_2
    hide knb_game_text_3
    with dspr
    window show dissolve

    "Я показывал «камень», а Алиса «бумагу». Я проиграл."

    window hide dissolve
    show hand_dv_paper:
        subpixel True
        align (0.5, 0.5)
        pos (0.2, 0.7)
        zoom 0.55
        rotate 0
        ease 1.0 rotate 45 pos (0.0, 1.2)
    show  hand_me_stone:
        subpixel True
        align (0.5, 0.5)
        pos (0.75, 0.7)
        zoom 0.65
        rotate 0
        ease 1.0 rotate -45 pos (1.0, 1.2)
    show black_curtain_knb_down with dspr:
        subpixel True
        ypos 0.85
        ease 1.5 ypos 1.0
    show black_curtain_knb_up with dspr:
        subpixel True
        ypos -0.85
        ease 1.5 ypos -1.0
    show bg ext_clubs_day:
        subpixel True
        zoom 1.2
        blur 0
    show dv normal pioneer:
        subpixel True
        blur 0
    with dissolve
    show bg ext_clubs_day with dspr:
        subpixel True
        ease 2.0 zoom 1.0
    $ renpy.pause(2.0)
    show dv normal pioneer at center with dissolve
    window show dissolve

    dv "Лезь давай, заодно, будешь и обливать."
    me "Так, погоди-ка, это уже лишнее."

    show dv angry pioneer with dspr

    dv "Залезай под чёртово дерево и не задавай вопросов, времени мало!"
    
    $ wnfh_set_name("kat", "Голос")
    
    kat "Ау? Есть тут кто?"

    "За воротами послышался чей-то голос."

    show dv smile pioneer with dspr

    dv "Так, давай-ка мы тебе поможем."
    
    "Тихо сказала Алиса и резко толкнула меня под дерево."
    "И, на удивление, я никак не поранился о ветки. Да и за кустами оказалось много свободного места."
    "Я поднялся и выглянул наружу."

    show usw smile pioneer at right
    show dv smile pioneer at left
    with dissolve

    "В это же время подбежала Ульяна с полным ведром воды."
    
    usw "Где наш герой?"
        
    show usw grin pioneer close at right with dspr

    "Алиса указала на меня, и, подойдя ко мне, Ульяна протянула ведро."

    usw "Держи, Семён, предоставляю эту честь тебе."
    me "Слушайте, я думал меня здесь ждёт горячий окорок[wp]{nw=2.5}"
    kat "Здесь есть кто-нибудь?"
    
    "Вновь донеслось из-за ворот."

    show usw dontlike pioneer close at right with dspr
    
    usw "Кончай вертеться и бери. Ты же согласился на эту авантюру, а значит должен был быть готов ко всему!"
    me "Я просто не уверен[wp]"
    
    "За воротами послышались приближающиеся шаги."

    show usw angry pioneer close at right with dspr
    
    usw "Я сейчас тебя самого оболью!"
    
    "Она занесла ведро для атаки."
    
    me "Ладно-ладно, давай сюда."
    
    show usw calml pioneer close at right with dspr

    usw "Так бы сразу."

    "Я взял ведро и притаился."

    show dv normal pioneer far at cright
    show usw normal pioneer far at fright
    with dissolve

    "Рыжие же отошли подальше в сторону."
    "И как только из-за приоткрывшихся ворот показался силуэт, я сразу же вылил на него всё содержимое ведра."

    $ wnfh_set_name("kat", "Новенькая")

    show kat scared casual shirt at left with dissolve

    "Неожиданно для себя я заметил, что жертвой оказалась девушка."
    
    hide dv
    hide usw
    with dissolve

    th "Ой-ой[wp] Пора сваливать."
    
    "Мои рыжие подруги уже сверкали пятками, и я собирался присоединится к ним."
    "Я резво выпрыгнул из кустов, кое-как встал на ноги и только собирался побежать, как врезался в своего товарища — Шурика."

    show sh serious at right with dissolve

    "Шурик смотрел на меня недовольным взглядом."
    
    sh "Семён, вот что-что, а такого я от тебя не ожидал. Взял и окатил девушку из ведра!"
    sh "Это неподобающее поведение не только для пионера, но и для советского гражданина!"
    
    "Начал говорить он занудным голосом."
    
    th "Вот блять, нотаций от Шурика мне ещё не хватало[wp]"
    #Фильтр
    
    sh "Тем более, как я понимаю, это новенькая у нас, а ты своим поступком портишь ей впечатление о лагере и местном контингенте."
    sh "А это повлияет на репутацию лагеря! Она же теперь точно понесёт весть о том, что тут людей из ведра обливают на входе."
    
    th "Пристрелите меня уже."
    
    sh "Из-за этого запустят проверку, мол, почему это происходит, во всём обвинят нашу замечательную вожатую. В том, что она не следит за своими пионерами и их воспитанием."
    sh "Короче говоря[wp]"
    
    "Он взял меня за плечи и развернул лицом к новенькой, которая всё ещё стояла в шоке и пыталась хоть как-то избавится от влаги."

    show sh normal at right with dspr
    
    sh "Иди и извинись перед ней. {w}Искренне."
    
    th "Ох, знал я, что не стоит на это подписываться."

    window hide dissolve
    call screen wnfh_choice(
        ["kat", "Стоит извиниться", "Я же не знал, что там будет она", "d7_sh_yes_1", {"kat":1}],
        ["neutral", "Меня подставили", "Пусть Алиса с Ульяной извиняются", "d7_sh_no_1", {"kat":-2}],
        ["d7_choice_n9", "Шурик требует Семёна извнится перед Катей"]
        ) with sphere_blure_dissolve2

label d7_sh_yes_1:

    window show dissolve

    me "Хорошо, сейчас."

    "Шурик отпустил меня и легонько толкнул к девушке."
    "Я аккуратно подошёл."
    
    me "Слушай[wp] Прости, пожалуйста, что так вышло. Мы[wp] Я[wp] Хотел мимо вылить, чтобы подшутить, но что вышло, то вышло."
    
    "Извинение моё было ужасным, но оно смогло хоть немного успокоить девушку."
    
    show kat sad casual shirt at left with dspr

    kat "Вот как[wp]"
    me "Ну ладно, раз я тут в провинившихся перед тобой, пойдём хотя бы проведу тебя к складу, где тебе выдадут сухую форму."
    kat "Д-Да, было бы неплохо[wp]"
    
    hide sh with dissolve

    "Я быстренько оглянулся в сторону Шурика, который одобрительно мне кивнул и ушёл."
    
    me "Ну, пойдём тогда."
    
    "Вместе мы зашагали вглубь лагеря."

    jump d7_me_meet_kat_alt

label d7_sh_no_1:

    $ wnfh_Data.FlagSet("me_neznayu_imya_kat", True)

    window show dissolve

    me "Слушай, меня Алиса с Ульяной знатно так подставили, пусть они извиняются!"

    show sh surprise at right with dspr

    sh "Но облил-то её ты. Это тоже накладывает ответственность."
    me "Меня заставили это сделать под угрозами быть облитым вместо неё!"

    show sh normal at right with dspr

    sh "Понятно[wp]"

    show sh serious at right with dspr

    sh "Ну, иди тогда, ищи этих рыжих и заставь их извиниться перед новенькой, а я пока проведу её к складу."
    
    th "Так, а вот этого мне не надо! Меня же потом вожатая с потрохами сожрёт!"
    
    me "Слушай, мне вожатая велела сопроводить пополнение, и если попытаюсь свалить на кого-нибудь, мне такое устроят[wp]"

    show sv angry pioneer glasses tablet at center with dissolve
    
    "В это же время сюда пришла главная помощница нашей вожатой — Светлана. Она же Планшетик."
    
    sv "Так, что здесь творится?"

    show sv happy pioneer glasses tablet at center with dspr

    sv "О, я так понимаю, это и есть наше пополнение."
    #КОСЯК: в альтернативном варианте ей никто ничего не говорил о прибытии новичков, и она ничего не знала. А тут почему-то знает.
    
    "Сказала она, указав рукой на новенькую."
    
    show sv angry pioneer glasses tablet at center with dspr

    sv "И почему она вся мокрая?"
    
    "Мы с Шуриком переглянулись."
    
    sh "Алиса с Ульяной постарались."
    sv "Ясно."
    sv "Значит так, Семён."
    
    "Грозно сказала она и бросила свой тяжелый взгляд на меня."
    
    sv "Поскольку ты не справился со своей задачей сопроводить новоприбывшую в целостности и сохранности[wp]"
    sv "Сопровождение переходит под мою юрисдикцию, а тебя за плохое выполнение работы будет ждать наказание от вожатой, понял?"
    me "Понял."

    show sv happy pioneer glasses tablet at center with dspr

    sv "Отлично."
    # me "Ля ты крыса..."
    
    show sv happy pioneer glasses tablet:
        ease 0.8 xcenter 0.4
    $ renpy.pause(1.0)
    show sv happy pioneer glasses tablet:
        ease 1.0 xcenter -0.2
    show kat sad casual shirt:
        ease 1.0 xcenter -0.2

    "Она отошла к новенькой, что-то сказала ей и повела за собой."

    sh "Да уж, Семён, не завидую я твоему положению."
    me "И не говори[wp]"

    show sh laugh at right with dspr

    sh "Ну, зато ты спас наш клуб от визита Светы!"
    
    "Задорным голосом проговорил Шурик."
    
    show sh normal_smile at right with dspr

    sh "Пойдём к нам тогда, у меня как раз есть работёнка для тебя."
    
    th "Вот холера[wp] Не одно, так другое!"

    jump d7_male_clubs
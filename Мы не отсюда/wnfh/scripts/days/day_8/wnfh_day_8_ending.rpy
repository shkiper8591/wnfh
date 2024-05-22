label d8_ending:
    $ wnfh_set_time("night")
    scene bg ext_lenin_square_night_wnfh with santa_barbara_in_blure_dissolve2
    play ambience ambience_camp_center_night fadein 3.5
    window show dissolve

    if wnfh_Data.getChoice_result_number("d8_choice_n9") == 1:

        "Поужинав в гордом одиночестве, я пришёл на площадь, где присел отдохнуть. А там и пришла ночь."

    else:

        "Поужинав в компании Кати, мы попрощались на площади. Она пошла к себе домой, а я же присел отдохнуть на лавочке, где и встретил ночь[wp]"

    th "Люблю ночь. Людей почти нет, тихо, разве что сверчки только трещат[wp] Или сверщат? Какие они вообще издают звуки?"

    "Расположившись поудобнее на лавочке, я запрокинул голову наверх, в надежде посмотреть на звёздное небо."

    show dv smile pioneer close at center with dissolve

    "Но я увидел над собой Алису с хитрой улыбкой."

    dv "Эх, не получилось напугать."
    me "И тебе привет."

    "Ловким движением, Алиса перепрыгнула спинку лавки и села рядом со мной."

    dv "Ну здравствуй, пионер!"
    me "Чего тебе на ночь глядя?"

    show dv normal pioneer close at center with dspr

    dv "Диалог вчерашний помнишь?"
    me "Какой из?"

    "Алиса громко цокнула и закатила глаза."

    show dv angry pioneer close at center with dspr

    dv "На сцене вечером."
    me "Честно, смутно."

    show dv rage pioneer close at center with dspr

    dv "Семён, я тебя сейчас задушу."

    "Я посмотрел на мою подругу."
    "Её взгляд был хладнокровен и убийственен, так что сложно было сомневаться в её словах."

    th "Твою же дивизию, видимо придётся напрячь память."

    dv "Даю тебе пять секунд на вспоминание."
    me "Погоди, этого мало!"
    dv "Раз!"

    th "Так, давай думать Семён, диалог[wp] Диалог это когда разговаривают[wp]"

    dv "Два!"

    th "Я вчера пришёл на сцену, чтобы отдохнуть от всех и подумать о своём, потом[wp]"

    dv "Три!"

    th "Потом пришла Алиса, мы о чём-то поговорили и я ушёл[wp] О чём мы говорили[wp]"

    dv "Четыре!"

    th "Говорили о всяком, но чем всё закончилось[wp] {w=0.5}Точно!"

    "Когда Алиса уже готовилась сказать заветное «пять», я перебил её."

    me "Ты про посиделки под гитарку?"

    show dv laugh pioneer close at center with dspr

    dv "В точку!"
    me "А ты бы действительно меня придушила, если я не ответил?"

    show dv grin pioneer close at center with dspr

    dv "Кто знает[wp] {w=0.5}Ну так что, пошли?"

    window hide dissolve
    call screen wnfh_choice(
        ["dv", "Пошли", "Е-е-е рок!", "d8_me_dv_agree", {"dv":1}],
        ["neutral", "Я устал", "Я ухожу спать", "d8_me_dv_disagree", {"dv":-1}],
        ["d8_choice_n10", "Д8.Алиса зовёт Семёна поиграть на гитарах"]
        ) with sphere_blure_dissolve2

label d8_me_dv_agree:

    window show dissolve

    me "Ладно, убедила, пойдём вдарим року в этой дыре."

    show dv smile pioneer close at center with dspr

    dv "Ой-ой, какие мы бунтари, сразу за рок."
    me "А что?"
    dv "Ничего, идём уже, а то времени мало."

    jump d8_dv_ending

label d8_me_dv_disagree:

    window show dissolve

    me "Пожалуй откажусь, а то я что-то устал за сегодня[wp]"

    show dv normal pioneer close at center with dspr

    "Алиса глубоко вздохнула."

    dv "Вот оно что[wp]"

    show dv rage pioneer close at center with dspr

    dv "Значит я задушу тебя!"

    "Алиса уже занесла руки для нападения, как между нами появилась книжка."

    un "Не надо человека душить."

    show un normal pioneer close at left with dissolve
    show dv angry pioneer close at right with dspr

    dv "А он заслужил!"

    show un shy pioneer at left with dspr

    un "Чем же человек заслужил столь ужасную участь как удушение?"
    un "Это же совсем не гуманно, причинять столько боли[wp]"

    "Алиса злобно фыркнула."

    show dv normal pioneer close at right with dspr

    dv "Вот зануда, всю тему обломает."
    dv "Ладно, раз уж друзей душить запрещают, пойду поиграю на гитаре в гордом одиночестве."
    me "Хорошей игры."
    dv "Ага, спасибо."

    hide dv with dissolve

    "Резко встав, Алиса быстрым шагом ушла куда-то в сторону эстрады."
    "Я же облегчённо выдохнул."

    jump d8_un_ending
init:
    $ mods["live2dtest"] = "Интеграция Liev2D"

    # Путь до спрайта может быть любым, главное, чтобы шёл до корневой папки спрайта
    image Epsilon = Live2D("live2d/images/Epsilon", base=.8, loop=True)
    image Hiyori = Live2D("live2d/images/Hiyori", base=.6, loop=True)
    image Hibiki = Live2D("live2d/images/Hibiki", base=.6, loop=True)

    $ _live2d_fade = True # Для плавного перехода между анимациями вместо резкого окончания анимации. Опционально.
label live2dtest:
    ".."

    show Epsilon idle_01 at left with dissolve

    "Epsilon!"

    show Hiyori m01 at right with dissolve

    "Hiyori!"

    show Hibiki 01 at center with dissolve

    "Hibiki!"

    show Epsilon m_sp_01

    "Epsilon движение - m_sp_01"

    show Hibiki 05

    "Hibiki движение - 05"

    show Hiyori m10

    "Hiyori движение - m10"

    show Epsilon still
    show Hiyori still
    show Hibiki still

    "Сброс движений и полная остановка с помощью атрибута 'still'."

    show Epsilon idle_01
    show Hiyori m01
    show Hibiki 01

    "Сброс движений, восстановление дефолтных анимок."

    show Epsilon angry

    "Epsilon эмоция - Angry"

    show Hibiki angry

    "Hibiki эмоция - Angry"
    "У Hiyori нет эмоций."
    "Название движений — в папке 'motions'."
    "Пример: название файла 'Hiyori_m01.motion3.json', название движения - 'm01'."
    "Название эмоций — в папке 'expressions'."
    "Вне зависимости от названия, эмоции должны писаться строчными буквами."
    "Также можно прописывать свои имена названиям эмоций и движений через атрибут alias."
    "Подробнее о работе с Live2D {a=https://www.renpy.org/doc/html/live2d.html}здесь{/a}."
    return

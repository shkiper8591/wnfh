label d7_me_v_medpunkte:

    window hide dissolve
    stop ambience fadeout 2.5
    scene bg int_aidpost_day with sphere_blure_dissolve2
    play ambience ambience_medstation_inside_day fadein 2.5
    $ renpy.pause(1.0)
    window show dissolve

    "Уже через несколько минут я был на месте."
    "Постучавшись, я вошёл."

    me "Здраствуйте, Виола. Это я, Семён."

    "Медсестра что-то записала в свой журнал, а после повернулась ко мне."

    show cs normal at center with dissolve

    cs "Что, плохо себя чувствуешь, пионер?"

    if wnfh_Data.getChoice_result_number("d7_choice_n1") == 1:

        cs "Или ты опять упал?"

    me "Нет, у меня просто голова разболелась, вот и всё."
    me "У вас есть что-нибудь от головной боли?"
    cs "Есть ли у меня что-нибудь от головной боли[wp]"

    "Задумчиво произнесла медсестра и, открыв ящик стола, стала копаться в нём."
    "И через пару секунд достала оттуда небольшую стеклянную банку."

    cs "Вот, иди сюда."

    "Я подошёл к Виоле, после чего она протянула мне таблетку и стакан."

    cs "Воды там налить можешь."

    "Сказала она и указала на умывальник позади меня."

    me "Ага, понял."

    "Налив прохладной воды, я запил ей таблетку, после чего вернул стакан."

    me "Спасибо вам огромное."
    cs "Если это всё, то попрошу покинуть помещение. Отвлекаешь от работы."
    me "Всё, тогда до свидания."
    cs "До свидания."

    "Я быстро покинул медпункт."

    window hide dissolve
    stop ambience fadeout 2.5
    scene bg ext_aidpost_day with dissolve2
    play ambience ambience_camp_center_day fadein 2.5
    window show dissolve

    th "Ух, ну всё, теперь можно не бояться подохнуть от боли."
    th "А значит, пора идти домой, отдыхать."

    jump d7_me_doma
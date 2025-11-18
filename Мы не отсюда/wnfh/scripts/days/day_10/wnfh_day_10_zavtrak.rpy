label d10_zavtrak_raspredelitelnya_shlyapa_hogwartsa:

    if wnfh_Data.FlagGet("journalist") == True:

        "Плэйсхолдер"

        jump d10_zavtrak_w_kat

    else:

        jump d10_zavtrak_w_males

label d10_zavtrak_w_un:

    if wnfh_Data.FlagGet("me_stukach") == True:

        jump d10_zavtrak_w_un_2

    else:

        jump d10_zavtrak_w_un_1

label d10_zavtrak_w_un_1:

    "placeholder"

label d10_zavtrak_w_un_2:

    "placeholder"

label d10_zavtrak_w_dv:

    "placeholder"

label d10_zavtrak_w_males:

    "placeholder"

label d10_zavtrak_w_kat:

    "placeholder"

label d10_zavtrak_w_dv_n_mi:

    "placeholder"

label d10_zavtrak_w_mi:

    "placeholder"
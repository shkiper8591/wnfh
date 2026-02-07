screen wnfh_time_skip(timeskip, timeskip_size = 30, timeskip_transition = dissolve):
    add "black"
    frame:
        background debug_frame["red"]
        area(0.5, 0.5, 1500, 400)
        xanchor 0.5 yanchor 0.5
        text timeskip:
            style "wnfh_text_" + renpy.store.wnfh_tymeofday
            size timeskip_size

    timer 5 action Hide("wnfh_time_skip", transition = timeskip_transition)
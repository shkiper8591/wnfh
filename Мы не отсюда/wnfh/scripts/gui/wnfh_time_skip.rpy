screen wnfh_time_skip(ts, ts_size = 30, ts_transition = dissolve, ts_text_spd = False, ts_timer = 5):
    add "black"
    frame:
        background debug_frame["red"]
        area(0.5, 0.5, 1500, 400)
        xanchor 0.5 yanchor 0.5
        text ts:
            style "wnfh_text_" + renpy.store.wnfh_tymeofday
            size ts_size
            slow_cps ts_text_spd

    timer ts_timer action Hide("wnfh_time_skip", transition = ts_transition)
##Ничего необычного. За основу взят оригинальный экран счётчика кадров. Здесь он упрощён.##

init -1010 python:
    config.per_frame_screens.append("ESPE_performance")

screen ESPE_performance():
    zorder 1000

    on "show" action Function(_clear_performance)

    python:
        frame_times = renpy.display.interface.frame_times

        if len(frame_times) < 11:
            fps = 0.0
            cur_time = 0
            max_time = 0

        else:
            ift = [ (j - i) for i, j in zip(frame_times, frame_times[1:]) ]

            fps = 1.0 / (sum(ift[-10:]) / 10.0)

            cur_time = ift[-1] * 1000
            max_time = max(ift) * 1000
    
    frame:
        xalign 1.0
        yalign 1.0
        xpadding 5
        ypadding 5
        xminimum 150
        background "#00000066"

        vbox:
            text "{:.1f} FPS".format(fps) style "espe_text_24"
            text "{:.3f} мс".format(cur_time) style "espe_text_24"
            text "{:.3f} мс худш.".format(max_time) style "espe_text_24" size 20
init:
    style espe_text_heading_36:
        size 36
        outlines([(absolute(1), "#000000", absolute(1), absolute(1))])
        xalign 0.5
        textalign 0.5

    style espe_text_heading_24:
        size 24
        outlines([(absolute(1), "#000000", absolute(1), absolute(1))])
        xalign 0.5
        textalign 0.5

    style espe_text_heading_24_0xalign:
        size 24
        outlines([(absolute(1), "#000000", absolute(1), absolute(1))])
        textalign 0.5

    style espe_text_24:
        size 24
        outlines([(1, "#000000", 0, 0)])
        xalign 0.5
        textalign 0.5

    style espe_text_24_0align:
        size 24
        outlines([(1, "#000000", 0, 0)])
        xalign 0.0
        textalign 0.0

    style espe_text_24_extra:
        size 24
        outlines([(2, "#000000", 0, 0)])
        xalign 0.5
        textalign 0.5
    
    style espe_button_text_24:
        size 24
        outlines([(1, "#000000", 0, 0)])
        xalign 0.5
        textalign 0.5
        hover_color "#a5a5a5"
        insensitive_color "#494949"
    
    style espe_button_text_36:
        size 36
        outlines([(1, "#000000", 0, 0)])
        xalign 0.5
        textalign 0.5
        hover_color "#a5a5a5"
        insensitive_color "#494949"

    style espe_button:
        xalign 0.5
        background None
        mouse "ESPE_cursor_choice"

    style espe_property_bar:
        xmaximum 0.7
        xalign 0.5
        left_bar "espe_property_bar_full"
        right_bar "espe_property_bar_empty"
        thumb "espe_property_bar_thumb"
        thumb_offset 11
        mouse "ESPE_cursor_choice"

    style espe_property_inactive_bar:
        xmaximum 0.7
        xalign 0.5
        left_bar "espe_property_bar_full_insensitive"
        right_bar "espe_property_bar_empty_insensitive"
        thumb "espe_property_bar_thumb_insensitive"
        thumb_offset 11
        mouse "default"
    
    style espe_scrollbar:
        xsize 0.0115
        ysize 0.8
        bar_vertical True
        bar_invert True
        base_bar "espe_scrollbar"
        thumb "espe_scrollbar_thumb"
        thumb_offset 19
        mouse "ESPE_cursor_choice"
    
    style espe_scrollbar_horizontal:
        xsize 0.8
        ymaximum 0.05
        base_bar "espe_scrollbar_horiz"
        thumb "espe_scrollbar_thumb_horiz"
        thumb_offset 19
        mouse "ESPE_cursor_choice"
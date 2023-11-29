init 2:
    screen wnfh_quit():
        tag menu
        modal True
    
        add wnfh_gui["main_menu"]["exit"]
    
        text translation["Quit_confirm"][_preferences.language]:
            style "settings_link"
            size 60
            text_align 0.5
            xalign 0.3 yalign 0.33
            color "#031a68"
            antialias True
            kerning 2
    
        textbutton translation["Yes"][_preferences.language]:
            text_size 70
            style "log_button"
            text_style "settings_link"
            xalign 0.22 yalign 0.55
            text_color "#3b5bc2"
            text_hover_color "#ff7b02"
            action Quit(confirm=False)

        textbutton translation["No"][_preferences.language]:
            text_size 70
            style "log_button"
            text_style "settings_link"
            xalign 0.49 yalign 0.55
            text_color "#3b5bc2"
            text_hover_color "#ff7b02"
            action Return()

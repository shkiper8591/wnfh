init -5:
    $ global frame_transparent
    $ global frame_black
    $ global frame_red
    $ global frame_green
    $ global frame_blue
    $ global frame_purpl
    $ global frame_yellow
    $ global frame_turquoise

    $ global debug_switch

    $ frame_transparent = "#0000"
    $ frame_black       = "#0005"
    $ frame_red         = "#F005"
    $ frame_green       = "#0F05"
    $ frame_blue        = "#00F5"
    $ frame_purpl       = "#F0F5"
    $ frame_yellow      = "#FF05"
    $ frame_turquoise   = "#0FF5"
 
    $ debug_switch = 1
    $ debug_frame = {
        "black":     frame_black      if persistent.wnfh_debug_color else frame_transparent,
        "red":       frame_red        if persistent.wnfh_debug_color else frame_transparent,
        "green":     frame_green      if persistent.wnfh_debug_color else frame_transparent,
        "blue":      frame_blue       if persistent.wnfh_debug_color else frame_transparent,
        "purple":    frame_purpl      if persistent.wnfh_debug_color else frame_transparent,
        "yellow":    frame_yellow     if persistent.wnfh_debug_color else frame_transparent,
        "turquoise": frame_turquoise  if persistent.wnfh_debug_color else frame_transparent,
    }
from enum import Enum

FADE_STEPS = 30

def fade(fade_from, fade_to, steps = FADE_STEPS):
    from_r, from_g, from_b = fade_from
    to_r, to_g, to_b = fade_to
    red_delta = to_r - from_r
    green_delta = to_g - from_g
    blue_delta = to_b - from_b

    colours = []
    for i in range(steps):
        ratio = i / steps
        r = from_r + round(ratio * red_delta)
        g = from_g + round(ratio * green_delta)
        b = from_b + round(ratio * blue_delta)
        colours.append((r, g, b))

    colours.append(fade_to)
    return colours

class Effect(Enum):
    """
    An enum of all the possible effects the bulb can accept
    """
    seven_color_cross_fade = 0x25       #:
    red_gradual_change = 0x26           #:
    green_gradual_change = 0x27         #:
    blue_gradual_change = 0x28          #:
    yellow_gradual_change = 0x29        #:
    cyan_gradual_change = 0x2a          #:
    purple_gradual_change = 0x2b        #:
    white_gradual_change = 0x2c         #:
    red_green_cross_fade = 0x2d         #:
    red_blue_cross_fade = 0x2e          #:
    green_blue_cross_fade = 0x2f        #:
    seven_color_stobe_flash = 0x30      #:
    red_strobe_flash = 0x31             #:
    green_strobe_flash = 0x32           #:
    blue_strobe_flash = 0x33            #:
    yellow_strobe_flash = 0x34          #:
    cyan_strobe_flash = 0x35            #:
    purple_strobe_flash = 0x36          #:
    white_strobe_flash = 0x37           #:
    seven_color_jumping_change = 0x38   #:



import json
from enum import Enum
from homeassistant.util import slugify

FADE_STEPS = 30

COLOURS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 63, 255),
    'purple': (255, 0, 255),
    'sky': (36, 255, 255),
    'sun': (255, 63, 0),
    'white': (255, 100, 109),
    'mint': (146, 159, 127),
    'pink': (236, 71, 148),
    'new_colour': (146, 159, 127),
}

def colour(value):
    """Return a colour value as an rgb tuple"""
    if isinstance(value, str):     # Passing in string
        return COLOURS[value]
    elif isinstance(value, list):  # Passing in array
        return tuple(value)
    elif isinstance(value, tuple): # Passing in rgb tuple
        return value

def map_to_colour(colours):
    """Call 'colour' on all items within list"""
    return list(map(lambda each: colour(each), colours))

def include_in_effects(hass, entity_name):
    state = hass.states.get(f'input_boolean.include_{slugify(entity_name)}')
    if state is not None:
        if state.state == 'on':
            return True
    return False

def configured_colours(hass):
    """Return an array of colours that are "on" with state"""
    colours = []
    for each in COLOURS.keys():
        state = hass.states.get(f'input_boolean.colour_{each}')
        if state is not None:
            if state.state == 'on':
                colours.append(each)

    if len(colours) == 0:
        colours = list(COLOURS.keys())

    return colours

def colour_from_index(hass, index):
    all_colours = full_colour_spectrum(hass)

    print("colour_from_index", index, all_colours)
    if index >= len(all_colours):
        index = 0
    rgb = all_colours[index]

    print("Returnig")
    print(rgb)
    # Increment index
    # self.index += 1
    return rgb


def full_colour_spectrum(hass):
    colours = configured_colours(hass)

    fade_steps_state = hass.states.get('input_number.effect_transition_steps')
    fade_steps = int(float(fade_steps_state.state))
    if fade_steps > 0:
        colours = spectrum(colours, fade_steps)

    return colours

def update_mood_state(hass, rgb):
    def _update_mood_state():
        hass.states.set('input_text.mood_rgb', str(colour(rgb)))
    hass.add_job(_update_mood_state)

def update_colours_json(hass, colours):
    def _update_colours_json():
        mapped_colours = map_to_colour(colours)
        print("\n\nDUMPING", json.dumps(mapped_colours))
        hass.states.set('input_text.colours_json', json.dumps(mapped_colours).replace(" ", ""))
    hass.add_job(_update_colours_json)


def fade(fade_from, fade_to, steps = FADE_STEPS):
    """Transition an rgb tuple to another in x many steps"""
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

def spectrum(colours, steps = FADE_STEPS):
    """Take a list of colours, and accordian it out with "fade" steps between each"""
    output = []
    colours = map_to_colour(colours)
    for i in range(len(colours)):
        start = colours[i]
        end = colours[i+1] if i + 1 < len(colours) else colours[0]
        next_fade = fade(start, end, steps)
        next_fade_without_final_colour = next_fade[:-1]
        output.extend(next_fade_without_final_colour)
    return output

class Effect(Enum):
    """An enum of all the possible effects the bulb can accept"""
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

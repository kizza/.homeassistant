import json

from homeassistant.components import websocket_api
from homeassistant.exceptions import HomeAssistantError
from homeassistant.core import callback

from .util.effects import (full_colour_spectrum, include_in_effects, map_to_colour)

# @websocket_api.async_response

def light_states(hass):
    def entity_is_included(entity_id):
        return include_in_effects(hass, entity_id)

    def get_light_state(entity_id):
        key = f'{entity_id}_colour_index'
        if entity_is_included(entity_id) and key in hass.data:
            return hass.data[key]
        return 'unknown'

    return {
        'tv': get_light_state('tv_backlight'),
        'frame': get_light_state('frame_backlight'),
        'deck': get_light_state('deck_backlight'),
        'bedroom': get_light_state('bedroom_backlight'),
        'downstairs': get_light_state('downstairs_backlight')
    }

@callback
@websocket_api.websocket_command({"type": "lovelace/colours"})
def websocket_effect_colours(hass, connection, msg):
    """Send lovelace UI config over websocket config."""
    colours = full_colour_spectrum(hass, True)
    mapped_colours = map_to_colour(colours)

    message = websocket_api.result_message(
        msg['id'], {
            "colours": mapped_colours,
            "states": light_states(hass)
        }
    )

    connection.send_message(message)

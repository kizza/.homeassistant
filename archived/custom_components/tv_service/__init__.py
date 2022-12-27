DOMAIN = 'tv_service'

import logging
from homeassistant.components.media_player import (
    DOMAIN as MEDIA_PLAYER_DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

# def get_entity(hass, domain, entity_id):
#     return hass.data[domain].get_entity(f'{domain}.big_tv')

# def ping_entity(hass, domain, entity_id):
#     entity = get_entity(hass, domain, entity_id)
#     _LOGGER.debug(f'Pinging {entity}...')
#     # value = entity.ping.ping()
#     entity.update()
#     return entity.is_on

# def refresh_state(hass, domain, entity_id):
#     """Call binary sensor state, update local state and return value"""
#     value = ping_entity(hass, domain, entity_id)
#     set_state(hass, domain, entity_id, value)
#     return value

def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""
    TV_ENTITY_ID = 'big_tv_android'

    def is_on():
        state = hass.states.get(f'{MEDIA_PLAYER_DOMAIN}.{TV_ENTITY_ID}')
        if state is not None:
            return state not in ['off', 'unavailable']
        return False

    def handle_turn_on(call):
        """If currently off, turn on"""
        if not is_on():
            _LOGGER.debug("Turning on TV (and backlight)")
            hass.services.call("script", "turn_big_tv_on_off", None, False)
            hass.services.call("script", "turn_on_tv_backlight", None, False)
        else:
            _LOGGER.debug("TV is already on")

    def handle_turn_off(call):
        """If currently on, turn off, and set state"""
        if is_on():
            _LOGGER.debug("Turning off TV")
            hass.services.call("script", "turn_big_tv_on_off", None, False)
        else:
            _LOGGER.debug("TV is already off")

    def handle_toggle(call):
        """Will immediately send a toggle, then become consistent"""
        hass.services.call("script", "turn_big_tv_on_off", None, False)

    hass.services.register(DOMAIN, 'turn_on', handle_turn_on)
    hass.services.register(DOMAIN, 'turn_off', handle_turn_off)
    hass.services.register(DOMAIN, 'toggle', handle_toggle)

    # Return boolean to indicate that initialization was successfully.
    return True

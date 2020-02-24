DOMAIN = 'tv_service'

import logging
from homeassistant.components.binary_sensor import (
    DOMAIN as BINARY_SENSOR_DOMAIN,
)

ATTR_NAME = 'name'
DEFAULT_NAME = 'World'
_LOGGER = logging.getLogger(__name__)

def get_entity(hass, domain, entity_id):
    return hass.data[domain].get_entity(f'{domain}.big_tv')

def ping_entity(hass, domain, entity_id):
    entity = get_entity(hass, domain, entity_id)
    _LOGGER.debug(f'Pinging {entity}...')
    # value = entity.ping.ping()
    entity.update()
    return entity.is_on

def refresh_state(hass, domain, entity_id):
    """Call binary sensor state, update local state and return value"""
    value = ping_entity(hass, domain, entity_id)
    set_state(hass, domain, entity_id, value)
    return value

def get_state(hass, domain, entity_id):
    return hass.states.get(f'{domain}.{entity_id}')

def set_state(hass, domain, entity_id, value):
    state = "on" if value else "off"
    _LOGGER.debug("Setting state to '%s'", state)
    hass.states.set(f'{domain}.{entity_id}', state, {
        # 'name': 'My name',
        # 'label': 'My label',
        # 'icon': 'mdi:power',
        'friendly_name': 'Big TV',
        # 'value': 'ME',
        # 'description': 'My description',
        # 'device_class': 'connectivity'
    }, force_update=True)

    if value is True:
        hass.services.call("script", "turn_on_tv_backlight", None, False)

def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""
    TV_ENTITY_ID = 'big_tv'

    def _toggle_state():
        """Toggle the current state"""
        state = get_state(hass, BINARY_SENSOR_DOMAIN, TV_ENTITY_ID)
        value = state.state == 'on'
        _LOGGER.debug("Toggling state from %s", str(value))
        set_state(hass, BINARY_SENSOR_DOMAIN, TV_ENTITY_ID, not value)

    def _calculate_and_set_state():
        """Get the current refreshed state of the binary sensor"""
        return refresh_state(hass, BINARY_SENSOR_DOMAIN, TV_ENTITY_ID)

    def _set_state(value):
        """Set the new state of the sensor based on actions"""
        set_state(hass, BINARY_SENSOR_DOMAIN, TV_ENTITY_ID, value)

    def handle_turn_on(call):
        """If currently off, turn on, and set state"""
        _toggle_state()  # Just toggle for visual appeal
        value = _calculate_and_set_state()
        if value is False:
            hass.services.call("script", "turn_big_tv_on_off", None, False)
            _set_state(True)

    def handle_turn_off(call):
        """If currently on, turn off, and set state"""
        _toggle_state()  # Just toggle for visual appeal
        value = _calculate_and_set_state()
        if value is True:
            hass.services.call("script", "turn_big_tv_on_off", None, False)
            _set_state(False)

    def handle_toggle(call):
        """Will immediately send a toggle, then become consistent"""
        _toggle_state()
        hass.services.call("script", "turn_big_tv_on_off", None, False)
        schedule_refresh()

    def schedule_refresh():
        hass.async_add_job(_become_eventually_consistant)

    def _become_eventually_consistant():
        """Ping the tv, and set it's state"""
        _calculate_and_set_state()

    def temp():
        # for k, v in hass.data.items():
        #     print(k)
        print(hass.data['my_platform'])
        print("Items...")
        for entity in hass.data['my_platform']:
            print(entity)
        # hass.states.set('hello_service.hello', name)

    hass.services.register(DOMAIN, 'turn_on', handle_turn_on)
    hass.services.register(DOMAIN, 'turn_off', handle_turn_off)
    hass.services.register(DOMAIN, 'toggle', handle_toggle)

    # Return boolean to indicate that initialization was successfully.
    return True

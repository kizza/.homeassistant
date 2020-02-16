import logging

from homeassistant.const import ( STATE_ON, STATE_OFF )
from homeassistant.components.light import ( Light )

_LOGGER = logging.getLogger(__name__)

class Base(Light):
    def __init__(self, hass, config_entry):
        self._hass = hass
        self._config_entry = config_entry
        self._device_id = None
        self._state = STATE_OFF
        self._rgb = (255, 255, 255)
        self._brightness = 255
        self._available = True
        self._effects = []
        # self.lock = asyncio.Lock()

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def rgb_color(self):
        return self._rgb

    @property
    def brightness(self):
        return self._brightness

    @property
    def effect_list(self):
        return self._effects

    @property
    def available(self):
        return self._available

    @property
    def icon(self):
        if self._state == STATE_ON:
            return "mdi:lightbulb-on-outline"
        else:
            return "mdi:lightbulb-outline"

    def is_on(self):
        return self._state == STATE_ON

    def turn_on(self):
        print("THIS SHOULD NOT HAPPEN")
        self._state = STATE_ON
        self.schedule_update_ha_state()

    def turn_off(self):
        self._state = STATE_OFF
        self.schedule_update_ha_state()

    async def wrap_and_catch(self, fun, description):
        """Catch any connection errors and set unavailable."""
        try:
            await fun
        except Exception as ex:
        # except ConnectionError as ex:
            _LOGGER.error(f'ERROR: Could not {description} {self.name}\n{ex}')
            self.failed_action(description)
        else:
            self.successful_action(description)

    #async def async_added_to_hass(self):
    #    debug("Added to hass!")

    #async def async_setup_entry(self):
    #    debug("About to remove from hass")

    #def update(self):
    #    _LOGGER.debug("%s.update()", self)
    #    self.hass.add_job(self._update_blocking)

    #async def async_update(self):
    #    debug("doing async update")

    #def _update_blocking(self):
    #    #_LOGGER.debug("%s._update_blocking()", self)
    #    print("\n\n_update_blocking\n\n")
    #    try:
    #        # if not self._light.test_connection():
    #            # self._light.connect(self._hci_device_id)
    #        # device_info = self._light.get_device_info()
    #        # self._state = False
    #        # self._rgb = (device_info['r'], device_info['g'], device_info['b'])
    #        self._rgb = (0, 255, 0)
    #        self._brightness = 100 # device_info['brightness']
    #        self._effect = None
    #        self._available = True
    #        print("Set is available")
    #    except Exception as ex:
    #        print("\n\nTHERE IS A PROBLEM\n\n\n");
    #        _LOGGER.debug("%s._update_blocking(): Exception during update status: %s", self, ex)
    #        self._available = False

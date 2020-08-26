import asyncio
import logging

from homeassistant.const import ( STATE_ON, STATE_OFF )
from homeassistant.components.light import ( Light )
import homeassistant.util.color as color_util

_LOGGER = logging.getLogger(__name__)

class Queue(Light):
    def __init__(self):
        self._queue = []

    def _enqueue(self, message, callback=None):
        data, description = self._format_enqueued_message(message)
        self._queue.append((data, description, callback))

    def _enqueue_effect(self, data, callback=None):
        self._queue.append((data, 'Effect', callback))

    def _clear_enqueue(self):
        self._queue = []

class Bulb(Queue):
    def __init__(self, hass, config_entry):
        super().__init__()
        self._hass = hass
        self._config_entry = config_entry
        self._device_id = None
        self._state = STATE_OFF
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
        return self._raw_rgb

    @property
    def hs_color(self):
        """This makes the bulb icon change :)"""
        return color_util.color_RGB_to_hs(*self._raw_rgb)

    @property
    def brightness(self):
        return self._brightness

    @property
    def effect_list(self):
        return self._effects

    @property
    def available(self):
        return self._available

    # @property
    # def icon(self):
    #     if self._state == STATE_ON:
    #         return "mdi:lightbulb-on-outline"
    #     else:
    #         return "mdi:lightbulb-outline"

    def is_on(self):
        return self._state == STATE_ON

    def turn_on(self):
        print("THIS SHOULD NOT HAPPEN")
        self._state = STATE_ON
        self.schedule_update_ha_state()

    def turn_off(self):
        self._state = STATE_OFF
        self.schedule_update_ha_state()

    def safe(self, fun, description):
        try:
            fun()
        except Exception as ex:
            _LOGGER.warning(f'Safe {description} failed')

    async def wrap_and_catch(self, fun, description, attempts=1):
        """Catch any connection errors and set unavailable."""
        print("Doing a wrap_and_catch for "+ description)
        try:
            await fun()
        except Exception as ex:
        # except ConnectionError as ex:
            _LOGGER.error(f'ERROR: Could not {description} {self.name}\n{ex} after {attempts} attempts')
            self.failed_action(description, attempts)
            if attempts <= 5:
                print("Running attempt again")
                await asyncio.sleep(10)
                await self.wrap_and_catch(fun, description, attempts + 1)
        else:
            self.successful_action(description, attempts)

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

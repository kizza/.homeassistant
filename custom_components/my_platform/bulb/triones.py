import colorsys
import logging
import math
import random
import time
from bluepy import btle
# from ..test import FakeBtle as btle

from . import Bulb
from ..const import ( debug, DOMAIN )
from ..util import ( map_tuple )
from ..util.effects import ( colour, Effect, fade )

from homeassistant.const import (CONF_NAME, CONF_MAC, STATE_ON, STATE_OFF)
from homeassistant.util.color import color_hsv_to_RGB
from homeassistant.components.light import (
    ATTR_BRIGHTNESS, ATTR_HS_COLOR, ATTR_RGB_COLOR, ATTR_EFFECT,
    SUPPORT_COLOR, SUPPORT_BRIGHTNESS, SUPPORT_EFFECT
)

_LOGGER = logging.getLogger(__name__)
NEXT_MESSAGE_DELAY = 0
ERRORED_MESSAGE_DELAY = 0.8
TURN_ON = 'TURN_ON'
TURN_OFF = 'TURN_OFF'
NO_COLOUR = 'NO_COLOUR'

class Triones(Bulb):

    def __init__(self, hass, config_entry, config):
        super().__init__(hass, config_entry)
        self._name = config.get(CONF_NAME)
        self._mac = config.get(CONF_MAC)
        self._characteristic = None
        self._effects = [e for e in Effect.__members__.keys()]
        self._raw_rgb = (0, 255, 0)
        self._brightness = 255
        self._rgb = self._filter_colour_with_brightness()

    @property
    def unique_id(self):
        return f'triones-{self._mac}'

    @property
    def supported_features(self):
        return SUPPORT_BRIGHTNESS | SUPPORT_COLOR | SUPPORT_EFFECT

    @property
    def device_info(self):
        return {
            "identifiers": { (DOMAIN, self.unique_id) },
            "name": self.name,
            "manufacturer": "Kizza",
            "model": "Model thing",
            "sw_version": "Version 0.0.1",
            "connections": { (self._hass.helpers.device_registry.CONNECTION_NETWORK_MAC, self._mac) },
            "via_device": (DOMAIN, self._device_id)
        }

    @property
    def effect_list(self):
        return self._effects

    async def async_added_to_hass(self):
        self.hass.async_add_job(self.safe, self.connect, f'{self.name} initial connect')

    def successful_action(self, description, attempts):
        _LOGGER.debug(f'{self} Able to {description} after {attempts} attempts')
        self._available = True

    def failed_action(self, description, attempts):
        _LOGGER.warning(f'{self} Unable to {description} ({attempts} attempts)')
        self._characteristic = None

    def connect(self):
        """Connect to device and store characteristic"""
        # if random.random() < .5:
        #     raise ValueError("Custom random error")

        if self._characteristic is not None:
            return

        _LOGGER.debug(f'{self} Connecting to {self._mac}...')
        device = btle.Peripheral(self._mac)
        service = device.getServiceByUUID(btle.UUID("ffd5"))
        self._characteristic = service.getCharacteristics()[0]
        _LOGGER.debug(f'{self} Connected')

    async def flash(self):
        self._clear_enqueue()
        self._flash()
        self.process_message_queue()

    async def theme(self, rgb):
        self._clear_enqueue()
        self._raw_rgb = colour(rgb)

        if not self.is_on():
            self._rgb = (0, 0, 0)
            self._set_on(True)

        to_rgb = self._filter_colour_with_brightness()
        self._fade_colour(to_rgb)
        self.process_message_queue()

    async def turn_on(self, **kwargs):
        _LOGGER.debug("%s.turn_on()", self)
        self._clear_enqueue()  # Remove any messages

        if ATTR_EFFECT in kwargs:
            self._effect = kwargs[ATTR_EFFECT]
            self._set_effect(Effect[self._effect].value, 10)

        elif ATTR_BRIGHTNESS in kwargs:
            self._brightness = kwargs[ATTR_BRIGHTNESS]
            to_rgb = self._filter_colour_with_brightness()
            self._fade_colour(to_rgb)

        elif ATTR_HS_COLOR in kwargs:
            hue, saturation = kwargs[ATTR_HS_COLOR]
            self._raw_rgb = color_hsv_to_RGB(hue, saturation, 100)
            _LOGGER.debug("%s set rgb to %s", self, self._raw_rgb)
            to_rgb = self._filter_colour_with_brightness()
            self._fade_colour(to_rgb)

        else:
            self._fade_on()

        self.process_message_queue()

    async def turn_off(self):
        _LOGGER.debug("%s.turn_off()", self)
        self._clear_enqueue()
        self._fade_off()
        self.process_message_queue()

    # def set_random_color(self):
    #     self.set_color([random.randint(1, 255) for i in range(3)])

    def _format_enqueued_message(self, message):
        """Messages are enqueued in human readable form, format them here"""
        if message == TURN_ON:
            return Protocol.TURN_ON, 'turn on'
        elif message == TURN_OFF:
            return Protocol.TURN_OFF, 'turn off'
        elif message == NO_COLOUR:
            return Protocol.NO_COLOUR, 'blank colour'
        else:
            return Protocol.encode_rgb(*message), str(message)

    def process_message_queue(self):
        """Process the queue, update ha state if complete"""
        if len(self._queue) > 0:
            item = self._queue.pop(0)
            self.hass.async_add_job(self.process_message, item)
        else:
            _LOGGER.debug("%s, queue processed, scheduling state update", self.name)
            self.schedule_update_ha_state()

    def process_message(self, item, attempts = 1):
        """Process a single provided message"""
        (message, description, callback) = item
        try:
            self.connect()
            self._write_to_characteristic(message)
            if callback:
                callback()
            # self.successful_action(description, attempts)
            self.process_next_message()
        except Exception as ex:
            if attempts < 5:
                _LOGGER.warning("%s failed %s, retrying...", self.name, ex)
                time.sleep(ERRORED_MESSAGE_DELAY)
                self.hass.async_add_job(self.process_message, item, attempts + 1)
            else:
                _LOGGER.warning("%s failed after too many attempts %s", self.name, ex)
                self.failed_action(description, attempts)
                self.hass.async_add_job(self.process_message_queue)

    def process_next_message(self):
        """Process the next message on the queue"""
        # time.sleep(NEXT_MESSAGE_DELAY)
        self.hass.async_add_job(self.process_message_queue)

    #
    # _set_*
    #

    def _set_on(self, silently = False):
        _LOGGER.debug("%s set_on", self)
        def callback():
            self._state = STATE_ON
        if silently:
            self._enqueue(NO_COLOUR)
        self._enqueue(TURN_ON, callback)

    def _set_off(self):
        _LOGGER.debug("%s turn_on", self)
        def callback():
            self._state = STATE_OFF
        self._enqueue(TURN_OFF, callback)

    def _fade_on(self):
        _LOGGER.debug("%s fade_on", self)
        def callback():
            self._state = STATE_ON

        # Initial
        self._enqueue(NO_COLOUR)
        self._enqueue(TURN_ON)

        # Fade
        for rgb in fade((0, 0, 0), self._rgb):
            self._enqueue(rgb)

        # Final
        self._enqueue(self._rgb, callback)

    def _fade_off(self):
        _LOGGER.debug("%s fade_off", self)
        def callback():
            self._state = STATE_OFF

        # Fade
        for rgb in fade(self._rgb, (0, 0, 0)):
            self._enqueue(rgb)

        # Final
        self._enqueue(NO_COLOUR)
        self._enqueue(TURN_OFF, callback)

    def _flash(self):
        _LOGGER.debug("%s flash", self)
        # fade_out = fade(self._rgb, (0, 0, 0), 12)
        # fade_in = fade((0, 0, 0), self._rgb, 12)
        fade_out = fade(self._rgb, (255, 0, 0), 12)
        fade_in = fade((255, 0, 0), self._rgb, 12)

        # Create colours
        colours = []
        if self.is_on():
            print("Doing the on version")
            colours.extend(fade_out)
            colours.extend(fade_in)
            for rgb in colours:
                self._enqueue(rgb)
        else:
            print("Doing the off version")
            self._enqueue(NO_COLOUR)
            self._enqueue(TURN_ON)
            colours.extend(fade_in)
            colours.extend(fade_out)
            for rgb in colours:
                self._enqueue(rgb)
            self._enqueue(TURN_OFF)

    def _filter_colour_with_brightness(self):
        """Apply the brightness level to the rgb level"""
        ratio = self._brightness / 255
        percentage = ratio * 0.5   # Bulb has no effect after 50%
        return map_tuple(lambda x: math.ceil(x * percentage), self._raw_rgb)

    def _set_colour(self):
        _LOGGER.debug("%s set_colour", self)
        def callback():
            self._state = STATE_ON

        self._enqueue(self._rgb)

    def _fade_colour(self, to_rgb):
        _LOGGER.debug("%s fade_colour", self)
        def callback():
            self._rgb = to_rgb  # Set the "go to" colour when complete

        # Fade
        colours = fade(self._rgb, to_rgb)
        for rgb in colours:
            self._enqueue(rgb)

        # Final
        self._enqueue(to_rgb, callback)

    def _set_effect(self, effect, effect_speed):
        _LOGGER.debug("%s set_effect", self)
        data = Protocol.encode_effect(effect, effect_speed)
        self._enqueue_effect(data)

    def _write_to_characteristic(self, message):
        if self._characteristic:
            data = bytearray([x % 256 for x in message])
            self._characteristic.write(data, False)

class Protocol():
    TURN_ON = [-52, 35, 51]
    TURN_OFF = [-52, 36, 51]
    NO_COLOUR = [86, 0, 0, 0, 100, -16, -86]

    def encode_rgb(red, green, blue):
        return [86, red, green, blue, 100, -16, -86]

    def encode_effect(effect, effect_speed):
        return [-69, effect, effect_speed, 68]

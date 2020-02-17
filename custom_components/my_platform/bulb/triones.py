import colorsys
import logging
import math
import random
import time
from bluepy import btle
# from ..test import FakeBtle as btle
from enum import Enum

from . import Base
from ..const import ( debug, DOMAIN )
from ..util import ( map_tuple )

from homeassistant.const import (CONF_NAME, CONF_MAC, STATE_ON, STATE_OFF)
from homeassistant.util.color import color_hsv_to_RGB
from homeassistant.components.light import (
    ATTR_BRIGHTNESS, ATTR_HS_COLOR, ATTR_RGB_COLOR, ATTR_EFFECT,
    SUPPORT_COLOR, SUPPORT_BRIGHTNESS, SUPPORT_EFFECT
)

_LOGGER = logging.getLogger(__name__)
NEXT_MESSAGE_DELAY = 0
ERRORED_MESSAGE_DELAY = 0.3
FADE_STEPS = 20

class Protocol():
    TURN_ON = [-52, 35, 51]
    TURN_OFF = [-52, 36, 51]
    NO_COLOUR = [86, 0, 0, 0, 100, -16, -86]

    def encode_rgb(red, green, blue):
        return [86, red, green, blue, 100, -16, -86]

def fade(fade_from, fade_to, steps = 40):
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

class Triones(Base):

    def __init__(self, hass, config_entry, config):
        super().__init__(hass, config_entry)
        self._name = config.get(CONF_NAME)
        self._mac = config.get(CONF_MAC)
        self._characteristic = None
        self._effects = [e for e in Effect.__members__.keys()]

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

        _LOGGER.debug(f'{self} connecting to {self._mac}...')
        device = btle.Peripheral(self._mac)
        # dev = btle.Peripheral("ff:ff:bc:00:2b:09")
        # for svc in device.services:
        #     print(str(svc))
        service = device.getServiceByUUID(btle.UUID("ffd5"))
        self._characteristic = service.getCharacteristics()[0]
        _LOGGER.debug(f'{self} connected')

    # async def async_update(self):
        # print(f'Async update for {self.name}')

    async def do_custom_thing(self):
        self._flash()
        self.process_message_queue()

    async def turn_on(self, **kwargs):
        print("\nAsked light to turn on by homeassistant")
        print(kwargs)
        _LOGGER.debug("%s.turn_on()", self)

        self._clear_enqueue()  # Remove any messages

        if ATTR_EFFECT in kwargs:
            # self._set_effect(Effect[kwargs[ATTR_EFFECT]].value, 10)
            await self.wrap_and_catch(lambda: {
                self._set_effect(Effect[kwargs[ATTR_EFFECT]].value, 10)
                }, 'set effect'
            )

        elif ATTR_BRIGHTNESS in kwargs:
            self._brightness = kwargs[ATTR_BRIGHTNESS]
            self._set_color()

        elif ATTR_HS_COLOR in kwargs:
            hue, saturation = kwargs[ATTR_HS_COLOR]
            # self._rgb = color_hsv_to_RGB(hue, saturation, 100)
            new_rgb = color_hsv_to_RGB(hue, saturation, 100)
            self._fade_colour(new_rgb)
            # self._set_color()

        else:
            self._set_on()

        self.process_message_queue()

    async def turn_off(self):
        _LOGGER.debug("%s.turn_off()", self)
        self._set_off()
        self.process_message_queue()

    # def set_random_color(self):
    #     self.set_color([random.randint(1, 255) for i in range(3)])

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
        # _LOGGER.debug("Processing message %s...", description)
        try:
            self.connect()
            self._write(message)
            if callback:
                callback()
            # self.successful_action(description, attempts)
            self.process_next_message()
        except Exception as ex:
            _LOGGER.warning("%s failed %s", self.name, ex)
            if attempts < 5:
                time.sleep(ERRORED_MESSAGE_DELAY)
                self.hass.async_add_job(self.process_message, item, attempts + 1)
            else:
                print("Checking queue")
                self.failed_action(description, attempts)
                self.hass.async_add_job(self.process_message_queue)

    def process_next_message(self):
        """Process the next message on the queue"""
        # time.sleep(NEXT_MESSAGE_DELAY)
        self.hass.async_add_job(self.process_message_queue)

    #
    # _set_*
    #

    def _set_on(self):
        self._fade_on()
        # print("\nASKED: To set on")
        # def callback():
        #     self._state = STATE_ON
        # self._enqueue(Protocol.TURN_ON, 'turn on', callback)

    def _fade_on(self):
        print("\nASKED: To fade on")
        def callback():
            self._state = STATE_ON

        # Initial
        self._enqueue(Protocol.NO_COLOUR, 'blank colour')
        self._enqueue(Protocol.TURN_ON, 'turn on')

        # Fade
        colours = fade((0, 0, 0), self._rgb)
        for rgb in colours:
            self._enqueue(Protocol.encode_rgb(*rgb), f'increment')

        # Final
        self._enqueue(Protocol.encode_rgb(*self._rgb), 'final', callback)

        # Fade back
        fade_out = fade(self._rgb, (0, 0, 0))
        colours.extend(fade_out)

    def _set_off(self):
        self._fade_off()
        # print("\nASKED: To turn off")
        # def callback():
        #     self._state = STATE_OFF
        # self._enqueue(Protocol.TURN_OFF, 'turn off', callback)

    def _fade_off(self):
        print("\nASKED: To fade off")
        def callback():
            self._state = STATE_OFF

        # Fade
        colours = fade(self._rgb, (0, 0, 0))
        for rgb in colours:
            self._enqueue(Protocol.encode_rgb(*rgb), f'increment')

        # Final
        self._enqueue(Protocol.NO_COLOUR, 'blank colour')
        self._enqueue(Protocol.TURN_OFF, 'turn off', callback)

    def _flash(self):
        print("\nASKED: To flash")
        fade_out = fade(self._rgb, (0, 0, 0))
        fade_in = fade((0, 0, 0), self._rgb)

        # Create colours
        colours = []
        if self.is_on():
            print("Doing the on version")
            colours.extend(fade_out)
            colours.extend(fade_in)
            for rgb in colours:
                self._enqueue(Protocol.encode_rgb(*rgb), f'flash when on')
        else:
            print("Doing the off version")
            self._enqueue(Protocol.NO_COLOUR, 'blank colour')
            self._enqueue(Protocol.TURN_ON, 'turn on')
            colours.extend(fade_in)
            colours.extend(fade_out)
            for rgb in colours:
                self._enqueue(Protocol.encode_rgb(*rgb), f'flash when off')
            self._enqueue(Protocol.TURN_OFF, 'turn off')

    def _set_color(self):
        print("\nASKED: To set color")
        ratio = self._brightness / 255
        percentage = ratio * 0.5   # Bulb has no effect after 50%
        rgb = map_tuple(lambda x: math.ceil(x * percentage), self._rgb)

        def callback():
            self._state = STATE_ON
        self._enqueue(Protocol.encode_rgb(*rgb), 'set colour')

    def _fade_colour(self, to_rgb):
        print("\nASKED: To fade colour")
        def callback():
            self._rgb = to_rgb

        # Fade
        colours = fade(self._rgb, to_rgb)
        for rgb in colours:
            self._enqueue(Protocol.encode_rgb(*rgb), f'increment')
            print(f'Faded replayed {rgb}')

        # Final
        self._enqueue(Protocol.encode_rgb(*to_rgb), 'set colour', callback)

    async def _set_effect(self, effect, effect_speed):
        print("\nASKED: To set effect")
        print(effect)
        self.connect()
        data = self._encode_effect(effect)
        self._write(data)
        self._effect = effect
        print("_write finished")

    def _encode_effect(self, effect):
        print("Creating a effect here")
        return [-69, effect, 10, 68]

    def _write(self, message):
        if self._characteristic:
            data = bytearray([x % 256 for x in message])
            self._characteristic.write(data, False)
            _LOGGER.debug(f'Writing to characteristic {data}')
        else:
            _LOGGER.debug(f'No characteristic for write :(')


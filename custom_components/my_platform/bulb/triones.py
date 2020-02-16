import colorsys
import logging
import math
import time
from bluepy import btle
from enum import Enum
# from ..test import FakeBtle as btle

from . import Base
from ..const import ( debug, DOMAIN )
from homeassistant.const import (CONF_NAME, CONF_MAC, STATE_ON, STATE_OFF)
from homeassistant.components.light import (
    ATTR_BRIGHTNESS, ATTR_HS_COLOR, ATTR_RGB_COLOR, ATTR_EFFECT,
    SUPPORT_COLOR, SUPPORT_BRIGHTNESS, SUPPORT_EFFECT
)

_LOGGER = logging.getLogger(__name__)

def color_hsv_to_rgb(iH, iS, iV):
    """Convert an hsv color into its rgb representation.
    Hue is scaled 0-360
    Sat is scaled 0-100
    Val is scaled 0-100
    """
    fRGB = colorsys.hsv_to_rgb(iH / 360, iS / 100, iV / 100)
    return (int(fRGB[0] * 255), int(fRGB[1] * 255), int(fRGB[2] * 255))

def map_tuple(func, tup):
    new_tuple = ()
    for each in tup:
        new_tuple += (func(each),)
    return new_tuple

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
        _LOGGER.debug(f'Added {self} to hass')
        try:
            self.connect()
        except Exception as ex:
            pass
        # await self.wrap_and_catch(lambda: self.connect(), 'initialise connect')

    def successful_action(self, description, attempts):
        _LOGGER.debug(f'Was able to {description} {self.name} after {attempts} attempts')
        self._available = True

    def failed_action(self, description, attempts):
        _LOGGER.warning(f'Was unable to {description} {self.name} ({attempts} attempts)')
        self._characteristic = None

    def connect(self):
        """Connect to device and store characteristic"""
        if self._characteristic is not None:
            print("Alread connected :)")
            return

        # try:

        _LOGGER.debug(f'Connecting to {self.name} at {self._mac}...')
        device = btle.Peripheral(self._mac)
        # dev = btle.Peripheral("ff:ff:bc:00:2b:09")
        # for svc in device.services:
        #     print(str(svc))
        service = device.getServiceByUUID(btle.UUID("ffd5"))
        self._characteristic = service.getCharacteristics()[0]
        _LOGGER.debug(f'Connected to {self} at {self._mac}!')

        # except Exception as ex:
        #     print("Could not get connect to device");
        #     self.failed_action('connect', 1);
        #     _LOGGER.error("%s.connect(): Exception during connection: %s", self, ex)

    # async def async_update(self):
        # print(f'Async update for {self.name}')

    async def do_custom_thing(self):
        await self.wrap_and_catch(lambda: self._flash(), 'flash')

    async def turn_on(self, **kwargs):
        print("\nAsked light to turn on by homeassistant")
        print(kwargs)
        _LOGGER.debug("%s.turn_on()", self)

        if ATTR_EFFECT in kwargs:
            # self._set_effect(Effect[kwargs[ATTR_EFFECT]].value, 10)
            await self.wrap_and_catch(lambda: {
                self._set_effect(Effect[kwargs[ATTR_EFFECT]].value, 10)
                }, 'set effect'
            )

        elif ATTR_BRIGHTNESS in kwargs:
            self._brightness = kwargs[ATTR_BRIGHTNESS]
            await self.wrap_and_catch(lambda: self._set_color(), 'set colour')

        elif ATTR_HS_COLOR in kwargs:
            hue, saturation = kwargs[ATTR_HS_COLOR]
            self._rgb = color_hsv_to_rgb(hue, saturation, 100)
            await self.wrap_and_catch(lambda: self._set_color(), 'set colour')

        else:
            await self.wrap_and_catch(lambda: self._set_on(), 'turn on')

        self.schedule_update_ha_state()

    async def turn_off(self):
        _LOGGER.debug("%s.turn_off()", self)
        await self.wrap_and_catch(lambda: self._set_off(), 'turn off')
        self.schedule_update_ha_state()

    # def set_random_color(self):
    #     self.set_color([random.randint(1, 255) for i in range(3)])

    async def _set_on(self):
        print("\nASKED: To set on")
        self.connect()
        self._write([-52, 35, 51])
        self._state = STATE_ON

    async def _set_off(self):
        print("\nASKED: To turn off")
        self.connect()
        self._write([-52, 36, 51])
        self._state = STATE_OFF

    async def _flash(self):
        print("\nASKED: To flash")
        delay = 0.3
        self.connect()
        if self.is_on():
            print("Doing the on version")
            self._write([-52, 36, 51]) # off first
            time.sleep(delay)
            self._write([-52, 35, 51])
            time.sleep(delay)
            self._write([-52, 36, 51])
            time.sleep(delay)
            self._write([-52, 35, 51])
        else:
            print("Doing the off version")
            self._write([-52, 35, 51])
            time.sleep(delay)
            self._write([-52, 36, 51])
            time.sleep(delay)
            self._write([-52, 35, 51])
            time.sleep(delay)
            self._write([-52, 35, 51])

    async def _set_color(self):
        print("\nASKED: To set color")
        self.connect()
        ratio = self._brightness / 255
        percentage = ratio * 0.5 # Bulb has no effect after 50%
        rgb = map_tuple(lambda x: math.ceil(x * percentage), self._rgb)

        data = self._encode_color(*rgb)
        self._write(data)
        self._state = STATE_ON

    async def _set_effect(self, effect, effect_speed):
        print("\nASKED: To set effect")
        print(effect)
        self.connect()
        data = self._encode_effect(effect)
        self._write(data)
        self._effect = effect
        print("_write finished")

    def _encode_color(self, red, green, blue):
        return [86, red, green, blue, 100, -16, -86]

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


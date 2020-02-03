# This file is being loaded
from bluepy import btle
import math
import colorsys
from enum import Enum

import functools
import logging
import threading

import voluptuous as vol

# Import the device class from the component that you want to support
from homeassistant.components.light import (
    ATTR_BRIGHTNESS, ATTR_RGB_COLOR, ATTR_EFFECT,
    SUPPORT_COLOR, SUPPORT_BRIGHTNESS, SUPPORT_EFFECT,
    Light, PLATFORM_SCHEMA
)

import homeassistant.helpers.config_validation as cv

CONF_NAME = 'name'
CONF_ADDRESS = 'address'
CONF_VERSION = 'version'
CONF_HCI_DEVICE_ID = 'hci_device_id'
DEFAULT_VERSION = 9
DEFAULT_HCI_DEVICE_ID = 0

# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_NAME): cv.string,
    vol.Required(CONF_ADDRESS): cv.string,
    vol.Optional(CONF_VERSION, default=DEFAULT_VERSION): cv.positive_int,
    vol.Optional(CONF_HCI_DEVICE_ID, default=DEFAULT_HCI_DEVICE_ID):
        cv.positive_int
})

_LOGGER = logging.getLogger(__name__)

class Effect(Enum):
    """
    An enum of all the possible effects the bulb can accept
    """
    seven_color_cross_fade = 37 # 0x25       #:
    red_gradual_change = 38 # 0x26           #:
    green_gradual_change = 39 # 0x27         #:
    blue_gradual_change = 40 # 0x28          #:
    yellow_gradual_change = 41 # 0x29        #:
    cyan_gradual_change = 42 # 0x2a          #:
    purple_gradual_change = 43 # 0x2b        #:
    white_gradual_change = 44 # 0x2c         #:
    red_green_cross_fade = 45 # 0x2d         #:
    red_blue_cross_fade = 46 # 0x2e          #:
    green_blue_cross_fade = 47 # 0x2f        #:
    seven_color_stobe_flash = 48 # 0x30      #:
    red_strobe_flash = 49 # 0x31             #:
    green_strobe_flash = 50 # 0x32           #:
    blue_strobe_flash = 51 # 0x33            #:
    yellow_strobe_flash = 52 # 0x34          #:
    cyan_strobe_flash = 53 # 0x35            #:
    purple_strobe_flash = 54 # 0x36          #:
    white_strobe_flash = 55 # 0x37           #:
    seven_color_jumping_change = 56 # 0x38   #:

# region Decorators
def comm_lock(blocking=True):
    """
    Lock method (per instance) such that the decorated method cannot be ran from multiple thread simulatinously.
    If blocking = True (default), the thread will wait for the lock to become available and then execute the method.
    If blocking = False, the thread will try to acquire the lock, fail and _not_ execute the method.
    """
    def ensure_lock(instance):
        if not hasattr(instance, '_comm_lock'):
            instance._comm_lock = threading.Lock()

        return instance._comm_lock

    def call_wrapper(func):
        """Call wrapper for decorator."""

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            """Lock method (per instance) such that the decorated method cannot be ran from multiple thread simulatinously."""

            lock = ensure_lock(self)

            locked = lock.acquire(blocking)
            if locked:
                _LOGGER.debug('comm_lock(): %s.%s: entry', self, func.__name__)
                vals = func(self, *args, **kwargs)
                lock.release()
                _LOGGER.debug('comm_lock(): %s.%s: exit', self, func.__name__)
                return vals

            _LOGGER.debug('comm_lock(): %s.%s: lock not acquired, exiting', self, func.__name__)

        return wrapper

    return call_wrapper
# endregion


# region Home-Assistant
def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the MagicBlue platform."""
    # from magicblue import MagicBlue

    # Assign configuration variables. The configuration check takes care they are
    # present.
    bulb_name = config.get(CONF_NAME)
    bulb_mac_address = config.get(CONF_ADDRESS)
    bulb_version = config.get(CONF_VERSION)
    hci_device_id = config.get(CONF_HCI_DEVICE_ID)

    # bulb = MagicBlue(bulb_mac_address, bulb_version)

    # Add devices
    # add_devices([MagicBlueLight(hass, bulb, bulb_name, hci_device_id)])
    add_devices([MagicBlueLight(hass, bulb_name, hci_device_id)])


def hsv_to_rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b

def color_hsv_to_rgb(iH, iS, iV):
    """Convert an hsv color into its rgb representation.
    Hue is scaled 0-360
    Sat is scaled 0-100
    Val is scaled 0-100
    """
    fRGB = colorsys.hsv_to_rgb(iH / 360, iS / 100, iV / 100)
    return (int(fRGB[0] * 255), int(fRGB[1] * 255), int(fRGB[2] * 255))

class Connection(Light):
    """The connection"""
    def __init__(self):
        print("\n\nInitialzied class\n\n")
        self._state = False
        self._characteristic = None

    def bail(self):
        self._characteristic = None

    def connect(self):
        if self._characteristic is not None:
            print("Already connected :)")
            return

        try:
            print("Connecting to light strip...")
            service = btle.UUID("ffd5")
            dev = btle.Peripheral("ff:ff:bc:00:2b:09")

            for svc in dev.services:
                print(str(svc))
            svc = dev.getServiceByUUID(service)
            self._characteristic = svc.getCharacteristics()[0]
            print("Connected!")
        except Exception as ex:
            print("Could not get connect to device");
            self._characteristic = None
            self.bail();
            _LOGGER.debug("%s._update_blocking(): Exception during update status: %s", self, ex)

    def turn_on(self):
        print("\nASKED: To turn on")
        self.connect()
        try:
            self._write([-52, 35, 51])
            self._state = True
            print("_write finished")
        except Exception as ex:
            print("ERROR: turing on!!")
            print(ex)
            self.bail();

    def turn_off(self):
        print("\nASKED: To turn off")
        self.connect()
        try:
            self._write([-52, 36, 51])
            self._state = False
            print("_write finished")
        except Exception as ex:
            print("ERROR: turing off!!")
            print(ex)
            self.bail();

    def set_color(self, rgb_color):
        print("\nASKED: To set color")
        self.connect()
        try:
            data = self._encode_color(*rgb_color)
            self._write(data)
            print("_write finished")
        except Exception as ex:
            print("ERROR: setting color!!")
            print(ex)
            self.bail();

    def set_effect(self, effect, effect_speed):
        print("\nASKED: To set color")
        print(effect)
        self.connect()
        try:
            data = self._encode_effect(effect)
            self._write(data)
            print("_write finished")
        except Exception as ex:
            print("ERROR: setting effect!!")
            print(ex)
            self.bail();

    def _encode_color(self, red, green, blue):
        print("Creating a rgb here")
        print(red)
        print(green)
        print(blue)
        return [86, red, green, blue, 100, -16, -86]

    def _encode_effect(self, effect):
        print("Creating a effect here")
        return [-69, effect, 10, 68]

    def set_random_color(self):
        self.set_color([random.randint(1, 255) for i in range(3)])

    def is_on(self):
        return self._state

    def _write(self, message):
        data = bytearray([x % 256 for x in message])
        self._characteristic.write(data, False)
        print("\nWrote the data via class IT SHOULD HAVE CHANGED\n")



class MagicBlueLight(Light):
    """Representation of an MagicBlue Light."""
    # def __init__(self, hass, light, name):
    def __init__(self, hass, name, hci_device_id):
        """Initialize an MagicBlueLight."""
        print("Loading the effect")
        # from magicblue import Effect

        light = Connection()

        self.hass = hass
        self._light = light
        self._name = name
        self._state = False
        self._rgb = (255, 255, 255)
        self._brightness = 100
        self._available = True
        self._effects = []
        self._effects = [e for e in Effect.__members__.keys()]
        self._hci_device_id = hci_device_id
        print("\n\nTrying to connect\n\n")

        try:
            print("Initialized") 
        except Exception as ex:
            print("\n\n\nFAILED TO INITIALIZE\n\n\n");
            print(ex)
            _LOGGER.debug("%s._update_blocking(): Exception during update status: %s", self, ex)
            self._available = False
        return

    @property
    def name(self):
        """Return the display name of this light."""
        return self._name

    @property
    def rgb_color(self):
        """Return the RBG color value."""
        return self._rgb

    @property
    def brightness(self):
        """Return the brightness of the light (an integer in the range 1-255)."""
        return self._brightness

    @property
    def is_on(self):
        """Return true if light is on."""
        return self._state

    @property
    def supported_features(self):
        """Return the supported features."""
        return SUPPORT_COLOR | SUPPORT_EFFECT
        # return SUPPORT_BRIGHTNESS | SUPPORT_COLOR | SUPPORT_EFFECT

    @property
    def effect_list(self):
        """Return the list of supported effects."""
        return self._effects

    @property
    def available(self):
        print("Asked available!!")
        print(self._available)
        return self._available

    def update(self):
        _LOGGER.debug("%s.update()", self)
        self.hass.add_job(self._update_blocking)

    @comm_lock(False)
    def _update_blocking(self):
        _LOGGER.debug("%s._update_blocking()", self)
        print("_update_blocking")
        try:
            # if not self._light.test_connection():
                # self._light.connect(self._hci_device_id)
            # device_info = self._light.get_device_info()
            # self._state = False
            # self._rgb = (device_info['r'], device_info['g'], device_info['b'])
            self._rgb = (0, 255, 0)
            self._brightness = 100 # device_info['brightness']
            self._effect = None
            self._available = True
            print("Set is available")
        except Exception as ex:
            print("\n\nTHERE IS A PROBLEM\n\n\n");
            _LOGGER.debug("%s._update_blocking(): Exception during update status: %s", self, ex)
            self._available = False

    @comm_lock()
    def turn_on(self, **kwargs):
        """Instruct the light to turn on."""
        print("\nAsked light to turn on by homeassistant")
        # from magicblue import Effect
        _LOGGER.debug("%s.turn_on()", self)


        print(kwargs)
        # if ATTR_BRIGHTNESS in kwargs:
        if "brightness" in kwargs:
            print("Set brightness ")
            # self._rgb = (255, 255, 255)
            self._brightness = kwargs[ATTR_BRIGHTNESS]
            # self._light.set_warm_light(self._brightness / 255)

        # if "brightness_pct" in kwargs:
        #     self._rgb = (255, 255, 255)
        #     self._brightness = kwargs[ATTR_BRIGHTNESS]
        #     self._light.set_color(self._rgb)
        #     # self._light.set_warm_light(self._brightness / 255)

        # if "rgb_color" in kwargs:
        #     self._rgb = kwargs["rgb_color"]
        #     # self._light.set_warm_light(self._brightness / 255)
        #     self._light.set_color(self._rgb)
        #     print("Set rgb color")

        if ATTR_EFFECT in kwargs:
            self._effect = kwargs[ATTR_EFFECT]
            self._light.set_effect(Effect[kwargs[ATTR_EFFECT]].value, 10)
            # self._light.set_effect(37, 10)

        if "hs_color" in kwargs:
            print("Color property in turn on args")
            hue, saturation = kwargs["hs_color"]
            # self._rgb = hsv_io_igb(hue, saturation, 255)
            self._rgb = color_hsv_to_rgb(hue, saturation, self._brightness)

            red, green, blue = self._rgb

            print(self._rgb)
            self._brightness = 100
            print("\n\nTried to set a colour\n\n")
            print(self._rgb)
            self._light.set_color(self._rgb)


        self._light.turn_on()
        self._state = self._light.is_on()

        print("Real is on value reported as")
        print(self._state)
        return

        # if not self._light.test_connection():
        #     try:
        #         self._light.connect(self._hci_device_id)
        #     except Exception as e:
        #         _LOGGER.error('%s.turn_on(): Could not connect to %s', self, self._light)
        #         return

        # if not self._state:
        #     self._light.turn_on()

        # if ATTR_RGB_COLOR in kwargs:
        #     self._rgb = kwargs[ATTR_RGB_COLOR]
        #     self._brightness = 255
        #     self._light.set_color(self._rgb)


        # self._state = True

    @comm_lock()
    def turn_off(self, **kwargs):
        """Instruct the light to turn off."""
        print("\n\nTurn it off")
        self._light.turn_off()
        self._state = self._light.is_on()
        print('Set state to')
        print(self._light.is_on())
        return


        _LOGGER.debug("%s: MagicBlueLight.turn_off()", self)
        if not self._light.test_connection():
            try:
                self._light.connect(self._hci_device_id)
            except Exception as e:
                _LOGGER.error('%s.turn_off(): Could not connect to %s', self, self._light)
                return

        self._light.turn_off()
        self._state = False

    def __str__(self):
        return "<MagicBlueLight('{}', '{}')>".format(self._light, self._name)

    def __repr__(self):
        return "<MagicBlueLight('{}', '{}')>".format(self._light, self._name)
# endregion

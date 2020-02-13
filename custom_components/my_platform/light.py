import logging
import datetime

from .bulb.triones import Triones
from .const import ( debug, DOMAIN )
from homeassistant.const import (CONF_NAME, CONF_MAC, STATE_ON, STATE_OFF)
from homeassistant.components.light import (
    DOMAIN as LIGHT_DOMAIN,
    ATTR_BRIGHTNESS, ATTR_RGB_COLOR, ATTR_EFFECT,
    SUPPORT_COLOR, SUPPORT_BRIGHTNESS, SUPPORT_EFFECT,
    Light, PLATFORM_SCHEMA
)

SCAN_INTERVAL = datetime.timedelta(seconds=30)
_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up entry."""
    config = hass.data[DOMAIN]

    entities = []
    for each in config:
        entities.append(
            Triones(
                hass,
                config_entry,
                each
            )
        )

    async_add_entities(entities)
    return True

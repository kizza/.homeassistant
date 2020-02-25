import logging
import datetime

from .bulb.triones import Triones
from .const import ( debug, DOMAIN )
from .services import ( register_theme_service, register_flash_service, register_effect_service )

SCAN_INTERVAL = datetime.timedelta(seconds=30)
_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up entry."""
    config = hass.data[DOMAIN]

    # Add entities
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

    register_flash_service(hass, entities)
    register_theme_service(hass, entities)
    register_effect_service(hass, entities)

    return True


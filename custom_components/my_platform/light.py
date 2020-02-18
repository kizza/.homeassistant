import logging
import datetime

from .bulb.triones import Triones
from .const import ( debug, DOMAIN )
from homeassistant.const import (ATTR_ENTITY_ID, CONF_NAME, CONF_MAC, STATE_ON, STATE_OFF)
from homeassistant.components.light import (
    DOMAIN as LIGHT_DOMAIN,
    ATTR_BRIGHTNESS, ATTR_RGB_COLOR, ATTR_EFFECT,
    SUPPORT_COLOR, SUPPORT_BRIGHTNESS, SUPPORT_EFFECT,
    Light, PLATFORM_SCHEMA
)
from homeassistant.util import slugify
import homeassistant.helpers.config_validation as cv

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

    return True

def find_entity(entities, entity_id):
    for entity in entities:
        if entity_id == f'{LIGHT_DOMAIN}.{slugify(entity.name)}':
            return entity
    return None

def register_flash_service(hass, entities):
    """Add "flash" service"""

    async def async_handle_light_flash_service(service):
        params = service.data.copy()
        entity_id = service.data.get(ATTR_ENTITY_ID)
        entity = find_entity(entities, entity_id)
        await entity.flash()

    hass.services.async_register(
        DOMAIN,
        "flash",
        async_handle_light_flash_service,
        # schema=cv.make_entity_service_schema(LIGHT_TURN_ON_SCHEMA),
    )

def register_theme_service(hass, entities):
    """Add "theme" service"""

    async def async_handle_light_theme_service(service):
        params = service.data.copy()
        entity_id = service.data.get(ATTR_ENTITY_ID)
        rgb = service.data.get(ATTR_RGB_COLOR)
        for entity in entities:
            await entity.theme(tuple(rgb))

    hass.services.async_register(
        DOMAIN,
        "theme",
        async_handle_light_theme_service,
        # schema=cv.make_entity_service_schema(LIGHT_TURN_ON_SCHEMA),
    )

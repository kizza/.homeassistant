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


    async def async_handle_light_flash_service(service):
        params = service.data.copy()
        data_ent_id = service.data.get(ATTR_ENTITY_ID)
        for entity in entities:
            entity_name = f'{LIGHT_DOMAIN}.{slugify(entity.name)}'
            if entity_name == data_ent_id:
                await entity.do_custom_thing()

    # Listen for light on and light off service calls.
    hass.services.async_register(
        DOMAIN,
        "flash",
        async_handle_light_flash_service,
        # schema=cv.make_entity_service_schema(LIGHT_TURN_ON_SCHEMA),
    )

    return True

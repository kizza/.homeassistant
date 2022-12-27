import logging

from ..const import ( debug, DOMAIN )
from ..util.hass import ( find_entity )
from homeassistant.const import ( ATTR_ENTITY_ID )

_LOGGER = logging.getLogger(__name__)

def register_flash_service(hass, entities):
    """Add "flash" service"""

    async def async_handle_light_flash_service(service):
        params = service.data.copy()
        entity_id = service.data.get(ATTR_ENTITY_ID)
        entity = find_entity(entities, entity_id)
        if entity:
            await entity.flash()
        else:
            print("No 'flash', just a string entity")

    hass.services.async_register(
        DOMAIN,
        "flash",
        async_handle_light_flash_service,
        # schema=cv.make_entity_service_schema(LIGHT_TURN_ON_SCHEMA),
    )

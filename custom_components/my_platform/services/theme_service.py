import logging

from ..const import ( debug, DOMAIN )
from ..util.hass import ( find_entity )
from ..util.effects import ( update_mood_state )
from homeassistant.const import ( ATTR_ENTITY_ID )
from homeassistant.components.light import ( ATTR_RGB_COLOR )

_LOGGER = logging.getLogger(__name__)

def register_theme_service(hass, entities):
    """Add "theme" service"""

    async def async_handle_light_theme_service(service):
        params = service.data.copy()
        entity_id = service.data.get(ATTR_ENTITY_ID)
        rgb = params.get(ATTR_RGB_COLOR)
        _LOGGER.debug("Running theme %s", rgb)
        update_mood_state(hass, rgb)
        for entity in entities:
            await entity.theme(rgb)

    hass.services.async_register(
        DOMAIN,
        "theme",
        async_handle_light_theme_service,
        # schema=cv.make_entity_service_schema(LIGHT_TURN_ON_SCHEMA),
    )

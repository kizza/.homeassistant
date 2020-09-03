import logging

from ..const import ( debug, DOMAIN )
from ..util.hass import ( find_entity )
from ..util.effects import ( colour, colour_from_index, include_in_effects, update_mood_state )
from homeassistant.const import ( ATTR_ENTITY_ID )
from homeassistant.components.light import ( ATTR_BRIGHTNESS, ATTR_RGB_COLOR )

_LOGGER = logging.getLogger(__name__)
ATTR_COLOUR_INDEX = "colour_index"

def register_theme_service(hass, entities):
    """Add "theme" service"""

    def is_custom_version(entity):
        return hasattr(entity, 'theme')

    async def async_set_colour(entity, rgb):
        if is_custom_version(entity):
            await entity.theme(rgb)
        else:
            def _call_theme_service_job(hass):
                service_data = { ATTR_RGB_COLOR: colour(rgb), ATTR_BRIGHTNESS: 255, ATTR_ENTITY_ID: entity }
                hass.services.call('light', 'turn_on', service_data, False)

            await hass.async_add_job(_call_theme_service_job, hass)

    def entity_is_included(entity):
        if is_custom_version(entity):
            return include_in_effects(hass, entity.name)
        else:
            return include_in_effects(hass, entity.replace("light.", ""))

    async def async_handle_light_theme_service(service):
        params = service.data.copy()
        entity_id = service.data.get(ATTR_ENTITY_ID)
        colour_index = service.data.get(ATTR_COLOUR_INDEX)
        rgb = params.get(ATTR_RGB_COLOR)
        _LOGGER.debug("Running theme rgb %s, index %s", rgb, colour_index)

        # Number of steps
        steps_state = hass.states.get('input_number.effect_transition_steps')
        fade_steps = int(float(steps_state.state))

        # Set a default rgb from index (if present) and update "mood" text
        if not colour_index is None:
            rgb = colour_from_index(hass, colour_index)
        update_mood_state(hass, rgb)

        # Stagger the colours across lights? (offset on the colour index)
        offset_colours_state = hass.states.get('input_boolean.effect_offset_colours').state == 'on'

        included_entities = filter(entity_is_included, entities)
        for index, entity in enumerate(included_entities):
            if not colour_index is None:
                # fade_steps = int(float(steps_state.state))
                each_colour_index = colour_index
                # if offset_colours_state:
                #     offset_band = index * (fade_steps)
                #     each_colour_index = colour_index + offset_band

                rgb = colour_from_index(hass, each_colour_index)

                # _LOGGER.debug("Now the colour is! original:%s banded:%s rgb:%s", colour_index, each_colour_index, rgb)
            await async_set_colour(entity, rgb)


    hass.services.async_register(
        DOMAIN,
        "theme",
        async_handle_light_theme_service,
        # schema=cv.make_entity_service_schema(LIGHT_TURN_ON_SCHEMA),
    )

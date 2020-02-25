import logging

from ..const import ( debug, DOMAIN )
from ..util.hass import ( find_entity )
from ..util.effects import ( configured_colours )
from homeassistant.helpers.event import async_call_later

_LOGGER = logging.getLogger(__name__)
EFFECT_KEY = 'fade_effect'

def register_effect_service(hass, entities):
    def schedule_update_effect_running_state():
        def _update_effect_running_state():
            value = 'on' if EFFECT_KEY in hass.data else 'off'
            hass.states.set('input_boolean.effect_running', value)
        hass.add_job(_update_effect_running_state)

    async def start_effect():
        if EFFECT_KEY in hass.data:
            await hass.data[EFFECT_KEY].run()

    def stop_effect():
        if EFFECT_KEY in hass.data:
            hass.data[EFFECT_KEY].stop()
            del hass.data[EFFECT_KEY]

    async def async_handle_light_effect_start_service(service):
        params = service.data.copy()
        colours = service.data.get("colours")
        delay = service.data.get("delay")

        # if colours == 'auto':
        #     colours = configured_colours(hass)

        stop_effect()
        hass.data[EFFECT_KEY] = FadeEffect(hass, entities, colours, delay)
        await start_effect()
        schedule_update_effect_running_state()

    async def async_handle_light_effect_stop_service(service):
        stop_effect()
        schedule_update_effect_running_state()

    hass.services.async_register(
        DOMAIN,
        "start_effect",
        async_handle_light_effect_start_service,
        # schema=cv.make_entity_service_schema(LIGHT_TURN_ON_SCHEMA),
    )

    hass.services.async_register(
        DOMAIN,
        "stop_effect",
        async_handle_light_effect_stop_service,
        # schema=cv.make_entity_service_schema(LIGHT_TURN_ON_SCHEMA),
    )

class FadeEffect():
    def __init__(self, hass, entities, colours, delay):
        self.hass = hass
        self.entities = entities
        self._colours = colours
        self.delay = delay
        self.index = 0
        self._cancel_next = None
        _LOGGER.debug("Started effect service with colours %s every %s", self.colours, self.delay)

    async def run(self, now = None):
        rgb = self._get_next_colour()
        _LOGGER.debug("Running effect %s", rgb)
        for entity in self.entities:
            await entity.theme(rgb)
        self._schedule_next()

    def stop(self):
        if self._cancel_next is not None:
            _LOGGER.debug("Cancelling effect service")
            self._cancel_next()
        self._cancel_next = None

    @property
    def colours(self):
        if self._colours:
            return self._colours
        else:
            return configured_colours(self.hass)

    def _get_next_colour(self):
        colours = self.colours
        if self.index >= len(self.colours):
            self.index = 0
        rgb = self.colours[self.index]
        self.index += 1
        return rgb

    def _schedule_next(self):
        self._cancel_next = async_call_later(
            self.hass, self.delay, self.run
        )

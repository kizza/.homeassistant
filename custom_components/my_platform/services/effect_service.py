import logging
import math

from ..const import ( debug, DOMAIN )
from ..util.hass import ( find_entity )
from ..util.effects import ( full_colour_spectrum, spectrum, update_mood_state )
from .theme_service import ( ATTR_COLOUR_INDEX )
from homeassistant.components.light import ( ATTR_RGB_COLOR )
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
        fade_steps = service.data.get("fade_steps")

        # Get delay from state field
        delay_state = hass.states.get('input_number.effect_delay')
        delay = int(float(delay_state.state))

        # Get fade steps from state field
        steps_state = hass.states.get('input_number.effect_transition_steps')
        fade_steps = int(float(steps_state.state))

        stop_effect()
        hass.data[EFFECT_KEY] = FadeEffect(hass, entities, colours, fade_steps, delay)
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
    def __init__(self, hass, entities, colours, fade_steps, delay):
        self.hass = hass
        self.entities = entities
        self._colours = colours
        self.fade_steps = fade_steps
        self.delay = delay
        self.index = 0
        self._cancel_next = None
        _LOGGER.debug("Started effect service with colours %s faded at %s every %s", self.colours, self.fade_steps, self.delay)

    async def run(self, now = None):
        # rgb = self._get_next_colour()
        # _LOGGER.debug("Running effect %s", rgb)
        self._call_theme_service()
        self._schedule_next()

    def stop(self):
        if self._cancel_next is not None:
            _LOGGER.debug("Cancelling effect service")
            self._cancel_next()
        self._cancel_next = None

    @property
    def colours(self):
        if self._colours:
            output = self._colours
        else:
            # output = configured_colours(self.hass)
            output = full_colour_spectrum(self.hass)
        return output
        # return self._apply_colour_fades(output)

    def _call_theme_service(self):
        """Call 'theme' service and pass in current running index!"""
        def _call_theme_service_job(hass):
            running_index = self.hass.states.get('input_number.effect_index_key')
            if running_index:
                # Run theme with this index
                running_index_int = int(float(running_index.state))
                service_data = { ATTR_COLOUR_INDEX: running_index_int }
                hass.services.call(DOMAIN, 'theme', service_data, False)
                # Update the index
                self._set_new_global_effect_index(running_index_int)
            else:
                _LOGGER.error("No effect index key found")

        self.hass.add_job(_call_theme_service_job, self.hass)

    def _apply_colour_fades(self, colours):
        if self.fade_steps is not None:
            colours = spectrum(colours, self.fade_steps)
            return colours
        else:
            return colours

    def _set_new_global_effect_index(self, current_index):
        all_colours = self.colours
        print("Getting all colours", len(all_colours))
        print(all_colours)
        if current_index >= len(all_colours):
            next_index = 0
        else:
            next_index = current_index + 1
        self.hass.states.set('input_number.effect_index_key', next_index)


    # def _get_next_colour(self):
    #     all_colours = self.colours
    #     print("Getting all colours")
    #     print(all_colours)
    #     if self.index >= len(all_colours):
    #         self.index = 0
    #     rgb = all_colours[self.index]
    #     self.index += 1
    #     return rgb

    def _schedule_next(self):
        self._cancel_next = async_call_later(
            self.hass, self.delay, self.run
        )

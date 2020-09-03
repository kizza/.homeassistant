"""My Platform"""

import logging
import voluptuous as vol

from .const import ( debug, DOMAIN )
from homeassistant.const import ( CONF_NAME, CONF_TYPE, CONF_MAC )
from homeassistant.config_entries import SOURCE_IMPORT
from homeassistant.helpers import config_validation as cv
from homeassistant.components.light import DOMAIN as LIGHT_DOMAIN

from .util.effects import ( full_colour_spectrum, map_to_colour )
# Websocket
from homeassistant.components import websocket_api
from homeassistant.exceptions import HomeAssistantError
from homeassistant.core import callback


_LOGGER = logging.getLogger(__name__)

INTERFACE_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_NAME): cv.string,
        vol.Required(CONF_MAC): cv.string,
        vol.Required(CONF_TYPE): cv.string
    }
)

CONFIG_SCHEMA = vol.Schema(
    {DOMAIN: vol.Schema(vol.All(cv.ensure_list, [INTERFACE_SCHEMA]))},
    extra=vol.ALLOW_EXTRA,
)

async def async_setup(hass, hass_config):
    """Set up the component."""
    config = hass_config.get(DOMAIN)
    if config is not None:
        # Put config into data for later setup
        hass.data[DOMAIN] = config or {}

        # Create a config entry
        hass.async_create_task(
            hass.config_entries.flow.async_init(
                DOMAIN,
                context={"source": SOURCE_IMPORT},
                data={"unique_id": "this is my unique id"},
            )
        )

    # GET_SPECTRUM = 'lovelace/colours'
    # GET_SPECTRUM_SCHEMA = websocket_api.BASE_COMMAND_MESSAGE_SCHEMA.extend({
    #     vol.Required('type')
    #     # vol.Any(WS_TYPE_GET_LOVELACE_UI, OLD_WS_TYPE_GET_LOVELACE_UI),
    # })


    hass.components.websocket_api.async_register_command(
        websocket_lovelace_config
    )
        # GET_SPECTRUM, websocket_lovelace_config,
        # GET_SPECTRUM_SCHEMA)

    return True

# @websocket_api.async_response
@callback
@websocket_api.websocket_command({"type": "lovelace/colours"})
def websocket_lovelace_config(hass, connection, msg):
    """Send lovelace UI config over websocket config."""
    mapped_colours = map_to_colour(full_colour_spectrum(hass))
    message = websocket_api.result_message(
        msg['id'], mapped_colours
    )
    connection.send_message(message)
    # connection.send_message_outside(message)
    # connection.send_message(websocket_api.result_message(msg["id"], panels))
    return
    # error = None
    # try:
    #     config = await hass.async_add_job(
    #         load_yaml, hass.config.path('ui-lovelace.yaml'))
    #     message = websocket_api.result_message(
    #         msg['id'], config
    #     )
    # except FileNotFoundError:
    #     error = ('file_not_found',
    #                 'Could not find ui-lovelace.yaml in your config dir.')
    # except HomeAssistantError as err:
    #     error = 'load_error', str(err)

    # if error is not None:
    #     message = websocket_api.error_message(msg['id'], *error)

    # connection.send_message_outside(message)

async def async_setup_entry(hass, entry):
    """Set up a config entry"""
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, LIGHT_DOMAIN)
    )
    return True


async def async_unload_entry(hass, entry):
    """Unload a config entry."""
    await hass.config_entries.async_forward_entry_unload(entry, LIGHT_DOMAIN)
    return True

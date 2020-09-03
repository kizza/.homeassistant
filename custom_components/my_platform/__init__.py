"""My Platform"""

import logging
import voluptuous as vol

from .const import ( debug, DOMAIN )
from homeassistant.const import ( CONF_NAME, CONF_TYPE, CONF_MAC )
from homeassistant.config_entries import SOURCE_IMPORT
from homeassistant.helpers import config_validation as cv
from homeassistant.components.light import DOMAIN as LIGHT_DOMAIN

from .websocket import websocket_effect_colours

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

    # Setup webhook
    hass.components.websocket_api.async_register_command(
        websocket_effect_colours
    )

    return True


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

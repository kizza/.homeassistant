from .const import ( debug, DOMAIN )
from homeassistant import config_entries
from homeassistant.helpers import config_entry_flow

async def _async_has_devices(hass):
    """Return if there are devices that can be discovered."""
    return True

config_entry_flow.register_discovery_flow(
    DOMAIN, "This is my integration title", _async_has_devices, config_entries.CONN_CLASS_LOCAL_POLL
)

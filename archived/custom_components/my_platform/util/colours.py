from functools import reduce

from homeassistant.components.lovelace.const import DOMAIN as LOVELACE_DOMAIN

def _extract_colours(container):
    if 'cards' in container:
        colours = container['cards']

        def is_colour_input_boolean(card):
            return card['entity'].startswith("input_boolean.colour_")
        colour_input_booleans = list(filter(is_colour_input_boolean, container['cards']))

        def colour_from_input_boolean(card):
            return card['entity'].replace("input_boolean.colour_", "")
        colour_strings = list(map(colour_from_input_boolean, colour_input_booleans))

        return colour_strings
    return []

def colours_from_lovelace(hass):
    flat_map = lambda f, xs: reduce(lambda a, b: a + b, map(f, xs))

    dashboards = hass.data[LOVELACE_DOMAIN]['dashboards']
    if dashboards:
        dashboard_keys = filter(lambda key: key is not None, dashboards.keys())
        views = list(flat_map(lambda key: dashboards[key]._data['config']['views'],dashboard_keys))
        view_cards = list(flat_map(lambda view: view['cards'], views))
        horizontal_stacks = list(filter(lambda view_card: view_card['type'] == 'horizontal-stack', view_cards))
        colours = list(flat_map(lambda stack: _extract_colours(stack), horizontal_stacks))
        return colours
    return []

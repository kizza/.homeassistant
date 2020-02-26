from homeassistant.util import slugify
from homeassistant.components.light import DOMAIN as LIGHT_DOMAIN

# e = hass.data[DOMAIN]
# for each in e:
#     print(each)
# e = hass.data[LIGHT_DOMAIN]
# print(e.get_entity(f'{LIGHT_DOMAIN}.tv_backlight'))

def find_entity(entities, entity_id):
    for entity in entities:
        if entity_id == f'{LIGHT_DOMAIN}.{slugify(entity.name)}':
            return entity
    return None

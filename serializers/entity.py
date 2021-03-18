import json
from xml.dom.minidom import Entity

from domain.Entity import Entity

class EntityJsonEncoder(json.JSONEncoder):

    def default(self, o: Entity):
        try:
            to_serialize = {
                "dni" : o.dni,
                "name": o.name,
                "price": o.price
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
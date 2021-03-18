import json
from domain.deal import  Deal


class DealJSONSerializer(json.JSONEncoder):

    def default(self, o: Deal):
        try:
            serial = {
                'id': o.id,
                'name': o.name,
                'stage': o.stage,
                'close_date': o.close_date,
                'amount': o.amount,
                'deal_type': o.deal_type
            }
            return serial
        except AttributeError:
            return  super().default(o)

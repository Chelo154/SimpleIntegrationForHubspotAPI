from mongoengine import *
from interfaces.iparseable import IParseable
from domain.deal import Deal


class DealEntity(Document):

    id = UUIDField('id')
    name = StringField('name')
    stage = StringField('stage')
    close_date = StringField('close_date')
    amount = FloatField('amount')
    deal_type = StringField('deal_type')
    meta = {'collection': 'deals'}

    def parse(self):
        return Deal.from_dict(dict=self.to_mongo())
        pass


pass

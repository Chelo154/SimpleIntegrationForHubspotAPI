from mongoengine import *
from interfaces.iparseable import IParseable
from domain.deal import Deal


class DealEntity(Document, IParseable):

    id = UUIDField('id')
    name = StringField('name')
    stage = StringField('stage')
    closeDate = StringField('close_date')
    amount = FloatField('amount')
    dealType = StringField('deal_type')

    def parse(self):
        return Deal.from_dict(dict=self.to_mongo())
        pass


pass

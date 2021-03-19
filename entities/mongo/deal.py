from mongoengine import *
from interfaces.iparseable import IParseable
from domain.deal import Deal


class DealEntity(Document):

    identifier = IntField(unique=True)
    name = StringField()
    stage = StringField()
    close_date = StringField()
    amount = FloatField()
    deal_type = StringField()
    username = StringField()
    meta = {'collection': 'deals'}

    def parse(self):
        return Deal.from_dict(dict=self.to_mongo())
        pass


pass

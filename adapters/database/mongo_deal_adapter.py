from mongoengine import connect,disconnect
from entities.mongo.deal import DealEntity
from interfaces.irepository import IRepository
from domain.deal import Deal
from adapters.database.mongo_config import *


class MongoDealAdapter(IRepository):

    def connect(self):
        connect(
            db=MONGO_DB,
            username=MONGO_USER,
            password=MONGO_PASS,
            host=MONGO_HOST,
        )

    def insert(self, data):
        pass

    def insert_many(self, data_collection: [Deal]):
        self.connect()

        for data in data_collection:
            deal = DealEntity(
                id= data.id,
                name=data.name,
                stage=data.stage,
                close_date=data.close_date,
                amount=float(data.amount),
                deal_type=data.deal_type
            )
            print(deal.amount)
            deal.save()

        disconnect()

    def get_all(self):
        self.connect()

        data_rows = DealEntity.objects
        deals = list()

        for data in data_rows:
            deals.append(data_rows.parse())

        disconnect()
        return deals

    def get_one(self, identifier):
        pass

    def update(self, identifier, data):
        pass

    def delete(self, identifier, data):
        pass

    def __init__(self):
        pass



pass

from mongoengine import  connect
from adapters.database.mongo_config import  URI
from interfaces.irepository import  IRepository


class MongoDealAdapter(IRepository):

    def insert(self, data):
        pass

    def get(self):
        pass

    def update(self, identifier, data):
        pass

    def delete(self, identifier, data):
        pass

    def __init__(self):
        pass


pass

from mongoengine import connect
from interfaces.irepository import IRepository
from adapters.database.mongo_config import URI


class MongoUserAdapter(IRepository):

    def __init__(self):
        pass

    def insert(self, data):
        connect(URI)

    def get(self):
        pass

    def update(self, identifier, data):
        pass

    def delete(self, identifier, data):
        pass


pass

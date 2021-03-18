from mongoengine import connect,disconnect
from interfaces.irepository import IRepository
from adapters.database.mongo_config import URI
from domain.user import User
from entities.mongo.user import UserEntity


class MongoUserAdapter(IRepository):

    def __init__(self):
        pass

    def insert(self, data: User):
        connect(
            db='hubspot-api',
            username='chelo',
            password='chelo',
            host='mongodb+srv://chelo:chelo@cluster0.pswx4.mongodb.net/hubspot-api',

        )

        data_row = UserEntity(
            code=data.code,
            access_token=data.access_token,
            refresh_token=data.refresh_token
        )

        data_row.save()

        disconnect()

        return True

    def get(self):
        pass

    def update(self, identifier, data):
        pass

    def delete(self, identifier, data):
        pass


pass

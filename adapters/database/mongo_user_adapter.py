from mongoengine import connect,disconnect,ConnectionFailure
from interfaces.irepository import IRepository
from adapters.database.mongo_config import *
from domain.user import User
from entities.mongo.user import UserEntity


class MongoUserAdapter(IRepository):

    def __init__(self):
        pass

    def connect(self):
        connect(
            db=MONGO_DB,
            username=MONGO_USER,
            password=MONGO_PASS,
            host=MONGO_HOST,

        )

    def insert(self, data: User):
        self.connect()

        data_row = UserEntity(
            code=data.code,
            username = data.username,
            access_token=data.access_token,
            refresh_token=data.refresh_token
        )

        if self.exists(data.username):
            print("USER ALREADY EXIST -- UPDATING TOKENS")

            user = self.get_one(data.username)
            user.update(access_token=data.access_token, refresh_token=data.refresh_token)

            print("SUCCESSFUL UPDATE")

        else:
            data_row.save()

        disconnect()

        return True

    def get_all(self):
        pass

    def update(self, identifier, data):
        pass

    def delete(self, identifier, data):
        pass

    def insert_many(self, data_collection):
        pass

    def exists(self, username):
        number = self.get_one(username)
        return number != None

    def get_one(self, identifier):
        try:
            user = UserEntity.objects(username__exact=identifier)
            user = user[0].parse()
            return user
        except ConnectionFailure:
            self.connect()
            user = UserEntity.objects(username__exact=identifier)
            user = user[0].parse()
            disconnect()
            return user



pass


from mongoengine import *
from interfaces.iparseable import IParseable
from domain.user import User


class UserEntity(Document):

    code = StringField(unique=True)
    access_token = StringField()
    refresh_token = StringField()
    meta = {'collection': 'users'}

    def parse(self):
        return User.from_dict(self.to_mongo())


pass

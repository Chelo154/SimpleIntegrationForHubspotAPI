from mongoengine import *
from interfaces.iparseable import IParseable
from domain.user import User


class UserEntity(Document):

    code = StringField(unique=True)
    username = StringField(unique=True)
    access_token = StringField()
    refresh_token = StringField()
    meta = {'collection': 'users'}

    def parse(self):
        dictionary ={
            "code": self.code,
            "username": self.username,
            "access_token": self.access_token,
            "refresh_token": self.refresh_token
        }
        return User.from_dict(dictionary)


pass

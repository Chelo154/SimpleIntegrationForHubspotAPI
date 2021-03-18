import json
from domain.user import User


class UserJsonEncoder(json.JSONEncoder):

    def default(self, o: User):
        try:
            serial = {
                "code" : o.code,
                "access_token" : o.access_token,
                "refresh_token" : o.refresh_token
            }
            return serial
        except AttributeError:
            return super().default(o)


pass

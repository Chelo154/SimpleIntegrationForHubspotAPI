import dataclasses


@dataclasses.dataclass()
class User:

    code : str
    access_token : str
    refresh_token : str

    def __init__(self,code,access_token,refresh_token):
        self.code = code
        self.access_token = access_token
        self.refresh_token = refresh_token

    @classmethod
    def from_dict(self,dict):
        return self(**dict)

    def to_dict(self):
        return dataclasses.asdict(self)


pass

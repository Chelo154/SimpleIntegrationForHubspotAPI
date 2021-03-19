import abc
from domain.user import User

class IDealConnector(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_deals(self, user: User):
        pass


pass

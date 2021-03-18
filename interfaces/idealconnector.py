import abc


class IDealConnector(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_deals(self, access_token):
        pass


pass

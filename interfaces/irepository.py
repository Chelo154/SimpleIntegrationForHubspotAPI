import abc


class IRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def insert(self, data):
        pass

    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def update(self, identifier, data):
        pass

    @abc.abstractmethod
    def delete(self, identifier, data):
        pass


pass

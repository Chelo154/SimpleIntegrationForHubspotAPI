import abc


class IRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def insert(self, data):
        pass

    @abc.abstractmethod
    def insert_many(self, data_collection):
        pass

    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def get_one(self,identifier):
        pass

    @abc.abstractmethod
    def update(self, identifier, data):
        pass

    @abc.abstractmethod
    def delete(self, identifier, data):
        pass


pass

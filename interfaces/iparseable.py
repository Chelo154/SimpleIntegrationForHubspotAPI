import abc


class IParseable(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def parse(self):
        pass


pass

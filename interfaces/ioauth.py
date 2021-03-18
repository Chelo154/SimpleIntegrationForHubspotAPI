import abc


class IOAuth(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_oauth_url(self):
        pass

    @abc.abstractmethod
    def get_tokens(self):
        pass

    @abc.abstractmethod
    def refresh_token(self):
        pass


pass

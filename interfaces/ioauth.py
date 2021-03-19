import abc


class IOAuth(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_oauth_url(self):
        pass

    @abc.abstractmethod
    def get_tokens(self, code):
        pass

    @abc.abstractmethod
    def refresh_token(self,refresh_token):
        pass

    @abc.abstractmethod
    def get_username(self, access_token):
        pass

pass

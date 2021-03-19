from adapters.apiconnector.deal_api_connector import DealAPIConnector


class DealAPIHandler:

    api = DealAPIConnector()

    @staticmethod
    def get_api():
        return DealAPIHandler.api


pass


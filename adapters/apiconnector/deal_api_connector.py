from interfaces.idealconnector import IDealConnector
from domain.deal import Deal
from errors.access_token_error import AccessTokenError
import datetime
import requests


class DealAPIConnector(IDealConnector):

    def __init__(self):
        pass

    def get_deals(self, user):
        header = {
            'Authorization': 'Bearer {token}'.format(token=user.access_token)
        }

        properties = '?properties=dealname&properties=dealstage&properties=closedate&properties=amount&properties' \
                     '=dealtype '

        deals_url = 'https://api.hubapi.com/deals/v1/deal/paged/'

        response = requests.get(url=f'{deals_url}{properties}', headers=header)

        if response.status_code == 401:
            raise AccessTokenError()

        response = response.json()

        deals_data = response['deals']

        print(deals_data)

        deals = list()

        for item in deals_data:

            dictionary ={
                'id': int(item['dealId']),
                'user': user,
                'name': item['properties']['dealname']['value'],
                'stage': item['properties']['dealstage']['value'],
                'close_date': item['properties']['closedate']['value'],
                'amount': float(item['properties']['amount']['value']),
                'deal_type': item['properties']['dealtype']['value']
            }

            deal = Deal.from_dict(dictionary)

            deals.append(deal)

        return deals


pass

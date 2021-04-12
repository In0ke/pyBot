import requests


class RegruCloudApi:
    def __init__(self):
        self.url = 'https://api.cloudvps.reg.ru/v1/'

    def _request(self, route, method, user_token):
        current_url = self.url + route
        response = requests.request(method, current_url, headers=user_token)

        return response.json()

    def get_balance_data(self, user):
        route = 'balance_data'
        response = self._request(route, 'GET', user.token)


regru = RegruCloudApi()
regru.get_balance_data()

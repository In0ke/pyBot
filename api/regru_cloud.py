import requests

from api.api_contracts import APIContractGetBalance
from entities.user import User
from loguru import logger


class RegruCloudApi:
    def __init__(self):
        self.url = "https://api.cloudvps.reg.ru/v1/"

    def _request(self, route: str, method: str, user_token: dict):
        current_url = self.url + route
        logger.debug(f"Make {method} request to {current_url}, with token {user_token}")
        response = requests.request(method, current_url, headers=user_token)
        logger.debug(f"Response from api: {response.json()}")
        return response.json()

    def get_balance_data(self, user: User) -> APIContractGetBalance:
        route = "balance_data"
        response = self._request(route, "GET", user.get_api_token())
        return APIContractGetBalance.parse_obj(response["balance_data"])


cloud_api = RegruCloudApi()

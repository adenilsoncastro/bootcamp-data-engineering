from abc import ABC, abstractmethod
import datetime

import requests
from backoff import on_exception, expo
import ratelimit
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class MercadoBitcoinApi(ABC):
    def __init__(self, coin: str) -> None:
        self.coin = coin
        self.base_endpoint = 'https://www.mercadobitcoin.net/api'

    #
    # '_' na frente classifica o método como interno da classe
    #
    @abstractmethod
    def _get_endpoint(self, **kwargs) -> str:
        pass

    @on_exception(expo, ratelimit.RateLimitException, max_tries=10)
    @ratelimit.limits(calls=10, period=30)
    @on_exception(expo, requests.exceptions.HTTPError, max_tries=10)
    def get_data(self, **kwargs) -> dict:
        endpoint = self._get_endpoint(**kwargs)
        logger.info(f'getting data from {endpoint}')

        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()


class DaySummaryApi(MercadoBitcoinApi):
    type = 'day-summary'

    def _get_endpoint(self, date: datetime.date) -> str:
        return f'{self.base_endpoint}/{self.coin}/{self.type}/{date.year}/{date.month}/{date.day}'


# print(DaySummaryApi(coin='btc').get_data(date=datetime.date(2021, 7, 9)))


class TradesApi(MercadoBitcoinApi):
    type = 'trades'

    def _get_unix_epoch(self, date: datetime.datetime) -> int:
        return int(date.timestamp())

    def _get_endpoint(self, date_from: datetime.datetime = None, date_to: datetime.datetime = None) -> str:

        if date_from and not date_to:
            unix_date_from = self._get_unix_epoch(date_from)
            endpoint = f'{self.base_endpoint}/{self.coin}/{self.type}/{unix_date_from}'
        elif date_from and date_to:
            unix_date_from = self._get_unix_epoch(date_from)
            unix_date_to = self._get_unix_epoch(date_to)
            endpoint = f'{self.base_endpoint}/{self.coin}/{self.type}/{unix_date_from}/{unix_date_to}'
        else:
            endpoint = f'{self.base_endpoint}/{self.coin}/{self.type}'

        return endpoint

# print(TradesApi(coin='btc').get_data())
# print(TradesApi(coin='btc').get_data(date_from=datetime.datetime(2021, 7, 1)))
# print(TradesApi(coin='btc').get_data(date_from=datetime.datetime(
#    2021, 7, 1), date_to=datetime.datetime(2021, 7, 2)))

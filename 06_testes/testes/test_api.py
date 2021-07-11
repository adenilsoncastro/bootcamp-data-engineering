import datetime
import pytest

from apis import DaySummaryApi, TradesApi


class TestDaySummaryApi:
    @pytest.mark.parametrize(
        "coin, date, expected",
        [
            (
                "btc",
                datetime.date(2021, 6, 21),
                "https://www.mercadobitcoin.net/api/btc/day-summary/2021/6/21",
            ),
            (
                "eth",
                datetime.date(2021, 6, 21),
                "https://www.mercadobitcoin.net/api/eth/day-summary/2021/6/21",
            ),
            (
                "eth",
                datetime.date(2019, 3, 17),
                "https://www.mercadobitcoin.net/api/eth/day-summary/2019/3/17",
            ),
        ],
    )
    def test_get_endpoint_(self, coin, date, expected):
        api = DaySummaryApi(coin=coin)
        actual = api._get_endpoint(date=date)

        assert actual == expected


class TestTradesApi:
    @pytest.mark.parametrize(
        "coin, date_from, date_to, expected",
        [
            (
                "test",
                datetime.datetime(2019, 1, 1),
                datetime.datetime(2019, 1, 1),
                "https://www.mercadobitcoin.net/api/test/trades/1546308000/1546308000",
            ),
            (
                "test",
                None,
                None,
                "https://www.mercadobitcoin.net/api/test/trades",
            ),
            (
                "test",
                None,
                datetime.datetime(2019, 1, 1),
                "https://www.mercadobitcoin.net/api/test/trades",
            ),
            (
                "test",
                datetime.datetime(2019, 1, 1),
                None,
                "https://www.mercadobitcoin.net/api/test/trades/1546308000",
            ),
        ],
    )
    def test_get_endpoint_(self, coin, date_from, date_to, expected):
        actual = TradesApi(coin=coin)._get_endpoint(
            date_from=date_from, date_to=date_to
        )
        assert actual == expected

    def test_get_endpoint_date_from_greater_than_date_to(self):
        with pytest.raises(RuntimeError):
            TradesApi(coin="test")._get_endpoint(
                date_from=datetime.datetime(2021, 6, 15),
                date_to=datetime.datetime(2021, 6, 12),
            )

    @pytest.mark.parametrize(
        "date, expected",
        [(datetime.datetime(2019, 1, 1), 1546308000)],
    )
    def test_get_unix_epoch(self, date, expected):
        actual = TradesApi(coin="test")._get_unix_epoch(date)
        assert actual == expected

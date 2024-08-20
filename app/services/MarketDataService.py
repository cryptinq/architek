import requests

from core.exceptions.KernelException import KernelException
from core.kernel.services.classes.BaseService import BaseService


class MarketDataService(BaseService):

    PAIR_ID_MAP: dict[str, int] = {"USDT": 825, "USD": 2781, "USDC": 3408, "BTC": 1}

    DEFAULT_PAIR: str = "USDT"
    DEFAULT_LIMIT: int = 50
    ENDPOINT_URL: str = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest"

    def __init__(self): super().__init__()

    def fetch_data(self, slug: str, pair: str = DEFAULT_PAIR, limit: int = DEFAULT_LIMIT):

        if pair not in self.PAIR_ID_MAP.keys(): KernelException(
            "InvalidPairException",
            f"Invalid pair {pair}, need to be one of \"{self.PAIR_ID_MAP.keys()}\""
        )

        payload = {
            "slug": slug, "start": 1, "quoteCurrencyId": self.PAIR_ID_MAP[pair], "limit": limit,
            "category": "spot", "centerType": "cex", "sort": "cmc_rank_advanced",
            "direction": "desc", "spotUntracked": "true"
        }

        req = requests.get(self.ENDPOINT_URL, params=payload)

        return req.json()

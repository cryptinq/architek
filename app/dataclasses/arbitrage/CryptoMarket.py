from dataclasses import dataclass


@dataclass
class CryptoMarket:
    name: str
    slug: str
    base_symbol: str
    quote_symbol: str
    price: float
    update_time: str
    volume_usd: float
    market_url: str
    market_reputation: float
    difference_percentage: float = 0.0

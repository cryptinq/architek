from dataclasses import dataclass, field
from typing import Optional

from app.dataclasses.arbitrage.CryptoMarket import CryptoMarket


@dataclass
class Crypto:
    slug: str
    quote_symbol: str
    base_symbol: Optional[str] = ""
    pair: Optional[str] = ""
    market_data: Optional[list[CryptoMarket]] = field(default_factory=list)
    lowest_market: Optional[CryptoMarket] = None
    highest_market: Optional[CryptoMarket] = None

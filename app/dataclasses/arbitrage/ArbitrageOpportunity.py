from dataclasses import dataclass

from app.dataclasses.arbitrage.CryptoMarket import CryptoMarket


@dataclass
class ArbitrageOpportunity:
    id: str
    market_buy: CryptoMarket
    market_sell: CryptoMarket
    profit_percent: float
    exemple_profit: float

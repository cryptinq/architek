from app.dataclasses.arbitrage.ArbitrageOpportunity import ArbitrageOpportunity
from app.dataclasses.arbitrage.Crypto import Crypto
from app.utilities.UUIDGenerator import UUIDGenerator
from core.kernel.services.classes.BaseService import BaseService


class ArbitrageService(BaseService):

    EXEMPLE_PROFIT_BASE = 1000

    MINIMUM_REPUTATION: float = 0.5
    MINIMUM_VOLUME_USD: float = 1000000
    MINIMUM_PROFIT_PERCENT: float = 0.5

    def __init__(self):
        super().__init__()

    def analyze(self, crypto_data: Crypto) -> list[ArbitrageOpportunity]:

        opportunities: list[ArbitrageOpportunity] = []

        for crypto_market in crypto_data.market_data:

            if crypto_market.market_reputation <= self.MINIMUM_REPUTATION:
                if self.kernel.verbose(0): self.console.info(f"{crypto_market.name} → insufficient market reputation ({crypto_market.market_reputation})")
                continue
            if crypto_market.volume_usd <= self.MINIMUM_VOLUME_USD:
                if self.kernel.verbose(0): self.console.info(f"{crypto_market.name} → insufficient USD volume ({crypto_market.volume_usd})")
                continue
            if crypto_market.difference_percentage <= self.MINIMUM_PROFIT_PERCENT:
                if self.kernel.verbose(0): self.console.info(f"{crypto_market.name} → insufficient difference % ({crypto_market.difference_percentage})")
                continue

            opportunity = ArbitrageOpportunity(
                UUIDGenerator.generate_uuid(), crypto_data.highest_market, crypto_market,
                crypto_market.difference_percentage, self.EXEMPLE_PROFIT_BASE * crypto_market.difference_percentage
            )

            opportunities.append(opportunity)

        return opportunities

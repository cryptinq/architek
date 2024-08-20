from app.dataclasses.arbitrage.ArbitrageOpportunity import ArbitrageOpportunity
from app.dataclasses.arbitrage.Crypto import Crypto
from app.dataclasses.arbitrage.CryptoMarket import CryptoMarket
from app.services.ArbitrageService import ArbitrageService
from app.services.MarketDataService import MarketDataService
from core.kernel.Base import Base


class App(Base):

    def __init__(self):
        super().__init__()
        self.market_data: MarketDataService = self.service("market_data")
        self.arbitrage: ArbitrageService = self.service("arbitrage")

    def boot(self):

        input("")
        exit()

        crypto_data: Crypto = Crypto("bitcoin", "USDT")  # create crypto dataclass to store data
        data = self.market_data.fetch_data(crypto_data.slug, crypto_data.quote_symbol, 100)  # fetch market data for given crypto

        # store data into crypto dataclass
        for data in data["data"]["marketPairs"]:
            crypto_data.market_data.append(
                CryptoMarket(
                    data['exchangeName'], data['exchangeSlug'], data['baseSymbol'], data['quoteSymbol'],
                    float(data['price']), data['lastUpdated'], float(data['volumeUsd']), data['marketUrl'],
                    float(data['marketReputation'])
                )
            )

        # assign base symbol & pair based on fetched market data
        crypto_data.base_symbol = crypto_data.market_data[0].base_symbol
        crypto_data.pair = f"{crypto_data.base_symbol}/{crypto_data.quote_symbol}"

        crypto_data.market_data.sort(key=lambda x: x.price, reverse=True)  # sort market from higher to lower
        crypto_data.highest_market = crypto_data.market_data[0]  # update crypto_data accordingly
        crypto_data.lowest_market = crypto_data.market_data[0]  # update crypto_data accordingly

        for index, crypto_market in enumerate(crypto_data.market_data):
            # calculate difference of price in percent
            crypto_data.market_data[index].difference_percentage = ((crypto_data.highest_market.price /crypto_market.price) * 100) - 100

        # call arbitrage service to determine posible arbitrage opportunities
        arbitrage_opportunities: list[ArbitrageOpportunity] = self.arbitrage.analyze(crypto_data)

        if len(arbitrage_opportunities) == 0:
            self.console.info(
                f"No arbitrage opportunities found for ∑9{crypto_data.pair}∑f (scanned {len(crypto_data.market_data)} markets)"
            )

        else:
            self.console.info(
                f"Found ∑9{len(arbitrage_opportunities)}∑f arbitrage "
                f"opportunit{'y' if len(arbitrage_opportunities) == 1 else 'ies'} "
                f"for ∑9{crypto_data.pair}∑f \n"
            )
            for arbitrage in arbitrage_opportunities:
                self.console.info(
                    f"∑cBUY ∑f {arbitrage.market_buy.name} @ ${round(arbitrage.market_buy.price, 2):,.2f}  →  "
                    f"∑aSELL ∑f {arbitrage.market_sell.name} @ ${round(arbitrage.market_sell.price, 2):,.2f}  |  "
                    f"PROFIT : ∑9{round(arbitrage.profit_percent, 2)}%  ∑f|  ${ArbitrageService.EXEMPLE_PROFIT_BASE} "
                    f"→ ∑a${round((ArbitrageService.EXEMPLE_PROFIT_BASE * arbitrage.profit_percent) / 100, 2)} "
                )

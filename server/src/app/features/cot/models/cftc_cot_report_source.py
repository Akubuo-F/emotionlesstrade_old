from typing import Final

from src.app.domain.models.asset import Asset, ReportedAssets
from src.app.features.cot.models.base.abstract_cot_report_source import AbstractCOTReportSource


class CFTCCotReportSource(AbstractCOTReportSource):
    MARKET_AND_EXCHANGE_NAMES: Final[dict[str, str]] = {
        "AUD": "AUSTRALIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE", #
        "BTC": "BITCOIN - CHICAGO MERCANTILE EXCHANGE", #
        "CAD": "CANADIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE", #
        "CHF": "SWISS FRANC - CHICAGO MERCANTILE EXCHANGE", #
        "DJI": "DJIA x $5 - CHICAGO BOARD OF TRADE", #
        "EUR": "EURO FX - CHICAGO MERCANTILE EXCHANGE", #
        "GBP": "BRITISH POUND - CHICAGO MERCANTILE EXCHANGE", #
        "JPY": "JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE", #
        "NZD": "NZ DOLLAR - CHICAGO MERCANTILE EXCHANGE",
        "NDX": "NASDAQ MINI - CHICAGO MERCANTILE EXCHANGE", #
        "SPX": "E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE", #
        "USD": "USD INDEX - ICE FUTURES U.S.",
        "USO": "WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE", #
        "XAG": "SILVER - COMMODITY EXCHANGE INC.", #
        "XAU": "GOLD - COMMODITY EXCHANGE INC.", #
        "XCU": "COPPER- #1 - COMMODITY EXCHANGE INC.", #
        "XPT": "PLATINUM - NEW YORK MERCANTILE EXCHANGE", #
    }

    COLUMNS_TO_KEEP: Final[list[str]] = [
        "Market and Exchange Names",
        "As of Date in Form YYYY-MM-DD",
        "Open Interest (All)",
        "Noncommercial Positions-Long (All)",
        "Noncommercial Positions-Short (All)",
        "Change in Open Interest (All)",
        "Change in Noncommercial-Long (All)",
        "Change in Noncommercial-Short (All)",
    ]

    def convert(self, assets: list[Asset]) -> list[str]:
        """
        Converts the names of the listed to how they are represented on the CFTC
        COT report.
        :param assets: A tradable financial instrument.
        :return: The converted names of the listed assets.
        """
        market_and_exchange_names: list[str] = []
        for asset in assets:
            asset_code: str = asset.code
            asset_market_and_exchange_name: str = CFTCCotReportSource.MARKET_AND_EXCHANGE_NAMES.get(asset_code, "")
            if asset_market_and_exchange_name == "":
                raise KeyError("Can't get convert asset. Asset not found.")
            market_and_exchange_names.append(asset_market_and_exchange_name)
        return market_and_exchange_names

    def get_asset(self, market_and_exchange_name: str) -> Asset:
        for key, value in CFTCCotReportSource.MARKET_AND_EXCHANGE_NAMES.items():
            if value == market_and_exchange_name:
                for asset in ReportedAssets.ALL:
                    if asset.code == key:
                        return asset


    @property
    def columns_to_keep(self) -> list[str]:
        return CFTCCotReportSource.COLUMNS_TO_KEEP



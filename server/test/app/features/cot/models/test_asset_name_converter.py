import unittest

from src.app.domain.models.asset import ReportedAssets, Asset
from src.app.features.cot.models.base.abstract_cot_report_source import AbstractAssetNameConverter
from src.app.features.cot.models.cftc_cot_report_source import CFTCAssetNameConverter


class TestAssetNameConverter(unittest.TestCase):

    def setUp(self):
        self.reported_assets: list[Asset] = ReportedAssets.ALL
        self.asset_name_converter: AbstractAssetNameConverter = CFTCAssetNameConverter()

    def test_convert(self):
        expected = [
            "AUSTRALIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE",
            "BITCOIN - CHICAGO MERCANTILE EXCHANGE",
            "CANADIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE",
            "SWISS FRANC - CHICAGO MERCANTILE EXCHANGE",
            "DOW JONES U.S. REAL ESTATE IDX - CHICAGO BOARD OF TRADE",
            "EURO FX - CHICAGO MERCANTILE EXCHANGE",
            "BRITISH POUND - CHICAGO MERCANTILE EXCHANGE",
            "JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE",
            "NEW ZEALAND - CHICAGO MERCANTILE EXCHANGE",
            "NASDAQ MINI - CHICAGO MERCANTILE EXCHANGE",
            "E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE",
            "WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE",
            "SILVER - COMMODITY EXCHANGE INC.",
            "GOLD - COMMODITY EXCHANGE INC.",
            "COPPER- #1 - COMMODITY EXCHANGE INC.",
            "PLATINUM - NEW YORK MERCANTILE EXCHANGE",
        ]
        self.assertEqual(expected, self.asset_name_converter.convert(self.reported_assets))


if __name__ == '__main__':
    unittest.main()
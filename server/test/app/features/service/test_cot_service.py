import unittest

import pandas as pd

from src.app.domain.models.asset import ReportedAssets
from src.app.features.cot.data.cot_report_downloader import COTReportDownloader
from src.app.features.cot.data.cot_repository import COTRepository
from src.app.features.cot.models.cftc_cot_report_source import CFTCCotReportSource
from src.app.features.cot.service.cot_service import COTService
from src.app.utils.dataframe_rule import DataFrameRule


class TestCOTService(unittest.TestCase):

    def setUp(self):
        self.cot_service = COTService()

    def test_latest_report(self):
        result = self.cot_service.latest_report(
            reported_assets=ReportedAssets.ALL,
            cot_repository=COTRepository(
                "report.csv",
                cot_report_downloader=COTReportDownloader()
            ),
            dataframe_rule=DataFrameRule(pd.DataFrame()),
            cot_report_source=CFTCCotReportSource(),
        )
        for report in result:
            print(report)
            print(report.to_dict())
        self.assertEqual(len(ReportedAssets.ALL), len(result))


if __name__ == '__main__':
    unittest.main()

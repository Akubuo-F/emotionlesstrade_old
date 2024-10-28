import unittest

import pandas as pd

from src.app.domain.models.asset import ReportedAssets
from src.app.features.cot.data.cot_repository import COTRepository
from src.app.features.cot.data.half_year_cot_report_downloader import HalfYearCOTReportDownloader
from src.app.features.cot.models.cftc_cot_report_source import CFTCCotReportSource
from src.app.features.cot.service.cot_service import COTService
from src.app.utils.base.directory_helper import DirectoryHelper
from src.app.utils.dataframe_rule import DataFrameRule


class TestCOTService(unittest.TestCase):

    def setUp(self):
        self.cot_service = COTService(
            cot_repository=COTRepository(
                local_csv=f"{DirectoryHelper.root_dir()}/storage/tests/cot_reports.csv",
                cot_report_downloader=HalfYearCOTReportDownloader(
                    dataframe_rule=DataFrameRule(pd.DataFrame()),
                    report_source=CFTCCotReportSource()
                )
            ),
            dataframe_rule=DataFrameRule(pd.DataFrame())
        )

    def test_latest_report(self):
        result = self.cot_service.latest_report(reported_assets=ReportedAssets.ALL)
        print(sorted(result, key=lambda report: -report.percentage_net_change))
        self.assertEqual(len(ReportedAssets.ALL), len(result))

    def test_historical_report(self):
        result = self.cot_service.historical_reports(ReportedAssets.btc, 4)
        #print(result)
        self.assertEqual(4, len(result))


if __name__ == '__main__':
    unittest.main()

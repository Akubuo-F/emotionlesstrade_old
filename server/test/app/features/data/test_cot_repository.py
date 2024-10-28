import unittest
import pandas as pd

from src.app.features.cot.data.cot_repository import COTRepository
from src.app.features.cot.data.half_year_cot_report_downloader import HalfYearCOTReportDownloader
from src.app.features.cot.models.cftc_cot_report_source import CFTCCotReportSource
from src.app.utils.base.directory_helper import DirectoryHelper
from src.app.utils.dataframe_rule import DataFrameRule


class TestCOTRepository(unittest.TestCase):

    def setUp(self):
        local_csv = f"{DirectoryHelper.root_dir()}/storage/tests/cot_reports.csv"
        self.cot_repository = COTRepository(
            local_csv,
            HalfYearCOTReportDownloader(
                DataFrameRule(pd.DataFrame()),
                CFTCCotReportSource()
            )
        )

    def test_fetch(self):
        result = self.cot_repository.fetch_report(DataFrameRule(pd.DataFrame()))
        self.cot_repository.store_report(result)
        self.assertFalse(0, len(result))


if __name__ == '__main__':
    unittest.main()
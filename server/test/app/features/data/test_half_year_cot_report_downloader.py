import unittest
from unittest.mock import MagicMock, patch
import pandas as pd
from datetime import datetime

from src.app.features.cot.data.half_year_cot_report_downloader import HalfYearCOTReportDownloader


class TestHalfYearCOTReportDownloader(unittest.TestCase):

    def setUp(self):
        # Create mock instances for AbstractDataFrameRule and AbstractCOTReportSource
        self.mock_dataframe_rule = MagicMock()
        self.mock_report_source = MagicMock()

        # Set up the mock methods for the report source
        self.mock_report_source.date_column_name.return_value = 'date'
        self.mock_report_source.report_type.return_value = 'legacy report futures and options'

        # Create an instance of HalfYearCOTReportDownloader
        self.downloader = HalfYearCOTReportDownloader(
            dataframe_rule=self.mock_dataframe_rule,
            report_source=self.mock_report_source
        )

    @patch('cot_reports.cot_year')
    def test_download_with_enough_reports(self, mock_cot_year):
        # Mock the return value of the web scraper for the current year
        current_year = datetime.now().year
        mock_cot_year.side_effect = [
            pd.DataFrame({'date': [
                f'{current_year}-01-01', f'{current_year}-01-08',
                f'{current_year}-01-15', f'{current_year}-01-22',
                f'{current_year}-02-01', f'{current_year}-02-08',
                f'{current_year}-02-15', f'{current_year}-02-22',
                f'{current_year}-03-01', f'{current_year}-03-08'
            ]}),
            pd.DataFrame({'date': [
                f'{current_year - 1}-01-01', f'{current_year - 1}-01-08',
                f'{current_year - 1}-01-15', f'{current_year - 1}-01-22',
                f'{current_year - 1}-02-01', f'{current_year - 1}-02-08',
                f'{current_year - 1}-02-15', f'{current_year - 1}-02-22',
                f'{current_year - 1}-03-01', f'{current_year - 1}-03-08'
            ]})  # Simulate enough reports from the previous year
        ]

        # Call the download method
        result = self.downloader.download()

        self.assertEqual(result, self.mock_dataframe_rule.apply)

    @patch('cot_reports.cot_year')
    def test_download_with_missing_reports(self, mock_cot_year):
        # Mock the return value of the web scraper for the current year
        current_year = datetime.now().year
        mock_cot_year.side_effect = [
            pd.DataFrame({'date': [f'{current_year}-01-01']}),  # Only one report
            pd.DataFrame({'date': [
                f'{current_year - 1}-01-01', f'{current_year - 1}-01-08',
                f'{current_year - 1}-01-15', f'{current_year - 1}-01-22',
                f'{current_year - 1}-02-01',  # etc.
                f'{current_year - 1}-02-08', f'{current_year - 1}-02-15',
                f'{current_year - 1}-02-22', f'{current_year - 1}-03-01', f'{current_year - 1}-03-08'
            ]})  # Simulate enough reports from the previous year
        ]

        # Call the download method
        result = self.downloader.download()

        # Assertions
        self.mock_dataframe_rule.set_dataframe.assert_called()
        self.mock_dataframe_rule.keep_only_values.assert_called_once()
        self.assertEqual(result, self.mock_dataframe_rule.apply)

    def test_get_dates_to_keep(self):
        # Create a sample DataFrame
        sample_df = pd.DataFrame({
            'date': ['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-15']
        })

        # Mock the set_dataframe and sort_by methods
        self.mock_dataframe_rule.apply = sample_df
        self.mock_dataframe_rule.sort_by.return_value = None

        # Call the private method _get_dates_to_keep
        dates_to_keep = self.downloader._get_dates_to_keep(sample_df, keep_count=3)

        # Assertions
        self.assertEqual(dates_to_keep, {'2023-01-01', '2023-01-15', '2023-02-01'})

if __name__ == '__main__':
    unittest.main()
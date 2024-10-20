from datetime import datetime

import pandas as pd
import cot_reports as cot_webscraper

from src.app.features.cot.data.base.abstract_cot_report_downloader import AbstractCOTReportDownloader
from src.app.features.cot.models.base.abstract_cot_report_source import AbstractCOTReportSource
from src.app.utils.base.abstract_dataframe_rule import AbstractDataFrameRule


class HalfYearCOTReportDownloader(AbstractCOTReportDownloader):

    def __init__(self, dataframe_rule: AbstractDataFrameRule, report_source: AbstractCOTReportSource):
        self._dataframe_rule = dataframe_rule
        self._report_source = report_source

    def download(self) -> pd.DataFrame:
        """Returns 6-months COT reports of each asset as a data frame."""
        current_year: int = datetime.now().year
        current_year_report: pd.DataFrame = self._download_with_webscraper(current_year)
        dates_to_keep: set[str] = self._get_dates_to_keep(current_year_report, keep_count=24)
        missing_reports_count: int = 24 - len(dates_to_keep)
        previous_year_report: pd.DataFrame | None = None
        if missing_reports_count > 0:
            previous_year = current_year - 1
            previous_year_report = self._download_with_webscraper(previous_year)
            dates_to_keep.update(self._get_dates_to_keep(previous_year_report, keep_count=missing_reports_count))
        total_report: pd.DataFrame = pd.concat(
            [current_year_report, previous_year_report],
            ignore_index=True,
        ) if previous_year_report is not None else current_year_report
        self._dataframe_rule.set_dataframe(total_report)
        self._dataframe_rule.keep_only_values(column=self._report_source.date_column_name(), values=list(dates_to_keep))
        return self._dataframe_rule.apply


    def _download_with_webscraper(self, report_year: int):
        return cot_webscraper.cot_year(
            year=report_year,
            cot_report_type=self._report_source.report_type(),
            store_txt=False,
            verbose=False
        )

    def _get_dates_to_keep(self, dataframe: pd.DataFrame, keep_count: int) -> set[str]:
        self._dataframe_rule.set_dataframe(dataframe)
        self._dataframe_rule.sort_by(self._report_source.date_column_name(), increasing=False)
        dates_to_keep = set()
        for _, row in self._dataframe_rule.apply.iterrows():
            if len(dates_to_keep) == keep_count:
                break
            date: str = row[self._report_source.date_column_name()]
            dates_to_keep.add(date)
        return dates_to_keep

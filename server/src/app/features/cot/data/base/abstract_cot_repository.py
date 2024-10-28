from abc import ABC, abstractmethod

import pandas as pd

from src.app.features.cot.data.base.abstract_cot_report_downloader import AbstractCOTReportDownloader
from src.app.features.cot.models.base.abstract_cot_report_source import AbstractCOTReportSource
from src.app.utils.base.abstract_dataframe_rule import AbstractDataFrameRule


class AbstractCOTRepository(ABC):
    """
    Base class for COT repository. Handles fetching and storing of the COT report.
    """

    def __init__(self, local_csv: str, cot_report_downloader: AbstractCOTReportDownloader):
        """
        :param local_csv: Local csv file of the COT report.
        :param cot_report_downloader:
        """
        self._local_csv = local_csv
        self._cot_report_downloader = cot_report_downloader

    @abstractmethod
    def fetch_report(self, dataframe_rule: AbstractDataFrameRule) -> pd.DataFrame:
        """
        Handles COT report fetching. First checks if the locally stored COT report is valid, then returns it,
        if not, downloads the report from the official CFTC Website.
        :param dataframe_rule: A set of rules that will be applied on a data frame to modify the data frame.
        :return: pd.DataFrame
        """
        ...

    @abstractmethod
    def store_report(self, cot_dataframe: pd.DataFrame) -> None:
        """
        Stores the cot report data frame content as csv.
        :param cot_dataframe: The COT report as a data frame
        :return: None
        """
        ...

    @property
    def report_source(self) -> AbstractCOTReportSource:
        """returns the report source of this COT repository."""
        return self._cot_report_downloader.report_source
from abc import ABC, abstractmethod

import pandas as pd

from src.app.features.cot.models.base.abstract_cot_report_source import AbstractCOTReportSource


class AbstractCOTReportDownloader(ABC):
    """
    Base class for COT report downloader. Handles downloading of the COT report from a COT report source.
    """

    def __init__(self, report_source: AbstractCOTReportSource):
        self._report_source = report_source

    @abstractmethod
    def download(self) -> pd.DataFrame:
        """Downloads and return the COT report as a data frame."""
        ...

    @property
    def report_source(self) -> AbstractCOTReportSource:
        """returns the report source of this COT downloader."""
        return self._report_source
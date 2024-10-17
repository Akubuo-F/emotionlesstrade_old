from abc import ABC, abstractmethod

import pandas as pd


class AbstractCOTReportDownloader(ABC):
    """
    Base class for COT report downloader. Handles downloading of the COT report from the CFTC website.
    """

    @abstractmethod
    def download(self) -> pd.DataFrame:
        """Downloads and return the COT report as a data frame."""
        ...
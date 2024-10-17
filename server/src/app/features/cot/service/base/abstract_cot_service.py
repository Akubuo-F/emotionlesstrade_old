from abc import ABC, abstractmethod

from src.app.domain.models.asset import Asset
from src.app.features.cot.data.base.abstract_cot_repository import AbstractCOTReportDownloader
from src.app.features.cot.model.cot_report import COTReport


class AbstractCOTService(ABC):
    """
    Base class for COTService. Handles all operations related to the COT report.
    """

    @abstractmethod
    def latest_report(
            self,
            reported_assets: list[Asset],
            cot_report_downloader: AbstractCOTReportDownloader,
    ) -> list[COTReport]:
        """
        Gets the latest report of the assets listed in reported assets.
        :param reported_assets: A list of tradable financial instruments.
        :param cot_report_downloader: Handles downloading of the COT report from the CFTC website.
        :return: COTReport
        """
        ...
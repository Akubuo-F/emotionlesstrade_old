from abc import ABC, abstractmethod

from src.app.domain.models.asset import Asset
from src.app.features.cot.models.cot_report import COTReport


class AbstractCOTService(ABC):
    """
    Base class for COTService. Handles all operations related to the COT report.
    """

    @abstractmethod
    def latest_report(self, reported_assets: list[Asset]) -> list[COTReport]:
        """
        Gets the latest report of the assets listed in reported assets.
        :param reported_assets: A list of tradable financial instruments.
        :return: list[COTReport]
        """
        ...

    @abstractmethod
    def historical_reports(self, asset: Asset, period: int = 6) -> list[COTReport]:
        """
        Gets the historical reports of an asset.
        :param asset: A tradable financial instrument
        :param period: The number of reports.
        :return: list[COTReport]
        """
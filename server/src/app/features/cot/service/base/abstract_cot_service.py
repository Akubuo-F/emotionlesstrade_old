from abc import ABC, abstractmethod

from src.app.domain.models.asset import Asset
from src.app.features.cot.data.base.abstract_cot_repository import AbstractCOTRepository
from src.app.features.cot.models.base.abstract_cot_report_source import AbstractCOTReportSource
from src.app.features.cot.models.cot_report import COTReport
from src.app.utils.base.abstract_dataframe_rule import AbstractDataFrameRule


class AbstractCOTService(ABC):
    """
    Base class for COTService. Handles all operations related to the COT report.
    """

    @abstractmethod
    def latest_report(
            self,
            reported_assets: list[Asset],
            cot_repository: AbstractCOTRepository,
            dataframe_rule: AbstractDataFrameRule,
            cot_report_source: AbstractCOTReportSource,

    ) -> list[COTReport]:
        """
        Gets the latest report of the assets listed in reported assets.
        :param reported_assets: A list of tradable financial instruments.
        :param cot_repository: Handles fetching and storing of the COT report.
        :param dataframe_rule: A set of rules that will be applied on a data frame to modify the data frame.
        :param cot_report_source: Handle the conversion of report values to how they are represented on a COT report source.
        :return: COTReport
        """
        ...
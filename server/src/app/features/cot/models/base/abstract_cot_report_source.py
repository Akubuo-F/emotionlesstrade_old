from abc import ABC, abstractmethod

from src.app.domain.models.asset import Asset


class AbstractCOTReportSource(ABC):
    """
    Base class for COT report source. Handle the conversion of report values to how they are represented
    on a COT report source.
    """

    @staticmethod
    @abstractmethod
    def convert(assets: list[Asset]) -> list[str]:
        """
        Converts the names of the listed to how they are represented on the COT
        report source.
        :param assets: A tradable financial instrument.
        :return: The converted names of the listed assets.
        """
        ...

    @staticmethod
    @abstractmethod
    def get_asset(market_and_exchange_name: str) -> Asset:
        """
        Returns the asset with the corresponding market and exchange name.
        :param market_and_exchange_name: The name of how the asset is represented on the COT report source.
        :return: Asset
        """
        ...

    @staticmethod
    @abstractmethod
    def columns_to_keep() -> list[str]:
        """Returns only the important data frame columns for analysis."""
        ...

    @staticmethod
    @abstractmethod
    def date_column_name() -> str:
        """returns the name of the date column."""

    @staticmethod
    @abstractmethod
    def report_type() -> str:
        """returns the report type of this report source. e.g. legacy report futures and options."""
        ...

from abc import ABC, abstractmethod

from src.app.domain.models.asset import Asset


class AbstractCOTReportSource(ABC):
    """
    Base class for COT report source. Handle the conversion of report values to how they are represented
    on a COT report source.
    """

    @abstractmethod
    def convert(self, assets: list[Asset]) -> list[str]:
        """
        Converts the names of the listed to how they are represented on the COT
        report source.
        :param assets: A tradable financial instrument.
        :return: The converted names of the listed assets.
        """
        ...

    @abstractmethod
    def get_asset(self, market_and_exchange_name: str) -> Asset:
        """
        Returns the asset with the corresponding market and exchange name.
        :param market_and_exchange_name: The name of how the asset is represented on the COT report source.
        :return: Asset
        """
        ...

    @property
    @abstractmethod
    def columns_to_keep(self) -> list[str]:
        """Returns only the important data frame columns for analysis."""
        ...
from datetime import datetime
from typing import Callable

import pandas as pd

from src.app.domain.models.asset import Asset
from src.app.features.cot.data.base.abstract_cot_repository import AbstractCOTRepository
from src.app.features.cot.models.cot_report import COTReport
from src.app.features.cot.models.cot_report_dataframe_formats import COTReportDataFrameFormats
from src.app.features.cot.service.base.abstract_cot_service import AbstractCOTService
from src.app.utils.base.abstract_dataframe_rule import AbstractDataFrameRule


class COTService(AbstractCOTService):

    def __init__(
            self,
            cot_repository: AbstractCOTRepository,
            dataframe_rule: AbstractDataFrameRule
    ):
        """

        :param cot_repository: Handles fetching and storing of the COT report.
        :param dataframe_rule: A set of rules that will be applied on a data frame to modify the data frame.
        """
        self._cot_repository = cot_repository
        self._dataframe_rule = dataframe_rule
        self._report_source = cot_repository.report_source
        self._name_column: str = COTReportDataFrameFormats.COLUMN_NAMES[0]
        self._date_column: str = COTReportDataFrameFormats.COLUMN_NAMES[1]

    def latest_report(
            self,
            reported_assets: list[Asset],
    ) -> list[COTReport]:
        market_and_exchange_names: list[str] = self._get_assets_market_and_exchange_names(reported_assets)
        rules: list[Callable[[], AbstractDataFrameRule]] = self._dataframe_preformat_rules()
        rules.extend([
            lambda: self._dataframe_rule.keep_only_values(
                column=self._name_column,
                values=market_and_exchange_names
            ),
            lambda: self._dataframe_rule.sort_by(
                column=COTReportDataFrameFormats.COLUMN_NAMES[1],
                increasing=False
            ),
            lambda: self._dataframe_rule.remove_duplicates([self._name_column]),
            lambda: self._dataframe_rule.sort_by(
                column=self._name_column,
                increasing=True
            ),
        ])
        return self._make_cot_report(rules)

    def historical_reports(self, asset: Asset, period: int = 24) -> list[COTReport]:
        asset_market_and_exchange_name: str = self._get_assets_market_and_exchange_names([asset])[0]
        rules: list[Callable[[], AbstractDataFrameRule]] = self._dataframe_preformat_rules()
        rules.extend([
            lambda: self._dataframe_rule.keep_only_values(
                column=self._name_column,
                values=[asset_market_and_exchange_name]
            ),
            lambda: self._dataframe_rule.sort_by(
                column=self._date_column,
                increasing=False
            )
        ])
        return self._make_cot_report(rules)[ : period]

    def _get_assets_market_and_exchange_names(self, assets: list[Asset]) -> list[str]:
        """
        Returns the market and exchange names of the assets from the report source.
        :param assets: A list of tradable financial instruments.
        :return: list[str]
        """
        return self._report_source.convert(assets)

    def _dataframe_preformat_rules(self) -> list[Callable[[], AbstractDataFrameRule]]:
        """List of rules to apply to format the COT report data frame to retain consistency."""
        return [
            lambda: self._dataframe_rule.keep_only_columns(self._report_source.columns_to_keep()),
            lambda: self._dataframe_rule.rename_columns_to(COTReportDataFrameFormats.COLUMN_NAMES),
        ]

    def _make_cot_report(self, rules: list[Callable[[], AbstractDataFrameRule]]) -> list[COTReport]:
        """
        Applies the given dataframe rules to the fetched reports and parses each entry in the
        fetched reports to a COTReport.
        :param rules: The Rules to be applied on the fetched reports.
        :return: list[COTReport]
        """
        self._dataframe_rule.set_future_rules(rules)
        fetched_reports: pd.DataFrame = self._cot_repository.fetch_report(self._dataframe_rule)
        cot_reports: list[COTReport] = []
        for _, row in fetched_reports.iterrows():
            asset: Asset = self._report_source.get_asset(row[COTReportDataFrameFormats.COLUMN_NAMES[0]])
            released_on: str = datetime.strptime(
                row[COTReportDataFrameFormats.COLUMN_NAMES[1]],
                "%Y-%m-%d"
            ).strftime("%Y-%m-%d")
            open_interest: int = int(row[COTReportDataFrameFormats.COLUMN_NAMES[2]])
            long_contracts: int = int(row[COTReportDataFrameFormats.COLUMN_NAMES[3]])
            short_contracts: int = int(row[COTReportDataFrameFormats.COLUMN_NAMES[4]])
            change_in_open_interest: int = int(row[COTReportDataFrameFormats.COLUMN_NAMES[5]])
            change_in_long_contracts: int = int(row[COTReportDataFrameFormats.COLUMN_NAMES[6]])
            change_in_short_contracts: int = int(row[COTReportDataFrameFormats.COLUMN_NAMES[7]])
            cot_report: COTReport = COTReport(
                released_on=released_on,
                asset=asset,
                long=long_contracts,
                short=short_contracts,
                long_change=change_in_long_contracts,
                short_change=change_in_short_contracts,
                open_interest=open_interest,
                open_interest_change=change_in_open_interest
            )
            cot_reports.append(cot_report)
        return cot_reports

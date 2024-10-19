from datetime import datetime
from typing import Callable

import pandas as pd

from src.app.domain.models.asset import Asset
from src.app.features.cot.data.base.abstract_cot_repository import AbstractCOTRepository
from src.app.features.cot.models.base.abstract_cot_report_source import AbstractCOTReportSource
from src.app.features.cot.models.cot_report import COTReport
from src.app.features.cot.models.cot_report_dataframe_formats import COTReportDataFrameFormats
from src.app.features.cot.service.base.abstract_cot_service import AbstractCOTService
from src.app.utils.base.abstract_dataframe_rule import AbstractDataFrameRule


class COTService(AbstractCOTService):

    def latest_report(
            self,
            reported_assets: list[Asset],
            cot_repository: AbstractCOTRepository,
            dataframe_rule: AbstractDataFrameRule,
            cot_report_source: AbstractCOTReportSource
    ) -> list[COTReport]:
        market_and_exchange_names: list[str] = cot_report_source.convert(reported_assets)
        rules: list[Callable[[], AbstractDataFrameRule]] = [
            lambda: dataframe_rule.keep_only_columns(cot_report_source.columns_to_keep),
            lambda: dataframe_rule.rename_columns_to(COTReportDataFrameFormats.COLUMN_NAMES),
            lambda: dataframe_rule.keep_only_values(
                column=COTReportDataFrameFormats.COLUMN_NAMES[0],
                values=market_and_exchange_names
            ),
            lambda: dataframe_rule.sort_by(
                column=COTReportDataFrameFormats.COLUMN_NAMES[1],
                increasing=False
            ),
            lambda: dataframe_rule.remove_duplicates([COTReportDataFrameFormats.COLUMN_NAMES[0]]),
            lambda: dataframe_rule.sort_by(
                column=COTReportDataFrameFormats.COLUMN_NAMES[0],
                increasing=True
            ),
        ]
        dataframe_rule.set_future_rules(rules)
        dataframe: pd.DataFrame = cot_repository.fetch_report(dataframe_rule)
        return self._make_cot_report(dataframe, cot_report_source)


    @staticmethod
    def _make_cot_report(data: pd.DataFrame, cot_report_source: AbstractCOTReportSource) -> list[COTReport]:
        cot_reports: list[COTReport] = []
        for _, row in data.iterrows():
            asset: Asset = cot_report_source.get_asset(row[COTReportDataFrameFormats.COLUMN_NAMES[0]])
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

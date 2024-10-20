import os.path

import pandas as pd

from src.app.features.cot.data.base.abstract_cot_report_downloader import AbstractCOTReportDownloader
from src.app.features.cot.data.base.abstract_cot_repository import AbstractCOTRepository
from src.app.utils.base.abstract_dataframe_rule import AbstractDataFrameRule


class COTRepository(AbstractCOTRepository):

    def __init__(self, local_csv: str, cot_report_downloader: AbstractCOTReportDownloader):
        super().__init__(
            local_csv=local_csv,
            cot_report_downloader=cot_report_downloader,
        )

    def fetch_report(self, dataframe_rule: AbstractDataFrameRule) -> pd.DataFrame:
        data: pd.DataFrame
        if self._local_csv.endswith(".csv") and os.path.exists(self._local_csv):
            return pd.read_csv(self._local_csv, index_col=0)
        else:
            data = self._cot_report_downloader.download()
            dataframe_rule.set_dataframe(data)
            return dataframe_rule.apply_future_rules.reset_index(drop=True)

    def store_report(self, cot_dataframe: pd.DataFrame) -> None:
        cot_dataframe.to_csv(self._local_csv, index=True)

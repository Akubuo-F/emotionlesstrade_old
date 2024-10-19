import pandas as pd

from src.app.features.cot.data.base.abstract_cot_report_downloader import AbstractCOTReportDownloader


class COTReportDownloader(AbstractCOTReportDownloader):

    def download(self) -> pd.DataFrame:
        return pd.read_csv("report.csv")
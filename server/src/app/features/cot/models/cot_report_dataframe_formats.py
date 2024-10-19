from typing import Final


class COTReportDataFrameFormats:

    COLUMN_NAMES: Final[list[str]] = [
        "asset name",
        "reported on",
        "open interest",
        "long contracts",
        "short contracts",
        "change in open interest",
        "change in long contracts",
        "change in short contracts",
    ]
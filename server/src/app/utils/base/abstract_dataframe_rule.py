from abc import ABC, abstractmethod

import pandas as pd


class AbstractDataFrameRule(ABC):
    """
    A set of rules that will be applied on a data frame to modify the data frame.
    """

    @abstractmethod
    def apply(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        ...
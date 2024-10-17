import pandas as pd


class DataFrameRule:
    """
    A set of rules that will be applied on a data frame to modify the data frame.
    """

    def apply(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        ...
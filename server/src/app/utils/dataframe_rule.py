import pandas as pd

class DataFrameRule:
    """
    A set of rules that will be applied on a data frame to modify the data frame.
    """

    def __init__(self, dataframe: pd.DataFrame):
        """
        :param dataframe: Data frame rules will be applied on.
        """
        self._dataframe = dataframe

    def keep_only_columns(self, columns: list[str]) -> "DataFrameRule":
        """
        Only specified columns are kept in the data frame.
        Make sure the specified columns are present in the data frame.
        :param columns: Columns to keep.
        :return: DataFrameRule
        """
        self._dataframe = self._dataframe[columns]
        return self

    def rename_columns_to(self, new_columns: list[str]) -> "DataFrameRule":
        """
        Renames all the columns in the data frame to the new column according to their orderings.
        Make sure the ith column in the dataframe you want to rename matches new_columns[i].
        :param new_columns: New column names.
        :return: DataFrameRule
        """
        self._dataframe.columns = new_columns
        return self

    def sort_by(self, column: str, increasing: bool = True) -> "DataFrameRule":
        """
        Sorts the specified column in the order specified.
        Make sure the column specified exists in the data frame.
        :param column: column to sort.
        :param increasing: sorting order of the column.
        :return: DataFrameRule
        """
        self._dataframe = self._dataframe.sort_values(by=column, ascending=increasing)
        return self

    def keep_only_values(self, column: str, values: list[str]) -> "DataFrameRule":
        """
        Keeps only the values of a column you want in the data frame.
        For example, if in the AssetName column, you want to keep only Gold, Silver, and Dollar.
        This will keep in the data frame only rows where their AssetName column has values of Gold,
        Silver, or Dollar.
        :param column: Column that contains the values you want to keep.
        :param values: Values to keep.
        :return: DataFrameRule
        """
        self._dataframe = self._dataframe[self._dataframe[column].isin(values)]
        return self

    @property
    def apply(self) -> pd.DataFrame:
        """returns the data frame."""
        return self._dataframe

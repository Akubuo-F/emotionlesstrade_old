from abc import ABC, abstractmethod
from typing import Callable

import pandas as pd

class AbstractDataFrameRule(ABC):
    """
    Base class for DataFrame Rule. A set of rules that will be applied on a data frame to modify the data frame.
    """

    @abstractmethod
    def keep_only_columns(self, columns: list[str]) -> "AbstractDataFrameRule":
        """
        Only specified columns are kept in the data frame.
        Make sure the specified columns are present in the data frame.
        :param columns: Columns to keep.
        :return: AbstractDataFrameRule
        """
        ...

    @abstractmethod
    def rename_columns_to(self, new_columns: list[str]) -> "AbstractDataFrameRule":
        """
        Renames all the columns in the data frame to the new column according to their orderings.
        Make sure the ith column in the dataframe you want to rename matches new_columns[i].
        :param new_columns: New column names.
        :return: AbstractDataFrameRule
        """
        ...

    @abstractmethod
    def sort_by(self, column: str, increasing: bool = True) -> "AbstractDataFrameRule":
        """
        Sorts the specified column in the order specified.
        Make sure the column specified exists in the data frame.
        :param column: column to sort.
        :param increasing: sorting order of the column.
        :return: AbstractDataFrameRule
        """
        ...

    @abstractmethod
    def remove_duplicates(self, columns: list[str]) -> "AbstractDataFrameRule":
        """
        Keeps only one copy of each value in the column.
        :param columns: Target columns to remove their duplicate values.
        :return:
        """
        ...

    @abstractmethod
    def keep_only_values(self, column: str, values: list[str]) -> "AbstractDataFrameRule":
        """
        Keeps only the values of a column you want in the data frame.
        For example, if in the AssetName column, you want to keep only Gold, Silver, and Dollar.
        This will keep in the data frame only rows where their AssetName column has values of Gold,
        Silver, or Dollar.
        :param column: Column that contains the values you want to keep.
        :param values: Values to keep.
        :return: AbstractDataFrameRule
        """
        ...

    @abstractmethod
    def set_dataframe(self, dataframe: pd.DataFrame) -> None:
         ...

    @abstractmethod
    def set_future_rules(self, future_rules: list[Callable[[], "AbstractDataFrameRule"]]) -> None:
        """
        Set rules that can be applied later to the data frame.
        :param future_rules: List of functions that take a data frame and returns a modified data frame.
        :return: None
        """
        ...

    @property
    @abstractmethod
    def apply_future_rules(self) -> pd.DataFrame:
        """applies the set future rules on the data frame and returns it."""
        ...

    @property
    @abstractmethod
    def apply(self) -> pd.DataFrame:
        """returns the data frame."""
        ...
import unittest
import pandas as pd
from src.app.utils.dataframe_rule import DataFrameRule

class TestDataFrameRule(unittest.TestCase):
    def setUp(self):
        data = {
            'Name': ['Gold', 'Silver', 'Dollar', 'Bitcoin'],
            'Value': [1500, 15, 1, 60000]
        }
        self._df = pd.DataFrame(data)

    def test_keep_only_columns(self):
        dataframe_rule = DataFrameRule(self._df.copy(deep=True))
        result = dataframe_rule.keep_only_columns(["Name"]).apply
        self.assertTrue('Value' not in result.columns)
        self.assertTrue('Name' in result.columns)

    def test_rename_columns(self):
        dataframe_rule = DataFrameRule(self._df.copy(deep=True))
        result = dataframe_rule.rename_columns_to(["AssetName", "AssetValue"]).apply
        self.assertEqual(list(result.columns), ['AssetName', 'AssetValue'])

    def test_sort_by(self):
        dataframe_rule = DataFrameRule(self._df.copy(deep=True))
        result = dataframe_rule.sort_by("Value", increasing=False).apply
        self.assertEqual(result.iloc[0]['Value'], 60000)
        self.assertEqual(result.iloc[1]['Value'], 1500)
        self.assertEqual(result.iloc[-1]['Value'], 1)

    def test_keep_only_values(self):
        dataframe_rule = DataFrameRule(self._df.copy(deep=True))
        result = dataframe_rule.keep_only_values("Name", ["Gold", "Bitcoin"]).apply
        self.assertEqual(len(result), 2)
        self.assertTrue('Gold' in result['Name'].values)
        self.assertTrue('Bitcoin' in result['Name'].values)
        self.assertFalse("Silver" in result['Name'].values)

    def test_apply_future_rules(self):
        dataframe_rule = DataFrameRule(self._df.copy(deep=True))
        future_rules = [
            lambda : dataframe_rule.keep_only_columns(['Name']),
            lambda : dataframe_rule.rename_columns_to(['AssetName']),
            lambda : dataframe_rule.sort_by('AssetName', increasing=False),
            lambda : dataframe_rule.keep_only_values('AssetName', ['Gold', 'Bitcoin'])
        ]
        dataframe_rule.set_future_rules(future_rules)
        result = dataframe_rule.apply_future_rules
        self.assertTrue('Gold' in result["AssetName"].values)
        self.assertTrue('Bitcoin' in result["AssetName"].values)
        self.assertFalse('Silver' in result["AssetName"].values)
        self.assertTrue(result.iloc[0]["AssetName"] == "Gold")

if __name__ == '__main__':
    unittest.main()

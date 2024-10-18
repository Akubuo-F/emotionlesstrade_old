import unittest

from src.app.features.cot.models.cot_report import COTReport


class TestCOTReport(unittest.TestCase):

    def setUp(self):
        self.long = 1000
        self.short = 500
        self.long_change = 100
        self.short_change = 50
        self.open_interest = 1500
        self.open_interest_change = 200

        self.cot_report = COTReport(
            long=self.long,
            short=self.short,
            long_change=self.long_change,
            short_change=self.short_change,
            open_interest=self.open_interest,
            open_interest_change=self.open_interest_change
        )

    def test_percentage_long(self):
        self.assertAlmostEqual(66.7, self.cot_report.percentage_long)

    def test_percentage_short(self):
        self.assertAlmostEqual(33.3, self.cot_report.percentage_short)

    def test_percentage_net(self):
        self.assertAlmostEqual(33.4, self.cot_report.percentage_net)

    def test_percentage_long_change(self):
        expected = round((100/1900) * 100, 1)
        self.assertAlmostEqual(expected, self.cot_report.percentage_long_change)

    def test_percentage_short_change(self):
        expected = round((50/950) * 100, 1)
        self.assertAlmostEqual(expected, self.cot_report.percentage_short_change)

    def test_percentage_net_change(self):
        self.assertAlmostEqual(5.3, self.cot_report.percentage_net_change)

    def test_percentage_open_interest_change(self):
        expected = round((200/2800)*100, 1)
        print(expected)
        self.assertAlmostEqual(expected, self.cot_report.percentage_open_interest_change)

    def test_to_dict(self):
        self.assertLess(0, len(self.cot_report.to_dict()))

if __name__ == '__main__':
    unittest.main()

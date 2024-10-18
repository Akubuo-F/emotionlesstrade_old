from src.app.utils import util
from src.app.utils.util import do_percentage, do_abs_sum, do_difference


class COTReport:
    """
    A report issued by the CFTC showing the positions of market participants (Noncommercial).
    """

    def __init__(
            self,
            long: int,
            short: int,
            long_change: int,
            short_change: int,
            open_interest: int,
            open_interest_change: int
    ):
        """
        :param long: number of long contracts.
        :param short: number of short contracts.
        :param long_change: change in long contracts from the previous report.
        :param short_change: change in short contacts from the previous report.
        :param open_interest: change in open interest from the previous report.
        :param open_interest_change: change in open interest from the previous report.
        """
        percentage_long_short_and_float: list[float] = COTReport._calculate_percentage_long_short_and_net(long, short)
        self._percentage_long = percentage_long_short_and_float[0]
        self._percentage_short = percentage_long_short_and_float[1]
        self._percentage_net = percentage_long_short_and_float[2]
        percentage_change_long_short_and_net: list[float] = COTReport._calculate_percentage_change_long_short_and_net(
            long=long,
            short=short,
            long_change=long_change,
            short_change=short_change,
            net=long-short
        )
        self._percentage_change_long = percentage_change_long_short_and_net[0]
        self._percentage_change_short = percentage_change_long_short_and_net[1]
        self._percentage_change_net = percentage_change_long_short_and_net[2]
        self._percentage_change_open_interest: float = COTReport._calculate_open_interest_percentage_change(
            open_interest,
            open_interest_change
        )

    def to_dict(self) -> dict:
        """returns a dictionary representation of the COT report."""
        return {
            "percentage_long": self._percentage_long,
            "percentage_short": self._percentage_short,
            "percentage_net": self._percentage_net,
            "percentage_change_long": self._percentage_change_long,
            "percentage_change_short": self._percentage_change_short,
            "percentage_change_net": self._percentage_change_net,
            "percentage_change_open_interest": self._percentage_change_open_interest
        }

    @property
    def percentage_long(self) -> float:
        """returns the percentage of long contracts."""
        return self._percentage_long

    @property
    def percentage_short(self) -> float:
        """returns the percentage of short contracts."""
        return self._percentage_short

    @property
    def percentage_net(self) -> float:
        """returns the net percentage between long and short contracts."""
        return self._percentage_net

    @property
    def percentage_long_change(self) -> float:
        """returns the percentage change in long contracts from the previous report."""
        return self._percentage_change_long

    @property
    def percentage_short_change(self) -> float:
        """returns the percentage change in short contracts from the previous report."""
        return self._percentage_change_short

    @property
    def percentage_net_change(self) -> float:
        """returns the net percentage change from the previous report."""
        return self._percentage_change_net

    @property
    def percentage_open_interest_change(self) -> float:
        """returns the percentage change in open interest from the previous report."""
        return self._percentage_change_open_interest

    @staticmethod
    def _calculate_percentage_long_short_and_net(long: int, short: int) -> list[float]:
        total: int = util.do_abs_sum(long, short)
        percentage_long: float = util.do_percentage(long, total)
        percentage_short: float = util.do_percentage(short, total)
        percentage_net: float = round(util.do_difference(percentage_long, percentage_short), 1)
        return [percentage_long, percentage_short, percentage_net]

    @staticmethod
    def _calculate_percentage_change_long_short_and_net(long, short, net, long_change, short_change) -> list[float]:
        previous_long: int = util.do_difference(long, long_change)
        previous_short: int = util.do_difference(short, short_change)
        current_and_previous_long = util.do_abs_sum(long, previous_long)
        current_and_previous_short = util.do_abs_sum(short, previous_short)
        percentage_long_change: float = util.do_percentage(long_change, current_and_previous_long)
        percentage_short_change: float = util.do_percentage(short_change, current_and_previous_short)

        previous_net: int = util.do_difference(previous_long, previous_short)
        net_change: int = util.do_difference(net, previous_net)
        current_and_previous_net: int = util.do_abs_sum(net, previous_net)
        percentage_net_change: float = util.do_percentage(net_change, current_and_previous_net)
        return [percentage_long_change, percentage_short_change, percentage_net_change]

    @staticmethod
    def _calculate_open_interest_percentage_change(open_interest: int, open_interest_change: int):
        previous_open_interest: int = util.do_difference(open_interest, open_interest_change)
        current_and_previous_open_interest: int = util.do_sum(open_interest, previous_open_interest)
        return util.do_percentage(open_interest_change, current_and_previous_open_interest)

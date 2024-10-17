def do_sum(a: int | float, b: int | float) -> int | float:
    return a + b


def do_difference(a: int | float, b: int | float) -> int | float:
    return a - b


def do_percentage(dividend: int | float, divisor: int | float, decimal_digits: int = 1) -> int | float:
    return round((dividend / divisor) * 100, decimal_digits)
def do_sum(a: int | float, b: int | float) -> int | float:
    return a + b

def do_difference(a: int | float, b: int | float) -> int | float:
    return a - b

def do_abs_sum(a: int | float, b: int | float) -> int | float:
    return abs(a) + abs(b)

def do_percentage(dividend: int | float, divisor: int | float, decimal_digits: int = 1) -> int | float:
    result =  round((dividend / divisor) * 100, decimal_digits)
    abs_result = abs(result)
    return 0.0 if abs_result == 0.0 else result
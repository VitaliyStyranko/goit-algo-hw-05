import re
from typing import Callable

text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, "
        "доповнений додатковими надходженнями 27.45 і 324.00 доларів.")


def generator_numbers(text: str):
    # Regular expression to find valid numbers (including decimals)
    pattern = r'\b\d+\.\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable):
    numbers_generator = func(text)  # Call the generator function
    total_sum = sum(numbers_generator)  # Calculate the sum using the generator
    return total_sum


total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")

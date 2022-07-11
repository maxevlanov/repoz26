numbers: list[list[int]] = [
    [1, 5, -2, 4, -8],
    [1, 5, -2, 4, -8],
    [1, 5, -2, 4, -8],
    [1, 5, -2, 4, -8],
    [1, 5, -2, 4, -8],
]


def get_abs_numbers(numbers: list[list[int]]) -> int:
    count: int = 0
    for raw in numbers:
        for number in raw:
            if number < 0 and number % 2:
                count += number


return count * -1

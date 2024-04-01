"""Utils exercise."""

__author__ = "730431261"


def all(input0: list[int], inputint: int) -> bool:
    """All Function."""
    if len(input0) == 0:
        return False
    index = 0
    if input0[index] == inputint:
        index += 1
        return True
    else:
        return False


def max(input: list[int]) -> int:
    """Max Function."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    largest_number = input[0]
    for number in input:
        if number > largest_number:
            largest_number = number
    return largest_number
    

def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Is Equal Function."""
    if input1 == input2:
        return True
    else:
        return False


def extend(input3: list[int], input4: list[int]) -> None:
    """Extend Function."""
    for number in input4:
        input3.append(number)

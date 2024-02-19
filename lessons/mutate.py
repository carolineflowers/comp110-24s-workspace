"""Mutating functions."""
__author__ = "730431261"


def manual_append(the_list: list[int], number: int) -> None:
    """Manual append function."""
    the_list.append(number)


def double(the_list: list[int]) -> None:
    """Double function."""
    index = 0
    while index < len(the_list):
        the_list[index] *= 2
        index += 1

"""Summing the elements of a list using different loops."""

__author__ = "730431261"


def w_sum(vals: list[float]) -> float:
    """While loops to iterate through vals."""
    index = 0
    sum = 0.0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """For...in... loop to iterate through vals."""
    sum = 0.0
    for value in vals:
        sum += value
    return sum


def f_range_sum(vals: list[float]) -> float:
    """For...in range(0,len(xs)) to iterate through vals."""
    sum = 0.0
    for value in range(len(vals)):
        sum += vals[value]
    return sum
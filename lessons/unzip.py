"""Splitting a dictionary into two lists."""

__author__ = "730431261"


def get_keys(keys: dict[str, int]) -> list[str]:
    """Get keys."""
    return list(keys.keys())


def get_values(values: dict[str, int]) -> list[int]:
    """Get values."""
    return list(values.values())

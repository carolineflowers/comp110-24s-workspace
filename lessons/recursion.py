"""CQ07: Writing a Recursive Function."""

__author__ = "730431261"


def f(n: int, k: int) -> int:
    """Recursive function."""
    if n == 0:      # base case
        return 0
    else:        # recursive rule
        return k + f(n - 1, k)
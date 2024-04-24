"""CQ08: Practice with OOP."""

from __future__ import annotations

__author__ = "730431261"


class Point:   # class Point
    """Poinit x and y."""
    def __init__(self, x_init: float, y_init: float):    # constructor with attributes x and y that are floats
        """Function assigns initial x and y values."""
        self.x = x_init   # assigns initial value for attribute x -- do self. first (refer to instantiating.py from class the other day)
        self.y = y_init    # assigns initial value for attribute y
        
    def scale_by(self, factor: int) -> None:     # method scale_by with parameters self and factor: int return None
        """Update x and y attributes."""
        self.x *= factor     # update x attribute to x = x * factor
        self.y *= factor      # update y attribute to y = y * factor

    def scale(self, factor: int) -> Point:    # method scale with parameters self and factor: int return Point
        """Return new point with new x and y."""
        return Point(self.x * factor, self.y * factor)     # return a new Point with x and y attributes equal to self.x * factor and self.y * factor
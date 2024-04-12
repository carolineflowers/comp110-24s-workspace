"""Check Methods for CQ08."""

from lessons.CQ08.point import Point

point = Point(2.5, 3.5)
print("Original Point:", point.x, point.y)

point.scale_by(2)
print("Scaled by 2:", point.x, point.y)

scaled_point = point.scale(3)
print("Scaled by 3 (new Point):", scaled_point.x, scaled_point.y)
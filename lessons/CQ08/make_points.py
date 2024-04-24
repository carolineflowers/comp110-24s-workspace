"""Check Methods for CQ08."""

from lessons.CQ08.point import Point

point = Point(11, 11)   # sets original point as x = 11 and y = 11
print("Original Point:", point.x, point.y)   # prints points 11,11

point.scale_by(222)    # scales the points by 222
print("Scaled by 222:", point.x, point.y)    # prints the scaled version of 11, 11 by 222

scaled_point = point.scale(555)   # new scaled point by 555
print("Scaled by 555 (new Point):", scaled_point.x, scaled_point.y)   # prints the scaled point by 555
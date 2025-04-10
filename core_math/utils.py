from numpy import (sin, cos, deg2rad)
from primitives import (Point, Line)


def angle_upcast(angle: float) -> float:
    """Scale the angle to values within [-180, 180]."""

    return (angle + 180) % 360 - 180


def get_point(begin: Point, angle: float, dist: float) -> Point:
    """
    Adds dX to the initial X and dY to Y. dX and dY are calculated by finding their projections on the vertical.

    Arguments:
        begin -- first.
        angle -- the angle between vertical and vector of displacement.
        dist -- displacement module (distance from beginning point to the target point).

    Returns target point.
    """

    angle = deg2rad(angle)
    return Point(begin.x + dist * sin(angle), begin.y + dist * cos(angle))


def get_intersection_point(
        line1: Line,
        line2: Line
) -> Point | None:
    """
    Arguments:
        x1, y1 -- first point coordinates
        x2, y2 -- second point coordinates

    Returns the coordinates of the intersection of two lines.
    """

    pass





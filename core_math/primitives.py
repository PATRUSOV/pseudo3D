from typing import NamedTuple


class Point(NamedTuple):
    """2D point."""

    x: int | float
    y: int | float


class Line:
    """2D line."""

    def __init__(self, begin: Point, end: Point):
        self.begin = begin
        self.end = end

    def length(self) -> float:
        return ((self.end.x - self.begin.x) ** 2 + (self.end.y - self.begin.y) ** 2) ** 0.5

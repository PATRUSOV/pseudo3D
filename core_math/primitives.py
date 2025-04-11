from typing import NamedTuple


class Point(NamedTuple):
    """Двумерная точка"""

    x: int | float
    y: int | float


class Line:
    """Линия на плоскости."""

    def __init__(self, begin: Point, end: Point):
        self.begin = begin
        self.end = end

    def length(self) -> float:
        return ((self.end.x - self.begin.x) ** 2 + (self.end.y - self.begin.y) ** 2) ** 0.5

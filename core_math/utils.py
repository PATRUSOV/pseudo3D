from numpy import (sin, cos, deg2rad, isclose)
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


def get_lines_intersection(line1: Line, line2: Line) -> Point | None:
    # ПИСАЛА НЕЙРОНКА
    """
    Находит точку пересечения двух бесконечных прямых.

    Аргументы:
        line1: Первая прямая (определяется двумя точками)
        line2: Вторая прямая (определяется двумя точками)

    Возвращает:
        Точку пересечения или None, если прямые параллельны или совпадают
    """
    # Вычисляем коэффициенты уравнений прямых
    A1 = line1.end.y - line1.begin.y
    B1 = line1.begin.x - line1.end.x
    C1 = A1 * line1.begin.x + B1 * line1.begin.y

    A2 = line2.end.y - line2.begin.y
    B2 = line2.begin.x - line2.end.x
    C2 = A2 * line2.begin.x + B2 * line2.begin.y

    # Вычисляем определитель
    denominator = A1 * B2 - A2 * B1

    if isclose(denominator, 0.0, atol=1e-9):
        return None

    # Вычисляем координаты точки пересечения
    x = (B2 * C1 - B1 * C2) / denominator
    y = (A1 * C2 - A2 * C1) / denominator

    return Point(x, y)

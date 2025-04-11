from numpy import (sin, cos, deg2rad, isclose)
from primitives import (Point, Line)


def angle_upcast(angle: float) -> float:
    """
    Приводит угол к диапазону [-180, 180].

    Аргументы:
        angle: Угол любой величины

    """

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
    """
    Находит точку пересечения двух бесконечных прямых.

    Аргументы:
        line1: Первая прямая (определяется двумя точками)
        line2: Вторая прямая (определяется двумя точками)

    Возвращает:
        Точку пересечения или None, если прямые параллельны или совпадают
    """
    A1 = line1.end.y - line1.begin.y
    B1 = line1.begin.x - line1.end.x
    C1 = A1 * line1.begin.x + B1 * line1.begin.y

    A2 = line2.end.y - line2.begin.y
    B2 = line2.begin.x - line2.end.x
    C2 = A2 * line2.begin.x + B2 * line2.begin.y

    denominator = A1 * B2 - A2 * B1

    if isclose(denominator, 0.0, atol=1e-9):
        return None

    return Point(
        (B2 * C1 - B1 * C2) / denominator,
        (A1 * C2 - A2 * C1) / denominator
    )


def is_point_on_line(point: Point, line: Line) -> bool:
    """
    Проверяет, лежит ли точка на прямой, заданной двумя точками.

    Параметры:
        point: Проверяемая точка (Point)
        line: Прямая (Line), заданная двумя точками

    Возвращает:
        bool: True если точка на прямой (с погрешностью 1e-9)
    """
    x1, y1 = line.begin.x, line.begin.y
    x2, y2 = line.end.x, line.end.y

    cross = (y2 - y1) * (point.x - x1) - (x2 - x1) * (point.y - y1)

    return isclose(cross, 0.0, atol=1e-9)



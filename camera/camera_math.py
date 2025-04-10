from core_math.utils import (get_point, angle_upcast)
from core_math.primitives import (Point, Line)
from numpy import (deg2rad, sin, cos)


class _render:

    def __init__(self):
        self._dist_to_normal_line = 5


def _get_normal_line_points(self) -> tuple[tuple[float, float], tuple[float, float], tuple[float, float]]:
    dist_to_left = dist_to_right = self._dist_to_normal_line / cos(self._fov / 2)
    left_angle = self._gaze_direction - self._fov / 2
    right_angle = self._gaze_direction + self._fov / 2

    left = get_point(self._X, self._Y, left_angle, dist_to_left)
    middle = get_point(self._X, self._Y, self._gaze_direction, self._dist_to_normal_line)
    right = get_point(self._X, self._Y, right_angle, dist_to_right)
    return left, middle, right


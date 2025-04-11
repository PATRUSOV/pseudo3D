from core_math.utils import (get_point, get_lines_intersection)
from core_math.primitives import (Point, Line)
from numpy import (sin, cos)


class CameraRender:
    from .__init__ import Camera
    def __init__(self, camera: Camera):
        self.camera = camera

    def calculate(self) -> None:
        self._get_normal_line_points()

    def _get_normal_line_points(self) -> None:
        dist_to_left = dist_to_right = self.camera.state.dist_to_normal_line / cos(self.camera.state.fov / 2)
        left_angle = self.camera.state.gaze_direction - self.camera.state.fov / 2
        right_angle = self.camera.state.gaze_direction + self.camera.state.fov / 2

        self.normal_left: Point = get_point(self.camera.state.position, left_angle, dist_to_left)
        self.normal_mid: Point = get_point(self.camera.state.position, self.camera.state.gaze_direction,
                                           self.camera.state.dist_to_normal_line)
        self.normal_right: Point = get_point(self.camera.state.position, right_angle, dist_to_right)

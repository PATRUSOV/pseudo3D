from graphic import MainWindow
from exceptions import *
from world import World


class Camera:
    """Сущность на которую проецируются объекты"""

    def __init__(self) -> None:

        # Модули камеры
        from .state import CameraState
        self.state = CameraState(self)
        from .render import CameraRender
        self.render = CameraRender(self)

    def set_speed(self, speed: float) -> None:
        """
        Устанавливает количество единиц пути проходимых за шаг.

        Аргументы:
            speed: скорость, диапазоне [0; inf]
        """
        if speed < 0:
            raise IncorrectValue("The speed value cannot be less than zero.")
        self.state.speed = speed

    def set_dist_to_normal_line(self, dist: float):
        """
        Устанавливает расстояние от камеры до линии нормали.

        Аргументы:
            dist: расстояние, в диапазоне [0; inf]
        """
        if dist < 0:
            raise IncorrectValue(
                "The engine does not work with a negative distance from the camera to the line of normal.")
        self.state.dist_to_normal_line = dist

    def set_gaze_direction(self, angle: float) -> None:
        """
        Устанавливает направление взгляда.

        Аргументы:
            angle: Угол между вертикалью и вектором взгляда, в диапазоне [-180; 180].
        """

        self.state.gaze_direction = (angle + 180) % 360 - 180

    def set_fov(self, angle: float, radius: float) -> None:
        """
        Устанавливает угол и радиус обзора камеры.

        Аргументы:
            angle: угол обзора (fov)
            radius: радиус обзора
        """
        self.state.fov = angle
        self.state.radius_of_view = radius

    def goto(self, X: float, Y: float) -> None:
        """
        Перемещает камеру в заданную точку.
        """
        # if X > self.__world._length or Y > self.__world._width:
        #    raise IncorrectValue("You can't go over the world's borders.")
        self.state.position.x = X
        self.state.position.y = Y

    def turn(self, angle: float):
        self.state.gaze_direction += angle
        self.state.gaze_direction = (self.state.gaze_direction + 180) % 360 - 180

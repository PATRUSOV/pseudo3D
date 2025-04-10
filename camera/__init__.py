from graphic import MainWindow
from exceptions import *
from world import World



class Camera:
    """
        The camera is the entity onto which the steel objects are projected
    """

    def __init__(self, X: float, Y: float) -> None:
        self._X: float = X
        self._Y: float = Y
        self._gaze_direction = 0
        """
        The angle between the vertical perpendicular, and the view vector.
        In the range [-180; 180].
        """
        self.__world = World()
        self.__window = MainWindow()

    def set_speed(self, speed: int) -> None:
        """
        Sets the number of units traversed per step.
        """
        if speed < 0:
            raise IncorrectValue("The speed value cannot be less than zero.")
        self._speed = speed

    def set_dist_to_normal_line(self, dist: int):
        """
        Sets the distance from the camera to the normal line. 
        """
        if dist < 0:
            raise IncorrectValue(
                "The engine does not work with a negative distance from the camera to the line of normal.")
        self._dist_to_normal_line = dist

    def set_gaze_direction(self, angle: int) -> None:
        """
        Sets the direction of gaze.

        Arguments:
            angle -- The angle between the vertical perpendicular, and the view vector.
            In the range [-180; 180].
        """

        self._gaze_direction = (angle + 180) % 360 - 180

    def set_fov(self, angle: int, radius: int) -> None:
        self._fov = angle
        self._radius_of_view = radius

    def goto(self, X: int, Y: int) -> None:
        """
        Moves the camera to a point
        """
        if X > self.__world._length or Y > self.__world._width:
            raise IncorrectValue("You can't go over the world's borders.")
        self._X = X
        self._Y = Y

    def move(self) -> None:
        self._X += sin(deg2rad(self._gaze_direction)) * self._speed
        self._Y += cos(deg2rad(self._gaze_direction)) * self._speed

    def turn(self, angle: float):
        self._gaze_direction += angle
        self._gaze_direction = (self._gaze_direction + 180) % 360 - 180



    def draw(self):
        self.__window.clear()
        self.__window.circle(self._X, self._Y, 5)
        self.__window.circle(self._X, self._Y, 1)

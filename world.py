from exceptions import *
from core_math.primitives import Point


class _world:
    """
    Main game class.
    """

    _object = None

    def __init__(self):
        self._length: float = 800
        self._width: float = 600
        self.MAP: dict[Point, list[Point]] = {
            Point(1, 10): [Point(100, 5), Point(25, 10)],
            Point(100, 5): [Point(4, 10)]
        }

    def get_size(self) -> tuple[float, float]:
        """
        Get the width and length of the world.
        """
        return self._length, self._width

    def set_size(self, length: int, wight: int) -> None:
        """
        Set the width and length of the world.

        Arguments:
            length, wight -- must be => 0
        """
        if length <= 0 or wight <= 0:
            raise IncorrectValue("Negative coordinates cannot be entered")
        self._length = length
        self._width = wight

    def lead_objects(self) -> None:
        pass


def World() -> _world:
    """
    Singleton to interact with the _world.
    """
    if _world._object == None:
        _world._object = _world()
    return _world._object

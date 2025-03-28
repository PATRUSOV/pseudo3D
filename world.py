from exceptions import *

class _world:
    """
    Main game class.
    """

    _object = None

    def __init__(self):
        self._length = 800
        self._width = 600
        MAP = {
            (4, 10): [(100, 5), (25, 10)], 
            (100, 5) : [(4, 10)]
        }

    def get_size(self) -> tuple[int, int]:
        """
        Get the width and length of the world.
        """
        return (self._X, self._Y)

    def set_size(self, length:int, wight:int) -> None:
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
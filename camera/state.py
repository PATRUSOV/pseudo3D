class _camera_state:

    def __init__(self):
        self._X: float = 0
        self._Y: float = 0
        self._gaze_direction = 0
        """
        The angle between the vertical perpendicular, and the view vector.
        In the range [-180; 180].
        """
        self._speed: float = 0
        self._dist_to_normal_line: float = 0
        """
        Дистанция от камеры до линии нормали. 
        В диапазоне [0; inf)
        """
        self._fov = 0
        self._radius_of_view = 0
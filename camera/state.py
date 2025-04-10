class CameraState:

    from .__init__ import Camera
    def __init__(self, camera: Camera):

        from core_math.primitives import Point
        self.position: Point = Point(0, 0)
        self.gaze_direction: float = 0
        """
        The angle between the vertical perpendicular, and the view vector.
        In the range [-180; 180].
        """
        self.speed: float = 0
        self.dist_to_normal_line: float = 0
        """
        Дистанция от камеры до линии нормали. 
        В диапазоне [0; inf)
        """
        self.fov = 0
        self.radius_of_view = 0
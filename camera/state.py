class CameraState:
    """Класс для хранения состояния камеры"""

    from .__init__ import Camera
    def __init__(self, camera: Camera):
        self.camera = camera

        from core_math.primitives import Point
        self.position: Point = Point(0, 0)
        self.gaze_direction: float = 0
        """
        Угол между вертикалью и вектором взгляда, в диапазоне [-180; 180]
        """
        self.speed: float = 0
        self.dist_to_normal_line: float = 0
        """
        Дистанция от камеры до линии нормали, диапазоне [0; inf]
        """
        self.fov = 0
        self.radius_of_view = 0

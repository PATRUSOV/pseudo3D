def move(self) -> None:
    self._X += sin(deg2rad(self.gaze_direction)) * self.speed
    self._Y += cos(deg2rad(self.gaze_direction)) * self.speed

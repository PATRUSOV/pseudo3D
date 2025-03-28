import numpy
from time import time

def angle_upcast(angle: float) -> float:
    return (angle + 180) % 360 - 180

STEP_ANGLE_TABLE = 5
ANGLES = numpy.arange(-180, 181, STEP_ANGLE_TABLE)
RADS = numpy.deg2rad(ANGLES)
SIN_TABLE = {angle: numpy.float32(numpy.sin(rad)) for angle, rad in zip(ANGLES, RADS)}
COS_TABLE = {angle: numpy.float32(numpy.cos(rad)) for angle, rad in zip(ANGLES, RADS)}

def sin(angle: float) -> float:
    angle = angle_upcast(angle)
    if angle % STEP_ANGLE_TABLE == 0:
        return SIN_TABLE[angle]

    lower_angle = angle - (angle % STEP_ANGLE_TABLE)
    upper_angle = lower_angle + STEP_ANGLE_TABLE
    factor = (angle - lower_angle) / STEP_ANGLE_TABLE
    return SIN_TABLE[lower_angle] + factor * (SIN_TABLE[upper_angle] - SIN_TABLE[lower_angle])

def speed(func) -> float:
    start = time()
    func()
    return time() - start


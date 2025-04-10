from time import time


def speed(func) -> float:
    start = time()
    func()
    return time() - start

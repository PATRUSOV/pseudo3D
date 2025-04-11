import turtle


class _MainWindow(turtle.Turtle):
    """
    Класс для взаимодействия с библиотекой отрисовки.
    """

    _object = None

    def __init__(self):
        self.screen = turtle.Screen()
        # ПЕРЕПИСАТЬ
        super().__init__(visible=False)
        self.speed(0)

    def bgcolor(self, color: str) -> None:
        self.screen.bgcolor(color)

    def title(self, name: str) -> None:
        self.screen.title(name)

    def setup(self, width: int = 500, height: int = 500) -> None:
        self.screen.setup(width=width, height=height)

    def close(self) -> None:
        self.screen.bye()

    def listen(self) -> None:
        self.screen.listen()

    def key_bind(self, func, key: str):
        self.screen.onkey(func, key)

    def Done(self) -> None:
        """
        Fixes the canvas to finalize the work with the window.
        """
        turtle.done()

    # КОСТЫЛЬ
    def circle(self, X: float, Y: float, radius: float) -> None:
        super().penup()
        super().goto(X, Y - radius)
        super().pendown()
        super().circle(radius)

    # КОСТЫЛЬ
    def line(self, X1: float, Y1: float, X2: float, Y2: float) -> None:
        self.penup()
        self.goto(X1, Y1)
        self.pendown()
        self.goto(X2, Y2)

    # КОСТЫЛЬ
    def clear(self):
        super().clear()


def MainWindow() -> _MainWindow:
    if _MainWindow._object is None:
        _MainWindow._object = _MainWindow()
    return _MainWindow._object

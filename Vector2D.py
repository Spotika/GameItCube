import math


class Vector2D:
    """Двумерный радиус-вектор"""

    _x: float
    _y: float

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)):
            self._x = value
        else:
            raise ValueError

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)):
            self._y = value
        else:
            raise ValueError

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def get_len(self) -> float:
        """возвращает длину вектора"""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __abs__(self) -> float:
        """возвращает длину вектора"""
        return self.get_len()

    def __len__(self) -> float:
        """возвращает длину вектора"""
        return self.get_len()

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float):
        return Vector2D(self.x * other, self.y * other)

    def __str__(self):
        return f"vector {self.x}, {self.y}"

    @classmethod
    def from_polar(cls, tetha: float, r: float):
        return Vector2D(r * math.cos(tetha), r * math.sin(tetha))

    def zero(self):
        """Обнуляет вектор"""
        self.x = 0
        self.y = 0

    def __call__(self):
        return self.x, self.y

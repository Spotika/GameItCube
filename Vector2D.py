import math


class Vector2D:
    """Двумерный радиус-вектор"""

    x: float
    y: float

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
    def from_polar(cls, teta: float, r: float):
        return Vector2D(r * math.cos(teta), r * math.sin(teta))

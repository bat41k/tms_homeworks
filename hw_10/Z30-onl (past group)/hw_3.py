# Импортировать из base.py класс Shape и унаследовать класс Circle.
# Реализовать конструктор (__init__) (подумать, какие параметры нужны при создании объекта) и
# метод get_area.
# Реализовать методы сложения и вычитания объектов,
# результатом которых будет новое значение площади (объекты при этом не меняются).
# Написать проверки.

from base import Shape
import math


class Circle(Shape):
    def __init__(self, radius: int | float) -> None:
        self.radius = radius

    def get_area(self) -> int | float:
        return round(math.pi * self.radius ** 2, 2)

    def __add__(self, other: Shape) -> int | float:
        if isinstance(other, Circle):
            return self.get_area() + other.get_area()
        else:
            raise TypeError

    def __sub__(self, other: Shape) -> int | float:
        if isinstance(other, Circle):
            return self.get_area() - other.get_area()
        else:
            raise TypeError


circle_1 = Circle(radius=1)
circle_2 = Circle(radius=2)

if __name__ == '__main__':
    assert circle_1.get_area() == 3.14
    assert circle_2.get_area() == 12.57

    assert circle_1 + circle_2 == 15.71
    assert circle_2 - circle_1 == 9.43
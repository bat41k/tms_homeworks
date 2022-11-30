# Импортировать из base.py класс Shape и унаследовать класс Rectangle.
# Реализовать конструктор (__init__) (подумать, какие параметры нужны при создании объекта) и
# метод get_area.
# Реализовать методы сложения и вычитания объектов,
# результатом которых будет новое значение площади (объекты при этом не меняются).
# Написать проверки.

from base import Shape


class Rectangle(Shape):
    def __init__(self, length: int | float, width: int | float) -> None:
        self.length = length
        self.width = width

    def get_area(self) -> int | float:
        return self.length * self.width

    def __add__(self, other: Shape) -> int | float:
        if isinstance(other, Rectangle):
            return self.get_area() + other.get_area()
        else:
            raise NotImplemented

    def __sub__(self, other: Shape) -> int | float:
        if isinstance(other, Rectangle):
            return self.get_area() - other.get_area()
        else:
            raise NotImplemented


rectangle_1 = Rectangle(length=1, width=2)
rectangle_2 = Rectangle(length=3, width=4)

assert rectangle_1.get_area() == 2
assert rectangle_2.get_area() == 12

assert rectangle_1 + rectangle_2 == 14
assert rectangle_2 - rectangle_1 == 10
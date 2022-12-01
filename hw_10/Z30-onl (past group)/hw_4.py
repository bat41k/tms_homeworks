# Реализовать класс Box, который принимает в себя экземпляры класса Shape.
# Реализовать методы
# - add_shape - добавляет фигуру в текущую коллекцию
# - remove_shape - удаляет последн добавленную фигуру
# - get_common_area - возвращает общую площадь всех фигур

from base import Shape
from hw_2 import Rectangle
from hw_3 import Circle


class Box:
    def __init__(self, shapes: list = None) -> None:
        self._shapes = shapes if shapes else []

    def add_shape(self, shape: Shape) -> None:
        if isinstance(shape, Shape):
            self._shapes.append(shape)
        else:
            raise TypeError('Unsupported classes cannot be added')

    def remove_shape(self) -> None:
        del self._shapes[-1]

    def get_common_area(self) -> int | float:
        return round(sum([s.get_area() for s in self._shapes]), 2)


box = Box()

box.add_shape(Rectangle(length=5, width=6))
box.add_shape(Circle(radius=3))

if __name__ == '__main__':
    assert box.get_common_area() == 58.27
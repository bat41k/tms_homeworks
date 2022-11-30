# Реализовать базовый класс Shape.
# Должен предоставлять в качестве интерфейса метод get_area.
# Класс положить в отдельный модуль base.py

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        raise NotImplementedError
from hw_1 import Auto
from time import sleep


class Truck(Auto):
    def __init__(self, brand: str, age: int, color: str, mark: str, weight: int, max_load: int) -> None:
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load

    def drive(self) -> None:
        print(f'Attention!')
        super().drive()

    @staticmethod
    def load() -> None:
        sleep(1)
        print('load')
        sleep(1)


class Sedan(Auto):
    def __init__(self, brand: str, age: int, color: str, mark: str, weight: int, max_speed: int) -> None:
        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed

    def drive(self) -> None:
        super().drive()
        print(f'Max speed of sedan {self.brand} {self.mark} is {self.max_speed}')


mercedes = Truck(brand='Mercedes', age=1, color='black', mark='Actros', weight=10000, max_load=20000)
iveco = Truck(brand='Iveco', age=1, color='white', mark='S-Way', weight=10000, max_load=20000)

bmw = Sedan(brand='BMW', age=1, color='black', mark='M8', weight=2000, max_speed=300)
volkswagen = Sedan(brand='Volkswagen', age=1, color='white', mark='Golf GTI', weight=2000, max_speed=300)

print(mercedes.__dict__)
mercedes.load()
mercedes.drive()
mercedes.stop()
mercedes.use()
assert mercedes.age == 2

print(iveco.__dict__)
iveco.load()
iveco.drive()
iveco.stop()
iveco.use()
assert iveco.age == 2

print(bmw.__dict__)
bmw.drive()
bmw.stop()
bmw.use()
assert bmw.age == 2

print(volkswagen.__dict__)
volkswagen.drive()
volkswagen.stop()
volkswagen.use()
assert volkswagen.age == 2
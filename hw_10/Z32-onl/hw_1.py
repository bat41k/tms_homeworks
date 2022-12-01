class Auto:
    def __init__(self, brand: str, age: int, color: str, mark: str, weight: int) -> None:
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def drive(self) -> None:
        print(f'Car {self.brand} {self.mark} drives')

    def stop(self) -> None:
        print(f'Car {self.brand} {self.mark} stops')

    def use(self) -> None:
        self.age += 1


audi = Auto(brand='Audi', age=1, color='black', mark='RS6', weight=2000)

if __name__ == '__main__':
    audi.drive()
    audi.stop()
    audi.use()
    assert audi.age == 2
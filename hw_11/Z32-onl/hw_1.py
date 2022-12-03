from dataclasses import dataclass


@dataclass
class Dish:
    name: str
    price: int
    weight: int
    amount: int


class Order:
    def __init__(self) -> None:
        self._dishes = []
        self.__remainder = 0

    def add_dish(self, dish: Dish) -> None:
        if isinstance(dish, Dish):
            self._dishes.append(dish)
        else:
            raise TypeError('Only dishes can be added to the order')

    @property
    def total_price(self) -> int:
        return sum([d.price * d.amount for d in self._dishes])

    @property
    def total_amount(self) -> int:
        return sum([d.amount for d in self._dishes])

    @property
    def total_weight(self) -> int:
        return sum([d.weight * d.amount for d in self._dishes])

    @property
    def remainder(self) -> int:
        return self.__remainder

    def payment(self, money: int) -> None:
        self.__remainder = self.total_price - money


order = Order()

order.add_dish(Dish(name='khinkali', price=14, weight=400, amount=1))
order.add_dish(Dish(name='kharcho', price=9, weight=250, amount=2))
order.add_dish(Dish(name='khachapuri', price=11, weight=300, amount=3))

if __name__ == '__main__':
    assert order.total_price == 65
    assert order.total_amount == 6
    assert order.total_weight == 1800
    order.payment(50)
    assert order.remainder == 15
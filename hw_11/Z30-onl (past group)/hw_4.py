# Есть класс Account.
# Конструктор принимает person_id (уникальный), currency (реализовать через enum) и amount (кол-во денег на счету).
# Person_id можно релазиовать через uuid4.
# Реализовать свойство amount, которое при попытке записать в значение сумму <0 - выдает ошибку (либо предупреждение и
# не меняет значение)
# См. getter/setter

from enum import Enum
import uuid


class Currency(Enum):
    belarussian_ruble = 'BYN'
    dollar = 'USD'
    euro = 'EUR'


class Account:
    def __init__(self, person_id: uuid, currency: str, amount: int | float) -> None:
        self.person_id = person_id
        self.currency = currency
        self._amount = amount if amount > 0 else 0

    @property
    def amount(self) -> int | float:
        return self._amount

    @amount.setter
    def amount(self, new_amount: int | float) -> None:
        if new_amount < 0:
            print('Баланс не может быть отрицательным')
        else:
            self._amount = new_amount


Person = Account(person_id=uuid, currency=Currency.belarussian_ruble.value, amount=100)
Person.amount = -100

assert Person.amount == 100
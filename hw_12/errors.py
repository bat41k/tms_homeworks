from dataclasses import dataclass


class InputFormulaError(Exception):
    ...


class InputNumberError(Exception):
    ...


class InputOperatorError(Exception):
    ...


class InvalidLogin(Exception):
    ...


class InvalidPassword(Exception):
    ...


class InvalidEmail(Exception):
    ...


class ValidationError(Exception):
    ...


@dataclass
class InvalidIntDivision(Exception):
    value: int
    name: str = 'InvalidIntDivision'

    def __str__(self):
        return f'{self.name} -> {self.value}'


@dataclass
class InvalidIntLength(Exception):
    value: int
    name: str = 'InvalidIntLength'

    def __str__(self):
        return f'{self.name} -> {self.value}'


@dataclass
class InvalidFloatLength(Exception):
    value: float
    name: str = 'InvalidFloatLength'

    def __str__(self):
        return f'{self.name} -> {self.value}'


@dataclass
class InvalidStrLength(Exception):
    value: str
    name: str = 'InvalidStrLength'

    def __str__(self):
        return f'{self.name} -> {self.value}'


@dataclass
class InvalidDuplicate(Exception):
    value: int | float | str
    name: str = 'InvalidDuplicate'

    def __str__(self):
        return f'{self.name} -> {self.value}'
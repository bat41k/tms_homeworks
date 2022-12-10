from errors import InputFormulaError, InputNumberError, InputOperatorError


class Calculator:
    operators = ['+', '-', '*', '/', '**']
    operation = {'+': lambda a, b: a + b,
                 '-': lambda a, b: a - b,
                 '*': lambda a, b: a * b,
                 '/': lambda a, b: a / b,
                 '**': lambda a, b: a ** b,
                 }

    @classmethod
    def data_validation(cls, data: str) -> tuple:
        data = data.split()

        if len(data) != 3:
            raise InputFormulaError
        else:
            o_1, op, o_2 = data

        try:
            o_1, o_2 = float(o_1), float(o_2)
        except ValueError:
            raise InputNumberError

        if op not in cls.operators:
            raise InputOperatorError

        return o_1, op, o_2


if __name__ == '__main__':
    while True:
        data_from_user = input('Enter data in the format "operand_1 operator operand_2": ')

        if data_from_user == 'quit':
            print('Calculator closed')
            break
        else:
            operand_1, operator, operand_2 = Calculator.data_validation(data_from_user)
            result = Calculator.operation[operator](operand_1, operand_2)
            print(result)
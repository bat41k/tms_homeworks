from errors import InvalidIntDivision, InvalidIntLength, InvalidFloatLength, InvalidStrLength, InvalidDuplicate


class Queue:
    queue = []

    @classmethod
    def add(cls, *args) -> None:
        for value in args:
            if value not in cls.queue:
                if isinstance(value, int):
                    Queue.validate_int(value)
                if isinstance(value, float):
                    Queue.validate_float(value)
                if isinstance(value, str):
                    Queue.validate_str(value)
            else:
                print(InvalidDuplicate(value))

    @classmethod
    def validate_int(cls, value: int) -> None:
        if value % 8 == 0:
            if len(str(value)) < 5:
                cls.queue.append(value)
            else:
                print(InvalidIntLength(value))
        else:
            print(InvalidIntDivision(value))

    @classmethod
    def validate_float(cls, value: float) -> None:
        if len(str(value).split('.')[1]) < 3:
            cls.queue.append(value)
        else:
            print(InvalidFloatLength(value))

    @classmethod
    def validate_str(cls, value: str) -> None:
        if len(value) < 5:
            cls.queue.append(value)
        else:
            print(InvalidStrLength(value))


if __name__ == '__main__':
    Queue.add(1, 8, 10000, 1.11, 1.111, 'str', 'string', 8)
    print(Queue.queue)
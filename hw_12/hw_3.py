from errors import InvalidIntDivision, InvalidIntLength, InvalidFloatLength, InvalidStrLength, InvalidDuplicate


class Queue:
    queue = []

    @classmethod
    def add(cls, *args) -> None:
        for value in args:
            if value not in cls.queue:
                if isinstance(value, int) and cls.validate_int(value):
                    cls.queue.append(value)
                if isinstance(value, float) and cls.validate_float(value):
                    cls.queue.append(value)
                if isinstance(value, str) and cls.validate_str(value):
                    cls.queue.append(value)
            else:
                print(InvalidDuplicate(value))

    @classmethod
    def validate_int(cls, value: int) -> bool:
        if value % 8 == 0:
            if len(str(value)) < 5:
                return True
            else:
                print(InvalidIntLength(value))
                return False
        else:
            print(InvalidIntDivision(value))
            return False

    @classmethod
    def validate_float(cls, value: float) -> bool:
        if len(str(value).split('.')[1]) < 3:
            return True
        else:
            print(InvalidFloatLength(value))
            return False

    @classmethod
    def validate_str(cls, value: str) -> bool:
        if len(value) < 5:
            return True
        else:
            print(InvalidStrLength(value))
            return False


if __name__ == '__main__':
    Queue.add(1, 8, 10000, 1.11, 1.111, 'str', 'string', 8)
    print(Queue.queue)
class Deque:
    deque = []

    @classmethod
    def append_left(cls, instance) -> None:
        if isinstance(instance, DataObject):
            if len(cls.deque) < 5:
                cls.deque.insert(0, instance)
            else:
                print('The queue is full')
        else:
            raise TypeError('Unsupported classes cannot be added')

    @classmethod
    def append_right(cls, instance) -> None:
        if isinstance(instance, DataObject):
            if len(cls.deque) < 5:
                cls.deque.append(instance)
            else:
                print('The queue is full')
        else:
            raise TypeError('Unsupported classes cannot be added')

    @classmethod
    def pop_left(cls) -> object:
        return cls.deque.pop(0)

    @classmethod
    def pop_right(cls) -> object:
        return cls.deque.pop()


class DataObject:
    data = 'information'


in_1 = DataObject()
in_2 = DataObject()

if __name__ == '__main__':
    Deque.append_right(in_1)
    Deque.append_left(in_2)
    print(Deque.pop_right())
    print(Deque.pop_left())
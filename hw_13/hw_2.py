from typing import Iterator


class MySquareIterator:
    def __init__(self, collection: list[int]) -> None:
        self.collection = collection
        self.counter = 0

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.counter < len(self.collection):
            square_number = self.collection[self.counter] ** 2
            self.counter += 1
            return square_number
        raise StopIteration


if __name__ == '__main__':
    itr = MySquareIterator([1, 2, 3, 4, 5])

    for number in itr:
        print(number)
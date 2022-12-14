from typing import Iterator


class EvenRange:
    def __init__(self, start: int, end: int) -> None:
        self.start = start if start % 2 == 0 else start + 1
        self.end = end

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.start <= self.end:
            number_even = self.start
            self.start += 2
            return number_even
        print('Out of number!')
        raise StopIteration


if __name__ == '__main__':
    er1 = EvenRange(7, 11)
    print(next(er1))
    print(next(er1))
    print(next(er1))

    # er2 = EvenRange(3, 14)
    #
    # for number in er2:
    #     print(number)
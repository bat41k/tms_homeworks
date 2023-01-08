from typing import Generator
from time import sleep


def endless_fib_generator() -> Generator:
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    gen = endless_fib_generator()
    counter = -1

    while True:
        sleep(1)
        counter += 1
        print(f'Fibonacci number "{counter + 1}" — {next(gen)}')
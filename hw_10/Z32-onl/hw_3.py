class Counter:
    def __init__(self, start: int = 0, stop: int = -1) -> None:
        self.start = start
        self.stop = stop

    def increment(self) -> None:
        self.start += 1

    def get(self) -> None:
        if self.start == self.stop:
            print('Maximal value is reached')
        else:
            print(self.start)


c = Counter(start=1, stop=10)

if __name__ == '__main__':
    c.increment()
    c.get()
class Counter:
    def __init__(self, start: int = '', stop: int = '') -> None:
        self.start = start if start else 0
        self.stop = stop

    def increment(self) -> None:
        while True:
            if self.stop == self.start:
                c.get()
                break
            else:
                self.start += 1

    @staticmethod
    def get() -> None:
        print('Maximal value is reached')


c = Counter(start=1, stop=10)
c.increment()
class ft_range:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            stop = start
            start = 0
        if step == 0:
            raise ValueError("range() arg 3 must not be zero")
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if ((self.step > 0 and self.current >= self.stop)
                or (self.step < 0 and self.current <= self.stop)):
            raise StopIteration
        v = self.current
        self.current += self.step
        return v

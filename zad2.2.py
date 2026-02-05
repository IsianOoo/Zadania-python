class PowerGenerator:
    def __init__(self, a, n):
        self.a = a
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        val = self.a ** self.i
        self.i += 1
        return val


if __name__ == "__main__":
    print("2.2 test:")
    g = PowerGenerator(2, 8)
    print(list(g))

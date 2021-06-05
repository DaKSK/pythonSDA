class EvensAndOdds:

    def __init__(self, start, end, mode):
        self.current = start
        self.end = end
        self.even = mode

    def __iter__(self):
        return self

    def is_even(self, n):
        return n % 2 == 0

    def is_odd(self, n):
        return n % 2 != 0

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            current = self.current
            self.current += 1
            if self.even == "evens":
                if self.is_even(current):
                    return current
                else:
                    return self.__next__()
            elif self.even == "odds":
                if self.is_odd(current):
                    return current
                else:
                    return self.__next__()
            else:
                return self.__next__()


evens_list = EvensAndOdds(5, 40, "odds")
for item in evens_list:
    print(item)


class range0():
    def __init__(self, *args):
        if(len(args) == 1):
            self.stop = args[0]
            self.start = 1
            self.value = 1
        if(len(args) == 2):
            self.start = args[0]
            self.stop = args[1]
            self.value = self.start
        if(len(args) > 2):
            raise TypeError(
                "range0 expected at most 2 arguments, got {}".format(len(args)))

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.stop:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

    def __repr__(self):
        return "range0({0}, {1})".format(self.start, self.stop)


for x in range0(2, 5):
    print("31:", x)
print("\n")
for x in range0(5):
    print("34:", x)
print("\n")

for x in range0(0, 5):
    print("38:", x)
print("\n")

y = range0(6)
print("42:", y)
print("\n")

#y = range0(1, 2, 3, 4)
print("46:", list(map(lambda x: x*x, y)))

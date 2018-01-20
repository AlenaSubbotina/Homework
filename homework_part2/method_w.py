class Counter:
    def __init__(self):  # constructor
        self.count = 0

    def inc(self):       # method 1
        self.count += 1

    def reset(self):     # method 2
        self.count = 0

Counter
x = Counter()  # call the constructor
x.inc()  # вызывается функция inc и подставляется в качестве аргумента x
print(x.count)
Counter.inc(x)  # эквивалентно x.inc
print(x.count)  # 2
x.reset()
print(x.count)  # 0

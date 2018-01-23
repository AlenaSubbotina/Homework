class Buffer:
    def __init__(self):
        self.buf = []
    def add(self, *a):
        summ = 0
        self.buf.extend(a)
        while len(self.buf) >= 5:
            for i in range(5):
                summ += self.buf[i]
            self.buf = self.buf[5:]
            print(summ)
            summ = 0

    def get_current_part(self):
        while len(self.buf) >= 5:
            for i in range(5):
                self.buf = self.buf[5:]
        return self.buf

a = [int(i) for i in input().split()]


# ХОРОШЕЕ РЕШЕНИЕ

class Buffer:
    def __init__(self):
        self.part = []

    def add(self, *a):
        for i in a:
            self.part.append(i)
            if len(self.part) == 5:
                print(sum(self.part))
                self.part.clear()

    def get_current_part(self):
        return self.part
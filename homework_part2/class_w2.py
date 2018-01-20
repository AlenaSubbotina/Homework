class Counter:
    def __init__(self):  # присваиваем каждому созданному экземпляру значение 0
        self.count = 0

    # pass   пустое тело

Counter
x = Counter()
print(x.count)  # 0
x.count += 1  # объект = 0
print(x)  # объект стал 1

# ф-я init может принимать и другие аргументы

class Counter:
    def __init__(self, start = 0):
        self.count = 0

Counter
x1 = Counter(10)
x = Counter()
print(x.count)  # 0
x.count += 1
class MoneyBox:
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity

    def can_add(self, v):
        if self.count + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if MoneyBox.can_add(self, v) == True:
            self.count += v

# лучшее решение
class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        return self.capacity >= v

    def add(self, v):
        self.capacity -= v
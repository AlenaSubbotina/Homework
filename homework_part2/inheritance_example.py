class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0

class MyList(list, EvenLengthMixin):
    def pop(self):
        x = super(MyList, self).pop()  # super - чтобы вызвать pop не из родителей класса MyList (list)
        print("Last value is", x)
        return x

ml = MyList([1, 2, 4, 17])  # ml.pop() - проассоциируется из класса MyList
z = ml.pop()
print(z)
print(ml)
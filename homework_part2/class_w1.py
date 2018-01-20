# СИНТАКСИС
class MyClass:  # создается отдельный неймспейс
    a = 10  # тело класса

    def func(self):
        print('Hello')


MyClass.a  # так можно достучаться до класса, a, func() - атрибуты класса
MyClass.func

x = MyClass  # вызвали конструктор класса MyClass и создали объект x
print(type(x))
print(type(MyClass))
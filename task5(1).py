import math
n = str(input())

if n == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b +c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))

elif n == 'прямоугольник':
    a = int(input())
    b = int(input())
    s = a * b

elif n == 'круг':
    r = int(input())
    s = 3.14 * r ** 2
print(float(s))
a = int(input())
b = int(input())
s = 0
n = 0

while a % 3 != 0:
    a += 1

for j in range(a, b + 1, 3):
    s += j
    n += 1

print(s / n)

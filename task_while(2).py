a = int(input())
b = int(input())

if a > b:
    s = a
else:
    s = b
while s % a != 0 or s % b != 0:
    s += 1
print(s)

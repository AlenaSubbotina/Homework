a = int(input())
b = int(input())
c = int(input())
maxi = int
mini = int
mid = int

if a <= b and a <= c:
    mini = a
elif b <= a and b <= c:
    mini = b
elif c <= a and c <= b:
    mini = c

if a >= b and a >= c:
    maxi = a
elif b >= a and b >= c:
    maxi = b
elif c >= a and c >= b:
    maxi = c

if b <= a <= c or c <= a <= b:
    mid = a
elif a <= b <= c or c <= b <= a:
        mid = b
elif b <= c <= a or a <= c <= b:
    mid = c

print(maxi)
print(mini)
print(mid)
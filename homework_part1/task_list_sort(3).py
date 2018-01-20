a = [int(i) for i in input().split()]
a.sort()
s = []

for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        if a[i] not in s:
            s.append(a[i])
            print(a[i], end=' ')
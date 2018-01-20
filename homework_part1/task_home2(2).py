n = int(input())

s = [int(i) for i in range(n + 1)]
m = []

for i in s:
    for j in range(s[i]):
        m.append(s[i])
        if len(m) <= n:
            print(s[i], end=' ')

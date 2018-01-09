s = input().lower().split()
d ={}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
m = d.items()
for j, k in m:
    print(j, k)
    
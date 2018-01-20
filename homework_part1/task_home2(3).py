lst = [int(i) for i in input().split()]
x = int(input())
m = 0

for i in range(0, len(lst)):
    if x == lst[i]:
        m += 1
        print(i, end=' ')
if m == 0:
    print('Отсутствует')
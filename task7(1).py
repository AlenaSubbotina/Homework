n = int(input())

if 11 <= n % 100 <= 14:
    print(n, 'программистов')
elif n % 10 == 1:
    print(n, 'программист')
elif 2 <= n % 10 <= 4:
    print(n, 'программиста')
else:
    print(n, 'программистов')
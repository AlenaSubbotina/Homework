n, k = map(int, input().split())

def fset(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return fset(n - 1, k) + fset(n - 1, k - 1)

print(fset(n, k))

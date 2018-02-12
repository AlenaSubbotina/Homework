import itertools

def primes():
    x = 2
    while True:
        for i in range(2, x):
                if x % i == 0:
                    break
        else:
            yield x
        x += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))


ok_status = True
vowels = ["a", "u", "i", "e", "o"]

def check(word):
    global ok_status
    for vowel in vowels:
        if vowel in word:
            return True

    ok_status = False
    return False

print(check("abacaba")) # True
print(ok_status) # True
print(check("www")) # значение ok_status поменялось False
print(ok_status) # False

Это не совсем верно, если обернуть все в функцию:

def f():
    ok_status = True
    vowels = ["a", "u", "i", "e", "o"]

    def check(word):
        global ok_status
        for vowel in vowels:
            if vowel in word:
                return True

        ok_status = False
        return False

    print(check("abacaba"))
    print(ok_status)
    print(check("www")) # значение ok_status поменялось
    print(ok_status) # True -- ok_status is not global

f()
print(ok_status) # False -- global ok_status

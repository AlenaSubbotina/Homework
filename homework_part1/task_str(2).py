s = input()
i = 0
k = 1
dnk = ''

for i in range(len(s)):
    if i < (len(s) - 1):
        if s[i] == s[i+1]:
            k += 1
            i += 1
        else:
            dnk += s[i] + str(k)
            i += 1
            k = 1
    else:
        dnk += s[i] + str(k)
        print(dnk)
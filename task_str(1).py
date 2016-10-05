s = str(input())

a = s.upper().count('C')
b = s.upper().count('G')

print(((a + b) / len(s)) * 100)
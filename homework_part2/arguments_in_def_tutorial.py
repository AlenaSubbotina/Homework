def printab(a, b):
    print(a)
    print(b)

# CORRECT WAYS TO CALL A FUNCTION
printab(10, 20)
printab(a=10, b=20)

# reyword arguments always after non-keyword arguments
printab(10, b=20)

lst = [10, 20]
printab(*lst) # = printab(lst[0], lst[1])

args = {'a':10, 'b': 20}
printab(**args) # = printab(key1 = args[key1], key2 = args[key2])

def printab(a = 10, b = 10): # аргументы по умолчанию (должны быть полсе обычных)
    print(a)
    print(b)

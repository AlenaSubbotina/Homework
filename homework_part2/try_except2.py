
def f(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as e:
        print(type(e))
        print(e)
        print(e.args)

print(f(5, 0))
print(f(5, []))

# не указывая тип ошибки

def f(x, y):
    try:
        return x / y
    except:
        print("Error :(")

print(f(5, 0))
print(f(5, []))

#

try:
    15 / 0
    # e
except ArithmeticError:  # isinstance(e, ArithmeticError) == True
    print("arithmetic error")

#

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero")
    else:
        print("result is", result)
    finally:
        print("finally")

divide(2, 1)
divide(2, 0)
divide(2, [])


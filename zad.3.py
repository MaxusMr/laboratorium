

def even(a):
    b = bool(a % 2 == 0)
    if b is True:
        return "Even number"
    else:
        return "Odd number"


e = int(input("Give number "))
print(even(e))

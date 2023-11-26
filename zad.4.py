

def check(a, b, c):
    return bool(a+b == c or a+b >= c)


f = int(input("Give number "))
g = int(input("Give second number "))
h = int(input("Give third number "))
print(check(f, g, h))

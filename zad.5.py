
def inside(a, b):
    return bool(b in a)


lista = [3, 6, 9, 15, 26, 27, 97, 4, 83, 20, 74, 37, 17, 268, 36, 375]
i = int(input("Give number "))
print(inside(lista, i))

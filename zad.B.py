

def multiplication(lista):
    lista3 = []
    for element in lista:
        lista3.append(element * 2)
    return lista3


def multiplication2(lista):
    return [element * 2 for element in lista]


lista1 = [1, 2, 3, 4, 5]
score1 = multiplication(lista1)
print(score1)


lista2 = [1, 2, 3, 4, 5]
score2 = multiplication2(lista2)
print(score2)

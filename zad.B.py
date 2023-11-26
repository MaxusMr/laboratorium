

def przez2(lista):
    nowa_lista = []
    for element in lista:
        nowa_lista.append(element * 2)
    return nowa_lista


def przez2_skladana(lista):
    return [element * 2 for element in lista]


lista1 = [1, 2, 3, 4, 5]
wynik1 = przez2(lista1)
print(wynik1)


lista2 = [1, 2, 3, 4, 5]
wynik2 = przez2_skladana(lista2)
print(wynik2)

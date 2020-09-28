def BuscaBin(list, item):
    prim = 0
    ult = len(list) - 1
    found = False

    while prim <= ult and not found:
        meio = (prim + ult) // 2
        if list[meio] == item:
            found = True
        else:
            if item < list[meio]:
                ult = meio - 1
            else:
                prim = meio + 1


lista = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(BuscaBin(lista, 3))
print(BuscaBin(lista, 13))

def quickSort(lis):
    # caso base
    if(len(lis) <= 1):
        return lis
    # caso recursivo
    piv = lis.pop()

    lis1 = []
    lis2 = []

    for i in lis:
        if i <= piv:
            lis1.append(i)
        else:
            lis2.append(i)

    lis1 = quickSort(lis1)
    lis2 = quickSort(lis2)

    return lis1 + [piv] + lis2


lista = [75, 2, 45, 36, 85, 92, 14, 21, 25, 7]

print(lista)
print(quickSort(lista))

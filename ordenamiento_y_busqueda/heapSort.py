def heapIfy(lis2, pos):
    # si el nodo tiene dos hijos
    if 2 * pos + 2 <= len(lis2)-1:
        if lis2[2 * pos + 1] <= lis2[2 * pos + 2]:
            min = 2 * pos + 1
        else:
            min = 2 * pos + 2

        if lis2[pos] > lis2[min]:
            aux = lis2[pos]
            lis2[pos] = lis2[min]
            lis2[min] = aux

        heapIfy(lis2, min)
    # si el nodo solo tiene un hijo
    elif 2 * pos + 1 <= len(lis2) - 1:
        if lis2[pos] > lis2[2 * pos + 1]:
            aux = lis2[pos]
            lis2[pos] = lis2[2 * pos + 1]
            lis2[2 * pos + 1] = aux
    return lis2


def heapSort(lis):
    lisN = []

    for i in range(len(lis)//2 - 1, -1, -1):
        lis = heapIfy(lis, i)

    for i in range(0, len(lis)):
        aux = lis[0]
        lis[0] = lis[len(lis) - 1]
        lis[len(lis) - 1] = aux
        lisN.append(aux)

        lis = lis[:len(lis) - 1]

        lis = heapIfy(lis, 0)

    return lisN


lista = [28, 47, 31, 26, 12, 5, 10, 58]
print(lista)
print(heapSort(lista))

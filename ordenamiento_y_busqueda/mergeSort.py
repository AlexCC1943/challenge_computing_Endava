def merge(lista1, lista2):
    lista3 = []
    while (len(lista1) > 0 and len(lista2) > 0):
        if lista1[0] < lista2[0]:
            lista3.append(lista1[0])
            lista1 = lista1[1:]
        else:
            lista3.append(lista2[0])
            lista2 = lista2[1:]

    if len(lista1) > 0:
        lista3 = lista3 + lista1
    elif len(lista2) > 0:
        lista3 = lista3 + lista2

    return lista3


def mergeSort(lis):
    # caso base
    if(len(lis) == 1):
        return lis
    # caso recursivo
    lisIz = lis[:len(lis)//2]
    lisDe = lis[len(lis)//2:]

    lisIz = mergeSort(lisIz)
    lisDe = mergeSort(lisDe)

    return merge(lisIz, lisDe)


lista = [4, 8, 1, 0, 25, 14, 10, 16, 78, 45, 61]

print(lista)
print(mergeSort(lista))

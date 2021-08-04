import random


def radixSort(lista):
    # se busca el mayor numero de digitos entre los elementos de la lista
    n = 0
    for ele in lista:
        if len(ele) > n:
            n = len(ele)
    # se añade 0 a los numeros que les falte digitos
    for i in range(0, len(lista)):
        while(len(lista[i]) < n):
            lista[i] = "0" + lista[i]
    # range(valor incial, valor final, formato de conteo(aumenta o decrementa))
    for j in range(n - 1, -1, -1):
        grupos = [[] for i in range(10)]
        for i in range(len(lista)):
            grupos[int(lista[i][j])].append(
                lista[i])  # lista[elemento][digito]

        lista = []
        for g in grupos:
            lista += g

    return [int(i) for i in lista]


lista = [str(random.randint(0, 200)) for i in range(10)]
print(lista)
print(radixSort(lista))

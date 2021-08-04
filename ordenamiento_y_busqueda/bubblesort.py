def bubbleSort(lista):
    n = len(lista)
    for i in range(1, n):
        for j in range(0, n-1):
            if(lista[j] > lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista


lista = [20, 19, 5, 6, 15, -4, 0, 18, 7, 3]

print(lista)
print(bubbleSort(lista))

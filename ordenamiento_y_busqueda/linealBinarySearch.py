# Este metodo requiere tener todos los elementos ordenados
def linealBinarySearch(lista, ele):
    if len(lista) == 0:
        m = "No hay elementos"
    elif ele == lista[len(lista)//2]:
        m = "Se encontro el elemento", ele

    elif ele < lista[len(lista)//2]:
        nlist = lista[:len(lista)//2]
        ind = False
        for i in nlist:
            if ele == i:
                ind = True
        if ind == True:
            m = "Se encontro el elemento", ele
        else:
            m = "No se encontro el elemento", ele
    else:
        nlist = lista[len(lista)//2+1:]
        ind = False
        for i in nlist:
            if ele == i:
                ind = True
        if ind == True:
            m = "Se encontro el elemento", ele
        else:
            m = "No se encontro el elemento", ele

    return m


n = 1
lisN = [1, 2, 3, 4, 8, 12, 25, 34, 47, 89, 92, 135, 147, 150]
# lisN=[]
print(linealBinarySearch(lisN, n))

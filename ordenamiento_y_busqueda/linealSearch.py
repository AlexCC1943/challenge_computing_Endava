def linealSearch(lista, ele):
    for i in lista:
        if (i == ele):
            return True
    return False


Lisn = [12, 45, 78, 32, 10, 5, 98, 7, 74, 19]
n = 4
print("¿El elemento", n, "esta en la lista?")
print("La respuesta es: ", linealSearch(Lisn, n))

def convertChain(chain):
    varSa = ""

    for i in chain:
        varSa += str(ord(i))

    return int(varSa)


def hashFun(chain, tam):
    i = convertChain(chain)

    return int(tam*(i*0.000000000000000021 % 1))


def appenD(chain, tabla, tam):
    resi = hashFun(chain, tam)
    tabla[resi].append(chain)


def hashSearch(chain, tabla, tam):
    hash = hashFun(chain, tam)

    for i in tabla[hash]:
        if i == chain:
            return True
    return False


n = 15

hTab = [[] for i in range(n)]

lisCha = ["Hola", "poster", "lampara", "televisor",
          "consola", "celular", "computador", "gorro", "silla"]

for j in lisCha:
    appenD(j, hTab, n)

print(hTab)

print(hashSearch("consola", hTab, n))
print(hashSearch("lampara", hTab, n))
print(hashSearch("amor", hTab, n))

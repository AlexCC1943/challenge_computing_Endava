# Crear clase para definir un vertice (nodo)


class Nodo:
    # constructor
    def __init__(self, i):
        # se crea el atributo id para poder diferenciar a cada vertice o nodo
        self.id = i  # "n" + str(i)
        # se crea el atributo visitado para saber si ya estubo ahi o no
        self.visitado = False
        # se crea nivel para indicar su nivel de profundidad en BFS
        self.nivel = -1
        # se crea padre para indicar que nodo es padre en DFS
        self.padre = None
        # se crea el atributo vecinos para saber sus vecinos, todos los nodos a los que este conectado
        self.vecinos = []

    def appNeighboor(self, idNei):
        if not idNei in self.vecinos:
            self.vecinos.append(idNei)

# clase que define a una grafica


class Graphic:

    def __init__(self):
        self.nodos = {}

    def appNodo(self, nod):
        if not nod in self.nodos:
            self.nodos[nod] = Nodo(nod)

    def appConect(self, n1, n2):
        # no direccionado
        if n1 in self.nodos and n2 in self.nodos:
            self.nodos[n1].appNeighboor(n2)
            self.nodos[n2].appNeighboor(n1)

    # funcion que realiza bfs
    def bfs(self, nodoIni):
        if nodoIni in self.nodos:
            queue = [nodoIni]

            self.nodos[nodoIni].visitado = True
            self.nodos[nodoIni].nivel = 0

            print("(" + str(nodoIni) + "," +
                  str(self.nodos[nodoIni].nivel) + ")")

            while len(queue) > 0:
                actu = queue[0]
                queue = queue[1:]

                for n in self.nodos[actu].vecinos:
                    if self.nodos[n].visitado == False:
                        queue.append(n)
                        self.nodos[n].visitado = True
                        self.nodos[n].nivel = self.nodos[actu].nivel + 1

                        print("(" + str(n) + ", " +
                              str(self.nodos[n].nivel) + ")")
    # funcion que realiza dfs

    def dfs(self, nodoIni):
        if nodoIni in self.nodos:
            self.nodos[nodoIni].visitado = True

            for n in self.nodos[nodoIni].vecinos:
                if self.nodos[n].visitado == False:
                    self.nodos[n].padre = nodoIni
                    print("(" + str(n) + ", " + str(nodoIni) + ")")
                    self.dfs(n)


def main():

    g = Graphic()

    LisNod = [0, 1, 2, 3, 4, 5, 6]
    for n in LisNod:
        g.appNodo(n)

    lisCon = [2, 0, 0, 6, 6, 3, 0, 5, 6, 5, 0, 1, 6, 4, 1, 4]
    for i in range(0, len(lisCon) - 1, 2):
        g.appConect(lisCon[i], lisCon[i+1])

    for j in g.nodos:
        print(j, g.nodos[j].vecinos)

    print("\n\n")
    print("BFS")
    g.bfs(2)

    g2 = Graphic()

    lisNod2 = [1, 2, 3, 4, 5, 6]
    for i in lisNod2:
        g2.appNodo(i)

    lisCon2 = [1, 2, 1, 5, 2, 3, 2, 5, 3, 4, 4, 5, 4, 6]
    for j in range(0, len(lisCon2) - 1, 2):
        g2.appConect(lisCon2[j], lisCon2[j+1])

    print("DFS")
    print("(1,null)")
    g2.dfs(1)


main()

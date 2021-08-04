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
        # se crea el atributo al que le corresponde el costo
        self.distancia = float('inf')

    def appNeighboor(self, idNei, pe):
        if not idNei in self.vecinos:
            self.vecinos.append([idNei, pe])


class Graphic:
    def __init__(self):
        self.nodos = {}

    def appNodo(self, id):
        if id not in self.nodos:
            self.nodos[id] = Nodo(id)

    def appConnect(self, n1, n2, pe):
        if n1 in self.nodos and n2 in self.nodos:
            self.nodos[n1].appNeighboor(n2, pe)
            self.nodos[n2].appNeighboor(n1, pe)

    def minimo(self, lista):
        if len(lista) > 0:
            dis = self.nodos[lista[0]].distancia
            nodo = lista[0]

            for n in lista:
                if dis > self.nodos[n].distancia:
                    dis = self.nodos[n].distancia
                    nodo = n

            return nodo

    def printGraphic(self):  # imprime los costos registrados en la ruta seleccionada

        for n in self.nodos:
            print("Llegar al nodo " + str(n) + " desde el nodo " + str(self.nodos[n].padre) +
                  " tiene un costo de: " + str(self.nodos[n].distancia))

    def way(self, des):  # funcion en la que se indica el recorrido deseado en la grafica, con origen y destino
        way = []
        actual = des

        while actual != None:  # actua hasta encontrar el nodo orgine que tiene
            way.insert(0, actual)
            actual = self.nodos[actual].padre

        return [way, self.nodos[des].distancia]

    def dijkstra(self, nodoIni):
        if nodoIni in self.nodos:
            self.nodos[nodoIni].distancia = 0
            act = nodoIni
            noVisi = []
            for n in self.nodos:
                if n != act:  # mientras no se encuentre el nodo inicial se va a determinar la distancia como inf
                    self.nodos[n].distancia = float('inf')
                self.nodos[n].padre = None
                noVisi.append(n)

            while len(noVisi) > 0:
                # se va arecorrer a cada vecino de actual
                for nei in self.nodos[act].vecinos:
                    # aqui se valida si el vecino esta vsistado o no
                    if self.nodos[nei[0]].visitado == False:
                        if self.nodos[act].distancia + nei[1] < self.nodos[nei[0]].distancia:
                            self.nodos[nei[0]
                                       ].distancia = self.nodos[act].distancia + nei[1]
                            self.nodos[nei[0]].padre = act

                self.nodos[act].visitado = True

                noVisi.remove(act)

                act = self.minimo(noVisi)
        else:
            return False


class main:

    g = Graphic()
    LisNod = [1, 2, 3, 4, 5, 6]
    for n in LisNod:
        g.appNodo(n)

    lisCon = [1, 6, 14, 1, 2, 7, 1, 3, 9, 2, 3, 10,
              2, 4, 15, 3, 4, 11, 3, 6, 2, 4, 5, 6, 5, 6, 9]
    for i in range(0, len(lisCon) - 1, 3):
        print(lisCon[i], lisCon[i+1], lisCon[i+2])
        g.appConnect(lisCon[i], lisCon[i+1], lisCon[i+2])

    print("la ruta más rápida por dijkstra junto con su costo es:")
    g.dijkstra(1)
    print(g.way(6))
    print("los valores finales de la grafoca son los siguientes: ")
    g.printGraphic()

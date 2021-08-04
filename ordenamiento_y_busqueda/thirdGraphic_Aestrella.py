# Crear clase para definir un vertice (nodo)
import math


class Nodo:
    # constructor
    def __init__(self, i, h=0):
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
        self.costo = float('inf')
        # se crea el costo f o costo tentativo
        self.costoF = float('inf')
        # se crea el atributo de aprendizaje heuristica
        self.heuristica = h

    def appNeighboor(self, idNei, pe):
        if not idNei in self.vecinos:
            self.vecinos.append([idNei, pe])

# clase que define a una grafica


class Graphic:

    def __init__(self):
        self.nodos = {}

    def appNodo(self, nod, h=0):
        if not nod in self.nodos:
            # Genera un elemento en el diccionario, donde la id es el id del nodo y el valor es el nodo
            self.nodos[nod] = Nodo(nod, h)

    def appConnect(self, n1, n2, pe):
        # no direccionado
        # se añade una conexion entre los nodos en la lista vecinos de cada nodo con su peso
        if n1 in self.nodos and n2 in self.nodos:
            self.nodos[n1].appNeighboor(n2, pe)
            self.nodos[n2].appNeighboor(n1, pe)

    def printGraphic(self):  # imprime los costos registrados en la ruta seleccionada

        for n in self.nodos:
            print("Llegar al nodo " + str(n) + " desde el nodo " + str(self.nodos[n].padre) +
                  " tiene un costo de: " + str(self.nodos[n].costo))

    def way(self, des):  # funcion en la que se indica el recorrido deseado en la grafica, con origen y destino
        way = []
        actual = des

        while actual != None:  # actua hasta encontrar el nodo orgine que tiene
            way.insert(0, actual)
            actual = self.nodos[actual].padre

        return [way, self.nodos[des].costo]

    def minimoH(self, lista):
        if len(lista) > 0:
            cosF = self.nodos[lista[0]].costoF
            n = lista[0]

            for ele in lista:
                if cosF > self.nodos[ele].costoF:
                    cosF = self.nodos[ele].costoF
                    n = ele
            return n

    def aEstrella(self, nIni, nFin):
        if nIni in self.nodos and nFin in self.nodos:
            self.nodos[nIni].costo = 0
            self.nodos[nIni].costoF = self.nodos[nIni].costo + \
                self.nodos[nIni].heuristica

        for n in self.nodos:  # se recorren todos los nodos distintos al incial y se les asigna inf como costos
            if n != nIni:
                self.nodos[n].costo = float('inf')
                self.nodos[n].costoF = float('inf')

            # se asgina a TODOS los nodos un pade none
            self.nodos[n].padre = None

        conAbierto = [nIni]  # lista de nodos descubiertos pero no evaluados

        while len(conAbierto) > 0:
            act = self.minimoH(conAbierto)

            if act == nFin:
                return [self.way(nFin), self.nodos[nFin].costo]

            conAbierto.remove(act)
            self.nodos[act].visitado = True

            for no in self.nodos[act].vecinos:
                if self.nodos[no[0]].visitado == False:
                    if self.nodos[no[0]].id not in conAbierto:
                        conAbierto.append(no[0])

                    if self.nodos[act].costo + no[1] < self.nodos[no[0]].costo:
                        self.nodos[no[0]].padre = act
                        self.nodos[no[0]].costo = self.nodos[act].costo + no[1]
                        self.nodos[no[0]].costoF = self.nodos[no[0]
                                                              ].costo + self.nodos[no[0]].heuristica


def main():

    g = Graphic()
    LisNod = [0, 55, 1, 40, 2, 20, 3, 40, 4, 45, 5, 20, 6, 0]
    for n in range(0, len(LisNod) - 1, 2):
        g.appNodo(LisNod[n], LisNod[n+1])

    lisCon = [0, 1, 15, 0, 4, 20, 1, 2, 20, 2,
              3, 30, 3, 6, 40, 4, 5, 30, 5, 6, 20]
    for i in range(0, len(lisCon) - 1, 3):
        print(lisCon[i], lisCon[i+1], lisCon[i+2])
        g.appConnect(lisCon[i], lisCon[i+1], lisCon[i+2])

    g.aEstrella(1, 6)
    print(g.way(6))
    g.printGraphic()


main()

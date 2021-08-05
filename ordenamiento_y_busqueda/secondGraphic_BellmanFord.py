# Crear clase para definir un vertice (nodo)
import math


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
        self.costo = float('inf')

    def appNeighboor(self, idNei, pe):
        if not idNei in self.vecinos:
            self.vecinos.append([idNei, pe])

# clase que define a una grafica


class Graphic:

    def __init__(self):
        self.nodos = {}

    def appNodo(self, nod):
        if not nod in self.nodos:
            # Genera un elemento en el diccionario, donde la id es el id del nodo y el valor es el nodo
            self.nodos[nod] = Nodo(nod)

    def appConect(self, n1, n2, pe):
        # no direccionado
        # se añade una conexion entre los nodos en la lista vecinos de cada nodo con su peso
        if n1 in self.nodos and n2 in self.nodos:
            self.nodos[n1].appNeighboor(n2, pe)
            self.nodos[n2].appNeighboor(n1, pe)

    def printGraphic(self):  # imprime los costos registrados en la ruta seleccionada

        for n in self.nodos:
            print("Llegar al nodo " + str(n) + " desde el nodo " + str(self.nodos[n].padre) +
                  " tiene un costo de: " + str(self.nodos[n].costo))

    def way(self, ini, des):  # funcion en la que se indica el recorrido deseado en la grafica, con origen y destino
        way = []
        actual = des

        while actual != None:  # actua hasta encontrar el nodo orgine que tiene
            way.insert(0, actual)
            actual = self.nodos[actual].padre

        return [way, self.nodos[des].costo]

    def bellmanFord(self, a):
        if a in self.nodos:
            self.nodos[a].costo = 0

        for n in self.nodos:
            if n != a:
                self.nodos[n].costo = float('inf')
            self.nodos[n].padre = None
        for x in range(len(self.nodos)-1):
            for act in self.nodos:
                for pe in self.nodos[act].vecinos:
                    #print("peso", pe[0])
                    # pe[1] es el indice de la lista interna de vecinos, es decir, la que compone a cada vecino, en este caso pe[1] es el peso
                    if self.nodos[act].costo + pe[1] < self.nodos[pe[0]].costo:
                        self.nodos[pe[0]].costo = self.nodos[act].costo + pe[1]
                        self.nodos[pe[0]].padre = act

        for actu in self.nodos:
            for pe in self.nodos[actu].vecinos:
                if self.nodos[actu].costo + pe[1] < self.nodos[pe[0]].costo:
                    return "Error: se encontro un ciclo con peso negativo"


def main():

    g = Graphic()
    #LisNod = [1, 2, 3, 4, 5, 6]
    LisNod = ["n1","n2","n4","n5","n6","n7","n8","n9"]
    for n in LisNod:
        g.appNodo(n)

    lisCon = ["n1","n2",2, "n1","n7",7 ,"n2","n5",1 ,"n2","n6",1 ,"n2","n9",2 ,"n4","n6",7 ,"n5","n7",3 ,"n5","n8",1 ,"n6","n8",5 ,"n7","n8",1 ,"n9","n4",6 ,"n2","n1",2]
    #lisCon = [1, 6, 14, 1, 2, 7, 1, 3, 9, 2, 3, 10,
     #         2, 4, 15, 3, 4, 11, 3, 6, 2, 4, 5, 6, 5, 6, 9]
    for i in range(0, len(lisCon) - 1, 3):
        #print(lisCon[i], lisCon[i+1], lisCon[i+2])
        g.appConect(lisCon[i], lisCon[i+1], lisCon[i+2])

    lisNodAux = LisNod.copy()
    print(lisNodAux)
    for j in lisNodAux:
        print(j)
        g.bellmanFord(j)
        print(j)
        for m in lisNodAux:
            print(j)
            print(m)
            print(g.way(j,m))
        print(j)
           
    #g.bellmanFord(1)
    #print(g.way(6))
    #g.bellmanFord(2)
    #print(g.way(6))
    g.printGraphic()


main()

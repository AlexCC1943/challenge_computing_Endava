import math

class Nodo:

    def __init__(self,i):
        self.id = i
        self.neighbors = []
        self.distance = float('inf')
        self.visited = False
        self.father = None
    
    def addNeighbor(self, idNei, pe):
        if not idNei in self.neighbors:
            self.neighbors.append([idNei,pe])

class Graphic:

    def __init__(self):
        self.nodos = {}

    def addNodo(self,nod):
        if not nod in self.nodos:
            self.nodos[nod] = Nodo(nod)

    def addArista(self,n1,n2,p):
        if n1 in self.nodos and n2 in self.nodos:
            self.nodos[n1].addNeighbor(n2, p)
            self.nodos[n2].addNeighbor(n1, p) 

    def printGraphic(self):
        for g in self.nodos:
            print("Del nodo " + str(self.nodos[g].father) + "al nodo " + str(g) + "hay una distancia de " + str(self.nodos[g].distance))   
    
    def way(self, des):
        way = []
        act = des

        while act != None:
            way.insert(0,act)
            act = self.nodos[act].father
        
        return ["La mejor ruta en este orden es: ", way, "con una distancia recorrida de" , self.nodos[des].distance]

    
    #TODO ver si se require un nuevo atributo para encontrar la mejor ruta ultimo visitado o ultimo padre
    #TODO metodo que genere 10 graficas y a partir de ellas generar los dos puntos sigiuentes
def main():
    print()


main()
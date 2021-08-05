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

    def minimo(self, lista): #funcion para allar el nodo con menor distancia tentativa
        if len(lista) > 0: # se ejecutara si hay elementos en la lista que recibe, la de no visitados
            dis = self.nodos[lista[0]].distance # se crea la variable dis como la distancia del primer elemento de la lista recibida
            nodo = lista[0] # se crea una variable nodo como el primer nodo de la lista

            for n in lista: # se reocorre la lista
                if dis > self.nodos[n].distance: # si la distancia del nodo actual es mayor que la del nodo n
                    dis = self.nodos[n].distance # se reemplaza dis por la distancia del nodo n
                    nodo = n # se cambia la varible nodo por el nodo n, esto hallara al final el nodo con menor distancia

            return nodo # se retorna el nodo

    def dijkstra(self, nodoIni, nodoFin): #funcion de dijkstra
        if nodoIni in self.nodos: #se valida si el nodo inicial esta en la grafica
            self.nodos[nodoIni].distance = 0 #se iguala a 0 su distancia ya que este es el incio
            act = nodoIni #se crea la variable act de nodo actual 
            noVisi = [] #se crea la lista noVisi de nodos no visitados (cola de prioridad)
            noRev = []
            for n in self.nodos: #se recorren los nodos
                if n != act:  # si no se encuentre el nodo inicial se va a determinar la distancia como inf
                    self.nodos[n].distance = float('inf') 
                self.nodos[n].father = None #se le asgina a todos los nodos un padre none 
                noVisi.append(n) #se añaden los nodos a la lista noVisi
                noRev.append(n)

            while len(noVisi) > 0: #mientras hayan nodos no visitados se hara este ciclo
                for nei in self.nodos[act].neighbors: # se va a recorrer a cada vecino de actual
                    if self.nodos[nei[0]].visited == False: # aqui se valida si el vecino esta vsistado o no
                        #nei es un nodo, nei[0] es su nodo vecino y nei[1] es su costo
                        if self.nodos[act].distance + nei[1] < self.nodos[nei[0]].distance: #si la suma entre la distancia del nodo actual con la distancia de su vecino son menores a la distancia del vecino se actualioza esa distnaica para el vecino  
                            self.nodos[nei[0]].distance = self.nodos[act].distance + nei[1] #se cambia la distnacia
                            self.nodos[nei[0]].father = act #se asigna como padre el nodo actual

                self.nodos[act].visited = True #se aclara que esta visitado

                noVisi.remove(act) #se remueve el nodo actual de noVisi
 
                act = self.minimo(noVisi) #se obtiene eel nodo con menor distancia para analizar
            
            way = []
            actual = nodoFin


            print(actual)
            while actual != None:  # actua hasta encontrar el nodo orgine que tiene
               way.insert(0, actual)
               actual = self.nodos[actual].father

            return [way, self.nodos[nodoFin].distance]    
        else:
            return False
    
    #TODO ver si se require un nuevo atributo para encontrar la mejor ruta ultimo visitado o ultimo padre
    #TODO metodo que genere 10 graficas y a partir de ellas generar los dos puntos sigiuentes
def main():
    file_object = open("input.txt", "r")
    contents = file_object.read()
    listN = []
    listAr = []
    listAux1 = contents.split()
    listAux2 = []
    for m in listAux1:
        if len(m) == 2:
            listN.append(m)
        else:
            listAux2.append(m)

    for i in listAux2:
        aux = i.split(",")
        nA = aux[:1]
        nB = aux[1:2]
        pe = aux[2:]
        listAr.append(nA[0])
        listAr.append(nB[0])
        listAr.append(int(pe[0]))
        
    print(listN)
    print(listAr)    

    g = Graphic()
    for n in listN:
        g.addNodo(n)
    for i in range(0, len(listAr) - 1, 3):
        g.addArista(listAr[i], listAr[i+1], listAr[i+2])
    print(g.dijkstra("n1","n4"))

    a = [[] for i in range(len(listN))]


    print(a)

main()
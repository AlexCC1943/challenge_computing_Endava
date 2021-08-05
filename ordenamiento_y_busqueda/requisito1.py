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
        self.nodes = {}

    def addNode(self,nod):
        if not nod in self.nodes:
            self.nodes[nod] = Nodo(nod)

    def addArista(self,n1,n2,p):
        if n1 in self.nodes and n2 in self.nodes:
            self.nodes[n1].addNeighbor(n2, p)
            self.nodes[n2].addNeighbor(n1, p) 
    def wayAll(self):
        print()

    def searchAllRoute(self,nodIni):
        if nodIni in self.nodes and len(self.nodes[nodIni].neighbors) > 0: # se valida que el nodo este en la grafica y que este conectado
            print("si?",nodIni)
            self.nodes[nodIni].distance = 0
            act = nodIni
        for n in self.nodes:
            if n != nodIni:
                self.nodes[n].distance = float('inf')
        noVisi = [] #se crea la lista noVisi de nodos no visitados (cola de prioridad)
        noRev = []
        for n in self.nodes: #se recorren los nodos
            if n != act:  # si no se encuentre el nodo inicial se va a determinar la distancia como inf
                self.nodes[n].distance = float('inf') 
            self.nodes[n].father = None #se le asgina a todos los nodos un padre none 
            noVisi.append(n) #se añaden los nodos a la lista noVisi
            noRev.append(n)
        for x in range(len(self.nodes)-1):
            for actu in self.nodes:
                nDis = float('inf')
                for pe in self.nodes[actu].neighbors:
                    if pe[1] < nDis:
                        nDis = pe[1]
                        pe = actu
                        print("nueva dis",nDis)
                        print("nuevo act", pe)


    
    def way(self, des):  # funcion en la que se indica el recorrido deseado en la grafica, con origen y destino
        way = []
        actual = des

        while actual != None:  # actua hasta encontrar el nodo orgine que tiene
            way.insert(0, actual)
            actual = self.nodes[actual].father

        return [way, self.nodes[des].distance]

  
    def bellmanFord(self, a):
        if a in self.nodes:
            self.nodes[a].distance = 0

        for n in self.nodes:
            if n != a:
                self.nodes[n].distance = float('inf')
            self.nodes[n].father = None
        for x in range(len(self.nodes)-1):
            for act in self.nodes:
                for pe in self.nodes[act].neighbors:
                    # pe[1] es el indice de la lista interna de vecinos, es decir, la que compone a cada vecino, en este caso pe[1] es el peso
                    if self.nodes[act].distance + pe[1] < self.nodes[pe[0]].distance:
                        self.nodes[pe[0]].distance = self.nodes[act].distance + pe[1]
                        self.nodes[pe[0]].father = act

        for actu in self.nodes:
            for pe in self.nodes[actu].neighbors:
                if self.nodes[actu].distance + pe[1] < self.nodes[pe[0]].distance:
                    return "Error: se encontro un ciclo con peso negativo"

def main():
    lisNod = ["n1","n2","n3","n4","n5","n6","n7","n8","n9"]
    lisCon = ["n1","n2",2, "n1","n7",7 ,"n2","n5",1 ,"n2","n6",1 ,"n2","n9",2 ,"n4","n6",7 ,"n5","n7",3 ,"n5","n8",1 ,"n6","n8",5 ,"n7","n8",1 ,"n9","n4",6]
    lisNodAux = lisNod.copy()
    print(lisNodAux)
    g = Graphic()
    for n in lisNod:
        g.addNode(n)
    for i in range(0, len(lisCon) - 1, 3):
        g.addArista(lisCon[i], lisCon[i+1], lisCon[i+2])
   
    
    for j in lisNod:
        g.searchAllRoute(j)
    '''for j in lisNodAux:
        g.bellmanFord(j)
        for m in lisNodAux:
            print(j)
            print(m)
            print(g.way(m))'''

    '''listGra = []
    for i in range(len(lisNod)):
        g = Graphic()
        for n in lisNod:
            g.addNode(n)
        for ar in range(0, len(lisCon) - 1, 3):
            g.addArista(lisCon[ar], lisCon[ar+1], lisCon[ar+2])
        listGra.append(g)
    listGraAux=[]
    for j in listGra:
        for nod in lisNod:
            j.dijkstra(nod)
            
        for nodo in listGraAux:
            print("hola")
            print(j.way(nodo))

        
    print(listGra)'''

main()

'''file_object = open("input.txt", "r")
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

    a = [[] for i in range(len(listN))]

    
    print(a)'''
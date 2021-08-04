file_object = open("input.txt", "r")
print(file_object)
file_object2 = open("new_text2.txt","w+")#sentencia para crea un nuevo archivo open("nombre del archivo.extension", "w+") el w+ sginifica wrtie y el + add?

for i in range(10):#se escribe la linea indicada 10 veces en el archivo
    file_object2.write("this is line %d\r\n" % (i+1))

file_object2.close()#se cierra el archivo para guardar los cambios

contents = file_object.read()
print(contents)
print(len(contents))
print("contents", file_object2)

listaAr=[]
listaN=[]
'''for n in range(len(contents)):#ciclo for para insertar los nodos 
    if contents[n] != '\n':
        if contents[n] == "n":
            print("incio:",contents[n]+"+"+contents[n+1]+"+"+contents[n+2]+"+"+contents[n+3])
            nodoN=contents[n]+contents[n+1]
            if not nodoN in listaN:
                listaN.append(nodoN)'''

listaAux1 = contents.split()
listaAux2 = []
for m in listaAux1:
    if len(m) == 2:
        listaN.append(m)
    else:
        listaAux2.append(m)


for i in listaAux2:
    print(i.split(","))
    aux = i.split(",")
    nA = aux[:1]
    nB = aux[1:2]
    pe = aux[2:]
    print(nA)
    print(nB)
    print(pe)
    listaAr.append(nA[0])
    listaAr.append(nB[0])
    listaAr.append(int(pe[0]))
    print(i[6:])
    
#print(contents.split())            
print(listaN)
print(listaAr)
#print(listaAux2)

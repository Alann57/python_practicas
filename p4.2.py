def imprimir(l):
    for x in range (len(l)):
        print(f" | {l[x]}", end=" ")

def ordenar(ls, ord):#ORDENAR AL VECTOR ORIGINAL NO UNA COPIA
    if(ord == "DSC"):
        for y in range(len (ls)-1):
            if(ls[y]< ls[y+1]):
                aux = ls[y]
                ls[y]= ls [y+1]
                ls[y+1]=aux
lista= [45,23,25,14,15,19,8,2,1,4,300] #LISTA SE COMPORTA... PUNTERO
print("Vector original")
imprimir (lista)
orden ="DSC"
ordenar(lista, orden)
print (end="\n")
print (f"Vector ordenado {orden}")
imprimir(lista)                
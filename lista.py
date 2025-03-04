#lista
calificaciones=[1,2,3,4,5]
nombres=["Moises","Camila ","Fernanda ","Pablo","Tatiana"]
lista_variada= [True, 10.5 ,"abc",[0,1,1]]
print("Estudiantes",nombres[-3])
print("calificaciones", calificaciones[-2])
print("lista dentro de otra",lista_variada[[3][0]])
print("imprimir un rango o slices",nombres[0:3])
"agregar elementos a una lista"
nombres.append("Anibal")
print(nombres)
#remover elementos de una lista 
nombres.remove("Pablo")
print(nombres)
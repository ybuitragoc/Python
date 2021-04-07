#metodos de las listas
lista = [1, "dos",3]

buscar = 0

#validar si existe elemento en listabusca
if buscar in lista:
    lista.index(buscar)
else:
    print("No existe el elemento")

#agregar elementos a la lista
lista.append("agregar a lista")
print(lista)

#Cantidad de veces que esta un elemento en una lista
print(lista.count(3))

#agregar elemento a la lista a una posicion concreta
lista.insert(2,"nuevo elemento")
print(lista)

#transformar la lista y agregar cadena
iterable= "cadena ejemplo"
lista.extend(iterable)
print(lista)

#Borrar elemento de la lista
lista.pop(0) # si no pongo indice me borra el ultimo
print(lista)

lista.remove("a") #valor del elemento que quiero eliminar y solo borra la primer ocurrencia
print(lista)

#eliminar un valor exacto en una cadena
for i in lista:
    if i == "e":
        lista.remove(i)
print(lista)

#invertir elementos de la lista

lista.reverse()
print(lista)
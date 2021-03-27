#Listas / Arreglos / vectores / Lists / Arrays / vectors
lista =  [2, "text", True,["uno",10]]
print (lista)

#imprimir posicion 1 de la  / print position 1 of the list
print(lista[0])

#imprimir la lista de la lista / print the list from the list
print(lista[3])

#imprimir una elemento de la lista de la lista / print a list item from the list
print(lista[3][1])

#imprimir rango de posiciones / print position range
print(lista[0:3])

#imprimir sin tener en cuenta las posiciones pares / print regardless of even positions
print(lista[0::2])

#imprimir entre un rango, las posiciones pares / print between a range, even positions
print(lista[0:3:2])

#Asignar valores a posiciones de la lista y volver a imprimir la lista / Assign values ​​to list positions and reprint the list
lista_2 = lista[0:2] = [4,3]
print(lista_2 + lista [2:])

#imprimir ultimo elemento de una lista  / print last element of a list
print(lista[-1])


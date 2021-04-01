#Cantidad caracteres de una cadena
s = "Palabra seguida y seguidas"
print(len(s))

#contar numero de veces que se repite un caracteres o una cadena
print(s.count("a"))
#contar numero de veces que se repite un caracteres o una cadena desde una posicion hasta otra posicion des 0 hasta len-1
print(s.count("a",0,3))

#cadena en minusculas
print(s.lower())

#cadena en mayusculas
print(s.upper())

#reemplazar elementos de la cadena
print(s.replace('a','x'))

#Cuantas veces quiero que se ejecuta el replace sobre la cadena
print(s.replace('a','x',1))

#dividir una cadena cada que se encuentre un caracteres (separar en columnas) / se elimina ese caracter
print (s.split(" ",2))

#buscar un caracteres dentro de un string / muestra la ubicacion de la primer letras buscada 
print (s.find('a'))

#alreves buscar un caracteres dentro de un string / muestra la ubicacion de la primer letras buscada 
print (s.rfind('a'))

#creamos una tupla / join en ua tuplca
t= "h","o","l","a"
s= ";"
print(s.join(t))
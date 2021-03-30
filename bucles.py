#Bucles / ciclos

#While

edad = 0
while edad <= 20:
    print ("Tienes:"+str(edad))
    edad = edad + 1

#Condicion  mas ciclo
edad =0
while edad <= 20:
    if edad == 15:
       edad = edad + 1
       break
    print ("Tienes:"+str(edad))
    edad = edad + 1

#for i 

lista = ['elemento 1','elemento 2','elemento 3']

#recorrer letras de una string
for letra in "cadena":
    print(letra)

#recorrer una lista / tupla o diccionario
for elementos in lista:
    print(elementos)

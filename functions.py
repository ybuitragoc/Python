#functions

#Suma dos numeros / # Add two numbers
def my_function(number_one=0, number_two=0):
    print(number_one + number_two)
my_function(1)

#Imprimir mas elementos / #Print more items
def cantidad_cadenas (cadena, v=2, *algomas):
    for cadena in algomas:
        print(cadena * v)

cantidad_cadenas("cadena",5,[1,2,3,4,5,6,7,8,9])

#crear un diccionario e imprimirlo / #create a dictionary and print it
def create_dicc (cad,v=0,**algomas):
    print (algomas['cadenaextra'])
  
create_dicc("Hola", 3, cadenaextra='Hola')

#return valor / value return

def ret (num_1=0, numer_2=2):
    return num_1 + numer_2
resultado_suma = ret (1,2)
print(resultado_suma)



#POO

#Crear clase / Create class
class Human:
    def __init__(self,edad, pais, nombre):
        self.edad = edad
        self.pais = pais
        self.nombre = nombre
        print ("I'm a new object")
    def toTalk(self, mensaje):
        print(mensaje, "I'm", self.nombre)

#create object
object_1 = Human(18, 'Colombia', 'Pedro')
object_2 = Human(39, 'Peru', 'Raul')

#print atribute
print("I'm ",object_1.nombre, "and I'm " , object_1.edad, " Years old, and I'm from ", object_1.pais)
print("I'm ",object_2.nombre, "and I'm " , object_2.edad, " Years old, and I'm from ", object_2.pais)

#method
object_1.toTalk("Hi")
object_2.toTalk("Hi")
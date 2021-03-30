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

#created  new class
#heredar una clase
class SystEng(Human):
    def developer(self,code):
        print("I'm goint to programming in", code)
 #heredar una clase   
class Lowyer(Human):
    def studyCase(self,de):
        print("I must study", de)


   
#create object
object_1 = SystEng(18, 'Colombia', 'Pedro')
object_2 = Lowyer(39, 'Peru', 'Raul')

#print atribute
print("I'm ",object_1.nombre, "and I'm " , object_1.edad, " Years old, and I'm from ", object_1.pais)
print("I'm ",object_2.nombre, "and I'm " , object_2.edad, " Years old, and I'm from ", object_2.pais)

#cada objeto comparte los atributos de clase Humano, pero tiene sus funciones 
object_1.developer("Python")
object_2.studyCase("laws")
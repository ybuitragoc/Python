#POO

#Crear clase / Create class
class Human:
    def __init__(self):
      print ("I'm a new object")
    def toTalk(self, mensaje):
        print(mensaje)

#created  new class
#heredar una clase
class SystEng(Human):
    def __init__(self):
        print("Hola")

    def developer(self,code):
        print("I'm goint to programming in", code)
 #heredar una clase   
class Lowyer(Human):
    def __init__(self, escuela):
        print("Licenciado de derecho egregado de",escuela)
    def studyCase(self,de):
        print("I must study", de)

#herecia multiple // tener en cuenta el orden para ingresar los parametros
class Estudioso(Lowyer, SystEng):
    pass

object_1 = Estudioso("Universidad central")
object_1.toTalk("Soy herencia multiple")
object_1.developer("En C++")
object_1.studyCase("Familia")
#Booleans, logical operators, and strings

#String con salto de linea / #String with line break
text_uno = 'text \n uno'
text_dos = "text dos"
print (text_uno)


#String con salto de linea y tabulacion / String with line break and tab
text_dos = "text \n\tdos"
print (text_dos)

#String multiples saltos / String multiple jumps
text_tres = """texto 3
text 4
text 5
text 6
text 7
text8
"""
print (text_tres)

#repetir la cadena n veces // #repeat the string n times
text_cuatro = "Cadena " * 5
print (text_cuatro)

#concatenar dos cadenas // #concatenate two strings
texto_cinco = "Cadena 1 "
text_seis = "Cadena 2"
text_siete = texto_cinco+text_seis
print (text_siete)

#Valores boleanos // #Boolean values
bT = True
bF = False

#Operadores logicos // #Logical operators
bAnd = True and False
bOr = True or False
bNot = not True 
print(bAnd)
print(bOr)
print(bNot)
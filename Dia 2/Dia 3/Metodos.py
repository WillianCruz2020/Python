texto ="Este es el texto de Willian"

#Convierte todo a mayuscula
resultado = texto.upper()
#R/: ESTE ES EL TEXTO DE WILLIAN

#Devuelve solo el indice indicado en mayuscula
resultado1 = texto[2].upper()
#R/: T

#Devuelve todo el texto en minuscula
resultado2 = texto.lower()
#R/: este es el texto de willian

#Devuelve el indice indicado en minuscula si este
#esta en mayuscula si ya estaba en minuscula no devuelve
#nada
resultado3 = texto[0].lower()
#R/: e

#Split: Separa el texto tomando como separador los espacios en blanco
resultado4 = texto.split()
#R/: ['Este', 'es', 'el', 'texto', 'de', 'Willian']

#Split: Cuando especificamos una letra dentro de los parentesis, esa toma como separador
resultado5 = texto.split("t")

#find: Busca el caracter y devuelve el indice donde se encuentra
# a diferencia de index, cuando no encuentra un caracter no devuelve
# error, si no un -1
resultado6 = texto.find("e")
resultado7 = texto.find("z")
#R/: 3
#R/: -1

#replace: Remplaza el texto buscado dentro las primeras comillas y
# lo remplaza por el texto en las segundas comillas
resultado8 = texto.replace("Willian", "Wallas")
#R/: Este es el texto de Wallas

#join: Crea Texto a partir de una lista
#en el metodo primero se define el separador entre comillas
a = "Willian"
b = "aprendera"
c = "a"
d = "Programar, cueste lo que cueste"
e = "-".join([a,b,c,d])

resultado9 = e
#R/: Willian-aprendera-a-Programar, cueste lo que cueste



print(resultado)
print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)
print(resultado7)
print(resultado8)
print(resultado9)

lista_palabras = ["La","legibilidad","cuenta."]
resultado = " ".join(lista_palabras)
print(resultado)


texto1 = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado10 = texto1.replace("difícil","fácil")
resultado11 = resultado10.replace("mala","buena")
print(resultado11)
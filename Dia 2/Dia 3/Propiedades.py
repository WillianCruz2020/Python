#Los string son inmutables, no se pueden cambiar
#lo que se puede hacer es sustituir las variables

n1 = "Kari"
n2 = "na"
#Suma de string
print(n1 + n2)
#R/: Karina

#Multiplicacion de los string
print(n1 * 5)
#R/: KariKariKariKariKari

#Depende de las lineas que querramos que contenga nuestro
#Texto debemos de agregar la cantidad de comillas
poema = """Mil pequielos peces blancos 
como si hirviera 
el color del agua"""

print(poema)
#R/: Mil pequielos peces blancos
#como si hirviera
#el color del agua

#Consulta si texto o palabras estan dentro de los string
#in: es relativo a si esta dentro del texto
#not in: es relativo a si no esta

print("agua" in poema)
#R/: True

print("sol" in poema)
#R/: False

print("sol" not in poema)
#R/: True

print("agua" not in poema)
#R/: False

# la propiedad lend: cuenta cuantos caracteres posee
print(len(poema))
#R/: 64
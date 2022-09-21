mi_lista = ["a","b","c"]
mi_lista2 = ["d","e","f"]
#Con las listas es posible sumar es decir concatenar las listas
#y tambien a diferencia de los string estas si son mutables o
#modificables.

#Concatenar listas
print(mi_lista+mi_lista2)

#Imprimir con type el tipo de elemento de la lista
print(type(mi_lista))

#cuenta los elementos de una lista
print(len(mi_lista))

#Se pueden indexar ubicar por medio del indice los
# los valores que estan dentro de la lista
print(mi_lista[0])
print(mi_lista2[0])

#Se pueden sustituir los valores de la lista,
#dentro de los corchetes se coloca el indice del elemento
#a sustituir
mi_lista[1] = "Alfa"
print(mi_lista)

#Agregar un elemento de una lista por medio de el metodo append
#y colocar entre comillas el elemento a agregar
mi_lista.append("g")
print(mi_lista)

#Metodo pop sirve para elimiar elmentos de una lista,
#si los parentesis se dejan sin contenigo elimina el ultimo
#elemento de la lista
mi_lista.pop()
print(mi_lista)

#Se puede agregar a una variable el elemento eliminado
#de la lista
eliminado = mi_lista.pop(2)
print(eliminado)

#El metodo sort funciona para ordenar la lista de forma ascendente
mi_lista.sort()
print(mi_lista)


#El metodo reverse es para ordenar la lista pero
#de atras hacia adelante.
mi_lista.reverse()
print(mi_lista)


#LISTA DE NÚMEROS ENTEROS

numeros = [4,3,8,12,6,10,14,3,6]
print("La lista es ",numeros)

numeros.pop() #elimina el último elemento de la lista
#nombredelalista.pop([nrodelelemento])
print("- Sin el último elemento ",numeros)

numeros.insert(0,2) #inserta un elemento en la lista
#nombredelalista.insert(posicion, "elemento")
print("- Con el '2' agregado ",numeros)

numeros = set(numeros) #convierte la lista en un set
#en un set para que nos devuelva la lista ordenada y sin los elementos repetidos
print("- Sin los elementos repetidos ", numeros)

medianumeros = sum(numeros)/ len(numeros) #promedio
print("- La media de la lista modificada es ", medianumeros)

numeros = list(numeros) #lo volvemos a convertir a lista para poder acceder a elementos
#para sacar la mediana de una lista par, sumamos los 2 datos de la mitad y lo dividimos en 2.
numeros = (numeros[3]+numeros[4])/2
print("- La mediana de la lista es ", int(numeros))
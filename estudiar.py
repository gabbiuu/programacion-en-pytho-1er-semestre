parrafo = "La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad suspilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participación democrática"
parrafoo = parrafo.upper()
palabrauniversidad = parrafoo.count("UNIVERSIDAD")

print("La palabra universidad se repite: ", palabrauniversidad, "veces.")

lista1 = []
for i in range(500, 801, 10):
    lista1.append(i)
print(len(lista1))

lista2=[]
for i in range(456, 0, -2):
    lista2.append(i)
    if len(lista2) == 31:
        break
listas = lista1 + lista2
print(sum(listas))

### ESTUDIAR
i = 0
while i >= 0 and i <= 9:
    print(round(i, 2))
    i += 0.1


for i in range(100, 200):
    print(i)
    
for i in range(5,21,3):
    print(i)
    
num = int(input("Ingrese número entero positivo: "))
num2 = (num*2)-1
if num>0:
    for i in range(num, num2 ):
        print(i)
else:
    print("ingrese un numero positivo.")
    
cantidad = int(input("Ingrese cantidad: "))
num= []
for i in range(cantidad):
    numss = (int(input("Ingrese un número:")))
    num.append(numss)
    sum(num)
print(sum(num))

for i in range(0,101,3):
    print(i)
    i+= 1
    
#append: agrega un elemento a la lista 
#insert : inserta un elemento en una pocicion espesifica de la lista 
#remove elimina la primera ocurrencia de una lista 
#pop : borra y retorna el ultimo elemento de una lista 
#sort : ordena los elementos de la lista de manera asendente 
#count : devuelve el numero de veces que aparece el valor en la tupla 
#index : devuelve el indice del elemento seleccionado en la tupla 
#sorted : entrega una lista ordenada con los elementos de una tupla 
#item :devuelve una lista de tuplas, donde cada tupla tiene su clave 
#keys : devuelve una lista con todas las claves de un diccionario 
#round : dos decimales
#diccionarios
#keys() devuelve claves de un diccionario
#values() devuelve valores de un diccionario
# items() devuelve una lista de tuplas, con clave y valores del diccionario.
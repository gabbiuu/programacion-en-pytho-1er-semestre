# FUNCIONES

# Declarando una función
def mi_primera_funcion():
    print("Esta es mi primera función")   
mi_primera_funcion()

# DECLARANDO UNA FUNCIÓN Y UTILIZANDO LISTAS
def concatenar(lista1, lista2):
    return lista1 + lista2

lista1 = [1,2,3]
lista2 = [4,5,6]

#concatenar() no hace nada
print(concatenar(lista1, lista2)) 

# FUNCIONES CON OPERACIONES
def multiplicacion(num1,num2):
    return num1*num2

#multiplicacion() no hace nada, hay que darle argumentos
print(multiplicacion(10,2))

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

a = int(input("Ingrese valor de a: "))
b = int(input("Ingrese valor de : "))

resultado = suma(a,b) # se llama a la función suma
print("La suma es de ", resultado)
    
resultado2 = resta(a,b) # se llama a la función resta
print("La resta es de ", resultado2)


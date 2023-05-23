#01-DATOS DE TIPO NUMÉRICO
edad = 29 #entero
estatura = 1.62 #real
peso = 70.5
complejo = 1+4j #complejo

print("######## 01-DATOS NUMÉRICOS ########");
print(f"mi estatura es de {estatura} y el peso es de {peso}")
print()

#OPERACIÓN ARITMÉTICA BÁSICA
imc =peso / (estatura**2)
print("Mi imc es de :", imc,"\n")

#"\n" salto de linea

print("Mi imc es de: {:.2f} ".format (imc),"\n") #determina los decimales que queremos mostrar

#02-DATOS DE TIPO CADENA DE CARACTERES
asignatura = 'Programación'
carrera = "Ingeniería civil en Informática"
print("La asignatura de", asignatura, "corresponde a la carrera de", carrera)

#Función para contar caracteres ,len
#UTILIZANDO LA FUNCIÓN len (CUENTA LA CANTIDAD DE CARACTERES)
print("La cantidad de caracteres de la palabra", asignatura, "es de:" ,len(asignatura))
print("La cantidad de caracteres de la palabra", carrera, "es de:" ,len(carrera))

#03-VALORES BOOLEANOS
ampolleta = False
interruptor = True
print(ampolleta,interruptor)
print("La variable ampolleta es de tipo:", type(interruptor),"\n") 
#type sirve para indicar el tipo de dato con el que estamos trabajando

#PODEMOS TRANSFORMAR CUALQUIER VALOR A UN BOOLEANO AL IGUAL QUE UN STRING, INT, ETC.
print(bool(0))
print(bool(""))
print(bool(None))
print(bool("True"))
print(bool(1))
print("\n")
#Booleano es un tipo de dato: verdadero/falso

#INICIALIZANDO LISTAS DE 2 MANERAS
nueva_lista = list()
otra_lista = []
print("Esta es una lista vacía:", nueva_lista)
print("Esta es otra lista vacía:", otra_lista)
print(type(otra_lista))

#DECLARANDO TRES LISTAS DIFERENTES
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian", "Marco"]
num = [1,2,3,4,5,6]
lenguaje = ["Phyton"]

data = ['Osorno', {'UV':'nivel bajo','Temp"C': 15}, (-40.5725,-73.1353)]
listamixta = ['Felipe', 100, True]

print("Lista de cadena de caracteres:", estudiantes)
print("Lista de números:", num)
print("Lista de un elemento:", lenguaje)
print("Esta es una lista mixta:", listamixta)
print("Esto igual es una lista:", data)
print(len(listamixta)) #para saber la cantidad de elementos de una lista
print(estudiantes.count("Marco")) #Cantidad de ocurrencias de un elemeto.
#.count => cantidad de veces que se repite un elemento.
#len => cantidad ded elementos que hay en una lista.
print(num.count(1))

lenguaje = ["JavaScript"]
print("Nuevo valor del arreglo de un elemento:", lenguaje)

print(estudiantes[0]) #1° elemento de la lista
print(estudiantes[1]) #2° elemento de la lista
print(estudiantes[4]) #INCORRECTO no existe
print("Posicion -2", estudiantes [-2]) 

#SUMA DE LISTAS
print("suma de listas", estudiantes + num)

#funciones
print(list("Phyton"))
print(list(range(10)))
print("\n")

#05 - TUPLAS (No mutables)
newtupla = tuple()
grupo1 = ("Daniel", "Cristian", "Felipe", 200, 100, "Daniel")
print("####### 05-TUPLAS- #######")
print(type(grupo1))

#accediendo al primer elemento de la tupla
print(grupo1[0])

#muyestra el indice del primer elemento buscado
print("Indice del elemento:", grupo1.index ("Daniel"))

#Las duplas no mutan
#grupo1[0] = "Constanza"
#print(grupo1)#

#obteniendo un trozo de la tupla
grupo2 = ("Pedro", 100, )

#MODIFICAR UNA TUPLA
#grupo1 = list(grupo1)
#print("La tupla ahora es de tipo:", type(grupo1,"\n"))
#print("\n")

#06 - SETS (CONJUNTOS) - ESTRUCTURA FIJA
#FORMAAS DE INICIALIZAR UN SET
conjunto_vacio = set()
conjunto_vacio1 = {} 
print(type(conjunto_vacio1))
conjunto_colores = set({"Azul", "Rojo", "Verde"}) #UTILIZANDO LA FUNCIÓN SET
conjunto_animales = {"Gato", "Perro", "Loro"} #UTILIZANDO LLAVES

print(type(conjunto_colores)) #TIPO DE DATO SET
print(type(conjunto_animales)) #TIPO DE DATO SET

#print(conjunto_animales[0]) #ACCEDIENDO AL PRIMER ELEMENTO DEL SET #no se puede hacer????
conjunto_colores.add("Celeste") #PARA AGREGAR ELEMENTOS A LA LISTA (.ADD)
print("El set de elementos lo conforman:", conjunto_colores)

diccionario1 = dict()
diccionario2 = {}

datos_personales = {
    "Nombre": "Victor",
    "Institucion": "ULagos",
    "Edad": 29,
    "Asignatura": {"Estructura de Datos", "Programación"}
} 
print("Diccionario inicial:", datos_personales)

#Consulta la cantidad de elementos de un diccionario
print(len(datos_personales))

print(datos_personales["Institucion"])

#Agregando un nuevo clave al diccionario
datos_personales["Ciudad"]="Osorno"
print(datos_personales)
print("Diccionario con el nuevo campo:", datos_personales)

#Eliminando un nuevo clave del diccionario
del datos_personales ["Ciudad"]



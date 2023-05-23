PI=3,14

#01-DECLARANDO VARIABLES DE TIPO CADENA DE TEXTO
nombre = "Gabriela"
name = "Victor"

#02-IMPRESION DE UNA VARIABLE
print(nombre)
print("hola soy", nombre)

#Declarando una tercera variable de tipo numérico
edad = 18

#IMPRESION DE TEXTO + VARIABLE
print("Mi edad es de", edad)

#IMPRIMIENDO 2 VARIABLES EN UNA MISMA LINEA
print("Hola mi nombre es", nombre, "y tengo", edad) #impresión separada con comas
print("Hola mi nombre es"+  " " + nombre + " " + "y tengo"+ " " +  str(edad)+ " " + "años" ) #concatenación con +
print(f"Hola mi nombre es {nombre} y tengo {edad} años") #formato de cadenas literales

#05-ACTUALIZANDO LA VARIABLE NOMBRE (Mutable)
nombre = "Millaray"
name = "Diego"
print("Hola, mi nuevo nombre es", nombre)

#06- ¿VARIABLES EN UNA SOLA LINEA? (se puede, pero no es recomendable)
ciudad, region, pais, year = "Puerto Montt", "Los Lagos", "Chile", 2023.
print("Nací en la ciudad de", ciudad, ", región de", region, ", país", pais, ",en el año", year) 

#UTILIZANDO LA INSTRUCCIÓN INPUT
nombre1 = input("¿Cuál es tu nombre?\n")
edad1 = input("¿Cuál es tu edad?\n")

print("Tu nombre es:",nombre1, "y tu edad es", edad1)
      



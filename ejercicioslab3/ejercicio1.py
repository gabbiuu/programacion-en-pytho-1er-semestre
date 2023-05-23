#DETERMINAR EL NÚMERO MENOR Y MAYOR ENTRE LOS 3

num1 = int(input("Ingrese el primer número entero "))
num2 = int(input("Ingrese el segundo número entero "))
num3 = int(input("Ingrese el tercer número entero "))

if num1 > num2 and num1 > num3:
    print("El número ", num1, " es el mayor de los tres")
elif num2 > num1 and num2 > num3:
    print("El número ", num2, " es el mayor de los tres")
elif num3 > num1 and num3 > num2:
    print("El número ", num3, " es el mayor de los tres")
else:
    print("Inválido, ingrese nuevos valores")
    
if num1 < num2 and num1 < num3:
    print("El número ", num1, " es el menor de los tres")
elif num2 < num1 and num2 < num3:
    print("El número ", num2, " es el menor de los tres")
elif num3 < num1 and num3 < num2:
    print("El número ", num3, " es el menor de los tres")
else:
    print("Inválido, ingrese nuevos valores")
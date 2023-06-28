# ÁREA DE UN TRIÁNGULO

a = abs(float(input(("Ingrese la medida en cm del primer lado "))))
b = abs(float(input(("Ingrese la medida en cm del segundo lado "))))
c = abs(float(input(("Ingrese la medida en cm del tercer lado "))))
#¿cómo se le ponen restricciones para que solo acepte número positivos?
#'abs' transforma números negativos en positivos

p = (a + b + c)/2
area = p*(p-a)*(p-b)*(p-c)


if a == b and b != c and c != a :
    print("Es un triángulo isósceles")
elif a != b and b == c and c != a :
    print("Es un triángulo isósceles")
elif a != b and b != c and c ==a :
    print("Es un triángulo isósceles")
elif a != b and b != c and c != a :
    print("Es un triángulo escaleno")
else:
    print("Es un triángulo equilátero")
    
print("Y su área es ", area)
    

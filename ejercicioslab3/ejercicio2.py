# DETERMINAR QUÉ PALABRA TIENE MÁS CARÁCTERES Y CUÁL MENOS

palabra1 = str(input("Ingrese la primera palabra "))
palabra2 = str(input("Ingrese la segunda palabra "))

#¿cómo hago que sólo me acepte o me lea las palabras y no los números?

if len(palabra1) > len(palabra2):
    print("La palabra", palabra1, "tiene más carácteres")
    print("La palabra", palabra2, "tiene menos carácteres")
elif len(palabra1) < len(palabra2):
    print("La palabra", palabra2, "tiene más carácteres")
    print("La palabra", palabra1, "tiene menos carácteres")
else:
    print("Ambas palabras tinen la misma cantidad de carácteres")
    

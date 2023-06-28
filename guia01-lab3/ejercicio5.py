# PROMEDIOS

lab1 = abs(float(input("Ingrese nota del primer laboratorio: ")))
lab2 = abs(float(input("Ingrese nota del segundo laboratorio: ")))
lab3 = abs(float(input("Ingrese nota del tercer laboratorio: ")))

operacion = lab1 * 0.3 + lab2 * 0.4 + lab3 * 0.3
print("Su promedio es ",operacion)

if operacion < 4.0:
    print("El estudiante reprobó la meteria")
elif operacion > 4.0:
    print("El estudiante aprobó la asignatura")
elif operacion > 6.0:
    print("El estudiante aprobó con distinción")
else:
    print("Inválido, intente nuevamente")
datos_personales = {
    "Nombre": input("ingrese su nombre "),
    "Asignatura": input("Ingrese asignatura "),
    "Nota del laboratorio n°1": float(input("Ingrese nota n°1 del laboratorio ")),
    "Nota del laboratorio n°2": float(input("Ingrese nota n°2 del laboratorio "))
} 

nombre = datos_personales["Nombre"]
asignatura = datos_personales["Asignatura"]
notalab= datos_personales["Nota del laboratorio n°1"]
notalab2=datos_personales["Nota del laboratorio n°2"]

op = notalab*0.3 + notalab2*0.7


datos_personales["promedio"]=round(op,1)

print (datos_personales)

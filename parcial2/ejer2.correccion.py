# Calcular la media de calificaciones de la asignatura de Programación. Deducir cuántas son
# más altas que la media y cuántas más bajas que dicha media. Se solicita un mínimo de 10
# notas. Estas calificaciones se ingresarán por teclado y no se permite notas inferiores a 1.0 ni
# mayores a 7.0

veces = int(input("¿cuántas notas ingresará?: "))
lista = []
mayoramedia = []
menoramedia = []

if veces >= 10:
    for i in range(veces):
        nota = (float(input("Inserte nota: ")))
        
        if nota >= 1.0 and  nota <= 7.0:
             lista.append(nota)
             media = sum(lista)/len(lista)
        else:
             print("NOTA INVVÁLIDA")                                     
else: 
    print("Mínimo 10 notas")

print(media) 

print("Las notas mayor a la media son: ", mayoramedia)
print("Las notas menor a la media son: ", menoramedia)

while nota >= media:
    print()
    mayoramedia.append(nota)
    print(mayoramedia)
    break
while nota <= media:
    menoramedia.append(nota)
    print(menoramedia)
    break
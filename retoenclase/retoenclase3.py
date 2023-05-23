ciudades = ["Santiago", "Temuco", "Osorno", "Punta Arenas"]
indicecalidadaire = [134, 99, 245, 50]
print()
min = min(indicecalidadaire)
max = max(indicecalidadaire)
ciumin = ciudades[indicecalidadaire.index(min)]
ciumax = ciudades[indicecalidadaire.index(max)]
print("El nombre de la ciudad con el índice más bajo es : ", ciumin)
print("El nombre de la ciudad con el índice más alto es : ", ciumax)
print()
print("CATEGORIAS")
if min > 0 and min <= 50:
    print("El índice de la ciudad más bajo es : BUENA")
elif min > 50 and min <= 100:
    print("El índice de la ciudad más bajo es :MODERADA")
elif min >100 and min <= 150:
    print("El índice de la ciudad más bajo es :DAÑINA A LA SALUD PARA GRUPOS SENSIBLES")
elif min > 150 and min <= 200:
    print("El índice de la ciudad más bajo es :DAÑINA A LA SALUD")
elif min > 200 and min <= 300:
    print("El índice de la ciudad más bajo es :MUY DAÑINA A LA SALUD")
elif min > 300:
    print("El índice de la ciudad más bajo es :PELIGROSA")
else: print("NO ENTRA EN NINGUNA CATEGORÍA")

if max > 0 and max <= 50:
    print("El índice de la ciudad más alta es :BUENA")
elif max > 50 and max <= 100:
    print("El índice de la ciudad más alta es :MODERADA")
elif max >100 and max <= 150:
    print("El índice de la ciudad más alta es :DAÑINA A LA SALUD PARA GRUPOS SENSIBLES")
elif max > 150 and max <= 200:
    print("El índice de la ciudad más alta es :DAÑINA A LA SALUD")
elif max > 200 and max <= 300:
    print("El índice de la ciudad más alta es :MUY DAÑINA A LA SALUD")
elif max > 300:
    print("El índice de la ciudad más alta es :PELIGROSA")
else: print("NO ENTRA EN NINGUNA CATEGORÍA")



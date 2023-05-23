regiones = {
    "ID Región" : {8, 10}, 
    "Nombre" : {"BioBío", "Los Lagos"},
    "Superficie (Km2)" : {23890, 48583},
    "Habitantes(2017)" : {1556805, 828708}
}
print("El diccionario es: ", regiones)

densidad1 = 1556805 / 23890
densidad2 = 828708 / 48583
regiones["Densidad"] = round(densidad1,1), round(densidad2,1)

print()
regiones["Capital"] = "Concepción", "Puerto Montt"

comBioBio = ["Lota", "Lebu", "Los Ángeles"]
comLagos = ["Castro", " Puerto Varas", "Purranque"]
regiones["Comunas: "] = comBioBio, comLagos

provbiobio = ("BioBío", "Arauco", "Concepción")
provloslagos = ("Osorno", "LLanquihue", "Chiloé", "Palena")
regiones["Provincia"] = provbiobio, provloslagos

print("El diccionario con las modificaciones es :",regiones)
print()
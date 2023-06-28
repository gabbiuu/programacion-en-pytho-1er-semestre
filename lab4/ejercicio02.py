
a = ["Rojo", "Verde", "Celeste", "Violeta"]
b = ["Osorno", "Puerto Montt", "Puerto Varas", "Valdivia"]

def encontrar_palabra_mas_larga(a):
    palabra_mas_larga = ""
    for palabra in a:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga

palabra_mas_larga_a = encontrar_palabra_mas_larga(a)
print(palabra_mas_larga_a)

def encontrar_palabra_mas_corta(b):
    palabra_mas_corta = b[0]
    for palabra in b:
        if len(palabra) < len(palabra_mas_corta):
            palabra_mas_corta = palabra
    return palabra_mas_corta

palabra_mas_corta_b = encontrar_palabra_mas_corta(b)
print(palabra_mas_corta_b)

def concatenar_listas(a, b):
    return a + b

lista_concatenada = concatenar_listas(a, b)
print(lista_concatenada)

def transformar_a_mayusculas(lista):
    lista_mayusculas = []
    for palabra in lista:
        lista_mayusculas.append(palabra.upper())
    return lista_mayusculas

a_mayusculas = transformar_a_mayusculas(a)
b_mayusculas = transformar_a_mayusculas(b)

print(a_mayusculas)
print(b_mayusculas)

def ordenar_lista(lista):
    return sorted(lista)

a_ordenada = ordenar_lista(a)
b_ordenada = ordenar_lista(b)

print(a_ordenada)
print(b_ordenada)
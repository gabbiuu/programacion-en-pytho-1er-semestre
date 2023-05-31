# FUNCIÓN QUE RECIBA UNA FRASE POR CONSOLA, Y DEVUELVA UN DICCIONARIO CON LAS PALABRAS QUE CONTIENE Y SU LONGITUD.

def fraseadiccionario (frase ):
    palabras = frase.split()
    diccionario = {}
    
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
        
    return diccionario
    
frase = str(input("Ingrese frase: "))
print(fraseadiccionario (frase))

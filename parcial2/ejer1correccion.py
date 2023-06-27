# Construir un algoritmo que permita generar enteros de 3 en 3 comenzado por el 2 hasta el
# valor máximo que será menor que 30. Calcular la suma de los enteros generados que sean
# divisibles por 5, y la suma de los enteros generados que sean impares. 

divin5 = []
impares = []  
for i in range(2, 30, 3):
    print(i)
    while i % 5 == 0:
        divin5.append(i)
        break
    while i % 2 !=  0:
        impares.append(i)
        break
        
print("Los números divisibles en 5 son: ", divin5)
print("- Su suma es: ", sum(divin5))
print("Los números impares son: ", impares)
print("- Su suma es: ", sum(impares))

    
    



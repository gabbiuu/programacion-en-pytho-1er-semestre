#  HACER UN ALGORITMO QUE DETECTE SI UN NÚMERO ES PAR O IMPAR.
# ADEMÁS SI ES UN NÚMERO PRIMO Y SI ES MAYOR O MENOR A 50.

num = int(input("Ingrese número: "))
 
if num % 2 == 0 :
    print("Es un número par\n")
else:
    print("Es un número impar\n")

def es_primo(num):
    if num < 2:
        return False
    for i in range (2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def es_mayor_a_50(num):
    if num >50:
        return True
    else:
        return False

if es_primo (num):
    print(num, " es un número primo")  
else:
    print(num, " no es un número primo")
    
if es_mayor_a_50(num):
    print(num, " es mayor a 50")
else:
    print(num, " es menor o igual a 50")
    

    

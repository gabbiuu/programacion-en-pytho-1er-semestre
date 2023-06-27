
def bisiesto(año): 
    if año < 0: 
        print("el año",año, "no existe")
    elif (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        print("el año",año, "es bisiesto")
    else: 
        print("el año", año, "no es bisiesto")

año = int(input("ingrese el año \n")) 
bisiesto(año)
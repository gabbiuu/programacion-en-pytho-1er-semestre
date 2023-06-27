#BUCLES
#BUCLE INFINITO
# control + c para terminarlo


# WHILE
num = 0
while num <= 200 :
     print (num)
     num += 2
else: print("Mi condición es igual o mayor a 200")
print("Segundo bucle terminado\n")

while num <= 300 :
     print (num)
     num += 2
     if num == 250: #si el if se corre a la izquiera no lo lee
        print("Mi condición es igual a 250")
print("tercer bucle terminado\n")

while num <= 400 :
    print(num)
    num +=2
    if num == 350:
        print("Se detiene la ejecución")
        break
print(num)
print("Cuarto bucle terminado\n")

#LOOP INFINITO + BREAK
while True :
    parametro = input (">")
    if parametro == "exit": #EL EXIT TERMINA EL BUCLE INFINITO
        break
    else: 
        print(parametro)
  
# FOR       
for i in (1,2,3,4,5,6,7,8,9,10): #ESTO NO ES LA MANERA CORRECTA DE HACERLO
    print(i)
    
newlist = [1,2,3,4,5,6,7,8,9,10] #ASI SE DEBE HACER
for i in newlist:
    print(i)
    
for i in range(11): #TAMBIÉN SE PUEDE HACER ASÍ (del 0 al 10)
    print(i)
    
for i in range(1,11): #TAMBIÉN SE PUEDE HACER ASÍ (del 1 al 10)
    print(i)




        




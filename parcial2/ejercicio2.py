veces = int(input("¿cuántas notas ingresará?: "))
lista = []

if veces >= 10:
    for i in range(veces):
        nota = (print(float(input("Inserte nota: "))))
        
        if nota >= 1.0 and nota <= 7.0:
             lista.append(nota)
             media = sum(lista)/len(lista)
             print(media) 
                        
        else:
            print("NOTA INVÁLIDA")
else: 
    print("Mínimo 10 notas")


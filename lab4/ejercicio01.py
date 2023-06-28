pacientes = [["Pedro", 1.78], ["Constanza", 1.56], ["Amanda", 1.62], ["Dario", 1.89], ["Fernanda", 1.67]]

def estatura_minima(pacientes):
    estatura_min = pacientes[0][1]
    
    for paciente in pacientes:
        if paciente[1] < estatura_min:
            estatura_min = paciente[1]
    
    return round(estatura_min, 1)


def insertar_paciente(pacientes, nuevo_paciente):
    pacientes.append(nuevo_paciente)
    return pacientes

nuevo_paciente = ["Ricardo", 1.71]


def encontrar_paciente(pacientes):
    for paciente in pacientes:
        if paciente[0] == "Dario":
            print(pacientes[3])
            return
    print("No se encuentra el paciente")



estatura_menor = estatura_minima(pacientes)
print(estatura_menor)

pacientes_actualizada = insertar_paciente(pacientes, nuevo_paciente)
print(pacientes_actualizada)

encontrar_paciente(pacientes)
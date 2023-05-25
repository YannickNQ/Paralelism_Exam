"""
Curso: Paralelismo, Concurrencia y Sistemas Distribuidos
Estudiante: Nina Quispe Yánnick Axel
"""
import subprocess as sp

def listInstallPrograms():
    #Ejecutar el comando wmic para obtener la lista de programas instalados
    output = sp.check_output(['wmic', 'product', 'get', 'name']).decode('latin-1')
    #Dividir la salida en lineas e ignorar el encabezado (primera linea)
    lines = output.split('\n')
    lines = lines[1:]

    installPrograms = [] #lista de programas instalados

    for line in lines:
        line = line.strip()
        if line:
            installPrograms.append(line)
    
    return installPrograms

#Llamar a la función para obtener la lista de programas instalados
ProgramsList = listInstallPrograms()
print("Programas Instalados")
print("--------------------")
for program in ProgramsList:
    print(program)
"""
Curso: Paralelismo, Concurrencia y Sistemas Distribuidos
Estudiante: Nina Quispe Yánnick Axel
"""
import psutil

def listProcesses():
    processes = []
    for process in psutil.process_iter(['pid', 'name', 'status', 'num_threads']):
        processes.append({
            'ProcessId': process.info['pid'],
            'ProcessName': process.info['name'],
            'ProcessStatus': process.info['status'],
            'ProcessThreadCount': process.info['num_threads']
        })
    return processes

# Llamar a la función para obtener la lista de processs
list_process = listProcesses()

#Imprimir los procesos en ejecución
print("Procesos en ejecución:")
print("----------------------")

for process in list_process:
    if process['ProcessStatus'] == 'running':
        print(f"| ProcessId: {process['ProcessId']}\t| ProcessName: {process['ProcessName']}|\t ProcessThreadCount: {process['ProcessThreadCount']} |")

print("Procesos Detenidos:")
print("----------------------")
for process in list_process:
    if process['ProcessStatus'] == 'stopped':
        print(f"| ProcessId: {process['ProcessId']}\t| ProcessName: {process['ProcessName']}|\t ProcessThreadCount: {process['ProcessThreadCount']} |")

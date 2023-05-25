import subprocess as sp
import psutil

def resourcesMemory():
    total_memory = psutil.virtual_memory().total
    available_memory = psutil.virtual_memory().available
    hardware_reserved = total_memory - available_memory

    output_Speed = sp.check_output(["wmic", "memorychip", "get", "speed"]).decode('latin-1')
    lines_speed = output_Speed.strip().split('\r\r\n')

    output_Bank = sp.check_output(["wmic", "memorychip", "get", "BankLabel"]).decode('latin-1')
    lines_bank = output_Bank.strip().split('\r\r\n')
    
    resources_Memory = {
        "Speed": 0,
        "Slots": 0,
        "HardwareMemoryReserved": 0
    }

    for line in lines_speed[1:]:
        if line.strip():
            resources_Memory["Speed"] = int(line.strip())

    count = 0
    for line in lines_bank[1:]:
        if line.strip():
            count += 1
    resources_Memory["Slots"] = count

    resources_Memory["HardwareMemoryReserved"] = hardware_reserved/(1024**3)
    
    return resources_Memory

    

memoryResources = resourcesMemory()

print(f"Velocidad: {memoryResources['Speed']} MHz")
print(f"Numero de Slots: {memoryResources['Slots']}")
print(f"Reserva de Hardware: {memoryResources['HardwareMemoryReserved']} MB")

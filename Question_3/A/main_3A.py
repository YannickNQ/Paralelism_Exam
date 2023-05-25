import subprocess as sp

def resourcesCPU():
    # Ejecutar el comando wmic para obtener la información de la CPU
    command = "wmic cpu get NumberOfCores, NumberOfLogicalProcessors, L2CacheSize, L3CacheSize"
    output = sp.run(command, capture_output=True, text=True)

    # Parsear el resultado
    lines = output.stdout.strip().split('\n')
    header = lines[0].strip().split()
    sockets = len(lines) - 2

    resources_CPU = {
        "Sockets": sockets,
        "Nucleos": [],
        "ProcesadoresLogicos": [],
        "CacheL2": [],
        "CacheL3": []
    }

    for line in lines[2:]:
         values = line.strip().split()
         for i in range(len(header)):
            key = header[i]
            value = values[i]
            if key == "NumberOfCores":
                cores = int(value)
                resources_CPU["Nucleos"].append(cores)
            elif key == "NumberOfLogicalProcessors":
                logicalProcessors = int(value)
                resources_CPU["ProcesadoresLogicos"].append(logicalProcessors)
            elif key == "L2CacheSize":
                cachel2 = value
                resources_CPU["CacheL2"].append(cachel2)
            elif key == "L3CacheSize":
                cachel3 = value
                resources_CPU["CacheL3"].append(cachel3)

    return resources_CPU

# Llamar a la función y mostrar los recursos.

cpu_resources = resourcesCPU()
print("Recursos de la CPU:")
print("-------------------")
print(f"Sockets: {cpu_resources['Sockets']}\n")
for i in range(cpu_resources['Sockets']):
    print(f" > Socket {i+1}: ")
    print(f" \t>> Núcleos: {cpu_resources['Nucleos'][i]}")
    print(f" \t>> Procesadores lógicos: {cpu_resources['ProcesadoresLogicos'][i]}")
    print(f" \t>> Caché L2: {cpu_resources['CacheL2'][i]}")
    print(f" \t>> Caché L3: {cpu_resources['CacheL3'][i]}")
print("------------------------------")

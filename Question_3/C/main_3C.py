import pynvml

def gpuMemory():
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)  # Índice 0 para obtener la primera GPU disponible
    info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    gpu_memory = info.free/(1024**3)

    return gpu_memory

# Llamar a la función y mostrar el tamaño de la memoria de la GPU.

gpu_size = gpuMemory()
print("Tamaño de la memoria de la GPU:")
print("-----------------------------")
print(f"Tamaño disponible: {gpu_size:.2f} GB")
print("------------------------------")

import psutil

def diskInfo():
    partitions = psutil.disk_partitions()

    disk_info = []
    for partition in partitions:
        mount_point = partition.mountpoint
        try:
            usage = psutil.disk_usage(mount_point)
            device = partition.device
            fs_type = partition.fstype

            disk_info.append({
                "Mount Point": mount_point,
                "Capacity": usage.total / (1024**3),  # Convertir a GB
                "Format": fs_type
            })
        except PermissionError:
            continue

    return disk_info

def diskSpeed():
    disk_speed = {}
    disk_io = psutil.disk_io_counters(perdisk=True)
    for disk in disk_io:
        read_speed = disk_io[disk].read_bytes / (1024**2)  # Convertir a MB/s
        write_speed = disk_io[disk].write_bytes / (1024**2)  # Convertir a MB/s
        disk_speed[disk] = {
            "Read Speed": read_speed,
            "Write Speed": write_speed
        }

    return disk_speed

# Obtener información del disco
disk_information = diskInfo()
disk_speed = diskSpeed()

# Mostrar información del disco
print("Información del Disco:")
print("----------------------")
for disk in disk_information:
    mount_point = disk["Mount Point"]
    capacity = disk["Capacity"]
    fs_type = disk["Format"]

    print(f"Mount Point: {mount_point}")
    print(f"Capacidad: {capacity:.2f} GB")
    print(f"Formato: {fs_type}")
    if mount_point in disk_speed:
        read_speed = disk_speed[mount_point]["Read Speed"]
        write_speed = disk_speed[mount_point]["Write Speed"]
        print(f"Velocidad de Lectura: {read_speed:.2f} MB/s")
        print(f"Velocidad de Escritura: {write_speed:.2f} MB/s")
    print("------------------------------")

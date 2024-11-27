print("Hecho por: NIETO ALONSO YAREI ALELHÍ Y OLIMAN SORIANO FRANCISCO PAUL")
print("Dada la aplicación básica de un menú (“Celulares”) con la estructura while")

celulares = {
    "472839": {"Modelo": "iPhone 14 Pro", "Procesador": "A16 Bionic", "RAM": "6 GB", "Almacenamiento": "128 GB", "CP": "48 MP", "CF": "12 MP", "Batería": "3200 mAh", "SO": "iOS", "Precio": "$1,099"},
    "935827": {"Modelo": "Galaxy S23 Ultra", "Procesador": "8 Gen 2", "RAM": "8 GB", "Almacenamiento": "256 GB", "CP": "200 MP", "CF": "12 MP", "Batería": "5000 mAh", "SO": "Android", "Precio": "$1,199"},
    "587239": {"Modelo": "Pixel 7 Pro", "Procesador": "Google", "RAM": "12 GB", "Almacenamiento": "128 GB", "CP": "50 MP", "CF": "10.8 MP", "Batería": "4820 mAh", "SO": "Android", "Precio": "$899"},
    "128456": {"Modelo": "Xiaomi 13 Pro", "Procesador": "8 Gen 2", "RAM": "12 GB", "Almacenamiento": "128 GB", "CP": "50 MP", "CF": "16 MP", "Batería": "5000 mAh", "SO": "Android", "Precio": "$699"},
    "394582": {"Modelo": "OnePlus 11", "Procesador": "8 Gen 2", "RAM": "8 GB", "Almacenamiento": "256 GB", "CP": "50 MP", "CF": "32 MP", "Batería": "4600 mAh", "SO": "OxygenOS", "Precio": "$899"},
    "876943": {"Modelo": "Huawei P50", "Procesador": "Kirin", "RAM": "12 GB", "Almacenamiento": "256 GB", "CP": "12 MP", "CF": "16 MP", "Batería": "4100 mAh", "SO": "HarmonyOS", "Precio": "$1,299"},
    "319485": {"Modelo": "Sony Xperia", "Procesador": "Snapdragon", "RAM": "12 GB", "Almacenamiento": "256 GB", "CP": "50 MP", "CF": "12 MP", "Batería": "5000 mAh", "SO": "Android", "Precio": "$1,049"},
    "284791": {"Modelo": "Oppo Find", "Procesador": "Snapdragon", "RAM": "12 GB", "Almacenamiento": "256 GB", "CP": "50 MP", "CF": "13 MP", "Batería": "4700 mAh", "SO": "ColorOS", "Precio": "$1,049"},
    "629548": {"Modelo": "Vivo X80", "Procesador": "Snapdragon", "RAM": "12 GB", "Almacenamiento": "256 GB", "CP": "50 MP", "CF": "12 MP", "Batería": "4700 mAh", "SO": "Android", "Precio": "$899"},
    "745839": {"Modelo": "Motorola Edge 30", "Procesador": "Snapdragon", "RAM": "12 GB", "Almacenamiento": "256 GB", "CP": "200 MP", "CF": "32 MP", "Batería": "4600 mAh", "SO": "Android", "Precio": "$899"}
}

# Contraseña inicial
CONTRASEÑA = "admin123"

# Validar contraseña con while
while True:
    intento = input("Introduce la contraseña: ")
    if intento == CONTRASEÑA:
        print("Contraseña correcta. Accediendo al sistema...")
        break  # Salir del ciclo while si la contraseña es correcta
    else:
        print("Contraseña incorrecta. Inténtalo nuevamente.")

# Funciones del menú
def mostrar_celulares():
    if celulares:
        print("\nLista de Celulares:")
        # Encabezado de la tabla
        encabezado = f"{'Celular':<10}{'Codigo':<10}{'Modelo':<20}{'Procesador':<20}{'RAM':<10}{'Almacenamiento':<15}{'CP':<10}{'CF':<10}{'Batería':<15}{'SO':<10}{'Precio':<10}"
        print(encabezado)
        print("-" * len(encabezado))  # Línea divisoria

        contador = 1  # Contador para numerar los celulares
        for codigo, detalles in celulares.items():
            fila = f"Celular {contador:<4} " \
                   f"{codigo:<10} " \
                   f"{detalles['Modelo']:<20} " \
                   f"{detalles['Procesador']:<20} " \
                   f"{detalles['RAM']:<10} " \
                   f"{detalles['Almacenamiento']:<15} " \
                   f"{detalles['CP']:<10} " \
                   f"{detalles['CF']:<10} " \
                   f"{detalles['Batería']:<15} " \
                   f"{detalles['SO']:<10} " \
                   f"{detalles['Precio']:<10}"
            print(fila)
            contador += 1
    else:
        print("No hay celulares en la base de datos.")

def agregar_celular():
    codigo = input("Código (6 dígitos): ")
    if codigo in celulares:
        print("Este código ya existe.")
    else:
        modelo = input("Modelo: ")
        procesador = input("Procesador: ")
        ram = input("RAM: ")
        almacenamiento = input("Almacenamiento: ")
        cp = input("Cámara Principal (MP): ")
        cf = input("Cámara Frontal (MP): ")
        bateria = input("Batería: ")
        so = input("Sistema Operativo: ")
        precio = input("Precio: ")
        celulares[codigo] = {
            "Modelo": modelo,
            "Procesador": procesador,
            "RAM": ram,
            "Almacenamiento": almacenamiento,
            "CP": cp,
            "CF": cf,
            "Batería": bateria,
            "SO": so,
            "Precio": precio
        }
        print(f"Celular {modelo} agregado con éxito.")

def modificar_celular():
    codigo = input("Código del celular a modificar: ")
    if codigo in celulares:
        modelo = input("Nuevo Modelo: ")
        procesador = input("Nuevo Procesador: ")
        ram = input("Nueva RAM: ")
        almacenamiento = input("Nuevo Almacenamiento: ")
        cp = input("Nueva Cámara Principal (MP): ")
        cf = input("Nueva Cámara Frontal (MP): ")
        bateria = input("Nueva Batería: ")
        so = input("Nuevo Sistema Operativo: ")
        precio = input("Nuevo Precio: ")
        celulares[codigo] = {
            "Modelo": modelo,
            "Procesador": procesador,
            "RAM": ram,
            "Almacenamiento": almacenamiento,
            "CP": cp,
            "CF": cf,
            "Batería": bateria,
            "SO": so,
            "Precio": precio
        }
        print(f"Celular {modelo} modificado con éxito.")
    else:
        print("Código no encontrado.")

def eliminar_celular():
    codigo = input("Código del celular a eliminar: ")
    if codigo in celulares:
        eliminado = celulares.pop(codigo)
        print(f"Celular {eliminado['Modelo']} eliminado con éxito.")
    else:
        print("Código no encontrado.")

# Menú principal
while True:
    print("\nMenú de Celulares")
    print("1. Agregar = Insertar = Alta")
    print("2. Consulta = Mostrar")
    print("3. Modificar = Editar")
    print("4. Eliminar = Borrar")
    print("5. Salir del programa")

    opcion = input("Elige una opción (1/2/3/4/5): ")
    if opcion == "1":
        agregar_celular()
    elif opcion == "2":
        mostrar_celulares()
    elif opcion == "3":
        modificar_celular()
    elif opcion == "4":
        eliminar_celular()
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida.")

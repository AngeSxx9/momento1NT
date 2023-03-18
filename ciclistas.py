# Definir una lista vacía para almacenar los datos de los ciclistas
ciclistas = []

# Función para añadir un ciclista a la lista
def agregar_ciclista():
    # Pedir datos al usuario
    codigo = input("Ingrese el código del ciclista: ")
    nombre = input("Ingrese el nombre del ciclista: ")
    edad = int(input("Ingrese la edad del ciclista: "))
    pais = input("Ingrese el país del ciclista: ")
    equipo = input("Ingrese el equipo del ciclista: ")
    tiempo = int(input("Ingrese el tiempo en minutos de la última prueba de crono individual del ciclista: "))

    # Crear un diccionario con los datos del ciclista y añadirlo a la lista
    ciclistas.append({"codigo": codigo, "nombre": nombre, "edad": edad, "pais": pais, "equipo": equipo, "tiempo": tiempo})

# Función para mostrar la tabla de posiciones
def mostrar_tabla():
    # Ordenar la lista de ciclistas por tiempo
    ciclistas_ordenados = sorted(ciclistas, key=lambda k: k['tiempo'])
    
    # Mostrar la tabla de posiciones
    print("Tabla de posiciones:")
    print("--------------------")
    print("Código  Nombre               País    Equipo  Tiempo")
    print("--------------------------------------------------")
    for i, ciclista in enumerate(ciclistas_ordenados):
        print(f"{ciclista['codigo']}  {ciclista['nombre'].ljust(20)}  {ciclista['pais'].ljust(6)}  {ciclista['equipo'].ljust(6)}  {ciclista['tiempo']}")

# Función para corregir el tiempo de un ciclista
def corregir_tiempo():
    # Pedir el código del ciclista y el nuevo tiempo al usuario
    codigo = input("Ingrese el código del ciclista que desea corregir: ")
    nuevo_tiempo = int(input("Ingrese el nuevo tiempo en minutos para el ciclista: "))
    
    # Buscar el ciclista en la lista y actualizar su tiempo
    for ciclista in ciclistas:
        if ciclista['codigo'] == codigo:
            ciclista['tiempo'] = nuevo_tiempo
            print("El tiempo del ciclista ha sido actualizado.")
            return

    # Si el código no se encuentra en la lista, mostrar un mensaje de error
    print("No se encontró ningún ciclista con ese código.")

# Función para retirar un ciclista de la tabla de posiciones
def retirar_ciclista():
    # Pedir el código del ciclista al usuario
    codigo = input("Ingrese el código del ciclista que desea retirar: ")
    
    # Buscar el ciclista en la lista y retirarlo
    for i, ciclista in enumerate(ciclistas):
        if ciclista['codigo'] == codigo:
            ciclistas.pop(i)
            print("El ciclista ha sido retirado.")
            return

    # Si el código no se encuentra en la lista, mostrar un mensaje de error
    print("No se encontró ningún ciclista con ese código.")

# Función para mostrar el menú y procesar la opción elegida por el usuario
def menu():
    while True:
        print("\nMenu:")
        print("1. Agregar ciclista")
        print("2. Mostrar tabla de posiciones")
        print("3. Corregir tiempo de un ciclista")
        print("4. Retirar un ciclista de la tabla")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_ciclista()
        elif opcion == "2":
            mostrar_tabla()
        elif opcion == "3":
            corregir_tiempo()
        elif opcion == "4":
            retirar_ciclista()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor seleccione otra.")

menu()
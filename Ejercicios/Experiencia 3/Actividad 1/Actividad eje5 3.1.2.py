# Lista de productos con precios
productos = {
    1: {"nombre": "Manzanas", "precio": 1000},
    2: {"nombre": "Pan", "precio": 2000},
    3: {"nombre": "Leche", "precio": 1500},
    4: {"nombre": "Huevos", "precio": 3000},
    5: {"nombre": "Queso", "precio": 2500}
}

# Lista para almacenar el carro de compras
carro_de_compras = []

# Función para agregar productos al carro de compras
def agregar_productos():
    while True:
        print("\nMenú de productos:")
        for key, value in productos.items():
            print(f"{key}. {value['nombre']} - ${value['precio']:.2f}")
        opcion = input("Seleccione un producto por su número (o '0' para regresar al menú principal): ")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 0:
                break
            elif opcion in productos:
                carro_de_compras.append(productos[opcion])
                print(f"{productos[opcion]['nombre']} ha sido agregado al carro de compras.")
            else:
                print("Opción no válida. Intente de nuevo.")
        else:
            print("Entrada no válida. Intente de nuevo.")

# Función para ver la canasta
def ver_canasta():
    if carro_de_compras:
        print("\nProductos en la canasta:")
        for producto in carro_de_compras:
            print(f"{producto['nombre']} - ${producto['precio']:.2f}")
    else:
        print("\nLa canasta está vacía.")

# Función para ver el total a pagar
def ver_total():
    total = sum(producto['precio'] for producto in carro_de_compras)
    print(f"\nEl total a pagar es: ${total:.2f}")

# Función para mostrar el menú
def mostrar_menu():
    while True:
        print("\nMenú principal:")
        print("1. Agregar productos")
        print("2. Ver canasta")
        print("3. Ver total")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_productos()
        elif opcion == "2":
            ver_canasta()
        elif opcion == "3":
            ver_total()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
mostrar_menu()

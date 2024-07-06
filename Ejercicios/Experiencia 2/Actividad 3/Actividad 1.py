def ejecutar():
    # Solicitar la cantidad de pasajes a vender
    try:
        cantidad_pasajes = int(input("Ingresa la cantidad de pasajes a vender: "))
    except ValueError:
        print("Error: Debes ingresar un número entero.")
        return

    totalIngresos = 0

    # Bucle for para iterar sobre la cantidad de pasajes
    for i in range(cantidad_pasajes):
        while True:
            try:
                precio = float(input(f"Ingrese el precio del pasaje {i + 1}: "))
                if precio < 0:
                    raise ValueError("El precio no puede ser negativo.")
                totalIngresos += precio
                break
            except ValueError as e:
                print(f"Entrada inválida: {e}. Por favor, proporciona un valor numérico válido.")
                return

    # Imprimir el total de ingresos por la venta de pasajes
    print(f"\nEl total de ingresos por la venta de pasajes es: $ {totalIngresos}")

ejecutar()

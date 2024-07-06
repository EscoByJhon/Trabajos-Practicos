def pago_tarjeta_de_credito(deuda):
    try:
        monto_pago = float(input("Ingrese el monto a pagar en la tarjeta de crédito: "))
        
        if monto_pago < 0:
            raise ValueError("El monto a pagar no puede ser negativo.")
        
        if monto_pago > deuda:
            print(f"No puedes pagar más de ${deuda}.")
        else:
            deuda -= monto_pago
            print(f"Se ha realizado un pago de ${monto_pago}. Deuda restante: ${deuda}")
        
    except ValueError as e:
        print(f"Error: {e}. Ingresa un monto válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    return deuda

def simulacion_compras(deuda):
    try:
        while True:
            monto_compra = float(input("Ingrese el monto de la compra (o '0' para finalizar): "))
            
            if monto_compra < 0:
                raise ValueError("El monto de la compra no puede ser negativo.")
            
            if monto_compra == 0:
                break
            
            deuda += monto_compra
            print(f"Compra realizada por ${monto_compra}. Deuda actual: ${deuda}")
    
    except ValueError as e:
        print(f"Error: {e}. Ingresa un monto válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    return deuda

def menu():
    deuda = 100000
    
    while True:
        print("\nMenú de opciones:")
        print("1. Pago de Tarjeta de Crédito")
        print("2. Simulación de Compras")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1/2/3): ")
        
        if opcion == '1':
            deuda = pago_tarjeta_de_credito(deuda)
        elif opcion == '2':
            deuda = simulacion_compras(deuda)
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

menu()

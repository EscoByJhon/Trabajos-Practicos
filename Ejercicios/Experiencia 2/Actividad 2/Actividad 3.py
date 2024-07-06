def ejecutar():
    # Captura de errores para valores y división por cero
    try:
        # Solicitar un número
        numero = float(input("Ingresa un número: "))
        
        # Solicitar un divisor
        divisor = float(input("Ingresa un divisor: "))
        
        # Realizar la división
        resultado = numero / divisor
        print(f"El resultado de la división es: {resultado}")

    except ValueError:
        print("Error: Debes ingresar un número válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

ejecutar()

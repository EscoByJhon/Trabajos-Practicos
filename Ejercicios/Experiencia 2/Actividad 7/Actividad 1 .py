def pagar_con_tarjeta():
    try:
        num_tarjeta = input("Ingrese el número de tarjeta de crédito: ")
        nombre_titular = input("Ingrese el nombre del titular: ")
        mes_vencimiento = input("Ingrese el mes de vencimiento (MM): ")
        anio_vencimiento = input("Ingrese el año de vencimiento (YYYY): ")
        
        print("\nPago realizado con tarjeta de crédito:")
        print(f"Número de tarjeta: {num_tarjeta}")
        print(f"Nombre del titular: {nombre_titular}")
        print(f"Fecha de vencimiento: {mes_vencimiento}/{anio_vencimiento}")
        
    except Exception as e:
        print(f"Error al procesar el pago con tarjeta: {e}")

def pagar_con_paypal():
    try:
        usuario_paypal = input("Ingrese el nombre de usuario de PayPal: ")
        contrasena_paypal = input("Ingrese la contraseña de PayPal: ")
        
        print("\nPago realizado con PayPal:")
        print(f"Usuario de PayPal: {usuario_paypal}")
        
    except Exception as e:
        print(f"Error al procesar el pago con PayPal: {e}")

def pagar_con_transferencia():
    try:
        print("\nPago realizado por transferencia electrónica:")
        print("Datos para la transferencia:")
        print("Banco: Banco de Ejemplo")
        print("Cuenta: 123456789")
        print("Código de referencia: TC2024")
        
    except Exception as e:
        print(f"Error al procesar el pago por transferencia: {e}")

def menu_pago_online():
    while True:
        print("\nMétodos de Pago Online - Dulce Capricho")
        print("1) Pagar con tarjeta de crédito")
        print("2) Pagar con PayPal")
        print("3) Pagar por transferencia electrónica")
        print("4) Cancelar")
        print("5) Salir")
        
        opcion = input("Seleccione una opción (1/2/3/4/5): ")
        
        if opcion == '1':
            pagar_con_tarjeta()
        elif opcion == '2':
            pagar_con_paypal()
        elif opcion == '3':
            pagar_con_transferencia()
        elif opcion == '4':
            print("Pago cancelado.")
        elif opcion == '5':
            print("Gracias por visitar Dulce Capricho. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2, 3, 4 o 5.")

# Ejecución del menú de pago online
menu_pago_online()

def ejecutar():
    # Inicialización de variables
    bultos_livianos = 0
    bultos_normales = 0
    costo_liviano = 1000
    costo_normal = 2000

    # Solicitar cantidad de bultos
    try:
        cantidad_bultos = int(input("Ingresa la cantidad de bultos: "))
    except ValueError:
        print("Error: Debes ingresar un número entero.")
        return

    # Procesar cada bulto
    for i in range(cantidad_bultos):
        while True:
            try:
                peso = float(input(f"Ingrese el peso del bulto {i + 1}: "))
                if peso <= 0:
                    raise ValueError("El peso debe ser un número positivo.")
                break
            except ValueError as e:
                print(f"Entrada inválida: {e}")

        # Clasificar y acumular valores y contadores
        if 1 <= peso <= 5:
            bultos_livianos += 1
        elif 6 <= peso <= 10:
            bultos_normales += 1
        else:
            print(f"El peso del bulto {i + 1} no está en el rango permitido (1-10 kg).")

    # Calcular costos
    total_livianos = bultos_livianos * costo_liviano
    total_normales = bultos_normales * costo_normal
    total_pagar = total_livianos + total_normales

    # Imprimir resultados
    print(f"\n{bultos_livianos} bulto(s) liviano(s) $ {total_livianos}")
    print(f"{bultos_normales} bulto(s) normal(es) $ {total_normales}")
    print(f"Valor total a pagar: $ {total_pagar}")

ejecutar()

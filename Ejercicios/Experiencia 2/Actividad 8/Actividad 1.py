import os

def calcular_costo_envio(nombre_cliente, peso, distancia):
    # Validación de datos
    if not nombre_cliente or len(nombre_cliente) > 30:
        raise ValueError("El nombre del cliente no puede estar vacío y debe tener máximo 30 caracteres.")
    
    try:
        peso = float(peso)
        distancia = float(distancia)
    except ValueError:
        raise ValueError("El peso y la distancia deben ser valores numéricos.")

    if peso <= 0 or distancia <= 0:
        raise ValueError("El peso y la distancia deben ser valores numéricos positivos.")

    # Cálculo del costo de envío
    costo_base = 5000
    adicional_peso = peso * 500

    recargo_distancia = 0
    if distancia > 100:
        recargo_distancia = (distancia - 100) * 100

    costo_total = costo_base + adicional_peso + recargo_distancia

    return costo_base, adicional_peso, recargo_distancia, costo_total

def mostrar_desglose(nombre_cliente, peso, distancia, costo_base, adicional_peso, recargo_distancia, costo_total):
    print("\nDesglose del Costo de Envío")
    print(f"Cliente: {nombre_cliente}")
    print(f"Peso del paquete: {peso} kg")
    print(f"Distancia de envío: {distancia} km")
    print(f"Costo base: ${costo_base} CLP")
    print(f"Adicional por peso: ${adicional_peso} CLP")
    if recargo_distancia > 0:
        print(f"Recargo por distancia: ${recargo_distancia} CLP")
    print(f"Costo total de envío: ${costo_total} CLP")

def generar_archivo_envio(nombre_cliente, peso, distancia, costo_total):
    nombre_archivo = f"envio_{nombre_cliente.replace(' ', '_')}.txt"
    contenido = f"Cliente: {nombre_cliente}\n"
    contenido += f"Peso del paquete: {peso} kg\n"
    contenido += f"Distancia de envío: {distancia} km\n"
    contenido += f"Costo total de envío: ${costo_total} CLP\n"

    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)
        print(f"\nArchivo '{nombre_archivo}' generado exitosamente.")
    except Exception as e:
        print(f"Error al generar el archivo: {e}")

# Ejemplo de uso de las funciones
nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
peso = input("Ingrese el peso del paquete en kilogramos: ").strip()
distancia = input("Ingrese la distancia de envío en kilómetros: ").strip()

try:
    costo_base, adicional_peso, recargo_distancia, costo_total = calcular_costo_envio(nombre_cliente, peso, distancia)
    mostrar_desglose(nombre_cliente, peso, distancia, costo_base, adicional_peso, recargo_distancia, costo_total)
    generar_archivo_envio(nombre_cliente, peso, distancia, costo_total)
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Error inesperado: {e}")

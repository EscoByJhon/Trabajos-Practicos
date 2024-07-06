# Crear el arreglo 10x4 para simular un bus
filas = 10
columnas = 4
bus = [[0 for _ in range(columnas)] for _ in range(filas)]

# Asignar los números de asiento automáticamente
asiento = 1
for i in range(filas):
    for j in range(columnas):
        bus[i][j] = asiento
        asiento += 1

# Mostrar los números de asiento por pantalla
print("Asientos del bus:")
for fila in bus:
    for asiento in fila:
        print(asiento, end=" ")
    print()  # Imprimir nueva línea después de cada fila

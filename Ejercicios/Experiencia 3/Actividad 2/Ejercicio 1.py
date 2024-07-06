# Crear el arreglo 3x4
filas = 3
columnas = 4
matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

# Ingresar elementos numéricos por pantalla
print("Ingrese los elementos de la matriz 3x4:")
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = int(input(f"Ingrese el elemento en la posición [{i}][{j}]: "))

# Mostrar los elementos de la matriz de forma ordenada
print("\nMatriz 3x4:")
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end=" ")
    print()  # Imprimir nueva línea después de cada fila

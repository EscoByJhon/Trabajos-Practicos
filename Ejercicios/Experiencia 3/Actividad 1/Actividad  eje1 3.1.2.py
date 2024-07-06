# Solicitar los tres nombres
nombres = []
for i in range(3):
    nombre = input(f"Ingrese el nombre {i + 1}: ")
    nombres.append(nombre)

# Encontrar el nombre con la mayor cantidad de caracteres
nombre_mas_largo = max(nombres, key=len)

# Mostrar el nombre con la mayor cantidad de caracteres
print(f"El nombre con la mayor cantidad de caracteres es: {nombre_mas_largo}")

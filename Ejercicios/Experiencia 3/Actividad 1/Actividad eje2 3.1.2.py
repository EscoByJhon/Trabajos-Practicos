# Solicitar los tres nombres
nombres = []
for i in range(3):
    nombre = input(f"Ingrese el nombre {i + 1}: ")
    nombres.append(nombre)

# Solicitar los tres apellidos
apellidos = []
for i in range(3):
    apellido = input(f"Ingrese el apellido {i + 1}: ")
    apellidos.append(apellido)

# Ordenar las listas de nombres y apellidos
nombres_ordenados = sorted(nombres)
apellidos_ordenados = sorted(apellidos)

# Mostrar los nombres y apellidos ordenados
print("\nNombres ordenados:")
for nombre in nombres_ordenados:
    print(nombre)

print("\nApellidos ordenados:")
for apellido in apellidos_ordenados:
    print(apellido)

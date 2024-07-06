# Crear el arreglo 3x3x3 manualmente
arreglo = [
    [
        ["amarillo", "rojo", "Naranja"],
        ["Verde", "Blanco", "amarillo"],
        ["rojo", "Naranja", "Verde"]
    ],
    [
        ["Blanco", "Verde", "amarillo"],
        ["rojo", "Naranja", "Blanco"],
        ["amarillo", "Verde", "rojo"]
    ],
    [
        ["Naranja", "Blanco", "Verde"],
        ["rojo", "amarillo", "Naranja"],
        ["Blanco", "Verde", "amarillo"]
    ]
]

# Inicializar contadores para cada color
conteo_colores = {
    "amarillo": 0,
    "rojo": 0,
    "Naranja": 0,
    "Verde": 0,
    "Blanco": 0
}

# Contar los elementos de cada color
for i in range(3):
    for j in range(3):
        for k in range(3):
            color = arreglo[i][j][k]
            if color in conteo_colores:
                conteo_colores[color] += 1

# Mostrar la información
print("Número de elementos de cada color:")
for color, conteo in conteo_colores.items():
    print(f"{color}: {conteo}")

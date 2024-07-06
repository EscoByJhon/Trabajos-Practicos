def agregar_nombres():
    nombres = []
    while True:
        nombre = input("Ingrese un nombre: ")
        nombres.append(nombre)
        respuesta = input("¿Desea agregar otro nombre? (sí/no): ").strip().lower()
        if respuesta == "no":
            break
    return nombres

def eliminar_nombre_mas_corto(nombres):
    nombre_mas_corto = min(nombres, key=len)
    nombres.remove(nombre_mas_corto)
    return nombre_mas_corto

# Agregar nombres a la lista
nombres = agregar_nombres()

# Eliminar el nombre con la menor cantidad de caracteres
nombre_eliminado = eliminar_nombre_mas_corto(nombres)

# Mostrar resultados
print(f"\nNombre eliminado (con la menor cantidad de caracteres): {nombre_eliminado}")
print("Lista de nombres actualizada:")
for nombre in nombres:
    print(nombre)

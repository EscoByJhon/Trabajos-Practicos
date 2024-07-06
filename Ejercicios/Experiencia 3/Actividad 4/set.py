texto = input("Por favor, ingresa un texto: ")

texto = texto.lower()

palabras = texto.split()

frecuencia_palabras = {}

for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1


print("\nFrecuencia de palabras:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"{palabra}: {frecuencia}")

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

inicio_rango = int(input("Ingresa el número de inicio del rango: "))
fin_rango = int(input("Ingresa el número de fin del rango: "))

conjunto_primos = set()

for numero in range(inicio_rango, fin_rango + 1):
    if es_primo(numero):
        conjunto_primos.add(numero)

print("\nNúmeros primos en el rango de", inicio_rango, "a", fin_rango, ":")
print(conjunto_primos)

lista_nombres_edades = []

while True:
    nombre = input("Ingresa un nombre (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    edad = int(input("Ingresa la edad: "))
    lista_nombres_edades.append((nombre, edad))

edades_unicas = set()

for _, edad in lista_nombres_edades:
    edades_unicas.add(edad)

print("\nLista de nombres y edades:")
for nombre, edad in lista_nombres_edades:
    print(f"Nombre: {nombre}, Edad: {edad}")

print("\nEdades únicas:")
print(edades_unicas)

informacion = ("Jhon", 24, "PuertoMontt")

print("Nombre:", informacion[0])
print("Edad:", informacion[1])
print("Ciudad:", informacion[2])

nombre, edad, ciudad = informacion
print("\nDesempaquetado:")
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)
print()


numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

suma = sum(numeros)
print("Suma de los elementos de la tupla:", suma)

maximo = max(numeros)
minimo = min(numeros)
print("Valor máximo en la tupla:", maximo)
print("Valor mínimo en la tupla:", minimo)

conteo_cinco = numeros.count(5)
print("El número 5 aparece", conteo_cinco, "veces en la tupla.")
print()

letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')

primeras_5_letras = letras[:5]
print("Primeras 5 letras:", primeras_5_letras)

ultimas_3_letras = letras[-3:]
print("Últimas 3 letras:", ultimas_3_letras)

cada_segunda_letra = letras[::2]
print("Cada segunda letra:", cada_segunda_letra)



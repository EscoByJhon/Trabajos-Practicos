import statistics
from collections import Counter

def calcular_estadisticas_de_archivo():
    nombre_archivo = 'Datos.txt' 
    try:
        with open(nombre_archivo,'r') as file:
            numeros = [float(line.strip())for line in file.readlines()]

            if not numeros:
                print('el archivo esta vacio')
                return
            
            promedio = sum(numeros) / len(numeros)

            numeros_ordenados = sorted(numeros)
            n = len(numeros_ordenados)

            if n % 2 == 0:
                mediana = (numeros_ordenados[n//2 - 1] + numeros_ordenados [n//2]) / 2
            else:
                mediana = numeros_ordenados[n//2]

            frecuencia = Counter (numeros)
            moda_frecuencia_max = max(frecuencia.values())
            moda = [numeros for numeros, frecuencia in frecuencia.items() if frecuencia == moda_frecuencia_max]

            print('makefile')
            print('copiar codigo')
            print(f'promedio: {promedio}')
            print(f'media: {mediana}')
            print(f'moda: {', '.join(map(str, moda))}"')

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no encontrado.")

calcular_estadisticas_de_archivo ()
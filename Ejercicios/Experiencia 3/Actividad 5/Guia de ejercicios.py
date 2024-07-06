import csv
import json


mayores = []


with open('datos.csv', mode='r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    
   
    for fila in lector_csv:
        nombre = fila['Nombre']
        edad = int(fila['Edad'])
        comuna = fila['Comuna']
        
        
        if edad >= 18:
            estado_edad = 'Mayor de edad'
        else:
            estado_edad = 'Menor de edad'
        
        # Imprimimos la información en la consola
        print(f"Nombre: {nombre}, Edad: {edad}, Estado: {estado_edad}, Comuna: {comuna}")
        
    
        if edad >= 25:
            mayores.append({'Nombre': nombre, 'Edad': edad, 'Comuna': comuna})


with open('mayores.json', mode='w') as archivo_json:
    json.dump(mayores, archivo_json, indent=4)

print("Archivo 'mayores.json' creado con éxito.")

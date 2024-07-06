import csv
import json

ganadores = []

with open('listadoRun.csv', mode='r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)  
    
    for fila in lector_csv:
        run, nombre = fila
        
        run_sin_dv = run.split('-')[0]
        ultimos_dos_digitos = run_sin_dv[-2:]
        
        if ultimos_dos_digitos in ['92', '95', '84']:
            ganadores.append({'run': run, 'nombre': nombre})

with open('ganadores.json', mode='w') as archivo_json:
    json.dump(ganadores, archivo_json, indent=4)

print("Archivo 'ganadores.json' creado con éxito.")

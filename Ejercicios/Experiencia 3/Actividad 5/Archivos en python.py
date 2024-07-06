import csv
import json

def clasificar_empresa(ventas):
    if ventas <= 100000000:
        return "Pequeño Contribuyente"
    elif 100000001 <= ventas <= 200000000:
        return "Mediano Contribuyente"
    else:
        return "Gran Contribuyente"

def cargar_datos(nombre_archivo):
    empresas = []
    with open(nombre_archivo, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            empresa = {
                "rut": row["rut"],
                "nombre": row["nombre"],
                "ventas": int(row["ventas"]),
                "clasificacionEmpresa": clasificar_empresa(int(row["ventas"]))
            }
            empresas.append(empresa)
    return empresas

def guardar_datos(empresas, nombre_archivo):
    with open(nombre_archivo, 'w') as jsonfile:
        json.dump(empresas, jsonfile, indent=4)

if __name__ == "__main__":
    nombre_archivo_csv = "listadoRutEmpresa.csv"
    nombre_archivo_json = "segmentacionEmpresas.json"
    
    # Cargar datos desde el archivo CSV
    empresas = cargar_datos(nombre_archivo_csv)
    
    # Guardar datos en el archivo JSON
    guardar_datos(empresas, nombre_archivo_json)
    
    print(f"Datos guardados en {nombre_archivo_json}")

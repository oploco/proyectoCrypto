import requests
import csv
from pathlib import Path

def obtener_datos_desde_api():
    url_api = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    respuesta = requests.get(url_api)
    datos_json = respuesta.json()
    return datos_json

def guardar_en_csv(datos, nombre_archivo):
    with open(nombre_archivo, 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        # Escribe las cabeceras si es necesario
        # escritor_csv.writerow(['columna1', 'columna2', ...])
        for fila in datos:
            escritor_csv.writerow(fila.values()) # Suponiendo que los datos son un diccionario

def guardar_en_csv2(datos, nombre_archivo):
    
        fileName = nombre_archivo
        fileObj = Path(fileName)
        if(fileObj.is_file()):
            print("existe")
            precios = [crypto['current_price'] for crypto in datos]
            fechault= [crypto['last_updated'] for crypto in datos]

            with open(nombre_archivo, 'a', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv) 
                escritor_csv.writerow(precios)
                escritor_csv.writerow(fechault)
        else:
            with open(nombre_archivo, 'a', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv) 
                nombres = [crypto['name'] for crypto in datos]
                escritor_csv.writerow(nombres)

def guardar_en_csv_Bitcoin(datos, nombre_archivo):
    
        fileName = nombre_archivo
        fileObj = Path(fileName)
        if(fileObj.is_file()):
            print("existe")
            precio = [datos['current_price'] ]
            fechault= [datos['last_updated'] ]

            lectura=[datos['current_price'] ,datos['last_updated'] ]
            
            with open(nombre_archivo, 'a', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv) 
                escritor_csv.writerow(lectura)             
        else:
            with open(nombre_archivo, 'a', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv) 
                escritor_csv.writerow(['Precio','fecha'])

if __name__ == "__main__":
    datos_desde_api = obtener_datos_desde_api()
    nombre_archivo_csv = "datos_desde_api.csv"
    nombre_archivo_csv2 = "datos_desde_api2.csv"
    nombre_archivo_csv_Bitcoin = "bitcoin.csv"
    guardar_en_csv(datos_desde_api[:12], nombre_archivo_csv)
    guardar_en_csv2(datos_desde_api[:12], nombre_archivo_csv2)
    guardar_en_csv_Bitcoin(datos_desde_api[id=='Bitcoin'], nombre_archivo_csv_Bitcoin)
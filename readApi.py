import requests
import matplotlib.pyplot as plt
import csv

def obtener_datos_api():
    url_api = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    respuesta = requests.get(url_api)
    datos_json = respuesta.json()
    return datos_json

def guardar_en_csv(datos, nombre_archivo):
    print('en guardar            ')
    
    with open(nombre_archivo, 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        # Escribe las cabeceras si es necesario
        # escritor_csv.writerow(['columna1', 'columna2', ...])
        for fila in datos:
            escritor_csv.writerow(fila.values()) # Suponiendo que los datos son un diccionario

def crear_grafico(datos):    
    nombres = [crypto['name'] for crypto in datos]
    precios = [crypto['current_price'] for crypto in datos]
    fechault= [crypto['last_updated'] for crypto in datos]

    print(nombres,precios,fechault)

    plt.figure(figsize=(10, 6))
    plt.barh(nombres, precios, color='skyblue')
    plt.xlabel('Precio (USD)')
    plt.title('Precios de criptomonedas en USD')
    plt.gca().invert_yaxis() # Invertir el eje y para que la criptomoneda con el precio más alto esté arriba
    plt.tight_layout()

    # Guardar el gráfico como imagen
    plt.savefig('grafico_criptomonedas.png')

    
if __name__ == "__main__":
    datos_api = obtener_datos_api()
    print(datos_api[id=='Bitcoin'])
    nombre_archivo_csv = "datos_desde_api.csv"    
    guardar_en_csv(datos_api, nombre_archivo_csv)
    crear_grafico(datos_api[:10]) # Mostrar solo los primeros 10 resultados por simplicidad
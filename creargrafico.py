import matplotlib.pyplot as plt
import pandas as pd
from datetime import date
from datetime import datetime

DATA_FILENAME = "FilesCryptos/bitcoin.csv"
CRYPTOS = ['Bitcoin','Ethereum','Tether','BNB','Solana','XRP','Lido Staked Ether','USDC','Dogecoin','Cardano','Avalanche','Shiba Inu']

def crear_grafico(moneda):    
    nombre_archivo_csv = "FilesCryptos/" + moneda + ".csv"

    df = pd.read_csv(nombre_archivo_csv,
                     parse_dates=['fecha'],                     
                     usecols=['fecha','Precio'])
    
    print(df)

    df.head()
    df.set_index(df['fecha'])
    
    # Crear una figura con un tamaño específico
    fig, ax = plt.subplots(figsize=(10, 6),facecolor='#eafff3')

    # Graficar los datos
    ax.plot(df['fecha'], df['Precio'], color='orange')
    ax.set_facecolor('#eafff5') 

    # Etiquetas de los ejes x e y
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Precio (USD)')

    # Escala lineal en el eje y
    ax.set_yscale('linear')

    # Título del gráfico
    ax.set_title(f'Precios de {moneda} en USD ({datetime.now().strftime("%H:%M")})')

    # Ajustar el diseño para evitar cortar las etiquetas
    plt.tight_layout()

    # Añadir leyenda
    ax.legend([moneda], loc='upper left', fontsize=10)

    # Añadir una cuadrícula de fondo para hacer más fácil la lectura de los valores exactos
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    ax.yaxis.set_major_locator(plt.MaxNLocator(5))
    
    #plt.setp(plt.xlabel, rotation=45, horizontalalignment='right') 

    # Guardar el gráfico como imagen
    plt.savefig("./crypto/coin/static/graphs/" + moneda + ".png")
    
if __name__ == "__main__":
    for crypto in CRYPTOS:         
        crear_grafico(crypto)
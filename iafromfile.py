
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Obtener datos de precios de criptomonedas (por ejemplo, Bitcoin)
# Supongamos que tienes un archivo CSV llamado "datos_cripto.csv" con columnas "fecha" y "precio"
datos_cripto = pd.read_csv("bitcoin.csv")

# Preprocesar datos
datos_cripto['fecha'] = pd.to_datetime(datos_cripto['fecha'])
datos_cripto.set_index('fecha', inplace=True)

# Crear características y objetivo
datos_cripto['precio_futuro'] = datos_cripto['Precio'].shift(-1) # Desplazar los precios hacia arriba para obtener el objetivo
X = datos_cripto.drop(columns=['precio_futuro'])
y = datos_cripto['precio_futuro'].fillna(value=70227, limit=1)

y.fillna(value=70227, limit=1)

# Dividir datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
print(y)


# Entrenar modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predecir precios futuros
predicciones_train = modelo.predict(X_train)
predicciones_test = modelo.predict(X_test)

# Calcular métricas de rendimiento
mse_train = mean_squared_error(y_train, predicciones_train)
mse_test = mean_squared_error(y_test, predicciones_test)
print("Error cuadrático medio (MSE) en conjunto de entrenamiento:", mse_train)
print("Error cuadrático medio (MSE) en conjunto de prueba:", mse_test)

# Visualizar resultados
plt.figure(figsize=(10, 6))
plt.plot(datos_cripto.index, datos_cripto['Precio'], label='Precio Real')
plt.plot(X_train.index, predicciones_train, label='Predicciones en Conjunto de Entrenamiento')
plt.plot(X_test.index, predicciones_test, label='Predicciones en Conjunto de Prueba')
plt.xlabel('Fecha')
plt.ylabel('Precio')
plt.title('Predicción de Precios de Criptomonedas')
plt.legend()
plt.show()

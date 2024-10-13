from collections import Counter
import matplotlib.pyplot as plot

"""
Aquí colocas tu texto para análisis. Este texto se utilizará para determinar las palabras más comunes.
"""

texto = "comer comer comer comida en el mundo de las gomitas"

# Preprocesar el texto
palabras = texto.lower().split()
conteo_palabras = Counter(palabras)

# Obtener las 10 palabras más comunes
palabras_comunes = conteo_palabras.most_common(10)

# Separar las palabras y las frecuencias para la gráfica
etiquetas, valores = zip(*palabras_comunes)

# Crear la gráfica de barras
plot.bar(etiquetas, valores)
plot.xlabel('Palabras')
plot.ylabel('Frecuencia')
plot.title('10 palabras más comunes')
plot.show()

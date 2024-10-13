"""
Vas a simular una carrera de autos. Cada auto tiene una
velocidad aleatoria (puedes usar la biblioteca random de
Python) y cada ciclo del bucle representa un segundo de la
carrera. Al final de cada segundo, cada auto avanza una
distancia igual a su velocidad. La carrera dura 10 segundos.
Al final de la carrera, debes imprimir el auto ganador.
Si hay un empate, debes imprimir todos los autos que empataron.

Nota: Este desafío puede requerir que aprendas sobre conceptos
adicionales, por ejemplo cómo generar números aleatorios.
"""

import os
import time
import random

def limpiar_pantalla():
    # Limpiar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

# Definir el número de autos
num_autos = 5

# Generar velocidades aleatorias para cada auto (por ejemplo entre 1 y 20 unidades por segundo)
velocidades = [random.randint(1, 3) for _ in range(num_autos)]

# Inicializar las distancias recorridas por cada auto
distancias = [0] * num_autos

# Simular la carrera por 10 segundos
for segundo in range(10):
    print(f"Vuelta {segundo + 1}:")
    for i in range(num_autos):
        distancias[i] += velocidades[i]
        
        # Se muestra la distancia recorrida de cada auto usando "*"
        print(f"Auto {i+1}: " + "🔥" * (distancias[i]) + " 🚗")
    print("\n")

    time.sleep(1)
    limpiar_pantalla()
    
# Encontrar la distancia máxima recorrida
distancia_maxima = max(distancias)

# Encontrar todos los autos que han recorrido la distancia máxima
ganadores = [i for i, distancia in enumerate(distancias) if distancia == distancia_maxima]

# Imprimir los resultados
for i in range(num_autos):
    print(f"Auto {i+1}: Velocidad = {velocidades[i]}, Distancia recorrida = {distancias[i]}" + " 🚗")

# Imprimir el ganador o los ganadores
if len(ganadores) == 1:
    print(f"\nEl auto ganador es el Auto {ganadores[0]+1}" + " 🏆")
else:
    print("\nHay un empate entre los autos:", ', '.join(f"Auto {ganador+1} 🏆" for ganador in ganadores))
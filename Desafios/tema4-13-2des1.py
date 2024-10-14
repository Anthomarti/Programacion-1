"""
# Titulo: Desafío 1 Polimorfismo
# Autor: Anthony Martinelli
# Fecha: 14/10/2024
# Descripción:
# Crea una clase Musico que tenga un método instrumento y crea dos subclases Guitarrista y Baterista
# que sobrescriban el método instrumento. Instancia objetos de estas clases y demuestra el polimorfismo.
"""

# Definimos la clase base Musico
class Musico:
    def __init__(self, nombre):
        self.nombre = nombre

    def instrumento(self):
        return f"\n{self.nombre} toca algún instrumento (esperando más información)"


# Creamos una subclase Guitarrista que hereda de Musico
class Guitarrista(Musico):
    def __init__(self, nombre, estilo):
        super().__init__(nombre)
        self.estilo = estilo

    def instrumento(self):
        return f"\n{self.nombre} toca la guitarra con estilo {self.estilo}"


# Creamos una subclase Baterista que hereda de Musico
class Baterista(Musico):
    def __init__(self, nombre, tecnica):
        super().__init__(nombre)
        self.tecnica = tecnica

    def instrumento(self):
        return f"\n{self.nombre} toca la batería con técnica {self.tecnica}"


# Instanciamos objetos de las clases Guitarrista y Baterista
guitarrista = Guitarrista("Jimi Hendrix", "Rock")
baterista = Baterista("John Bonham", "Hard Rock")
musico = Musico("Musico desconocido")

# Creamos una lista de músicos
musicos = [guitarrista, baterista, musico]

# Llamamos al método instrumento de cada músico en la lista
for musico in musicos:
    print(musico.instrumento())
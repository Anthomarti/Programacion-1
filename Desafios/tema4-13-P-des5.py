"""
# Titulo: Desafío 5 Polimorfismo
# Autor: Anthony Martinelli
# Fecha: 14/10/2024
# Descripción:
# En este desafío, aplicarás el polimorfismo para realizar diferentes operaciones matemáticas.
# Deberás crear una clase base Operacion con un método resultado y dos subclases Suma y Multiplicacion
# que sobrescriban este método para realizar las operaciones correspondientes.
"""

# Definimos la clase base Operacion
class Operacion:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def resultado(self):
        return "La operación no está definida"


# Creamos una subclase Suma que hereda de Operacion
class Suma(Operacion):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def resultado(self):
        return self.num1 + self.num2


# Creamos una subclase Multiplicacion que hereda de Operacion
class Multiplicacion(Operacion):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def resultado(self):
        return self.num1 * self.num2


# Función para realizar una operación
def realizar_operacion(operacion: Operacion):
    return operacion.resultado()


# Instanciamos objetos de las subclases
suma = Suma(5, 7)
multiplicacion = Multiplicacion(4, 2)

# Realizamos las operaciones
print(f"Resultado de la suma: {realizar_operacion(suma)}")
print(f"Resultado de la multiplicación: {realizar_operacion(multiplicacion)}")
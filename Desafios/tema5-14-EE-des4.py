"""
# Titulo: Desafío 4 Excepciones y errores
# Autor: Anthony Martinelli
# Fecha: 05/11/2024
# Descripción:
# Crea una excepción personalizada llamada NegativeNumberError
# que se dispare si el usuario intenta ingresar un número
# negativo en un programa de cálculo de raíces cuadradas.
# Implementa el manejo de esta excepción en el programa.
"""

# Define la excepción personalizada
class NegativeNumberError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def raiz_cuadrada(numero):
    try:
        # Verifica si el número es negativo
        if numero < 0:
            raise NegativeNumberError("No se puede calcular la raíz cuadrada de un número negativo.")
        
        # Calcula la raíz cuadrada
        resultado = numero ** 0.5
        return resultado
    
    except NegativeNumberError as error:
        print(f"Error: {error}")
        return None
    except TypeError as error:
        print(f"Error: {error}")
        return None

def main():
    while True:
        try:
            numero = float(input("Ingrese un número: "))
            break
        except ValueError:
            print("Error: El número debe ser un valor numérico.")
    
    resultado = raiz_cuadrada(numero)
    if resultado is not None:
        print(f"La raíz cuadrada de {numero} es: {resultado}")

if __name__ == "__main__":
    main()